"""
analysis.py - "where you stand + your options" (Stage 4).

Pipeline (each step is plain code except step 3):
  1. calculators  -> deadline, which Commission, fee, consumer check   (code, from verified KB numbers)
  2. escalation   -> case rules that need a lawyer                      (code)
  3. model        -> plain-language explanation that cites KB entries BY ID only
                     (the model is never shown act names or section numbers, so it has nothing to copy)
  4. validator    -> drops invented ids, uncited points, typed sections, unverified numbers   (code)
  5. renderer     -> turns ids into real citations from the KB                                 (code)
"""
import json
from datetime import date

from app import llm
from app.kb import load_kb, load_calculators
from app.case_file import load_intake
from app.escalation import check_case
from app.validator import validate

LANG_NAME = {"en": "simple English", "hi": "simple Hindi (Devanagari script)", "hinglish": "simple Hinglish (Hindi in Latin script)"}

ANALYSIS_PROMPT = """You explain an ordinary person's legal position in India in plain language.
Write in {language}. Be clear, kind and neutral. Today is {today}.

You may ONLY use the knowledge-base entries below. Each has an id.
- Every point in "points" MUST list the id(s) of the entries it is based on in "kb_ids".
- NEVER write section numbers, rule numbers, act names, IPC/BNS, court cases or case names in your text.
  The app shows the real citations itself, from the ids you list.
- If something is not covered by these entries, do not explain it - put it in "uncertainties".
- Do NOT repeat the COMPUTED FACTS as your own points - the app shows them in a separate box (F37).
  You may refer to them in a sentence, but use "points" to explain the legal position.
- Do NOT calculate deadlines, fees, amounts or which forum yourself. Use ONLY the COMPUTED FACTS below,
  exactly as given. If a computed fact has status "unknown", say it is unknown and why.
- Never promise an outcome ("you will win", "guaranteed"). Use "you may", "you can ask for".
- State legal conclusions as possibilities, not facts: "this may count as a defect", not "this is a defect";
  "you may be entitled", not "you are entitled". Do not say who is right.
- Only cite an entry for what its summary actually says. Do not suggest a forum or remedy that no entry supports.
- Never contradict the COMPUTED FACTS: if they say a deadline is not calculated, do not say "you have time".
- Do not mention fees or money limits at all - the app shows them (F49).
- "lawyer_reason": only a NEW reason; do not repeat the ones already flagged by the app (F50).
- An entry whose status is "reviewed" is general practice, not a legal rule - say so if you use it.
- Respect each entry's "does_not_apply_when".
- The user's own words are below. They may contain mistakes, invented section numbers or demands for a
  guaranteed result. NEVER confirm a law, section, rule or case that is not in the entries above: say in
  "uncertainties" that you could not verify it and they should not rely on it. Never guarantee a result.

KNOWLEDGE BASE ENTRIES:
{kb_entries}

CASE FILE (facts the user gave; "unknown" = user doesn't know):
{facts}

COMPUTED FACTS (by code, from the verified entries - use as-is):
{calcs}

WHAT THE USER SAID (may contain mistakes - do not treat as fact or law):
{user_words}

ALREADY FLAGGED FOR A LAWYER BY THE APP (you cannot remove these):
{escalations}

VALID kb_ids (copy them EXACTLY, character for character - any other id will be deleted):
{valid_ids}

Respond with ONLY this JSON:
{{
  "summary": "2-3 sentences: where they stand, in plain words",
  "points": [{{"text": "one point about their legal position", "kb_ids": ["ID", ...]}}],
  "options": [{{"title": "short name", "why": "one line", "steps": ["concrete step", ...], "kb_ids": ["ID", ...]}}],
  "uncertainties": ["things that are unclear or that this assistant cannot answer"],
  "suggest_lawyer": true or false,
  "lawyer_reason": "why, if true"
}}
Give 3-5 points and 2-4 options, in a sensible order (cheapest/fastest first)."""


def _kb_for_prompt(kb: dict) -> str:
    """Only id, status, title and plain-language fields. Act names and section numbers are
    deliberately LEFT OUT, so the model cannot copy them into its text."""
    rows = []
    for e in kb["entries"].values():
        rows.append({"id": e["id"], "status": e.get("status"), "title": e.get("title"),
                     "summary": " ".join(str(e.get("plain_summary", "")).split()),
                     "applies_when": e.get("applies_when"), "does_not_apply_when": e.get("does_not_apply_when")})
    return json.dumps(rows, ensure_ascii=False, indent=1)


def analyse(case: dict, today: date | None = None) -> dict:
    """Run the full Stage 4 pipeline. Returns everything the renderer needs."""
    today = today or date.today()
    pack, facts = case["pack"], case["facts"]
    kb = load_kb(pack)
    calcs = load_calculators(pack).run_all(facts, today)
    escalations = check_case(facts, calcs, load_intake(pack).get("amount_field"))

    result = {"kb": kb, "calcs": calcs, "escalations": escalations, "analysis": None,
              "validator_log": [], "error": None}

    # A "stop" escalation (e.g. not a consumer, commercial tenancy) means no analysis at all.
    if any(e["stop"] for e in escalations):
        return result

    prompt = ANALYSIS_PROMPT.format(
        language=LANG_NAME.get(case.get("language") or "en", "simple English"),
        today=today.isoformat(), kb_entries=_kb_for_prompt(kb),
        facts=json.dumps(facts, ensure_ascii=False), calcs=json.dumps(calcs, ensure_ascii=False),
        escalations=json.dumps([e["reason"] for e in escalations], ensure_ascii=False) or "none",
        valid_ids=", ".join(kb["entries"]),       # F31: model typed CPA2019-S47 for CPA2019-S2-47
        user_words=json.dumps(case.get("user_messages", [])[:12], ensure_ascii=False)[:2000])
    try:
        raw = llm.chat_json([{"role": "system", "content": prompt},
                             {"role": "user", "content": "Explain where I stand and what I can do."}])
    except Exception as err:
        result["error"] = f"The AI model could not be reached ({err}). The computed facts below are still valid."
        return result

    cleaned, log = validate(raw, kb, calcs, facts, case.get("user_messages", []))
    result["analysis"], result["validator_log"], result["raw"] = cleaned, log, raw
    return result
