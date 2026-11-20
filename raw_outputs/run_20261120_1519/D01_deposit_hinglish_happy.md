# D01_deposit_hinglish_happy
**Category:** normal  
**Description:** Rs 50,000 deposit, Rs 10,000 returned, landlord blames painting. Notice should be drafted.  
**Pack:** deposit  
**Run at:** 2026-11-20T15:22:36  
**Models that answered:** none (no AI call) (0 calls)  
**Time:** 0.1 s

> Unedited output of scripts/run_tests.py. Nothing below was changed by hand.

## Automatic checks
| Check | Result | Detail |
|---|---|---|
| escalation | PASS | expected none, got none |
| intake completed | **FAIL** | intake failed: All models failed. Last error: Error code: 429 - Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01m7tad3ere9n9ytqc4n37mvqs` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 198625, Requested 2575. Please try again in 8m38.4s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing |
| cites expected KB entry | **FAIL** | found none of ['ICA1872-S73', 'LIM1963-MONEY'] |
| language | **FAIL** | expected hinglish, got None |
| document deposit_notice | **FAIL** | expected unlocked, got locked/absent |

## Conversation
**Bot:** Tell me what happened with your security deposit, in your own words - English, Hindi or Hinglish is fine. For example: how much deposit you paid, when you moved out, and what the landlord is saying.

**User:** maine pune mein flat chhoda 31 august 2026 ko, 50000 deposit diya tha, makaan maalik ne sirf 10000 lautaya, bolta hai painting ka paisa kaatega

## Case file (final)
```json
{
 "pack": "deposit",
 "facts": {
  "residential": null,
  "deposit_amount": null,
  "amount_returned": null,
  "monthly_rent": null,
  "move_out_date": null,
  "agreement": null,
  "landlord_reason": null,
  "handover_proof": null,
  "complaints_made": null,
  "evidence": null,
  "desired_outcome": null,
  "user_city_state": null
 },
 "language": null,
 "user_messages": [
  "maine pune mein flat chhoda 31 august 2026 ko, 50000 deposit diya tha, makaan maalik ne sirf 10000 lautaya, bolta hai painting ka paisa kaatega"
 ]
}
```

**ERROR:** intake failed: All models failed. Last error: Error code: 429 - Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01m7tad3ere9n9ytqc4n37mvqs` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 198625, Requested 2575. Please try again in 8m38.4s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing