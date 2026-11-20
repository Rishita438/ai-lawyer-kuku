# Nyaya Saathi: an honest AI legal helper for everyday problems in India

An assistant that helps ordinary people in India understand **where they stand** on a common legal
problem, **what they can do next**, and **when they need a real lawyer**, in English, Hindi or Hinglish.

**Live demo:** `<STREAMLIT LINK>` · **Kuku AI Generalist Assignment, Problem 2 ("Build an AI Lawyer")**

> ⚠️ This is general information from a small, human-verified knowledge base, not legal advice.
> It is built to say "I don't know" and "see a lawyer" rather than guess.

---

## What it covers

| Problem | Depth | What you get |
|---|---|---|
| **Consumer refund / defective product** (online or shop) | Full | Intake → where you stand (time limit, which Commission, fee) → options → **grievance letter** + **District Commission complaint draft** |
| **Security deposit not returned** (rented home) | Full | Intake → amount due, time elapsed, state-law caveat → **notice to the landlord** |
| **Unpaid salary** (private job) | Basics | Intake → where you stand, incl. the Nov-2025 Labour Codes change. No documents yet |
| **"I got a legal notice"** | Basics | Who sent it, deadline countdown, court/police/govt → lawyer. No documents yet |

**Not covered (the app refers you to a lawyer or free legal aid):** anything criminal or police-related,
cheque bounce, court summons, family law, property, government jobs, commercial tenancies, safety
situations (directs to 112), and claims above Rs 10 lakh (flagged for a lawyer).

---

## How it works: the model does language, code does law

```
user message ──► keyword escalation (code) ──► intake: model extracts facts, code decides the next question
                                                      │
                                     case file (shown live to the user; nothing enters it unconfirmed)
                                                      │
           calculators (code): deadlines, which forum, fees, amounts  ──►  case escalation rules (code)
                                                      │
           model explains, citing knowledge-base IDs ONLY  ──►  validator (code)  ──►  citations rendered from KB (code)
                                                      │
           documents: code fills a template; model writes only the facts paragraph, checked by code
```

| Done by the model (Gemini, Groq fallback) | Done by plain code |
|---|---|
| Understanding messy Hinglish/Hindi/English stories | Which question to ask next; when intake is complete |
| Extracting facts | Merging facts safely (no invented fields, no overwriting answers) |
| Explaining the legal position in plain language | Deadlines, forum, fees, amounts (from verified tables) |
| Writing the "facts" paragraph of a document | Every legal citation, every document structure |
| | Every "see a lawyer" rule; the model can add one, never remove one |

**Adding a problem type = adding a folder.** Each `packs/<problem>/` holds `kb.yaml` (verified law),
`intake.yaml` (questions in 3 languages), `calculators.py` (deadlines, lawyer triggers) and optionally
`drafts.yaml` + `templates/`. The shared engine in `app/` has no problem-specific logic. The deposit,
salary and notice packs were added without changing it.

---

## How hallucination is controlled

1. **A small, human-verified knowledge base.** 26 entries: **23 verified against primary sources**
   (India Code, Gazette of India, PIB, official portals), **3 marked "reviewed"** (general practice, not
   law, shown as such). Every entry records its source URL, who verified it and when. The app shows
   *"Knowledge base last verified: <date>"* on every answer. No case law in v1.
2. **The model never sees an act name or a section number.** It gets each entry as `id + plain summary`,
   so all it can cite is an ID like `CPA2019-S69`; code then prints *"Consumer Protection Act, 2019, s. 69 ✅ verified"*.
3. **A validator checks every answer** (`app/validator.py`): drops invented IDs and any legal point
   without a valid citation; strips typed sections, act names, IPC/BNS, case names and law reports;
   strips numbers (days, rupees, years) not found in the KB, the calculators or the user's own facts;
   strips promised outcomes ("you will win", "pakka milega", "guaranteed"). Every removal is logged and
   shown to the user (🛡️ Safety checker).
4. **Deadlines, fees and forums are computed by code**, never by the model. Where the KB doesn't verify
   a start date (deposits, wage claims), code **refuses to compute a deadline** and says so.
5. **Documents never invent facts.** Personal details (names, addresses, phone, order IDs) are never
   asked for or sent to the AI; they're `[PLACEHOLDERS]`. The AI's facts paragraph is rejected if it
   contains any number or date not in the case file, any legal reference, or untranslated Hinglish.
   A formal complaint is locked if a key fact is unknown, the time limit may have passed, or it's out of scope.
6. **The law changes, and the app says so:** IPC → BNS (July 2024), Labour Codes (Nov 2025), e-Daakhil →
   e-Jagriti (Jan 2025), consumer fee table amended twice (2022, 2023).

---

## Testing: real runs, unedited outputs, honest failures

- **Offline checks** (no API key): `py scripts/run_all_checks.py`. The KB checker plus
  `<N>` tests covering calculators, escalation, the validator against a deliberately bad model answer,
  drafting and all 4 packs.
- **Real-model test suite:** `py scripts/run_tests.py`. **16 fictional cases** (`tests/cases.yaml`):
  normal, Hindi/Hinglish, and adversarial (a fake "Section 420B", "guarantee I'll win", time-barred,
  business purchase, shop deposit, cheque bounce, court summons, divorce, a safety threat).
  Every run saves **unedited** transcripts, answers, documents, validator logs and raw model JSON to
  `raw_outputs/run_<date>/`.

| Run | Result |
|---|---|
| First full run (`raw_outputs/run_20261120_1350`) | Crashed at case 11/16 (F38); D02 failed (F39). 10/11 completed cases passed all checks |
| Second full run (`raw_outputs/<RUN FOLDER>`) | `<X/Y>` automatic checks passed. `<NOTES>` |

**`FAILURES.md` logs `<NN>` real failures** found while building, each with its cause and fix. Examples:
the model cited a real-but-wrong section (`CPA2019-S47` for `S2-47`, caught by the validator); the model
overwrote a stated purchase date with the problem date; AI-suggested model names and a government
portal had been shut down or replaced; the consumer fee table had been amended twice since the AI's knowledge.
`DECISIONS.md` records each design choice and the alternatives considered.

---

## Run it yourself

Requires Python 3.11+ and a free API key from Google AI Studio (Groq optional, used as fallback).

```bash
git clone <REPO URL> && cd ai-lawyer-india
python -m venv .venv
.venv\Scripts\activate          # Windows   (macOS/Linux: source .venv/bin/activate)
pip install -r requirements.txt
copy .env.example .env          # macOS/Linux: cp .env.example .env  - then paste your key(s) into .env
python scripts/test_llm.py      # checks the key works
streamlit run app/main.py
```

**Swap the model** by editing `config.yaml` (provider URL, model name, key variable). Any
OpenAI-compatible API works; no code changes. The app automatically falls back to the second model if the
first fails (rate limit, outage).

---

## Known limitations (stated, not hidden)

- Central law only: no state rent acts or state labour rules yet; the app says so.
- The number check confirms a number appears in the KB/facts, not that it's used in the right place.
- Keyword escalation has false positives (e.g. "an order of 420 rupees" → criminal), kept visible in tests.
- Neutral tone and "don't repeat key facts" are prompt rules only; the model doesn't always follow them.
- A user can't correct an already-answered fact without starting over (future: an edit button).
- Salary and notice packs give analysis only, with no documents yet. Practice mode ("talk to the other side") is not built.
- Free-tier rate limits: under load, some answers come from the fallback model; each test report lists which model answered.

## How it scales

New problems are new folders (KB + questions + calculators), with no engine changes. The real bottleneck is
**human verification of each KB entry**, not compute. Next steps: per-state KB entries (rent acts,
labour rules) filtered by the user's state; a database with search once the KB outgrows the prompt;
WhatsApp/voice input (Groq Whisper) for low-literacy users; periodic re-verification of every entry.
