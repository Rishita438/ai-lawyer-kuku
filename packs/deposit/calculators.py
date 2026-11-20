"""
calculators.py - SECURITY DEPOSIT pack. Pure functions, no AI. Same contract as packs/consumer/calculators.py.

What the KB lets code say (and what it does NOT):
  - amount still due = deposit - returned                    (arithmetic on the user's own numbers)
  - time limit: "generally 3 years" (LIM1963-MONEY). The KB does NOT verify which article / start date
    applies to a deposit, so code NEVER computes a deadline date - it only shows time elapsed and
    sends the user to a lawyer when it's getting long.
  - Model Tenancy Act 2-month cap (MTA2021-S11): background only, never "the law says".
"""
from datetime import date

LIMIT_YEARS_GENERAL = 3          # LIM1963-MONEY: "most suits to recover money ... within 3 years"
LAWYER_AFTER_MONTHS = 30         # our safety margin: start date of the 3 years is not verified
MTA_CAP_MONTHS = 2               # MTA2021-S11 (model law, applies only if a state adopted it)


def _to_date(value):
    try:
        return date.fromisoformat(str(value))
    except (TypeError, ValueError):
        return None


def rupees(n) -> str:
    s = str(int(n))
    if len(s) <= 3:
        return s
    head, tail = s[:-3], s[-3:]
    groups = []
    while len(head) > 2:
        groups.insert(0, head[-2:]); head = head[:-2]
    return ",".join(([head] if head else []) + groups + [tail])


def residential(facts: dict) -> dict:
    out = {"name": "residential", "kb_ids": [], "status": {True: "yes", False: "no"}.get(facts.get("residential"), "unknown")}
    if out["status"] == "no":
        out["escalate"] = {"stop": True, "reason": "Shops, offices and other business premises are outside what this "
                           "assistant covers (commercial tenancy rules differ). Please consult a lawyer."}
        out["blocks_drafting"] = "Business premises are not covered - please consult a lawyer."
    return out


def amount_due(facts: dict) -> dict:
    out = {"name": "amount_due", "kb_ids": ["ICA1872-S73"]}
    dep, ret = facts.get("deposit_amount"), facts.get("amount_returned")
    if not isinstance(dep, (int, float)) or not isinstance(ret, (int, float)):
        return {**out, "status": "unknown", "display": "💰 **Amount still due:** unknown - deposit or amount returned not given."}
    if ret > dep:
        return {**out, "status": "inconsistent",
                "display": "💰 **Amount still due:** the amount returned is more than the deposit - please check the numbers.",
                "blocks_drafting": "The amounts don't add up (returned is more than the deposit) - please check them."}
    due = dep - ret
    if due == 0:
        return {**out, "status": "nothing_due", "due": 0,
                "display": "💰 **Amount still due:** nothing - the full deposit has been returned.",
                "blocks_drafting": "Nothing is due - the full deposit has been returned."}
    return {**out, "status": "ok", "due": due,
            "display": f"💰 **Amount still due:** Rs {rupees(due)} (deposit Rs {rupees(dep)} - returned Rs {rupees(ret)})."}


def time_elapsed(facts: dict, today: date | None = None) -> dict:
    today = today or date.today()
    out = {"name": "time_elapsed", "kb_ids": ["LIM1963-MONEY"]}
    moved = _to_date(facts.get("move_out_date"))
    general = (f"Most money claims must generally be filed in court within {LIMIT_YEARS_GENERAL} years, but when "
               "that period starts depends on the facts - this assistant does not calculate an exact deadline.")
    if moved is None:
        return {**out, "status": "unknown", "display": f"⏳ **Time:** move-out date unknown. {general}"}
    if moved > today:
        return {**out, "status": "date_in_future", "display": "⏳ **Time:** the move-out date given is in the future - please check it.",
                "escalate": {"stop": False, "reason": "The move-out date you gave is in the future - please check the dates."}}
    months = (today.year - moved.year) * 12 + today.month - moved.month - (today.day < moved.day)
    out.update(status="long" if months >= LAWYER_AFTER_MONTHS else "ok", months=months,
               display=f"⏳ **Time:** about {months} month(s) since you moved out. {general}")
    if months >= LAWYER_AFTER_MONTHS:
        out["escalate"] = {"stop": False, "reason": f"It has been about {months} months since you moved out. Money "
                           "claims generally have a 3-year limit - talk to a lawyer soon about whether you can still claim."}
    return out


def deposit_vs_rent(facts: dict) -> dict:
    out = {"name": "deposit_vs_rent", "kb_ids": ["MTA2021-S11"], "display": None}
    dep, rent = facts.get("deposit_amount"), facts.get("monthly_rent")
    if isinstance(dep, (int, float)) and isinstance(rent, (int, float)) and rent > 0 and dep > MTA_CAP_MONTHS * rent:
        out.update(status="above_model_cap",
                   display="ℹ️ **Background:** your deposit was more than two months' rent. The national *Model* Tenancy "
                           "Act suggests a two-month cap for homes, but it binds only if your state has passed a law based "
                           "on it - check your state's rent law.")
    else:
        out["status"] = "ok_or_unknown"
    return out


def state_law_note(facts: dict) -> dict:
    return {"name": "state_law", "kb_ids": [], "status": "info",
            "display": "🏠 **Note:** rent law is mostly state law. This assistant covers only general central law "
                       "(contract and time limits), not your state's rent act."}


def run_all(facts: dict, today: date | None = None) -> list[dict]:
    return [residential(facts), amount_due(facts), time_elapsed(facts, today), deposit_vs_rent(facts), state_law_note(facts)]


# ---------- document hooks ----------
def draft_slots(facts: dict, values: dict, cite) -> dict:
    dep, ret = facts.get("deposit_amount"), facts.get("amount_returned")
    known = isinstance(dep, (int, float)) and isinstance(ret, (int, float))
    return {"deposit_fmt": rupees(dep) if isinstance(dep, (int, float)) else "[DEPOSIT AMOUNT]",
            "unpaid_fmt": rupees(dep - ret) if known else "[AMOUNT STILL DUE]",
            "contract_citation": cite("ICA1872-S73")}


def plain_narrative(v: dict, own_words) -> str:
    return "\n\n".join([
        f"1. I was your tenant at the residential house at [ADDRESS OF THE RENTED HOUSE], {v['user_city_state']}, "
        f"and paid a security deposit of {v['deposit_amount']}.",
        f"2. I vacated the house and handed back possession and the keys on {v['move_out_date']}.",
        f"3. So far you have returned {v['amount_returned']} of the deposit.",
        f"4. Steps I have already taken: {own_words(v['complaints_made'])}.",
    ])
