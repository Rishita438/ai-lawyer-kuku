# C06_consumer_hindi
**Category:** language-hindi  
**Description:** Story in Devanagari Hindi. Questions and answer should be in Hindi.  
**Pack:** consumer  
**Run at:** 2026-11-20T13:56:20  
**Models that answered:** gemini-3.5-flash-lite (17 calls)  
**Time:** 62.5 s

> Unedited output of scripts/run_tests.py. Nothing below was changed by hand.

## Automatic checks
| Check | Result | Detail |
|---|---|---|
| escalation | PASS | expected none, got none |
| language | PASS | expected hi, got hi |
| document grievance_letter | PASS | expected unlocked, got unlocked |

## Conversation
**Bot:** Tell me what happened, in your own words - English, Hindi or Hinglish is fine. For example: what you bought, from whom, and what went wrong.

**User:** मैंने 10 अक्टूबर 2026 को मीशो से 2500 रुपये की साड़ी मंगवाई थी, लेकिन फटी हुई आई। रिफंड नहीं मिल रहा।

**Bot:** मीशो से मंगाई गई साड़ी फटी हुई आने और रिफंड न मिलने की बात मैंने नोट कर ली है। समस्या किस तारीख को हुई, या रिफंड कब मिलना था?

**User:** 10 अक्टूबर 2026

**Bot:** ठीक है, मैंने यह जानकारी नोट कर ली है। क्या आपने यह अपने निजी इस्तेमाल के लिए लिया था, या व्यापार / आगे बेचने के लिए?

**User:** अपने इस्तेमाल के लिए

**Bot:** मैं समझ गया कि आपने यह अपने इस्तेमाल के लिए लिया था। क्या आपने विक्रेता या प्लेटफ़ॉर्म से पहले शिकायत की है? अगर हाँ, तो कैसे और कब, और उन्होंने क्या कहा?

**User:** ऐप पर शिकायत की, जवाब नहीं आया

**Bot:** आपने ऐप पर शिकायत की और कोई जवाब नहीं मिला। आपके पास क्या सबूत है? (बिल/इनवॉइस, ऑर्डर आईडी, पेमेंट स्क्रीनशॉट, ईमेल, चैट, फ़ोटो, वारंटी कार्ड)

**User:** ऑर्डर आईडी और फ़ोटो

**Bot:** नमस्ते, आपने आर्डर आईडी और फोटो की जानकारी दी है। आप क्या चाहते हैं - रिफंड, बदला हुआ सामान, मरम्मत, या मुआवज़ा? (आपने बताया: रिफंड - क्या यह सही है?)

**User:** रिफंड

**Bot:** रिफंड न मिलने की इस बात को मैंने नोट कर लिया है। आप किस शहर और राज्य में रहते हैं? (इससे तय होता है कि आप शिकायत कहाँ दर्ज कर सकते हैं।)

**User:** पटना, बिहार

**Bot:** पटना, बिहार से अपनी बात बताने के लिए धन्यवाद।

## Case file (final)
```json
{
 "pack": "consumer",
 "facts": {
  "product_or_service": "साड़ी",
  "seller_name": "मीशो",
  "bought_online": true,
  "amount_paid": 2500,
  "purchase_date": "2026-10-10",
  "what_went_wrong": "साड़ी फटी हुई आई और रिफंड नहीं मिल रहा है।",
  "problem_date": "2026-10-10",
  "for_business_use": false,
  "complaints_made": "ऐप पर शिकायत की, जवाब नहीं आया",
  "evidence": [
   "ऑर्डर आईडी",
   "फ़ोटो"
  ],
  "desired_outcome": "रिफंड",
  "user_city_state": "पटना, बिहार"
 },
 "language": "hi",
 "user_messages": [
  "मैंने 10 अक्टूबर 2026 को मीशो से 2500 रुपये की साड़ी मंगवाई थी, लेकिन फटी हुई आई। रिफंड नहीं मिल रहा।",
  "10 अक्टूबर 2026",
  "अपने इस्तेमाल के लिए",
  "ऐप पर शिकायत की, जवाब नहीं आया",
  "ऑर्डर आईडी और फ़ोटो",
  "रिफंड",
  "पटना, बिहार"
 ],
 "suggested": {
  "desired_outcome": "रिफंड"
 }
}
```

## Answer shown to the user

### Where you stand

आपकी स्थिति के अनुसार, आप एक उपभोक्ता हैं क्योंकि आपने अपने निजी इस्तेमाल के लिए साड़ी खरीदी है। चूंकि सामान फटी हुई आने पर भी आपको रिफंड नहीं मिल रहा है, इसलिए आप उपभोक्ता आयोग के माध्यम से अपना रिफंड और मुआवजा पाने के लिए कानूनी कदम उठा सकते हैं।

- आप एक उपभोक्ता के रूप में गिने जाते हैं क्योंकि आपने निजी इस्तेमाल के लिए पैसे देकर सामान खरीदा है।<br><small>📘 **Consumer Protection Act, 2019, s. 2(7)**: Who is a "consumer" — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)</small>

- सामान में खराबी होना (जैसे फटी हुई साड़ी) एक 'दोष' माना जाता है।<br><small>📘 **Consumer Protection Act, 2019, s. 2(10)**: What is a "defect" (goods) — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)</small>

- अगर ऑनलाइन प्लेटफॉर्म या विक्रेता रिफंड देने से मना करता है या वापस लेने से इनकार करता है, तो इसे अनुचित व्यापार प्रथा माना जा सकता है।<br><small>📘 **Consumer Protection Act, 2019, s. 2(47)**: What is an "unfair trade practice" — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)</small>

- ऑनलाइन माध्यम से की गई खरीद के मामले में, ई-कॉमर्स कंपनियों को शिकायत मिलने पर तय समय के भीतर उसका समाधान करना होता है।<br><small>📘 **Consumer Protection (E-Commerce) Rules, 2020, Rule 4(4)-(5)**: E-commerce grievance officer — [source](https://egazette.gov.in/WriteReadData/2020/220661.pdf) (✅ verified 2026-11-19)</small>

- आप निर्धारित समय सीमा के भीतर जिला उपभोक्ता आयोग में अपनी शिकायत दर्ज करा सकते हैं।<br><small>📘 **Consumer Protection Act, 2019, s. 34**: District Commission - which one you can file in — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)<br>📘 **Consumer Protection Act, 2019, s. 69**: Time limit for filing a complaint — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)<br>📘 **Consumer Protection (Jurisdiction of the District Commission, the State Commission and the National Commission) Rules, 2021, Rules 3-5**: Money limits - which Commission — [source](https://www.pib.gov.in/PressReleasePage.aspx?PRID=1786342) (✅ verified 2026-11-19)</small>

#### Key facts (calculated by the app, not the AI)

⏳ **Time limit:** ✅ within the limit. Normally file by **2028-10-10** (2 years from 2026-10-10; dates are approximate).

🏛️ **Which Commission:** District Consumer Commission, for Rs 2,500 paid (you can file where you live or work: पटना, बिहार).

💰 **Filing fee:** nil (no fee).

<small>Based on: 📘 **Consumer Protection Act, 2019, s. 34**: District Commission - which one you can file in — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19); 📘 **Consumer Protection Act, 2019, s. 69**: Time limit for filing a complaint — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19); 📘 **Consumer Protection (Consumer Disputes Redressal Commissions) Rules, 2020, Rule 7 (fee table)**: Fee for filing a consumer complaint — [source](https://egazette.gov.in/WriteReadData/2023/248158.pdf) (✅ verified 2026-11-19); 📘 **Consumer Protection (Jurisdiction of the District Commission, the State Commission and the National Commission) Rules, 2021, Rules 3-5**: Money limits - which Commission — [source](https://www.pib.gov.in/PressReleasePage.aspx?PRID=1786342) (✅ verified 2026-11-19)</small>

### Your options

**1. राष्ट्रीय उपभोक्ता हेल्पलाइन (NCH) से संपर्क करें** — यह आयोग जाने से पहले की एक शुरुआती और आसान प्रक्रिया है, जहाँ आपकी शिकायत को आगे बढ़ाया जाता है।
   - 1915 या 1800 11 4000 पर कॉल करें।
   - मोबाइल ऐप, पोर्टल या एसएमएस के जरिए अपनी शिकायत दर्ज कराएं।

   <small>📘 **National Consumer Helpline (consumerhelpline.gov.in), Contact page and FAQ**: National Consumer Helpline (pre-litigation step) — [source](https://consumerhelpline.gov.in/) (✅ verified 2026-11-19)</small>

**2. ऑनलाइन पोर्टल पर औपचारिक शिकायत दर्ज करें** — आप आधिकारिक ऑनलाइन उपभोक्ता पोर्टल के माध्यम से अपनी शिकायत दर्ज कर सकते हैं।
   - ई-जागृति पोर्टल पर जाएं।
   - अपनी ऑर्डर आईडी और फोटो सबूत के साथ शिकायत दर्ज करें।
   - इस मामले में 2,500 रुपये की राशि पर कोई शुल्क (फीस) नहीं है।

   <small>📘 **Consumer Protection Act, 2019, s. 35**: How a complaint is filed — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)<br>📘 **Consumer Protection (Consumer Disputes Redressal Commissions) Rules, 2020, Rule 7 (fee table)**: Fee for filing a consumer complaint — [source](https://egazette.gov.in/WriteReadData/2023/248158.pdf) (✅ verified 2026-11-19)<br>📘 **e-Jagriti (Department of Consumer Affairs)**: File online on e-Jagriti — [source](https://e-jagriti.gov.in/) (✅ verified 2026-11-19)</small>

### What I'm not sure about
- यह स्पष्ट नहीं है कि क्या कंपनी के शिकायत अधिकारी ने समय सीमा के भीतर आपसे कोई संपर्क किया था या नहीं।
- परिणाम की कोई [removed: nobody can promise a legal outcome] नहीं दी जा सकती, यह पूरी तरह से आयोग के समक्ष प्रस्तुत किए गए सबूतों पर निर्भर करता है।

---
<small>Knowledge base last verified: 2026-11-19. Only verified sources are cited. The safety checker removed 1 unverified item(s) from the AI's draft. This is general information, not legal advice.</small>

## Safety checker log (items removed from the AI's draft)
```json
[
 {
  "type": "promised_outcome",
  "text": "गारंटी"
 }
]
```

## Raw model JSON for the answer (before the safety checker)
```json
{
 "summary": "आपकी स्थिति के अनुसार, आप एक उपभोक्ता हैं क्योंकि आपने अपने निजी इस्तेमाल के लिए साड़ी खरीदी है। चूंकि सामान फटी हुई आने पर भी आपको रिफंड नहीं मिल रहा है, इसलिए आप उपभोक्ता आयोग के माध्यम से अपना रिफंड और मुआवजा पाने के लिए कानूनी कदम उठा सकते हैं।",
 "points": [
  {
   "text": "आप एक उपभोक्ता के रूप में गिने जाते हैं क्योंकि आपने निजी इस्तेमाल के लिए पैसे देकर सामान खरीदा है।",
   "kb_ids": [
    "CPA2019-S2-7"
   ]
  },
  {
   "text": "सामान में खराबी होना (जैसे फटी हुई साड़ी) एक 'दोष' माना जाता है।",
   "kb_ids": [
    "CPA2019-S2-10"
   ]
  },
  {
   "text": "अगर ऑनलाइन प्लेटफॉर्म या विक्रेता रिफंड देने से मना करता है या वापस लेने से इनकार करता है, तो इसे अनुचित व्यापार प्रथा माना जा सकता है।",
   "kb_ids": [
    "CPA2019-S2-47"
   ]
  },
  {
   "text": "ऑनलाइन माध्यम से की गई खरीद के मामले में, ई-कॉमर्स कंपनियों को शिकायत मिलने पर तय समय के भीतर उसका समाधान करना होता है।",
   "kb_ids": [
    "ECOM2020-R4-5"
   ]
  },
  {
   "text": "आप निर्धारित समय सीमा के भीतर जिला उपभोक्ता आयोग में अपनी शिकायत दर्ज करा सकते हैं।",
   "kb_ids": [
    "CPA2019-S34",
    "CPA2019-S69",
    "CPR2021-PECUNIARY"
   ]
  }
 ],
 "options": [
  {
   "title": "राष्ट्रीय उपभोक्ता हेल्पलाइन (NCH) से संपर्क करें",
   "why": "यह आयोग जाने से पहले की एक शुरुआती और आसान प्रक्रिया है, जहाँ आपकी शिकायत को आगे बढ़ाया जाता है।",
   "steps": [
    "1915 या 1800 11 4000 पर कॉल करें।",
    "मोबाइल ऐप, पोर्टल या एसएमएस के जरिए अपनी शिकायत दर्ज कराएं।"
   ],
   "kb_ids": [
    "PROC-NCH"
   ]
  },
  {
   "title": "ऑनलाइन पोर्टल पर औपचारिक शिकायत दर्ज करें",
   "why": "आप आधिकारिक ऑनलाइन उपभोक्ता पोर्टल के माध्यम से अपनी शिकायत दर्ज कर सकते हैं।",
   "steps": [
    "ई-जागृति पोर्टल पर जाएं।",
    "अपनी ऑर्डर आईडी और फोटो सबूत के साथ शिकायत दर्ज करें।",
    "इस मामले में 2,500 रुपये की राशि पर कोई शुल्क (फीस) नहीं है।"
   ],
   "kb_ids": [
    "CPA2019-S35",
    "CPR2020-FEES",
    "PROC-EJAGRITI"
   ]
  }
 ],
 "uncertainties": [
  "यह स्पष्ट नहीं है कि क्या कंपनी के शिकायत अधिकारी ने समय सीमा के भीतर आपसे कोई संपर्क किया था या नहीं।",
  "परिणाम की कोई गारंटी नहीं दी जा सकती, यह पूरी तरह से आयोग के समक्ष प्रस्तुत किए गए सबूतों पर निर्भर करता है।"
 ],
 "suggest_lawyer": false,
 "lawyer_reason": ""
}
```

## Document: grievance_letter
Offered: yes
Drafting log: ['model paragraph rejected -> plain version used: seller_name missing']

```text
To,
The Grievance Officer,
मीशो

**Subject: Complaint regarding साड़ी – Order ID [ORDER ID]**

Dear Sir/Madam,

I am writing to register a formal complaint about my purchase from मीशो.

1. On 10 October 2026, I purchased साड़ी from मीशो for Rs 2,500.

2. On 10 October 2026, the following problem arose: (in my own words) "साड़ी फटी हुई आई और रिफंड नहीं मिल रहा है।".

3. I purchased it for my personal use.

4. Steps I have already taken: (in my own words) "ऐप पर शिकायत की, जवाब नहीं आया".

**My request:** रिफंड.

Under Rule 4(4)-(5) of the Consumer Protection (E-Commerce) Rules, 2020, the grievance officer is required to acknowledge a consumer complaint within 48 hours and redress it within one month of receiving it. I request you to do so.

I have the following documents and will share them on request: ऑर्डर आईडी, फ़ोटो.

Please treat this letter as a formal complaint and keep a record of it.

Yours faithfully,
[YOUR FULL NAME]
[YOUR EMAIL / PHONE NUMBER]
Date: [DATE OF SENDING]

```

## Document: commission_complaint
Offered: yes
Drafting log: ['model paragraph rejected -> plain version used: seller_name missing']

```text
**BEFORE THE DISTRICT CONSUMER DISPUTES REDRESSAL COMMISSION, [DISTRICT NAME], बिहार**

Consumer Complaint No. ______ of ______ (to be filled by the Commission)

**Complainant:**
[YOUR FULL NAME], [YOUR FULL ADDRESS], पटना, बिहार

**Versus**

**Opposite Party:**
मीशो, [OPPOSITE PARTY'S REGISTERED ADDRESS – see your invoice or the website's legal/contact page]

---

**COMPLAINT**

**1. Facts of the case**

1. On 10 October 2026, I purchased साड़ी from मीशो for Rs 2,500.

2. On 10 October 2026, the following problem arose: (in my own words) "साड़ी फटी हुई आई और रिफंड नहीं मिल रहा है।".

3. I purchased it for my personal use.

4. Steps I have already taken: (in my own words) "ऐप पर शिकायत की, जवाब नहीं आया".

**2. Jurisdiction**

(a) The value of the goods/services paid as consideration is Rs 2,500, which is within the limit of this Commission (Rules 3-5 of the Consumer Protection (Jurisdiction of the District Commission, the State Commission and the National Commission) Rules, 2021).

(b) The Complainant resides/personally works for gain at पटना, बिहार, within the area of this Commission (Section 34 of the Consumer Protection Act, 2019).

**3. Limitation**

The cause of action arose on or about 10 October 2026. This complaint is filed within the period allowed (Section 69 of the Consumer Protection Act, 2019).

**4. Relief sought**

The Complainant respectfully requests this Commission to direct the Opposite Party to:
(a) grant the following relief: रिफंड;
(b) pay such compensation and costs as this Commission considers just (Section 39 of the Consumer Protection Act, 2019).

**5. List of documents**

1. ऑर्डर आईडी
2. फ़ोटो

**Verification**

I, [YOUR FULL NAME], the Complainant, state that the contents of this complaint are true and correct to the best of my knowledge and belief, and nothing material has been concealed.

Place: [PLACE]
Date: [DATE]

[SIGNATURE OF COMPLAINANT]

```