# N01_notice_private_loan
**Category:** normal  
**Description:** Lawyer's notice from a lending app demanding repayment within 15 days. Explain, don't stop.  
**Pack:** notice  
**Run at:** 2026-11-20T15:16:00  
**Models that answered:** openai/gpt-oss-120b (9 calls)  
**Time:** 73.4 s

> Unedited output of scripts/run_tests.py. Nothing below was changed by hand.

## Automatic checks
| Check | Result | Detail |
|---|---|---|
| escalation | PASS | expected none, got none |
| cites expected KB entry | PASS | found ['PROC-NOTICE-PRIVATE'] of ['PROC-NOTICE-PRIVATE'] |

## Conversation
**Bot:** Tell me about the notice you received, in your own words - English, Hindi or Hinglish is fine. For example: who sent it, what it asks you to do, and whether it gives a date. (Please don't paste personal details like your address or account numbers.)

**User:** mujhe ek loan app ke vakil ka legal notice aaya hai, 18000 rupaye 15 din mein bharne ko bol rahe hain, nahi to case karenge

**Bot:** मैं समझता हूँ कि आपको एक कानूनी नोटिस मिला है। क्या यह नोटिस अदालत, पुलिस, किसी ट्रिब्यूनल/आयोग, या सरकारी या टैक्स ऑफ़िस से आया है?

**User:** nahi, police se nahi, vakil ka notice hai

**Bot:** समझ गया, यह वकील का नोटिस है। आपको नोटिस किस तारीख को मिला?

**User:** 18 november 2026

**Bot:** मैं समझ गया हूँ कि आपने यह जानकारी दी है। क्या नोटिस में कोई समय-सीमा दी गई है? अगर हाँ, तो किस तारीख तक (या कितने दिन में)? (आपने बताया: 2026-12-03 - क्या यह सही है?)

**User:** 15 din mein, yaani 3 december 2026

**Bot:** धन्यवाद, अब हमारे पास आपके मामले की मुख्य जानकारी है।

## Case file (final)
```json
{
 "pack": "notice",
 "facts": {
  "official_sender": false,
  "sender": "lawyer of loan app",
  "about": "loan repayment",
  "what_it_demands": "pay Rs 18000",
  "received_date": "2026-11-18",
  "deadline_in_notice": "2026-12-03"
 },
 "language": "hi",
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

आपको एक निजी वकील का नोटिस मिला है, जिसमें 18,000 रुपये 3 दिसंबर 2026 तक चुकाने को कहा गया है। यह नोटिस अदालत का आदेश नहीं है, पर इसे अनदेखा नहीं करना चाहिए; इसे सुरक्षित रखें और जवाब देने से पहले सलाह लें।

- यह नोटिस एक निजी वकील द्वारा भेजा गया है, इसलिए यह अदालत का आदेश नहीं है, बल्कि एक औपचारिक मांग है।<br><small>📝 *A legal notice from a person or company is not a court order (general practice)* — general practice, not a legal rule (reviewed 2026-11-19)</small>

- नोटिस में 18,000 रुपये की राशि 3 दिसंबर 2026 तक देने को कहा गया है, जो आज से 13 दिन बाद है।<br><small>📝 *A legal notice from a person or company is not a court order (general practice)* — general practice, not a legal rule (reviewed 2026-11-19)</small>

- नोटिस को अनदेखा न करें; इसे सुरक्षित रखें, लिफाफ़ और प्राप्ति की तारीख का प्रमाण रखें, और जवाब देने से पहले सलाह लें।<br><small>📝 *A legal notice from a person or company is not a court order (general practice)* — general practice, not a legal rule (reviewed 2026-11-19)</small>

- यदि आप आर्थिक रूप से सक्षम हैं, तो आप वकील से परामर्श कर सकते हैं; यदि आप पात्र हैं तो मुफ्त कानूनी सहायता भी मिल सकती है।<br><small>📘 **Legal Services Authorities Act, 1987, s. 12**: Who can get free legal aid — [source](https://indiacode.gov.in/act/a742f03e-3129-4b8d-8dda-af2a36190b18/sections?spc.sf=dc.date.issued&spc.sd=DESC&spc.page=2&spc.rpp=10) (✅ verified 2026-11-19)<br>📘 **National Legal Services Authority**: How to reach free legal aid — [source](https://nalsa.gov.in/legal-aid/#Free-Legal-Aid) (✅ verified 2026-11-19)</small>

- नोटिस की शर्तों को समझने और संभावित बचाव या पुनर्भुगतान योजना तैयार करने के लिए पेशेवर सलाह लेना उपयोगी रहेगा।<br><small>📝 *A legal notice from a person or company is not a court order (general practice)* — general practice, not a legal rule (reviewed 2026-11-19)</small>

#### Key facts (calculated by the app, not the AI)

📨 **Who sent it:** a private party (not a court or government). A legal notice like this is a formal demand, not a court order.

📅 **Deadline:** 2026-12-03 - 13 day(s) from today.

<small>Based on: 📝 *A legal notice from a person or company is not a court order (general practice)* — general practice, not a legal rule (reviewed 2026-11-19)</small>

### Your options

**1. नोटिस सुरक्षित रखें और स्पष्टता माँगें** — पहले ही कदम से आप समय सीमा को याद रख सकते हैं और संभावित गलतफहमी दूर कर सकते हैं।
   - नोटिस और लिफाफ़ को सुरक्षित जगह पर रखें।
   - नोटिस में दी गई समय सीमा (3 दिसंबर 2026) को कैलेंडर में लिखें।
   - वकील या लेंडर से संपर्क करके राशि, ब्याज, या अन्य शर्तों की स्पष्टता माँगें।

   <small>📝 *A legal notice from a person or company is not a court order (general practice)* — general practice, not a legal rule (reviewed 2026-11-19)</small>

**2. किसी वकील से परामर्श लें (मुफ़्त सहायता सहित)** — आपके अधिकार और संभावित बचाव को समझने के लिए पेशेवर सलाह आवश्यक है।
   - क्या आप फ्री लीगल एड के मानदंडों (जैसे आय सीमा, सामाजिक वर्ग) में आते हैं, देखें।
   - नालसा हेल्पलाइन 15100 पर कॉल करें या नजदीकी जिला कानूनी सेवा प्राधिकरण में आवेदन करें।
   - एक वकील से मिलें और नोटिस की प्रतिलिपि साथ ले जाएँ।

   <small>📘 **Legal Services Authorities Act, 1987, s. 12**: Who can get free legal aid — [source](https://indiacode.gov.in/act/a742f03e-3129-4b8d-8dda-af2a36190b18/sections?spc.sf=dc.date.issued&spc.sd=DESC&spc.page=2&spc.rpp=10) (✅ verified 2026-11-19)<br>📘 **National Legal Services Authority**: How to reach free legal aid — [source](https://nalsa.gov.in/legal-aid/#Free-Legal-Aid) (✅ verified 2026-11-19)</small>

**3. भुगतान या पुनर्भुगतान योजना पर बातचीत करें** — यदि आप राशि चुकाने में सक्षम हैं, तो समझौता करके आगे की कानूनी कार्रवाई से बचा जा सकता है।
   - वकील के माध्यम से लेंडर को लिखित प्रस्ताव भेजें (जैसे किस्तों में भुगतान)।
   - प्रस्ताव में स्पष्ट तारीखें और राशि लिखें।
   - लेंडर की प्रतिक्रिया का रिकॉर्ड रखें।

   <small>📝 *A legal notice from a person or company is not a court order (general practice)* — general practice, not a legal rule (reviewed 2026-11-19)</small>

**4. यदि नोटिस को अनदेखा किया तो संभावित मुकदमा** — नोटिस अनदेखा करने पर लेंडर कोर्ट में केस दायर कर सकता है, जिससे आपको आगे की कानूनी प्रक्रिया का सामना करना पड़ेगा।
   - समय सीमा के बाद भी भुगतान न करने पर संभावित कानूनी परिणामों के लिए तैयार रहें।
   - वकील से संपर्क करके संभावित मुकदमे की तैयारी करें।

   <small>📝 *A legal notice from a person or company is not a court order (general practice)* — general practice, not a legal rule (reviewed 2026-11-19)</small>

### ⚖️ When to get a real lawyer
- एक वकील आपको नोटिस की वैधता, आपके ऋण के वास्तविक दायित्व, और संभावित बचाव या पुनर्भुगतान विकल्पों पर सटीक सलाह दे सकता है।
- Free legal help may be available: District Legal Services Authority / NALSA helpline **15100**.

### What I'm not sure about
- आपके मूल ऋण समझौते की शर्तें और क्या आप वास्तव में इस राशि के देनदार हैं, यह स्पष्ट नहीं है।
- नोटिस में ब्याज, दंड या अतिरिक्त शुल्क की जानकारी नहीं दी गई है; यह जानने के लिए मूल अनुबंध देखना पड़ेगा।
- यदि आप भुगतान नहीं कर पाते तो कौन‑सी कानूनी बचाव उपलब्ध हैं, यह आपके विशिष्ट परिस्थितियों पर निर्भर करेगा।

---
<small>Knowledge base last verified: 2026-11-19. Only verified sources are cited. This is general information, not legal advice.</small>

## Safety checker log (items removed from the AI's draft)
```json
[]
```

## Raw model JSON for the answer (before the safety checker)
```json
{
 "summary": "आपको एक निजी वकील का नोटिस मिला है, जिसमें 18,000 रुपये 3 दिसंबर 2026 तक चुकाने को कहा गया है। यह नोटिस अदालत का आदेश नहीं है, पर इसे अनदेखा नहीं करना चाहिए; इसे सुरक्षित रखें और जवाब देने से पहले सलाह लें।",
 "points": [
  {
   "text": "यह नोटिस एक निजी वकील द्वारा भेजा गया है, इसलिए यह अदालत का आदेश नहीं है, बल्कि एक औपचारिक मांग है।",
   "kb_ids": [
    "PROC-NOTICE-PRIVATE"
   ]
  },
  {
   "text": "नोटिस में 18,000 रुपये की राशि 3 दिसंबर 2026 तक देने को कहा गया है, जो आज से 13 दिन बाद है।",
   "kb_ids": [
    "PROC-NOTICE-PRIVATE"
   ]
  },
  {
   "text": "नोटिस को अनदेखा न करें; इसे सुरक्षित रखें, लिफाफ़ और प्राप्ति की तारीख का प्रमाण रखें, और जवाब देने से पहले सलाह लें।",
   "kb_ids": [
    "PROC-NOTICE-PRIVATE"
   ]
  },
  {
   "text": "यदि आप आर्थिक रूप से सक्षम हैं, तो आप वकील से परामर्श कर सकते हैं; यदि आप पात्र हैं तो मुफ्त कानूनी सहायता भी मिल सकती है।",
   "kb_ids": [
    "LSA1987-S12",
    "PROC-NALSA"
   ]
  },
  {
   "text": "नोटिस की शर्तों को समझने और संभावित बचाव या पुनर्भुगतान योजना तैयार करने के लिए पेशेवर सलाह लेना उपयोगी रहेगा।",
   "kb_ids": [
    "PROC-NOTICE-PRIVATE"
   ]
  }
 ],
 "options": [
  {
   "title": "नोटिस सुरक्षित रखें और स्पष्टता माँगें",
   "why": "पहले ही कदम से आप समय सीमा को याद रख सकते हैं और संभावित गलतफहमी दूर कर सकते हैं।",
   "steps": [
    "नोटिस और लिफाफ़ को सुरक्षित जगह पर रखें।",
    "नोटिस में दी गई समय सीमा (3 दिसंबर 2026) को कैलेंडर में लिखें।",
    "वकील या लेंडर से संपर्क करके राशि, ब्याज, या अन्य शर्तों की स्पष्टता माँगें।"
   ],
   "kb_ids": [
    "PROC-NOTICE-PRIVATE"
   ]
  },
  {
   "title": "किसी वकील से परामर्श लें (मुफ़्त सहायता सहित)",
   "why": "आपके अधिकार और संभावित बचाव को समझने के लिए पेशेवर सलाह आवश्यक है।",
   "steps": [
    "क्या आप फ्री लीगल एड के मानदंडों (जैसे आय सीमा, सामाजिक वर्ग) में आते हैं, देखें।",
    "नालसा हेल्पलाइन 15100 पर कॉल करें या नजदीकी जिला कानूनी सेवा प्राधिकरण में आवेदन करें।",
    "एक वकील से मिलें और नोटिस की प्रतिलिपि साथ ले जाएँ।"
   ],
   "kb_ids": [
    "LSA1987-S12",
    "PROC-NALSA"
   ]
  },
  {
   "title": "भुगतान या पुनर्भुगतान योजना पर बातचीत करें",
   "why": "यदि आप राशि चुकाने में सक्षम हैं, तो समझौता करके आगे की कानूनी कार्रवाई से बचा जा सकता है।",
   "steps": [
    "वकील के माध्यम से लेंडर को लिखित प्रस्ताव भेजें (जैसे किस्तों में भुगतान)।",
    "प्रस्ताव में स्पष्ट तारीखें और राशि लिखें।",
    "लेंडर की प्रतिक्रिया का रिकॉर्ड रखें।"
   ],
   "kb_ids": [
    "PROC-NOTICE-PRIVATE"
   ]
  },
  {
   "title": "यदि नोटिस को अनदेखा किया तो संभावित मुकदमा",
   "why": "नोटिस अनदेखा करने पर लेंडर कोर्ट में केस दायर कर सकता है, जिससे आपको आगे की कानूनी प्रक्रिया का सामना करना पड़ेगा।",
   "steps": [
    "समय सीमा के बाद भी भुगतान न करने पर संभावित कानूनी परिणामों के लिए तैयार रहें।",
    "वकील से संपर्क करके संभावित मुकदमे की तैयारी करें।"
   ],
   "kb_ids": [
    "PROC-NOTICE-PRIVATE"
   ]
  }
 ],
 "uncertainties": [
  "आपके मूल ऋण समझौते की शर्तें और क्या आप वास्तव में इस राशि के देनदार हैं, यह स्पष्ट नहीं है।",
  "नोटिस में ब्याज, दंड या अतिरिक्त शुल्क की जानकारी नहीं दी गई है; यह जानने के लिए मूल अनुबंध देखना पड़ेगा।",
  "यदि आप भुगतान नहीं कर पाते तो कौन‑सी कानूनी बचाव उपलब्ध हैं, यह आपके विशिष्ट परिस्थितियों पर निर्भर करेगा।"
 ],
 "suggest_lawyer": true,
 "lawyer_reason": "एक वकील आपको नोटिस की वैधता, आपके ऋण के वास्तविक दायित्व, और संभावित बचाव या पुनर्भुगतान विकल्पों पर सटीक सलाह दे सकता है।"
}
```