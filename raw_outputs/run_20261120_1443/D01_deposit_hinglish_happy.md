# D01_deposit_hinglish_happy
**Category:** normal  
**Description:** Rs 50,000 deposit, Rs 10,000 returned, landlord blames painting. Notice should be drafted.  
**Pack:** deposit  
**Run at:** 2026-11-20T14:57:41  
**Models that answered:** openai/gpt-oss-120b (16 calls)  
**Time:** 121.9 s

> Unedited output of scripts/run_tests.py. Nothing below was changed by hand.

## Automatic checks
| Check | Result | Detail |
|---|---|---|
| escalation | PASS | expected none, got none |
| intake completed | **FAIL** | intake failed: All models failed. Last error: Error code: 429 - Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01m7tad3ere9n9ytqc4n37mvqs` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Used 5706, Requested 2352. Please try again in 435ms. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing |
| cites expected KB entry | **FAIL** | found none of ['ICA1872-S73', 'LIM1963-MONEY'] |
| language | PASS | expected hinglish, got hinglish |
| document deposit_notice | **FAIL** | expected unlocked, got locked/absent |

## Conversation
**Bot:** Tell me what happened with your security deposit, in your own words - English, Hindi or Hinglish is fine. For example: how much deposit you paid, when you moved out, and what the landlord is saying.

**User:** maine pune mein flat chhoda 31 august 2026 ko, 50000 deposit diya tha, makaan maalik ne sirf 10000 lautaya, bolta hai painting ka paisa kaatega

**Bot:** Shukriya, maine note kar liya. Kya yeh ghar tha jismein aap rehte the (dukaan, office ya business ki jagah nahi)?

**User:** haan ghar tha, family ke saath rehte the

**Bot:** समझ गया, आप अपने परिवार के साथ घर में रहते थे। मकान मालिक ने अब तक डिपॉज़िट में से कितना वापस किया है? (कुछ नहीं तो 0 बोलिए।) (आपने बताया: 10000 - क्या यह सही है?)

**User:** 10000

**Bot:** धन्यवाद, मैंने नोट कर लिया। महीने का किराया कितना था?

**User:** 15000

**Bot:** मैं समझ गया। आपने किस तारीख को घर खाली करके चाबी वापस दी थी? (आपने बताया: 2026-08-31 - क्या यह सही है?)

**User:** 31 august 2026

**Bot:** समझ गया। क्या आपके पास लिखित किराया अनुबंध है? अगर हाँ, तो उसमें डिपॉज़िट वापस करने के बारे में क्या लिखा है?

**User:** 11 mahine ka agreement hai, usmein likha hai deposit refundable hai

**Bot:** Aapke agreement ke terms samajh aagaye. Kya aapke paas saboot hai ki aapne ghar theek haalat mein wapas kiya (photo, video, message ya handover note)?

**User:** flat chhodte waqt ki photos aur video hain

**Bot:** मैं समझता हूँ कि आपके पास फ्लैट छोड़ते समय की फोटो और वीडियो हैं। क्या आपने मकान मालिक से डिपॉज़िट माँगा है? अगर हाँ, तो कैसे और कब, और उन्होंने क्या कहा?

**User:** whatsapp pe 2 baar maanga, bolta hai dekhenge

**Bot:** मैं समझता हूँ कि आपने व्हाट्सएप पर कई बार माँगा और वह कहता है कि देखेंगे। आपके पास क्या सबूत है? (किराया अनुबंध, डिपॉज़िट की रसीद, बैंक/UPI ट्रांसफ़र, किराये की रसीद, चैट, फ़ोटो) (आपने बताया: photos, video, rent agreement, WhatsApp chat - क्या यह सही है?)

**User:** rent agreement, deposit ka UPI transfer, whatsapp chats, photos

**Bot:** Samajh gaya, aapke paas rent agreement, deposit ka UPI transfer, whatsapp chats, photos hain. Aapko poora deposit wapas chahiye, ya kisi katauti ke baad jo aapko theek lagti hai?

**User:** poora deposit wapas

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
  "handover_proof": "photos and video",
  "complaints_made": "whatsapp pe 2 baar maanga, bolta hai dekhenge",
  "evidence": [
   "rent agreement",
   "deposit UPI transfer",
   "whatsapp chats",
   "photos",
   "video"
  ],
  "desired_outcome": null,
  "user_city_state": "Pune, Maharashtra"
 },
 "language": "hinglish",
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
   "rent agreement",
   "WhatsApp chat"
  ]
 }
}
```

**ERROR:** intake failed: All models failed. Last error: Error code: 429 - Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01m7tad3ere9n9ytqc4n37mvqs` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Used 5706, Requested 2352. Please try again in 435ms. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing