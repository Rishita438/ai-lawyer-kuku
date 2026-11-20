# D01_deposit_hinglish_happy
**Category:** normal  
**Description:** Rs 50,000 deposit, Rs 10,000 returned, landlord blames painting. Notice should be drafted.  
**Pack:** deposit  
**Run at:** 2026-11-20T14:21:30  
**Models that answered:** gemini-3.5-flash-lite (22 calls)  
**Time:** 84.4 s

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

**Bot:** Makaan maalik ne deposit se kuch paise kaat kar aapko wapas diye hain. Kya yeh ghar tha jismein aap rehte the (dukaan, office ya business ki jagah nahi)?

**User:** haan ghar tha, family ke saath rehte the

**Bot:** Theek hai, aap wahan par apne parivar ke saath rehte the. Makaan maalik ne ab tak deposit mein se kitna wapas kiya hai? (Kuch nahi to 0 boliye.) (Aapne bataya: 10000 - sahi hai?)

**User:** 10000

**Bot:** Theek hai, maine ye note kar liya hai. Mahine ka kiraya kitna tha?

**User:** 15000

**Bot:** Theek hai, maine yeh amount note kar liya hai. Aapne kis date ko ghar khaali karke chaabi wapas di thi? (Aapne bataya: 2026-08-31 - sahi hai?)

**User:** 31 august 2026

**Bot:** Theek hai, mujhe yeh date mil gayi hai. Kya aapke paas likhit rent agreement hai? Agar haan, to usmein deposit wapas karne ke baare mein kya likha hai?

**User:** 11 mahine ka agreement hai, usmein likha hai deposit refundable hai

**Bot:** Theek hai, aapne bataya ki agreement 11 mahine ka tha aur deposit refundable likha hai. Kya aapke paas saboot hai ki aapne ghar theek haalat mein wapas kiya (photo, video, message ya handover note)?

**User:** flat chhodte waqt ki photos aur video hain

**Bot:** Aapke paas flat chhodne ke samay ki photos aur video hain. Kya aapne makaan maalik se deposit maanga hai? Agar haan, to kaise aur kab, aur unhone kya kaha?

**User:** whatsapp pe 2 baar maanga, bolta hai dekhenge

**Bot:** Aapne unse WhatsApp par baat ki hai. Aapke paas kya saboot hai? (rent agreement, deposit ki rasid, bank/UPI transfer, kiraye ki rasid, chats, photos) (Aapne bataya: photos, video - sahi hai?)

**User:** rent agreement, deposit ka UPI transfer, whatsapp chats, photos

**Bot:** Maine aapke paas rent agreement, UPI transfer ka saboot, WhatsApp chats aur photos hone ki baat note kar li hai. Aapko poora deposit wapas chahiye, ya kisi katauti ke baad jo aapko theek lagti hai?

**User:** poora deposit wapas

**Bot:** Maine samajh liya ki aap apna poora deposit wapas chahte hain.

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
   "deposit ka UPI transfer",
   "whatsapp chats",
   "photos",
   "video"
  ],
  "desired_outcome": "poora deposit wapas",
  "user_city_state": "Pune, Maharashtra"
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

Aapka makaan maalik bina kisi solid agreement clause ke deposit ke paise kaat raha hai jabki aapke paas agreement aur video/photos jaise saboot hain. Aap apna bacha hua paisa wapas maangne ke haqdaar hain, aur aap ek written notice bhej sakte hain ya legal help le sakte hain.

- Aapke paas 11 mahine ka written agreement hai jismein deposit refundable likha hai, isliye agar makaan maalik bina sahi wajah ke paise kaat raha hai toh aapko nuksaan ke liye compensation ya poora bacha hua paisa maangne ka haq hai.<br><small>📘 **Indian Contract Act, 1872, s. 73**: Compensation when a contract is broken — [source](https://indiacode.gov.in/act/0e782442-f035-4d53-aace-81b1552a8cf2/sections?spc.rpp=10&spc.sf=dc.date.issued&spc.sd=DESC&spc.page=8) (✅ verified 2026-11-19)</small>

- Aapke paas flat chhodne waqt ki photos, videos aur WhatsApp chats ke roop mein acche saboot maujood hain, jo yeh saabit karne mein madad karenge ki flat sahi haalat mein chhoda gaya tha.<br><small>📘 **Indian Contract Act, 1872, s. 73**: Compensation when a contract is broken — [source](https://indiacode.gov.in/act/0e782442-f035-4d53-aace-81b1552a8cf2/sections?spc.rpp=10&spc.sf=dc.date.issued&spc.sd=DESC&spc.page=8) (✅ verified 2026-11-19)</small>

- Aam taur par paise recover karne ke liye court jaane ki miyaad 3 saal tak hoti hai, aur abhi aapko flat chhode hue sirf thoda hi waqt hua hai.<br><small>📘 **Limitation Act, 1963, Schedule (Articles 7, 22, 55, 113 as examples)**: Time limit to sue for money — [source](https://indiacode.gov.in/server/api/core/bitstreams/ad4711f7-2ef9-41c3-8b7a-30050493cbb2/content) (✅ verified 2026-11-19)</small>

- Aapke state ke local rent laws alag ho sakte hain, aur national model law ke mutabiq residential deposit ki limit do mahine ke rent tak honi chahiye, lekin yeh state ke enact karne par nirbhar karta hai.<br><small>📘 **Model Tenancy Act, 2021, s. 11**: Security deposit cap and refund (ONLY in states that adopted it) — [source](https://www.mohua.gov.in/static/uploads/2025/11/9ada3e2d46992be72cabf7028d633b87.pdf) (✅ verified 2026-11-19)</small>

#### Key facts (calculated by the app, not the AI)

💰 **Amount still due:** Rs 40,000 (deposit Rs 50,000 - returned Rs 10,000).

⏳ **Time:** about 2 month(s) since you moved out. Most money claims must generally be filed in court within 3 years, but when that period starts depends on the facts - this assistant does not calculate an exact deadline.

ℹ️ **Background:** your deposit was more than two months' rent. The national *Model* Tenancy Act suggests a two-month cap for homes, but it binds only if your state has passed a law based on it - check your state's rent law.

🏠 **Note:** rent law is mostly state law. This assistant covers only general central law (contract and time limits), not your state's rent act.

<small>Based on: 📘 **Indian Contract Act, 1872, s. 73**: Compensation when a contract is broken — [source](https://indiacode.gov.in/act/0e782442-f035-4d53-aace-81b1552a8cf2/sections?spc.rpp=10&spc.sf=dc.date.issued&spc.sd=DESC&spc.page=8) (✅ verified 2026-11-19); 📘 **Limitation Act, 1963, Schedule (Articles 7, 22, 55, 113 as examples)**: Time limit to sue for money — [source](https://indiacode.gov.in/server/api/core/bitstreams/ad4711f7-2ef9-41c3-8b7a-30050493cbb2/content) (✅ verified 2026-11-19); 📘 **Model Tenancy Act, 2021, s. 11**: Security deposit cap and refund (ONLY in states that adopted it) — [source](https://www.mohua.gov.in/static/uploads/2025/11/9ada3e2d46992be72cabf7028d633b87.pdf) (✅ verified 2026-11-19)</small>

### Your options

**1. Legal Notice bhejein** — Yeh ek aam aur asardaar pehla kadam hai jisse makaan maalik par formal dabav banta hai.
   - Ek written notice taiyaar karein jismein deposit ki rakam, flat chhodne ki tareekh aur bacha hua paisa dene ki antim tareekh likhi ho.
   - Speed post ya email ke zariye notice bhejein aur uski receipt sambhal kar rakhein.
   - Aap ise khud bhi bhej sakte hain, iske liye lawyer hona zaroori nahi hai.

   <small>📝 *Send a legal notice first (general practice)* — general practice, not a legal rule (reviewed 2026-11-19)</small>

**2. Free Legal Aid (Muft Kanooni Sahayata) ki madad lein** — Agar aapko kanooni salah ya madad chahiye toh sarkar dwara muft sahayata uplabdh ho sakti hai.
   - Nirday ya District Legal Services Authority (DLSA) se sampark karein.
   - Helpline number 15100 par call karein ya NALSA ki website ke zariye aavedan karein.

   <small>📘 **Legal Services Authorities Act, 1987, s. 12**: Who can get free legal aid — [source](https://indiacode.gov.in/act/a742f03e-3129-4b8d-8dda-af2a36190b18/sections?spc.sf=dc.date.issued&spc.sd=DESC&spc.page=2&spc.rpp=10) (✅ verified 2026-11-19)<br>📘 **National Legal Services Authority**: How to reach free legal aid — [source](https://nalsa.gov.in/legal-aid/#Free-Legal-Aid) (✅ verified 2026-11-19)</small>

### ⚖️ When to get a real lawyer
- Agar makaan maalik legal notice ke baad bhi paise lautane se mana kar deta hai, toh civil court ya consumer forum mein aage ki karwayi ke liye ek vakeel ki zaroorat pad sakti hai.
- Free legal help may be available: District Legal Services Authority / NALSA helpline **15100**.

### What I'm not sure about
- Kya Maharashtra ke local rent laws ke tahat painting charges kaatne ka koi specific niyam hai, ise is assistant dwara verify nahi kiya gaya.
- Kya agreement mein painting ya maintenance ke naam par katoti karne ka koi clause tha, yeh fully clear nahi hai.

---
<small>Knowledge base last verified: 2026-11-19. Only verified sources are cited. This is general information, not legal advice.</small>

## Safety checker log (items removed from the AI's draft)
```json
[]
```

## Raw model JSON for the answer (before the safety checker)
```json
{
 "summary": "Aapka makaan maalik bina kisi solid agreement clause ke deposit ke paise kaat raha hai jabki aapke paas agreement aur video/photos jaise saboot hain. Aap apna bacha hua paisa wapas maangne ke haqdaar hain, aur aap ek written notice bhej sakte hain ya legal help le sakte hain.",
 "points": [
  {
   "text": "Aapke paas 11 mahine ka written agreement hai jismein deposit refundable likha hai, isliye agar makaan maalik bina sahi wajah ke paise kaat raha hai toh aapko nuksaan ke liye compensation ya poora bacha hua paisa maangne ka haq hai.",
   "kb_ids": [
    "ICA1872-S73"
   ]
  },
  {
   "text": "Aapke paas flat chhodne waqt ki photos, videos aur WhatsApp chats ke roop mein acche saboot maujood hain, jo yeh saabit karne mein madad karenge ki flat sahi haalat mein chhoda gaya tha.",
   "kb_ids": [
    "ICA1872-S73"
   ]
  },
  {
   "text": "Aam taur par paise recover karne ke liye court jaane ki miyaad 3 saal tak hoti hai, aur abhi aapko flat chhode hue sirf thoda hi waqt hua hai.",
   "kb_ids": [
    "LIM1963-MONEY"
   ]
  },
  {
   "text": "Aapke state ke local rent laws alag ho sakte hain, aur national model law ke mutabiq residential deposit ki limit do mahine ke rent tak honi chahiye, lekin yeh state ke enact karne par nirbhar karta hai.",
   "kb_ids": [
    "MTA2021-S11"
   ]
  }
 ],
 "options": [
  {
   "title": "Legal Notice bhejein",
   "why": "Yeh ek aam aur asardaar pehla kadam hai jisse makaan maalik par formal dabav banta hai.",
   "steps": [
    "Ek written notice taiyaar karein jismein deposit ki rakam, flat chhodne ki tareekh aur bacha hua paisa dene ki antim tareekh likhi ho.",
    "Speed post ya email ke zariye notice bhejein aur uski receipt sambhal kar rakhein.",
    "Aap ise khud bhi bhej sakte hain, iske liye lawyer hona zaroori nahi hai."
   ],
   "kb_ids": [
    "PROC-LEGAL-NOTICE"
   ]
  },
  {
   "title": "Free Legal Aid (Muft Kanooni Sahayata) ki madad lein",
   "why": "Agar aapko kanooni salah ya madad chahiye toh sarkar dwara muft sahayata uplabdh ho sakti hai.",
   "kb_ids": [
    "LSA1987-S12",
    "PROC-NALSA"
   ],
   "steps": [
    "Nirday ya District Legal Services Authority (DLSA) se sampark karein.",
    "Helpline number 15100 par call karein ya NALSA ki website ke zariye aavedan karein."
   ]
  }
 ],
 "uncertainties": [
  "Kya Maharashtra ke local rent laws ke tahat painting charges kaatne ka koi specific niyam hai, ise is assistant dwara verify nahi kiya gaya.",
  "Kya agreement mein painting ya maintenance ke naam par katoti karne ka koi clause tha, yeh fully clear nahi hai."
 ],
 "suggest_lawyer": true,
 "lawyer_reason": "Agar makaan maalik legal notice ke baad bhi paise lautane se mana kar deta hai, toh civil court ya consumer forum mein aage ki karwayi ke liye ek vakeel ki zaroorat pad sakti hai."
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

**Subject: Refund of security deposit for the house at [ADDRESS OF THE RENTED HOUSE], Pune, Maharashtra**

Sir/Madam,

1. I vacated the premises and handed over the flat on 31 August 2026, and I have photographs and a video taken at the time of leaving the flat as proof.

2. A security deposit of Rs 50,000 was paid by me, out of which only Rs 10,000 has been returned.

3. The landlord stated that he will deduct money for painting.

4. I asked for the remaining amount twice on WhatsApp, to which the landlord replied that he will see.

As on the date of this notice, **Rs 40,000** out of the security deposit of Rs 50,000 has not been returned to me.

**My request:** poora deposit wapas. Please pay Rs 40,000 to me by [DEADLINE DATE YOU CHOOSE]. I will share my bank details on request.

If the amount is not paid, I may take the further steps available to me under law, including claiming compensation for the loss caused by the breach of our agreement (Section 73 of the Indian Contract Act, 1872).

Please treat this as a formal notice and keep it on record.

Yours faithfully,
[YOUR FULL NAME]
[YOUR PHONE NUMBER / EMAIL]

Documents I can provide: rent agreement, deposit ka UPI transfer, whatsapp chats, photos, video

```