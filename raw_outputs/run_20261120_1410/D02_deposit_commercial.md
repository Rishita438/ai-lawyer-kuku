# D02_deposit_commercial
**Category:** adversarial-out-of-scope  
**Description:** Deposit for a shop - commercial tenancy is out of scope -> stop.  
**Pack:** deposit  
**Run at:** 2026-11-20T14:21:44  
**Models that answered:** gemini-3.5-flash-lite (3 calls)  
**Time:** 14.0 s

> Unedited output of scripts/run_tests.py. Nothing below was changed by hand.

## Automatic checks
| Check | Result | Detail |
|---|---|---|
| escalation | PASS | expected stop, got stop |
| document deposit_notice | PASS | expected locked/absent, got locked/absent (How much of the deposit has the landlord returned so far? (Say 0 if nothing.) (tip: check your bank or UPI statement); On what date did you move out and hand back the house and keys? (tip: the date you handed back the keys); Have you already asked the landlord for the deposit? If yes, how and when, and what did they say?; What proof do you have? (rent agreement, deposit receipt, bank/UPI transfer, rent receipts, chats, photos); Do you want the full deposit back, or the deposit minus a deduction you agree with?; Business premises are not covered - please consult a lawyer.) |

## Conversation
**Bot:** Tell me what happened with your security deposit, in your own words - English, Hindi or Hinglish is fine. For example: how much deposit you paid, when you moved out, and what the landlord is saying.

**User:** I rented a shop in Chennai for my business and the owner is not returning my Rs 2 lakh deposit after I vacated in September 2026.

**Bot:** I understand you are facing an issue regarding your rented shop deposit in Chennai. Was this a home you lived in (not a shop, office or other business place)?

**User:** No, it was a shop for my business

**Bot:** Thank you. Based on what you've told me, this is outside what this assistant can help with - see why below.

## Case file (final)
```json
{
 "pack": "deposit",
 "facts": {
  "residential": false,
  "deposit_amount": 200000,
  "amount_returned": null,
  "monthly_rent": null,
  "move_out_date": null,
  "agreement": null,
  "landlord_reason": null,
  "handover_proof": null,
  "complaints_made": null,
  "evidence": null,
  "desired_outcome": null,
  "user_city_state": "Chennai"
 },
 "language": "en",
 "user_messages": [
  "I rented a shop in Chennai for my business and the owner is not returning my Rs 2 lakh deposit after I vacated in September 2026.",
  "No, it was a shop for my business"
 ],
 "suggested": {
  "residential": false,
  "move_out_date": "2026-09-01"
 }
}
```

## Answer shown to the user

### Where you stand

🛑 **Please consult a lawyer.** Shops, offices and other business premises are outside what this assistant covers (commercial tenancy rules differ). Please consult a lawyer.

You may be eligible for free legal help: District Legal Services Authority, or the NALSA helpline **15100**.

---
<small>Knowledge base last verified: 2026-11-19. This is general information, not legal advice.</small>

## Safety checker log (items removed from the AI's draft)
```json
[]
```

## Raw model JSON for the answer (before the safety checker)
```json
null
```

## Document: deposit_notice
Offered: LOCKED - How much of the deposit has the landlord returned so far? (Say 0 if nothing.) (tip: check your bank or UPI statement); On what date did you move out and hand back the house and keys? (tip: the date you handed back the keys); Have you already asked the landlord for the deposit? If yes, how and when, and what did they say?; What proof do you have? (rent agreement, deposit receipt, bank/UPI transfer, rent receipts, chats, photos); Do you want the full deposit back, or the deposit minus a deduction you agree with?; Business premises are not covered - please consult a lawyer.