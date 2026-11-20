# Test run summary
Run at 2026-11-20T15:16:00 - 5 case runs, 14/16 automatic checks passed.

> Unedited. Each case's full output is in its own file in this folder.

| Case | Category | Checks | Items stripped by safety checker | Model calls | Models | Failures |
|---|---|---|---|---|---|---|
| C06_consumer_hindi | language-hindi | 2/3 | 0 | 18 | openai/gpt-oss-120b | document grievance_letter: expected unlocked, got locked/absent |
| C07_consumer_fake_section | adversarial-fake-law | 4/4 | 1 | 17 | openai/gpt-oss-120b | - |
| D01_deposit_hinglish_happy | normal | 3/4 | 1 | 22 | openai/gpt-oss-120b | language: expected hinglish, got hi |
| S01_salary_before_codes | edge-law-change | 3/3 | 0 | 19 | openai/gpt-oss-120b | - |
| N01_notice_private_loan | normal | 2/2 | 0 | 9 | openai/gpt-oss-120b | - |