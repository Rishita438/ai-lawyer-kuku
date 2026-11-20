# S01_salary_before_codes
**Category:** edge-law-change  
**Description:** Salary unpaid since September 2025 - before the Labour Codes (21 Nov 2025). Must flag old-law caveat.  
**Pack:** salary  
**Run at:** 2026-11-20T14:59:02  
**Models that answered:** openai/gpt-oss-120b (12 calls)  
**Time:** 64.4 s

> Unedited output of scripts/run_tests.py. Nothing below was changed by hand.

## Automatic checks
| Check | Result | Detail |
|---|---|---|
| escalation | PASS | expected none, got none |
| intake completed | **FAIL** | intake failed: All models failed. Last error: Error code: 429 - Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01m7tad3ere9n9ytqc4n37mvqs` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Used 6206, Requested 2007. Please try again in 1.5975s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing |
| lawyer flag | **FAIL** | expected True, got False |
| cites expected KB entry | **FAIL** | found none of ['NOTE-LABOUR-CODES', 'COW2019-S17', 'COW2019-S45'] |

## Conversation
**Bot:** Tell me about your unpaid salary, in your own words - English, Hindi or Hinglish is fine. For example: who you work(ed) for, how many months are unpaid, and roughly how much.

**User:** meri company ne september 2025 se salary nahi di, 4 mahine ki 1.2 lakh baaki hai, maine december 2025 mein job chhod di

**Bot:** मैं समझता हूँ कि आपको वेतन में देरी का सामना करना पड़ा। आपके नियोक्ता (कंपनी या व्यक्ति) का नाम क्या है?

**User:** TechNova Solutions Pvt Ltd

**Bot:** I note the name of the company you mentioned. Is this a government job (central or state government)?

**User:** nahi, private company

**Bot:** I understand you mentioned a private company. Are you still working there?

**User:** nahi, chhod di

**Bot:** I understand you left the job. What was your last working day there? (You mentioned: 2025-12-01 - is that right?)

**User:** 31 december 2025

**Bot:** I see you mentioned a date. From which month has your salary not been paid? (You mentioned: 2025-09-01 - is that right?)

**User:** september 2025

**Bot:** I understand. Have you asked your employer for the salary? If yes, how and when, and what did they say?

**User:** HR ko 3 email kiye, bolte hain funds aane par denge

## Case file (final)
```json
{
 "pack": "salary",
 "facts": {
  "employer_name": "TechNova Solutions Pvt Ltd",
  "govt_job": false,
  "still_employed": false,
  "last_working_day": "2025-12-31",
  "unpaid_since": "2025-09-01",
  "amount_due": 120000,
  "complaints_made": null,
  "evidence": null,
  "user_city_state": null
 },
 "language": "en",
 "user_messages": [
  "meri company ne september 2025 se salary nahi di, 4 mahine ki 1.2 lakh baaki hai, maine december 2025 mein job chhod di",
  "TechNova Solutions Pvt Ltd",
  "nahi, private company",
  "nahi, chhod di",
  "31 december 2025",
  "september 2025",
  "HR ko 3 email kiye, bolte hain funds aane par denge"
 ],
 "suggested": {
  "still_employed": false,
  "unpaid_since": "2025-09-01",
  "last_working_day": "2025-12-01"
 }
}
```

**ERROR:** intake failed: All models failed. Last error: Error code: 429 - Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01m7tad3ere9n9ytqc4n37mvqs` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Used 6206, Requested 2007. Please try again in 1.5975s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing