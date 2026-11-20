# N01_notice_private_loan
**Category:** normal  
**Description:** Lawyer's notice from a lending app demanding repayment within 15 days. Explain, don't stop.  
**Pack:** notice  
**Run at:** 2026-11-20T14:59:44  
**Models that answered:** openai/gpt-oss-120b (6 calls)  
**Time:** 41.7 s

> Unedited output of scripts/run_tests.py. Nothing below was changed by hand.

## Automatic checks
| Check | Result | Detail |
|---|---|---|
| escalation | PASS | expected none, got none |
| intake completed | **FAIL** | intake failed: All models failed. Last error: Error code: 429 - Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01m7tad3ere9n9ytqc4n37mvqs` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Used 6032, Requested 2044. Please try again in 570ms. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing |
| cites expected KB entry | **FAIL** | found none of ['PROC-NOTICE-PRIVATE'] |

## Conversation
**Bot:** Tell me about the notice you received, in your own words - English, Hindi or Hinglish is fine. For example: who sent it, what it asks you to do, and whether it gives a date. (Please don't paste personal details like your address or account numbers.)

**User:** mujhe ek loan app ke vakil ka legal notice aaya hai, 18000 rupaye 15 din mein bharne ko bol rahe hain, nahi to case karenge

**Bot:** मैं समझता हूँ कि आपको एक कानूनी नोटिस मिला है। क्या यह नोटिस अदालत, पुलिस, किसी ट्रिब्यूनल/आयोग, या सरकारी या टैक्स ऑफ़िस से आया है?

**User:** nahi, police se nahi, vakil ka notice hai

**Bot:** समझ गया, यह वकील का नोटिस है। आपको नोटिस किस तारीख को मिला?

**User:** 18 november 2026

**Bot:** आपने एक तिथि बताई है। क्या नोटिस में कोई समय-सीमा दी गई है? अगर हाँ, तो किस तारीख तक (या कितने दिन में)? (आपने बताया: 2026-12-03 - क्या यह सही है?)

**User:** 15 din mein, yaani 3 december 2026

## Case file (final)
```json
{
 "pack": "notice",
 "facts": {
  "official_sender": false,
  "sender": "loan app ke vakil",
  "about": "loan repayment",
  "what_it_demands": "pay Rs 18000",
  "received_date": "2026-11-18",
  "deadline_in_notice": null
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

**ERROR:** intake failed: All models failed. Last error: Error code: 429 - Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01m7tad3ere9n9ytqc4n37mvqs` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Used 6032, Requested 2044. Please try again in 570ms. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing