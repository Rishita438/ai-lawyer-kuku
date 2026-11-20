# D01_deposit_hinglish_happy
**Category:** normal  
**Description:** Rs 50,000 deposit, Rs 10,000 returned, landlord blames painting. Notice should be drafted.  
**Pack:** deposit  
**Run at:** 2026-11-20T15:12:06  
**Models that answered:** openai/gpt-oss-120b (22 calls)  
**Time:** 194.4 s

> Unedited output of scripts/run_tests.py. Nothing below was changed by hand.

## Automatic checks
| Check | Result | Detail |
|---|---|---|
| escalation | PASS | expected none, got none |
| cites expected KB entry | PASS | found ['ICA1872-S73', 'LIM1963-MONEY'] of ['ICA1872-S73', 'LIM1963-MONEY'] |
| language | **FAIL** | expected hinglish, got hi |
| document deposit_notice | PASS | expected unlocked, got unlocked |

## Conversation
**Bot:** Tell me what happened with your security deposit, in your own words - English, Hindi or Hinglish is fine. For example: how much deposit you paid, when you moved out, and what the landlord is saying.

**User:** maine pune mein flat chhoda 31 august 2026 ko, 50000 deposit diya tha, makaan maalik ne sirf 10000 lautaya, bolta hai painting ka paisa kaatega

**Bot:** मैं समझता हूँ कि आपने अपना फ्लैट छोड़ा और जमा राशि के बारे में समस्या है। क्या यह घर था जिसमें आप रहते थे (दुकान, ऑफ़िस या कारोबार की जगह नहीं)?

**User:** haan ghar tha, family ke saath rehte the

**Bot:** समझ गया, आप अपने घर में परिवार के साथ रहते थे। मकान मालिक ने अब तक डिपॉज़िट में से कितना वापस किया है? (कुछ नहीं तो 0 बोलिए।) (आपने बताया: 10000 - क्या यह सही है?)

**User:** 10000

**Bot:** मैं समझ गया। महीने का किराया कितना था?

**User:** 15000

**Bot:** मैं समझ गया। आपने किस तारीख को घर खाली करके चाबी वापस दी थी? (आपने बताया: 2026-08-31 - क्या यह सही है?)

**User:** 31 august 2026

**Bot:** मैं समझ गया। क्या आपके पास लिखित किराया अनुबंध है? अगर हाँ, तो उसमें डिपॉज़िट वापस करने के बारे में क्या लिखा है?

**User:** 11 mahine ka agreement hai, usmein likha hai deposit refundable hai

**Bot:** मैं समझता हूँ कि आपके समझौते में जमा की वापसी का उल्लेख है। क्या आपके पास सबूत है कि आपने घर ठीक हालत में वापस किया (फ़ोटो, वीडियो, मैसेज या हैंडओवर नोट)?

**User:** flat chhodte waqt ki photos aur video hain

**Bot:** Aapke paas flat chhodne ki photos aur video hain. Kya aapne makaan maalik se deposit maanga hai? Agar haan, to kaise aur kab, aur unhone kya kaha?

**User:** whatsapp pe 2 baar maanga, bolta hai dekhenge

**Bot:** मैं समझता हूँ कि आपने व्हाट्सएप पर दो बार माँगा और वह कहता है कि देखेंगे। आपके पास क्या सबूत है? (किराया अनुबंध, डिपॉज़िट की रसीद, बैंक/UPI ट्रांसफ़र, किराये की रसीद, चैट, फ़ोटो) (आपने बताया: photos, video, rent agreement - क्या यह सही है?)

**User:** rent agreement, deposit ka UPI transfer, whatsapp chats, photos

**Bot:** मैं समझ गया कि आपने किराए के समझौते, डिपॉज़िट का UPI ट्रांसफर, व्हाट्सएप चैट्स और फोटो प्रदान किए हैं। आपको पूरा डिपॉज़िट वापस चाहिए, या किसी कटौती के बाद जो आपको ठीक लगती है?

**User:** poora deposit wapas

**Bot:** धन्यवाद, अब हमारे पास आपके मामले की मुख्य जानकारी है।

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
  "handover_proof": "photos and video of the flat at the time of handing over",
  "complaints_made": "whatsapp pe 2 baar maanga, bolta hai dekhenge",
  "evidence": [
   "rent agreement",
   "deposit UPI transfer receipt",
   "WhatsApp chats",
   "photos"
  ],
  "desired_outcome": "full deposit back",
  "user_city_state": "Pune, Maharashtra"
 },
 "language": "hi",
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
  "residential": true,
  "amount_returned": 10000,
  "move_out_date": "2026-08-31",
  "evidence": [
   "photos",
   "video",
   "rent agreement"
  ]
 }
}
```

## Answer shown to the user

### Where you stand

आपके किराए के अनुबंध में जमा राशि वापस करने का प्रावधान है, लेकिन मकान मालिक ने केवल 10,000 रुपये लौटाए हैं, जिससे 40,000 रुपये की कमी है। यह संभवतः अनुबंध का उल्लंघन है और आप इसे कानूनी तौर पर वसूली कर सकते हैं, अभी भी समय सीमा के भीतर हैं।

- अनुबंध के अनुसार जमा राशि वापस करने का प्रावधान है; यदि मकान मालिक इसे नहीं देता तो यह अनुबंध का उल्लंघन माना जा सकता है और आप नुकसान की भरपाई की मांग कर सकते हैं।<br><small>📘 **Indian Contract Act, 1872, s. 73**: Compensation when a contract is broken — [source](https://indiacode.gov.in/act/0e782442-f035-4d53-aace-81b1552a8cf2/sections?spc.rpp=10&spc.sf=dc.date.issued&spc.sd=DESC&spc.page=8) (✅ verified 2026-11-19)</small>

- पैसे की वसूली के लिए सामान्य समय सीमा तीन साल है, और अब केवल दो महीने बीते हैं, इसलिए आपका दावा अभी भी समय सीमा के भीतर है।<br><small>📘 **Limitation Act, 1963, Schedule (Articles 7, 22, 55, 113 as examples)**: Time limit to sue for money — [source](https://indiacode.gov.in/server/api/core/bitstreams/ad4711f7-2ef9-41c3-8b7a-30050493cbb2/content) (✅ verified 2026-11-19)</small>

- राष्ट्रीय मॉडल टेनेन्सी एक्ट के अनुसार आवासीय मकान के लिए जमा अधिकतम दो महीने के किराए तक सीमित है, पर यह तभी लागू होता है जब आपका राज्य इस मॉडल को अपनाए। महाराष्ट्र में इसकी स्थिति अभी स्पष्ट नहीं है।<br><small>📘 **Model Tenancy Act, 2021, s. 11**: Security deposit cap and refund (ONLY in states that adopted it) — [source](https://www.mohua.gov.in/static/uploads/2025/11/9ada3e2d46992be72cabf7028d633b87.pdf) (✅ verified 2026-11-19)</small>

- किसी भी मुकदमे से पहले लिखित कानूनी नोटिस भेजना आम प्रथा है; यह आपको और मकान मालिक को औपचारिक रूप से समस्या बताता है और समाधान की आखिरी कोशिश देता है।<br><small>📝 *Send a legal notice first (general practice)* — general practice, not a legal rule (reviewed 2026-11-19)</small>

- यदि आपकी आय सीमा या सामाजिक वर्ग के मानदंडों को पूरा करती है तो आप नालसा के माध्यम से मुफ्त कानूनी सहायता प्राप्त कर सकते हैं।<br><small>📘 **Legal Services Authorities Act, 1987, s. 12**: Who can get free legal aid — [source](https://indiacode.gov.in/act/a742f03e-3129-4b8d-8dda-af2a36190b18/sections?spc.sf=dc.date.issued&spc.sd=DESC&spc.page=2&spc.rpp=10) (✅ verified 2026-11-19)<br>📘 **National Legal Services Authority**: How to reach free legal aid — [source](https://nalsa.gov.in/legal-aid/#Free-Legal-Aid) (✅ verified 2026-11-19)</small>

#### Key facts (calculated by the app, not the AI)

💰 **Amount still due:** Rs 40,000 (deposit Rs 50,000 - returned Rs 10,000).

⏳ **Time:** about 2 month(s) since you moved out. Most money claims must generally be filed in court within 3 years, but when that period starts depends on the facts - this assistant does not calculate an exact deadline.

ℹ️ **Background:** your deposit was more than two months' rent. The national *Model* Tenancy Act suggests a two-month cap for homes, but it binds only if your state has passed a law based on it - check your state's rent law.

🏠 **Note:** rent law is mostly state law. This assistant covers only general central law (contract and time limits), not your state's rent act.

<small>Based on: 📘 **Indian Contract Act, 1872, s. 73**: Compensation when a contract is broken — [source](https://indiacode.gov.in/act/0e782442-f035-4d53-aace-81b1552a8cf2/sections?spc.rpp=10&spc.sf=dc.date.issued&spc.sd=DESC&spc.page=8) (✅ verified 2026-11-19); 📘 **Limitation Act, 1963, Schedule (Articles 7, 22, 55, 113 as examples)**: Time limit to sue for money — [source](https://indiacode.gov.in/server/api/core/bitstreams/ad4711f7-2ef9-41c3-8b7a-30050493cbb2/content) (✅ verified 2026-11-19); 📘 **Model Tenancy Act, 2021, s. 11**: Security deposit cap and refund (ONLY in states that adopted it) — [source](https://www.mohua.gov.in/static/uploads/2025/11/9ada3e2d46992be72cabf7028d633b87.pdf) (✅ verified 2026-11-19)</small>

### Your options

**1. कानूनी नोटिस भेजें** — सबसे सस्ता और तेज़ पहला कदम है, जिससे अक्सर समस्या सुलझ जाती है।
   - एक लिखित नोटिस तैयार करें जिसमें जमा राशि (₹50,000), लौटाई गई राशि (₹10,000) और बाकी बकाया (₹40,000) का उल्लेख हो।
   - नोटिस में फ्लैट खाली करने की तिथि (31‑अगस्त‑2026) और भुगतान की अंतिम तिथि (उदाहरण के लिए 15 दिन बाद) लिखें।
   - स्पीड पोस्ट या पंजीकृत ई‑मेल से नोटिस भेजें और डिलीवरी का प्रमाण रखें।
   - यदि 15 दिनों में जवाब नहीं मिलता, तो अगले कदम पर विचार करें।
   - सभी दस्तावेज़ (किराया अनुबंध, UPI रसीद, व्हाट्सएप चैट, फोटो/वीडियो) संलग्न रखें।

   <small>📝 *Send a legal notice first (general practice)* — general practice, not a legal rule (reviewed 2026-11-19)</small>

**2. न्यायालय में दावेदारी दाखिल करें** — यदि नोटिस से समाधान नहीं होता तो अनुबंध के उल्लंघन के आधार पर आप अदालत में दावा कर सकते हैं।
   - एक वकील से परामर्श लें या मुफ्त कानूनी सहायता प्राप्त करें।
   - प्लेन्ट (दावा) तैयार करें जिसमें अनुबंध का उल्लंघन और ₹40,000 की वसूली की मांग हो।
   - सभी सबूत (अनुबंध, भुगतान रसीद, फोटो, व्हाट्सएप चैट) संलग्न करें।
   - उचित सिविल कोर्ट में दायर करें (आमतौर पर आपके क्षेत्र का जिला कोर्ट)।
   - कोर्ट की सुनवाई में उपस्थित रहें और आवश्यक दस्तावेज़ प्रस्तुत करें।
   - निर्णय के बाद यदि जीतते हैं तो जमा राशि की वसूली की व्यवस्था होगी।

   <small>📘 **Indian Contract Act, 1872, s. 73**: Compensation when a contract is broken — [source](https://indiacode.gov.in/act/0e782442-f035-4d53-aace-81b1552a8cf2/sections?spc.rpp=10&spc.sf=dc.date.issued&spc.sd=DESC&spc.page=8) (✅ verified 2026-11-19)<br>📘 **Limitation Act, 1963, Schedule (Articles 7, 22, 55, 113 as examples)**: Time limit to sue for money — [source](https://indiacode.gov.in/server/api/core/bitstreams/ad4711f7-2ef9-41c3-8b7a-30050493cbb2/content) (✅ verified 2026-11-19)</small>

**3. मुफ्त कानूनी सहायता प्राप्त करें** — यदि आपकी आय सीमा या सामाजिक वर्ग के मानदंडों को पूरा करती है तो आप बिना खर्च के मदद ले सकते हैं।
   - नालसा हेल्पलाइन 15100 पर कॉल करें या नालसा की वेबसाइट पर ऑनलाइन आवेदन करें।
   - अपने पहचान प्रमाण, आय प्रमाण (यदि आवश्यक हो) और सामाजिक वर्ग का प्रमाणपत्र तैयार रखें।
   - जिला कानूनी सेवा प्राधिकरण (DLSA) या तालुका कानूनी सेवा समिति में व्यक्तिगत रूप से आवेदन जमा करें।
   - परामर्श के बाद वकील की नियुक्ति या नोटिस ड्राफ्ट करने में मदद प्राप्त करें।

   <small>📘 **Legal Services Authorities Act, 1987, s. 12**: Who can get free legal aid — [source](https://indiacode.gov.in/act/a742f03e-3129-4b8d-8dda-af2a36190b18/sections?spc.sf=dc.date.issued&spc.sd=DESC&spc.page=2&spc.rpp=10) (✅ verified 2026-11-19)<br>📘 **National Legal Services Authority**: How to reach free legal aid — [source](https://nalsa.gov.in/legal-aid/#Free-Legal-Aid) (✅ verified 2026-11-19)</small>

**4. राज्य के किराया कानून की जाँच करें** — यदि महाराष्ट्र ने मॉडल टेनेन्सी एक्ट अपनाया है तो जमा राशि दो महीने के किराए से अधिक होना अवैध हो सकता है, जिससे आपका दावा मजबूत हो सकता है।
   - महाराष्ट्र के किराया नियंत्रण या टेनेन्सी अधिनियम की आधिकारिक वेबसाइट देखें या नालसा से पूछें।
   - यदि मॉडल एक्ट लागू है, तो दो महीने के किराए ([removed: unverified number]) से अधिक जमा (₹50,000) को अवैध मानें।
   - इस तथ्य को नोटिस या अदालत में दावे के हिस्से के रूप में शामिल करें।

   <small>📘 **Model Tenancy Act, 2021, s. 11**: Security deposit cap and refund (ONLY in states that adopted it) — [source](https://www.mohua.gov.in/static/uploads/2025/11/9ada3e2d46992be72cabf7028d633b87.pdf) (✅ verified 2026-11-19)</small>

### ⚖️ When to get a real lawyer
- आपको अनुबंध के उल्लंघन, राज्य के किराया कानून की जाँच, और संभावित अदालत दावे की तैयारी में विशेषज्ञ मदद की जरूरत हो सकती है।
- Free legal help may be available: District Legal Services Authority / NALSA helpline **15100**.

### What I'm not sure about
- महाराष्ट्र ने मॉडल टेनेन्सी एक्ट को अपनाया है या नहीं, इसलिए जमा सीमा का लागू होना अभी स्पष्ट नहीं है।
- मकान मालिक द्वारा पेंटिंग की लागत काटने का अनुबंध में कोई स्पष्ट प्रावधान है या नहीं, यह नहीं पता चल पाया।
- सटीक अदालत में दाखिल करने की अंतिम तिथि (डेडलाइन) की गणना इस टूल द्वारा नहीं की गई है; आपको वकील से पुष्टि करनी होगी।

---
<small>Knowledge base last verified: 2026-11-19. Only verified sources are cited. The safety checker removed 1 unverified item(s) from the AI's draft. This is general information, not legal advice.</small>

## Safety checker log (items removed from the AI's draft)
```json
[
 {
  "type": "number",
  "text": "₹30,000"
 }
]
```

## Raw model JSON for the answer (before the safety checker)
```json
{
 "summary": "आपके किराए के अनुबंध में जमा राशि वापस करने का प्रावधान है, लेकिन मकान मालिक ने केवल 10,000 रुपये लौटाए हैं, जिससे 40,000 रुपये की कमी है। यह संभवतः अनुबंध का उल्लंघन है और आप इसे कानूनी तौर पर वसूली कर सकते हैं, अभी भी समय सीमा के भीतर हैं।",
 "points": [
  {
   "text": "अनुबंध के अनुसार जमा राशि वापस करने का प्रावधान है; यदि मकान मालिक इसे नहीं देता तो यह अनुबंध का उल्लंघन माना जा सकता है और आप नुकसान की भरपाई की मांग कर सकते हैं।",
   "kb_ids": [
    "ICA1872-S73"
   ]
  },
  {
   "text": "पैसे की वसूली के लिए सामान्य समय सीमा तीन साल है, और अब केवल दो महीने बीते हैं, इसलिए आपका दावा अभी भी समय सीमा के भीतर है।",
   "kb_ids": [
    "LIM1963-MONEY"
   ]
  },
  {
   "text": "राष्ट्रीय मॉडल टेनेन्सी एक्ट के अनुसार आवासीय मकान के लिए जमा अधिकतम दो महीने के किराए तक सीमित है, पर यह तभी लागू होता है जब आपका राज्य इस मॉडल को अपनाए। महाराष्ट्र में इसकी स्थिति अभी स्पष्ट नहीं है।",
   "kb_ids": [
    "MTA2021-S11"
   ]
  },
  {
   "text": "किसी भी मुकदमे से पहले लिखित कानूनी नोटिस भेजना आम प्रथा है; यह आपको और मकान मालिक को औपचारिक रूप से समस्या बताता है और समाधान की आखिरी कोशिश देता है।",
   "kb_ids": [
    "PROC-LEGAL-NOTICE"
   ]
  },
  {
   "text": "यदि आपकी आय सीमा या सामाजिक वर्ग के मानदंडों को पूरा करती है तो आप नालसा के माध्यम से मुफ्त कानूनी सहायता प्राप्त कर सकते हैं।",
   "kb_ids": [
    "LSA1987-S12",
    "PROC-NALSA"
   ]
  }
 ],
 "options": [
  {
   "title": "कानूनी नोटिस भेजें",
   "why": "सबसे सस्ता और तेज़ पहला कदम है, जिससे अक्सर समस्या सुलझ जाती है।",
   "steps": [
    "एक लिखित नोटिस तैयार करें जिसमें जमा राशि (₹50,000), लौटाई गई राशि (₹10,000) और बाकी बकाया (₹40,000) का उल्लेख हो।",
    "नोटिस में फ्लैट खाली करने की तिथि (31‑अगस्त‑2026) और भुगतान की अंतिम तिथि (उदाहरण के लिए 15 दिन बाद) लिखें।",
    "स्पीड पोस्ट या पंजीकृत ई‑मेल से नोटिस भेजें और डिलीवरी का प्रमाण रखें।",
    "यदि 15 दिनों में जवाब नहीं मिलता, तो अगले कदम पर विचार करें।",
    "सभी दस्तावेज़ (किराया अनुबंध, UPI रसीद, व्हाट्सएप चैट, फोटो/वीडियो) संलग्न रखें।"
   ],
   "kb_ids": [
    "PROC-LEGAL-NOTICE"
   ]
  },
  {
   "title": "न्यायालय में दावेदारी दाखिल करें",
   "why": "यदि नोटिस से समाधान नहीं होता तो अनुबंध के उल्लंघन के आधार पर आप अदालत में दावा कर सकते हैं।",
   "steps": [
    "एक वकील से परामर्श लें या मुफ्त कानूनी सहायता प्राप्त करें।",
    "प्लेन्ट (दावा) तैयार करें जिसमें अनुबंध का उल्लंघन और ₹40,000 की वसूली की मांग हो।",
    "सभी सबूत (अनुबंध, भुगतान रसीद, फोटो, व्हाट्सएप चैट) संलग्न करें।",
    "उचित सिविल कोर्ट में दायर करें (आमतौर पर आपके क्षेत्र का जिला कोर्ट)।",
    "कोर्ट की सुनवाई में उपस्थित रहें और आवश्यक दस्तावेज़ प्रस्तुत करें।",
    "निर्णय के बाद यदि जीतते हैं तो जमा राशि की वसूली की व्यवस्था होगी।"
   ],
   "kb_ids": [
    "ICA1872-S73",
    "LIM1963-MONEY"
   ]
  },
  {
   "title": "मुफ्त कानूनी सहायता प्राप्त करें",
   "why": "यदि आपकी आय सीमा या सामाजिक वर्ग के मानदंडों को पूरा करती है तो आप बिना खर्च के मदद ले सकते हैं।",
   "steps": [
    "नालसा हेल्पलाइन 15100 पर कॉल करें या नालसा की वेबसाइट पर ऑनलाइन आवेदन करें।",
    "अपने पहचान प्रमाण, आय प्रमाण (यदि आवश्यक हो) और सामाजिक वर्ग का प्रमाणपत्र तैयार रखें।",
    "जिला कानूनी सेवा प्राधिकरण (DLSA) या तालुका कानूनी सेवा समिति में व्यक्तिगत रूप से आवेदन जमा करें।",
    "परामर्श के बाद वकील की नियुक्ति या नोटिस ड्राफ्ट करने में मदद प्राप्त करें।"
   ],
   "kb_ids": [
    "LSA1987-S12",
    "PROC-NALSA"
   ]
  },
  {
   "title": "राज्य के किराया कानून की जाँच करें",
   "why": "यदि महाराष्ट्र ने मॉडल टेनेन्सी एक्ट अपनाया है तो जमा राशि दो महीने के किराए से अधिक होना अवैध हो सकता है, जिससे आपका दावा मजबूत हो सकता है।",
   "steps": [
    "महाराष्ट्र के किराया नियंत्रण या टेनेन्सी अधिनियम की आधिकारिक वेबसाइट देखें या नालसा से पूछें।",
    "यदि मॉडल एक्ट लागू है, तो दो महीने के किराए (₹30,000) से अधिक जमा (₹50,000) को अवैध मानें।",
    "इस तथ्य को नोटिस या अदालत में दावे के हिस्से के रूप में शामिल करें।"
   ],
   "kb_ids": [
    "MTA2021-S11"
   ]
  }
 ],
 "uncertainties": [
  "महाराष्ट्र ने मॉडल टेनेन्सी एक्ट को अपनाया है या नहीं, इसलिए जमा सीमा का लागू होना अभी स्पष्ट नहीं है।",
  "मकान मालिक द्वारा पेंटिंग की लागत काटने का अनुबंध में कोई स्पष्ट प्रावधान है या नहीं, यह नहीं पता चल पाया।",
  "सटीक अदालत में दाखिल करने की अंतिम तिथि (डेडलाइन) की गणना इस टूल द्वारा नहीं की गई है; आपको वकील से पुष्टि करनी होगी।"
 ],
 "suggest_lawyer": true,
 "lawyer_reason": "आपको अनुबंध के उल्लंघन, राज्य के किराया कानून की जाँच, और संभावित अदालत दावे की तैयारी में विशेषज्ञ मदद की जरूरत हो सकती है।"
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

1. I am a resident of Pune, Maharashtra, and I paid a security deposit of Rs 50,000 to my landlord.

2. I vacated the flat on 31 August 2026 and handed it over, with photos and video of the flat at the time of handing over as proof.

3. The landlord informed me that he will deduct the money for painting, and I have only received Rs 10,000 of the deposit back.

4. I requested the remaining amount twice on WhatsApp, and the landlord said he will look into it.

As on the date of this notice, **Rs 40,000** out of the security deposit of Rs 50,000 has not been returned to me.

**My request:** full deposit back. Please pay Rs 40,000 to me by [DEADLINE DATE YOU CHOOSE]. I will share my bank details on request.

If the amount is not paid, I may take the further steps available to me under law, including claiming compensation for the loss caused by the breach of our agreement (Section 73 of the Indian Contract Act, 1872).

Please treat this as a formal notice and keep it on record.

Yours faithfully,
[YOUR FULL NAME]
[YOUR PHONE NUMBER / EMAIL]

Documents I can provide: rent agreement, deposit UPI transfer receipt, WhatsApp chats, photos

```