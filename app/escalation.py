"""
escalation.py - when the bot must say "get a real lawyer". Plain rules, no AI.

Two kinds:
  1. KEYWORD rules on every user message (criminal, court, safety, out of scope)
     -> HARD STOP: the bot gives no legal analysis, only the referral message.
  2. CASE rules on the finished case file (time limit, amount, not a consumer)
     -> the analysis is still shown, with a clear "you should see a lawyer" box,
        except "not a consumer", which stops the consumer analysis.
The model may ADD a lawyer recommendation later; it can never remove one of these.
"""
import re

from app.kb import load_escalation


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
                return {"category": name, "message": " ".join(cat["message"].split()), "matched": kw}
    return None


def check_case(facts: dict, calc_results: list[dict]) -> list[dict]:
    """Case-based escalation reasons after intake. Each: {"reason", "kb_ids", "stop": bool}."""
    rules = load_escalation()
    calc = {c["name"]: c for c in calc_results}
    reasons = []

    if calc["consumer_check"]["status"] == "probably_not":
        reasons.append({"stop": True, "kb_ids": ["CPA2019-S2-7"],
                        "reason": "You bought this for resale or business use, so consumer law may not cover "
                                  "you. A lawyer can advise on other remedies."})

    t = calc["time_limit"]
    if t["status"] == "passed":
        reasons.append({"stop": False, "kb_ids": ["CPA2019-S69"],
                        "reason": "The normal 2-year time limit may already have passed. A late complaint is "
                                  "possible only if the Commission accepts your reason for the delay - "
                                  "please talk to a lawyer before filing."})
    elif t["status"] == "near":
        reasons.append({"stop": False, "kb_ids": ["CPA2019-S69"],
                        "reason": f"You may be close to the 2-year time limit (about {t['days_left']} days left, "
                                  "based on approximate dates). Act quickly and consider talking to a lawyer."})
    elif t["status"] == "date_in_future":
        reasons.append({"stop": False, "kb_ids": [],
                        "reason": "The problem date you gave is in the future - please check the dates."})

    f = calc["forum"]
    amount = facts.get("amount_paid")
    if isinstance(amount, (int, float)) and amount > rules["high_value_threshold_rupees"]:
        reasons.append({"stop": False, "kb_ids": [],
                        "reason": "The amount involved is high. For a claim this size, a lawyer's help is "
                                  "strongly recommended."})
    if f.get("status") == "near_boundary":
        reasons.append({"stop": False, "kb_ids": ["CPR2021-PECUNIARY"],
                        "reason": "The amount is close to a limit that decides which Commission hears the case. "
                                  "Confirm the right Commission with a lawyer."})
    return reasons
