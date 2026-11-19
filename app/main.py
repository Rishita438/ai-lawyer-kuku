"""
main.py - the Streamlit web app.   Run:  streamlit run app/main.py

Stage 3 version: collects the facts of a consumer problem and shows the live case file.
Legal analysis, citations and drafting arrive in Stages 4-5.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))                    # so "from app import ..." works under streamlit

import streamlit as st
import yaml

from app import llm
from app.case_file import new_case, load_intake, missing, can_draft, UNKNOWN
from app.intake import run_turn

PACKS_READY = ["consumer"]                       # packs that have an intake.yaml so far

st.set_page_config(page_title="Nyaya Saathi - AI legal helper", page_icon="⚖️", layout="wide")


def kb_last_verified(pack: str) -> str:
    data = yaml.safe_load((ROOT / "packs" / pack / "kb.yaml").read_text(encoding="utf-8"))
    return str(data.get("kb_last_verified") or "NOT VERIFIED")


def reset(pack: str):
    st.session_state.case = new_case(pack)
    st.session_state.history = [{"role": "assistant",
                                 "content": load_intake(pack)["opening_message"].strip()}]
    st.session_state.done = False


# ---------- sidebar ----------
with st.sidebar:
    st.header("Settings")
    pack = st.selectbox("Problem type", PACKS_READY,
                        format_func=lambda p: load_intake(p)["title"])
    if st.button("Start over") or "case" not in st.session_state or st.session_state.case["pack"] != pack:
        reset(pack)
    st.caption(f"Model: `{llm.CONFIG['model']}` (set in config.yaml)")
    st.caption(f"Knowledge base last verified: **{kb_last_verified(pack)}**")
    st.caption("Coming next: deposit, salary and notice explainer.")

# ---------- header ----------
st.title("⚖️ Nyaya Saathi")
st.warning("This is an AI assistant, not a lawyer. It gives general information from a small, "
           "verified knowledge base and will tell you when you need a real lawyer. "
           "Please don't share Aadhaar, bank or card numbers.", icon="⚠️")

chat_col, case_col = st.columns([2, 1])

# ---------- chat ----------
with chat_col:
    for msg in st.session_state.history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    user_text = st.chat_input("Type your message (English / हिंदी / Hinglish)")
    if user_text:
        st.session_state.history.append({"role": "user", "content": user_text})
        with st.chat_message("user"):
            st.markdown(user_text)
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    result = run_turn(st.session_state.case, st.session_state.history[:-1], user_text)
                    reply = result["reply"]
                    st.session_state.done = result["done"]
                except Exception as err:          # model down, bad JSON twice, etc.
                    reply = f"Sorry, something went wrong talking to the AI model ({err}). Please try again."
            st.markdown(reply)
        st.session_state.history.append({"role": "assistant", "content": reply})
        st.rerun()

# ---------- live case file ----------
with case_col:
    st.subheader("📁 Your case file")
    intake = load_intake(pack)
    for f in intake["fields"]:
        value = st.session_state.case["facts"].get(f["key"])
        label = f["key"].replace("_", " ").capitalize()
        if value is None:
            st.markdown(f"❓ **{label}:** _not yet_")
        elif value == UNKNOWN:
            st.markdown(f"➖ **{label}:** you don't know")
        else:
            if isinstance(value, bool):
                shown = "Yes" if value else "No"
            elif isinstance(value, list):
                shown = ", ".join(value)
            else:
                shown = value
            st.markdown(f"✅ **{label}:** {shown}")

    still_needed = len(missing(st.session_state.case, intake))
    st.divider()
    if st.session_state.done:
        st.success("Intake complete.")
    else:
        st.info(f"{still_needed} question(s) left.")
    st.caption("Ready to draft a complaint: " + ("yes" if can_draft(st.session_state.case, intake) else "not yet"))
