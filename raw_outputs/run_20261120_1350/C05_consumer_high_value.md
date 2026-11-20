# C05_consumer_high_value
**Category:** edge-high-value  
**Description:** Rs 12 lakh car repair dispute - above our Rs 10 lakh threshold -> recommend a lawyer; fee Rs 400.  
**Pack:** consumer  
**Run at:** 2026-11-20T13:55:18  
**Models that answered:** gemini-3.5-flash-lite (12 calls)  
**Time:** 42.8 s

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

**Bot:** I understand you are facing issues with your car engine and the dealer's refusal to replace it. On what date did the problem happen, or the refund become due? (You mentioned: 2026-11-01 - is that right?)

**User:** 1 November 2026

**Bot:** Got it. Did you buy this for your own personal use, or to resell / use in a business? (You mentioned: no - is that right?)

**User:** personal car

**Bot:** I understand you are facing an issue with your personal car. What proof do you have? (invoice/bill, order ID, payment screenshot, emails, chats, photos, warranty card)

**User:** invoice, service record, emails

**Bot:** Thank you for sharing those documents with me. What would you like - refund, replacement, repair, or compensation? (You mentioned: replacement - is that right?)

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

You bought a new car that developed a major engine failure shortly after purchase, and the dealer is refusing to replace it. Because you bought it for personal use, you are treated as a consumer and can seek legal remedy.

- Since you bought the car for personal use and not for resale or commercial purposes, you are considered a consumer under the law.<br><small>📘 **Consumer Protection Act, 2019, s. 2(7)**: Who is a "consumer" — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)</small>

- A serious engine failure within months of purchase is considered a defect in the goods.<br><small>📘 **Consumer Protection Act, 2019, s. 2(10)**: What is a "defect" (goods) — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)</small>

- Refusing to take back or replace defective goods as promised can also be treated as an unfair trade practice.<br><small>📘 **Consumer Protection Act, 2019, s. 2(47)**: What is an "unfair trade practice" — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)</small>

- You are well within the two-year time limit to file a consumer complaint regarding this issue.<br><small>📘 **Consumer Protection Act, 2019, s. 69**: Time limit for filing a complaint — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)</small>

#### Key facts (calculated by the app, not the AI)

⏳ **Time limit:** ✅ within the limit. Normally file by **2028-11-01** (2 years from 2026-11-01; dates are approximate).

🏛️ **Which Commission:** District Consumer Commission, for Rs 12,00,000 paid (you can file where you live or work: Bengaluru, Karnataka).

💰 **Filing fee:** Rs 400.

<small>Based on: 📘 **Consumer Protection Act, 2019, s. 34**: District Commission - which one you can file in — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19); 📘 **Consumer Protection Act, 2019, s. 69**: Time limit for filing a complaint — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19); 📘 **Consumer Protection (Consumer Disputes Redressal Commissions) Rules, 2020, Rule 7 (fee table)**: Fee for filing a consumer complaint — [source](https://egazette.gov.in/WriteReadData/2023/248158.pdf) (✅ verified 2026-11-19); 📘 **Consumer Protection (Jurisdiction of the District Commission, the State Commission and the National Commission) Rules, 2021, Rules 3-5**: Money limits - which Commission — [source](https://www.pib.gov.in/PressReleasePage.aspx?PRID=1786342) (✅ verified 2026-11-19)</small>

### Your options

**1. Contact National Consumer Helpline** — This is a pre-litigation step where an attempt is made to resolve the grievance without going to court.
   - Call the helpline or use their web portal, app, or WhatsApp to register your grievance.
   - Provide details of your purchase, the vehicle defect, and your communications with the dealer.

   <small>📘 **National Consumer Helpline (consumerhelpline.gov.in), Contact page and FAQ**: National Consumer Helpline (pre-litigation step) — [source](https://consumerhelpline.gov.in/) (✅ verified 2026-11-19)</small>

**2. File a formal complaint at the District Consumer Commission** — You can ask the Commission to order a replacement of the car, a refund, or compensation for your loss.
   - Prepare your complaint with supporting evidence like your invoice, service records, and emails.
   - File the complaint online through the official consumer portal, paying the required filing fee.
   - You can file where you live or where the dealer carries on business.

   <small>📘 **Consumer Protection Act, 2019, s. 34**: District Commission - which one you can file in — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)<br>📘 **Consumer Protection Act, 2019, s. 35**: How a complaint is filed — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)<br>📘 **Consumer Protection Act, 2019, s. 39**: What the Commission can order — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)<br>📘 **Consumer Protection (Jurisdiction of the District Commission, the State Commission and the National Commission) Rules, 2021, Rules 3-5**: Money limits - which Commission — [source](https://www.pib.gov.in/PressReleasePage.aspx?PRID=1786342) (✅ verified 2026-11-19)<br>📘 **Consumer Protection (Consumer Disputes Redressal Commissions) Rules, 2020, Rule 7 (fee table)**: Fee for filing a consumer complaint — [source](https://egazette.gov.in/WriteReadData/2023/248158.pdf) (✅ verified 2026-11-19)<br>📘 **e-Jagriti (Department of Consumer Affairs)**: File online on e-Jagriti — [source](https://e-jagriti.gov.in/) (✅ verified 2026-11-19)</small>

**3. Seek free legal aid** — Depending on your category or income level, you may be eligible for free legal assistance to help draft and manage your case.
   - Check if you qualify under the legal services criteria (such as category or income limits).
   - Reach out to your local District Legal Services Authority in person, by post, online, or via their helpline.

   <small>📘 **Legal Services Authorities Act, 1987, s. 12**: Who can get free legal aid — [source](https://indiacode.gov.in/act/a742f03e-3129-4b8d-8dda-af2a36190b18/sections?spc.sf=dc.date.issued&spc.sd=DESC&spc.page=2&spc.rpp=10) (✅ verified 2026-11-19)<br>📘 **National Legal Services Authority**: How to reach free legal aid — [source](https://nalsa.gov.in/legal-aid/#Free-Legal-Aid) (✅ verified 2026-11-19)</small>

### ⚖️ When to get a real lawyer
- The amount involved is high. For a claim this size, a lawyer's help is strongly recommended.
- The amount involved is high. For a claim this size, a lawyer's help is strongly recommended.
- Free legal help may be available: District Legal Services Authority / NALSA helpline **15100**.

### What I'm not sure about
- We could not independently verify the mechanical condition of the car or whether proper maintenance was followed after purchase, which the dealer may raise in defense.

---
<small>Knowledge base last verified: 2026-11-19. Only verified sources are cited. This is general information, not legal advice.</small>

## Safety checker log (items removed from the AI's draft)
```json
[]
```

## Raw model JSON for the answer (before the safety checker)
```json
{
 "summary": "You bought a new car that developed a major engine failure shortly after purchase, and the dealer is refusing to replace it. Because you bought it for personal use, you are treated as a consumer and can seek legal remedy.",
 "points": [
  {
   "text": "Since you bought the car for personal use and not for resale or commercial purposes, you are considered a consumer under the law.",
   "kb_ids": [
    "CPA2019-S2-7"
   ]
  },
  {
   "text": "A serious engine failure within months of purchase is considered a defect in the goods.",
   "kb_ids": [
    "CPA2019-S2-10"
   ]
  },
  {
   "text": "Refusing to take back or replace defective goods as promised can also be treated as an unfair trade practice.",
   "kb_ids": [
    "CPA2019-S2-47"
   ]
  },
  {
   "text": "You are well within the two-year time limit to file a consumer complaint regarding this issue.",
   "kb_ids": [
    "CPA2019-S69"
   ]
  }
 ],
 "options": [
  {
   "title": "Contact National Consumer Helpline",
   "why": "This is a pre-litigation step where an attempt is made to resolve the grievance without going to court.",
   "steps": [
    "Call the helpline or use their web portal, app, or WhatsApp to register your grievance.",
    "Provide details of your purchase, the vehicle defect, and your communications with the dealer."
   ],
   "kb_ids": [
    "PROC-NCH"
   ]
  },
  {
   "title": "File a formal complaint at the District Consumer Commission",
   "why": "You can ask the Commission to order a replacement of the car, a refund, or compensation for your loss.",
   "steps": [
    "Prepare your complaint with supporting evidence like your invoice, service records, and emails.",
    "File the complaint online through the official consumer portal, paying the required filing fee.",
    "You can file where you live or where the dealer carries on business."
   ],
   "kb_ids": [
    "CPA2019-S34",
    "CPA2019-S35",
    "CPA2019-S39",
    "CPR2021-PECUNIARY",
    "CPR2020-FEES",
    "PROC-EJAGRITI"
   ]
  },
  {
   "title": "Seek free legal aid",
   "why": "Depending on your category or income level, you may be eligible for free legal assistance to help draft and manage your case.",
   "steps": [
    "Check if you qualify under the legal services criteria (such as category or income limits).",
    "Reach out to your local District Legal Services Authority in person, by post, online, or via their helpline."
   ],
   "kb_ids": [
    "LSA1987-S12",
    "PROC-NALSA"
   ]
  }
 ],
 "uncertainties": [
  "We could not independently verify the mechanical condition of the car or whether proper maintenance was followed after purchase, which the dealer may raise in defense."
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

1. I purchased a New car from the Authorised car dealer on 5 September 2026 for Rs 12,00,000.

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