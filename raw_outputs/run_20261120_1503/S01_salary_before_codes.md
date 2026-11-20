# S01_salary_before_codes
**Category:** edge-law-change  
**Description:** Salary unpaid since September 2025 - before the Labour Codes (21 Nov 2025). Must flag old-law caveat.  
**Pack:** salary  
**Run at:** 2026-11-20T15:14:46  
**Models that answered:** openai/gpt-oss-120b (19 calls)  
**Time:** 160.2 s

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

**Bot:** मैं समझ रहा हूँ कि आप अपनी वेतन के बारे में बता रहे हैं। आपके नियोक्ता (कंपनी या व्यक्ति) का नाम क्या है?

**User:** TechNova Solutions Pvt Ltd

**Bot:** Aapne TechNova Solutions Pvt Ltd ka zikr kiya. Kya yeh sarkari naukri hai (central ya state government)?

**User:** nahi, private company

**Bot:** Samajh gaya, aap private company mein kaam karte the. Kya aap abhi bhi wahan kaam kar rahe hain?

**User:** nahi, chhod di

**Bot:** Samajh gaya, aapne kaam chhod diya. Wahan aapka aakhri working din kaunsa tha? (Aapne bataya: 2025-12-01 - sahi hai?)

**User:** 31 december 2025

**Bot:** Samajh gaya aapka sandesh. Kis mahine se aapki salary nahi mili hai? (Aapne bataya: 2025-09-01 - sahi hai?)

**User:** september 2025

**Bot:** Aapke bataye gaye baare mein dhyan diya hai. Kya aapne employer se salary maangi hai? Agar haan, to kaise aur kab, aur unhone kya kaha?

**User:** HR ko 3 email kiye, bolte hain funds aane par denge

**Bot:** मैं समझता हूँ कि आपने HR को कई ईमेल भेजे हैं। आपके पास क्या सबूत है? (ऑफ़र/नियुक्ति पत्र, सैलरी स्लिप, बैंक स्टेटमेंट, हाज़िरी रिकॉर्ड, ईमेल या चैट)

**User:** offer letter, payslips, bank statement, emails

**Bot:** मैं समझता हूँ कि आपने ये दस्तावेज़ एकत्र किए हैं। आपके काम की जगह किस शहर और राज्य में है (या थी)?

**User:** Noida, Uttar Pradesh

**Bot:** धन्यवाद, अब हमारे पास आपके मामले की मुख्य जानकारी है।

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
 "language": "hi",
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
  "last_working_day": "2025-12-01",
  "unpaid_since": "2025-09-01"
 }
}
```

## Answer shown to the user

### Where you stand

आपकी कंपनी को आपके नौकरी छोड़ने के दो कार्यदिवसों के भीतर बकाया वेतन देना था, लेकिन नहीं दिया। आप अभी भी तीन साल के भीतर एक वेतन दावा दायर कर सकते हैं, पर यह स्पष्ट नहीं है कि कौन सा कानून लागू होता है क्योंकि वेतन का बकाया 21 नवम्बर 2025 से पहले शुरू हुआ था।

- नौकरी छोड़ने के बाद दो कार्यदिवसों के भीतर बकाया वेतन देना नियोक्ता की कानूनी ज़िम्मेदारी है, और यह अभी तक पूरा नहीं हुआ है।<br><small>📘 **Code on Wages, 2019, s. 17**: Deadline for paying wages — [source](https://indiacode.gov.in/act/77a51a9b-c4c0-455c-809c-13d2efb3c8e5/sections?spc.rpp=10&spc.sf=dc.date.issued&spc.sd=DESC&spc.page=1) (✅ verified 2026-11-19)</small>

- आपके पास वेतन दावा दायर करने का अधिकार है; ऐसा दावा आम तौर पर घटना के तीन साल के भीतर दायर किया जा सकता है और आपका मामला इस सीमा में है।<br><small>📘 **Code on Wages, 2019, s. 45**: Filing a wage claim with the authority — [source](https://indiacode.gov.in/act/77a51a9b-c4c0-455c-809c-13d2efb3c8e5/sections?spc.rpp=10&spc.sf=dc.date.issued&spc.sd=DESC&spc.page=5) (✅ verified 2026-11-19)</small>

- बकाया वेतन 21 नवम्बर 2025 से पहले शुरू हुआ, इसलिए यह स्पष्ट नहीं है कि नया कोड या पुराना कानून लागू होगा; स्थानीय लेबर ऑफिस या वकील से पुष्टि आवश्यक है।<br><small>📘 **Ministry of Labour and Employment (PIB release, 21 Nov 2025); Code on Wages, 2019 (Section 69)**: Labour law changed recently — [source](https://labour.gov.in/sites/default/files/pib2192463.pdf) (✅ verified 2026-11-19)</small>

- पहला सामान्य कदम लिखित मांग पत्र (या ई‑मेल) भेजना है, जिसमें बकाया राशि, महीनों की सूची और भुगतान की अंतिम तिथि बताई जाए; यह कानूनी आवश्यकता नहीं, पर आपके दावे को मजबूत करता है।<br><small>📝 *Send a written demand first (general practice)* — general practice, not a legal rule (reviewed 2026-11-19)</small>

- यदि आपकी आय सीमा या सामाजिक वर्ग मानदंडों के तहत आप आते हैं, तो मुफ्त कानूनी सहायता प्राप्त करने की संभावना है।<br><small>📘 **Legal Services Authorities Act, 1987, s. 12**: Who can get free legal aid — [source](https://indiacode.gov.in/act/a742f03e-3129-4b8d-8dda-af2a36190b18/sections?spc.sf=dc.date.issued&spc.sd=DESC&spc.page=2&spc.rpp=10) (✅ verified 2026-11-19)</small>

#### Key facts (calculated by the app, not the AI)

⚖️ **Which law:** your unpaid salary started before 21 November 2025, when the new Labour Codes came into force - the older law may still matter for your claim.

💼 **Final dues:** when someone leaves, resigns or is removed, wages due must be paid within two working days.

⏳ **Time:** salary unpaid for about 14 month(s). A wage claim can generally be filed within 3 years from when it arose; the law does not define the exact start, so this assistant does not calculate a deadline.

<small>Based on: 📘 **Code on Wages, 2019, s. 17**: Deadline for paying wages — [source](https://indiacode.gov.in/act/77a51a9b-c4c0-455c-809c-13d2efb3c8e5/sections?spc.rpp=10&spc.sf=dc.date.issued&spc.sd=DESC&spc.page=1) (✅ verified 2026-11-19); 📘 **Code on Wages, 2019, s. 45**: Filing a wage claim with the authority — [source](https://indiacode.gov.in/act/77a51a9b-c4c0-455c-809c-13d2efb3c8e5/sections?spc.rpp=10&spc.sf=dc.date.issued&spc.sd=DESC&spc.page=5) (✅ verified 2026-11-19); 📘 **Ministry of Labour and Employment (PIB release, 21 Nov 2025); Code on Wages, 2019 (Section 69)**: Labour law changed recently — [source](https://labour.gov.in/sites/default/files/pib2192463.pdf) (✅ verified 2026-11-19)</small>

### Your options

**1. लिखित मांग पत्र भेजें** — सबसे तेज़ और कम लागत वाला कदम, जिससे आप अपना दावा औपचारिक रूप से दर्ज कर सकते हैं।
   - एक पत्र/ई‑मेल में बकाया राशि, महीनों की सूची और दो कार्यदिवसों के भीतर भुगतान की अंतिम तिथि लिखें।
   - सभी प्रमाण (ऑफ़र लेटर, पेस्लिप, बैंक स्टेटमेंट, ई‑मेल) संलग्न करें।
   - एक प्रति अपने पास रखें और ई‑मेल के रीड रसीद को सुरक्षित रखें।

   <small>📝 *Send a written demand first (general practice)* — general practice, not a legal rule (reviewed 2026-11-19)</small>

**2. लेबर अथॉरिटी में वेतन दावा दायर करें** — यदि मांग पत्र के बाद भी भुगतान नहीं होता, तो आधिकारिक निकाय से वसूली की प्रक्रिया शुरू की जा सकती है।
   - ऑफ़र लेटर, पेस्लिप, बैंक स्टेटमेंट, ई‑मेल आदि सभी दस्तावेज़ इकट्ठा करें।
   - स्थानीय लेबर अथॉरिटी (गजेटेड अधिकारी स्तर) की वेबसाइट या कार्यालय से आवेदन फ़ॉर्म प्राप्त करें।
   - आवेदन फ़ॉर्म भरें और सभी दस्तावेज़ संलग्न करके जमा करें (ऑनलाइन या व्यक्तिगत)।
   - आवेदन की रसीद रखें; अथॉरिटी को तीन महीने के भीतर निर्णय देना होता है।

   <small>📘 **Code on Wages, 2019, s. 45**: Filing a wage claim with the authority — [source](https://indiacode.gov.in/act/77a51a9b-c4c0-455c-809c-13d2efb3c8e5/sections?spc.rpp=10&spc.sf=dc.date.issued&spc.sd=DESC&spc.page=5) (✅ verified 2026-11-19)</small>

**3. मुफ़्त कानूनी सहायता प्राप्त करें** — यदि आप आय सीमा या सामाजिक वर्ग मानदंडों के तहत आते हैं, तो आप बिना खर्च के वकील की मदद ले सकते हैं।
   - नालसा हेल्पलाइन 15100 पर कॉल करें या नालसा की वेबसाइट पर जाएँ।
   - आवश्यक पहचान प्रमाण और यदि हो तो वर्ग प्रमाणपत्र तैयार रखें।
   - नजदीकी तालुका/जिला/राज्य कानूनी सेवा प्राधिकरण में लिखित या मौखिक आवेदन दें।
   - सहायता मिलने पर वकील के साथ आगे की प्रक्रिया (जैसे दावा दायर करना) आगे बढ़ाएँ।

   <small>📘 **Legal Services Authorities Act, 1987, s. 12**: Who can get free legal aid — [source](https://indiacode.gov.in/act/a742f03e-3129-4b8d-8dda-af2a36190b18/sections?spc.sf=dc.date.issued&spc.sd=DESC&spc.page=2&spc.rpp=10) (✅ verified 2026-11-19)<br>📘 **National Legal Services Authority**: How to reach free legal aid — [source](https://nalsa.gov.in/legal-aid/#Free-Legal-Aid) (✅ verified 2026-11-19)</small>

### ⚖️ When to get a real lawyer
- Your unpaid salary started before the Labour Codes came into force (21 Nov 2025). Which law applies can be tricky - check with your local Labour Office or a lawyer.
- क्योंकि आपका वेतन बकाया नई कोड के लागू होने से पहले शुरू हुआ है, इसलिए लागू कानून की पहचान और संभावित राज्य‑विशिष्ट प्रक्रियाओं के लिए वकील की सलाह आवश्यक है।
- Free legal help may be available: District Legal Services Authority / NALSA helpline **15100**.

### What I'm not sure about
- बकाया वेतन पर कौन सा विशेष कानून (पुराना या नया कोड) लागू होगा, यह स्पष्ट नहीं है; राज्य‑विशिष्ट नियम भी अलग हो सकते हैं।
- दावे की सटीक समय सीमा (कब से गिनना शुरू करना है) का निर्धारण इस सहायक द्वारा नहीं किया गया है।

---
<small>Knowledge base last verified: 2026-11-19. Only verified sources are cited. This is general information, not legal advice.</small>

## Safety checker log (items removed from the AI's draft)
```json
[]
```

## Raw model JSON for the answer (before the safety checker)
```json
{
 "summary": "आपकी कंपनी को आपके नौकरी छोड़ने के दो कार्यदिवसों के भीतर बकाया वेतन देना था, लेकिन नहीं दिया। आप अभी भी तीन साल के भीतर एक वेतन दावा दायर कर सकते हैं, पर यह स्पष्ट नहीं है कि कौन सा कानून लागू होता है क्योंकि वेतन का बकाया 21 नवम्बर 2025 से पहले शुरू हुआ था।",
 "points": [
  {
   "text": "नौकरी छोड़ने के बाद दो कार्यदिवसों के भीतर बकाया वेतन देना नियोक्ता की कानूनी ज़िम्मेदारी है, और यह अभी तक पूरा नहीं हुआ है।",
   "kb_ids": [
    "COW2019-S17"
   ]
  },
  {
   "text": "आपके पास वेतन दावा दायर करने का अधिकार है; ऐसा दावा आम तौर पर घटना के तीन साल के भीतर दायर किया जा सकता है और आपका मामला इस सीमा में है।",
   "kb_ids": [
    "COW2019-S45"
   ]
  },
  {
   "text": "बकाया वेतन 21 नवम्बर 2025 से पहले शुरू हुआ, इसलिए यह स्पष्ट नहीं है कि नया कोड या पुराना कानून लागू होगा; स्थानीय लेबर ऑफिस या वकील से पुष्टि आवश्यक है।",
   "kb_ids": [
    "NOTE-LABOUR-CODES"
   ]
  },
  {
   "text": "पहला सामान्य कदम लिखित मांग पत्र (या ई‑मेल) भेजना है, जिसमें बकाया राशि, महीनों की सूची और भुगतान की अंतिम तिथि बताई जाए; यह कानूनी आवश्यकता नहीं, पर आपके दावे को मजबूत करता है।",
   "kb_ids": [
    "PROC-DEMAND-LETTER"
   ]
  },
  {
   "text": "यदि आपकी आय सीमा या सामाजिक वर्ग मानदंडों के तहत आप आते हैं, तो मुफ्त कानूनी सहायता प्राप्त करने की संभावना है।",
   "kb_ids": [
    "LSA1987-S12"
   ]
  }
 ],
 "options": [
  {
   "title": "लिखित मांग पत्र भेजें",
   "why": "सबसे तेज़ और कम लागत वाला कदम, जिससे आप अपना दावा औपचारिक रूप से दर्ज कर सकते हैं।",
   "steps": [
    "एक पत्र/ई‑मेल में बकाया राशि, महीनों की सूची और दो कार्यदिवसों के भीतर भुगतान की अंतिम तिथि लिखें।",
    "सभी प्रमाण (ऑफ़र लेटर, पेस्लिप, बैंक स्टेटमेंट, ई‑मेल) संलग्न करें।",
    "एक प्रति अपने पास रखें और ई‑मेल के रीड रसीद को सुरक्षित रखें।"
   ],
   "kb_ids": [
    "PROC-DEMAND-LETTER"
   ]
  },
  {
   "title": "लेबर अथॉरिटी में वेतन दावा दायर करें",
   "why": "यदि मांग पत्र के बाद भी भुगतान नहीं होता, तो आधिकारिक निकाय से वसूली की प्रक्रिया शुरू की जा सकती है।",
   "steps": [
    "ऑफ़र लेटर, पेस्लिप, बैंक स्टेटमेंट, ई‑मेल आदि सभी दस्तावेज़ इकट्ठा करें।",
    "स्थानीय लेबर अथॉरिटी (गजेटेड अधिकारी स्तर) की वेबसाइट या कार्यालय से आवेदन फ़ॉर्म प्राप्त करें।",
    "आवेदन फ़ॉर्म भरें और सभी दस्तावेज़ संलग्न करके जमा करें (ऑनलाइन या व्यक्तिगत)।",
    "आवेदन की रसीद रखें; अथॉरिटी को तीन महीने के भीतर निर्णय देना होता है।"
   ],
   "kb_ids": [
    "COW2019-S45"
   ]
  },
  {
   "title": "मुफ़्त कानूनी सहायता प्राप्त करें",
   "why": "यदि आप आय सीमा या सामाजिक वर्ग मानदंडों के तहत आते हैं, तो आप बिना खर्च के वकील की मदद ले सकते हैं।",
   "steps": [
    "नालसा हेल्पलाइन 15100 पर कॉल करें या नालसा की वेबसाइट पर जाएँ।",
    "आवश्यक पहचान प्रमाण और यदि हो तो वर्ग प्रमाणपत्र तैयार रखें।",
    "नजदीकी तालुका/जिला/राज्य कानूनी सेवा प्राधिकरण में लिखित या मौखिक आवेदन दें।",
    "सहायता मिलने पर वकील के साथ आगे की प्रक्रिया (जैसे दावा दायर करना) आगे बढ़ाएँ।"
   ],
   "kb_ids": [
    "LSA1987-S12",
    "PROC-NALSA"
   ]
  }
 ],
 "uncertainties": [
  "बकाया वेतन पर कौन सा विशेष कानून (पुराना या नया कोड) लागू होगा, यह स्पष्ट नहीं है; राज्य‑विशिष्ट नियम भी अलग हो सकते हैं।",
  "दावे की सटीक समय सीमा (कब से गिनना शुरू करना है) का निर्धारण इस सहायक द्वारा नहीं किया गया है।"
 ],
 "suggest_lawyer": true,
 "lawyer_reason": "क्योंकि आपका वेतन बकाया नई कोड के लागू होने से पहले शुरू हुआ है, इसलिए लागू कानून की पहचान और संभावित राज्य‑विशिष्ट प्रक्रियाओं के लिए वकील की सलाह आवश्यक है।"
}
```