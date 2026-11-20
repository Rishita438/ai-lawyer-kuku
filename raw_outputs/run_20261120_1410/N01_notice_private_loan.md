# N01_notice_private_loan
**Category:** normal  
**Description:** Lawyer's notice from a lending app demanding repayment within 15 days. Explain, don't stop.  
**Pack:** notice  
**Run at:** 2026-11-20T14:23:35  
**Models that answered:** gemini-3.5-flash-lite (9 calls)  
**Time:** 34.5 s

> Unedited output of scripts/run_tests.py. Nothing below was changed by hand.

## Automatic checks
| Check | Result | Detail |
|---|---|---|
| escalation | PASS | expected none, got none |
| cites expected KB entry | PASS | found ['PROC-NOTICE-PRIVATE'] of ['PROC-NOTICE-PRIVATE'] |

## Conversation
**Bot:** Tell me about the notice you received, in your own words - English, Hindi or Hinglish is fine. For example: who sent it, what it asks you to do, and whether it gives a date. (Please don't paste personal details like your address or account numbers.)

**User:** mujhe ek loan app ke vakil ka legal notice aaya hai, 18000 rupaye 15 din mein bharne ko bol rahe hain, nahi to case karenge

**Bot:** Loan app ke vakil se legal notice aane ki baat suni maine. Kya yeh notice court, police, kisi tribunal/commission, ya sarkari ya tax office se aaya hai?

**User:** nahi, police se nahi, vakil ka notice hai

**Bot:** Theik hai, yeh police se nahi balki vakil ka notice hai. Aapko notice kis date ko mila?

**User:** 18 november 2026

**Bot:** Theek hai, maine yeh note kar liya hai. Kya notice mein koi deadline di gayi hai? Agar haan, to kis date tak (ya kitne din mein)? (Aapne bataya: 2026-12-03 - sahi hai?)

**User:** 15 din mein, yaani 3 december 2026

**Bot:** Maine ye note kar liya hai.

## Case file (final)
```json
{
 "pack": "notice",
 "facts": {
  "official_sender": false,
  "sender": "loan app ke vakil",
  "about": "loan",
  "what_it_demands": "18000 rupaye bharne ko bol rahe hain, nahi to case karenge",
  "received_date": "2026-11-18",
  "deadline_in_notice": "2026-12-03"
 },
 "language": "hinglish",
 "user_messages": [
  "mujhe ek loan app ke vakil ka legal notice aaya hai, 18000 rupaye 15 din mein bharne ko bol rahe hain, nahi to case karenge",
  "nahi, police se nahi, vakil ka notice hai",
  "18 november 2026",
  "15 din mein, yaani 3 december 2026"
 ],
 "suggested": {
  "official_sender": false,
  "deadline_in_notice": "2026-12-03"
 }
}
```

## Answer shown to the user

### Where you stand

Aapko kisi loan app ke vakil ki taraf se ek legal notice mila hai jisme 18,000 rupaye bharne ki maang ki gayi hai. Yaad rakhiye ki yeh ek formal demand hai, kisi court ka order nahi hai, lekin isko bina dekhe ignore nahi karna chahiye.

- Aapko jo notice mila hai, woh kisi court, police ya government authority ka order nahi hai, balki ek private lawyer ya company ki formal demand hai. Yeh general practice ke taur par bataya ja raha hai.<br><small>📝 *A legal notice from a person or company is not a court order (general practice)* — general practice, not a legal rule (reviewed 2026-11-19)</small>

- Notice ke sath aaye envelope aur kisi bhi aise saboot ko sambhal kar rakhiye jisse yeh pata chale ki aapko yeh notice kis tarikh ko mila tha.<br><small>📝 *A legal notice from a person or company is not a court order (general practice)* — general practice, not a legal rule (reviewed 2026-11-19)</small>

- Kuch khaas categories ke log (jaise mahilaein, SC/ST sadasya, ya jinki aay rajya sarkar ki tay seema se kam hai) free legal aid ke liye paatra ho sakte hain.<br><small>📘 **Legal Services Authorities Act, 1987, s. 12**: Who can get free legal aid — [source](https://indiacode.gov.in/act/a742f03e-3129-4b8d-8dda-af2a36190b18/sections?spc.sf=dc.date.issued&spc.sd=DESC&spc.page=2&spc.rpp=10) (✅ verified 2026-11-19)</small>

- Free legal aid ke liye aap District Legal Services Authority (DLSA) se sampark kar sakte hain, jiska toll-free helpline number 15100 hai.<br><small>📘 **National Legal Services Authority**: How to reach free legal aid — [source](https://nalsa.gov.in/legal-aid/#Free-Legal-Aid) (✅ verified 2026-11-19)</small>

#### Key facts (calculated by the app, not the AI)

📨 **Who sent it:** a private party (not a court or government). A legal notice like this is a formal demand, not a court order.

📅 **Deadline:** 2026-12-03 - 13 day(s) from today.

<small>Based on: 📘 **National Legal Services Authority (for legal aid route)**: Court, police, tribunal or government notices need a lawyer — [source](https://nalsa.gov.in/legal-aid/) (✅ verified 2026-11-19); 📝 *A legal notice from a person or company is not a court order (general practice)* — general practice, not a legal rule (reviewed 2026-11-19)</small>

### Your options

**1. Notice aur envelope ko surakshit rakhein** — Yeh dekhne ke liye ki aapko notice kab mila, envelope aur uske saboot zaruri hain.
   - Notice aur uske envelope ko sambhal kar ek jagah rakhein.
   - Praapt hone ki tarikh ko note kar lein.

   <small>📝 *A legal notice from a person or company is not a court order (general practice)* — general practice, not a legal rule (reviewed 2026-11-19)</small>

**2. Vakil ya salahkar se salah lein** — Jawab dene se pehle kisi expert ki rai lena behtar hota hai.
   - Notice ko lekar kisi vakil ya legal advisor se milein.
   - Deadline se pehle apni aage ki ranniti tay karein.

   <small>📝 *A legal notice from a person or company is not a court order (general practice)* — general practice, not a legal rule (reviewed 2026-11-19)</small>

**3. Muft kanooni sahayta (Free Legal Aid) ke liye sampark karein** — Agar aapko sahayta ki zarurat hai aur aap paatra hain, toh aap muft madat le sakte hain.
   - Helpline number 15100 par call karein.
   - Apne nazdeek ke District Legal Services Authority (DLSA) mein sampark karein.

   <small>📘 **Legal Services Authorities Act, 1987, s. 12**: Who can get free legal aid — [source](https://indiacode.gov.in/act/a742f03e-3129-4b8d-8dda-af2a36190b18/sections?spc.sf=dc.date.issued&spc.sd=DESC&spc.page=2&spc.rpp=10) (✅ verified 2026-11-19)<br>📘 **National Legal Services Authority**: How to reach free legal aid — [source](https://nalsa.gov.in/legal-aid/#Free-Legal-Aid) (✅ verified 2026-11-19)</small>

### ⚖️ When to get a real lawyer
- Kyunki yeh ek legal notice hai jisme paise maange gaye hain aur deadline di gayi hai, isliye kisi vakil se salah lena aapke liye surakshit rahega.
- Free legal help may be available: District Legal Services Authority / NALSA helpline **15100**.

### What I'm not sure about
- Kya yeh loan app RBI dwara registerd hai ya nahi, iski jankari is notice mein spasht nahi hai.
- Kya is loan ke silsile mein pehle koi aur batcheet ya agreement hui thi, yeh bhi yahan spasht nahi hai.

---
<small>Knowledge base last verified: 2026-11-19. Only verified sources are cited. This is general information, not legal advice.</small>

## Safety checker log (items removed from the AI's draft)
```json
[]
```

## Raw model JSON for the answer (before the safety checker)
```json
{
 "summary": "Aapko kisi loan app ke vakil ki taraf se ek legal notice mila hai jisme 18,000 rupaye bharne ki maang ki gayi hai. Yaad rakhiye ki yeh ek formal demand hai, kisi court ka order nahi hai, lekin isko bina dekhe ignore nahi karna chahiye.",
 "points": [
  {
   "text": "Aapko jo notice mila hai, woh kisi court, police ya government authority ka order nahi hai, balki ek private lawyer ya company ki formal demand hai. Yeh general practice ke taur par bataya ja raha hai.",
   "kb_ids": [
    "PROC-NOTICE-PRIVATE"
   ]
  },
  {
   "text": "Notice ke sath aaye envelope aur kisi bhi aise saboot ko sambhal kar rakhiye jisse yeh pata chale ki aapko yeh notice kis tarikh ko mila tha.",
   "kb_ids": [
    "PROC-NOTICE-PRIVATE"
   ]
  },
  {
   "text": "Kuch khaas categories ke log (jaise mahilaein, SC/ST sadasya, ya jinki aay rajya sarkar ki tay seema se kam hai) free legal aid ke liye paatra ho sakte hain.",
   "kb_ids": [
    "LSA1987-S12"
   ]
  },
  {
   "text": "Free legal aid ke liye aap District Legal Services Authority (DLSA) se sampark kar sakte hain, jiska toll-free helpline number 15100 hai.",
   "kb_ids": [
    "PROC-NALSA"
   ]
  }
 ],
 "options": [
  {
   "title": "Notice aur envelope ko surakshit rakhein",
   "why": "Yeh dekhne ke liye ki aapko notice kab mila, envelope aur uske saboot zaruri hain.",
   "steps": [
    "Notice aur uske envelope ko sambhal kar ek jagah rakhein.",
    "Praapt hone ki tarikh ko note kar lein."
   ],
   "kb_ids": [
    "PROC-NOTICE-PRIVATE"
   ]
  },
  {
   "title": "Vakil ya salahkar se salah lein",
   "why": "Jawab dene se pehle kisi expert ki rai lena behtar hota hai.",
   "steps": [
    "Notice ko lekar kisi vakil ya legal advisor se milein.",
    "Deadline se pehle apni aage ki ranniti tay karein."
   ],
   "kb_ids": [
    "PROC-NOTICE-PRIVATE"
   ]
  },
  {
   "title": "Muft kanooni sahayta (Free Legal Aid) ke liye sampark karein",
   "why": "Agar aapko sahayta ki zarurat hai aur aap paatra hain, toh aap muft madat le sakte hain.",
   "kb_ids": [
    "LSA1987-S12",
    "PROC-NALSA"
   ],
   "steps": [
    "Helpline number 15100 par call karein.",
    "Apne nazdeek ke District Legal Services Authority (DLSA) mein sampark karein."
   ]
  }
 ],
 "uncertainties": [
  "Kya yeh loan app RBI dwara registerd hai ya nahi, iski jankari is notice mein spasht nahi hai.",
  "Kya is loan ke silsile mein pehle koi aur batcheet ya agreement hui thi, yeh bhi yahan spasht nahi hai."
 ],
 "suggest_lawyer": true,
 "lawyer_reason": "Kyunki yeh ek legal notice hai jisme paise maange gaye hain aur deadline di gayi hai, isliye kisi vakil se salah lena aapke liye surakshit rahega."
}
```