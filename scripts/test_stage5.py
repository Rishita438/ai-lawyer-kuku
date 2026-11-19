"""
test_stage5.py - offline checks for document drafting. No API key needed (the model is faked).

Run:  py scripts\\test_stage5.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.stdout.reconfigure(encoding="utf-8")                       # F29: Hindi/emoji safe when saved to a file
from app import llm, drafting

results = []


def check(name, condition, detail=""):
    results.append(condition)
    print(f"{'PASS' if condition else 'FAIL'}  {name}" + (f"   ({detail})" if detail else ""))


case = {"pack": "consumer", "language": "hinglish", "facts": {
    "product_or_service": "Redmi phone", "seller_name": "Flipkart", "bought_online": True, "amount_paid": 15000,
    "purchase_date": "2026-09-19", "what_went_wrong": "Phone stopped working within a week",
    "problem_date": "2026-10-26", "for_business_use": False,
    "complaints_made": "Complained to Flipkart customer care, no response",
    "evidence": ["invoice", "order ID", "chat screenshots"], "desired_outcome": "a full refund",
    "user_city_state": "Rohtak, Haryana"}}

good = lambda m: {"paragraphs": ["1. On 19 September 2026, I purchased a Redmi phone from Flipkart for Rs 15,000.",
                                 "2. On 26 October 2026, the phone stopped working.",
                                 "3. I complained to Flipkart customer care but received no response."]}
sneaky = lambda m: {"paragraphs": ["1. On 12 August 2026 I bought a Redmi phone from Flipkart for Rs 18,000.",
                                   "2. Under Section 2(9) I am entitled to a refund and will surely win."]}

print("\n== 1. Complaint with a well-behaved model ==")
llm.chat_json = good
d = drafting.draft(case, "commission_complaint")
check("model paragraph accepted", d["log"] == [], str(d["log"]))
check("citations come from the verified KB", "Section 69 of the Consumer Protection Act, 2019" in d["text"])
check("name/address are placeholders, never invented", "[YOUR FULL NAME]" in d["text"] and "[YOUR FULL ADDRESS]" in d["text"])
check("district left as placeholder (not guessed)", "[DISTRICT NAME]" in d["text"])
check("state taken from user's answer", "HARYANA" in d["text"])
check("placeholders listed for the user", len(d["placeholders"]) >= 5, ", ".join(d["placeholders"]))
check("explanation in Hinglish", d["explain"].startswith("Yeh"))

print("\n== 2. Model invents a date, an amount and a section ==")
llm.chat_json = sneaky
d2 = drafting.draft(case, "commission_complaint")
check("paragraph rejected", any("rejected" in x for x in d2["log"]), d2["log"][0] if d2["log"] else "")
check("invented date not in document", "12 August" not in d2["text"])
check("invented amount not in document", "18,000" not in d2["text"])
check("typed section not in document", "Section 2(9)" not in d2["text"])
check("plain version uses the real facts", "19 September 2026" in d2["text"] and "Rs 15,000" in d2["text"])

print("\n== 3. Model unavailable (503) ==")
llm.chat_json = lambda m: (_ for _ in ()).throw(RuntimeError("Error code: 503"))
d3 = drafting.draft(case, "grievance_letter")
check("letter still produced from facts", "Flipkart" in d3["text"] and "[ORDER ID]" in d3["text"], d3["log"][0])
check("e-commerce rule cited from KB with verified numbers", "48 hours" in d3["text"] and "E-Commerce" in d3["text"])

print("\n== 4. Gates ==")
unknown = {**case, "facts": {**case["facts"], "purchase_date": "unknown"}}
docs = {x["id"]: x for x in drafting.available(unknown)}
check("unknown purchase date -> complaint locked", not docs["commission_complaint"]["ok"], docs["commission_complaint"]["why_not"][0])
check("...but grievance letter still allowed", docs["grievance_letter"]["ok"])
llm.chat_json = good
check("...with a placeholder, not a guess", "[PURCHASE DATE" in drafting.draft(unknown, "grievance_letter")["text"])
offline = {**case, "facts": {**case["facts"], "bought_online": False}}
check("shop purchase -> no e-commerce letter offered", "grievance_letter" not in {x["id"] for x in drafting.available(offline)})
late = {**case, "facts": {**case["facts"], "problem_date": "2023-01-10"}}
check("time limit passed -> complaint locked", not {x["id"]: x for x in drafting.available(late)}["commission_complaint"]["ok"])
biz = {**case, "facts": {**case["facts"], "for_business_use": True}}
check("business use -> complaint locked", not {x["id"]: x for x in drafting.available(biz)}["commission_complaint"]["ok"])

print("\n== 5. The complaint as the user would download it ==\n")
print(d["text"])
print(f"\n{sum(results)}/{len(results)} checks passed")
sys.exit(0 if all(results) else 1)
