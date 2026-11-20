"""
test_packs.py - offline checks for the deposit, salary and notice packs. No API key needed.

Run:  py scripts\\test_packs.py
"""
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.stdout.reconfigure(encoding="utf-8")
from app import llm, drafting
from app.kb import load_calculators, load_kb
from app.case_file import new_case, load_intake, next_field, merge, missing
from app.escalation import check_case
from app.render import computed_facts_md

TODAY = date(2026, 11, 20)
results = []


def check(name, condition, detail=""):
    results.append(condition)
    print(f"{'PASS' if condition else 'FAIL'}  {name}" + (f"   ({detail})" if detail else ""))


def calcs(pack, facts):
    return {c["name"]: c for c in load_calculators(pack).run_all(facts, TODAY)}


print("\n== Deposit pack (full) ==")
dep = {"residential": True, "deposit_amount": 50000, "amount_returned": 10000, "monthly_rent": 15000,
       "move_out_date": "2026-08-31", "complaints_made": "asked twice on WhatsApp", "evidence": ["rent agreement"],
       "desired_outcome": "full deposit back", "user_city_state": "pune,maharashtra", "agreement": "yes",
       "landlord_reason": "painting", "handover_proof": "photos"}
c = calcs("deposit", dep)
check("amount due = 50,000 - 10,000", c["amount_due"].get("due") == 40000)
check("no deadline DATE computed (start not verified)", "deadline" not in c["time_elapsed"] and "does not calculate" in c["time_elapsed"]["display"])
check("deposit > 2x rent -> Model Act shown as background only", "binds only if your state" in c["deposit_vs_rent"]["display"])
check("shop/office -> stop", calcs("deposit", {**dep, "residential": False})["residential"]["escalate"]["stop"])
check("returned > deposit -> numbers flagged", calcs("deposit", {**dep, "amount_returned": 60000})["amount_due"]["status"] == "inconsistent")
check("31 months since move-out -> lawyer", "escalate" in calcs("deposit", {**dep, "move_out_date": "2024-04-01"})["time_elapsed"])
case = {"pack": "deposit", "language": "en", "facts": dep}
check("notice offered when facts complete", [d["ok"] for d in drafting.available(case)] == [True])
llm.chat_json = lambda m: (_ for _ in ()).throw(RuntimeError("503"))
notice = drafting.draft(case, "deposit_notice")
check("notice works even with model down", "Rs 40,000" in notice["text"] and "Section 73 of the Indian Contract Act, 1872" in notice["text"])
check("landlord's name never invented", "[LANDLORD'S FULL NAME]" in notice["text"])
check("nothing due -> notice locked", not drafting.available({**case, "facts": {**dep, "amount_returned": 50000}})[0]["ok"])

print("\n== Salary pack (basics) ==")
sal = {"employer_name": "abc pvt ltd", "govt_job": False, "still_employed": True, "unpaid_since": "2026-08-01",
       "amount_due": 90000, "complaints_made": "emailed HR", "evidence": ["offer letter"], "user_city_state": "Noida, UP"}
c = calcs("salary", sal)
check("still employed -> monthly 7th rule shown", "7th" in c["payment_deadline"]["display"])
check("left the job -> two working days rule", "two working days" in calcs("salary", {**sal, "still_employed": False})["payment_deadline"]["display"])
check("unpaid since Aug 2025 -> old-law caveat + lawyer", "escalate" in calcs("salary", {**sal, "unpaid_since": "2025-08-01"})["law_in_force"])
check("government job -> stop", calcs("salary", {**sal, "govt_job": True})["government_job"]["escalate"]["stop"])
check("no wage-claim deadline date computed", "does not calculate" in c["claim_time"]["display"])
s_case = new_case("salary"); intake = load_intake("salary")
merge(s_case, {"still_employed": True}, asked_key="still_employed")
check("still employed -> 'last working day' skipped", "last_working_day" not in [f["key"] for f in missing(s_case, intake)])
check("salary pack has no documents (light)", drafting.available({"pack": "salary", "facts": sal}) == [])

print("\n== Notice pack (basics) ==")
check("court/police/govt notice -> stop", calcs("notice", {"official_sender": True})["sender_type"]["escalate"]["stop"])
check("private notice explained as a demand, not a court order", "not a court order" in calcs("notice", {"official_sender": False})["sender_type"]["display"])
check("deadline in 3 days -> urgent + lawyer", "escalate" in calcs("notice", {"deadline_in_notice": "2026-11-23"})["deadline"])
check("deadline passed -> flagged", calcs("notice", {"deadline_in_notice": "2026-11-01"})["deadline"]["status"] == "passed")
check("no deadline -> 'don't ignore it'", "don't ignore" in calcs("notice", {"deadline_in_notice": "unknown"})["deadline"]["display"])
from app.escalation import keyword_check_applies
n_case = new_case("notice"); n_case["user_messages"] = ["cheque bounce ka notice aaya hai"]
check("opening story is ALWAYS keyword-checked (F35)", keyword_check_applies(n_case, load_intake("notice")))
n_case["user_messages"].append("nahi, police se nahi, vakil ka hai")
check("reply to the official-sender question skips keywords (negation)", not keyword_check_applies(n_case, load_intake("notice")))

print("\n== Regressions from the real test run ==")
from app.validator import validate
weird = {"summary": {"text": "ok"}, "points": ["not a dict"], "options": "one option as text",
         "uncertainties": [{"issue": "state law", "note": "unclear"}, None]}
try:
    clean, _ = validate(weird, load_kb("consumer"), [], {})
    check("F38: odd model output shape doesn't crash the validator", "state law" in " ".join(clean["uncertainties"]))
except Exception as err:
    check("F38: odd model output shape doesn't crash the validator", False, repr(err))

from app.intake import run_turn
def shop_model(m):
    if m[0]["content"].startswith("You extract"):
        if "(opening message)" in m[-1]["content"]:
            return {"extracted": {"residential": False, "deposit_amount": 200000}, "language": "en"}
        return {"extracted": {"residential": False}, "language": "en"}
    k = m[0]["content"].split('"asked_field": "')[1].split('"')[0]
    q = m[0]["content"].split("nothing else: ")[1].split("\n")[0]
    return {"reply": "Thanks. " + q, "asked_field": k}
llm.chat_json = shop_model
d_case, hist = new_case("deposit"), []
r1 = run_turn(d_case, hist, "I rented a shop for my business, owner won't return Rs 2 lakh")
check("F39: yes/no question asked plainly, not as a double-negative confirmation", "You mentioned" not in r1["reply"], r1["reply"])
hist += [{"role": "user", "content": "story"}, {"role": "assistant", "content": r1["reply"]}]
r2 = run_turn(d_case, hist, "No, it was a shop for my business")
check("F39: stop condition known -> intake ends early (no more questions)", r2["done"] and r2.get("stopped_early"), r2["reply"][:60])

print("\n== Regressions from the second real run (F40-F47) ==")
from app.validator import clean_text
check("F40: 'guarantee nahi di ja sakti' kept (honest refusal)", clean_text("koi guarantee nahi di ja sakti.", set(), []) == "koi guarantee nahi di ja sakti.")
check("F40: 'pakka refund milega, koi shak nahi' still removed", "removed" in clean_text("Aapko pakka refund milega, koi shak nahi.", set(), []))
check("F40: 'could not verify Section 420B' kept but marked unverified",
      "not verified" in clean_text("I could not verify the Section 420B you mentioned.", set(), [], allow_unverified_refs=True))
from app.validator import validate
c44, _ = validate({"summary": "4 mahine ki salary baaki hai."}, load_kb("salary"), [], {}, ["4 mahine ki 1.2 lakh baaki hai"])
check("F44: user's own number ('4 mahine') not stripped", "4 mahine" in c44["summary"], c44["summary"])

from app.intake import phrase
fake_case = {"pack": "consumer", "language": "hinglish", "facts": {}, "user_messages": []}
llm.chat_json = lambda m: {"reply": "Aapne section 420B ka zikr kiya. Aap kahan rehte hain?", "asked_field": "user_city_state"}
city_field = [f for f in load_intake("consumer")["fields"] if f["key"] == "user_city_state"][0]
check("F41: acknowledgement mentioning a law is replaced", "420B" not in phrase(fake_case, "x", city_field))

def wrong_field_model(m):          # model attaches "pata nahi" to the WRONG field, like in C09
    if m[0]["content"].startswith("You extract"):
        return {"extracted": {"purchase_date": "unknown"}, "language": "hinglish"}
    k = m[0]["content"].split('"asked_field": "')[1].split('"')[0]
    return {"reply": "Theek hai. Agla sawaal?", "asked_field": k}
llm.chat_json = wrong_field_model
c46 = new_case("consumer"); c46["facts"].update({"product_or_service": "mixer", "seller_name": "Amazon", "for_business_use": False,
                                                  "bought_online": True, "amount_paid": 3200, "purchase_date": "unknown",
                                                  "what_went_wrong": "kharab"})
h46 = [{"role": "user", "content": "story"}, {"role": "assistant", "content": "q"}]
r46 = run_turn(c46, h46, "pata nahi")
check("F46: 'pata nahi' recorded by code for the asked field", c46["facts"]["problem_date"] == "unknown" and r46["asked"] != "problem_date", r46["asked"])

check("F47: business-use question comes 3rd in the consumer pack",
      [f["key"] for f in load_intake("consumer")["fields"]].index("for_business_use") == 2)

biz = {"pack": "consumer", "language": "en", "facts": {"bought_online": True, "for_business_use": True}}
check("F43: business purchase -> every document locked", all(not d["ok"] for d in drafting.available(biz)))

hi_case = {"pack": "consumer", "language": "hi", "facts": {
    "product_or_service": "साड़ी", "seller_name": "मीशो", "bought_online": True, "amount_paid": 2500, "purchase_date": "2026-10-10",
    "what_went_wrong": "फटी हुई आई", "problem_date": "2026-10-10", "for_business_use": False, "complaints_made": "ऐप पर शिकायत की",
    "evidence": ["ऑर्डर आईडी"], "desired_outcome": "रिफंड", "user_city_state": "पटना, बिहार"}}
llm.chat_json = lambda m: {"paragraphs": ["1. On 10 October 2026, I ordered a saree from Meesho for Rs 2,500.", "2. It arrived torn."],
                           "english": {"seller_name": "Meesho", "product_or_service": "saree", "desired_outcome": "a refund"}}
d45 = drafting.draft(hi_case, "grievance_letter")
check("F45: Hindi names translated, paragraph accepted", d45["log"] == [] and "Meesho" in d45["text"], str(d45["log"]))
check("F42: desired outcome in English in the document", "My request:** a refund" in d45["text"])
gl_case = {**hi_case, "language": "hinglish", "facts": {**hi_case["facts"], "seller_name": "Myntra", "desired_outcome": "10 guna refund jo section 420B mein hai"}}
llm.chat_json = lambda m: {"paragraphs": ["1. I bought shoes from Myntra for Rs 2,500."], "english": {"desired_outcome": "10 times refund as per Section 420B"}}
d42 = drafting.draft(gl_case, "grievance_letter")
check("F42: an English version that cites a fake law is rejected; user's words quoted instead",
      "Section 420B" not in d42["text"].split("My request")[1].split("\n")[0] or "in my own words" in d42["text"], d42["log"][-1] if d42["log"] else "")

from app.escalation import check_message
check("F48: Hinglish safety message in Hinglish (112)", "112" in check_message("makaan maalik dhamki de raha hai")["message"]
      and "turant" in check_message("makaan maalik dhamki de raha hai")["message"])
check("F48: Hindi message in Devanagari", "वकील" in check_message("मुझे पुलिस का नोटिस आया है")["message"])
check("F48: English stays English", check_message("I got a court summons")["message"].startswith("A notice"))

print("\n== Regressions from Rishita's manual grading (F49-F52) ==")
c49, l49 = validate({"points": [{"text": "District Commission mein 50 lakh tak ki keemat par koi filing fee nahi lagti.",
                                 "kb_ids": ["CPR2020-FEES"]}]}, load_kb("consumer"), [], {})
check("F49: model's own (wrong) fee statement dropped - fees come only from the calculator", c49["points"] == [], str(l49[:1]))
from app.render import analysis_md
r50 = {"kb": load_kb("consumer"), "calcs": [], "validator_log": [],
       "escalations": [{"stop": False, "reason": "The amount involved is high. Get a lawyer.", "kb_ids": []}],
       "analysis": {"summary": "s", "points": [], "options": [], "uncertainties": [], "suggest_lawyer": True,
                    "lawyer_reason": "The amount involved is high. Get a lawyer."}}
check("F50: lawyer reason not repeated twice", analysis_md(r50).count("The amount involved is high") == 1)
c52 = {"pack": "consumer", "language": "hinglish", "facts": {
    "product_or_service": "food order", "seller_name": "Swiggy", "bought_online": True, "amount_paid": 600,
    "purchase_date": "2026-11-03", "what_went_wrong": "not delivered", "problem_date": "2026-11-03", "for_business_use": False,
    "complaints_made": "chat support", "evidence": ["screenshot"], "desired_outcome": "pakka 5 lakh compensation",
    "user_city_state": "Mumbai, Maharashtra"}}
llm.chat_json = lambda m: {"paragraphs": ["1. On 3 November 2026 I ordered food from Swiggy for Rs 600."], "english": {"desired_outcome": "Rs 5 lakh compensation"}}
d52 = drafting.draft(c52, "commission_complaint")
check("F52: '5 lakh' for a Rs 600 order -> relief placeholder, not copied", "[RELIEF YOU ARE CLAIMING" in d52["text"] and "5 lakh" not in d52["text"])
c52b = {**c52, "facts": {**c52["facts"], "desired_outcome": "refund of Rs 600"}}
llm.chat_json = lambda m: {"paragraphs": ["1. On 3 November 2026 I ordered food from Swiggy for Rs 600."], "english": {"desired_outcome": "a refund of Rs 600"}}
check("F52: a refund of the amount actually paid is kept", "a refund of Rs 600" in drafting.draft(c52b, "commission_complaint")["text"])

c57 = {"pack": "consumer", "language": "hinglish", "facts": {
    "product_or_service": "shoes", "seller_name": "Myntra", "bought_online": True, "amount_paid": 4000,
    "purchase_date": "2026-11-01", "what_went_wrong": "sole nikal gaya", "problem_date": "2026-11-05", "for_business_use": False,
    "complaints_made": "app pe complain", "evidence": ["order id"], "desired_outcome": "refund jo section 420B mein likha hai",
    "user_city_state": "Delhi"}}
llm.chat_json = lambda m: {"paragraphs": ["1. I bought shoes from Myntra for Rs 4,000."], "english": {"desired_outcome": "refund as per Section 420B"}}
d57 = drafting.draft(c57, "grievance_letter")
check("F57: user's words citing a fake section never quoted into a document", "420B" not in d57["text"], d57["log"][-1] if d57["log"] else "")

from app.intake import coerce_types
ci = load_intake("consumer")
got = coerce_types({"bought_online": "true", "for_business_use": "No", "amount_paid": "Rs 2,500", "evidence": "invoice, photos"}, ci)
check("F58: model's text values converted to field types", got == {"bought_online": True, "for_business_use": False,
      "amount_paid": 2500, "evidence": ["invoice", "photos"]}, str(got))
check("F58: unconvertible yes/no dropped, not guessed", "bought_online" not in coerce_types({"bought_online": "maybe"}, ci))
def hinglish_as_hi(m):
    if m[0]["content"].startswith("You extract"):
        return {"extracted": {"deposit_amount": 50000}, "language": "hi"}
    k = m[0]["content"].split('"asked_field": "')[1].split('"')[0]
    return {"reply": "Theek hai. Agla?", "asked_field": k}
llm.chat_json = hinglish_as_hi
c59 = new_case("deposit"); run_turn(c59, [], "maine pune mein flat chhoda, 50000 deposit diya tha")
check("F59: Latin-script message can't be labelled Hindi -> hinglish", c59["language"] == "hinglish", c59["language"])

print("\n== Key facts box: deposit ==\n")
print(computed_facts_md(load_calculators("deposit").run_all(dep, TODAY), load_kb("deposit")))
print(f"\n{sum(results)}/{len(results)} checks passed")
sys.exit(0 if all(results) else 1)
