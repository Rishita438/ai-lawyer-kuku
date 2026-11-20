# D01_deposit_hinglish_happy
**Category:** normal  
**Description:** Rs 50,000 deposit, Rs 10,000 returned, landlord blames painting. Notice should be drafted.  
**Pack:** deposit  
**Run at:** 2026-11-20T14:01:08  
**Models that answered:** gemini-3.5-flash-lite (22 calls)  
**Time:** 100.5 s

> Unedited output of scripts/run_tests.py. Nothing below was changed by hand.

## Automatic checks
| Check | Result | Detail |
|---|---|---|
| escalation | PASS | expected none, got none |
| cites expected KB entry | PASS | found ['ICA1872-S73', 'LIM1963-MONEY'] of ['ICA1872-S73', 'LIM1963-MONEY'] |
| language | PASS | expected hinglish, got hinglish |
| document deposit_notice | PASS | expected unlocked, got unlocked |

## Conversation
**Bot:** Tell me what happened with your security deposit, in your own words - English, Hindi or Hinglish is fine. For example: how much deposit you paid, when you moved out, and what the landlord is saying.

**User:** maine pune mein flat chhoda 31 august 2026 ko, 50000 deposit diya tha, makaan maalik ne sirf 10000 lautaya, bolta hai painting ka paisa kaatega

**Bot:** Pune mein flat chhote waqt deposit ki poori rakam nahi milne par aapko pareshaani hui hogi. Kya yeh ghar tha jismein aap rehte the (dukaan, office ya business ki jagah nahi)?

**User:** haan ghar tha, family ke saath rehte the

**Bot:** Theek hai, aap wahan par apne parivar ke sath rehte the. Makaan maalik ne ab tak deposit mein se kitna wapas kiya hai? (Kuch nahi to 0 boliye.) (Aapne bataya: 10000 - sahi hai?)

**User:** 10000

**Bot:** Aapne kiraye ki rakam bata di. Mahine ka kiraya kitna tha?

**User:** 15000

**Bot:** Theek hai, mujhe yeh amount mil gaya hai. Aapne kis date ko ghar khaali karke chaabi wapas di thi? (Aapne bataya: 2026-08-31 - sahi hai?)

**User:** 31 august 2026

**Bot:** Maine yeh date note kar li hai. Kya aapke paas likhit rent agreement hai? Agar haan, to usmein deposit wapas karne ke baare mein kya likha hai?

**User:** 11 mahine ka agreement hai, usmein likha hai deposit refundable hai

**Bot:** Theek hai, aapne bataya ki agreement 11 mahine ka tha aur deposit refundable likha hai. Kya aapke paas saboot hai ki aapne ghar theek haalat mein wapas kiya (photo, video, message ya handover note)?

**User:** flat chhodte waqt ki photos aur video hain

**Bot:** Aapne flat chhodte waqt ki photos aur video sambhal ke rakhi hain. Kya aapne makaan maalik se deposit maanga hai? Agar haan, to kaise aur kab, aur unhone kya kaha?

**User:** whatsapp pe 2 baar maanga, bolta hai dekhenge

**Bot:** Aapne WhatsApp par maanga aur unhone dekhne ka bola, ye baat maine note kar li hai. Aapke paas kya saboot hai? (rent agreement, deposit ki rasid, bank/UPI transfer, kiraye ki rasid, chats, photos) (Aapne bataya: photos, video - sahi hai?)

**User:** rent agreement, deposit ka UPI transfer, whatsapp chats, photos

**Bot:** Maine aapke paas rent agreement, UPI transfer ka saboot, WhatsApp chats aur photos hone ki baat note kar li hai. Aapko poora deposit wapas chahiye, ya kisi katauti ke baad jo aapko theek lagti hai?

**User:** poora deposit wapas

**Bot:** Aap chahte hain ki aapka poora deposit wapas mil jaye.

## Case file (final)
```json
{
 "pack": "deposit",
 "facts": {
  "residential": true,
  "deposit_amount": 50000,
  "amount_returned": 10000,
  "monthly_rent": 15000,
  "move_out_date": "2026-08-31",
  "agreement": "11 mahine ka agreement hai, usmein likha hai deposit refundable hai",
  "landlord_reason": "painting ka paisa kaatega",
  "handover_proof": "flat chhodte waqt ki photos aur video hain",
  "complaints_made": "whatsapp pe 2 baar maanga, bolta hai dekhenge",
  "evidence": [
   "rent agreement",
   "deposit UPI transfer",
   "whatsapp chats",
   "photos"
  ],
  "desired_outcome": "poora deposit wapas",
  "user_city_state": "Pune"
 },
 "language": "hinglish",
 "user_messages": [
  "maine pune mein flat chhoda 31 august 2026 ko, 50000 deposit diya tha, makaan maalik ne sirf 10000 lautaya, bolta hai painting ka paisa kaatega",
  "haan ghar tha, family ke saath rehte the",
  "10000",
  "15000",
  "31 august 2026",
  "11 mahine ka agreement hai, usmein likha hai deposit refundable hai",
  "flat chhodte waqt ki photos aur video hain",
  "whatsapp pe 2 baar maanga, bolta hai dekhenge",
  "rent agreement, deposit ka UPI transfer, whatsapp chats, photos",
  "poora deposit wapas"
 ],
 "suggested": {
  "amount_returned": 10000,
  "move_out_date": "2026-08-31",
  "evidence": [
   "photos",
   "video"
  ]
 }
}
```

## Answer shown to the user

### Where you stand

Aapke agreement ke mutabiq deposit refundable hai, aur aapne 31 August 2026 ko flat chhod diya tha jiske baad makaan maalik ne Rs 50,000 mein se sirf Rs 10,000 wapas kiye hain aur Rs 40,000 rok rakhe hain. Aapka yeh bacha hua paisa maangne ka haq banta hai, kyonki agreement ke tutne par nuksaan ya wada khilafi ke liye compensation maanga ja sakta hai.

- 💰 **Amount still due:** Rs 40,000 (deposit Rs 50,000 - returned Rs 10,000). Agar agreement mein deposit refundable likha hai aur maalik bina kisi pakke adhaar ke paise kaat raha hai, toh aapko contract tootne par bacha hua nuksaan ya paisa maangne ka adhikaar hai.<br><small>📘 **Indian Contract Act, 1872, s. 73**: Compensation when a contract is broken — [source](https://indiacode.gov.in/act/0e782442-f035-4d53-aace-81b1552a8cf2/sections?spc.rpp=10&spc.sf=dc.date.issued&spc.sd=DESC&spc.page=8) (✅ verified 2026-11-19)</small>

- ⏳ **Time:** Aapko flat chhode hue abhi kareeb 2 mahine hue hain. Aam taur par paise recover karne ke mukadme 3 saal ke andar daakhil karne hote hain, lekin sahi deadline case ke facts par depend karti hai.<br><small>📘 **Limitation Act, 1963, Schedule (Articles 7, 22, 55, 113 as examples)**: Time limit to sue for money — [source](https://indiacode.gov.in/server/api/core/bitstreams/ad4711f7-2ef9-41c3-8b7a-30050493cbb2/content) (✅ verified 2026-11-19)</small>

- ℹ️ **Background:** Aapka deposit 2 mahine ke rent se zyada tha. Model Tenancy Act ke mutabiq residential property ka security deposit 2 mahine ke rent se zyada nahi hona chahiye, par yeh tabhi lagu hota hai jab aapke state ne is par koi kanoon banaya ho.<br><small>📘 **Model Tenancy Act, 2021, s. 11**: Security deposit cap and refund (ONLY in states that adopted it) — [source](https://www.mohua.gov.in/static/uploads/2025/11/9ada3e2d46992be72cabf7028d633b87.pdf) (✅ verified 2026-11-19)</small>

#### Key facts (calculated by the app, not the AI)

💰 **Amount still due:** Rs 40,000 (deposit Rs 50,000 - returned Rs 10,000).

⏳ **Time:** about 2 month(s) since you moved out. Most money claims must generally be filed in court within 3 years, but when that period starts depends on the facts - this assistant does not calculate an exact deadline.

ℹ️ **Background:** your deposit was more than two months' rent. The national *Model* Tenancy Act suggests a two-month cap for homes, but it binds only if your state has passed a law based on it - check your state's rent law.

🏠 **Note:** rent law is mostly state law. This assistant covers only general central law (contract and time limits), not your state's rent act.

<small>Based on: 📘 **Indian Contract Act, 1872, s. 73**: Compensation when a contract is broken — [source](https://indiacode.gov.in/act/0e782442-f035-4d53-aace-81b1552a8cf2/sections?spc.rpp=10&spc.sf=dc.date.issued&spc.sd=DESC&spc.page=8) (✅ verified 2026-11-19); 📘 **Limitation Act, 1963, Schedule (Articles 7, 22, 55, 113 as examples)**: Time limit to sue for money — [source](https://indiacode.gov.in/server/api/core/bitstreams/ad4711f7-2ef9-41c3-8b7a-30050493cbb2/content) (✅ verified 2026-11-19); 📘 **Model Tenancy Act, 2021, s. 11**: Security deposit cap and refund (ONLY in states that adopted it) — [source](https://www.mohua.gov.in/static/uploads/2025/11/9ada3e2d46992be72cabf7028d633b87.pdf) (✅ verified 2026-11-19)</small>

### Your options

**1. Legal Notice Bhejein (General Practice)** — Court jaane se pehle ek written notice dena aam practice hai jisse maalik ko amount aur deadline pata chale.
   - Ek likhit notice taiyar karein jismein deposit amount, flat chhodne ki tareekh, aur payment ki deadline likhi ho.
   - Iske saath speed post receipt ya email ka saboot sambhal kar rakhein.
   - Aap yeh notice khud bhi bhej sakte hain, iske liye lawyer hona zaroori nahi hai.

   <small>📝 *Send a legal notice first (general practice)* — general practice, not a legal rule (reviewed 2026-11-19)</small>

**2. Muft Kanooni Sahayata (Free Legal Aid) Lein** — Agar aapko aage lawyer ya kanooni madad ki zaroorat pade toh aap muft kanooni sahayata ke liye apply kar sakte hain.
   - District Legal Services Authority (DLSA) se district court mein ya toll-free helpline (15100) par sampark karein.
   - Apni identity proof aur written application ke zariye muft madad ke liye apply karein.

   <small>📘 **Legal Services Authorities Act, 1987, s. 12**: Who can get free legal aid — [source](https://indiacode.gov.in/act/a742f03e-3129-4b8d-8dda-af2a36190b18/sections?spc.sf=dc.date.issued&spc.sd=DESC&spc.page=2&spc.rpp=10) (✅ verified 2026-11-19)<br>📘 **National Legal Services Authority**: How to reach free legal aid — [source](https://nalsa.gov.in/legal-aid/#Free-Legal-Aid) (✅ verified 2026-11-19)</small>

### What I'm not sure about
- Kya Maharashtra state ne [removed: unverified legal reference] ke niyam apnaye hain, yeh is text se verify nahi hota.
- Kya painting ka kharcha kaatne ka koi clause agreement mein tha ya nahi, yeh assistant verify nahi kar sakta.
- Aapke case ki exact kanooni deadline kya hogi, iska poora faisla nahi kiya gaya hai.

---
<small>Knowledge base last verified: 2026-11-19. Only verified sources are cited. The safety checker removed 2 unverified item(s) from the AI's draft. This is general information, not legal advice.</small>

## Safety checker log (items removed from the AI's draft)
```json
[
 {
  "type": "uncited_point_dropped",
  "text": "🏠 **Note:** Rent law zyadatar state ka kanoon hota hai. Yeh assistant sirf general central law (contract aur time limits"
 },
 {
  "type": "legal_reference",
  "text": "Model Tenancy Act, 2021"
 }
]
```

## Raw model JSON for the answer (before the safety checker)
```json
{
 "summary": "Aapke agreement ke mutabiq deposit refundable hai, aur aapne 31 August 2026 ko flat chhod diya tha jiske baad makaan maalik ne Rs 50,000 mein se sirf Rs 10,000 wapas kiye hain aur Rs 40,000 rok rakhe hain. Aapka yeh bacha hua paisa maangne ka haq banta hai, kyonki agreement ke tutne par nuksaan ya wada khilafi ke liye compensation maanga ja sakta hai.",
 "points": [
  {
   "text": "💰 **Amount still due:** Rs 40,000 (deposit Rs 50,000 - returned Rs 10,000). Agar agreement mein deposit refundable likha hai aur maalik bina kisi pakke adhaar ke paise kaat raha hai, toh aapko contract tootne par bacha hua nuksaan ya paisa maangne ka adhikaar hai.",
   "kb_ids": [
    "ICA1872-S73"
   ]
  },
  {
   "text": "⏳ **Time:** Aapko flat chhode hue abhi kareeb 2 mahine hue hain. Aam taur par paise recover karne ke mukadme 3 saal ke andar daakhil karne hote hain, lekin sahi deadline case ke facts par depend karti hai.",
   "kb_ids": [
    "LIM1963-MONEY"
   ]
  },
  {
   "text": "ℹ️ **Background:** Aapka deposit 2 mahine ke rent se zyada tha. Model Tenancy Act ke mutabiq residential property ka security deposit 2 mahine ke rent se zyada nahi hona chahiye, par yeh tabhi lagu hota hai jab aapke state ne is par koi kanoon banaya ho.",
   "kb_ids": [
    "MTA2021-S11"
   ]
  },
  {
   "text": "🏠 **Note:** Rent law zyadatar state ka kanoon hota hai. Yeh assistant sirf general central law (contract aur time limits) cover karta hai, aapke state ka apna rent act alag ho sakta hai.",
   "kb_ids": []
  }
 ],
 "options": [
  {
   "title": "Legal Notice Bhejein (General Practice)",
   "why": "Court jaane se pehle ek written notice dena aam practice hai jisse maalik ko amount aur deadline pata chale.",
   "steps": [
    "Ek likhit notice taiyar karein jismein deposit amount, flat chhodne ki tareekh, aur payment ki deadline likhi ho.",
    "Iske saath speed post receipt ya email ka saboot sambhal kar rakhein.",
    "Aap yeh notice khud bhi bhej sakte hain, iske liye lawyer hona zaroori nahi hai."
   ],
   "kb_ids": [
    "PROC-LEGAL-NOTICE"
   ]
  },
  {
   "title": "Muft Kanooni Sahayata (Free Legal Aid) Lein",
   "why": "Agar aapko aage lawyer ya kanooni madad ki zaroorat pade toh aap muft kanooni sahayata ke liye apply kar sakte hain.",
   "kb_ids": [
    "LSA1987-S12",
    "PROC-NALSA"
   ],
   "steps": [
    "District Legal Services Authority (DLSA) se district court mein ya toll-free helpline (15100) par sampark karein.",
    "Apni identity proof aur written application ke zariye muft madad ke liye apply karein."
   ]
  }
 ],
 "uncertainties": [
  "Kya Maharashtra state ne Model Tenancy Act, 2021 ke niyam apnaye hain, yeh is text se verify nahi hota.",
  "Kya painting ka kharcha kaatne ka koi clause agreement mein tha ya nahi, yeh assistant verify nahi kar sakta.",
  "Aapke case ki exact kanooni deadline kya hogi, iska poora faisla nahi kiya gaya hai."
 ],
 "suggest_lawyer": false,
 "lawyer_reason": ""
}
```

## Document: deposit_notice
Offered: yes
Drafting log: AI paragraph accepted

```text
**NOTICE: DEMAND FOR REFUND OF SECURITY DEPOSIT**

Date: [DATE OF SENDING]

To,
[LANDLORD'S FULL NAME]
[LANDLORD'S ADDRESS]

From,
[YOUR FULL NAME]
[YOUR CURRENT ADDRESS]

**Subject: Refund of security deposit for the house at [ADDRESS OF THE RENTED HOUSE], Pune**

Sir/Madam,

1. I vacated the premises on 31 August 2026, and I have photographs and a video taken at the time of leaving the flat as proof.

2. A security deposit of Rs 50,000 was paid, out of which only Rs 10,000 has been returned.

3. The landlord stated that he will deduct money for painting.

4. I requested the remaining amount twice on WhatsApp, but he replied that he will see.

As on the date of this notice, **Rs 40,000** out of the security deposit of Rs 50,000 has not been returned to me.

**My request:** poora deposit wapas. Please pay Rs 40,000 to me by [DEADLINE DATE YOU CHOOSE]. I will share my bank details on request.

If the amount is not paid, I may take the further steps available to me under law, including claiming compensation for the loss caused by the breach of our agreement (Section 73 of the Indian Contract Act, 1872).

Please treat this as a formal notice and keep it on record.

Yours faithfully,
[YOUR FULL NAME]
[YOUR PHONE NUMBER / EMAIL]

Documents I can provide: rent agreement, deposit UPI transfer, whatsapp chats, photos

```