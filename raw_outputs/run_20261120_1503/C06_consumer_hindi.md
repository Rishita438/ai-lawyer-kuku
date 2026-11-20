# C06_consumer_hindi
**Category:** language-hindi  
**Description:** Story in Devanagari Hindi. Questions and answer should be in Hindi.  
**Pack:** consumer  
**Run at:** 2026-11-20T15:06:08  
**Models that answered:** openai/gpt-oss-120b (18 calls)  
**Time:** 161.8 s

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

**Bot:** मैं समझता हूँ कि आपको साड़ी में समस्या हुई है। क्या आपने यह अपने निजी इस्तेमाल के लिए लिया था, या व्यापार / आगे बेचने के लिए?

**User:** अपने इस्तेमाल के लिए

**Bot:** मैं समझता हूँ कि आप अपने इस्तेमाल के बारे में बता रहे हैं। क्या आपने यह ऑनलाइन (वेबसाइट/ऐप) खरीदा था या किसी दुकान से?

**User:** pata nahi

**Bot:** मैं समझता हूँ कि आप निश्चित नहीं हैं। समस्या किस तारीख को हुई, या रिफंड कब मिलना था?

**User:** 10 अक्टूबर 2026

**Bot:** मैं समझ गया हूँ। क्या आपने विक्रेता या प्लेटफ़ॉर्म से पहले शिकायत की है? अगर हाँ, तो कैसे और कब, और उन्होंने क्या कहा?

**User:** ऐप पर शिकायत की, जवाब नहीं आया

**Bot:** मैं समझता हूँ कि आपने ऐप पर शिकायत की थी और अभी तक जवाब नहीं मिला है। आपके पास क्या सबूत है? (बिल/इनवॉइस, ऑर्डर आईडी, पेमेंट स्क्रीनशॉट, ईमेल, चैट, फ़ोटो, वारंटी कार्ड)

**User:** ऑर्डर आईडी और फ़ोटो

**Bot:** मैंने आपका ऑर्डर आईडी और फोटो प्राप्त कर लिया है। आप क्या चाहते हैं - रिफंड, बदला हुआ सामान, मरम्मत, या मुआवज़ा? (आपने बताया: refund - क्या यह सही है?)

**User:** रिफंड

**Bot:** मैं समझ गया हूँ। आप किस शहर और राज्य में रहते हैं? (इससे तय होता है कि आप शिकायत कहाँ दर्ज कर सकते हैं।)

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
  "what_went_wrong": "साड़ी फटी हुई आई",
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

आप एक उपभोक्ता हैं और खरीदी गई साड़ी में दोष है। आप अभी भी दो साल की समय सीमा के भीतर हैं और पटना के जिला उपभोक्ता आयोग में कोई शुल्क नहीं देकर रिफंड की मांग कर सकते हैं।

- आप उपभोक्ता माने जाते हैं क्योंकि आपने व्यक्तिगत उपयोग के लिये साड़ी खरीदी और कीमत चुकाई है।<br><small>📘 **Consumer Protection Act, 2019, s. 2(7)**: Who is a "consumer" — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)</small>

- साड़ी फटी हुई आई है, जो वस्तु के दोष (defect) के रूप में माना जाता है, और विक्रेता द्वारा रिफंड न देना संभावित रूप से अनुचित व्यापार प्रथा (unfair trade practice) हो सकता है।<br><small>📘 **Consumer Protection Act, 2019, s. 2(10)**: What is a "defect" (goods) — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)<br>📘 **Consumer Protection Act, 2019, s. 2(47)**: What is an "unfair trade practice" — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)</small>

- उपभोक्ता शिकायत दाखिल करने की समय सीमा दो साल है; आपका मामला अभी भी इस सीमा के भीतर है।<br><small>📘 **Consumer Protection Act, 2019, s. 69**: Time limit for filing a complaint — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)</small>

- भुगतान की राशि (₹2,500) के आधार पर आप पटना, बिहार में जिला उपभोक्ता आयोग में शिकायत दर्ज कर सकते हैं।<br><small>📘 **Consumer Protection Act, 2019, s. 34**: District Commission - which one you can file in — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)<br>📘 **Consumer Protection (Jurisdiction of the District Commission, the State Commission and the National Commission) Rules, 2021, Rules 3-5**: Money limits - which Commission — [source](https://www.pib.gov.in/PressReleasePage.aspx?PRID=1786342) (✅ verified 2026-11-19)</small>

- यदि आयोग आपके दावे को मानता है तो वह विक्रेता को रिफंड, ब्याज और संभावित क्षतिपूर्ति देने का आदेश दे सकता है।<br><small>📘 **Consumer Protection Act, 2019, s. 39**: What the Commission can order — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)</small>

#### Key facts (calculated by the app, not the AI)

⏳ **Time limit:** ✅ within the limit. Normally file by **2028-10-10** (2 years from 2026-10-10; dates are approximate).

🏛️ **Which Commission:** District Consumer Commission, for Rs 2,500 paid (you can file where you live or work: पटना, बिहार).

💰 **Filing fee:** nil (no fee).

<small>Based on: 📘 **Consumer Protection Act, 2019, s. 34**: District Commission - which one you can file in — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19); 📘 **Consumer Protection Act, 2019, s. 69**: Time limit for filing a complaint — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19); 📘 **Consumer Protection (Consumer Disputes Redressal Commissions) Rules, 2020, Rule 7 (fee table)**: Fee for filing a consumer complaint — [source](https://egazette.gov.in/WriteReadData/2023/248158.pdf) (✅ verified 2026-11-19); 📘 **Consumer Protection (Jurisdiction of the District Commission, the State Commission and the National Commission) Rules, 2021, Rules 3-5**: Money limits - which Commission — [source](https://www.pib.gov.in/PressReleasePage.aspx?PRID=1786342) (✅ verified 2026-11-19)</small>

### Your options

**1. National Consumer Helpline** — पहले निवारक कदम के रूप में शिकायत दर्ज कर सकते हैं।
   - 1915 या 1800‑11‑4000 पर कॉल करें (रोज़ 8 am‑8 pm, छुट्टियों को छोड़कर)।
   - SMS 8800001915 भेजें या NCH की वेबसाइट/WhatsApp/UMANG ऐप पर grievance दर्ज करें।
   - यदि समाधान नहीं मिलता तो आगे की कानूनी कार्रवाई पर विचार करें।

   <small>📘 **National Consumer Helpline (consumerhelpline.gov.in), Contact page and FAQ**: National Consumer Helpline (pre-litigation step) — [source](https://consumerhelpline.gov.in/) (✅ verified 2026-11-19)</small>

**2. Online complaint (e‑Jagriti)** — डिजिटल रूप से जिला आयोग में शिकायत दाखिल करना तेज़ और मुफ्त है।
   - e‑Jagriti पोर्टल (https://ejagriti.gov.in) पर जाएँ।
   - उपभोक्ता के रूप में पंजीकरण करें और अपना विवरण भरें।
   - ऑर्डर आईडी, फोटो और रिफंड की मांग सहित सभी साक्ष्य अपलोड करें।
   - शुल्क शून्य है; ‘सबमिट’ पर क्लिक करके शिकायत दर्ज करें।

   <small>📘 **e-Jagriti (Department of Consumer Affairs)**: File online on e-Jagriti — [source](https://e-jagriti.gov.in/) (✅ verified 2026-11-19)<br>📘 **Consumer Protection Act, 2019, s. 35**: How a complaint is filed — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)<br>📘 **Consumer Protection (Consumer Disputes Redressal Commissions) Rules, 2020, Rule 7 (fee table)**: Fee for filing a consumer complaint — [source](https://egazette.gov.in/WriteReadData/2023/248158.pdf) (✅ verified 2026-11-19)</small>

**3. E‑commerce grievance officer** — यदि खरीद ऑनलाइन प्लेटफ़ॉर्म से हुई है तो प्लेटफ़ॉर्म को भी जवाबदेह ठहराया जा सकता है।
   - प्लेटफ़ॉर्म की वेबसाइट या ऐप पर grievance officer के संपर्क विवरण खोजें।
   - 48 घंटे के भीतर acknowledgement की माँग करें।
   - एक महीने के भीतर समाधान न मिलने पर उपभोक्ता आयोग में आगे की कार्रवाई करें।

   <small>📘 **Consumer Protection (E-Commerce) Rules, 2020, Rule 4(4)-(5)**: E-commerce grievance officer — [source](https://egazette.gov.in/WriteReadData/2020/220661.pdf) (✅ verified 2026-11-19)</small>

**4. Free legal aid** — यदि आप आय या सामाजिक वर्ग के मानदंडों को पूरा करते हैं तो वकील की मदद मुफ्त मिल सकती है।
   - नालसा या अपने जिला लीगल सर्विसेज अथॉरिटी से संपर्क करें (टोल‑फ्री 15100)।
   - आधार कार्ड, आय प्रमाण, और उपभोक्ता शिकायत का सार लिखित में तैयार रखें।
   - आवेदन जमा करें; यदि स्वीकृत हो तो वकील आपके पक्ष में शिकायत तैयार करेगा।

   <small>📘 **Legal Services Authorities Act, 1987, s. 12**: Who can get free legal aid — [source](https://indiacode.gov.in/act/a742f03e-3129-4b8d-8dda-af2a36190b18/sections?spc.sf=dc.date.issued&spc.sd=DESC&spc.page=2&spc.rpp=10) (✅ verified 2026-11-19)<br>📘 **National Legal Services Authority**: How to reach free legal aid — [source](https://nalsa.gov.in/legal-aid/#Free-Legal-Aid) (✅ verified 2026-11-19)</small>

### ⚖️ When to get a real lawyer
- शिकायत तैयार करने, सबूत व्यवस्थित करने और आयोग में प्रतिनिधित्व करने में वकील की सहायता से प्रक्रिया तेज़ और प्रभावी हो सकती है।
- Free legal help may be available: District Legal Services Authority / NALSA helpline **15100**.

### What I'm not sure about
- साड़ी की खरीद ऑनलाइन हुई या नहीं, इस पर जानकारी नहीं है; इसलिए ई‑कॉमर्स grievance officer की प्रक्रिया लागू है या नहीं, यह स्पष्ट नहीं है।

---
<small>Knowledge base last verified: 2026-11-19. Only verified sources are cited. This is general information, not legal advice.</small>

## Safety checker log (items removed from the AI's draft)
```json
[]
```

## Raw model JSON for the answer (before the safety checker)
```json
{
 "summary": "आप एक उपभोक्ता हैं और खरीदी गई साड़ी में दोष है। आप अभी भी दो साल की समय सीमा के भीतर हैं और पटना के जिला उपभोक्ता आयोग में कोई शुल्क नहीं देकर रिफंड की मांग कर सकते हैं।",
 "points": [
  {
   "text": "आप उपभोक्ता माने जाते हैं क्योंकि आपने व्यक्तिगत उपयोग के लिये साड़ी खरीदी और कीमत चुकाई है।",
   "kb_ids": [
    "CPA2019-S2-7"
   ]
  },
  {
   "text": "साड़ी फटी हुई आई है, जो वस्तु के दोष (defect) के रूप में माना जाता है, और विक्रेता द्वारा रिफंड न देना संभावित रूप से अनुचित व्यापार प्रथा (unfair trade practice) हो सकता है।",
   "kb_ids": [
    "CPA2019-S2-10",
    "CPA2019-S2-47"
   ]
  },
  {
   "text": "उपभोक्ता शिकायत दाखिल करने की समय सीमा दो साल है; आपका मामला अभी भी इस सीमा के भीतर है।",
   "kb_ids": [
    "CPA2019-S69"
   ]
  },
  {
   "text": "भुगतान की राशि (₹2,500) के आधार पर आप पटना, बिहार में जिला उपभोक्ता आयोग में शिकायत दर्ज कर सकते हैं।",
   "kb_ids": [
    "CPA2019-S34",
    "CPR2021-PECUNIARY"
   ]
  },
  {
   "text": "यदि आयोग आपके दावे को मानता है तो वह विक्रेता को रिफंड, ब्याज और संभावित क्षतिपूर्ति देने का आदेश दे सकता है।",
   "kb_ids": [
    "CPA2019-S39"
   ]
  }
 ],
 "options": [
  {
   "title": "National Consumer Helpline",
   "why": "पहले निवारक कदम के रूप में शिकायत दर्ज कर सकते हैं।",
   "steps": [
    "1915 या 1800‑11‑4000 पर कॉल करें (रोज़ 8 am‑8 pm, छुट्टियों को छोड़कर)।",
    "SMS 8800001915 भेजें या NCH की वेबसाइट/WhatsApp/UMANG ऐप पर grievance दर्ज करें।",
    "यदि समाधान नहीं मिलता तो आगे की कानूनी कार्रवाई पर विचार करें।"
   ],
   "kb_ids": [
    "PROC-NCH"
   ]
  },
  {
   "title": "Online complaint (e‑Jagriti)",
   "why": "डिजिटल रूप से जिला आयोग में शिकायत दाखिल करना तेज़ और मुफ्त है।",
   "steps": [
    "e‑Jagriti पोर्टल (https://ejagriti.gov.in) पर जाएँ।",
    "उपभोक्ता के रूप में पंजीकरण करें और अपना विवरण भरें।",
    "ऑर्डर आईडी, फोटो और रिफंड की मांग सहित सभी साक्ष्य अपलोड करें।",
    "शुल्क शून्य है; ‘सबमिट’ पर क्लिक करके शिकायत दर्ज करें।"
   ],
   "kb_ids": [
    "PROC-EJAGRITI",
    "CPA2019-S35",
    "CPR2020-FEES"
   ]
  },
  {
   "title": "E‑commerce grievance officer",
   "why": "यदि खरीद ऑनलाइन प्लेटफ़ॉर्म से हुई है तो प्लेटफ़ॉर्म को भी जवाबदेह ठहराया जा सकता है।",
   "steps": [
    "प्लेटफ़ॉर्म की वेबसाइट या ऐप पर grievance officer के संपर्क विवरण खोजें।",
    "48 घंटे के भीतर acknowledgement की माँग करें।",
    "एक महीने के भीतर समाधान न मिलने पर उपभोक्ता आयोग में आगे की कार्रवाई करें।"
   ],
   "kb_ids": [
    "ECOM2020-R4-5"
   ]
  },
  {
   "title": "Free legal aid",
   "why": "यदि आप आय या सामाजिक वर्ग के मानदंडों को पूरा करते हैं तो वकील की मदद मुफ्त मिल सकती है।",
   "steps": [
    "नालसा या अपने जिला लीगल सर्विसेज अथॉरिटी से संपर्क करें (टोल‑फ्री 15100)।",
    "आधार कार्ड, आय प्रमाण, और उपभोक्ता शिकायत का सार लिखित में तैयार रखें।",
    "आवेदन जमा करें; यदि स्वीकृत हो तो वकील आपके पक्ष में शिकायत तैयार करेगा।"
   ],
   "kb_ids": [
    "LSA1987-S12",
    "PROC-NALSA"
   ]
  }
 ],
 "uncertainties": [
  "साड़ी की खरीद ऑनलाइन हुई या नहीं, इस पर जानकारी नहीं है; इसलिए ई‑कॉमर्स grievance officer की प्रक्रिया लागू है या नहीं, यह स्पष्ट नहीं है।"
 ],
 "suggest_lawyer": true,
 "lawyer_reason": "शिकायत तैयार करने, सबूत व्यवस्थित करने और आयोग में प्रतिनिधित्व करने में वकील की सहायता से प्रक्रिया तेज़ और प्रभावी हो सकती है।"
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

1. I purchased a sari from Meeshow [BOUGHT ONLINE] on 10 October 2026, paying Rs 2,500.

2. The sari arrived torn.

3. I lodged a complaint on the app on 10 October 2026, but received no response.

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