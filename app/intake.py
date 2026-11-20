"""
intake.py - one conversation turn during fact-gathering.

Each turn = TWO small, focused model calls (F25: one call doing both jobs dropped facts):
  call 1 EXTRACT : messy story (any language) -> facts as JSON. Nothing else.
  code           : merge facts safely, decide WHICH question comes next
  call 2 PHRASE  : acknowledge + ask exactly that question, in the user's language
  code           : check the reply really asks it; otherwise use the exact intake.yaml question
The model is never asked for legal advice in this stage.
"""
import json
import re
from datetime import date

from app import llm
from app.case_file import load_intake, merge, next_field, UNKNOWN
from app.kb import load_calculators

DONT_KNOW = re.compile(r"pata nahi|nahi pata|maloom nahi|malum nahi|yaad nahi|don'?t know|not sure|no idea|"
                       r"don'?t remember|पता नहीं|मालूम नहीं|याद नहीं", re.IGNORECASE)

EXTRACT_PROMPT = """You extract facts from a person's description of a consumer/legal problem in India.
Today's date is {today}.

Fields (key [type]: what it means):
{field_list}

Rules:
1. Extract EVERY field the user actually stated in the USER MESSAGE - read it carefully, including
   facts mentioned in passing (e.g. "flipkart se redmi phone liya" gives seller AND product).
2. Never guess or assume. The example items written inside the field descriptions are NOT facts about
   this user - never copy them. If a fact was not said, leave the key out.
3. If the user says they don't know a fact, set it to "{unknown}".
4. Dates -> YYYY-MM-DD (month/year only -> 1st of month). Resolve "last week", "2 mahine pehle" from today.
5. If the question says "(You mentioned: X - is that right?)" and the user agrees ("haan", "yes", "sahi"),
   extract X for that field; if they correct it, extract their corrected value.
5b. Money -> plain number in rupees ("15k" = 15000, "1.2 lakh" = 120000).
6. yesno -> true/false.  list -> JSON list of short strings.
7. "language": "en", "hi" (Devanagari) or "hinglish" (Hindi in Latin script).

Respond with ONLY JSON: {{"extracted": {{<key>: <value>, ...}}, "language": "en|hi|hinglish"}}"""

PHRASE_PROMPT = """You are a kind, neutral assistant helping an ordinary person in India describe a legal problem.
Write ONE short reply in the user's language ({language}) and style:
- one short sentence acknowledging what they just said (no judging who is right or wrong,
  no "that's unfair" / "galat baat hai", no legal advice, no predictions), then
  Do NOT restate numbers, dates, durations or amounts in the acknowledgement (the case file shows them).
- then ask this question, word for word, and nothing else: {question}
If the question is NONE, thank them and say you now have the key facts of their case.

Respond with ONLY JSON: {{"reply": "<text>", "asked_field": "{key}"}}"""


YES = {"true", "yes", "y", "haan", "han", "ha", "ji", "हाँ", "हां", "online", "ऑनलाइन"}
NO = {"false", "no", "n", "nahi", "nahin", "na", "नहीं", "offline"}


def coerce_types(extracted: dict, intake: dict) -> dict:
    """Make the model's values match each field's type (F58). Unconvertible values are dropped, not guessed."""
    types = {f["key"]: f["type"] for f in intake["fields"]}
    out = {}
    for k, v in extracted.items():
        t = types.get(k)
        if v == UNKNOWN or t is None:
            out[k] = v
        elif t == "yesno":
            if isinstance(v, bool):
                out[k] = v
            elif str(v).strip().lower() in YES:
                out[k] = True
            elif str(v).strip().lower() in NO:
                out[k] = False
        elif t == "money":
            if isinstance(v, (int, float)) and not isinstance(v, bool):
                out[k] = v
            else:
                digits = re.sub(r"[^\d.]", "", str(v))
                if digits.replace(".", "", 1).isdigit():
                    out[k] = float(digits) if "." in digits else int(digits)
        elif t == "list":
            out[k] = v if isinstance(v, list) else [x.strip() for x in str(v).split(",") if x.strip()]
        else:
            out[k] = v if isinstance(v, str) else str(v)
    return out


def _field_list(intake: dict) -> str:
    lines = []
    for f in intake["fields"]:
        hint = f" ({f['hint']})" if f.get("hint") else ""
        lines.append(f"- {f['key']} [{f['type']}]: {f['question']}{hint}")
    return "\n".join(lines)


def _question(field: dict, language: str | None, case: dict | None = None) -> str:
    """The question in the user's language, from intake.yaml - chosen by code, not translated by the model (F27).
    If the user already mentioned this fact earlier, the question becomes a confirmation (F36)."""
    if language == "hinglish" and field.get("question_hinglish"):
        q = field["question_hinglish"]
    elif language == "hi" and field.get("question_hi"):
        q = field["question_hi"]
    else:
        q = field["question"]
    suggested = (case or {}).get("suggested", {})
    # F39: "Was it a home? (You mentioned: no - is that right?)" -> "No" is ambiguous. Yes/no questions are
    # quick to answer, so they are asked plainly, never as a confirmation.
    if field["key"] in suggested and field.get("type") != "yesno":
        v = suggested[field["key"]]
        shown = ", ".join(map(str, v)) if isinstance(v, list) else \
            ({"hinglish": "haan", "hi": "हाँ"}.get(language, "yes") if v is True else
             {"hinglish": "nahi", "hi": "नहीं"}.get(language, "no") if v is False else str(v))
        confirm = {"hinglish": f" (Aapne bataya: {shown} - sahi hai?)",
                   "hi": f" (आपने बताया: {shown} - क्या यह सही है?)"}.get(language, f" (You mentioned: {shown} - is that right?)")
        q = q + confirm
    return q


def _plain_reply(field: dict | None, language: str | None = None, case: dict | None = None) -> str:
    """Safe fallback: the exact question from intake.yaml, in the user's language."""
    thanks = {"hinglish": "Shukriya, maine note kar liya.", "hi": "धन्यवाद, मैंने नोट कर लिया।"}.get(language, "Thanks, I've noted that.")
    if field is None:
        done = {"hinglish": "Shukriya - ab mere paas aapke case ki zaroori jaankari hai.",
                "hi": "धन्यवाद - अब मेरे पास आपके मामले की ज़रूरी जानकारी है।"}
        return done.get(language, "Thanks - I now have the key facts of your case.")
    return thanks + " " + _question(field, language, case)


def extract(case: dict, history: list[dict], user_message: str, asked: dict | None) -> dict:
    """Call 1: facts only."""
    intake = load_intake(case["pack"])
    system = EXTRACT_PROMPT.format(today=date.today().isoformat(),
                                   field_list=_field_list(intake), unknown=UNKNOWN)
    last_q = _question(asked, "en", case) if asked else "(opening message)"   # includes "(You mentioned: X ...)"
    messages = [{"role": "system", "content": system}]
    messages += history[-4:]                              # a little context, cost stays flat
    messages.append({"role": "user", "content":
        f"QUESTION THE USER IS ANSWERING: {last_q}\nUSER MESSAGE: {user_message}"})
    return llm.chat_json(messages)


def phrase(case: dict, user_message: str, field: dict | None) -> str:
    """Call 2: a friendly reply that asks exactly `field`'s question. Verified by code."""
    lang = case.get("language") or "en"
    key = field["key"] if field else "NONE"
    question = _question(field, lang, case) if field else "NONE"
    system = PHRASE_PROMPT.format(language=lang, question=question, key=key)
    try:
        out = llm.chat_json([{"role": "system", "content": system},
                             {"role": "user", "content": user_message}])
        reply = (out.get("reply") or "").strip()
    except Exception as err:                              # F18: never lose the turn
        print(f"[intake] phrase call failed, using plain question: {err}")
        return _plain_reply(field, lang, case)
    if not reply or out.get("asked_field") != key:
        print(f"[intake] phrase reply unusable (asked {out.get('asked_field')!r}, wanted {key!r})")
        return _plain_reply(field, lang, case)
    from app.validator import LEGAL_PATTERNS, CASE_SENSITIVE, PROMISE_PATTERNS
    if any(re.search(p, reply, 0 if p in CASE_SENSITIVE else re.IGNORECASE) for p in LEGAL_PATTERNS + PROMISE_PATTERNS):
        # F41: the friendly acknowledgement echoed "section 420B" - acknowledgements may not mention any
        # law, section or promise. Use the plain question instead.
        print("[intake] acknowledgement mentioned a law/promise -> plain question")
        return _plain_reply(field, lang, case)
    if field is not None and "?" not in reply:            # F24: must actually ask
        reply += " " + question
    return reply


def run_turn(case: dict, history: list[dict], user_message: str) -> dict:
    """Process one user message. Updates `case` in place.
    Returns {"reply": str, "changed": [keys], "done": bool, "asked": key|None}."""
    intake = load_intake(case["pack"])
    # The question this message is answering. The opening story answers NO question (the bot only said
    # "tell me what happened"), so ask_explicitly facts in it become suggestions to confirm (F36).
    opening = not any(m.get("role") == "user" for m in history)
    asked = None if opening else next_field(case, intake)

    # F46: "pata nahi" / "I don't know" to a question is recorded by CODE (the model once attached it to the
    # wrong field and the bot asked the same question 3 times).
    if asked and DONT_KNOW.search(user_message) and len(user_message.split()) <= 6:
        merge(case, {asked["key"]: UNKNOWN}, asked_key=asked["key"])
    result = extract(case, history, user_message, asked)
    # F58: different models format values differently (Groq returned yes/no as text, numbers as strings).
    # Code converts every extracted value to its field's type before it enters the case file.
    result["extracted"] = coerce_types(result.get("extracted") or {}, intake)
    explicit = {f["key"] for f in intake["fields"] if f.get("ask_explicitly")}
    changed = merge(case, result.get("extracted", {}), explicit_only=explicit,
                    asked_key=asked["key"] if asked else None)
    # F30: short replies ("refund", "personal use", "Rohtak, Haryana") look English even from a
    # Hinglish speaker. Only a message of 4+ words may change the language once it is set.
    lang = result.get("language")
    if lang == "hi" and not re.search(r"[\u0900-\u097F]", user_message):
        lang = "hinglish"          # F59: no Devanagari script -> it can't be "hi" (Groq labelled Hinglish as hi)
    if lang in ("en", "hi", "hinglish"):
        if case.get("language") is None or len(user_message.split()) >= 4:
            case["language"] = lang

    # F39: if the facts so far already mean "see a lawyer, no analysis" (e.g. business use, a shop, a court
    # notice), stop asking questions - more questions would only waste the user's time.
    stops = [c for c in load_calculators(case["pack"]).run_all(case["facts"]) if (c.get("escalate") or {}).get("stop")]
    if stops:
        lang = case.get("language") or "en"
        reply = {"hinglish": "Shukriya. Aapne jo bataya hai, uske hisaab se yeh maamla is assistant ke daayre se bahar hai - neeche dekhiye kyun.",
                 "hi": "धन्यवाद। आपने जो बताया है, उसके हिसाब से यह मामला इस सहायक के दायरे से बाहर है - नीचे देखिए क्यों।"
                 }.get(lang, "Thank you. Based on what you've told me, this is outside what this assistant can help with - see why below.")
        return {"reply": reply, "changed": changed, "done": True, "asked": None, "stopped_early": True}

    # F46: never ask the same question more than twice - after that, record "unknown" and move on.
    if asked and case["facts"].get(asked["key"]) is None:
        tries = case.setdefault("attempts", {})
        tries[asked["key"]] = tries.get(asked["key"], 0) + 1
        if tries[asked["key"]] >= 2:
            merge(case, {asked["key"]: UNKNOWN}, asked_key=asked["key"])

    nxt = next_field(case, intake)              # CODE decides the next question
    reply = phrase(case, user_message, nxt)
    return {"reply": reply, "changed": changed, "done": nxt is None,
            "asked": nxt["key"] if nxt else None}
