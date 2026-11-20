"""
calculators.py - UNPAID SALARY pack (light). Pure functions, no AI. Same contract as the consumer pack.

From the verified KB:
  COW2019-S17      monthly wages due before the 7th of the next month; final dues within 2 working days of leaving
  COW2019-S45      wage claims: generally 3 years to file; start point not defined in the Code -> no exact deadline
  NOTE-LABOUR-CODES Codes in force from 21 Nov 2025; older law may matter for earlier claims; state rules vary
"""
from datetime import date

CODES_IN_FORCE = date(2025, 11, 21)    # NOTE-LABOUR-CODES
CLAIM_YEARS = 3                        # COW2019-S45
LAWYER_AFTER_MONTHS = 30               # safety margin: start of the 3 years is not defined


def _to_date(value):
    try:
        return date.fromisoformat(str(value))
    except (TypeError, ValueError):
        return None


def _months(since: date, today: date) -> int:
    return (today.year - since.year) * 12 + today.month - since.month - (today.day < since.day)


def government(facts: dict) -> dict:
    out = {"name": "government_job", "kb_ids": ["COW2019-S17"], "status": {True: "yes", False: "no"}.get(facts.get("govt_job"), "unknown")}
    if out["status"] == "yes":
        out["escalate"] = {"stop": True, "reason": "Salary disputes in government jobs follow different service rules, "
                           "which this assistant does not cover. Please consult a lawyer or your department's grievance cell."}
    return out


def law_in_force(facts: dict) -> dict:
    start = _to_date(facts.get("unpaid_since"))
    out = {"name": "law_in_force", "kb_ids": ["NOTE-LABOUR-CODES"]}
    if start is not None and start < CODES_IN_FORCE:
        return {**out, "status": "before_codes",
                "display": "⚖️ **Which law:** your unpaid salary started before 21 November 2025, when the new Labour "
                           "Codes came into force - the older law may still matter for your claim.",
                "escalate": {"stop": False, "reason": "Your unpaid salary started before the Labour Codes came into force "
                             "(21 Nov 2025). Which law applies can be tricky - check with your local Labour Office or a lawyer."}}
    return {**out, "status": "codes", "display": "⚖️ **Which law:** the Code on Wages, 2019 (in force since 21 November "
            "2025). Rules under it differ by state - your local Labour Office can confirm the process."}


def payment_deadline(facts: dict) -> dict:
    out = {"name": "payment_deadline", "kb_ids": ["COW2019-S17"]}
    if facts.get("still_employed") is False:
        return {**out, "status": "left", "display": "💼 **Final dues:** when someone leaves, resigns or is removed, wages "
                "due must be paid within two working days."}
    return {**out, "status": "employed", "display": "💼 **Monthly salary:** for monthly-paid employees, wages are due before "
            "the 7th day of the next month."}


def claim_time(facts: dict, today: date | None = None) -> dict:
    today = today or date.today()
    out = {"name": "claim_time", "kb_ids": ["COW2019-S45"]}
    start = _to_date(facts.get("unpaid_since"))
    general = (f"A wage claim can generally be filed within {CLAIM_YEARS} years from when it arose; the law does not "
               "define the exact start, so this assistant does not calculate a deadline.")
    if start is None:
        return {**out, "status": "unknown", "display": f"⏳ **Time:** {general}"}
    m = _months(start, today)
    out.update(status="long" if m >= LAWYER_AFTER_MONTHS else "ok", months=m,
               display=f"⏳ **Time:** salary unpaid for about {m} month(s). {general}")
    if m >= LAWYER_AFTER_MONTHS:
        out["escalate"] = {"stop": False, "reason": f"Your salary has been unpaid for about {m} months. Wage claims "
                           "generally have a 3-year limit - talk to a lawyer or the Labour Office soon."}
    return out


def run_all(facts: dict, today: date | None = None) -> list[dict]:
    return [government(facts), law_in_force(facts), payment_deadline(facts), claim_time(facts, today)]
