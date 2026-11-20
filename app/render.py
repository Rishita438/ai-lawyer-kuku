"""
render.py - turns the analysis into what the user reads. Plain code, no AI.

Citations are built HERE from the KB (act, section, title, link, verified date) -
the model only ever supplied ids. So a citation on screen cannot be invented.
"""
import re
from html import escape


def _m(text) -> str:
    """Escape model-written text (it is shown with HTML enabled for the citation styling)."""
    return escape(str(text or ""), quote=False)


def citation(kb: dict, kb_id: str) -> str:
    e = kb["entries"][kb_id]
    if e.get("status") == "reviewed":
        return f"📝 *{e['title']}* — general practice, not a legal rule (reviewed {e.get('last_verified')})"
    where = f"{e['act']}, {_sec(e)}" if e.get("type") == "law" else e.get("source_name", "")
    link = f" — [source]({e['source_url']})" if e.get("source_url") else ""
    badge = "✅ verified" if e.get("status") == "verified" else "⚠️ UNVERIFIED"
    return f"📘 **{where}**: {e['title']}{link} ({badge} {e.get('last_verified') or ''})"


def _sec(e: dict) -> str:
    s = str(e.get("section", ""))
    return s if s.lower().startswith(("rule", "sched")) else f"s. {s}"


def computed_facts_md(calcs: list[dict], kb: dict) -> str:
    """The "Key facts" box: each pack calculator supplies its own display line. No model involved."""
    lines = [c["display"] for c in calcs if c.get("display")]
    ids = sorted({i for c in calcs if c.get("display") for i in c.get("kb_ids", []) if i in kb["entries"]})
    if ids:
        lines.append("<small>Based on: " + "; ".join(citation(kb, i) for i in ids) + "</small>")
    return "\n\n".join(lines)


def analysis_md(result: dict) -> str:
    kb, a = result["kb"], result["analysis"]
    out = ["### Where you stand"]

    stops = [e for e in result["escalations"] if e["stop"]]
    if stops:
        out.append("🛑 **Please consult a lawyer.** " + " ".join(e["reason"] for e in stops))
        out.append("You may be eligible for free legal help: District Legal Services Authority, "
                   "or the NALSA helpline **15100**.")
        out.append(f"---\n<small>Knowledge base last verified: {kb['last_verified']}. "
                   "This is general information, not legal advice.</small>")
        return "\n\n".join(out)

    if result.get("error"):
        out.append(f"⚠️ {result['error']}")
    elif a:
        out.append(_m(a["summary"]))
        for p in a["points"]:
            refs = "<br>".join(citation(kb, i) for i in p["kb_ids"])
            out.append(f"- {_m(p['text'])}<br><small>{refs}</small>")

    facts_box = computed_facts_md(result["calcs"], kb)
    if facts_box:
        out.append("#### Key facts (calculated by the app, not the AI)")
        out.append(facts_box)

    if a and a["options"]:
        out.append("### Your options")
        for n, o in enumerate(a["options"], 1):
            block = f"**{n}. {_m(o['title'])}** — {_m(o['why'])}"
            block += "".join(f"\n   - {_m(s)}" for s in o["steps"])
            if o["kb_ids"]:
                block += "\n\n   <small>" + "<br>".join(citation(kb, i) for i in o["kb_ids"]) + "</small>"
            out.append(block)

    lawyer = list(dict.fromkeys(e["reason"] for e in result["escalations"]))       # F50: no duplicate bullets
    if a and a.get("suggest_lawyer") and a.get("lawyer_reason"):
        mine = _m(a["lawyer_reason"])
        norm = lambda t: re.sub(r"\W+", " ", t.lower()).strip()
        if not any(norm(mine)[:60] in norm(r) or norm(r)[:60] in norm(mine) for r in lawyer):
            lawyer.append(mine)
    if lawyer:
        out.append("### ⚖️ When to get a real lawyer\n" + "\n".join(f"- {r}" for r in lawyer)
                   + "\n- Free legal help may be available: District Legal Services Authority / NALSA helpline **15100**.")

    if a and a["uncertainties"]:
        out.append("### What I'm not sure about\n" + "\n".join(f"- {_m(u)}" for u in a["uncertainties"]))

    stripped = len(result.get("validator_log", []))
    note = f" The safety checker removed {stripped} unverified item(s) from the AI's draft." if stripped else ""
    out.append(f"---\n<small>Knowledge base last verified: {kb['last_verified']}. Only verified sources are "
               f"cited.{note} This is general information, not legal advice.</small>")
    return "\n\n".join(out)
