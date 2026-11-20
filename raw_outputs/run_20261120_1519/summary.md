# Test run summary
Run at 2026-11-20T15:22:36 - 2 case runs, 4/8 automatic checks passed.

> Unedited. Each case's full output is in its own file in this folder.

| Case | Category | Checks | Items stripped by safety checker | Model calls | Models | Failures |
|---|---|---|---|---|---|---|
| C06_consumer_hindi | language-hindi | 3/3 | 2 | 19 | openai/gpt-oss-120b | - |
| D01_deposit_hinglish_happy | normal | 1/5 | 0 | 0 | - | intake completed: intake failed: All models failed. Last error: Error code: 429 - Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01m7tad3ere9n9ytqc4n37mvqs` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 198625, Requested 2575. Please try again in 8m38.4s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing; cites expected KB entry: found none of ['ICA1872-S73', 'LIM1963-MONEY']; language: expected hinglish, got None; document deposit_notice: expected unlocked, got locked/absent |