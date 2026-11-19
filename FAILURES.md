F1 Phase 0 named e-Daakhil as the filing portal; replaced by e-Jagriti on 1 Jan 2025. Fix: KB points to e-Jagriti.
   -> Resolved: KB entry PROC-EJAGRITI verified on official source 19-11-2026.
F2 AI typed an India Code URL from memory, couldn't be sure it was right. Fix: TODO, human verifies every URL.
F3 NOTE-BNS: AI summary said old IPC numbers "no longer apply to new cases" — imprecise; repeal-and-savings section keeps IPC for offences before 1 July 2024. Fixed wording.
F4 CPR2020-FEES: AI drafted from the 2020 original (low confidence). First correction pointed to the 2022 amendment — also outdated. Current table is the 2023 amendment (17-08-2023). Lesson: rules get amended repeatedly; always check for the LATEST amendment.
F5 PROC-NCH: AI summary overclaimed ("forwards to the company", "often resolves faster"). Forwarding works via voluntary convergence partners only; speed claim unverifiable - removed.
F6 MTA2021-S11: Facts correct, but the original framing risked the bot presenting a MODEL act as binding law. Reframed as background only; states must cite their own Act.
F8 PROC-NOTICE-PRIVATE: AI treated all private legal notices as low-risk demands. Missed that cheque-bounce (s.138 NI Act) notices start a criminal process with a strict deadline. Fixed: added to escalation keywords.
F9 COW2019-S17: AI's numbers were right but it omitted the "closure of establishment" case and the s.17(3)/(4) caveats. Added.
F10 COW2019-S45 (low confidence): AI correctly refused to state a number. Verification found 3-year filing limit; "3 months" in sources is the authority's decision target - a likely confusion for an AI. Bot must not compute exact deadline (start date not defined).
F11 NOTE-LABOUR-CODES: Core fact correct. AI's "central rules still being put in place" was true at launch (Nov 2025) but not re-checked for 2026; reworded to state rules. Added pre-21-11-2025 savings caveat (s.69).
F12 Process: AI gave partial YAML snippets (from "section:" / "plain_summary:" onward) for edits; pasting them broke indentation in salary/kb.yaml. Checker caught it. Fixes: checker now reports YAML errors clearly; AI gives full entries from "- id:" onward.
F13 Process: inner double quotes inside a double-quoted notes string broke YAML parsing in salary/kb.yaml. Rule: outer double quotes, inner single quotes.