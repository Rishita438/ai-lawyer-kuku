"""
check_kb.py - checks every pack's kb.yaml for missing fields and duplicate IDs.

Run:  python scripts/check_kb.py
Why:  the bot is only allowed to cite KB entries, so a broken KB entry = a broken citation.
      This script catches mistakes before the bot ever sees them.
"""
import sys
from pathlib import Path
import yaml

# Every KB entry must have these fields (see packs/consumer/kb.yaml for an example).
REQUIRED = ["id", "type", "title", "plain_summary", "source_name",
            "source_url", "jurisdiction", "status"]
LAW_ONLY = ["act", "section"]          # extra fields required when type == law
VALID_STATUS = {"unverified", "verified", "reviewed"}

def check_pack(kb_path: Path) -> list[str]:
    errors, warnings = [], []
    data = yaml.safe_load(kb_path.read_text(encoding="utf-8")) or {}
    seen_ids = set()
    for i, entry in enumerate(data.get("entries", [])):
        label = entry.get("id", f"entry #{i}")
        needed = REQUIRED + (LAW_ONLY if entry.get("type") == "law" else [])
        for field in needed:
            # practice notes ("reviewed") have no official source, so no URL is required
            if field == "source_url" and entry.get("status") == "reviewed":
                continue
            if not entry.get(field):
                errors.append(f"{label}: missing '{field}'")
        if entry.get("status") not in VALID_STATUS:
            errors.append(f"{label}: status must be one of {VALID_STATUS}")
        url = str(entry.get("source_url") or "")
        if entry.get("status") != "reviewed" and not url.startswith("https://"):
            errors.append(f"{label}: source_url must start with https://")
        # Warnings: things a human should look at, but that don't break the bot.
        if url and url[-1] in ">)],.;'\"":
            errors.append(f"{label}: source_url ends with a stray '{url[-1]}' - link will break")
        note = str(entry.get("notes") or "").lower()
        if entry.get("status") in ("verified", "reviewed") and any(w in note for w in ("todo", "confirm ")):
            warnings.append(f"{label}: status is {entry['status']} but notes still read like a to-do")
        if label in seen_ids:
            errors.append(f"{label}: duplicate id")
        seen_ids.add(label)
    return errors, warnings

def main():
    packs = sorted(Path("packs").glob("*/kb.yaml"))
    total_errors = 0
    for kb in packs:
        # A broken YAML file (bad indentation, tabs, unclosed quote) should be reported
        # clearly, not crash the whole check.
        try:
            data = yaml.safe_load(kb.read_text(encoding="utf-8")) or {}
        except yaml.YAMLError as err:
            mark = getattr(err, "problem_mark", None)
            where = f" near line {mark.line + 1}" if mark else ""
            print(f"{kb.parent.name}: YAML SYNTAX ERROR{where} - check indentation (2 spaces before '- id:', 4 before other keys, no tabs)")
            total_errors += 1
            continue
        entries = data.get("entries", [])
        unverified = sum(1 for e in entries if e.get("status") == "unverified")
        reviewed = sum(1 for e in entries if e.get("status") == "reviewed")
        errs, warns = check_pack(kb)
        total_errors += len(errs)
        print(f"{kb.parent.name}: {len(entries)} entries, {unverified} unverified, "
              f"{reviewed} reviewed, {len(errs)} errors")
        for e in errs:
            print("   - ERROR:", e)
        for w in warns:
            print("   ! check:", w)
    sys.exit(1 if total_errors else 0)

if __name__ == "__main__":
    main()
