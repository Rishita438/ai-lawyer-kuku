"""
validator.py - the citation and number checker (ADR-007, ADR-008). Plain code, no AI.

After the model writes its analysis, this runs and:
  1. drops any kb_id that is not in the knowledge base (invented citations)
  2. drops any legal point that is left with no valid citation
  3. scans ALL free text for law-like references the model typed itself
     (section numbers, acts, IPC/BNS, case names, law reports) and removes them
  4. removes promises of outcome ("you will win", "pakka milega", "guaranteed")
  5. scans for numbers with units (days, years, rupees, lakh...) and removes any number that
     does not come from the KB, the calculators or the user's own facts
Every removal is logged, so the strip rate can be measured (it's a health metric).
"""
import re

REMOVED_REF = "[removed: unverified legal reference]"
REMOVED_NUM = "[removed: unverified number]"
REMOVED_PROMISE = "[removed: nobody can promise a legal outcome]"

# Promises of outcome (English / Hinglish / Hindi). Nobody can guarantee a legal result.
PROMISE_PATTERNS = [
    r"\byou will (?:definitely |surely |certainly )?(?:win|get (?:your|a|the) (?:full )?(?:refund|money|compensation))\b",
    r"\b(?:guaranteed?|guarantee that|100\s?%\s*(?:sure|chance|certain)|definitely win|sure to win|bound to win)\b",
    r"\b(?:pakka|zaroor|zarur|100\s?%)\s+(?:jeet|jeetoge|jeetenge|milega|mil jayega|refund milega)\w*",
    r"\bjeet (?:jaoge|jayenge|jaenge)\b",
    r"ज़रूर जीत|पक्का जीत|ज़रूर मिलेगा|पक्का मिलेगा|गारंटी",
]

# Things the model must never type itself. Citations are rendered by code from the KB.
LEGAL_PATTERNS = [
    r"\b(?:section|sec|sect)\.?\s*\d+[a-z]?(?:\s*\(\s*\w+\s*\))*",      # Section 69, Sec. 2(7)
    r"\bs\.\s?\d+[a-z]?(?:\(\w+\))*",                                  # s.69, s. 2(47)
    r"\bdhara\s*\d+[a-z]?",                                            # dhara 420
    r"धारा\s*\d+",                                                     # धारा 420
    r"\b(?:article|rule|regulation)\s+\d+[a-z]?(?:\s*\(\s*\w+\s*\))*",     # (not "order": order IDs)
    r"(?:(?<!\w)[A-Z(][\w()\-]*,?\s+){1,10}(?:Act|Code|Rules|Sanhita)\b,?\s*\d{4}",   # Consumer Protection Act, 2019
    r"\b(?:IPC|BNS|BNSS|CrPC|CPC|NI Act)\b",
    r"\b[A-Z][\w.&]*\s+(?:v|vs)\.\s+[A-Z][\w.&]*",                    # Sharma v. Union, Ram vs. Shyam
    r"\bAIR\s*\d{4}\b",                                               # AIR 2019 SC ...
    r"\(\d{4}\)\s*\d+\s*SCC\b|\b\d{4}\s*SCC\b",                       # (2020) 5 SCC
    r"\b(?:Code|Act)\s+on\s+[A-Z]\w*(?:\s+[A-Z]\w*)*,?\s*\d{4}",              # Code on Wages, 2019
]

# Patterns that rely on Capital Letters (act names, case names) must stay case-sensitive.
CASE_SENSITIVE = {LEGAL_PATTERNS[5], LEGAL_PATTERNS[7], LEGAL_PATTERNS[10]}

UNITS = r"(?:lakh|lac|crore|days?|din|months?|mahin[ea]|mahine|years?|saal|varsh|hours?|ghante|weeks?|hafte|rupees?|rupaye|rs\.?|%)"
NUMBER_WITH_UNIT = re.compile(
    rf"(?:₹|rs\.?\s*|inr\s*)?(\d[\d,]*(?:\.\d+)?)\s*{UNITS}\b|(?:₹|rs\.?\s*|inr\s*)(\d[\d,]*(?:\.\d+)?)",
    re.IGNORECASE)


def _numbers_in(text: str) -> set[str]:
    """All plain numbers in a text, normalised ('15,000' -> '15000')."""
    return {n.replace(",", "") for n in re.findall(r"\d[\d,]*(?:\.\d+)?", str(text))}


def allowed_numbers(kb: dict, calc_results: list, facts: dict) -> set[str]:
    """Numbers the model may use: from cited-able KB text, calculator outputs and the user's facts."""
    allowed = set()
    for e in kb["entries"].values():
        allowed |= _numbers_in(e.get("plain_summary", ""))
    allowed |= _numbers_in(calc_results)
    allowed |= _numbers_in(facts)
    return allowed


def clean_text(text: str, allowed_nums: set[str], log: list) -> str:
    if not text:
        return text
    for pat in LEGAL_PATTERNS:
        flags = 0 if pat in CASE_SENSITIVE else re.IGNORECASE
        for m in re.finditer(pat, text, flags=flags):
            log.append({"type": "legal_reference", "text": m.group(0)})
        text = re.sub(pat, REMOVED_REF, text, flags=flags)

    for pat in PROMISE_PATTERNS:                      # outcome promises -> removed (adversarial case)
        for m in re.finditer(pat, text, flags=re.IGNORECASE):
            log.append({"type": "promised_outcome", "text": m.group(0)})
        text = re.sub(pat, REMOVED_PROMISE, text, flags=re.IGNORECASE)

    def num_sub(m):
        num = (m.group(1) or m.group(2) or "").replace(",", "")
        if num in allowed_nums:
            return m.group(0)
        log.append({"type": "number", "text": m.group(0)})
        return REMOVED_NUM
    return NUMBER_WITH_UNIT.sub(num_sub, text)


def validate(analysis: dict, kb: dict, calc_results: list, facts: dict) -> tuple[dict, list]:
    """Return (cleaned_analysis, log). Never trusts the model's citations or numbers."""
    log, known = [], set(kb["entries"])
    nums = allowed_numbers(kb, calc_results, facts)

    def valid_ids(ids):
        good = []
        for i in ids or []:
            if i in known:
                good.append(i)
            else:
                log.append({"type": "invented_kb_id", "text": str(i)})
        return good

    out = {"summary": clean_text(analysis.get("summary", ""), nums, log),
           "points": [], "options": [], "uncertainties": [],
           "suggest_lawyer": bool(analysis.get("suggest_lawyer")),
           "lawyer_reason": clean_text(analysis.get("lawyer_reason", ""), nums, log)}

    for p in analysis.get("points", []):
        ids = valid_ids(p.get("kb_ids"))
        if not ids:                                   # a legal point with no real source -> drop it
            log.append({"type": "uncited_point_dropped", "text": str(p.get("text", ""))[:120]})
            continue
        out["points"].append({"text": clean_text(p.get("text", ""), nums, log), "kb_ids": ids})

    for o in analysis.get("options", []):
        out["options"].append({"title": clean_text(o.get("title", ""), nums, log),
                               "why": clean_text(o.get("why", ""), nums, log),
                               "steps": [clean_text(s, nums, log) for s in o.get("steps", [])],
                               "kb_ids": valid_ids(o.get("kb_ids"))})

    out["uncertainties"] = [clean_text(u, nums, log) for u in analysis.get("uncertainties", [])]
    return out, log
