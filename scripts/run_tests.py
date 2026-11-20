"""
run_tests.py - runs every case in tests/cases.yaml through the REAL app pipeline and saves the
UNEDITED outputs (Stage 7). Uses your real model (config.yaml), so it needs your API keys.

Run:   py scripts\\run_tests.py                 -> all cases
       py scripts\\run_tests.py --only C01 D01  -> cases whose id starts with C01 or D01
       py scripts\\run_tests.py --repeat 2      -> run each case twice (to see model variability)
       py scripts\\run_tests.py --sleep 4       -> wait 4 s between model calls (free-tier rate limits)

Output: raw_outputs/run_<date_time>/
          <case_id>[_r2].md   full transcript, case file, answer, documents, validator log, raw model JSON
          summary.md          one table: expected vs got, PASS/FAIL per check
Nothing in these files is edited by hand - that's the point.
"""
import argparse
import json
import re
import sys
import time
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.stdout.reconfigure(encoding="utf-8")                       # F29

import yaml
from app import llm, drafting
from app.case_file import new_case, load_intake, next_field
from app.intake import run_turn
from app.escalation import check_message, keyword_check_applies
from app.analysis import analyse
from app.render import analysis_md

MAX_TURNS = 20


def default_answer(case_lang: str | None) -> str:
    return "I don't know" if case_lang == "en" else "pata nahi"


def run_case(tc: dict, sleep: float) -> dict:
    """Simulate a user chatting with the app. Returns everything that happened."""
    pack = tc["pack"]
    intake = load_intake(pack)
    case = new_case(pack)
    case["user_messages"] = []
    history = [{"role": "assistant", "content": intake["opening_message"].strip()}]
    out = {"transcript": [("assistant", history[0]["content"])], "keyword_stop": None, "analysis": None,
           "analysis_md": "", "documents": {}, "doc_texts": {}, "error": None, "done": False}
    llm.CALLS.clear()
    message = tc["story"]
    for _ in range(MAX_TURNS):
        asked = next_field(case, intake)
        out["transcript"].append(("user", message))
        case["user_messages"].append(message)
        hit = check_message(message) if keyword_check_applies(case, intake) else None
        if hit:                                                      # same as the app: hard stop, no AI
            out["keyword_stop"] = hit
            out["transcript"].append(("assistant", f"⚖️ {hit['message']}"))
            break
        try:
            r = run_turn(case, history, message)
        except Exception as err:
            out["error"] = f"intake failed: {err}"
            break
        history += [{"role": "user", "content": message}, {"role": "assistant", "content": r["reply"]}]
        out["transcript"].append(("assistant", r["reply"]))
        time.sleep(sleep)
        if r["done"]:
            out["done"] = True
            break
        key = r["asked"]
        message = tc.get("answers", {}).get(key) or default_answer(case.get("language"))

    if out["done"]:
        res = analyse(case)
        out["analysis"] = res
        out["analysis_md"] = analysis_md(res)
        for d in drafting.available(case):
            out["documents"][d["id"]] = {"ok": d["ok"], "why_not": d["why_not"]}
            if d["ok"]:
                time.sleep(sleep)
                try:
                    doc = drafting.draft(case, d["id"])
                    out["doc_texts"][d["id"]] = doc
                except Exception as err:
                    out["documents"][d["id"]]["error"] = str(err)
    out["case"] = case
    out["stopped_early"] = any("Shukriya. Aapne jo bataya" in m or "outside what this assistant" in m or "दायरे से बाहर" in m
                               for r, m in out["transcript"] if r == "assistant")
    out["models_used"] = sorted(set(llm.CALLS))
    out["model_calls"] = len(llm.CALLS)
    return out


def checks(tc: dict, out: dict) -> list[tuple[str, bool, str]]:
    """Compare what happened with tc['expect']. Each: (check, passed, detail)."""
    exp, res = tc.get("expect", {}), []
    stops = [e for e in (out["analysis"] or {}).get("escalations", []) if e["stop"]]
    got_esc = out["keyword_stop"]["category"] if out["keyword_stop"] else ("stop" if stops else "none")
    if "escalation" in exp:
        res.append(("escalation", got_esc == exp["escalation"], f"expected {exp['escalation']}, got {got_esc}"))
    if exp.get("escalation", "none") == "none" and not out["done"]:
        res.append(("intake completed", False, out["error"] or "did not finish within the turn limit"))
    a = (out["analysis"] or {}).get("analysis") or {}
    non_stop = [e for e in (out["analysis"] or {}).get("escalations", []) if not e["stop"]]
    if "lawyer_flag" in exp:
        got = bool(non_stop) or bool(a.get("suggest_lawyer"))
        res.append(("lawyer flag", got == exp["lawyer_flag"], f"expected {exp['lawyer_flag']}, got {got}"))
    if "cites_any" in exp:
        cited = {i for p in a.get("points", []) for i in p["kb_ids"]} | {i for o in a.get("options", []) for i in o["kb_ids"]}
        cited |= {i for c in (out["analysis"] or {}).get("calcs", []) if c.get("display") for i in c.get("kb_ids", [])}
        hit = sorted(cited & set(exp["cites_any"]))
        res.append(("cites expected KB entry", bool(hit), f"found {hit or 'none'} of {exp['cites_any']}"))
    if "language" in exp:
        res.append(("language", out["case"].get("language") == exp["language"],
                    f"expected {exp['language']}, got {out['case'].get('language')}"))
    for doc_id, want in exp.get("documents", {}).items():
        d = out["documents"].get(doc_id)
        got = bool(d and d["ok"] and doc_id in out["doc_texts"])
        res.append((f"document {doc_id}", got == want, f"expected {'unlocked' if want else 'locked/absent'}, "
                    f"got {'unlocked' if got else 'locked/absent'}" + (f" ({'; '.join(d['why_not'])})" if d and d['why_not'] else "")))
    visible = out["analysis_md"] + "\n".join(t["text"] for t in out["doc_texts"].values()) + \
        "\n".join(m for r, m in out["transcript"] if r == "assistant")
    for s in exp.get("must_not_contain", []):
        res.append((f"no '{s}'", s.lower() not in visible.lower(), "found in output" if s.lower() in visible.lower() else "absent"))
    for s in exp.get("only_as_unverified", []):
        bad = [m.start() for m in re.finditer(re.escape(s), visible, re.IGNORECASE)
               if "not verified" not in visible[m.start(): m.start() + 80].lower()]
        res.append((f"'{s}' only as unverified", not bad,
                    "every mention is marked 'not verified'" if not bad else f"{len(bad)} unmarked mention(s)"))
    return res


def write_report(path: Path, tc: dict, out: dict, results: list, seconds: float) -> None:
    L = [f"# {tc['id']}", f"**Category:** {tc['category']}  ", f"**Description:** {tc['description']}  ",
         f"**Pack:** {tc['pack']}  ", f"**Run at:** {datetime.now().isoformat(timespec='seconds')}  ",
         f"**Models that answered:** {', '.join(out['models_used']) or 'none (no AI call)'} ({out['model_calls']} calls)  ",
         f"**Time:** {seconds:.1f} s", "", "> Unedited output of scripts/run_tests.py. Nothing below was changed by hand.", "",
         "## Automatic checks", "| Check | Result | Detail |", "|---|---|---|"]
    L += [f"| {n} | {'PASS' if ok else '**FAIL**'} | {d} |" for n, ok, d in results]
    L += ["", "## Conversation"]
    for role, msg in out["transcript"]:
        L += [f"**{'User' if role == 'user' else 'Bot'}:** {msg}", ""]
    L += ["## Case file (final)", "```json", json.dumps(out["case"], ensure_ascii=False, indent=1), "```"]
    if out["error"]:
        L += ["", f"**ERROR:** {out['error']}"]
    if out["analysis"]:
        L += ["", "## Answer shown to the user", "", out["analysis_md"], "",
              "## Safety checker log (items removed from the AI's draft)", "```json",
              json.dumps(out["analysis"].get("validator_log", []), ensure_ascii=False, indent=1), "```",
              "", "## Raw model JSON for the answer (before the safety checker)", "```json",
              json.dumps(out["analysis"].get("raw"), ensure_ascii=False, indent=1), "```"]
    for doc_id, info in out["documents"].items():
        L += ["", f"## Document: {doc_id}", f"Offered: {'yes' if info['ok'] else 'LOCKED - ' + '; '.join(info['why_not'])}"]
        if doc_id in out["doc_texts"]:
            d = out["doc_texts"][doc_id]
            L += [f"Drafting log: {d['log'] or 'AI paragraph accepted'}", "", "```text", d["text"], "```"]
    path.write_text("\n".join(L), encoding="utf-8")


def write_summary(run_dir: Path, rows: list, total_pass: int, total: int) -> None:
    summary = ["# Test run summary", f"Run at {datetime.now().isoformat(timespec='seconds')} - "
               f"{len(rows)} case runs, {total_pass}/{total} automatic checks passed.", "",
               "> Unedited. Each case's full output is in its own file in this folder.", "",
               "| Case | Category | Checks | Items stripped by safety checker | Model calls | Models | Failures |",
               "|---|---|---|---|---|---|---|"] + rows
    (run_dir / "summary.md").write_text("\n".join(summary), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", nargs="*", default=None)
    ap.add_argument("--repeat", type=int, default=1)
    ap.add_argument("--sleep", type=float, default=2.0)
    args = ap.parse_args()

    cases = yaml.safe_load((ROOT / "tests" / "cases.yaml").read_text(encoding="utf-8"))["cases"]
    if args.only:
        cases = [c for c in cases if any(c["id"].startswith(p) for p in args.only)]
    run_dir = ROOT / "raw_outputs" / f"run_{datetime.now().strftime('%Y%m%d_%H%M')}"
    run_dir.mkdir(parents=True, exist_ok=True)
    rows, total_pass, total = [], 0, 0
    for tc in cases:
        for r in range(1, args.repeat + 1):
            name = tc["id"] + (f"_r{r}" if args.repeat > 1 else "")
            print(f"--> {name} ...", flush=True)
            t0 = time.time()
            try:
                out = run_case(tc, args.sleep)
                res = checks(tc, out)
            except Exception as err:                       # F38: record the crash, keep going
                import traceback
                out = {"transcript": [], "keyword_stop": None, "analysis": None, "analysis_md": "", "documents": {},
                       "doc_texts": {}, "error": "CRASH: " + traceback.format_exc(), "done": False,
                       "case": {}, "models_used": sorted(set(llm.CALLS)), "model_calls": len(llm.CALLS)}
                res = [("ran without crashing", False, f"{type(err).__name__}: {err}")]
            write_report(run_dir / f"{name}.md", tc, out, res, time.time() - t0)
            passed = sum(ok for _, ok, _ in res)
            total_pass += passed; total += len(res)
            stripped = len((out["analysis"] or {}).get("validator_log", []))
            fails = "; ".join(f"{n}: {d}" for n, ok, d in res if not ok)
            rows.append(f"| {name} | {tc['category']} | {passed}/{len(res)} | {stripped} | {out['model_calls']} | "
                        f"{', '.join(out['models_used']) or '-'} | {fails or '-'} |")
            print(f"    {passed}/{len(res)} checks passed, {stripped} item(s) stripped, {out['model_calls']} model calls"
                  + (f"  FAILED: {fails}" if fails else ""))
            write_summary(run_dir, rows, total_pass, total)        # after every case, so a crash loses nothing
    write_summary(run_dir, rows, total_pass, total)
    print(f"\nSaved to {run_dir}\n{total_pass}/{total} automatic checks passed")


if __name__ == "__main__":
    main()
