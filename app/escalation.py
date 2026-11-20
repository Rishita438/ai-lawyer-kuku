"""
escalation.py - when the bot must say "get a real lawyer". Plain rules, no AI.

Two kinds:
  1. KEYWORD rules on every user message (criminal, court, safety, out of scope)
     -> HARD STOP: the bot gives no legal analysis, only the referral message.
  2. CASE rules on the finished case file. These come from each pack's calculators
     ("escalate" on a result) plus one shared rule: a high amount -> recommend a lawyer.
     stop=True means the pack's analysis is not shown at all (e.g. "not a consumer").
The model may ADD a lawyer recommendation later; it can never remove one of these.
"""
import re

from app.kb import load_escalation


HINGLISH = {"hai", "hain", "tha", "thi", "ho", "gaya", "nahi", "nahin", "kya", "mujhe", "mera", "meri", "maine",
            "aaya", "karun", "kar", "raha", "rahi", "lena", "batao", "ke", "ki", "ka", "ko", "se", "mein", "me", "de", "dega"}


def detect_language(text: str) -> str:
    """Rough language guess for the hard-stop message (no AI involved): Devanagari -> hi, Hindi words in
    Latin script -> hinglish, else en."""
    if re.search(r"[\u0900-\u097F]", text):
        return "hi"
    words = re.findall(r"[a-z]+", text.lower())
    return "hinglish" if sum(w in HINGLISH for w in words) >= 2 else "en"


def check_message(text: str) -> dict | None:
    """Return {"category", "message", "matched"} if a hard-stop keyword appears, else None."""
    rules = load_escalation()
    lowered = text.lower()
    # safety first, then the others in file order
    for name, cat in sorted(rules["categories"].items(), key=lambda kv: kv[0] != "safety"):
        for kw in cat["keywords"]:
            kw = str(kw).lower()
            # whole-word match for latin words; plain substring for Devanagari
            pattern = rf"(?<!\w){re.escape(kw)}(?!\w)" if kw.isascii() else re.escape(kw)
            if re.search(pattern, lowered):
                lang = detect_language(text)
                msg = cat.get(f"message_{lang}") or cat["message"]          # F48: reply in the user's language
                return {"category": name, "message": " ".join(str(msg).split()), "matched": kw, "language": lang}
    return None


def keyword_check_applies(case: dict, intake: dict) -> bool:
    """Keyword rules run on every message EXCEPT a reply to a question marked skip_keyword_check
    (e.g. "Is it from a court or the police?" -> "nahi, police se nahi"). The opening story is never
    a reply to that question, so it is always checked (F35: the skip wrongly covered the first message)."""
    from app.case_file import next_field
    asked = next_field(case, intake)
    replying = len(case.get("user_messages", [])) > 1          # current message already appended
    return not (replying and asked and asked.get("skip_keyword_check"))


def check_case(facts: dict, calc_results: list[dict], amount_field: str | None = None) -> list[dict]:
    """Case-based escalation reasons after intake. Each: {"reason", "kb_ids", "stop": bool}."""
    reasons = [{"stop": bool(c["escalate"].get("stop")), "reason": c["escalate"]["reason"],
                "kb_ids": c.get("kb_ids", [])}
               for c in calc_results if c.get("escalate")]
    amount = facts.get(amount_field) if amount_field else None
    if isinstance(amount, (int, float)) and amount > load_escalation()["high_value_threshold_rupees"]:
        reasons.append({"stop": False, "kb_ids": [],
                        "reason": "The amount involved is high. For a claim this size, a lawyer's help is "
                                  "strongly recommended."})
    return reasons
