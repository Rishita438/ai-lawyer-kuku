# S01_salary_before_codes
**Category:** edge-law-change  
**Description:** Salary unpaid since September 2025 - before the Labour Codes (21 Nov 2025). Must flag old-law caveat.  
**Pack:** salary  
**Run at:** 2026-11-20T14:23:00  
**Models that answered:** gemini-3.5-flash-lite (19 calls)  
**Time:** 76.7 s

> Unedited output of scripts/run_tests.py. Nothing below was changed by hand.

## Automatic checks
| Check | Result | Detail |
|---|---|---|
| escalation | PASS | expected none, got none |
| lawyer flag | PASS | expected True, got True |
| cites expected KB entry | PASS | found ['COW2019-S17', 'COW2019-S45', 'NOTE-LABOUR-CODES'] of ['NOTE-LABOUR-CODES', 'COW2019-S17', 'COW2019-S45'] |

## Conversation
**Bot:** Tell me about your unpaid salary, in your own words - English, Hindi or Hinglish is fine. For example: who you work(ed) for, how many months are unpaid, and roughly how much.

**User:** meri company ne september 2025 se salary nahi di, 4 mahine ki 1.2 lakh baaki hai, maine december 2025 mein job chhod di

**Bot:** Aapki salary na milna aur job chhodne ki sthiti ko hum samajh rahe hain. Aapke employer (company ya vyakti) ka naam kya hai?

**User:** TechNova Solutions Pvt Ltd

**Bot:** Main samajh gaya hoon ki aap TechNova Solutions Pvt Ltd ke baare mein baat kar rahe hain. Kya yeh sarkari naukri hai (central ya state government)?

**User:** nahi, private company

**Bot:** Main samajh sakta hoon ki aap private company ki situation ke baare mein bata rahe hain. Kya aap abhi bhi wahan kaam kar rahe hain?

**User:** nahi, chhod di

**Bot:** Theek hai, aapne naukri chhod di hai. Wahan aapka aakhri working din kaunsa tha? (Aapne bataya: 2025-12-31 - sahi hai?)

**User:** 31 december 2025

**Bot:** Theek hai, main samajh gaya hoon ki aapko salary ke baare mein samasya aa rahi hai. Kis mahine se aapki salary nahi mili hai? (Aapne bataya: 2025-09-01 - sahi hai?)

**User:** september 2025

**Bot:** Maine aapka yeh time-frame note kar liya hai. Kya aapne employer se salary maangi hai? Agar haan, to kaise aur kab, aur unhone kya kaha?

**User:** HR ko 3 email kiye, bolte hain funds aane par denge

**Bot:** Aapne HR ko emails kiye aur unhone funds aane par dene ko kaha. Aapke paas kya saboot hai? (offer/appointment letter, payslips, bank statement, attendance record, emails ya chats)

**User:** offer letter, payslips, bank statement, emails

**Bot:** Maine aapke documents ki list note kar li hai. Aapka kaam ki jagah kis shehar aur state mein hai (ya thi)?

**User:** Noida, Uttar Pradesh

**Bot:** Maine Noida, Uttar Pradesh note kar liya hai.

## Case file (final)
```json
{
 "pack": "salary",
 "facts": {
  "employer_name": "TechNova Solutions Pvt Ltd",
  "govt_job": false,
  "still_employed": false,
  "last_working_day": "2025-12-31",
  "unpaid_since": "2025-09-01",
  "amount_due": 120000,
  "complaints_made": "HR ko 3 email kiye, bolte hain funds aane par denge",
  "evidence": [
   "offer letter",
   "payslips",
   "bank statement",
   "emails"
  ],
  "user_city_state": "Noida, Uttar Pradesh"
 },
 "language": "hinglish",
 "user_messages": [
  "meri company ne september 2025 se salary nahi di, 4 mahine ki 1.2 lakh baaki hai, maine december 2025 mein job chhod di",
  "TechNova Solutions Pvt Ltd",
  "nahi, private company",
  "nahi, chhod di",
  "31 december 2025",
  "september 2025",
  "HR ko 3 email kiye, bolte hain funds aane par denge",
  "offer letter, payslips, bank statement, emails",
  "Noida, Uttar Pradesh"
 ],
 "suggested": {
  "still_employed": false,
  "last_working_day": "2025-12-31",
  "unpaid_since": "2025-09-01"
 }
}
```

## Answer shown to the user

### Where you stand

Aapki TechNova Solutions Pvt Ltd mein September 2025 se [removed: unverified number] ki salary (₹1,20,000) baki hai aur aapne 31 December 2025 ko job chhod di hai. Aapke paas offer letter, payslips, bank statement aur emails jaise acche saboot hain, aur aap legal raste se apna paisa maang sakte hain.

- Jab koi employee job chhodta hai ya nikal diya jata hai, toh niyam ke mutabik uski baki salary do working days ke andar milni chahiye.<br><small>📘 **Code on Wages, 2019, s. 17**: Deadline for paying wages — [source](https://indiacode.gov.in/act/77a51a9b-c4c0-455c-809c-13d2efb3c8e5/sections?spc.rpp=10&spc.sf=dc.date.issued&spc.sd=DESC&spc.page=1) (✅ verified 2026-11-19)</small>

- Aapka unpaid salary ka mamla 21 November 2025 se pehle shuru hua tha, isliye purane aur naye labour laws ke apply hone ke bare mein thodi confusion ho sakti hai aur ise check karna zaroori hai.<br><small>📘 **Ministry of Labour and Employment (PIB release, 21 Nov 2025); Code on Wages, 2019 (Section 69)**: Labour law changed recently — [source](https://labour.gov.in/sites/default/files/pib2192463.pdf) (✅ verified 2026-11-19)</small>

- Aapke paas salary claim file karne ke liye samay hai, kyunki aam taur par claim claim uthne ke 3 saal ke andar daer kiya ja sakta hai.<br><small>📘 **Code on Wages, 2019, s. 45**: Filing a wage claim with the authority — [source](https://indiacode.gov.in/act/77a51a9b-c4c0-455c-809c-13d2efb3c8e5/sections?spc.rpp=10&spc.sf=dc.date.issued&spc.sd=DESC&spc.page=5) (✅ verified 2026-11-19)</small>

- Aap employer ko written demand letter bhej sakte hain jismein baki mahino ki list, exact amount aur deadline ho. Yeh ek aam aur achhi shuruat hai, halanki yeh koi kanooni requirement nahi hai.<br><small>📝 *Send a written demand first (general practice)* — general practice, not a legal rule (reviewed 2026-11-19)</small>

#### Key facts (calculated by the app, not the AI)

⚖️ **Which law:** your unpaid salary started before 21 November 2025, when the new Labour Codes came into force - the older law may still matter for your claim.

💼 **Final dues:** when someone leaves, resigns or is removed, wages due must be paid within two working days.

⏳ **Time:** salary unpaid for about 14 month(s). A wage claim can generally be filed within 3 years from when it arose; the law does not define the exact start, so this assistant does not calculate a deadline.

<small>Based on: 📘 **Code on Wages, 2019, s. 17**: Deadline for paying wages — [source](https://indiacode.gov.in/act/77a51a9b-c4c0-455c-809c-13d2efb3c8e5/sections?spc.rpp=10&spc.sf=dc.date.issued&spc.sd=DESC&spc.page=1) (✅ verified 2026-11-19); 📘 **Code on Wages, 2019, s. 45**: Filing a wage claim with the authority — [source](https://indiacode.gov.in/act/77a51a9b-c4c0-455c-809c-13d2efb3c8e5/sections?spc.rpp=10&spc.sf=dc.date.issued&spc.sd=DESC&spc.page=5) (✅ verified 2026-11-19); 📘 **Ministry of Labour and Employment (PIB release, 21 Nov 2025); Code on Wages, 2019 (Section 69)**: Labour law changed recently — [source](https://labour.gov.in/sites/default/files/pib2192463.pdf) (✅ verified 2026-11-19)</small>

### Your options

**1. Written Demand Bhejna** — HR aur management ko ek final formal email ya letter bhejein jismein saaf likha ho ki ₹1,20,000 kab tak dena hai.
   - Apne offer letter, payslips, bank statements aur pehle ki gayi emails ko ek jagah collect karein.
   - HR aur manager ko ek written message ya email bhejein jismein amount aur deadline ho.
   - Reply ke liye kuch dino ka wait karein aur agar payment na aaye toh agla kadam uthayein.

   <small>📝 *Send a written demand first (general practice)* — general practice, not a legal rule (reviewed 2026-11-19)</small>

**2. Labour Authority ke Paas Claim File Karna** — Agar employer funds nahi de raha, toh aap appointed authority ke paas wage claim file kar sakte hain.
   - Apne sare saboot (payslips, emails, bank statement) taiyar rakhein.
   - Wahan ke niyam ke mutabik labour authority mein wage claim ka application submit karein.
   - Authority ki sunwayi mein hissa lein; agar employer nahi manta hai, toh recovery certificate ke zariye paisa vasool karne ki koshish ki ja sakti hai.

   <small>📘 **Code on Wages, 2019, s. 45**: Filing a wage claim with the authority — [source](https://indiacode.gov.in/act/77a51a9b-c4c0-455c-809c-13d2efb3c8e5/sections?spc.rpp=10&spc.sf=dc.date.issued&spc.sd=DESC&spc.page=5) (✅ verified 2026-11-19)<br>📝 *Send a written demand first (general practice)* — general practice, not a legal rule (reviewed 2026-11-19)</small>

**3. Muft Kanooni Madad (Free Legal Aid) Lena** — Agar aapko kanooni salah ya madad chahiye, toh aap NALSA ya District Legal Services Authority se muft mein sahayta le sakte hain.
   - Toll-free helpline 15100 par call karein ya apne nazdiki District Legal Services Authority se sampark karein.
   - Apne identity proof aur employment ke saboot ke sath application dein.

   <small>📘 **Legal Services Authorities Act, 1987, s. 12**: Who can get free legal aid — [source](https://indiacode.gov.in/act/a742f03e-3129-4b8d-8dda-af2a36190b18/sections?spc.sf=dc.date.issued&spc.sd=DESC&spc.page=2&spc.rpp=10) (✅ verified 2026-11-19)<br>📘 **National Legal Services Authority**: How to reach free legal aid — [source](https://nalsa.gov.in/legal-aid/#Free-Legal-Aid) (✅ verified 2026-11-19)</small>

### ⚖️ When to get a real lawyer
- Your unpaid salary started before the Labour Codes came into force (21 Nov 2025). Which law applies can be tricky - check with your local Labour Office or a lawyer.
- Your unpaid salary started before the Labour Codes came into force (21 Nov 2025). Which law applies can be tricky - check with your local Labour Office or a lawyer.
- Free legal help may be available: District Legal Services Authority / NALSA helpline **15100**.

### What I'm not sure about
- Kyunki yeh mamla 21 November 2025 se pehle ka hai, yeh verify karna zaroori hai ki is par purana law poori tarah lagu hoga ya naya, isliye kisi vakil ya local Labour Office se salah lena behtar hoga.
- Uttar Pradesh (Noida) ke state-specific rules aur appropriate Government ki notifications ke tahat time limits mein kya badlav hain, iski puri jankari yahan uplabdh nahi hai.

---
<small>Knowledge base last verified: 2026-11-19. Only verified sources are cited. The safety checker removed 1 unverified item(s) from the AI's draft. This is general information, not legal advice.</small>

## Safety checker log (items removed from the AI's draft)
```json
[
 {
  "type": "number",
  "text": "4 mahine"
 }
]
```

## Raw model JSON for the answer (before the safety checker)
```json
{
 "summary": "Aapki TechNova Solutions Pvt Ltd mein September 2025 se 4 mahine ki salary (₹1,20,000) baki hai aur aapne 31 December 2025 ko job chhod di hai. Aapke paas offer letter, payslips, bank statement aur emails jaise acche saboot hain, aur aap legal raste se apna paisa maang sakte hain.",
 "points": [
  {
   "text": "Jab koi employee job chhodta hai ya nikal diya jata hai, toh niyam ke mutabik uski baki salary do working days ke andar milni chahiye.",
   "kb_ids": [
    "COW2019-S17"
   ]
  },
  {
   "text": "Aapka unpaid salary ka mamla 21 November 2025 se pehle shuru hua tha, isliye purane aur naye labour laws ke apply hone ke bare mein thodi confusion ho sakti hai aur ise check karna zaroori hai.",
   "kb_ids": [
    "NOTE-LABOUR-CODES"
   ]
  },
  {
   "text": "Aapke paas salary claim file karne ke liye samay hai, kyunki aam taur par claim claim uthne ke 3 saal ke andar daer kiya ja sakta hai.",
   "kb_ids": [
    "COW2019-S45"
   ]
  },
  {
   "text": "Aap employer ko written demand letter bhej sakte hain jismein baki mahino ki list, exact amount aur deadline ho. Yeh ek aam aur achhi shuruat hai, halanki yeh koi kanooni requirement nahi hai.",
   "kb_ids": [
    "PROC-DEMAND-LETTER"
   ]
  }
 ],
 "options": [
  {
   "title": "Written Demand Bhejna",
   "why": "HR aur management ko ek final formal email ya letter bhejein jismein saaf likha ho ki ₹1,20,000 kab tak dena hai.",
   "steps": [
    "Apne offer letter, payslips, bank statements aur pehle ki gayi emails ko ek jagah collect karein.",
    "HR aur manager ko ek written message ya email bhejein jismein amount aur deadline ho.",
    "Reply ke liye kuch dino ka wait karein aur agar payment na aaye toh agla kadam uthayein."
   ],
   "kb_ids": [
    "PROC-DEMAND-LETTER"
   ]
  },
  {
   "title": "Labour Authority ke Paas Claim File Karna",
   "why": "Agar employer funds nahi de raha, toh aap appointed authority ke paas wage claim file kar sakte hain.",
   "steps": [
    "Apne sare saboot (payslips, emails, bank statement) taiyar rakhein.",
    "Wahan ke niyam ke mutabik labour authority mein wage claim ka application submit karein.",
    "Authority ki sunwayi mein hissa lein; agar employer nahi manta hai, toh recovery certificate ke zariye paisa vasool karne ki koshish ki ja sakti hai."
   ],
   "kb_ids": [
    "COW2019-S45",
    "PROC-DEMAND-LETTER"
   ]
  },
  {
   "title": "Muft Kanooni Madad (Free Legal Aid) Lena",
   "why": "Agar aapko kanooni salah ya madad chahiye, toh aap NALSA ya District Legal Services Authority se muft mein sahayta le sakte hain.",
   "steps": [
    "Toll-free helpline 15100 par call karein ya apne nazdiki District Legal Services Authority se sampark karein.",
    "Apne identity proof aur employment ke saboot ke sath application dein."
   ],
   "kb_ids": [
    "LSA1987-S12",
    "PROC-NALSA"
   ]
  }
 ],
 "uncertainties": [
  "Kyunki yeh mamla 21 November 2025 se pehle ka hai, yeh verify karna zaroori hai ki is par purana law poori tarah lagu hoga ya naya, isliye kisi vakil ya local Labour Office se salah lena behtar hoga.",
  "Uttar Pradesh (Noida) ke state-specific rules aur appropriate Government ki notifications ke tahat time limits mein kya badlav hain, iski puri jankari yahan uplabdh nahi hai."
 ],
 "suggest_lawyer": true,
 "lawyer_reason": "Your unpaid salary started before the Labour Codes came into force (21 Nov 2025). Which law applies can be tricky - check with your local Labour Office or a lawyer."
}
```