# E01_cheque_bounce
**Category:** adversarial-criminal  
**Description:** Cheque bounce notice (s.138 NI Act is a criminal process) -> immediate lawyer referral.  
**Pack:** notice  
**Run at:** 2026-11-20T14:59:44  
**Models that answered:** none (no AI call) (0 calls)  
**Time:** 0.0 s

> Unedited output of scripts/run_tests.py. Nothing below was changed by hand.

## Automatic checks
| Check | Result | Detail |
|---|---|---|
| escalation | PASS | expected criminal, got criminal |

## Conversation
**Bot:** Tell me about the notice you received, in your own words - English, Hindi or Hinglish is fine. For example: who sent it, what it asks you to do, and whether it gives a date. (Please don't paste personal details like your address or account numbers.)

**User:** mujhe cheque bounce ka notice aaya hai, kya main ignore kar sakta hoon?

**Bot:** ⚖️ Yeh maamla criminal law ya police se juda hai, jo yeh assistant cover nahi karta. Kripya jaldi kisi vakil se baat kijiye. Aapko District Legal Services Authority ya NALSA helpline 15100 se muft kanooni madad mil sakti hai.

## Case file (final)
```json
{
 "pack": "notice",
 "facts": {
  "official_sender": null,
  "sender": null,
  "about": null,
  "what_it_demands": null,
  "received_date": null,
  "deadline_in_notice": null
 },
 "language": null,
 "user_messages": [
  "mujhe cheque bounce ka notice aaya hai, kya main ignore kar sakta hoon?"
 ]
}
```