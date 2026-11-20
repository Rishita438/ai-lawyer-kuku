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


def _rupees(n) -> str:
    """Indian-style grouping: 1500000 -> 15,00,000."""
    s = str(int(n))
    if len(s) <= 3:
        return s
    head, tail = s[:-3], s[-3:]
    groups = []
    while len(head) > 2:
        groups.insert(0, head[-2:]); head = head[:-2]
    return ",".join(([head] if head else []) + groups + [tail])

NARRATIVE_PROMPT = """You write the "facts" section of a formal letter or complaint in India.
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

Also give English versions of these short fields, for use elsewhere in the document (same meaning, no
added detail; keep proper names, just write them in English/Latin letters):
{short_fields}

Respond with ONLY JSON: {{"paragraphs": ["1. ...", "2. ..."], "english": {{"<field>": "<English text>", ...}}}}"""


def load_drafts(pack: str) -> list[dict]:
    path = ROOT / "packs" / pack / "drafts.yaml"
    if not path.exists():                       # light packs may have no documents yet
        return []
    return yaml.safe_load(path.read_text(encoding="utf-8"))["documents"]


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
        elif f.get("capitalise"):                               # "flipkart" -> "Flipkart" in a formal letter
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


def check_narrative(text: str, values: dict, must_mention: str | None = None) -> list[str]:
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
    name = values.get(must_mention, "") if must_mention else ""
    if name and not name.startswith("[") and name.lower() not in text.lower():
        problems.append(f"{must_mention} missing")
    return problems


def _own_words(text: str) -> str:
    """Free text from the user goes in quotes, clearly marked as their words (F33)."""
    return text if text.startswith("[") else f'(in my own words) "{text}"'


def plain_narrative(case: dict, v: dict, fields: list[str]) -> str:
    """Deterministic fallback, no AI: the pack's own wording if it has one, else a numbered list of facts."""
    calc = load_calculators(case["pack"])
    if hasattr(calc, "plain_narrative"):
        return calc.plain_narrative(v, _own_words)
    labels = {f["key"]: f.get("label") or f["key"].replace("_", " ").capitalize()
              for f in load_intake(case["pack"])["fields"]}
    return "\n\n".join(f"{n}. {labels.get(k, k)}: {_own_words(v[k])}." for n, k in enumerate(fields, 1))


# Short free-text fields that appear directly in documents: the model gives an English version (checked),
# otherwise the user's words are quoted. (F42: "My request: 10 guna refund"; F45: seller "मीशो".)
ENGLISH_FIELDS = ("desired_outcome", "seller_name", "product_or_service", "employer_name")


def narrative(case: dict, values: dict, doc: dict, log: list) -> str:
    fields = doc.get("narrative_fields") or [k for k in values if k not in ("evidence", "desired_outcome")]
    facts = {k: values[k] for k in fields if k in values}
    short = {k: values[k] for k in ENGLISH_FIELDS if k in values and not values[k].startswith("[")}
    try:
        out = llm.chat_json([{"role": "system",
                              "content": NARRATIVE_PROMPT.format(facts=json.dumps(facts, ensure_ascii=False, indent=1),
                                                                 short_fields=json.dumps(short, ensure_ascii=False))},
                             {"role": "user", "content": "Write the facts section."}])
        text = "\n\n".join(str(p).strip() for p in out.get("paragraphs", []) if str(p).strip())
    except Exception as err:
        log.append(f"model unavailable ({err}) -> plain version used")
        return plain_narrative(case, values, fields)

    # F42/F45: English versions of short fields (desired outcome, names) - each checked like the paragraph.
    english = out.get("english") if isinstance(out.get("english"), dict) else {}
    for k, v in english.items():
        if k in short and isinstance(v, str) and v.strip():
            issues = check_narrative(v, values)
            if issues:
                log.append(f"English version of {k} rejected: " + "; ".join(issues))
            else:
                values[k] = v.strip()

    problems = check_narrative(text, values, doc.get("must_mention")) if text else ["empty"]
    if problems:
        log.append("model paragraph rejected -> plain version used: " + "; ".join(problems))
        return plain_narrative(case, values, fields)
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
        calcs = load_calculators(case["pack"]).run_all(case["facts"])
        stops = [c["escalate"]["reason"] for c in calcs if (c.get("escalate") or {}).get("stop")]
        if stops:                                          # F43: out of scope -> no documents at all
            why_not = list(dict.fromkeys(why_not + stops))
        elif d.get("requires_full_case"):
            why_not += [c["blocks_drafting"] for c in calcs if c.get("blocks_drafting")]
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

    city_state = v.get("user_city_state", "[CITY, STATE]")
    state = city_state.split(",")[-1].strip() if "," in city_state and not city_state.startswith("[") else "[STATE]"
    evidence = v.get("evidence", "[LIST OF DOCUMENTS]")
    story = narrative(case, v, doc, log)                  # may replace short fields with checked English versions
    slots = {
        **v,
        "narrative": story,
        "user_state": state.upper() if not state.startswith("[") else state,
        "evidence_list": "\n".join(f"{i}. {e.strip()}" for i, e in enumerate(evidence.split(","), 1))
                         if not evidence.startswith("[") else evidence,
    }
    # F52: "10 guna refund" / "5 lakh compensation" (for a Rs 600 order) went straight into the relief.
    # A desired outcome with a number or multiplier that is not one of the case's own amounts becomes a
    # placeholder the user must fill in deliberately.
    want = str(slots.get("desired_outcome", ""))
    case_nums = {n.replace(",", "") for k, val in case["facts"].items() if k != "desired_outcome"
                 for n in re.findall(r"\d[\d,]*", str(val))}
    want_nums = {n.replace(",", "") for n in re.findall(r"\d[\d,]*", want)}
    if not want.startswith("[") and ((want_nums - case_nums) or re.search(r"\bguna\b|\btimes\b|\b\d+x\b|गुना", want, re.I)):
        log.append(f"desired outcome '{want}' contains an amount not supported by the case -> placeholder")
        slots["desired_outcome"] = "[RELIEF YOU ARE CLAIMING – e.g. refund of the amount paid; compensation is decided by the Commission]"
    for k in ENGLISH_FIELDS:                           # still Hindi/Hinglish? quote it as the user's own words
        if k not in slots or slots[k].startswith("["):
            continue
        if any(re.search(p, slots[k], 0 if p in CASE_SENSITIVE else re.IGNORECASE) for p in LEGAL_PATTERNS):
            # F57: the fallback quoted "10 guna refund jo section 420B mein likha hai" into the documents.
            # A user's words that cite a law/section never go into a document - the user restates them.
            log.append(f"{k} mentions a law/section -> placeholder (not copied into the document)")
            slots[k] = f"[{k.replace('_', ' ').upper()} – please write this in your own words, without citing any law]"
        elif re.search(r"[\u0900-\u097F]", slots[k]) or hinglish_hits(slots[k]):
            slots[k] = _own_words(slots[k])
    calc = load_calculators(case["pack"])
    if hasattr(calc, "draft_slots"):                      # pack-specific slots (amounts, citations, ...)
        slots.update(calc.draft_slots(case["facts"], v, lambda kb_id: cite_inline(kb, kb_id)))
    template = (ROOT / "packs" / case["pack"] / doc["template"]).read_text(encoding="utf-8")
    text = template.format(**slots)
    placeholders = sorted(set(re.findall(r"\[[A-Z][^\]]*\]", text)))   # [CAPITALISED ...] = to fill in
    lang = case.get("language") or "en"
    explain = doc.get(f"explain_{lang}") or doc.get("explain_en")
    return {"title": doc["title"], "text": text, "placeholders": placeholders, "log": log,
            "explain": " ".join(str(explain).split()), "kb_last_verified": kb["last_verified"]}
