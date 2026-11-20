# C09_consumer_unknown_dates
**Category:** edge-missing-facts  
**Description:** User doesn't know key dates. Complaint must be locked; letter uses placeholders, not guesses.  
**Pack:** consumer  
**Run at:** 2026-11-20T14:20:05  
**Models that answered:** gemini-3.5-flash-lite (22 calls)  
**Time:** 84.3 s

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

**Bot:** Aapne Amazon se mixer grinder kharida tha aur woh kharab ho gaya. Aapne yeh kab khareeda tha (lagbhag date bhi chalegi)?

**User:** pata nahi

**Bot:** Theek hai, koi baat nahi. Problem kis date ko hui, ya refund kab milna tha?

**User:** pata nahi

**Bot:** Theek hai, koi baat nahi. Problem kis date ko hui, ya refund kab milna tha?

**User:** pata nahi

**Bot:** Koi baat nahi, yeh detail baad mein dekhi ja sakti hai. Problem kis date ko hui, ya refund kab milna tha?

**User:** pata nahi

**Bot:** Main samajh sakta hoon, is baare mein thoda confusions ho sakta hai. Kya aapne yeh apne personal use ke liye liya tha, ya business / aage bechne ke liye?

**User:** ghar ke liye

**Bot:** Aapne ghar ke liye kharidaari ki thi. Kya aapne seller ya platform ko pehle complain kiya hai? Agar haan, to kaise aur kab, aur unhone kya kaha?

**User:** abhi tak nahi kiya

**Bot:** Aapne bataya ki unhone abhi tak yeh kaam nahi kiya hai. Aapke paas kya proof hai? (bill/invoice, order ID, payment screenshot, emails, chats, photos, warranty card)

**User:** order history mein hoga

**Bot:** Theek hai, details order history mein mil jayengi. Aap kya chahte hain - refund, replacement, repair, ya compensation?

**User:** repair ya replacement

**Bot:** Main samajh sakta hoon ki aapko product repair ya replacement mein pareshani aa rahi hai. Aap kis shehar aur state mein rehte hain? (Isse tay hota hai ki aap complaint kahan file kar sakte hain.)

**User:** Kolkata, West Bengal

**Bot:** Theek hai, maine Kolkata, West Bengal note kar liya hai.

## Case file (final)
```json
{
 "pack": "consumer",
 "facts": {
  "product_or_service": "mixer grinder",
  "seller_name": "Amazon",
  "bought_online": true,
  "amount_paid": 3200,
  "purchase_date": "unknown",
  "what_went_wrong": "kuch time baad kharab ho gaya",
  "problem_date": "unknown",
  "for_business_use": false,
  "complaints_made": "nahi kiya",
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

Aapka mixer grinder kharab hone par aap consumer ki category mein aate hain kyunki aapne ise personal use ke liye kharida tha. Aapke paas iske order history ka saboot hai, aur aap online platform ya Consumer Commission ke zariye repair ya replacement ke liye koshish kar sakte hain.

- Aapne yeh mixer grinder apne ghar ke use ke liye kharida tha aur iske liye paise diye the, isliye aap ek consumer maane jaate hain.<br><small>📘 **Consumer Protection Act, 2019, s. 2(7)**: Who is a "consumer" — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)</small>

- Agar saman ki quality ya standard mein koi fault ya imperfection nikle, toh use defect kaha jata hai.<br><small>📘 **Consumer Protection Act, 2019, s. 2(10)**: What is a "defect" (goods) — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)</small>

- Aap online platform ke grievance officer se bhi shikayat kar sakte hain, jise unhe aam taur par ek nishchit samay ke andar dekhna hota hai.<br><small>📘 **Consumer Protection (E-Commerce) Rules, 2020, Rule 4(4)-(5)**: E-commerce grievance officer — [source](https://egazette.gov.in/WriteReadData/2020/220661.pdf) (✅ verified 2026-11-19)</small>

- Agar mamla na suljhe, toh aap District Consumer Commission mein shikayat darj kar sakte hain, jiske liye 50 lakh tak ki keemat par koi filing fee nahi lagti.<br><small>📘 **Consumer Protection Act, 2019, s. 34**: District Commission - which one you can file in — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)<br>📘 **Consumer Protection (Consumer Disputes Redressal Commissions) Rules, 2020, Rule 7 (fee table)**: Fee for filing a consumer complaint — [source](https://egazette.gov.in/WriteReadData/2023/248158.pdf) (✅ verified 2026-11-19)<br>📘 **Consumer Protection (Jurisdiction of the District Commission, the State Commission and the National Commission) Rules, 2021, Rules 3-5**: Money limits - which Commission — [source](https://www.pib.gov.in/PressReleasePage.aspx?PRID=1786342) (✅ verified 2026-11-19)</small>

- Consumer Commission mein shikayat aam taur par samasya shuru hone ke 2 saal ke andar karni hoti hai.<br><small>📘 **Consumer Protection Act, 2019, s. 69**: Time limit for filing a complaint — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)</small>

#### Key facts (calculated by the app, not the AI)

⏳ **Time limit:** can't calculate - the date the problem arose is unknown. The normal limit is 2 years from that date.

🏛️ **Which Commission:** District Consumer Commission, for Rs 3,200 paid (you can file where you live or work: Kolkata, West Bengal).

💰 **Filing fee:** nil (no fee).

<small>Based on: 📘 **Consumer Protection Act, 2019, s. 34**: District Commission - which one you can file in — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19); 📘 **Consumer Protection Act, 2019, s. 69**: Time limit for filing a complaint — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19); 📘 **Consumer Protection (Consumer Disputes Redressal Commissions) Rules, 2020, Rule 7 (fee table)**: Fee for filing a consumer complaint — [source](https://egazette.gov.in/WriteReadData/2023/248158.pdf) (✅ verified 2026-11-19); 📘 **Consumer Protection (Jurisdiction of the District Commission, the State Commission and the National Commission) Rules, 2021, Rules 3-5**: Money limits - which Commission — [source](https://www.pib.gov.in/PressReleasePage.aspx?PRID=1786342) (✅ verified 2026-11-19)</small>

### Your options

**1. Online platform ke grievance officer se sampark karein** — Yeh sabse tez aur aasan tarika hai apni shikayat darj karne ka.
   - Platform ke app ya website par grievance officer ki details dekhein.
   - Apni order history ke sath apni samasya likhkar unhe bhejein.

   <small>📘 **Consumer Protection (E-Commerce) Rules, 2020, Rule 4(4)-(5)**: E-commerce grievance officer — [source](https://egazette.gov.in/WriteReadData/2020/220661.pdf) (✅ verified 2026-11-19)</small>

**2. National Consumer Helpline (NCH) par koshish karein** — Court jaane se pehle yeh ek madadgar pre-litigation kadam ho sakta hai.
   - Helpline 1915 par call karein ya unke portal/app ke zariye apni shikayat darj karein.
   - Dekhein ki kya woh aapki samasya ko suljhane mein madad kar pate hain.

   <small>📘 **National Consumer Helpline (consumerhelpline.gov.in), Contact page and FAQ**: National Consumer Helpline (pre-litigation step) — [source](https://consumerhelpline.gov.in/) (✅ verified 2026-11-19)</small>

**3. District Consumer Commission mein online shikayat darj karein** — Agar platform se madad na mile, toh aap official portal par formal shikayat file kar sakte hain.
   - e-Jagriti portal par jayein.
   - Apni order history aur kharab hone ki jankari ke sath apna case file karein.

   <small>📘 **Consumer Protection Act, 2019, s. 35**: How a complaint is filed — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)<br>📘 **e-Jagriti (Department of Consumer Affairs)**: File online on e-Jagriti — [source](https://e-jagriti.gov.in/) (✅ verified 2026-11-19)</small>

### What I'm not sure about
- Samasya exact kis tarikh ko shuru hui thi, yeh abhi pata nahi hai, isliye 2 saal ki samay seema (time limit) ka sahi se pata nahi lagaya ja saka.
- Kya seller ya brand ne warranty di thi aur kya woh warranty period abhi chal raha hai, yeh clear nahi hai.

---
<small>Knowledge base last verified: 2026-11-19. Only verified sources are cited. This is general information, not legal advice.</small>

## Safety checker log (items removed from the AI's draft)
```json
[]
```

## Raw model JSON for the answer (before the safety checker)
```json
{
 "summary": "Aapka mixer grinder kharab hone par aap consumer ki category mein aate hain kyunki aapne ise personal use ke liye kharida tha. Aapke paas iske order history ka saboot hai, aur aap online platform ya Consumer Commission ke zariye repair ya replacement ke liye koshish kar sakte hain.",
 "points": [
  {
   "text": "Aapne yeh mixer grinder apne ghar ke use ke liye kharida tha aur iske liye paise diye the, isliye aap ek consumer maane jaate hain.",
   "kb_ids": [
    "CPA2019-S2-7"
   ]
  },
  {
   "text": "Agar saman ki quality ya standard mein koi fault ya imperfection nikle, toh use defect kaha jata hai.",
   "kb_ids": [
    "CPA2019-S2-10"
   ]
  },
  {
   "text": "Aap online platform ke grievance officer se bhi shikayat kar sakte hain, jise unhe aam taur par ek nishchit samay ke andar dekhna hota hai.",
   "kb_ids": [
    "ECOM2020-R4-5"
   ]
  },
  {
   "text": "Agar mamla na suljhe, toh aap District Consumer Commission mein shikayat darj kar sakte hain, jiske liye 50 lakh tak ki keemat par koi filing fee nahi lagti.",
   "kb_ids": [
    "CPA2019-S34",
    "CPR2020-FEES",
    "CPR2021-PECUNIARY"
   ]
  },
  {
   "text": "Consumer Commission mein shikayat aam taur par samasya shuru hone ke 2 saal ke andar karni hoti hai.",
   "kb_ids": [
    "CPA2019-S69"
   ]
  }
 ],
 "options": [
  {
   "title": "Online platform ke grievance officer se sampark karein",
   "why": "Yeh sabse tez aur aasan tarika hai apni shikayat darj karne ka.",
   "steps": [
    "Platform ke app ya website par grievance officer ki details dekhein.",
    "Apni order history ke sath apni samasya likhkar unhe bhejein."
   ],
   "kb_ids": [
    "ECOM2020-R4-5"
   ]
  },
  {
   "title": "National Consumer Helpline (NCH) par koshish karein",
   "why": "Court jaane se pehle yeh ek madadgar pre-litigation kadam ho sakta hai.",
   "steps": [
    "Helpline 1915 par call karein ya unke portal/app ke zariye apni shikayat darj karein.",
    "Dekhein ki kya woh aapki samasya ko suljhane mein madad kar pate hain."
   ],
   "kb_ids": [
    "PROC-NCH"
   ]
  },
  {
   "title": "District Consumer Commission mein online shikayat darj karein",
   "why": "Agar platform se madad na mile, toh aap official portal par formal shikayat file kar sakte hain.",
   "steps": [
    "e-Jagriti portal par jayein.",
    "Apni order history aur kharab hone ki jankari ke sath apna case file karein."
   ],
   "kb_ids": [
    "CPA2019-S35",
    "PROC-EJAGRITI"
   ]
  }
 ],
 "uncertainties": [
  "Samasya exact kis tarikh ko shuru hui thi, yeh abhi pata nahi hai, isliye 2 saal ki samay seema (time limit) ka sahi se pata nahi lagaya ja saka.",
  "Kya seller ya brand ne warranty di thi aur kya woh warranty period abhi chal raha hai, yeh clear nahi hai."
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

1. I purchased a Mixer grinder online from Amazon on [PURCHASE DATE – check your invoice or order history], and paid Rs 3,200 for it.

2. The product was not bought for business use.

3. The product stopped working after some time on [PROBLEM DATE – the date the product failed or the refund was due].

4. I have not made any complaints regarding this matter.

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