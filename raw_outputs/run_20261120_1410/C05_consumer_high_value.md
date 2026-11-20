# C05_consumer_high_value
**Category:** edge-high-value  
**Description:** Rs 12 lakh car repair dispute - above our Rs 10 lakh threshold -> recommend a lawyer; fee Rs 400.  
**Pack:** consumer  
**Run at:** 2026-11-20T14:14:42  
**Models that answered:** gemini-3.5-flash-lite (12 calls)  
**Time:** 49.6 s

> Unedited output of scripts/run_tests.py. Nothing below was changed by hand.

## Automatic checks
| Check | Result | Detail |
|---|---|---|
| escalation | PASS | expected none, got none |
| lawyer flag | PASS | expected True, got True |
| language | PASS | expected en, got en |

## Conversation
**Bot:** Tell me what happened, in your own words - English, Hindi or Hinglish is fine. For example: what you bought, from whom, and what went wrong.

**User:** I paid Rs 12,00,000 to an authorised car dealer in Bengaluru for a new car on 5 September 2026. The engine failed on 1 November 2026 and they refuse to replace it.

**Bot:** I understand you are facing issues with your car and the dealer refusing a replacement. On what date did the problem happen, or the refund become due? (You mentioned: 2026-11-01 - is that right?)

**User:** 1 November 2026

**Bot:** I have noted that date. Did you buy this for your own personal use, or to resell / use in a business?

**User:** personal car

**Bot:** I understand you are dealing with an issue regarding your personal car. What proof do you have? (invoice/bill, order ID, payment screenshot, emails, chats, photos, warranty card)

**User:** invoice, service record, emails

**Bot:** You have shared your invoice, service record, and emails. What would you like - refund, replacement, repair, or compensation? (You mentioned: replacement - is that right?)

**User:** replacement of the car

**Bot:** I understand you are looking for a replacement for your car.

## Case file (final)
```json
{
 "pack": "consumer",
 "facts": {
  "product_or_service": "new car",
  "seller_name": "authorised car dealer",
  "bought_online": false,
  "amount_paid": 1200000,
  "purchase_date": "2026-09-05",
  "what_went_wrong": "The engine failed and they refuse to replace it.",
  "problem_date": "2026-11-01",
  "for_business_use": false,
  "complaints_made": "Complained to the dealer, but they refuse to replace it.",
  "evidence": [
   "invoice",
   "service record",
   "emails"
  ],
  "desired_outcome": "replacement of the car",
  "user_city_state": "Bengaluru, Karnataka"
 },
 "language": "en",
 "user_messages": [
  "I paid Rs 12,00,000 to an authorised car dealer in Bengaluru for a new car on 5 September 2026. The engine failed on 1 November 2026 and they refuse to replace it.",
  "1 November 2026",
  "personal car",
  "invoice, service record, emails",
  "replacement of the car"
 ],
 "suggested": {
  "problem_date": "2026-11-01",
  "for_business_use": false,
  "desired_outcome": "replacement"
 }
}
```

## Answer shown to the user

### Where you stand

Since you bought the car for personal use and the engine failed, you are considered a consumer. You can file a complaint before the consumer commission against the car dealer, and you are well within the allowed time limit to do so.

- You qualify as a consumer because you bought the car for personal use, and a serious engine failure means the product has a defect.<br><small>📘 **Consumer Protection Act, 2019, s. 2(7)**: Who is a "consumer" — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)<br>📘 **Consumer Protection Act, 2019, s. 2(10)**: What is a "defect" (goods) — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)</small>

- If the seller refuses to take back or replace defective goods when promised or expected, it can also be treated as an unfair trade practice.<br><small>📘 **Consumer Protection Act, 2019, s. 2(47)**: What is an "unfair trade practice" — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)</small>

- You can file your consumer complaint where the dealer carries on business or has a branch office, or where you yourself live or work.<br><small>📘 **Consumer Protection Act, 2019, s. 34**: District Commission - which one you can file in — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)</small>

- If the consumer commission accepts your complaint, it can order the opposite party to replace the goods, refund the price, pay compensation for loss or injury, or cover your costs, though nothing is ever [removed: nobody can promise a legal outcome].<br><small>📘 **Consumer Protection Act, 2019, s. 39**: What the Commission can order — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)</small>

#### Key facts (calculated by the app, not the AI)

⏳ **Time limit:** ✅ within the limit. Normally file by **2028-11-01** (2 years from 2026-11-01; dates are approximate).

🏛️ **Which Commission:** District Consumer Commission, for Rs 12,00,000 paid (you can file where you live or work: Bengaluru, Karnataka).

💰 **Filing fee:** Rs 400.

<small>Based on: 📘 **Consumer Protection Act, 2019, s. 34**: District Commission - which one you can file in — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19); 📘 **Consumer Protection Act, 2019, s. 69**: Time limit for filing a complaint — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19); 📘 **Consumer Protection (Consumer Disputes Redressal Commissions) Rules, 2020, Rule 7 (fee table)**: Fee for filing a consumer complaint — [source](https://egazette.gov.in/WriteReadData/2023/248158.pdf) (✅ verified 2026-11-19); 📘 **Consumer Protection (Jurisdiction of the District Commission, the State Commission and the National Commission) Rules, 2021, Rules 3-5**: Money limits - which Commission — [source](https://www.pib.gov.in/PressReleasePage.aspx?PRID=1786342) (✅ verified 2026-11-19)</small>

### Your options

**1. Use the National Consumer Helpline** — This is a pre-litigation step where you can register your grievance before going to the Commission.
   - Call the helpline or use their web portal, app, or WhatsApp to register your complaint.
   - Provide your invoice, service records, and emails as details.

   <small>📘 **National Consumer Helpline (consumerhelpline.gov.in), Contact page and FAQ**: National Consumer Helpline (pre-litigation step) — [source](https://consumerhelpline.gov.in/) (✅ verified 2026-11-19)</small>

**2. File a formal consumer complaint online** — You can file your complaint digitally through the official portal for consumer disputes.
   - Prepare your documents including the invoice, service record, and emails.
   - Submit your complaint on the e-Jagriti portal along with the required fee.

   <small>📘 **Consumer Protection Act, 2019, s. 35**: How a complaint is filed — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)<br>📘 **e-Jagriti (Department of Consumer Affairs)**: File online on e-Jagriti — [source](https://e-jagriti.gov.in/) (✅ verified 2026-11-19)<br>📘 **Consumer Protection (Consumer Disputes Redressal Commissions) Rules, 2020, Rule 7 (fee table)**: Fee for filing a consumer complaint — [source](https://egazette.gov.in/WriteReadData/2023/248158.pdf) (✅ verified 2026-11-19)</small>

**3. Seek free legal aid** — If you meet the eligibility criteria under the law, you can get free legal assistance from the legal services authorities.
   - Contact the District Legal Services Authority at the district court or check their online website.
   - Submit a written application or call their helpline for guidance.

   <small>📘 **Legal Services Authorities Act, 1987, s. 12**: Who can get free legal aid — [source](https://indiacode.gov.in/act/a742f03e-3129-4b8d-8dda-af2a36190b18/sections?spc.sf=dc.date.issued&spc.sd=DESC&spc.page=2&spc.rpp=10) (✅ verified 2026-11-19)<br>📘 **National Legal Services Authority**: How to reach free legal aid — [source](https://nalsa.gov.in/legal-aid/#Free-Legal-Aid) (✅ verified 2026-11-19)</small>

### ⚖️ When to get a real lawyer
- The amount involved is high. For a claim this size, a lawyer's help is strongly recommended.
- The amount involved is high. For a claim this size, a lawyer's help is strongly recommended.
- Free legal help may be available: District Legal Services Authority / NALSA helpline **15100**.

### What I'm not sure about
- Whether the dealer's specific warranty terms or service history records contain any clauses that affect your claim.
- Whether any specific technical inspection reports might be required by the commission to prove the engine failure.

---
<small>Knowledge base last verified: 2026-11-19. Only verified sources are cited. The safety checker removed 1 unverified item(s) from the AI's draft. This is general information, not legal advice.</small>

## Safety checker log (items removed from the AI's draft)
```json
[
 {
  "type": "promised_outcome",
  "text": "guaranteed"
 }
]
```

## Raw model JSON for the answer (before the safety checker)
```json
{
 "summary": "Since you bought the car for personal use and the engine failed, you are considered a consumer. You can file a complaint before the consumer commission against the car dealer, and you are well within the allowed time limit to do so.",
 "points": [
  {
   "text": "You qualify as a consumer because you bought the car for personal use, and a serious engine failure means the product has a defect.",
   "kb_ids": [
    "CPA2019-S2-7",
    "CPA2019-S2-10"
   ]
  },
  {
   "text": "If the seller refuses to take back or replace defective goods when promised or expected, it can also be treated as an unfair trade practice.",
   "kb_ids": [
    "CPA2019-S2-47"
   ]
  },
  {
   "text": "You can file your consumer complaint where the dealer carries on business or has a branch office, or where you yourself live or work.",
   "kb_ids": [
    "CPA2019-S34"
   ]
  },
  {
   "text": "If the consumer commission accepts your complaint, it can order the opposite party to replace the goods, refund the price, pay compensation for loss or injury, or cover your costs, though nothing is ever guaranteed.",
   "kb_ids": [
    "CPA2019-S39"
   ]
  }
 ],
 "options": [
  {
   "title": "Use the National Consumer Helpline",
   "why": "This is a pre-litigation step where you can register your grievance before going to the Commission.",
   "steps": [
    "Call the helpline or use their web portal, app, or WhatsApp to register your complaint.",
    "Provide your invoice, service records, and emails as details."
   ],
   "kb_ids": [
    "PROC-NCH"
   ]
  },
  {
   "title": "File a formal consumer complaint online",
   "why": "You can file your complaint digitally through the official portal for consumer disputes.",
   "steps": [
    "Prepare your documents including the invoice, service record, and emails.",
    "Submit your complaint on the e-Jagriti portal along with the required fee."
   ],
   "kb_ids": [
    "CPA2019-S35",
    "PROC-EJAGRITI",
    "CPR2020-FEES"
   ]
  },
  {
   "title": "Seek free legal aid",
   "why": "If you meet the eligibility criteria under the law, you can get free legal assistance from the legal services authorities.",
   "steps": [
    "Contact the District Legal Services Authority at the district court or check their online website.",
    "Submit a written application or call their helpline for guidance."
   ],
   "kb_ids": [
    "LSA1987-S12",
    "PROC-NALSA"
   ]
  }
 ],
 "uncertainties": [
  "Whether the dealer's specific warranty terms or service history records contain any clauses that affect your claim.",
  "Whether any specific technical inspection reports might be required by the commission to prove the engine failure."
 ],
 "suggest_lawyer": true,
 "lawyer_reason": "The amount involved is high. For a claim this size, a lawyer's help is strongly recommended."
}
```

## Document: commission_complaint
Offered: yes
Drafting log: AI paragraph accepted

```text
**BEFORE THE DISTRICT CONSUMER DISPUTES REDRESSAL COMMISSION, [DISTRICT NAME], KARNATAKA**

Consumer Complaint No. ______ of ______ (to be filled by the Commission)

**Complainant:**
[YOUR FULL NAME], [YOUR FULL ADDRESS], Bengaluru, Karnataka

**Versus**

**Opposite Party:**
Authorised car dealer, [OPPOSITE PARTY'S REGISTERED ADDRESS – see your invoice or the website's legal/contact page]

---

**COMPLAINT**

**1. Facts of the case**

1. On 5 September 2026, I purchased a new car from the authorised car dealer for the amount of Rs 12,00,000.

2. On 1 November 2026, the engine failed.

3. I complained to the dealer, but they refuse to replace it.

**2. Jurisdiction**

(a) The value of the goods/services paid as consideration is Rs 12,00,000, which is within the limit of this Commission (Rules 3-5 of the Consumer Protection (Jurisdiction of the District Commission, the State Commission and the National Commission) Rules, 2021).

(b) The Complainant resides/personally works for gain at Bengaluru, Karnataka, within the area of this Commission (Section 34 of the Consumer Protection Act, 2019).

**3. Limitation**

The cause of action arose on or about 1 November 2026. This complaint is filed within the period allowed (Section 69 of the Consumer Protection Act, 2019).

**4. Relief sought**

The Complainant respectfully requests this Commission to direct the Opposite Party to:
(a) grant the following relief: replacement of the car;
(b) pay such compensation and costs as this Commission considers just (Section 39 of the Consumer Protection Act, 2019).

**5. List of documents**

1. invoice
2. service record
3. emails

**Verification**

I, [YOUR FULL NAME], the Complainant, state that the contents of this complaint are true and correct to the best of my knowledge and belief, and nothing material has been concealed.

Place: [PLACE]
Date: [DATE]

[SIGNATURE OF COMPLAINANT]

```