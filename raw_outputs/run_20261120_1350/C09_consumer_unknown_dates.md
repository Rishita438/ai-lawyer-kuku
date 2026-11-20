# C09_consumer_unknown_dates
**Category:** edge-missing-facts  
**Description:** User doesn't know key dates. Complaint must be locked; letter uses placeholders, not guesses.  
**Pack:** consumer  
**Run at:** 2026-11-20T13:59:27  
**Models that answered:** gemini-3.5-flash-lite, openai/gpt-oss-120b (18 calls)  
**Time:** 69.3 s

> Unedited output of scripts/run_tests.py. Nothing below was changed by hand.

## Automatic checks
| Check | Result | Detail |
|---|---|---|
| escalation | PASS | expected none, got none |
| document grievance_letter | PASS | expected unlocked, got unlocked |
| document commission_complaint | PASS | expected locked/absent, got locked/absent (When did you buy it (approximate date is fine)? (tip: check your invoice or order history); On what date did the problem happen, or the refund become due? (tip: the date the product failed or the refund was due)) |

## Conversation
**Bot:** Tell me what happened, in your own words - English, Hindi or Hinglish is fine. For example: what you bought, from whom, and what went wrong.

**User:** maine amazon se ek mixer grinder liya tha 3200 ka, kuch time baad kharab ho gaya, date yaad nahi

**Bot:** Amazon se kharida hua mixer grinder kharab ho gaya hai. Aapne yeh kab khareeda tha (lagbhag date bhi chalegi)?

**User:** pata nahi

**Bot:** Koi baat nahi, agar exact date yaad nahi hai to koi andaza bata sakte hain. Problem kis date ko hui, ya refund kab milna tha?

**User:** pata nahi

**Bot:** Samajh gaya, aapko is baare mein pata nahi hai. Kya aapne yeh apne personal use ke liye liya tha, ya business / aage bechne ke liye? (Aapne bataya: nahi - sahi hai?)

**User:** ghar ke liye

**Bot:** Aapne ghar ke liye kuch kharida tha jisme problem aa gayi hai. Kya aapne seller ya platform ko pehle complain kiya hai? Agar haan, to kaise aur kab, aur unhone kya kaha?

**User:** abhi tak nahi kiya

**Bot:** Maine aapki baat note kar li hai. Aapke paas kya proof hai? (bill/invoice, order ID, payment screenshot, emails, chats, photos, warranty card)

**User:** order history mein hoga

**Bot:** Theek hai, aapke order history mein details mil jayengi. Aap kya chahte hain - refund, replacement, repair, ya compensation?

**User:** repair ya replacement

**Bot:** Aapne repair ya replacement ke baare mein bataya. Aap kis shehar aur state mein rehte hain? (Isse tay hota hai ki aap complaint kahan file kar sakte hain.)

**User:** Kolkata, West Bengal

**Bot:** Main samajh gaya hoon ki aap Kolkata, West Bengal se hain.

## Case file (final)
```json
{
 "pack": "consumer",
 "facts": {
  "product_or_service": "mixer grinder",
  "seller_name": "amazon",
  "bought_online": true,
  "amount_paid": 3200,
  "purchase_date": "unknown",
  "what_went_wrong": "kuch time baad kharab ho gaya",
  "problem_date": "unknown",
  "for_business_use": false,
  "complaints_made": "abhi tak nahi kiya",
  "evidence": [
   "order history"
  ],
  "desired_outcome": "repair or replacement",
  "user_city_state": "Kolkata, West Bengal"
 },
 "language": "hinglish",
 "user_messages": [
  "maine amazon se ek mixer grinder liya tha 3200 ka, kuch time baad kharab ho gaya, date yaad nahi",
  "pata nahi",
  "pata nahi",
  "ghar ke liye",
  "abhi tak nahi kiya",
  "order history mein hoga",
  "repair ya replacement",
  "Kolkata, West Bengal"
 ],
 "suggested": {
  "for_business_use": false
 }
}
```

## Answer shown to the user

### Where you stand

Aapka mixer grinder kharab ho gaya hai aur aapne ise ghar ke use ke liye kharida tha, isliye aap ek consumer hain. Aap online platform ke grievance officer se baat kar sakte hain ya District Consumer Commission mein repair, replacement ya refund ke liye complaint file kar sakte hain.

- Aapne yeh mixer grinder apne personal use ke liye liya tha aur business ke liye nahi, isliye aap consumer hain.<br><small>📘 **Consumer Protection Act, 2019, s. 2(7)**: Who is a "consumer" — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)</small>

- Agar saman mein koi kharabi ya imperfection hai, toh use defect kaha jata hai.<br><small>📘 **Consumer Protection Act, 2019, s. 2(10)**: What is a "defect" (goods) — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)</small>

- Aapki khareed ki value ke mutabik, is mamle mein filing fee nil (koi fee nahi) hai.<br><small>📘 **Consumer Protection (Consumer Disputes Redressal Commissions) Rules, 2020, Rule 7 (fee table)**: Fee for filing a consumer complaint — [source](https://egazette.gov.in/WriteReadData/2023/248158.pdf) (✅ verified 2026-11-19)</small>

- Aap District Consumer Commission mein complaint file kar sakte hain, aur aap us jagah se bhi file kar sakte hain jahan aap rehte hain (Kolkata, West Bengal).<br><small>📘 **Consumer Protection Act, 2019, s. 34**: District Commission - which one you can file in — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)<br>📘 **Consumer Protection (Jurisdiction of the District Commission, the State Commission and the National Commission) Rules, 2021, Rules 3-5**: Money limits - which Commission — [source](https://www.pib.gov.in/PressReleasePage.aspx?PRID=1786342) (✅ verified 2026-11-19)</small>

#### Key facts (calculated by the app, not the AI)

⏳ **Time limit:** can't calculate - the date the problem arose is unknown. The normal limit is 2 years from that date.

🏛️ **Which Commission:** District Consumer Commission, for Rs 3,200 paid (you can file where you live or work: Kolkata, West Bengal).

💰 **Filing fee:** nil (no fee).

<small>Based on: 📘 **Consumer Protection Act, 2019, s. 34**: District Commission - which one you can file in — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19); 📘 **Consumer Protection Act, 2019, s. 69**: Time limit for filing a complaint — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19); 📘 **Consumer Protection (Consumer Disputes Redressal Commissions) Rules, 2020, Rule 7 (fee table)**: Fee for filing a consumer complaint — [source](https://egazette.gov.in/WriteReadData/2023/248158.pdf) (✅ verified 2026-11-19); 📘 **Consumer Protection (Jurisdiction of the District Commission, the State Commission and the National Commission) Rules, 2021, Rules 3-5**: Money limits - which Commission — [source](https://www.pib.gov.in/PressReleasePage.aspx?PRID=1786342) (✅ verified 2026-11-19)</small>

### Your options

**1. Online Platform Grievance Officer** — Platform ke grievance officer se pehle contact karke issue raise kiya ja sakta hai.
   - Amazon ke platform par grievance officer ki details dekhein.
   - Apni complaint darj karein.
   - Officer ko 48 ghante ke andar acknowledge karna hoga aur ek mahine ke andar solution dena hoga.

   <small>📘 **Consumer Protection (E-Commerce) Rules, 2020, Rule 4(4)-(5)**: E-commerce grievance officer — [source](https://egazette.gov.in/WriteReadData/2020/220661.pdf) (✅ verified 2026-11-19)</small>

**2. National Consumer Helpline (NCH)** — Formal case file karne se pehle helpline par pre-litigation step ke taur par madad mangi ja sakti hai.
   - 1915 ya 1800 11 4000 par call karein.
   - Ya phir app ya portal ke zariye apni shikayat darj karein.

   <small>📘 **National Consumer Helpline (consumerhelpline.gov.in), Contact page and FAQ**: National Consumer Helpline (pre-litigation step) — [source](https://consumerhelpline.gov.in/) (✅ verified 2026-11-19)</small>

**3. District Consumer Commission mein online filing** — Aap e-Jagriti portal par jaakar formal complaint darj kar sakte hain aur repair, replacement ya refund ki maang kar sakte hain.
   - e-Jagriti portal par jayein.
   - Apni complaint aur order history ke saboot ke sath form bharein.
   - District Commission mein case submit karein.

   <small>📘 **Consumer Protection Act, 2019, s. 35**: How a complaint is filed — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)<br>📘 **Consumer Protection Act, 2019, s. 39**: What the Commission can order — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)<br>📘 **e-Jagriti (Department of Consumer Affairs)**: File online on e-Jagriti — [source](https://e-jagriti.gov.in/) (✅ verified 2026-11-19)</small>

### What I'm not sure about
- Problem kis date ko shuru hui thi yeh pata nahi hai, isliye exact time limit (deadline) verify nahi ki ja saki.
- Kya seller ya platform ne koi warranty ya return policy di thi, yeh details case file mein nahi hain.

---
<small>Knowledge base last verified: 2026-11-19. Only verified sources are cited. This is general information, not legal advice.</small>

## Safety checker log (items removed from the AI's draft)
```json
[]
```

## Raw model JSON for the answer (before the safety checker)
```json
{
 "summary": "Aapka mixer grinder kharab ho gaya hai aur aapne ise ghar ke use ke liye kharida tha, isliye aap ek consumer hain. Aap online platform ke grievance officer se baat kar sakte hain ya District Consumer Commission mein repair, replacement ya refund ke liye complaint file kar sakte hain.",
 "points": [
  {
   "text": "Aapne yeh mixer grinder apne personal use ke liye liya tha aur business ke liye nahi, isliye aap consumer hain.",
   "kb_ids": [
    "CPA2019-S2-7"
   ]
  },
  {
   "text": "Agar saman mein koi kharabi ya imperfection hai, toh use defect kaha jata hai.",
   "kb_ids": [
    "CPA2019-S2-10"
   ]
  },
  {
   "text": "Aapki khareed ki value ke mutabik, is mamle mein filing fee nil (koi fee nahi) hai.",
   "kb_ids": [
    "CPR2020-FEES"
   ]
  },
  {
   "text": "Aap District Consumer Commission mein complaint file kar sakte hain, aur aap us jagah se bhi file kar sakte hain jahan aap rehte hain (Kolkata, West Bengal).",
   "kb_ids": [
    "CPA2019-S34",
    "CPR2021-PECUNIARY"
   ]
  }
 ],
 "options": [
  {
   "title": "Online Platform Grievance Officer",
   "why": "Platform ke grievance officer se pehle contact karke issue raise kiya ja sakta hai.",
   "steps": [
    "Amazon ke platform par grievance officer ki details dekhein.",
    "Apni complaint darj karein.",
    "Officer ko 48 ghante ke andar acknowledge karna hoga aur ek mahine ke andar solution dena hoga."
   ],
   "kb_ids": [
    "ECOM2020-R4-5"
   ]
  },
  {
   "title": "National Consumer Helpline (NCH)",
   "why": "Formal case file karne se pehle helpline par pre-litigation step ke taur par madad mangi ja sakti hai.",
   "steps": [
    "1915 ya 1800 11 4000 par call karein.",
    "Ya phir app ya portal ke zariye apni shikayat darj karein."
   ],
   "kb_ids": [
    "PROC-NCH"
   ]
  },
  {
   "title": "District Consumer Commission mein online filing",
   "why": "Aap e-Jagriti portal par jaakar formal complaint darj kar sakte hain aur repair, replacement ya refund ki maang kar sakte hain.",
   "steps": [
    "e-Jagriti portal par jayein.",
    "Apni complaint aur order history ke saboot ke sath form bharein.",
    "District Commission mein case submit karein."
   ],
   "kb_ids": [
    "CPA2019-S35",
    "CPA2019-S39",
    "PROC-EJAGRITI"
   ]
  }
 ],
 "uncertainties": [
  "Problem kis date ko shuru hui thi yeh pata nahi hai, isliye exact time limit (deadline) verify nahi ki ja saki.",
  "Kya seller ya platform ne koi warranty ya return policy di thi, yeh details case file mein nahi hain."
 ],
 "suggest_lawyer": false,
 "lawyer_reason": ""
}
```

## Document: grievance_letter
Offered: yes
Drafting log: AI paragraph accepted

```text
To,
The Grievance Officer,
Amazon

**Subject: Complaint regarding Mixer grinder – Order ID [ORDER ID]**

Dear Sir/Madam,

I am writing to register a formal complaint about my purchase from Amazon.

1. I purchased a Mixer grinder online from Amazon for Rs 3,200 on [PURCHASE DATE – check your invoice or order history] for personal use.

2. The product stopped working after some time on [PROBLEM DATE – the date the product failed or the refund was due].

3. I have not made any complaints regarding this matter until now.

**My request:** repair or replacement.

Under Rule 4(4)-(5) of the Consumer Protection (E-Commerce) Rules, 2020, the grievance officer is required to acknowledge a consumer complaint within 48 hours and redress it within one month of receiving it. I request you to do so.

I have the following documents and will share them on request: order history.

Please treat this letter as a formal complaint and keep a record of it.

Yours faithfully,
[YOUR FULL NAME]
[YOUR EMAIL / PHONE NUMBER]
Date: [DATE OF SENDING]

```

## Document: commission_complaint
Offered: LOCKED - When did you buy it (approximate date is fine)? (tip: check your invoice or order history); On what date did the problem happen, or the refund become due? (tip: the date the product failed or the refund was due)