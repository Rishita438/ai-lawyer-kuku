"""
case_file.py - the bot's structured memory (ADR-009).

Instead of re-reading the whole chat every turn, the bot keeps a small "case file":
one slot per fact from the pack's intake.yaml. The model only FILLS slots; plain code
decides what is still missing, what to ask next, and when drafting is allowed.
"""
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent.parent
UNKNOWN = "unknown"          # user said they don't know -> stop asking, but never invent a value


def load_intake(pack: str) -> dict:
    """Read packs/<pack>/intake.yaml."""
    return yaml.safe_load((ROOT / "packs" / pack / "intake.yaml").read_text(encoding="utf-8"))


def new_case(pack: str) -> dict:
    """An empty case file: every field starts as None (= not asked/answered yet)."""
    intake = load_intake(pack)
    return {"pack": pack,
            "facts": {f["key"]: None for f in intake["fields"]},
            "language": None}


def merge(case: dict, extracted: dict, explicit_only: set[str] = frozenset(),
          asked_key: str | None = None) -> list[str]:
    """Copy extracted facts into the case file. Returns the keys that changed.
    Rules (all enforced in code, not trusted to the model):
      - ignore keys that are not in the intake (the model can't invent new fields)
      - ignore empty values (None, "", [])
      - never overwrite a real answer with "unknown"
      - an answered fact (real value or "unknown") can only change when that question is asked again
      - fields in `explicit_only` are accepted ONLY if they were the question just asked
        (the model tends to assume answers like "personal use" - FAILURES F17)
    """
    changed = []
    for key, value in (extracted or {}).items():
        if key not in case["facts"] or value in (None, "", []):
            continue
        if key in explicit_only and key != asked_key:
            continue
        current = case["facts"][key]
        if value == UNKNOWN and current not in (None, UNKNOWN):
            continue
        if current is not None and key != asked_key:
            # F28 + F32: once a fact is answered (a real value OR "don't know"), only an answer to
            # THAT question may change it. The model had copied the problem-date answer
            # ("26 september") over the purchase date ("19 september") in a later turn.
            continue
        if value != current:
            case["facts"][key] = value
            changed.append(key)
    return changed


def missing(case: dict, intake: dict, for_draft: bool = False) -> list[dict]:
    """Fields still empty (None). 'unknown' counts as answered for asking, but NOT for drafting."""
    flag = "required_for_draft" if for_draft else "required"
    out = []
    for f in intake["fields"]:
        if not f.get(flag):
            continue
        value = case["facts"].get(f["key"])
        if value is None or (for_draft and value == UNKNOWN):
            out.append(f)
    return out


def next_field(case: dict, intake: dict) -> dict | None:
    """The next question to ask, in the order of intake.yaml. None = intake complete."""
    gaps = missing(case, intake)
    return gaps[0] if gaps else None


def can_draft(case: dict, intake: dict) -> bool:
    """Drafting gate: every required_for_draft fact must be a real value."""
    return not missing(case, intake, for_draft=True)
