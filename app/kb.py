"""
kb.py - loads the verified knowledge base and a pack's calculators.

The KB is the ONLY legal source the bot may cite. Everything here is read from the
packs/*/kb.yaml files that a human verified in Stage 2.
"""
import importlib.util
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent


def load_kb(pack: str) -> dict:
    """Entries of the pack + the shared pack, as {id: entry}. Also returns the oldest
    kb_last_verified date across the files used (the honest date to show users)."""
    entries, dates = {}, []
    for name in (pack, "_shared"):
        data = yaml.safe_load((ROOT / "packs" / name / "kb.yaml").read_text(encoding="utf-8"))
        dates.append(str(data.get("kb_last_verified") or "NOT VERIFIED"))
        for e in data.get("entries", []):
            entries[e["id"]] = e
    return {"entries": entries, "last_verified": min(dates)}


def load_calculators(pack: str):
    """Import packs/<pack>/calculators.py (pure functions, no AI)."""
    path = ROOT / "packs" / pack / "calculators.py"
    if not path.exists():                      # a pack may have no calculators at all
        import types
        return types.SimpleNamespace(run_all=lambda facts, today=None: [])
    spec = importlib.util.spec_from_file_location(f"calc_{pack}", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_escalation() -> dict:
    return yaml.safe_load((ROOT / "packs" / "_shared" / "escalation.yaml").read_text(encoding="utf-8"))
