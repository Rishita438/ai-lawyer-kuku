"""
intake.py - one conversation turn during fact-gathering.

Split of work (the core design idea):
  MODEL does : read a messy story (any language) -> pull out facts -> phrase the next question nicely
  CODE does  : decide WHICH question comes next, merge facts safely, decide when intake is done
The model is never asked for legal advice in this stage.
"""
import json
from datetime import date

from app import llm
from app.case_file import load_intake, merge, next_field, UNKNOWN

SYSTEM_PROMPT = """You help an ordinary person in India describe a legal problem. You are collecting facts only.
You do NOT give legal advice, do NOT mention laws or sections, and do NOT promise outcomes in this step.

Today's date is {today}.

Fields you may fill (key: description):
{field_list}

Rules:
1. Extract ONLY facts the user actually stated. Never guess or invent. If a fact was not said, leave it out.
2. If the user says they don't know a fact, set it to "{unknown}".
3. Dates: convert to YYYY-MM-DD. If only a month/year is given, use the 1st of that month.
   Resolve relative dates ("last week", "2 mahine pehle") using today's date.
4. Money: a plain number in rupees (e.g. 45000). "45k" = 45000. "1.2 lakh" = 120000.
5. yesno fields: true or false.
6. list fields: a JSON list of short strings.
7. Detect the user's language: "en", "hi" (Devanagari Hindi) or "hinglish" (Hindi in Latin script).
8. "reply": first briefly acknowledge what they told you (one short, kind sentence), then ask
   the NEXT QUESTION given below, in the user's language and style. Ask only that one question.
   If NEXT QUESTION is "NONE", thank them and say you now have the key facts.

Respond with ONLY a JSON object:
{{"extracted": {{<key>: <value>, ...}}, "language": "en|hi|hinglish", "reply": "<text>"}}"""


def _field_list(intake: dict) -> str:
    lines = []
    for f in intake["fields"]:
        hint = f" ({f['hint']})" if f.get("hint") else ""
        lines.append(f"- {f['key']} [{f['type']}]: {f['question']}{hint}")
    return "\n".join(lines)


def run_turn(case: dict, history: list[dict], user_message: str) -> dict:
    """Process one user message. Updates `case` in place.
    Returns {"reply": str, "changed": [keys], "done": bool}."""
    intake = load_intake(case["pack"])

    # 1) Ask the model to extract facts from the new message (+ short recent history for context).
    #    We tell it the question CODE will ask next, as of BEFORE this message;
    #    after merging we recompute, and re-ask the model to phrase the true next question if it changed.
    system = SYSTEM_PROMPT.format(today=date.today().isoformat(),
                                  field_list=_field_list(intake), unknown=UNKNOWN)
    known = {k: v for k, v in case["facts"].items() if v is not None}

    def ask(next_q: str) -> dict:
        messages = [{"role": "system", "content": system}]
        messages += history[-6:]                         # last few turns only (cost stays flat)
        messages.append({"role": "user", "content":
            f"FACTS ALREADY KNOWN: {json.dumps(known, ensure_ascii=False)}\n"
            f"NEXT QUESTION: {next_q}\n\n"
            f"USER MESSAGE: {user_message}"})
        return llm.chat_json(messages)

    before = next_field(case, intake)
    result = ask(before["question"] if before else "NONE")

    # 2) Code merges facts safely and decides what is next.
    explicit = {f["key"] for f in intake["fields"] if f.get("ask_explicitly")}
    changed = merge(case, result.get("extracted", {}), explicit_only=explicit,
                    asked_key=before["key"] if before else None)
    if result.get("language") in ("en", "hi", "hinglish"):
        case["language"] = result["language"]
    after = next_field(case, intake)

    # 3) If the story answered several questions at once, the model's reply may ask about
    #    something we now already know. Ask once more with the correct next question.
    reply = result.get("reply", "")
    if (after or {}).get("key") != (before or {}).get("key"):
        known = {k: v for k, v in case["facts"].items() if v is not None}
        try:
            reply = ask(after["question"] if after else "NONE").get("reply", reply)
        except Exception as err:
            # Facts are already saved; don't lose the turn. Ask the plain question from
            # intake.yaml instead (English, but correct). FAILURES F18.
            print(f"[intake] rephrase call failed, using plain question: {err}")
            reply = ("Thanks, I've noted that. " + after["question"]) if after else \
                    "Thanks - I now have the key facts of your case."

    return {"reply": reply, "changed": changed, "done": after is None}
