"""
calculators.py - NOTICE EXPLAINER pack (light). Pure functions, no AI.

Its job is mostly to escalate: official notices -> lawyer immediately (PROC-NOTICE-OFFICIAL);
a close deadline -> act now. Keyword rules (summons, police, cheque bounce...) already run on every message.
"""
from datetime import date

URGENT_DAYS = 7      # deadline within a week -> get advice now


def _to_date(value):
    try:
        return date.fromisoformat(str(value))
    except (TypeError, ValueError):
        return None


def sender_type(facts: dict) -> dict:
    status = {True: "official", False: "private"}.get(facts.get("official_sender"), "unknown")
    # cite only the entry that applies (N01 grading: a private notice showed the court/police entry too)
    ids = {"official": ["PROC-NOTICE-OFFICIAL"], "private": ["PROC-NOTICE-PRIVATE"]}.get(status, [])
    out = {"name": "sender_type", "kb_ids": ids, "status": status}
    if out["status"] == "official":
        out["escalate"] = {"stop": True, "reason": "A notice from a court, the police, a tribunal or a government/tax "
                           "office can carry a date you must not miss. This assistant will not advise on it - please "
                           "contact a lawyer quickly."}
    elif out["status"] == "private":
        out["display"] = ("📨 **Who sent it:** a private party (not a court or government). A legal notice like this is "
                          "a formal demand, not a court order.")
    return out


def deadline(facts: dict, today: date | None = None) -> dict:
    today = today or date.today()
    out = {"name": "deadline", "kb_ids": ["PROC-NOTICE-PRIVATE"]}
    d = _to_date(facts.get("deadline_in_notice"))
    if d is None:
        return {**out, "status": "none_or_unknown",
                "display": "📅 **Deadline:** none given (or not known). Still, don't ignore the notice."}
    days = (d - today).days
    if days < 0:
        status, text = "passed", f"📅 **Deadline:** {d.isoformat()} - already passed ({-days} day(s) ago)."
    else:
        status, text = ("urgent" if days <= URGENT_DAYS else "ok"), f"📅 **Deadline:** {d.isoformat()} - {days} day(s) from today."
    out.update(status=status, days=days, display=text)
    if status in ("passed", "urgent"):
        out["escalate"] = {"stop": False, "reason": "The deadline in the notice is very close or has passed. Get advice "
                           "from a lawyer or your District Legal Services Authority quickly before replying."}
    return out


def run_all(facts: dict, today: date | None = None) -> list[dict]:
    return [sender_type(facts), deadline(facts, today)]
