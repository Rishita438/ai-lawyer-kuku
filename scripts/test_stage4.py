"""
test_stage4.py - offline checks for Stage 4. No API key or internet needed.

Run:  py scripts\\test_stage4.py
It tests the CODE parts that guard against hallucination:
  calculators, escalation rules, and the citation/number validator (fed a deliberately bad answer).
"""
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
# Windows: when output is piped to a file, Python defaults to cp1252, which can't print
# Hindi or emojis (F29). Force UTF-8 so raw outputs are saved correctly.
sys.stdout.reconfigure(encoding="utf-8")
from app.kb import load_kb, load_calculators
from app.escalation import check_message, check_case
from app.validator import validate
from app.render import analysis_md

TODAY = date(2026, 11, 19)           # fixed, so results are repeatable
results = []


def check(name, condition, detail=""):
    results.append(condition)
    print(f"{'PASS' if condition else 'FAIL'}  {name}" + (f"   ({detail})" if detail else ""))


calc = load_calculators("consumer")
kb = load_kb("consumer")
rohtak = {"product_or_service": "redmi phone", "seller_name": "flipkart", "bought_online": True,
          "amount_paid": 15000, "purchase_date": "unknown", "what_went_wrong": "phone not working",
          "problem_date": "2026-10-26", "for_business_use": False, "complaints_made": "no response",
          "evidence": ["invoice", "order ID", "chat screenshots"], "desired_outcome": "refund",
          "user_city_state": "Rohtak, Haryana"}

print("\n== 1. Calculators (code, from verified KB numbers) ==")
r = {c["name"]: c for c in calc.run_all(rohtak, TODAY)}
check("time limit ok, deadline 2028-10-26", r["time_limit"]["status"] == "ok" and r["time_limit"]["deadline"] == "2028-10-26", str(r["time_limit"]))
check("District Commission for Rs 15,000", r["forum"]["level"] == "District")
check("fee is nil up to Rs 5 lakh", r["filing_fee"]["fee"] == 0)
check("fee Rs 400 for Rs 12 lakh", calc.filing_fee({"amount_paid": 12_00_000})["fee"] == 400)
check("fee Rs 7500 above Rs 10 crore", calc.filing_fee({"amount_paid": 11_00_00_000})["fee"] == 7500)
check("State Commission for Rs 60 lakh", calc.forum({"amount_paid": 60_00_000})["level"] == "State")
check("Rs 48 lakh flagged near boundary", calc.forum({"amount_paid": 48_00_000})["status"] == "near_boundary")
check("time limit passed (problem in 2024-10)", calc.time_limit({"problem_date": "2024-10-01"}, TODAY)["status"] == "passed")
check("time limit near (problem 2024-12-10)", calc.time_limit({"problem_date": "2024-12-10"}, TODAY)["status"] == "near")
check("unknown date -> unknown, not a guess", calc.time_limit({"problem_date": "unknown"}, TODAY)["status"] == "unknown")

print("\n== 2. Escalation rules (code, always fire) ==")
for text, expected in [("police ne FIR darj ki hai", "criminal"),
                       ("mujhe cheque bounce ka notice aaya hai", "criminal"),
                       ("पुलिस घर आई थी", "criminal"),
                       ("court se summons aaya hai", "court_or_official"),
                       ("divorce ke baare me batao", "out_of_scope"),
                       ("pati maarpeet karta hai", "safety"),
                       ("flipkart refund nahi de raha", None),
                       ("my order 420 rupees ka tha", "criminal")]:     # known false positive, kept visible
    hit = check_message(text)
    got = hit["category"] if hit else None
    check(f"{text!r} -> {expected}", got == expected, f"got {got}")
bad_case = dict(rohtak, for_business_use=True)
check("business use -> stop consumer analysis", any(e["stop"] for e in check_case(bad_case, calc.run_all(bad_case, TODAY))))
late = dict(rohtak, problem_date="2024-10-01")
check("time-barred -> lawyer flagged", any("time limit" in e["reason"] for e in check_case(late, calc.run_all(late, TODAY))))

print("\n== 3. Validator vs a deliberately BAD model answer ==")
evil = {
    "summary": "Under Section 2(7) of the Consumer Protection Act, 2019 you are a consumer and you will win.",
    "points": [
        {"text": "Flipkart must reply within 48 hours and fix it within one month.", "kb_ids": ["ECOM2020-R4-5"]},
        {"text": "You must file within 30 days.", "kb_ids": ["CPA2019-S69"]},
        {"text": "As held in Sharma v. Union of India, AIR 2019 SC 123, refunds are automatic.", "kb_ids": ["CASE-SHARMA"]},
        {"text": "IPC 420 also applies to the seller.", "kb_ids": []},
    ],
    "options": [{"title": "Complain to the grievance officer", "why": "fastest",
                 "steps": ["Email them citing Rule 4(5)", "Wait 48 hours"], "kb_ids": ["ECOM2020-R4-5", "FAKE-ID"]}],
    "uncertainties": ["Whether the warranty covers water damage."],
    "suggest_lawyer": False, "lawyer_reason": ""}
calcs = calc.run_all(rohtak, TODAY)
clean, log = validate(evil, kb, calcs, rohtak)
texts = " ".join([clean["summary"]] + [p["text"] for p in clean["points"]] + [s for o in clean["options"] for s in o["steps"]])
check("typed 'Section 2(7)' removed", "Section 2(7)" not in texts)
check("typed act name removed", "Consumer Protection Act" not in texts)
check("invented case law point dropped", not any("Sharma" in p["text"] for p in clean["points"]))
check("uncited IPC point dropped", not any("IPC" in p["text"] for p in clean["points"]))
check("invented kb_id 'FAKE-ID' removed", "FAKE-ID" not in clean["options"][0]["kb_ids"])
check("'30 days' (not in KB) removed", "30 days" not in texts)
check("'48 hours' (in verified KB) kept", "48 hours" in texts)
check("'Rule 4(5)' typed by model removed", "Rule 4(5)" not in texts)
check("'you will win' removed", "you will win" not in clean["summary"])
for promise in ["aapko pakka refund milega", "100% chance hai", "आपको ज़रूर मिलेगा"]:
    check(f"promise {promise!r} removed", "removed" in validate({"summary": promise}, kb, calcs, rohtak)[0]["summary"])
check("normal 'you may get a refund' kept", validate({"summary": "You may get a refund."}, kb, calcs, rohtak)[0]["summary"] == "You may get a refund.")
print(f"      -> validator removed {len(log)} item(s): " + ", ".join(sorted({x['type'] for x in log})))

print("\n== 4. Rendered answer for the bad model (what the user would see) ==\n")
print(analysis_md({"kb": kb, "calcs": calcs, "escalations": check_case(rohtak, calcs),
                   "analysis": clean, "validator_log": log}))

print(f"\n{sum(results)}/{len(results)} checks passed")
sys.exit(0 if all(results) else 1)
