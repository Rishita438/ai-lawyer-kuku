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


def allowed_numbers(kb: dict, calc_results: list, facts: dict, user_words: list | None = None) -> set[str]:
    """Numbers the model may use: from cited-able KB text, calculator outputs and the user's facts."""
    allowed = set()
    for e in kb["entries"].values():
        allowed |= _numbers_in(e.get("plain_summary", ""))
    allowed |= _numbers_in(calc_results)
    allowed |= _numbers_in(facts)
    allowed |= _numbers_in(user_words or [])       # F44: the user's own words ("4 mahine") are a valid source
    return allowed


# "no guarantee", "guarantee nahi di ja sakti", "could not verify section 420B" are HONEST refusals,
# not promises or citations (F40). A sentence containing one of these is treated as a negation.
NEGATION = re.compile(r"\b(?:not|no|never|cannot|can't|couldn't|could not|nahi|nahin|nahi\.|mat)\b|नहीं|न ही|मत ",
                      re.IGNORECASE)
VERIFY_WORDS = re.compile(r"verif|confirm|find|found|pata|sahi nahi|exist|nahi mil|सत्यापित|पुष्टि|नहीं मिल", re.IGNORECASE)


def _sentences(text: str) -> list[str]:
    return re.split(r"(?<=[.!?।])\s+", text)


# Fees and money limits come ONLY from the calculators ("Key facts" box). A model sentence that restates a
# fee or a forum money limit with a number is dropped (F49: "50 lakh tak koi filing fee nahi" - wrong,
# but "50 lakh" is a real KB number, so the membership-based number check passed it).
FEE_WORDS = re.compile(r"\bfees?\b|\bshulk\b|शुल्क|फ़ीस|फीस", re.IGNORECASE)
LIMIT_WORDS = re.compile(r"\b(?:lakh|lac|crore)\b|लाख|करोड़", re.IGNORECASE)
FORUM_WORDS = re.compile(r"commission|forum|aayog|आयोग|limit|seema|सीमा", re.IGNORECASE)


def restates_computed_fact(sentence: str) -> bool:
    has_num = bool(re.search(r"\d", sentence))
    return has_num and (bool(FEE_WORDS.search(sentence)) or
                        (bool(LIMIT_WORDS.search(sentence)) and bool(FORUM_WORDS.search(sentence))))


def clean_text(text: str, allowed_nums: set[str], log: list, allow_unverified_refs: bool = False,
               drop_computed: bool = True) -> str:
    """allow_unverified_refs: in "uncertainties", a sentence that says it could NOT verify a law may name it
    (e.g. "I could not verify the Section 420B you mentioned") - it is then marked as unverified."""
    if not text:
        return text
    out = []
    for sent in _sentences(text):
        if drop_computed and restates_computed_fact(sent):
            log.append({"type": "restated_fee_or_limit", "text": sent[:160]})
            continue
        negated = bool(NEGATION.search(sent))
        keep_refs = allow_unverified_refs and negated and VERIFY_WORDS.search(sent)
        for pat in LEGAL_PATTERNS:
            flags = 0 if pat in CASE_SENSITIVE else re.IGNORECASE
            if keep_refs:
                sent = re.sub(pat, lambda m: f"{m.group(0)} (⚠️ not verified - don't rely on it)", sent, flags=flags)
                continue
            for m in re.finditer(pat, sent, flags=flags):
                log.append({"type": "legal_reference", "text": m.group(0)})
            sent = re.sub(pat, REMOVED_REF, sent, flags=flags)
        for pat in PROMISE_PATTERNS:
            def promise_sub(m, sent=sent):
                # "koi guarantee nahi" / "no ... guaranteed" is a refusal: a negation must sit right next to
                # the promise word. "pakka jeetoge, haaroge nahi" is still a promise.
                before, after = sent[max(0, m.start() - 20): m.start()], sent[m.end(): m.end() + 7]
                if NEGATION.search(before) or NEGATION.search(after):
                    return m.group(0)
                log.append({"type": "promised_outcome", "text": m.group(0)})
                return REMOVED_PROMISE
            sent = re.sub(pat, promise_sub, sent, flags=re.IGNORECASE)
        out.append(sent)
    text = " ".join(out)

    def num_sub(m):
        num = (m.group(1) or m.group(2) or "").replace(",", "")
        if num in allowed_nums:
            return m.group(0)
        log.append({"type": "number", "text": m.group(0)})
        return REMOVED_NUM
    return NUMBER_WITH_UNIT.sub(num_sub, text)


def _text(x) -> str:
    """Models sometimes return an object or list where text was asked for (F38). Flatten it to text."""
    if isinstance(x, dict):
        return " ".join(_text(v) for v in x.values())
    if isinstance(x, (list, tuple)):
        return " ".join(_text(v) for v in x)
    return "" if x is None else str(x)


def _list(x) -> list:
    return x if isinstance(x, list) else ([] if x in (None, "") else [x])


def validate(analysis: dict, kb: dict, calc_results: list, facts: dict, user_words: list | None = None) -> tuple[dict, list]:
    """Return (cleaned_analysis, log). Never trusts the model's citations, numbers - or its output shape."""
    log, known = [], set(kb["entries"])
    if not isinstance(analysis, dict):
        log.append({"type": "bad_shape", "text": str(analysis)[:120]})
        analysis = {}
    nums = allowed_numbers(kb, calc_results, facts, user_words)

    def valid_ids(ids):
        good = []
        for i in _list(ids):
            i = _text(i).strip()
            if i in known:
                good.append(i)
            else:
                log.append({"type": "invented_kb_id", "text": str(i)})
        return good

    out = {"summary": clean_text(_text(analysis.get("summary", "")), nums, log),
           "points": [], "options": [], "uncertainties": [],
           "suggest_lawyer": bool(analysis.get("suggest_lawyer")),
           "lawyer_reason": clean_text(_text(analysis.get("lawyer_reason", "")), nums, log)}

    for p in _list(analysis.get("points")):
        p = p if isinstance(p, dict) else {"text": _text(p), "kb_ids": []}
        ids = valid_ids(p.get("kb_ids"))
        if not ids:                                   # a legal point with no real source -> drop it
            log.append({"type": "uncited_point_dropped", "text": str(p.get("text", ""))[:120]})
            continue
        txt = clean_text(_text(p.get("text", "")), nums, log)
        if txt.strip():                                  # the whole point may have been a restated fee
            out["points"].append({"text": txt, "kb_ids": ids})

    for o in _list(analysis.get("options")):
        o = o if isinstance(o, dict) else {"title": _text(o)}
        out["options"].append({"title": clean_text(_text(o.get("title", "")), nums, log),
                               "why": clean_text(_text(o.get("why", "")), nums, log),
                               "steps": [clean_text(_text(s), nums, log) for s in _list(o.get("steps"))],
                               "kb_ids": valid_ids(o.get("kb_ids"))})

    out["uncertainties"] = [clean_text(_text(u), nums, log, allow_unverified_refs=True)
                            for u in _list(analysis.get("uncertainties"))]
    return out, log
