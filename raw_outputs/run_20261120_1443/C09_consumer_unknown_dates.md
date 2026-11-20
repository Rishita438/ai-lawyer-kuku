# C09_consumer_unknown_dates
**Category:** edge-missing-facts  
**Description:** User doesn't know key dates. Complaint must be locked; letter uses placeholders, not guesses.  
**Pack:** consumer  
**Run at:** 2026-11-20T14:55:39  
**Models that answered:** openai/gpt-oss-120b (16 calls)  
**Time:** 92.2 s

> Unedited output of scripts/run_tests.py. Nothing below was changed by hand.

## Automatic checks
| Check | Result | Detail |
|---|---|---|
| escalation | PASS | expected none, got none |
| document grievance_letter | PASS | expected unlocked, got unlocked |
| document commission_complaint | PASS | expected locked/absent, got locked/absent (When did you buy it (approximate date is fine)? (tip: check your invoice or order history); On what date did the problem happen, or the refund become due? (tip: the date the product failed or the refund was due)) |

## Conversation
**Bot:** Tell me what happened, in your own words - English, Hindi or Hinglish is fine. For example: what you bought, from whom, and what went wrong.

**User:** maine amazon se ek mixer grinder liya tha 3200 ka, kuch time baad kharab ho gaya, date yaad nahi

**Bot:** Samajh gaya, aapka mixer grinder kharab ho gaya. Kya aapne yeh apne personal use ke liye liya tha, ya business / aage bechne ke liye?

**User:** ghar ke liye

**Bot:** Aapne ghar ke liye bataya. Problem kis date ko hui, ya refund kab milna tha? (Aapne bataya: unknown - sahi hai?)

**User:** pata nahi

**Bot:** Samajh gaya, aapko is baare mein pata nahi hai. Kya aapne seller ya platform ko pehle complain kiya hai? Agar haan, to kaise aur kab, aur unhone kya kaha?

**User:** abhi tak nahi kiya

**Bot:** मैं समझता हूँ कि आपने अभी तक नहीं किया है। आपके पास क्या सबूत है? (बिल/इनवॉइस, ऑर्डर आईडी, पेमेंट स्क्रीनशॉट, ईमेल, चैट, फ़ोटो, वारंटी कार्ड)

**User:** order history mein hoga

**Bot:** मैं समझ गया कि आप ऑर्डर इतिहास देखना चाहते हैं। आप क्या चाहते हैं - रिफंड, बदला हुआ सामान, मरम्मत, या मुआवज़ा?

**User:** repair ya replacement

**Bot:** मैं समझता हूँ कि आप मरम्मत या प्रतिस्थापन चाहते हैं। आप किस शहर और राज्य में रहते हैं? (इससे तय होता है कि आप शिकायत कहाँ दर्ज कर सकते हैं।)

**User:** Kolkata, West Bengal

**Bot:** धन्यवाद, अब आपके मामले की मुख्य जानकारी हमारे पास है।

## Case file (final)
```json
{
 "pack": "consumer",
 "facts": {
  "product_or_service": "mixer grinder",
  "seller_name": "Amazon",
  "for_business_use": false,
  "bought_online": true,
  "amount_paid": 3200,
  "purchase_date": "unknown",
  "what_went_wrong": "Mixer grinder stopped working / broke after some time",
  "problem_date": "unknown",
  "complaints_made": "No complaint made",
  "evidence": [
   "order history"
  ],
  "desired_outcome": "repair or replacement",
  "user_city_state": "Kolkata, West Bengal"
 },
 "language": "hi",
 "user_messages": [
  "maine amazon se ek mixer grinder liya tha 3200 ka, kuch time baad kharab ho gaya, date yaad nahi",
  "ghar ke liye",
  "pata nahi",
  "abhi tak nahi kiya",
  "order history mein hoga",
  "repair ya replacement",
  "Kolkata, West Bengal"
 ],
 "suggested": {
  "problem_date": "unknown"
 }
}
```

## Answer shown to the user

### Where you stand

आप एक उपभोक्ता हैं और खरीदा गया मिक्सर ग्राइंडर दोषपूर्ण माना जा सकता है। आप पहले Amazon के ई‑कॉमर्स grievance officer से संपर्क कर सकते हैं, और यदि समाधान नहीं मिलता तो जिला उपभोक्ता आयोग में शिकायत दर्ज कर सकते हैं, जिसमें कोई शुल्क नहीं है।

- आपने 3,200 रुपये में ऑनलाइन मिक्सर ग्राइंडर खरीदा है, इसलिए आप उपभोक्ता (consumer) माने जाते हैं।<br><small>📘 **Consumer Protection Act, 2019, s. 2(7)**: Who is a "consumer" — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)</small>

- उपकरण का काम बंद हो जाना एक दोष (defect) है, जो उपभोक्ता संरक्षण कानून में शामिल है।<br><small>📘 **Consumer Protection Act, 2019, s. 2(10)**: What is a "defect" (goods) — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)</small>

- आपकी शिकायत को जिला उपभोक्ता आयोग में दायर किया जा सकता है, क्योंकि भुगतान की राशि 50 लाख रुपये से नीचे है और आप कोलकाता में रहते हैं।<br><small>📘 **Consumer Protection Act, 2019, s. 34**: District Commission - which one you can file in — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)<br>📘 **Consumer Protection (Jurisdiction of the District Commission, the State Commission and the National Commission) Rules, 2021, Rules 3-5**: Money limits - which Commission — [source](https://www.pib.gov.in/PressReleasePage.aspx?PRID=1786342) (✅ verified 2026-11-19)</small>

- डिस्ट्रिक्ट आयोग में शिकायत दाखिल करने के लिए कोई फ़ाइलिंग शुल्क नहीं है (₹0)।<br><small>📘 **Consumer Protection (Consumer Disputes Redressal Commissions) Rules, 2020, Rule 7 (fee table)**: Fee for filing a consumer complaint — [source](https://egazette.gov.in/WriteReadData/2023/248158.pdf) (✅ verified 2026-11-19)</small>

#### Key facts (calculated by the app, not the AI)

⏳ **Time limit:** can't calculate - the date the problem arose is unknown. The normal limit is 2 years from that date.

🏛️ **Which Commission:** District Consumer Commission, for Rs 3,200 paid (you can file where you live or work: Kolkata, West Bengal).

💰 **Filing fee:** nil (no fee).

<small>Based on: 📘 **Consumer Protection Act, 2019, s. 34**: District Commission - which one you can file in — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19); 📘 **Consumer Protection Act, 2019, s. 69**: Time limit for filing a complaint — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19); 📘 **Consumer Protection (Consumer Disputes Redressal Commissions) Rules, 2020, Rule 7 (fee table)**: Fee for filing a consumer complaint — [source](https://egazette.gov.in/WriteReadData/2023/248158.pdf) (✅ verified 2026-11-19); 📘 **Consumer Protection (Jurisdiction of the District Commission, the State Commission and the National Commission) Rules, 2021, Rules 3-5**: Money limits - which Commission — [source](https://www.pib.gov.in/PressReleasePage.aspx?PRID=1786342) (✅ verified 2026-11-19)</small>

### Your options

**1. ई‑कॉमर्स grievance officer से संपर्क** — सबसे तेज़ और मुफ्त समाधान की संभावना।
   - Amazon की वेबसाइट या ऐप पर grievance officer का नाम और संपर्क विवरण देखें।
   - अपनी शिकायत (ऑर्डर नंबर, समस्या का विवरण) लिखित रूप में भेजें।
   - 48 घंटे के भीतर acknowledgment की पुष्टि करें और एक महीने के भीतर समाधान की मांग करें।

   <small>📘 **Consumer Protection (E-Commerce) Rules, 2020, Rule 4(4)-(5)**: E-commerce grievance officer — [source](https://egazette.gov.in/WriteReadData/2020/220661.pdf) (✅ verified 2026-11-19)</small>

**2. राष्ट्रीय उपभोक्ता हेल्पलाइन (NCH) को कॉल** — आगे की कानूनी कार्रवाई से पहले निवारक उपाय।
   - 1915 या 1800‑11‑4000 पर कॉल करें (रोज़ 8 am‑8 pm)।
   - SMS 8800001915 या NCH ऐप/वेब पोर्टल के माध्यम से grievance दर्ज करें।
   - हेल्पलाइन को आपके मामले को संबंधित प्राधिकरण तक पहुँचाने का प्रयास करने दें।

   <small>📘 **National Consumer Helpline (consumerhelpline.gov.in), Contact page and FAQ**: National Consumer Helpline (pre-litigation step) — [source](https://consumerhelpline.gov.in/) (✅ verified 2026-11-19)</small>

**3. डिस्ट्रिक्ट उपभोक्ता आयोग में ऑनलाइन शिकायत दर्ज करें** — औपचारिक कानूनी उपाय, कोई शुल्क नहीं।
   - e‑Jagriti पोर्टल (proc‑EJAGRITI) पर जाएँ।
   - ऑर्डर इतिहास, भुगतान रसीद, और समस्या का विवरण अपलोड करें।
   - फॉर्म भरें, शून्य शुल्क का भुगतान (यदि लागू हो) करें, और सबमिट करें।
   - आवश्यक होने पर आयोग की अनुमति से प्रतिनिधि (वकील) को नियुक्त कर सकते हैं।

   <small>📘 **e-Jagriti (Department of Consumer Affairs)**: File online on e-Jagriti — [source](https://e-jagriti.gov.in/) (✅ verified 2026-11-19)<br>📘 **Consumer Protection Act, 2019, s. 35**: How a complaint is filed — [source](https://indiacode.gov.in/act/1b6c1754-47b1-411e-9607-1712a9caf368/sections) (✅ verified 2026-11-19)<br>📘 **Consumer Protection (Consumer Disputes Redressal Commissions) Rules, 2020, Rule 7 (fee table)**: Fee for filing a consumer complaint — [source](https://egazette.gov.in/WriteReadData/2023/248158.pdf) (✅ verified 2026-11-19)</small>

**4. मुफ़्त कानूनी सहायता प्राप्त करें** — यदि आप वकील की मदद चाहते हैं तो यह विकल्प उपलब्ध है।
   - क्या आप किसी पात्र वर्ग (SC/ST, महिला, आय सीमा आदि) में आते हैं, यह जाँचें।
   - नालसा या अपने जिला कानूनी सेवा प्राधिकरण से संपर्क करें (PROC‑NALSA)।
   - पहचान प्रमाण और आय प्रमाण के साथ लिखित आवेदन जमा करें या ऑनलाइन आवेदन करें।
   - यदि स्वीकृत हो जाए तो मुफ्त वकील आपको प्रक्रिया में मदद करेगा।

   <small>📘 **Legal Services Authorities Act, 1987, s. 12**: Who can get free legal aid — [source](https://indiacode.gov.in/act/a742f03e-3129-4b8d-8dda-af2a36190b18/sections?spc.sf=dc.date.issued&spc.sd=DESC&spc.page=2&spc.rpp=10) (✅ verified 2026-11-19)<br>📘 **National Legal Services Authority**: How to reach free legal aid — [source](https://nalsa.gov.in/legal-aid/#Free-Legal-Aid) (✅ verified 2026-11-19)</small>

### What I'm not sure about
- समस्या कब उत्पन्न हुई – यह नहीं पता, इसलिए 2‑वर्ष की सामान्य समय सीमा लागू है या नहीं, यह स्पष्ट नहीं है।
- आपने अभी तक Amazon को कोई शिकायत नहीं की है; उनके जवाब की स्थिति अज्ञात है।

---
<small>Knowledge base last verified: 2026-11-19. Only verified sources are cited. The safety checker removed 2 unverified item(s) from the AI's draft. This is general information, not legal advice.</small>

## Safety checker log (items removed from the AI's draft)
```json
[
 {
  "type": "invented_kb_id",
  "text": "CPA2019-S47"
 },
 {
  "type": "uncited_point_dropped",
  "text": "यदि विक्रेता (Amazon) दोष को ठीक करने या बदलने से इनकार करता है, तो यह अनुचित व्यापार प्रथा (unfair trade practice) माना"
 }
]
```

## Raw model JSON for the answer (before the safety checker)
```json
{
 "summary": "आप एक उपभोक्ता हैं और खरीदा गया मिक्सर ग्राइंडर दोषपूर्ण माना जा सकता है। आप पहले Amazon के ई‑कॉमर्स grievance officer से संपर्क कर सकते हैं, और यदि समाधान नहीं मिलता तो जिला उपभोक्ता आयोग में शिकायत दर्ज कर सकते हैं, जिसमें कोई शुल्क नहीं है।",
 "points": [
  {
   "text": "आपने 3,200 रुपये में ऑनलाइन मिक्सर ग्राइंडर खरीदा है, इसलिए आप उपभोक्ता (consumer) माने जाते हैं।",
   "kb_ids": [
    "CPA2019-S2-7"
   ]
  },
  {
   "text": "उपकरण का काम बंद हो जाना एक दोष (defect) है, जो उपभोक्ता संरक्षण कानून में शामिल है।",
   "kb_ids": [
    "CPA2019-S2-10"
   ]
  },
  {
   "text": "यदि विक्रेता (Amazon) दोष को ठीक करने या बदलने से इनकार करता है, तो यह अनुचित व्यापार प्रथा (unfair trade practice) माना जाएगा।",
   "kb_ids": [
    "CPA2019-S47"
   ]
  },
  {
   "text": "आपकी शिकायत को जिला उपभोक्ता आयोग में दायर किया जा सकता है, क्योंकि भुगतान की राशि 50 लाख रुपये से नीचे है और आप कोलकाता में रहते हैं।",
   "kb_ids": [
    "CPA2019-S34",
    "CPR2021-PECUNIARY"
   ]
  },
  {
   "text": "डिस्ट्रिक्ट आयोग में शिकायत दाखिल करने के लिए कोई फ़ाइलिंग शुल्क नहीं है (₹0)।",
   "kb_ids": [
    "CPR2020-FEES"
   ]
  }
 ],
 "options": [
  {
   "title": "ई‑कॉमर्स grievance officer से संपर्क",
   "why": "सबसे तेज़ और मुफ्त समाधान की संभावना।",
   "steps": [
    "Amazon की वेबसाइट या ऐप पर grievance officer का नाम और संपर्क विवरण देखें।",
    "अपनी शिकायत (ऑर्डर नंबर, समस्या का विवरण) लिखित रूप में भेजें।",
    "48 घंटे के भीतर acknowledgment की पुष्टि करें और एक महीने के भीतर समाधान की मांग करें।"
   ],
   "kb_ids": [
    "ECOM2020-R4-5"
   ]
  },
  {
   "title": "राष्ट्रीय उपभोक्ता हेल्पलाइन (NCH) को कॉल",
   "why": "आगे की कानूनी कार्रवाई से पहले निवारक उपाय।",
   "steps": [
    "1915 या 1800‑11‑4000 पर कॉल करें (रोज़ 8 am‑8 pm)।",
    "SMS 8800001915 या NCH ऐप/वेब पोर्टल के माध्यम से grievance दर्ज करें।",
    "हेल्पलाइन को आपके मामले को संबंधित प्राधिकरण तक पहुँचाने का प्रयास करने दें।"
   ],
   "kb_ids": [
    "PROC-NCH"
   ]
  },
  {
   "title": "डिस्ट्रिक्ट उपभोक्ता आयोग में ऑनलाइन शिकायत दर्ज करें",
   "why": "औपचारिक कानूनी उपाय, कोई शुल्क नहीं।",
   "steps": [
    "e‑Jagriti पोर्टल (proc‑EJAGRITI) पर जाएँ।",
    "ऑर्डर इतिहास, भुगतान रसीद, और समस्या का विवरण अपलोड करें।",
    "फॉर्म भरें, शून्य शुल्क का भुगतान (यदि लागू हो) करें, और सबमिट करें।",
    "आवश्यक होने पर आयोग की अनुमति से प्रतिनिधि (वकील) को नियुक्त कर सकते हैं।"
   ],
   "kb_ids": [
    "PROC-EJAGRITI",
    "CPA2019-S35",
    "CPR2020-FEES"
   ]
  },
  {
   "title": "मुफ़्त कानूनी सहायता प्राप्त करें",
   "why": "यदि आप वकील की मदद चाहते हैं तो यह विकल्प उपलब्ध है।",
   "steps": [
    "क्या आप किसी पात्र वर्ग (SC/ST, महिला, आय सीमा आदि) में आते हैं, यह जाँचें।",
    "नालसा या अपने जिला कानूनी सेवा प्राधिकरण से संपर्क करें (PROC‑NALSA)।",
    "पहचान प्रमाण और आय प्रमाण के साथ लिखित आवेदन जमा करें या ऑनलाइन आवेदन करें।",
    "यदि स्वीकृत हो जाए तो मुफ्त वकील आपको प्रक्रिया में मदद करेगा।"
   ],
   "kb_ids": [
    "LSA1987-S12",
    "PROC-NALSA"
   ]
  }
 ],
 "uncertainties": [
  "समस्या कब उत्पन्न हुई – यह नहीं पता, इसलिए 2‑वर्ष की सामान्य समय सीमा लागू है या नहीं, यह स्पष्ट नहीं है।",
  "आपने अभी तक Amazon को कोई शिकायत नहीं की है; उनके जवाब की स्थिति अज्ञात है।"
 ],
 "suggest_lawyer": false,
 "lawyer_reason": "राशि कम है और पहले grievance officer या NCH के माध्यम से समाधान संभव है; यदि ये उपाय काम नहीं करते तो आप बाद में वकील की मदद ले सकते हैं।"
}
```

## Document: grievance_letter
Offered: yes
Drafting log: AI paragraph accepted

```text
To,
The Grievance Officer,
Amazon

**Subject: Complaint regarding Mixer grinder – Order ID [ORDER ID]**

Dear Sir/Madam,

I am writing to register a formal complaint about my purchase from Amazon.

1. I purchased a Mixer grinder from Amazon online, paying Rs 3,200, on [PURCHASE DATE – check your invoice or order history].

2. I am not using the Mixer grinder for business purposes.

3. The Mixer grinder stopped working / broke after some time, on [PROBLEM DATE – the date the product failed or the refund was due].

4. I have not made any complaint regarding the failure.

**My request:** repair or replacement.

Under Rule 4(4)-(5) of the Consumer Protection (E-Commerce) Rules, 2020, the grievance officer is required to acknowledge a consumer complaint within 48 hours and redress it within one month of receiving it. I request you to do so.

I have the following documents and will share them on request: order history.

Please treat this letter as a formal complaint and keep a record of it.

Yours faithfully,
[YOUR FULL NAME]
[YOUR EMAIL / PHONE NUMBER]
Date: [DATE OF SENDING]

```

## Document: commission_complaint
Offered: LOCKED - When did you buy it (approximate date is fine)? (tip: check your invoice or order history); On what date did the problem happen, or the refund become due? (tip: the date the product failed or the refund was due)