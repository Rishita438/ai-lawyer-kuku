"""
calculators.py - CONSUMER pack. Pure functions, no AI (ADR-008).

Deadlines, which Commission, and fees are facts people act on, and models are bad at
date arithmetic and table lookups. So code computes them from the VERIFIED KB numbers
and the model is only allowed to repeat them.

PACK CONTRACT (every pack's calculators.py may provide these; the shared engine calls them):
  run_all(facts, today) -> list of results. Each result may carry:
      "display"         : one markdown line for the "Key facts" box
      "escalate"        : {"stop": bool, "reason": str} -> "see a lawyer" (stop = no analysis at all)
      "blocks_drafting" : str -> formal documents are locked, with this reason
  draft_slots(facts, values, cite) -> extra template slots for this pack's documents   (optional)
  plain_narrative(values, own_words) -> code-written facts paragraph, used if the AI's fails (optional)
"""
from datetime import date

# --- numbers copied from VERIFIED KB entries (see packs/consumer/kb.yaml) ---
LIMITATION_YEARS = 2                    # CPA2019-S69
NEAR_DEADLINE_DAYS = 60                 # our safety margin: dates from chat are approximate
DISTRICT_MAX = 50_00_000                # CPR2021-PECUNIARY: up to Rs 50 lakh
STATE_MAX = 2_00_00_000                 # CPR2021-PECUNIARY: up to Rs 2 crore
BOUNDARY_MARGIN = 0.10                  # within 10% of a limit -> "check with a lawyer"

# CPR2020-FEES, table as substituted in 2023 (Gazette 17-08-2023): (upper limit in Rs, fee in Rs)
FEE_TABLE = [
    (5_00_000, 0), (10_00_000, 200), (20_00_000, 400), (50_00_000, 1000),
    (1_00_00_000, 2000), (2_00_00_000, 2500), (4_00_00_000, 3000),
    (6_00_00_000, 4000), (8_00_00_000, 5000), (10_00_00_000, 6000),
]
FEE_ABOVE_TOP = 7500


def _to_date(value):
    try:
        return date.fromisoformat(str(value))
    except (TypeError, ValueError):
        return None


def _add_years(d: date, years: int) -> date:
    try:
        return d.replace(year=d.year + years)
    except ValueError:                   # 29 Feb -> 28 Feb
        return d.replace(year=d.year + years, day=28)


def rupees(n) -> str:
    """Indian-style grouping: 1500000 -> 15,00,000."""
    s = str(int(n))
    if len(s) <= 3:
        return s
    head, tail = s[:-3], s[-3:]
    groups = []
    while len(head) > 2:
        groups.insert(0, head[-2:]); head = head[:-2]
    return ",".join(([head] if head else []) + groups + [tail])


# ---------- calculators ----------
def is_consumer(facts: dict) -> dict:
    v = facts.get("for_business_use")
    status = {False: "yes", True: "probably_not"}.get(v, "unknown")
    out = {"name": "consumer_check", "status": status, "kb_ids": ["CPA2019-S2-7"], "display": None}
    if status == "probably_not":
        reason = ("You bought this for resale or business use, so consumer law may not cover you. "
                  "A lawyer can advise on other remedies.")
        out["escalate"] = {"stop": True, "reason": reason}
        out["blocks_drafting"] = "Bought for business use - consumer law may not apply. Please consult a lawyer."
    return out


def time_limit(facts: dict, today: date | None = None) -> dict:
    today = today or date.today()
    start = _to_date(facts.get("problem_date"))
    out = {"name": "time_limit", "kb_ids": ["CPA2019-S69"], "years": LIMITATION_YEARS}
    if start is None:
        return {**out, "status": "unknown",
                "display": "⏳ **Time limit:** can't calculate - the date the problem arose is unknown. "
                           "The normal limit is 2 years from that date."}
    if start > today:
        return {**out, "status": "date_in_future", "start": start.isoformat(),
                "display": "⏳ **Time limit:** the problem date given is in the future - please check it.",
                "escalate": {"stop": False, "reason": "The problem date you gave is in the future - please check the dates."}}
    deadline = _add_years(start, LIMITATION_YEARS)
    days_left = (deadline - today).days
    status = "passed" if days_left < 0 else "near" if days_left <= NEAR_DEADLINE_DAYS else "ok"
    word = {"ok": "✅ within the limit", "near": "⚠️ close to the limit", "passed": "❌ may have passed"}[status]
    out.update(status=status, start=start.isoformat(), deadline=deadline.isoformat(), days_left=days_left,
               display=f"⏳ **Time limit:** {word}. Normally file by **{deadline.isoformat()}** "
                       f"(2 years from {start.isoformat()}; dates are approximate).")
    if status == "passed":
        out["escalate"] = {"stop": False, "reason": "The normal 2-year time limit may already have passed. A late "
                           "complaint is possible only if the Commission accepts your reason for the delay - please "
                           "talk to a lawyer before filing."}
        out["blocks_drafting"] = "The 2-year time limit may have passed - talk to a lawyer before filing."
    elif status == "near":
        out["escalate"] = {"stop": False, "reason": f"You may be close to the 2-year time limit (about {days_left} "
                           "days left, based on approximate dates). Act quickly and consider talking to a lawyer."}
    return out


def forum(facts: dict) -> dict:
    out = {"name": "forum", "kb_ids": ["CPR2021-PECUNIARY", "CPA2019-S34"]}
    amount = facts.get("amount_paid")
    if not isinstance(amount, (int, float)) or amount <= 0:
        return {**out, "status": "unknown", "display": "🏛️ **Which Commission:** unknown - amount paid not given."}
    level = "District" if amount <= DISTRICT_MAX else "State" if amount <= STATE_MAX else "National"
    near = any(abs(amount - lim) <= lim * BOUNDARY_MARGIN for lim in (DISTRICT_MAX, STATE_MAX))
    where = facts.get("user_city_state")
    where_txt = f" (you can file where you live or work: {where})" if where not in (None, "unknown") else ""
    out.update(status="near_boundary" if near else "ok", level=level, amount=amount, where=where,
               display=f"🏛️ **Which Commission:** {level} Consumer Commission, for Rs {rupees(amount)} paid{where_txt}."
                       + (" ⚠️ close to a limit - confirm with a lawyer" if near else ""))
    if near:
        out["escalate"] = {"stop": False, "reason": "The amount is close to a limit that decides which Commission "
                           "hears the case. Confirm the right Commission with a lawyer."}
    return out


def filing_fee(facts: dict) -> dict:
    out = {"name": "filing_fee", "kb_ids": ["CPR2020-FEES"]}
    amount = facts.get("amount_paid")
    if not isinstance(amount, (int, float)) or amount <= 0:
        return {**out, "status": "unknown", "display": "💰 **Filing fee:** unknown - amount paid not given."}
    fee = next((f for upper, f in FEE_TABLE if amount <= upper), FEE_ABOVE_TOP)
    return {**out, "status": "ok", "fee": fee, "amount": amount,
            "display": f"💰 **Filing fee:** {'nil (no fee)' if fee == 0 else 'Rs ' + rupees(fee)}."}


def online_purchase(facts: dict) -> dict:
    v = facts.get("bought_online")
    return {"name": "ecommerce_grievance", "status": {True: "applies", False: "not_applicable"}.get(v, "unknown"),
            "kb_ids": ["ECOM2020-R4-5"], "display": None}


def run_all(facts: dict, today: date | None = None) -> list[dict]:
    return [is_consumer(facts), time_limit(facts, today), forum(facts),
            filing_fee(facts), online_purchase(facts)]


# ---------- document hooks (Stage 5) ----------
def draft_slots(facts: dict, values: dict, cite) -> dict:
    amount = facts.get("amount_paid")
    ecom = cite("ECOM2020-R4-5")
    return {
        "amount_paid_fmt": rupees(amount) if isinstance(amount, (int, float)) else "[AMOUNT PAID]",
        "problem_date_fmt": values["problem_date"],
        "forum_citation": cite("CPR2021-PECUNIARY"),
        "territorial_citation": cite("CPA2019-S34"),
        "limitation_citation": cite("CPA2019-S69"),
        "relief_citation": cite("CPA2019-S39"),
        # numbers below come from the VERIFIED summary of ECOM2020-R4-5 (48 hours / one month)
        "ecom_rule_sentence": "" if ecom.startswith("[") else
            (f"Under {ecom}, the grievance officer is required to acknowledge a consumer complaint within "
             "48 hours and redress it within one month of receiving it. I request you to do so."),
    }


def plain_narrative(v: dict, own_words) -> str:
    """Code-written facts paragraph (used if the AI's paragraph fails the checks)."""
    return "\n\n".join([
        f"1. On {v['purchase_date']}, I purchased {v['product_or_service']} from {v['seller_name']} "
        f"for {v['amount_paid']}.",
        f"2. On {v['problem_date']}, the following problem arose: {own_words(v['what_went_wrong'])}.",
        "3. I purchased it for my personal use." if v.get("for_business_use") == "no" else
        "3. Purpose of purchase: [PERSONAL OR BUSINESS USE – please state].",
        f"4. Steps I have already taken: {own_words(v['complaints_made'])}.",
    ])
