"""
drafting.py - Stage 5: fill a document template from the case file.

Who writes what:
  CODE   : the whole document structure, every fact slot, every legal citation (from the verified KB),
           and a [PLACEHOLDER] for anything unknown - personal details (name, address, phone, order ID)
           are NEVER collected or sent to the AI; they are always placeholders (ADR-015, privacy).
  MODEL  : only the "facts of the case" paragraph, in formal English, from the case file.
  CHECK  : that paragraph may not contain ANY number or date that is not in the case file, nor any
           legal reference or promise. If it fails, code writes a plain version itself (never invents).
"""
import json
import re
from datetime import date
from pathlib import Path

import yaml

from app import llm
from app.case_file import load_intake, can_draft, missing, UNKNOWN
from app.kb import load_kb, load_calculators, ROOT
from app.validator import LEGAL_PATTERNS, CASE_SENSITIVE, PROMISE_PATTERNS
from app.render import _rupees

NARRATIVE_PROMPT = """You write the "facts of the case" section of a consumer complaint in India.
Write 3 to 5 short numbered paragraphs in formal, plain English, in the first person ("I").
Use ONLY the facts below. Do not add any fact, name, date, amount, place, opinion or legal conclusion.
Do not mention any law, section, rule or court case. Do not say what the outcome will be.
Write dates exactly as given (e.g. 26 October 2026). Write amounts as "Rs" followed by the number given.
Some facts are written in Hindi or Hinglish: translate them into plain, formal English with exactly the same
meaning. Do not add detail while translating (e.g. "thode time baad band ho gaya" -> "stopped working after a short time").
The whole text must be in English.
If a fact is a [PLACEHOLDER ...], copy the placeholder text exactly as it is.

FACTS:
{facts}

Respond with ONLY JSON: {{"paragraphs": ["1. ...", "2. ..."]}}"""


def load_drafts(pack: str) -> list[dict]:
    return yaml.safe_load((ROOT / "packs" / pack / "drafts.yaml").read_text(encoding="utf-8"))["documents"]


# ---------- formatting facts ----------
def _fmt_date(value) -> str | None:
    try:
        return date.fromisoformat(str(value)).strftime("%d %B %Y").lstrip("0")
    except (TypeError, ValueError):
        return None


def _placeholder(field: dict) -> str:
    label = field["key"].replace("_", " ").upper()
    hint = f" – {field['find_hint']}" if field.get("find_hint") else ""
    return f"[{label}{hint}]"


def fact_values(case: dict) -> dict:
    """Every fact as display text, or a [PLACEHOLDER] if missing/unknown. Never a guess."""
    intake = load_intake(case["pack"])
    out = {}
    for f in intake["fields"]:
        v = case["facts"].get(f["key"])
        if v is None or v == UNKNOWN:
            out[f["key"]] = _placeholder(f)
        elif f["type"] == "date":
            out[f["key"]] = _fmt_date(v) or _placeholder(f)
        elif f["type"] == "money":
            out[f["key"]] = f"Rs {_rupees(v)}" if isinstance(v, (int, float)) else _placeholder(f)
        elif f["type"] == "list":
            out[f["key"]] = ", ".join(map(str, v)) if isinstance(v, list) else str(v)
        elif f["key"] == "user_city_state":                       # "rohtak,haryana" -> "Rohtak, Haryana"
            out[f["key"]] = ", ".join(p.strip().title() for p in str(v).split(",") if p.strip())
        elif f["type"] == "yesno":
            out[f["key"]] = "yes" if v else "no"
        elif f["key"] in ("seller_name", "product_or_service"):  # "flipkart" -> "Flipkart" in a formal letter
            out[f["key"]] = str(v)[:1].upper() + str(v)[1:]
        else:
            out[f["key"]] = str(v)
    return out


# ---------- citations (built from the verified KB, never typed by the model) ----------
def cite_inline(kb: dict, kb_id: str) -> str:
    e = kb["entries"].get(kb_id)
    if not e or e.get("status") != "verified":
        return "[CHECK THE LEGAL PROVISION WITH A LAWYER]"
    sec = str(e.get("section", ""))
    if sec.lower().startswith(("rule", "sched")):
        return f"{sec} of the {e['act']}"
    return f"Section {sec} of the {e['act']}"


# ---------- the one AI step + its check ----------
def _allowed_numbers(values: dict) -> set[str]:
    nums = set()
    for v in values.values():
        nums |= {n.replace(",", "") for n in re.findall(r"\d[\d,]*", v)}
    return nums


# Common Hindi/Hinglish words that should never appear in an English legal document (F33).
HINGLISH_WORDS = {"hai", "hain", "tha", "thi", "the", "ho", "gaya", "gayi", "hogya", "nahi", "nahin", "ki", "ka",
                  "ke", "ko", "par", "baad", "thode", "kuch", "mujhe", "maine", "aur", "bhi", "koi", "jawab",
                  "band", "kiya", "liya", "diya", "raha", "rahi", "se", "mein", "me"}
ENGLISH_OK = {"the", "band"}          # also valid English words - only count them with other hits


def hinglish_hits(text: str) -> list[str]:
    words = re.findall(r"[a-z]+", text.lower())
    hits = [w for w in words if w in HINGLISH_WORDS and w not in ENGLISH_OK]
    return hits if len(hits) >= 2 else []


def check_narrative(text: str, values: dict) -> list[str]:
    """Problems found in the model's paragraph. Empty list = safe to use."""
    problems = []
    allowed = _allowed_numbers(values)
    for n in re.findall(r"\d[\d,]*", text):
        n = n.replace(",", "")
        if n not in allowed and not re.fullmatch(r"[1-5]", n):      # 1-5 = paragraph numbers
            problems.append(f"number not in case file: {n}")
    for pat in LEGAL_PATTERNS:
        flags = 0 if pat in CASE_SENSITIVE else re.IGNORECASE
        problems += [f"legal reference: {m.group(0)}" for m in re.finditer(pat, text, flags)]
    for pat in PROMISE_PATTERNS:
        problems += [f"promise: {m.group(0)}" for m in re.finditer(pat, text, re.IGNORECASE)]
    if re.search(r"[\u0900-\u097F]", text) or hinglish_hits(text):
        problems.append("not fully in English: " + " ".join(hinglish_hits(text)[:5] or ["Devanagari text"]))
    if values.get("seller_name", "").lower() not in text.lower() and not values["seller_name"].startswith("["):
        problems.append("seller name missing")
    return problems


def _own_words(text: str) -> str:
    """Free text from the user goes in quotes, clearly marked as their words (F33)."""
    return text if text.startswith("[") else f'(in my own words) "{text}"'


def plain_narrative(v: dict) -> str:
    """Deterministic fallback: a plain paragraph built only from the facts. No AI."""
    lines = [
        f"1. On {v['purchase_date']}, I purchased {v['product_or_service']} from {v['seller_name']} "
        f"for {v['amount_paid']}.",
        f"2. On {v['problem_date']}, the following problem arose: {_own_words(v['what_went_wrong'])}.",
        f"3. I purchased it for my personal use." if v.get("for_business_use") == "no" else
        f"3. Purpose of purchase: [PERSONAL OR BUSINESS USE – please state].",
        f"4. Steps I have already taken: {_own_words(v['complaints_made'])}.",
    ]
    return "\n\n".join(lines)


def narrative(case: dict, values: dict, log: list) -> str:
    facts = {k: values[k] for k in ("product_or_service", "seller_name", "bought_online", "amount_paid",
                                    "purchase_date", "what_went_wrong", "problem_date", "complaints_made")}
    facts["purpose"] = "personal use" if values.get("for_business_use") == "no" else values.get("for_business_use")
    try:
        out = llm.chat_json([{"role": "system",
                              "content": NARRATIVE_PROMPT.format(facts=json.dumps(facts, ensure_ascii=False, indent=1))},
                             {"role": "user", "content": "Write the facts section."}])
        text = "\n\n".join(str(p).strip() for p in out.get("paragraphs", []) if str(p).strip())
    except Exception as err:
        log.append(f"model unavailable ({err}) -> plain version used")
        return plain_narrative(values)
    problems = check_narrative(text, values) if text else ["empty"]
    if problems:
        log.append("model paragraph rejected -> plain version used: " + "; ".join(problems))
        return plain_narrative(values)
    return text


# ---------- assemble ----------
def available(case: dict) -> list[dict]:
    """Documents offered for this case, each with {"ok": bool, "why_not": [...]} ."""
    intake = load_intake(case["pack"])
    out = []
    for d in load_drafts(case["pack"]):
        cond = d.get("only_if", {})
        if any(case["facts"].get(k) != v for k, v in cond.items()):
            continue
        why_not = []
        if d.get("requires_full_case") and not can_draft(case, intake):
            why_not = [f"{f['question']}" + (f" (tip: {f['find_hint']})" if f.get("find_hint") else "")
                       for f in missing(case, intake, for_draft=True)]
        if d.get("requires_full_case"):
            calcs = {c["name"]: c for c in load_calculators(case["pack"]).run_all(case["facts"])}
            if calcs["consumer_check"]["status"] == "probably_not":
                why_not.append("Bought for business use - consumer law may not apply. Please consult a lawyer.")
            if calcs["time_limit"]["status"] == "passed":
                why_not.append("The 2-year time limit may have passed - talk to a lawyer before filing.")
        out.append({**d, "ok": not why_not, "why_not": why_not})
    return out


def draft(case: dict, doc_id: str) -> dict:
    """Build one document. Returns {"title", "text", "placeholders": [...], "log": [...], "explain"}."""
    doc = next(d for d in available(case) if d["id"] == doc_id)
    if not doc["ok"]:
        raise ValueError("This document needs more facts first: " + "; ".join(doc["why_not"]))
    kb = load_kb(case["pack"])
    v = fact_values(case)
    log = []

    city_state = v["user_city_state"]
    state = city_state.split(",")[-1].strip() if "," in city_state and not city_state.startswith("[") else "[STATE]"
    amount = case["facts"].get("amount_paid")
    slots = {
        **v,
        "narrative": narrative(case, v, log),
        "user_state": state.upper() if not state.startswith("[") else state,
        "amount_paid_fmt": _rupees(amount) if isinstance(amount, (int, float)) else "[AMOUNT PAID]",
        "problem_date_fmt": v["problem_date"],
        "evidence_list": "\n".join(f"{i}. {e.strip()}" for i, e in enumerate(v["evidence"].split(","), 1))
                         if not v["evidence"].startswith("[") else v["evidence"],
        "forum_citation": cite_inline(kb, "CPR2021-PECUNIARY"),
        "territorial_citation": cite_inline(kb, "CPA2019-S34"),
        "limitation_citation": cite_inline(kb, "CPA2019-S69"),
        "relief_citation": cite_inline(kb, "CPA2019-S39"),
        # numbers below come from the VERIFIED summary of ECOM2020-R4-5 (48 hours / one month)
        "ecom_rule_sentence": (f"Under {cite_inline(kb, 'ECOM2020-R4-5')}, the grievance officer is required to "
                               "acknowledge a consumer complaint within 48 hours and redress it within one month "
                               "of receiving it. I request you to do so.")
                              if kb["entries"].get("ECOM2020-R4-5", {}).get("status") == "verified" else "",
    }
    template = (ROOT / "packs" / case["pack"] / doc["template"]).read_text(encoding="utf-8")
    text = template.format(**slots)
    placeholders = sorted(set(re.findall(r"\[[A-Z][^\]]*\]", text)))   # [CAPITALISED ...] = to fill in
    lang = case.get("language") or "en"
    explain = doc.get(f"explain_{lang}") or doc.get("explain_en")
    return {"title": doc["title"], "text": text, "placeholders": placeholders, "log": log,
            "explain": " ".join(str(explain).split()), "kb_last_verified": kb["last_verified"]}
