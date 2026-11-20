# C06_consumer_hindi
**Category:** language-hindi  
**Description:** Story in Devanagari Hindi. Questions and answer should be in Hindi.  
**Pack:** consumer  
**Run at:** 2026-11-20T15:22:36  
**Models that answered:** openai/gpt-oss-120b (19 calls)  
**Time:** 181.3 s

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

**Bot:** मैं समझता हूँ कि आपको साड़ी में समस्या हुई है। क्या आपने यह अपने निजी इस्तेमाल के लिए लिया था, या व्यापार / आगे बेचने के लिए?

**User:** अपने इस्तेमाल के लिए

**Bot:** समझ गया। क्या आपने यह ऑनलाइन (वेबसाइट/ऐप) खरीदा था या किसी दुकान से?

**User:** ऑनलाइन, मीशो ऐप से

**Bot:** मैं समझ गया कि आप मीशो ऐप के माध्यम से ऑनलाइन समस्या का सामना कर रहे हैं। समस्या किस तारीख को हुई, या रिफंड कब मिलना था? (आपने बताया: 2026-10-10 - क्या यह सही है?)

**User:** 10 अक्टूबर 2026

**Bot:** मैं समझ गया। क्या आपने विक्रेता या प्लेटफ़ॉर्म से पहले शिकायत की है? अगर हाँ, तो कैसे और कब, और उन्होंने क्या कहा?

**User:** ऐप पर शिकायत की, जवाब नहीं आया

**Bot:** मैं समझता हूँ कि आपने ऐप पर शिकायत की और अभी तक जवाब नहीं मिला है। आपके पास क्या सबूत है? (बिल/इनवॉइस, ऑर्डर आईडी, पेमेंट स्क्रीनशॉट, ईमेल, चैट, फ़ोटो, वारंटी कार्ड)

**User:** ऑर्डर आईडी और फ़ोटो

**Bot:** मैंने आपका ऑर्डर आईडी और फ़ोटो प्राप्त कर लिया है। आप क्या चाहते हैं - रिफंड, बदला हुआ सामान, मरम्मत, या मुआवज़ा? (आपने बताया: रिफंड - क्या यह सही है?)

**User:** रिफंड

**Bot:** मैं समझ गया कि आप रिफंड के बारे में जानकारी चाहते हैं। आप किस शहर और राज्य में रहते हैं? (इससे तय होता है कि आप शिकायत कहाँ दर्ज कर सकते हैं।)

**User:** पटना, बिहार

**Bot:** धन्यवाद, अब हमारे पास आपके केस की मुख्य जानकारी है।

## Case file (final)
```json
{
 "pack": "consumer",
 "facts": {
  "product_or_service": "साड़ी",
  "seller_name": "मीशो",
  "for_business_use": false,
  "bought_online": true,
  "amount_paid": 2500,
  "purchase_date": "2026-10-10",
  "what_went_wrong": "साड़ी फटी हुई आई, रिफंड नहीं मिल रहा",
  "problem_date": "2026-10-10",
  "complaints_made": "ऐप पर शिकायत की, जवाब नहीं आया",
  "evidence": [
   "order ID",
   "photos"
  ],
  "desired_outcome": "refund",
  "user_city_state": "पटना, बिहार"
 },
 "language": "hi",
 "user_messages": [
  "मैंने 10 अक्टूबर 2026 को मीशो से 2500 रुपये की साड़ी मंगवाई थी, लेकिन फटी हुई आई। रिफंड नहीं मिल रहा।",
  "अपने इस्तेमाल के लिए",
  "ऑनलाइन, मीशो ऐप से",
  "10 अक्टूबर 2026",
  "ऐप पर शिकायत की, जवाब नहीं आया",
  "ऑर्डर आईडी और फ़ोटो",
  "रिफंड",
  "पटना, बिहार"
 ],
 "suggested": {
  "desired_outcome": "रिफंड",
  "problem_date": "2026-10-10"
 }
}
```

## Answer shown to the user

### Where you stand

आप एक उपभोक्ता हैं और खरीदी गई साड़ी में दोष है, इसलिए आप रिफंड या अन्य राहत के लिए उपभोक्ता आयोग में शिकायत दर्ज कर सकते हैं।

- आप ऑनलाइन खरीदी गई साड़ी के लिए उपभोक्ता माने जाते हैं।<br><small>📘 **Consumer Protection Act, 2019, s. 2(7)**: Who is a "consumer" — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)</small>

- साड़ी फटी हुई आई है, जो वस्तु के दोष (defect) के अंतर्गत आता है।<br><small>📘 **Consumer Protection Act, 2019, s. 2(10)**: What is a "defect" (goods) — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)</small>

- विक्रेता ने रिफंड नहीं दिया और ऐप पर आपकी शिकायत का कोई उत्तर नहीं दिया, जो अनुचित व्यापार प्रथा (unfair trade practice) हो सकती है।<br><small>📘 **Consumer Protection Act, 2019, s. 2(47)**: What is an "unfair trade practice" — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)</small>

- आपके पास शिकायत दर्ज करने के लिए दो साल का समय है, और अभी वह सीमा के भीतर है।<br><small>📘 **Consumer Protection Act, 2019, s. 69**: Time limit for filing a complaint — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)</small>

#### Key facts (calculated by the app, not the AI)

⏳ **Time limit:** ✅ within the limit. Normally file by **2028-10-10** (2 years from 2026-10-10; dates are approximate).

🏛️ **Which Commission:** District Consumer Commission, for Rs 2,500 paid (you can file where you live or work: पटना, बिहार).

💰 **Filing fee:** nil (no fee).

<small>Based on: 📘 **Consumer Protection Act, 2019, s. 34**: District Commission - which one you can file in — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19); 📘 **Consumer Protection Act, 2019, s. 69**: Time limit for filing a complaint — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19); 📘 **Consumer Protection (Consumer Disputes Redressal Commissions) Rules, 2020, Rule 7 (fee table)**: Fee for filing a consumer complaint — [source](https://egazette.gov.in/WriteReadData/2023/248158.pdf) (✅ verified 2026-11-19); 📘 **Consumer Protection (Jurisdiction of the District Commission, the State Commission and the National Commission) Rules, 2021, Rules 3-5**: Money limits - which Commission — [source](https://www.pib.gov.in/PressReleasePage.aspx?PRID=1786342) (✅ verified 2026-11-19)</small>

### Your options

**1. ई‑कॉमर्स ग्रिवेंस अधिकारी से संपर्क** — ऑनलाइन प्लेटफ़ॉर्म को 48 घंटे में जवाब देना और एक महीने में समाधान देना अनिवार्य है।
   - ऐप में ग्रिवेंस अधिकारी का नाम और संपर्क विवरण देखें।
   - उन्हें लिखित (या ऐप के माध्यम से) शिकायत भेजें, जिसमें ऑर्डर आईडी और फोटो संलग्न हों।
   - 48 घंटे के भीतर acknowledgment की पुष्टि करें और एक महीने में समाधान की अपेक्षा रखें।

   <small>📘 **Consumer Protection (E-Commerce) Rules, 2020, Rule 4(4)-(5)**: E-commerce grievance officer — [source](https://egazette.gov.in/WriteReadData/2020/220661.pdf) (✅ verified 2026-11-19)</small>

**2. राष्ट्रीय उपभोक्ता हेल्पलाइन (NCH) पर पंजीकरण** — आगे की कानूनी कार्रवाई से पहले निःशुल्क मध्यस्थता का अवसर मिलता है।
   - 1915 या 1800‑11‑4000 पर कॉल करें, या SMS/वेब पोर्टल के माध्यम से grievance दर्ज करें।
   - अपनी शिकायत, ऑर्डर विवरण और फोटो भेजें।
   - यदि समाधान नहीं मिलता, तो आगे की कार्रवाई के लिए आयोग में शिकायत दर्ज करें।

   <small>📘 **National Consumer Helpline (consumerhelpline.gov.in), Contact page and FAQ**: National Consumer Helpline (pre-litigation step) — [source](https://consumerhelpline.gov.in/) (✅ verified 2026-11-19)</small>

**3. जिला उपभोक्ता आयोग में शिकायत दाखिल करें** — दूरस्थ या ऑनलाइन शिकायतों के लिए यह सबसे सीधा कानूनी उपाय है।
   - सभी दस्तावेज़ तैयार करें: ऑर्डर आईडी, फोटो, भुगतान प्रमाण, ऐप पर की गई शिकायत की स्क्रीनशॉट।
   - e‑Jagriti पोर्टल (proc‑EJAGRITI) पर ऑनलाइन फॉर्म भरें और जमा करें।
   - फ़ॉर्म में पटना, बिहार को स्थान के रूप में चुनें; कोई शुल्क नहीं है।
   - आवश्यकतानुसार, आयोग की ओर से मिलने वाले नोटिस या आदेश का पालन करें।

   <small>📘 **Consumer Protection Act, 2019, s. 35**: How a complaint is filed — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)<br>📘 **Consumer Protection Act, 2019, s. 39**: What the Commission can order — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)<br>📘 **e-Jagriti (Department of Consumer Affairs)**: File online on e-Jagriti — [source](https://e-jagriti.gov.in/) (✅ verified 2026-11-19)<br>📘 **Consumer Protection (Jurisdiction of the District Commission, the State Commission and the National Commission) Rules, 2021, Rules 3-5**: Money limits - which Commission — [source](https://www.pib.gov.in/PressReleasePage.aspx?PRID=1786342) (✅ verified 2026-11-19)</small>

**4. नि:शुल्क कानूनी सहायता प्राप्त करें** — यदि आप वकील की मदद चाहते हैं तो यह विकल्प मददगार हो सकता है।
   - नजदीकी जिला कानूनी सेवा प्राधिकरण (DLDA) या NALSA के स्थानीय कार्यालय में जाएँ।
   - पहचान प्रमाण और आय प्रमाण (यदि लागू हो) साथ ले जाएँ।
   - आवेदन फॉर्म भरें और जमा करें; सहायता मिलने पर वकील से मिलें।

   <small>📘 **Legal Services Authorities Act, 1987, s. 12**: Who can get free legal aid — [source](https://indiacode.gov.in/act/a742f03e-3129-4b8d-8dda-af2a36190b18/sections?spc.sf=dc.date.issued&spc.sd=DESC&spc.page=2&spc.rpp=10) (✅ verified 2026-11-19)<br>📘 **National Legal Services Authority**: How to reach free legal aid — [source](https://nalsa.gov.in/legal-aid/#Free-Legal-Aid) (✅ verified 2026-11-19)</small>

### ⚖️ When to get a real lawyer
- कम्प्लेन तैयार करने, सबूत व्यवस्थित करने और आयोग में प्रक्रिया को सही ढंग से आगे बढ़ाने के लिए वकील की मदद से सफलता की संभावना बढ़ सकती है।
- Free legal help may be available: District Legal Services Authority / NALSA helpline **15100**.

### What I'm not sure about
- विक्रेता को ई‑कॉमर्स प्लेटफ़ॉर्म के रूप में मानना या केवल एक स्वतंत्र विक्रेता मानना, जिससे grievance officer की जिम्मेदारी पर असर पड़ सकता है।
- विक्रेता द्वारा अब तक की गई कोई लिखित प्रतिक्रिया या अतिरिक्त शर्तें, यदि हों, तो उनका प्रभाव।

---
<small>Knowledge base last verified: 2026-11-19. Only verified sources are cited. The safety checker removed 2 unverified item(s) from the AI's draft. This is general information, not legal advice.</small>

## Safety checker log (items removed from the AI's draft)
```json
[
 {
  "type": "restated_fee_or_limit",
  "text": "यह शिकायत 2 साल के भीतर, बिना किसी शुल्क के, पटना के जिला उपभोक्ता आयोग में की जा सकती है।"
 },
 {
  "type": "restated_fee_or_limit",
  "text": "राशि 2,500 रुपये होने के कारण आपका मामला जिला उपभोक्ता आयोग में सुना जाएगा और filing fee शून्य है।"
 }
]
```

## Raw model JSON for the answer (before the safety checker)
```json
{
 "summary": "आप एक उपभोक्ता हैं और खरीदी गई साड़ी में दोष है, इसलिए आप रिफंड या अन्य राहत के लिए उपभोक्ता आयोग में शिकायत दर्ज कर सकते हैं। यह शिकायत 2 साल के भीतर, बिना किसी शुल्क के, पटना के जिला उपभोक्ता आयोग में की जा सकती है।",
 "points": [
  {
   "text": "आप ऑनलाइन खरीदी गई साड़ी के लिए उपभोक्ता माने जाते हैं।",
   "kb_ids": [
    "CPA2019-S2-7"
   ]
  },
  {
   "text": "साड़ी फटी हुई आई है, जो वस्तु के दोष (defect) के अंतर्गत आता है।",
   "kb_ids": [
    "CPA2019-S2-10"
   ]
  },
  {
   "text": "विक्रेता ने रिफंड नहीं दिया और ऐप पर आपकी शिकायत का कोई उत्तर नहीं दिया, जो अनुचित व्यापार प्रथा (unfair trade practice) हो सकती है।",
   "kb_ids": [
    "CPA2019-S2-47"
   ]
  },
  {
   "text": "आपके पास शिकायत दर्ज करने के लिए दो साल का समय है, और अभी वह सीमा के भीतर है।",
   "kb_ids": [
    "CPA2019-S69"
   ]
  },
  {
   "text": "राशि 2,500 रुपये होने के कारण आपका मामला जिला उपभोक्ता आयोग में सुना जाएगा और filing fee शून्य है।",
   "kb_ids": [
    "CPR2021-PECUNIARY",
    "CPA2019-S34",
    "CPR2020-FEES"
   ]
  }
 ],
 "options": [
  {
   "title": "ई‑कॉमर्स ग्रिवेंस अधिकारी से संपर्क",
   "why": "ऑनलाइन प्लेटफ़ॉर्म को 48 घंटे में जवाब देना और एक महीने में समाधान देना अनिवार्य है।",
   "steps": [
    "ऐप में ग्रिवेंस अधिकारी का नाम और संपर्क विवरण देखें।",
    "उन्हें लिखित (या ऐप के माध्यम से) शिकायत भेजें, जिसमें ऑर्डर आईडी और फोटो संलग्न हों।",
    "48 घंटे के भीतर acknowledgment की पुष्टि करें और एक महीने में समाधान की अपेक्षा रखें।"
   ],
   "kb_ids": [
    "ECOM2020-R4-5"
   ]
  },
  {
   "title": "राष्ट्रीय उपभोक्ता हेल्पलाइन (NCH) पर पंजीकरण",
   "why": "आगे की कानूनी कार्रवाई से पहले निःशुल्क मध्यस्थता का अवसर मिलता है।",
   "steps": [
    "1915 या 1800‑11‑4000 पर कॉल करें, या SMS/वेब पोर्टल के माध्यम से grievance दर्ज करें।",
    "अपनी शिकायत, ऑर्डर विवरण और फोटो भेजें।",
    "यदि समाधान नहीं मिलता, तो आगे की कार्रवाई के लिए आयोग में शिकायत दर्ज करें।"
   ],
   "kb_ids": [
    "PROC-NCH"
   ]
  },
  {
   "title": "जिला उपभोक्ता आयोग में शिकायत दाखिल करें",
   "why": "दूरस्थ या ऑनलाइन शिकायतों के लिए यह सबसे सीधा कानूनी उपाय है।",
   "steps": [
    "सभी दस्तावेज़ तैयार करें: ऑर्डर आईडी, फोटो, भुगतान प्रमाण, ऐप पर की गई शिकायत की स्क्रीनशॉट।",
    "e‑Jagriti पोर्टल (proc‑EJAGRITI) पर ऑनलाइन फॉर्म भरें और जमा करें।",
    "फ़ॉर्म में पटना, बिहार को स्थान के रूप में चुनें; कोई शुल्क नहीं है।",
    "आवश्यकतानुसार, आयोग की ओर से मिलने वाले नोटिस या आदेश का पालन करें।"
   ],
   "kb_ids": [
    "CPA2019-S35",
    "CPA2019-S39",
    "PROC-EJAGRITI",
    "CPR2021-PECUNIARY"
   ]
  },
  {
   "title": "नि:शुल्क कानूनी सहायता प्राप्त करें",
   "why": "यदि आप वकील की मदद चाहते हैं तो यह विकल्प मददगार हो सकता है।",
   "steps": [
    "नजदीकी जिला कानूनी सेवा प्राधिकरण (DLDA) या NALSA के स्थानीय कार्यालय में जाएँ।",
    "पहचान प्रमाण और आय प्रमाण (यदि लागू हो) साथ ले जाएँ।",
    "आवेदन फॉर्म भरें और जमा करें; सहायता मिलने पर वकील से मिलें।"
   ],
   "kb_ids": [
    "LSA1987-S12",
    "PROC-NALSA"
   ]
  }
 ],
 "uncertainties": [
  "विक्रेता को ई‑कॉमर्स प्लेटफ़ॉर्म के रूप में मानना या केवल एक स्वतंत्र विक्रेता मानना, जिससे grievance officer की जिम्मेदारी पर असर पड़ सकता है।",
  "विक्रेता द्वारा अब तक की गई कोई लिखित प्रतिक्रिया या अतिरिक्त शर्तें, यदि हों, तो उनका प्रभाव।"
 ],
 "suggest_lawyer": true,
 "lawyer_reason": "कम्प्लेन तैयार करने, सबूत व्यवस्थित करने और आयोग में प्रक्रिया को सही ढंग से आगे बढ़ाने के लिए वकील की मदद से सफलता की संभावना बढ़ सकती है।"
}
```

## Document: grievance_letter
Offered: yes
Drafting log: AI paragraph accepted

```text
To,
The Grievance Officer,
Meisho

**Subject: Complaint regarding sari – Order ID [ORDER ID]**

Dear Sir/Madam,

I am writing to register a formal complaint about my purchase from Meisho.

1. I purchased a sari online from Meisho on 10 October 2026, paying Rs 2,500.

2. The sari arrived torn, and I have not received a refund.

3. I lodged a complaint on the app on 10 October 2026, but no response was received.

**My request:** refund.

Under Rule 4(4)-(5) of the Consumer Protection (E-Commerce) Rules, 2020, the grievance officer is required to acknowledge a consumer complaint within 48 hours and redress it within one month of receiving it. I request you to do so.

I have the following documents and will share them on request: order ID, photos.

Please treat this letter as a formal complaint and keep a record of it.

Yours faithfully,
[YOUR FULL NAME]
[YOUR EMAIL / PHONE NUMBER]
Date: [DATE OF SENDING]

```

## Document: commission_complaint
Offered: yes
Drafting log: AI paragraph accepted

```text
**BEFORE THE DISTRICT CONSUMER DISPUTES REDRESSAL COMMISSION, [DISTRICT NAME], बिहार**

Consumer Complaint No. ______ of ______ (to be filled by the Commission)

**Complainant:**
[YOUR FULL NAME], [YOUR FULL ADDRESS], पटना, बिहार

**Versus**

**Opposite Party:**
Meisho, [OPPOSITE PARTY'S REGISTERED ADDRESS – see your invoice or the website's legal/contact page]

---

**COMPLAINT**

**1. Facts of the case**

1. I purchased a sari from Meisho online on 10 October 2026, paying Rs 2,500.

2. The sari arrived torn, and I am not receiving a refund.

3. I lodged a complaint on the app on 10 October 2026, but no response was received.

4. The purchase was for personal use, not for business.

**2. Jurisdiction**

(a) The value of the goods/services paid as consideration is Rs 2,500, which is within the limit of this Commission (Rules 3-5 of the Consumer Protection (Jurisdiction of the District Commission, the State Commission and the National Commission) Rules, 2021).

(b) The Complainant resides/personally works for gain at पटना, बिहार, within the area of this Commission (Section 34 of the Consumer Protection Act, 2019).

**3. Limitation**

The cause of action arose on or about 10 October 2026. This complaint is filed within the period allowed (Section 69 of the Consumer Protection Act, 2019).

**4. Relief sought**

The Complainant respectfully requests this Commission to direct the Opposite Party to:
(a) grant the following relief: refund;
(b) pay such compensation and costs as this Commission considers just (Section 39 of the Consumer Protection Act, 2019).

**5. List of documents**

1. order ID
2. photos

**Verification**

I, [YOUR FULL NAME], the Complainant, state that the contents of this complaint are true and correct to the best of my knowledge and belief, and nothing material has been concealed.

Place: [PLACE]
Date: [DATE]

[SIGNATURE OF COMPLAINANT]

```