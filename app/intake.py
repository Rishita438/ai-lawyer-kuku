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
from datetime import date

from app import llm
from app.case_file import load_intake, merge, next_field, UNKNOWN

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
5. Money -> plain number in rupees ("15k" = 15000, "1.2 lakh" = 120000).
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


def _field_list(intake: dict) -> str:
    lines = []
    for f in intake["fields"]:
        hint = f" ({f['hint']})" if f.get("hint") else ""
        lines.append(f"- {f['key']} [{f['type']}]: {f['question']}{hint}")
    return "\n".join(lines)


def _question(field: dict, language: str | None) -> str:
    """The question in the user's language, from intake.yaml - chosen by code, not translated by the model (F27)."""
    if language == "hinglish" and field.get("question_hinglish"):
        return field["question_hinglish"]
    if language == "hi" and field.get("question_hi"):
        return field["question_hi"]
    return field["question"]


def _plain_reply(field: dict | None, language: str | None = None) -> str:
    """Safe fallback: the exact question from intake.yaml, in the user's language."""
    thanks = {"hinglish": "Shukriya, maine note kar liya.", "hi": "धन्यवाद, मैंने नोट कर लिया।"}.get(language, "Thanks, I've noted that.")
    if field is None:
        done = {"hinglish": "Shukriya - ab mere paas aapke case ki zaroori jaankari hai.",
                "hi": "धन्यवाद - अब मेरे पास आपके मामले की ज़रूरी जानकारी है।"}
        return done.get(language, "Thanks - I now have the key facts of your case.")
    return thanks + " " + _question(field, language)


def extract(case: dict, history: list[dict], user_message: str, asked: dict | None) -> dict:
    """Call 1: facts only."""
    intake = load_intake(case["pack"])
    system = EXTRACT_PROMPT.format(today=date.today().isoformat(),
                                   field_list=_field_list(intake), unknown=UNKNOWN)
    last_q = asked["question"] if asked else "(opening message)"
    messages = [{"role": "system", "content": system}]
    messages += history[-4:]                              # a little context, cost stays flat
    messages.append({"role": "user", "content":
        f"QUESTION THE USER IS ANSWERING: {last_q}\nUSER MESSAGE: {user_message}"})
    return llm.chat_json(messages)


def phrase(case: dict, user_message: str, field: dict | None) -> str:
    """Call 2: a friendly reply that asks exactly `field`'s question. Verified by code."""
    lang = case.get("language") or "en"
    key = field["key"] if field else "NONE"
    question = _question(field, lang) if field else "NONE"
    system = PHRASE_PROMPT.format(language=lang, question=question, key=key)
    try:
        out = llm.chat_json([{"role": "system", "content": system},
                             {"role": "user", "content": user_message}])
        reply = (out.get("reply") or "").strip()
    except Exception as err:                              # F18: never lose the turn
        print(f"[intake] phrase call failed, using plain question: {err}")
        return _plain_reply(field, lang)
    if not reply or out.get("asked_field") != key:
        print(f"[intake] phrase reply unusable (asked {out.get('asked_field')!r}, wanted {key!r})")
        return _plain_reply(field, lang)
    if field is not None and "?" not in reply:            # F24: must actually ask
        reply += " " + question
    return reply


def run_turn(case: dict, history: list[dict], user_message: str) -> dict:
    """Process one user message. Updates `case` in place.
    Returns {"reply": str, "changed": [keys], "done": bool, "asked": key|None}."""
    intake = load_intake(case["pack"])
    asked = next_field(case, intake)            # the question this message is answering

    result = extract(case, history, user_message, asked)
    explicit = {f["key"] for f in intake["fields"] if f.get("ask_explicitly")}
    changed = merge(case, result.get("extracted", {}), explicit_only=explicit,
                    asked_key=asked["key"] if asked else None)
    # F30: short replies ("refund", "personal use", "Rohtak, Haryana") look English even from a
    # Hinglish speaker. Only a message of 4+ words may change the language once it is set.
    if result.get("language") in ("en", "hi", "hinglish"):
        if case.get("language") is None or len(user_message.split()) >= 4:
            case["language"] = result["language"]

    nxt = next_field(case, intake)              # CODE decides the next question
    reply = phrase(case, user_message, nxt)
    return {"reply": reply, "changed": changed, "done": nxt is None,
            "asked": nxt["key"] if nxt else None}
