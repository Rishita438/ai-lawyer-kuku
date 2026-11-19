"""
calculators.py - CONSUMER pack. Pure functions, no AI (ADR-008).

Deadlines, which Commission, and fees are facts people act on, and models are bad at
date arithmetic and table lookups. So code computes them from the VERIFIED KB numbers
and the model is only allowed to repeat them.

Every result carries the kb_id it is based on, so the answer can cite it.
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


def is_consumer(facts: dict) -> dict:
    v = facts.get("for_business_use")
    status = {False: "yes", True: "probably_not"}.get(v, "unknown")
    return {"name": "consumer_check", "status": status, "kb_ids": ["CPA2019-S2-7"]}


def time_limit(facts: dict, today: date | None = None) -> dict:
    today = today or date.today()
    start = _to_date(facts.get("problem_date"))
    out = {"name": "time_limit", "kb_ids": ["CPA2019-S69"], "years": LIMITATION_YEARS}
    if start is None:
        return {**out, "status": "unknown"}
    if start > today:
        return {**out, "status": "date_in_future", "start": start.isoformat()}
    deadline = _add_years(start, LIMITATION_YEARS)
    days_left = (deadline - today).days
    status = "passed" if days_left < 0 else "near" if days_left <= NEAR_DEADLINE_DAYS else "ok"
    return {**out, "status": status, "start": start.isoformat(),
            "deadline": deadline.isoformat(), "days_left": days_left}


def forum(facts: dict) -> dict:
    out = {"name": "forum", "kb_ids": ["CPR2021-PECUNIARY", "CPA2019-S34"]}
    amount = facts.get("amount_paid")
    if not isinstance(amount, (int, float)) or amount <= 0:
        return {**out, "status": "unknown"}
    level = "District" if amount <= DISTRICT_MAX else "State" if amount <= STATE_MAX else "National"
    near = any(abs(amount - lim) <= lim * BOUNDARY_MARGIN for lim in (DISTRICT_MAX, STATE_MAX))
    return {**out, "status": "near_boundary" if near else "ok", "level": level,
            "amount": amount, "where": facts.get("user_city_state")}


def filing_fee(facts: dict) -> dict:
    out = {"name": "filing_fee", "kb_ids": ["CPR2020-FEES"]}
    amount = facts.get("amount_paid")
    if not isinstance(amount, (int, float)) or amount <= 0:
        return {**out, "status": "unknown"}
    fee = next((f for upper, f in FEE_TABLE if amount <= upper), FEE_ABOVE_TOP)
    return {**out, "status": "ok", "fee": fee, "amount": amount}


def online_purchase(facts: dict) -> dict:
    v = facts.get("bought_online")
    return {"name": "ecommerce_grievance", "status": {True: "applies", False: "not_applicable"}.get(v, "unknown"),
            "kb_ids": ["ECOM2020-R4-5"]}


def run_all(facts: dict, today: date | None = None) -> list[dict]:
    return [is_consumer(facts), time_limit(facts, today), forum(facts),
            filing_fee(facts), online_purchase(facts)]
