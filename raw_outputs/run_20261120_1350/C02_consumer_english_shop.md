# C02_consumer_english_shop
**Category:** normal  
**Description:** Washing machine from a local shop, English; no e-commerce letter should be offered.  
**Pack:** consumer  
**Run at:** 2026-11-20T13:52:25  
**Models that answered:** gemini-3.5-flash-lite (12 calls)  
**Time:** 37.5 s

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

**Bot:** Facing a leaky washing machine and a refusal to repair or replace it can be quite stressful. On what date did the problem happen, or the refund become due? (You mentioned: 2026-10-20 - is that right?)

**User:** 20 October 2026

**Bot:** Noted, thank you for sharing that date with me. Did you buy this for your own personal use, or to resell / use in a business? (You mentioned: no - is that right?)

**User:** for my family at home

**Bot:** I understand you purchased this for your family. What proof do you have? (invoice/bill, order ID, payment screenshot, emails, chats, photos, warranty card)

**User:** the bill, warranty card and photos of the leak

**Bot:** Got it, thanks for sharing those details. What would you like - refund, replacement, repair, or compensation? (You mentioned: repair or replacement - is that right?)

**User:** replacement

**Bot:** I understand you are dealing with a replacement issue.

## Case file (final)
```json
{
 "pack": "consumer",
 "facts": {
  "product_or_service": "washing machine",
  "seller_name": "Sharma Electronics",
  "bought_online": false,
  "amount_paid": 32000,
  "purchase_date": "2026-08-02",
  "what_went_wrong": "It started leaking on 20 October 2026 and the shop refuses to repair or replace it.",
  "problem_date": "2026-10-20",
  "for_business_use": false,
  "complaints_made": "Complained to Sharma Electronics, but they refuse to repair or replace it.",
  "evidence": [
   "bill",
   "warranty card",
   "photos of the leak"
  ],
  "desired_outcome": "replacement",
  "user_city_state": "Jaipur, Rajasthan"
 },
 "language": "en",
 "user_messages": [
  "I bought a washing machine for Rs 32,000 from Sharma Electronics, a shop in Jaipur, on 2 August 2026. It started leaking on 20 October 2026. The shop refuses to repair or replace it.",
  "20 October 2026",
  "for my family at home",
  "the bill, warranty card and photos of the leak",
  "replacement"
 ],
 "suggested": {
  "problem_date": "2026-10-20",
  "for_business_use": false,
  "desired_outcome": "repair or replacement"
 }
}
```

## Answer shown to the user

### Where you stand

You bought a washing machine for personal use that developed a leak within the warranty period, and the seller has refused to repair or replace it. Because you bought goods for personal use, you are considered a consumer under the law, and you have time to take formal action if needed.

- Since you purchased the washing machine for your family at home and not for business or resale, you are recognised as a consumer.<br><small>📘 **Consumer Protection Act, 2019, s. 2(7)**: Who is a "consumer" — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)</small>

- A fault or shortcoming in the quality or standard of goods is considered a defect.<br><small>📘 **Consumer Protection Act, 2019, s. 2(10)**: What is a "defect" (goods) — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)</small>

- Refusing to take back defective goods or provide a remedy as promised can amount to an unfair trade practice.<br><small>📘 **Consumer Protection Act, 2019, s. 2(47)**: What is an "unfair trade practice" — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)</small>

- ⏳ **Time limit:** ✅ within the limit. Normally file by **2028-10-20** (2 years from 2026-10-20; dates are approximate).<br><small>📘 **Consumer Protection Act, 2019, s. 69**: Time limit for filing a complaint — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)</small>

- 🏛️ **Which Commission:** District Consumer Commission, for Rs 32,000 paid (you can file where you live or work: Jaipur, Rajasthan).<br><small>📘 **Consumer Protection (Jurisdiction of the District Commission, the State Commission and the National Commission) Rules, 2021, Rules 3-5**: Money limits - which Commission — [source](https://www.pib.gov.in/PressReleasePage.aspx?PRID=1786342) (✅ verified 2026-11-19)<br>📘 **Consumer Protection Act, 2019, s. 34**: District Commission - which one you can file in — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)</small>

#### Key facts (calculated by the app, not the AI)

⏳ **Time limit:** ✅ within the limit. Normally file by **2028-10-20** (2 years from 2026-10-20; dates are approximate).

🏛️ **Which Commission:** District Consumer Commission, for Rs 32,000 paid (you can file where you live or work: Jaipur, Rajasthan).

💰 **Filing fee:** nil (no fee).

<small>Based on: 📘 **Consumer Protection Act, 2019, s. 34**: District Commission - which one you can file in — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19); 📘 **Consumer Protection Act, 2019, s. 69**: Time limit for filing a complaint — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19); 📘 **Consumer Protection (Consumer Disputes Redressal Commissions) Rules, 2020, Rule 7 (fee table)**: Fee for filing a consumer complaint — [source](https://egazette.gov.in/WriteReadData/2023/248158.pdf) (✅ verified 2026-11-19); 📘 **Consumer Protection (Jurisdiction of the District Commission, the State Commission and the National Commission) Rules, 2021, Rules 3-5**: Money limits - which Commission — [source](https://www.pib.gov.in/PressReleasePage.aspx?PRID=1786342) (✅ verified 2026-11-19)</small>

### Your options

**1. Contact the National Consumer Helpline** — This is a pre-litigation step to try and get the seller to resolve the issue before filing a formal complaint.
   - Call the helpline at 1915 or 1800 11 4000, or use their web portal, app, or WhatsApp.
   - Register your grievance with details of your purchase and the leak.
   - Wait for their intervention with the seller, noting this does not [removed: nobody can promise a legal outcome] an outcome.

   <small>📘 **National Consumer Helpline (consumerhelpline.gov.in), Contact page and FAQ**: National Consumer Helpline (pre-litigation step) — [source](https://consumerhelpline.gov.in/) (✅ verified 2026-11-19)</small>

**2. File a complaint before the District Consumer Commission** — If informal steps or the helpline do not work, you can file a formal consumer complaint.
   - Prepare your complaint along with your bill, warranty card, and photos of the leak.
   - File your complaint online through the e-Jagriti portal.
   - Note that the filing fee is nil (no fee) for a claim of this amount.
   - Ask the Commission for remedies such as a replacement of the washing machine, removal of the defect, or compensation.

   <small>📘 **Consumer Protection Act, 2019, s. 35**: How a complaint is filed — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)<br>📘 **Consumer Protection Act, 2019, s. 39**: What the Commission can order — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)<br>📘 **Consumer Protection (Consumer Disputes Redressal Commissions) Rules, 2020, Rule 7 (fee table)**: Fee for filing a consumer complaint — [source](https://egazette.gov.in/WriteReadData/2023/248158.pdf) (✅ verified 2026-11-19)<br>📘 **e-Jagriti (Department of Consumer Affairs)**: File online on e-Jagriti — [source](https://e-jagriti.gov.in/) (✅ verified 2026-11-19)</small>

**3. Seek free legal aid** — Depending on your category (such as women or income criteria), you may be eligible for free legal assistance to help with your case.
   - Check if you qualify under categories like women, children, or annual income limits set by the state government.
   - Contact the District Legal Services Authority at the district court or call the toll-free helpline at 15100.
   - Submit a simple written application, email, or online request through the NALSA website with your identity proof.

   <small>📘 **Legal Services Authorities Act, 1987, s. 12**: Who can get free legal aid — [source](https://indiacode.gov.in/act/a742f03e-3129-4b8d-8dda-af2a36190b18/sections?spc.sf=dc.date.issued&spc.sd=DESC&spc.page=2&spc.rpp=10) (✅ verified 2026-11-19)<br>📘 **National Legal Services Authority**: How to reach free legal aid — [source](https://nalsa.gov.in/legal-aid/#Free-Legal-Aid) (✅ verified 2026-11-19)</small>

### What I'm not sure about
- Whether the seller's refusal is covered under specific warranty terms or exclusions is unverified and depends on the exact documentation.
- The final outcome or any specific compensation amount cannot be [removed: nobody can promise a legal outcome].

---
<small>Knowledge base last verified: 2026-11-19. Only verified sources are cited. The safety checker removed 2 unverified item(s) from the AI's draft. This is general information, not legal advice.</small>

## Safety checker log (items removed from the AI's draft)
```json
[
 {
  "type": "promised_outcome",
  "text": "guarantee"
 },
 {
  "type": "promised_outcome",
  "text": "guaranteed"
 }
]
```

## Raw model JSON for the answer (before the safety checker)
```json
{
 "summary": "You bought a washing machine for personal use that developed a leak within the warranty period, and the seller has refused to repair or replace it. Because you bought goods for personal use, you are considered a consumer under the law, and you have time to take formal action if needed.",
 "points": [
  {
   "text": "Since you purchased the washing machine for your family at home and not for business or resale, you are recognised as a consumer.",
   "kb_ids": [
    "CPA2019-S2-7"
   ]
  },
  {
   "text": "A fault or shortcoming in the quality or standard of goods is considered a defect.",
   "kb_ids": [
    "CPA2019-S2-10"
   ]
  },
  {
   "text": "Refusing to take back defective goods or provide a remedy as promised can amount to an unfair trade practice.",
   "kb_ids": [
    "CPA2019-S2-47"
   ]
  },
  {
   "text": "⏳ **Time limit:** ✅ within the limit. Normally file by **2028-10-20** (2 years from 2026-10-20; dates are approximate).",
   "kb_ids": [
    "CPA2019-S69"
   ]
  },
  {
   "text": "🏛️ **Which Commission:** District Consumer Commission, for Rs 32,000 paid (you can file where you live or work: Jaipur, Rajasthan).",
   "kb_ids": [
    "CPR2021-PECUNIARY",
    "CPA2019-S34"
   ]
  }
 ],
 "options": [
  {
   "title": "Contact the National Consumer Helpline",
   "why": "This is a pre-litigation step to try and get the seller to resolve the issue before filing a formal complaint.",
   "steps": [
    "Call the helpline at 1915 or 1800 11 4000, or use their web portal, app, or WhatsApp.",
    "Register your grievance with details of your purchase and the leak.",
    "Wait for their intervention with the seller, noting this does not guarantee an outcome."
   ],
   "kb_ids": [
    "PROC-NCH"
   ]
  },
  {
   "title": "File a complaint before the District Consumer Commission",
   "why": "If informal steps or the helpline do not work, you can file a formal consumer complaint.",
   "steps": [
    "Prepare your complaint along with your bill, warranty card, and photos of the leak.",
    "File your complaint online through the e-Jagriti portal.",
    "Note that the filing fee is nil (no fee) for a claim of this amount.",
    "Ask the Commission for remedies such as a replacement of the washing machine, removal of the defect, or compensation."
   ],
   "kb_ids": [
    "CPA2019-S35",
    "CPA2019-S39",
    "CPR2020-FEES",
    "PROC-EJAGRITI"
   ]
  },
  {
   "title": "Seek free legal aid",
   "why": "Depending on your category (such as women or income criteria), you may be eligible for free legal assistance to help with your case.",
   "steps": [
    "Check if you qualify under categories like women, children, or annual income limits set by the state government.",
    "Contact the District Legal Services Authority at the district court or call the toll-free helpline at 15100.",
    "Submit a simple written application, email, or online request through the NALSA website with your identity proof."
   ],
   "kb_ids": [
    "LSA1987-S12",
    "PROC-NALSA"
   ]
  }
 ],
 "uncertainties": [
  "Whether the seller's refusal is covered under specific warranty terms or exclusions is unverified and depends on the exact documentation.",
  "The final outcome or any specific compensation amount cannot be guaranteed."
 ],
 "suggest_lawyer": false,
 "lawyer_reason": ""
}
```

## Document: commission_complaint
Offered: yes
Drafting log: AI paragraph accepted

```text
**BEFORE THE DISTRICT CONSUMER DISPUTES REDRESSAL COMMISSION, [DISTRICT NAME], RAJASTHAN**

Consumer Complaint No. ______ of ______ (to be filled by the Commission)

**Complainant:**
[YOUR FULL NAME], [YOUR FULL ADDRESS], Jaipur, Rajasthan

**Versus**

**Opposite Party:**
Sharma Electronics, [OPPOSITE PARTY'S REGISTERED ADDRESS – see your invoice or the website's legal/contact page]

---

**COMPLAINT**

**1. Facts of the case**

1. On 2 August 2026, I purchased a washing machine from Sharma Electronics for the amount of Rs 32,000.

2. The said washing machine started leaking on 20 October 2026.

3. I complained to Sharma Electronics regarding this issue, but they refuse to repair or replace it.

**2. Jurisdiction**

(a) The value of the goods/services paid as consideration is Rs 32,000, which is within the limit of this Commission (Rules 3-5 of the Consumer Protection (Jurisdiction of the District Commission, the State Commission and the National Commission) Rules, 2021).

(b) The Complainant resides/personally works for gain at Jaipur, Rajasthan, within the area of this Commission (Section 34 of the Consumer Protection Act, 2019).

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