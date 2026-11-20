# C02_consumer_english_shop
**Category:** normal  
**Description:** Washing machine from a local shop, English; no e-commerce letter should be offered.  
**Pack:** consumer  
**Run at:** 2026-11-20T14:46:07  
**Models that answered:** gemini-3.5-flash-lite (12 calls)  
**Time:** 52.9 s

> Unedited output of scripts/run_tests.py. Nothing below was changed by hand.

## Automatic checks
| Check | Result | Detail |
|---|---|---|
| escalation | PASS | expected none, got none |
| language | PASS | expected en, got en |
| document grievance_letter | PASS | expected locked/absent, got locked/absent |
| document commission_complaint | PASS | expected unlocked, got unlocked |

## Conversation
**Bot:** Tell me what happened, in your own words - English, Hindi or Hinglish is fine. For example: what you bought, from whom, and what went wrong.

**User:** I bought a washing machine for Rs 32,000 from Sharma Electronics, a shop in Jaipur, on 2 August 2026. It started leaking on 20 October 2026. The shop refuses to repair or replace it.

**Bot:** I understand you are facing an issue with a washing machine you purchased from a shop in Jaipur that is now leaking and not being repaired or replaced. Did you buy this for your own personal use, or to resell / use in a business?

**User:** for my family at home

**Bot:** I understand you are facing this issue regarding your family at home. On what date did the problem happen, or the refund become due? (You mentioned: 2026-10-20 - is that right?)

**User:** 20 October 2026

**Bot:** Noted. What proof do you have? (invoice/bill, order ID, payment screenshot, emails, chats, photos, warranty card)

**User:** the bill, warranty card and photos of the leak

**Bot:** Got it, thank you for sharing those documents. What would you like - refund, replacement, repair, or compensation? (You mentioned: repair or replacement - is that right?)

**User:** replacement

**Bot:** I understand you are dealing with a replacement issue.

## Case file (final)
```json
{
 "pack": "consumer",
 "facts": {
  "product_or_service": "washing machine",
  "seller_name": "Sharma Electronics",
  "for_business_use": false,
  "bought_online": false,
  "amount_paid": 32000,
  "purchase_date": "2026-08-02",
  "what_went_wrong": "It started leaking and the shop refuses to repair or replace it.",
  "problem_date": "2026-10-20",
  "complaints_made": "Complained to the shop, but they refuse to repair or replace it.",
  "evidence": [
   "bill",
   "warranty card",
   "photos of the leak"
  ],
  "desired_outcome": "replacement",
  "user_city_state": "Jaipur"
 },
 "language": "en",
 "user_messages": [
  "I bought a washing machine for Rs 32,000 from Sharma Electronics, a shop in Jaipur, on 2 August 2026. It started leaking on 20 October 2026. The shop refuses to repair or replace it.",
  "for my family at home",
  "20 October 2026",
  "the bill, warranty card and photos of the leak",
  "replacement"
 ],
 "suggested": {
  "problem_date": "2026-10-20",
  "desired_outcome": "repair or replacement"
 }
}
```

## Answer shown to the user

### Where you stand

You are a consumer since you bought the washing machine for your family home, and because the seller is refusing to repair or replace a faulty product, you have a valid basis to seek relief. You are well within the time limit to take legal action.

- Because you purchased the washing machine for personal use rather than for resale or commercial purposes, you qualify as a consumer.<br><small>📘 **Consumer Protection Act, 2019, s. 2(7)**: Who is a "consumer" — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)</small>

- The issue you are facing with the leaking machine counts as a product defect because it is a fault or shortcoming in quality.<br><small>📘 **Consumer Protection Act, 2019, s. 2(10)**: What is a "defect" (goods) — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)</small>

- Refusing to take back or fix a defective item when it is pointed out can be treated as an unfair trade practice.<br><small>📘 **Consumer Protection Act, 2019, s. 2(47)**: What is an "unfair trade practice" — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)</small>

- If you decide to approach the consumer forum, you can ask for remedies such as a replacement of the machine, a refund of the price, or compensation for the trouble caused.<br><small>📘 **Consumer Protection Act, 2019, s. 39**: What the Commission can order — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)</small>

#### Key facts (calculated by the app, not the AI)

⏳ **Time limit:** ✅ within the limit. Normally file by **2028-10-20** (2 years from 2026-10-20; dates are approximate).

🏛️ **Which Commission:** District Consumer Commission, for Rs 32,000 paid (you can file where you live or work: Jaipur).

💰 **Filing fee:** nil (no fee).

<small>Based on: 📘 **Consumer Protection Act, 2019, s. 34**: District Commission - which one you can file in — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19); 📘 **Consumer Protection Act, 2019, s. 69**: Time limit for filing a complaint — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19); 📘 **Consumer Protection (Consumer Disputes Redressal Commissions) Rules, 2020, Rule 7 (fee table)**: Fee for filing a consumer complaint — [source](https://egazette.gov.in/WriteReadData/2023/248158.pdf) (✅ verified 2026-11-19); 📘 **Consumer Protection (Jurisdiction of the District Commission, the State Commission and the National Commission) Rules, 2021, Rules 3-5**: Money limits - which Commission — [source](https://www.pib.gov.in/PressReleasePage.aspx?PRID=1786342) (✅ verified 2026-11-19)</small>

### Your options

**1. Contact the National Consumer Helpline** — This is a pre-litigation step where helpline staff attempt to resolve your grievance with the seller before you file a formal case.
   - Call the helpline or use their web portal, app, or WhatsApp to register your complaint.
   - Provide your purchase details, bill, and description of the leak.
   - Wait for their intervention to see if the seller agrees to a resolution.

   <small>📘 **National Consumer Helpline (consumerhelpline.gov.in), Contact page and FAQ**: National Consumer Helpline (pre-litigation step) — [source](https://consumerhelpline.gov.in/) (✅ verified 2026-11-19)</small>

**2. File a formal consumer complaint online** — You can file a case in the relevant consumer commission since the seller refused to help.
   - Prepare your documents, including the purchase bill, warranty card, and photos of the leak.
   - File your complaint electronically on the official e-Jagriti portal.
   - Pay any applicable fee if required, though online filing guides you through the process.

   <small>📘 **Consumer Protection Act, 2019, s. 35**: How a complaint is filed — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)<br>📘 **e-Jagriti (Department of Consumer Affairs)**: File online on e-Jagriti — [source](https://e-jagriti.gov.in/) (✅ verified 2026-11-19)<br>📘 **Consumer Protection (Consumer Disputes Redressal Commissions) Rules, 2020, Rule 7 (fee table)**: Fee for filing a consumer complaint — [source](https://egazette.gov.in/WriteReadData/2023/248158.pdf) (✅ verified 2026-11-19)</small>

**3. Seek free legal aid** — If you need professional guidance with drafting your complaint or understanding the process and happen to qualify under certain categories, you can access free legal services.
   - Check if you qualify under categories such as being a woman, having a low annual income, or belonging to a specific reserved category.
   - Reach out to your local District Legal Services Authority in person, by post, or through their helpline (15100).
   - Submit a simple written application with your identity proof.

   <small>📘 **Legal Services Authorities Act, 1987, s. 12**: Who can get free legal aid — [source](https://indiacode.gov.in/act/a742f03e-3129-4b8d-8dda-af2a36190b18/sections?spc.sf=dc.date.issued&spc.sd=DESC&spc.page=2&spc.rpp=10) (✅ verified 2026-11-19)<br>📘 **National Legal Services Authority**: How to reach free legal aid — [source](https://nalsa.gov.in/legal-aid/#Free-Legal-Aid) (✅ verified 2026-11-19)</small>

### What I'm not sure about
- Whether the seller will claim the damage was caused by misuse rather than an original manufacturing defect.

---
<small>Knowledge base last verified: 2026-11-19. Only verified sources are cited. This is general information, not legal advice.</small>

## Safety checker log (items removed from the AI's draft)
```json
[]
```

## Raw model JSON for the answer (before the safety checker)
```json
{
 "summary": "You are a consumer since you bought the washing machine for your family home, and because the seller is refusing to repair or replace a faulty product, you have a valid basis to seek relief. You are well within the time limit to take legal action.",
 "points": [
  {
   "text": "Because you purchased the washing machine for personal use rather than for resale or commercial purposes, you qualify as a consumer.",
   "kb_ids": [
    "CPA2019-S2-7"
   ]
  },
  {
   "text": "The issue you are facing with the leaking machine counts as a product defect because it is a fault or shortcoming in quality.",
   "kb_ids": [
    "CPA2019-S2-10"
   ]
  },
  {
   "text": "Refusing to take back or fix a defective item when it is pointed out can be treated as an unfair trade practice.",
   "kb_ids": [
    "CPA2019-S2-47"
   ]
  },
  {
   "text": "If you decide to approach the consumer forum, you can ask for remedies such as a replacement of the machine, a refund of the price, or compensation for the trouble caused.",
   "kb_ids": [
    "CPA2019-S39"
   ]
  }
 ],
 "options": [
  {
   "title": "Contact the National Consumer Helpline",
   "why": "This is a pre-litigation step where helpline staff attempt to resolve your grievance with the seller before you file a formal case.",
   "steps": [
    "Call the helpline or use their web portal, app, or WhatsApp to register your complaint.",
    "Provide your purchase details, bill, and description of the leak.",
    "Wait for their intervention to see if the seller agrees to a resolution."
   ],
   "kb_ids": [
    "PROC-NCH"
   ]
  },
  {
   "title": "File a formal consumer complaint online",
   "why": "You can file a case in the relevant consumer commission since the seller refused to help.",
   "steps": [
    "Prepare your documents, including the purchase bill, warranty card, and photos of the leak.",
    "File your complaint electronically on the official e-Jagriti portal.",
    "Pay any applicable fee if required, though online filing guides you through the process."
   ],
   "kb_ids": [
    "CPA2019-S35",
    "PROC-EJAGRITI",
    "CPR2020-FEES"
   ]
  },
  {
   "title": "Seek free legal aid",
   "why": "If you need professional guidance with drafting your complaint or understanding the process and happen to qualify under certain categories, you can access free legal services.",
   "steps": [
    "Check if you qualify under categories such as being a woman, having a low annual income, or belonging to a specific reserved category.",
    "Reach out to your local District Legal Services Authority in person, by post, or through their helpline (15100).",
    "Submit a simple written application with your identity proof."
   ],
   "kb_ids": [
    "LSA1987-S12",
    "PROC-NALSA"
   ]
  }
 ],
 "uncertainties": [
  "Whether the seller will claim the damage was caused by misuse rather than an original manufacturing defect."
 ],
 "suggest_lawyer": false,
 "lawyer_reason": ""
}
```

## Document: commission_complaint
Offered: yes
Drafting log: AI paragraph accepted

```text
**BEFORE THE DISTRICT CONSUMER DISPUTES REDRESSAL COMMISSION, [DISTRICT NAME], [STATE]**

Consumer Complaint No. ______ of ______ (to be filled by the Commission)

**Complainant:**
[YOUR FULL NAME], [YOUR FULL ADDRESS], Jaipur

**Versus**

**Opposite Party:**
Sharma Electronics, [OPPOSITE PARTY'S REGISTERED ADDRESS – see your invoice or the website's legal/contact page]

---

**COMPLAINT**

**1. Facts of the case**

1. I purchased a Washing machine from Sharma Electronics on 2 August 2026 for Rs 32,000.

2. On 20 October 2026, it started leaking and the shop refuses to repair or replace it.

3. I complained to the shop, but they refuse to repair or replace it.

**2. Jurisdiction**

(a) The value of the goods/services paid as consideration is Rs 32,000, which is within the limit of this Commission (Rules 3-5 of the Consumer Protection (Jurisdiction of the District Commission, the State Commission and the National Commission) Rules, 2021).

(b) The Complainant resides/personally works for gain at Jaipur, within the area of this Commission (Section 34 of the Consumer Protection Act, 2019).

**3. Limitation**

The cause of action arose on or about 20 October 2026. This complaint is filed within the period allowed (Section 69 of the Consumer Protection Act, 2019).

**4. Relief sought**

The Complainant respectfully requests this Commission to direct the Opposite Party to:
(a) grant the following relief: replacement;
(b) pay such compensation and costs as this Commission considers just (Section 39 of the Consumer Protection Act, 2019).

**5. List of documents**

1. bill
2. warranty card
3. photos of the leak

**Verification**

I, [YOUR FULL NAME], the Complainant, state that the contents of this complaint are true and correct to the best of my knowledge and belief, and nothing material has been concealed.

Place: [PLACE]
Date: [DATE]

[SIGNATURE OF COMPLAINANT]

```