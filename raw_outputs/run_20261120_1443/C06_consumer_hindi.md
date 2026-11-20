# C06_consumer_hindi
**Category:** language-hindi  
**Description:** Story in Devanagari Hindi. Questions and answer should be in Hindi.  
**Pack:** consumer  
**Run at:** 2026-11-20T14:50:19  
**Models that answered:** openai/gpt-oss-120b (18 calls)  
**Time:** 105.4 s

> Unedited output of scripts/run_tests.py. Nothing below was changed by hand.

## Automatic checks
| Check | Result | Detail |
|---|---|---|
| escalation | PASS | expected none, got none |
| language | PASS | expected hi, got hi |
| document grievance_letter | **FAIL** | expected unlocked, got locked/absent |

## Conversation
**Bot:** Tell me what happened, in your own words - English, Hindi or Hinglish is fine. For example: what you bought, from whom, and what went wrong.

**User:** मैंने 10 अक्टूबर 2026 को मीशो से 2500 रुपये की साड़ी मंगवाई थी, लेकिन फटी हुई आई। रिफंड नहीं मिल रहा।

**Bot:** मैं समझता हूँ कि आपको वस्तु में समस्या हुई है। क्या आपने यह अपने निजी इस्तेमाल के लिए लिया था, या व्यापार / आगे बेचने के लिए?

**User:** अपने इस्तेमाल के लिए

**Bot:** समझ गया। क्या आपने यह ऑनलाइन (वेबसाइट/ऐप) खरीदा था या किसी दुकान से?

**User:** pata nahi

**Bot:** मैं समझता हूँ कि आपको जानकारी नहीं है। समस्या किस तारीख को हुई, या रिफंड कब मिलना था?

**User:** 10 अक्टूबर 2026

**Bot:** मैं समझ गया। क्या आपने विक्रेता या प्लेटफ़ॉर्म से पहले शिकायत की है? अगर हाँ, तो कैसे और कब, और उन्होंने क्या कहा?

**User:** ऐप पर शिकायत की, जवाब नहीं आया

**Bot:** मैं समझता हूँ कि आपने ऐप पर शिकायत की थी। आपके पास क्या सबूत है? (बिल/इनवॉइस, ऑर्डर आईडी, पेमेंट स्क्रीनशॉट, ईमेल, चैट, फ़ोटो, वारंटी कार्ड)

**User:** ऑर्डर आईडी और फ़ोटो

**Bot:** मैंने आपका ऑर्डर आईडी और फ़ोटो प्राप्त कर लिया है। आप क्या चाहते हैं - रिफंड, बदला हुआ सामान, मरम्मत, या मुआवज़ा? (आपने बताया: refund - क्या यह सही है?)

**User:** रिफंड

**Bot:** मैं समझता हूँ कि आप रिफंड के बारे में जानकारी चाहते हैं। आप किस शहर और राज्य में रहते हैं? (इससे तय होता है कि आप शिकायत कहाँ दर्ज कर सकते हैं।)

**User:** पटना, बिहार

**Bot:** धन्यवाद, अब आपके केस की मुख्य जानकारी हमारे पास है।

## Case file (final)
```json
{
 "pack": "consumer",
 "facts": {
  "product_or_service": "साड़ी",
  "seller_name": "मीशो",
  "for_business_use": false,
  "bought_online": "unknown",
  "amount_paid": 2500,
  "purchase_date": "2026-10-10",
  "what_went_wrong": "साड़ी फटी हुई आई। रिफंड नहीं मिल रहा।",
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
  "pata nahi",
  "10 अक्टूबर 2026",
  "ऐप पर शिकायत की, जवाब नहीं आया",
  "ऑर्डर आईडी और फ़ोटो",
  "रिफंड",
  "पटना, बिहार"
 ],
 "suggested": {
  "desired_outcome": "refund"
 }
}
```

## Answer shown to the user

### Where you stand

आप एक उपभोक्ता हैं और खरीदी गई साड़ी में दोष है। विक्रेता ने रिफंड नहीं दिया, जो अनुचित व्यापार प्रथा माना जाता है, इसलिए आप दो साल के भीतर जिला उपभोक्ता आयोग में शिकायत दर्ज कर सकते हैं।

- आप उपभोक्ता हैं क्योंकि आपने कीमत चुकाकर साड़ी खरीदी थी और यह व्यक्तिगत उपयोग के लिये था।<br><small>📘 **Consumer Protection Act, 2019, s. 2(7)**: Who is a "consumer" — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)</small>

- साड़ी फटी हुई आई है, इसलिए यह वस्तु में दोष (defect) है, और विक्रेता द्वारा रिफंड न देना अनुचित व्यापार प्रथा (unfair trade practice) माना जाता है।<br><small>📘 **Consumer Protection Act, 2019, s. 2(10)**: What is a "defect" (goods) — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)<br>📘 **Consumer Protection Act, 2019, s. 2(47)**: What is an "unfair trade practice" — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)</small>

- आपको अपनी शिकायत दो साल के भीतर (अधिकतम 2028‑10‑10) दर्ज करनी होगी; देर से दाखिल करने पर भी कारण बताकर अनुमति मिल सकती है।<br><small>📘 **Consumer Protection Act, 2019, s. 69**: Time limit for filing a complaint — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)</small>

- राशि ₹2,500 होने के कारण जिला उपभोक्ता आयोग (पटना) उपयुक्त फोरम है, फ़ाइलिंग शुल्क शून्य है, और आयोग दोष हटाने, वस्तु बदलने या रिफंड सहित अन्य उपाय आदेश दे सकता है।<br><small>📘 **Consumer Protection (Jurisdiction of the District Commission, the State Commission and the National Commission) Rules, 2021, Rules 3-5**: Money limits - which Commission — [source](https://www.pib.gov.in/PressReleasePage.aspx?PRID=1786342) (✅ verified 2026-11-19)<br>📘 **Consumer Protection Act, 2019, s. 34**: District Commission - which one you can file in — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)<br>📘 **Consumer Protection (Consumer Disputes Redressal Commissions) Rules, 2020, Rule 7 (fee table)**: Fee for filing a consumer complaint — [source](https://egazette.gov.in/WriteReadData/2023/248158.pdf) (✅ verified 2026-11-19)<br>📘 **Consumer Protection Act, 2019, s. 39**: What the Commission can order — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)</small>

#### Key facts (calculated by the app, not the AI)

⏳ **Time limit:** ✅ within the limit. Normally file by **2028-10-10** (2 years from 2026-10-10; dates are approximate).

🏛️ **Which Commission:** District Consumer Commission, for Rs 2,500 paid (you can file where you live or work: पटना, बिहार).

💰 **Filing fee:** nil (no fee).

<small>Based on: 📘 **Consumer Protection Act, 2019, s. 34**: District Commission - which one you can file in — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19); 📘 **Consumer Protection Act, 2019, s. 69**: Time limit for filing a complaint — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19); 📘 **Consumer Protection (Consumer Disputes Redressal Commissions) Rules, 2020, Rule 7 (fee table)**: Fee for filing a consumer complaint — [source](https://egazette.gov.in/WriteReadData/2023/248158.pdf) (✅ verified 2026-11-19); 📘 **Consumer Protection (Jurisdiction of the District Commission, the State Commission and the National Commission) Rules, 2021, Rules 3-5**: Money limits - which Commission — [source](https://www.pib.gov.in/PressReleasePage.aspx?PRID=1786342) (✅ verified 2026-11-19)</small>

### Your options

**1. राष्ट्रीय उपभोक्ता हेल्पलाइन** — पहले बिना लागत के मदद ले सकते हैं और अक्सर समस्या जल्दी सुलझ जाती है।
   - 1915 या 1800‑11‑4000 पर कॉल करें (रोज़ 8 am‑8 pm, छुट्टियों को छोड़कर)।
   - SMS 8800001915 भेजें या NCH की वेबसाइट/WhatsApp/UMANG ऐप पर grievance दर्ज करें।
   - हेल्पलाइन आपके grievance को संबंधित प्राधिकरण तक पहुँचाएगी।

   <small>📘 **National Consumer Helpline (consumerhelpline.gov.in), Contact page and FAQ**: National Consumer Helpline (pre-litigation step) — [source](https://consumerhelpline.gov.in/) (✅ verified 2026-11-19)</small>

**2. ऑनलाइन शिकायत (e‑Jagriti)** — सरकारी पोर्टल पर मुफ्त में औपचारिक शिकायत दर्ज कर सकते हैं।
   - e‑Jagriti (https://ejagriti.gov.in) पर जाएँ।
   - ‘नया केस’ चुनें और उपभोक्ता शिकायत फ़ॉर्म भरें।
   - ऑर्डर आईडी, फ़ोटो और अन्य साक्ष्य अपलोड करें।
   - फ़ॉर्म जमा करें; कोई फ़ाइलिंग शुल्क नहीं है।

   <small>📘 **e-Jagriti (Department of Consumer Affairs)**: File online on e-Jagriti — [source](https://e-jagriti.gov.in/) (✅ verified 2026-11-19)<br>📘 **Consumer Protection Act, 2019, s. 35**: How a complaint is filed — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)</small>

**3. ई‑कॉमर्स ग्रिवेंस अधिकारी (यदि लागू हो)** — यदि साड़ी ऑनलाइन प्लेटफ़ॉर्म से खरीदी गई थी तो प्लेटफ़ॉर्म को 48 घंटे में जवाब देना और एक महीने में समाधान देना अनिवार्य है।
   - प्लेटफ़ॉर्म की वेबसाइट या ऐप पर grievance officer के संपर्क विवरण खोजें।
   - उन्हें लिखित/ई‑मेल में समस्या और साक्ष्य भेजें।
   - 48 घंटे में acknowledgment की पुष्टि करें और 30 दिन के भीतर समाधान का अनुरोध करें।

   <small>📘 **Consumer Protection (E-Commerce) Rules, 2020, Rule 4(4)-(5)**: E-commerce grievance officer — [source](https://egazette.gov.in/WriteReadData/2020/220661.pdf) (✅ verified 2026-11-19)</small>

**4. मुफ़्त कानूनी सहायता** — यदि आय या सामाजिक वर्ग के कारण आप पात्र हैं तो वकील की मदद बिना खर्च के मिल सकती है।
   - अपने निकटतम जिला कानूनी सेवा प्राधिकरण (DLDA) या NALSA की वेबसाइट पर जाएँ।
   - आवेदन फ़ॉर्म भरें (पहचान प्रमाण और आय प्रमाण साथ रखें)।
   - टोल‑फ्री हेल्पलाइन 15100 पर कॉल करके मार्गदर्शन प्राप्त करें।

   <small>📘 **Legal Services Authorities Act, 1987, s. 12**: Who can get free legal aid — [source](https://indiacode.gov.in/act/a742f03e-3129-4b8d-8dda-af2a36190b18/sections?spc.sf=dc.date.issued&spc.sd=DESC&spc.page=2&spc.rpp=10) (✅ verified 2026-11-19)<br>📘 **National Legal Services Authority**: How to reach free legal aid — [source](https://nalsa.gov.in/legal-aid/#Free-Legal-Aid) (✅ verified 2026-11-19)</small>

### What I'm not sure about
- साड़ी ऑनलाइन खरीदी गई थी या नहीं, इसलिए ई‑कॉमर्स grievance officer के बारे में निश्चित नहीं कहा जा सकता।
- विक्रेता के साथ कोई लिखित रिटर्न/रिफंड नीति थी या नहीं, यह जानकारी नहीं मिली।

---
<small>Knowledge base last verified: 2026-11-19. Only verified sources are cited. This is general information, not legal advice.</small>

## Safety checker log (items removed from the AI's draft)
```json
[]
```

## Raw model JSON for the answer (before the safety checker)
```json
{
 "summary": "आप एक उपभोक्ता हैं और खरीदी गई साड़ी में दोष है। विक्रेता ने रिफंड नहीं दिया, जो अनुचित व्यापार प्रथा माना जाता है, इसलिए आप दो साल के भीतर जिला उपभोक्ता आयोग में शिकायत दर्ज कर सकते हैं।",
 "points": [
  {
   "text": "आप उपभोक्ता हैं क्योंकि आपने कीमत चुकाकर साड़ी खरीदी थी और यह व्यक्तिगत उपयोग के लिये था।",
   "kb_ids": [
    "CPA2019-S2-7"
   ]
  },
  {
   "text": "साड़ी फटी हुई आई है, इसलिए यह वस्तु में दोष (defect) है, और विक्रेता द्वारा रिफंड न देना अनुचित व्यापार प्रथा (unfair trade practice) माना जाता है।",
   "kb_ids": [
    "CPA2019-S2-10",
    "CPA2019-S2-47"
   ]
  },
  {
   "text": "आपको अपनी शिकायत दो साल के भीतर (अधिकतम 2028‑10‑10) दर्ज करनी होगी; देर से दाखिल करने पर भी कारण बताकर अनुमति मिल सकती है।",
   "kb_ids": [
    "CPA2019-S69"
   ]
  },
  {
   "text": "राशि ₹2,500 होने के कारण जिला उपभोक्ता आयोग (पटना) उपयुक्त फोरम है, फ़ाइलिंग शुल्क शून्य है, और आयोग दोष हटाने, वस्तु बदलने या रिफंड सहित अन्य उपाय आदेश दे सकता है।",
   "kb_ids": [
    "CPR2021-PECUNIARY",
    "CPA2019-S34",
    "CPR2020-FEES",
    "CPA2019-S39"
   ]
  }
 ],
 "options": [
  {
   "title": "राष्ट्रीय उपभोक्ता हेल्पलाइन",
   "why": "पहले बिना लागत के मदद ले सकते हैं और अक्सर समस्या जल्दी सुलझ जाती है।",
   "steps": [
    "1915 या 1800‑11‑4000 पर कॉल करें (रोज़ 8 am‑8 pm, छुट्टियों को छोड़कर)।",
    "SMS 8800001915 भेजें या NCH की वेबसाइट/WhatsApp/UMANG ऐप पर grievance दर्ज करें।",
    "हेल्पलाइन आपके grievance को संबंधित प्राधिकरण तक पहुँचाएगी।"
   ],
   "kb_ids": [
    "PROC-NCH"
   ]
  },
  {
   "title": "ऑनलाइन शिकायत (e‑Jagriti)",
   "why": "सरकारी पोर्टल पर मुफ्त में औपचारिक शिकायत दर्ज कर सकते हैं।",
   "steps": [
    "e‑Jagriti (https://ejagriti.gov.in) पर जाएँ।",
    "‘नया केस’ चुनें और उपभोक्ता शिकायत फ़ॉर्म भरें।",
    "ऑर्डर आईडी, फ़ोटो और अन्य साक्ष्य अपलोड करें।",
    "फ़ॉर्म जमा करें; कोई फ़ाइलिंग शुल्क नहीं है।"
   ],
   "kb_ids": [
    "PROC-EJAGRITI",
    "CPA2019-S35"
   ]
  },
  {
   "title": "ई‑कॉमर्स ग्रिवेंस अधिकारी (यदि लागू हो)",
   "why": "यदि साड़ी ऑनलाइन प्लेटफ़ॉर्म से खरीदी गई थी तो प्लेटफ़ॉर्म को 48 घंटे में जवाब देना और एक महीने में समाधान देना अनिवार्य है।",
   "steps": [
    "प्लेटफ़ॉर्म की वेबसाइट या ऐप पर grievance officer के संपर्क विवरण खोजें।",
    "उन्हें लिखित/ई‑मेल में समस्या और साक्ष्य भेजें।",
    "48 घंटे में acknowledgment की पुष्टि करें और 30 दिन के भीतर समाधान का अनुरोध करें।"
   ],
   "kb_ids": [
    "ECOM2020-R4-5"
   ]
  },
  {
   "title": "मुफ़्त कानूनी सहायता",
   "why": "यदि आय या सामाजिक वर्ग के कारण आप पात्र हैं तो वकील की मदद बिना खर्च के मिल सकती है।",
   "steps": [
    "अपने निकटतम जिला कानूनी सेवा प्राधिकरण (DLDA) या NALSA की वेबसाइट पर जाएँ।",
    "आवेदन फ़ॉर्म भरें (पहचान प्रमाण और आय प्रमाण साथ रखें)।",
    "टोल‑फ्री हेल्पलाइन 15100 पर कॉल करके मार्गदर्शन प्राप्त करें।"
   ],
   "kb_ids": [
    "LSA1987-S12",
    "PROC-NALSA"
   ]
  }
 ],
 "uncertainties": [
  "साड़ी ऑनलाइन खरीदी गई थी या नहीं, इसलिए ई‑कॉमर्स grievance officer के बारे में निश्चित नहीं कहा जा सकता।",
  "विक्रेता के साथ कोई लिखित रिटर्न/रिफंड नीति थी या नहीं, यह जानकारी नहीं मिली।"
 ],
 "suggest_lawyer": false,
 "lawyer_reason": ""
}
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
Meeshow, [OPPOSITE PARTY'S REGISTERED ADDRESS – see your invoice or the website's legal/contact page]

---

**COMPLAINT**

**1. Facts of the case**

1. I bought the sari [BOUGHT ONLINE] from Meeshow on 10 October 2026, paying Rs 2,500.

2. The sari arrived torn.

3. I am not receiving a refund.

4. I lodged a complaint on the app, but no response was received.

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