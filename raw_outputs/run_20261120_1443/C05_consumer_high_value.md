# C05_consumer_high_value
**Category:** edge-high-value  
**Description:** Rs 12 lakh car repair dispute - above our Rs 10 lakh threshold -> recommend a lawyer; fee Rs 400.  
**Pack:** consumer  
**Run at:** 2026-11-20T14:48:34  
**Models that answered:** gemini-3.5-flash-lite, openai/gpt-oss-120b (12 calls)  
**Time:** 61.9 s

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

**Bot:** I understand you are facing an issue with your car dealer regarding a failed engine. Did you buy this for your own personal use, or to resell / use in a business?

**User:** personal car

**Bot:** I understand you are referring to a personal car. On what date did the problem happen, or the refund become due? (You mentioned: 2026-11-01 - is that right?)

**User:** 1 November 2026

**Bot:** I note the date you mentioned. What proof do you have? (invoice/bill, order ID, payment screenshot, emails, chats, photos, warranty card)

**User:** invoice, service record, emails

**Bot:** I see you have provided the invoice, service record, and emails. What would you like - refund, replacement, repair, or compensation? (You mentioned: replacement - is that right?)

**User:** replacement of the car

**Bot:** Thank you, I now have the key facts of your case.

## Case file (final)
```json
{
 "pack": "consumer",
 "facts": {
  "product_or_service": "new car",
  "seller_name": "authorised car dealer",
  "for_business_use": false,
  "bought_online": false,
  "amount_paid": 1200000,
  "purchase_date": "2026-09-05",
  "what_went_wrong": "The engine failed and the dealer refuses to replace it.",
  "problem_date": "2026-11-01",
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
  "personal car",
  "1 November 2026",
  "invoice, service record, emails",
  "replacement of the car"
 ],
 "suggested": {
  "for_business_use": false,
  "problem_date": "2026-11-01",
  "desired_outcome": "replacement"
 }
}
```

## Answer shown to the user

### Where you stand

You bought a car for personal use, making you a consumer under the law. Because the engine failed and the dealer refuses to replace it, you can seek relief before the consumer forum.

- Because you bought the car for personal use and not for a commercial purpose, you qualify as a consumer.<br><small>📘 **Consumer Protection Act, 2019, s. 2(7)**: Who is a "consumer" — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)</small>

- A fault or imperfection in the quality or standard of goods is considered a defect, which applies when a product is faulty.<br><small>📘 **Consumer Protection Act, 2019, s. 2(10)**: What is a "defect" (goods) — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)</small>

- Refusing to take back defective goods or provide a refund or replacement can be treated as an unfair trade practice.<br><small>📘 **Consumer Protection Act, 2019, s. 2(47)**: What is an "unfair trade practice" — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)</small>

- If the District Commission finds your complaint proved, it can order the opposite party to replace the goods, refund the price, or pay compensation for loss.<br><small>📘 **Consumer Protection Act, 2019, s. 39**: What the Commission can order — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)</small>

#### Key facts (calculated by the app, not the AI)

⏳ **Time limit:** ✅ within the limit. Normally file by **2028-11-01** (2 years from 2026-11-01; dates are approximate).

🏛️ **Which Commission:** District Consumer Commission, for Rs 12,00,000 paid (you can file where you live or work: Bengaluru, Karnataka).

💰 **Filing fee:** Rs 400.

<small>Based on: 📘 **Consumer Protection Act, 2019, s. 34**: District Commission - which one you can file in — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19); 📘 **Consumer Protection Act, 2019, s. 69**: Time limit for filing a complaint — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19); 📘 **Consumer Protection (Consumer Disputes Redressal Commissions) Rules, 2020, Rule 7 (fee table)**: Fee for filing a consumer complaint — [source](https://egazette.gov.in/WriteReadData/2023/248158.pdf) (✅ verified 2026-11-19); 📘 **Consumer Protection (Jurisdiction of the District Commission, the State Commission and the National Commission) Rules, 2021, Rules 3-5**: Money limits - which Commission — [source](https://www.pib.gov.in/PressReleasePage.aspx?PRID=1786342) (✅ verified 2026-11-19)</small>

### Your options

**1. Use the National Consumer Helpline** — This is a pre-litigation step where an attempt can be made to resolve the grievance before going to court.
   - Contact the National Consumer Helpline by phone, app, or portal.
   - Register your grievance with your invoice and details.
   - Wait for them to take it up with the dealer.

   <small>📘 **National Consumer Helpline (consumerhelpline.gov.in), Contact page and FAQ**: National Consumer Helpline (pre-litigation step) — [source](https://consumerhelpline.gov.in/) (✅ verified 2026-11-19)</small>

**2. File a formal consumer complaint online** — You can formally approach the appropriate Commission to seek a replacement or compensation.
   - Prepare your complaint along with your invoice, service record, and emails.
   - Access the online portal for filing consumer complaints.
   - Pay the required filing fee and submit your complaint.

   <small>📘 **Consumer Protection Act, 2019, s. 35**: How a complaint is filed — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)<br>📘 **e-Jagriti (Department of Consumer Affairs)**: File online on e-Jagriti — [source](https://e-jagriti.gov.in/) (✅ verified 2026-11-19)</small>

**3. Seek free legal aid** — Depending on your eligibility (such as category or income limits), you may be able to get free legal help.
   - Check if you qualify under the legal aid categories or income limits.
   - Reach out to the District Legal Services Authority with your identity proof.

   <small>📘 **Legal Services Authorities Act, 1987, s. 12**: Who can get free legal aid — [source](https://indiacode.gov.in/act/a742f03e-3129-4b8d-8dda-af2a36190b18/sections?spc.sf=dc.date.issued&spc.sd=DESC&spc.page=2&spc.rpp=10) (✅ verified 2026-11-19)<br>📘 **National Legal Services Authority**: How to reach free legal aid — [source](https://nalsa.gov.in/legal-aid/#Free-Legal-Aid) (✅ verified 2026-11-19)</small>

### ⚖️ When to get a real lawyer
- The amount involved is high. For a claim this size, a lawyer's help is strongly recommended.
- The amount involved is high. For a claim this size, a lawyer's help is strongly recommended.
- Free legal help may be available: District Legal Services Authority / NALSA helpline **15100**.

### What I'm not sure about
- Whether the dealer can prove the engine failure was caused by improper use or outside damage rather than an inherent manufacturing defect.

---
<small>Knowledge base last verified: 2026-11-19. Only verified sources are cited. This is general information, not legal advice.</small>

## Safety checker log (items removed from the AI's draft)
```json
[]
```

## Raw model JSON for the answer (before the safety checker)
```json
{
 "summary": "You bought a car for personal use, making you a consumer under the law. Because the engine failed and the dealer refuses to replace it, you can seek relief before the consumer forum.",
 "points": [
  {
   "text": "Because you bought the car for personal use and not for a commercial purpose, you qualify as a consumer.",
   "kb_ids": [
    "CPA2019-S2-7"
   ]
  },
  {
   "text": "A fault or imperfection in the quality or standard of goods is considered a defect, which applies when a product is faulty.",
   "kb_ids": [
    "CPA2019-S2-10"
   ]
  },
  {
   "text": "Refusing to take back defective goods or provide a refund or replacement can be treated as an unfair trade practice.",
   "kb_ids": [
    "CPA2019-S2-47"
   ]
  },
  {
   "text": "If the District Commission finds your complaint proved, it can order the opposite party to replace the goods, refund the price, or pay compensation for loss.",
   "kb_ids": [
    "CPA2019-S39"
   ]
  }
 ],
 "options": [
  {
   "title": "Use the National Consumer Helpline",
   "why": "This is a pre-litigation step where an attempt can be made to resolve the grievance before going to court.",
   "steps": [
    "Contact the National Consumer Helpline by phone, app, or portal.",
    "Register your grievance with your invoice and details.",
    "Wait for them to take it up with the dealer."
   ],
   "kb_ids": [
    "PROC-NCH"
   ]
  },
  {
   "title": "File a formal consumer complaint online",
   "why": "You can formally approach the appropriate Commission to seek a replacement or compensation.",
   "steps": [
    "Prepare your complaint along with your invoice, service record, and emails.",
    "Access the online portal for filing consumer complaints.",
    "Pay the required filing fee and submit your complaint."
   ],
   "kb_ids": [
    "CPA2019-S35",
    "PROC-EJAGRITI"
   ]
  },
  {
   "title": "Seek free legal aid",
   "why": "Depending on your eligibility (such as category or income limits), you may be able to get free legal help.",
   "steps": [
    "Check if you qualify under the legal aid categories or income limits.",
    "Reach out to the District Legal Services Authority with your identity proof."
   ],
   "kb_ids": [
    "LSA1987-S12",
    "PROC-NALSA"
   ]
  }
 ],
 "uncertainties": [
  "Whether the dealer can prove the engine failure was caused by improper use or outside damage rather than an inherent manufacturing defect."
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

1. I purchased a New car from Authorised car dealer on 5 September 2026 for Rs 12,00,000.

2. I am not using the car for business purposes.

3. On 1 November 2026 the engine failed.

4. I complained to the dealer, but they refuse to replace it.

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