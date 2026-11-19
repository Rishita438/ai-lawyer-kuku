"""
llm.py - the ONLY place in the app that talks to an AI model.

Every other file calls `chat()` or `chat_json()`. Because all providers here speak the
same OpenAI-compatible format, swapping Gemini -> Groq -> GPT -> Claude is a change in
config.yaml, not in code. (Decision D3 / ADR-010.)
"""
import json
import os
import re
from pathlib import Path

import yaml
from dotenv import load_dotenv
from openai import OpenAI

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")                       # reads API keys from .env into the environment
CONFIG = yaml.safe_load((ROOT / "config.yaml").read_text(encoding="utf-8"))


def _client(cfg: dict) -> OpenAI:
    """Build a client for one provider from its config block."""
    key = os.getenv(cfg["api_key_env"])
    if not key:
        raise RuntimeError(f"Missing API key: set {cfg['api_key_env']} in your .env file")
    # timeout: give up after N seconds instead of hanging (the default is 10 minutes!)
    # max_retries=1: one quick retry, then move on to the fallback model
    return OpenAI(base_url=cfg["base_url"], api_key=key,
                  timeout=CONFIG.get("timeout_seconds", 30), max_retries=1)


def chat(messages: list[dict], temperature: float | None = None) -> str:
    """Send a list of {"role": ..., "content": ...} messages; return the reply text.
    Tries the main model first, then the fallback model if one is configured."""
    temp = CONFIG.get("temperature", 0.2) if temperature is None else temperature
    attempts = [CONFIG] + ([CONFIG["fallback"]] if CONFIG.get("fallback", {}).get("model") else [])
    last_error = None
    for i, cfg in enumerate(attempts):
        if i > 0 and not os.getenv(cfg["api_key_env"]):
            print(f"[llm] fallback {cfg['model']} skipped: no {cfg['api_key_env']} in .env")
            continue
        try:
            resp = _client(cfg).chat.completions.create(
                model=cfg["model"], messages=messages, temperature=temp)
            return resp.choices[0].message.content or ""
        except Exception as err:            # rate limit, outage, missing key...
            last_error = err
            hint = ""
            if "404" in str(err):
                hint = " -> model name not found (renamed or shut down?). Run: py scripts\\test_llm.py --list"
            elif "429" in str(err):
                hint = " -> rate limit / free-tier quota hit. Wait a minute or use the fallback."
            elif "503" in str(err) or "500" in str(err):
                hint = " -> provider's servers busy/down. Try a -lite model or set up the fallback."
            elif "401" in str(err) or "403" in str(err):
                hint = " -> API key rejected. Check the key in .env."
            print(f"[llm] {cfg['model']} failed: {err}{hint}")
    raise RuntimeError(f"All models failed. Last error: {last_error}")


def parse_json(text: str) -> dict:
    """Models often wrap JSON in ```json fences or add a sentence around it.
    Pull out the first {...} block and parse it. Raises ValueError if there is none."""
    text = re.sub(r"```(?:json)?", "", text).strip()
    start, end = text.find("{"), text.rfind("}")
    if start == -1 or end == -1:
        raise ValueError(f"No JSON object in model reply: {text[:200]}")
    return json.loads(text[start:end + 1])


def chat_json(messages: list[dict]) -> dict:
    """Like chat(), but expects a JSON object back. Retries once if the JSON is broken."""
    reply = chat(messages)
    try:
        return parse_json(reply)
    except (ValueError, json.JSONDecodeError):
        retry = messages + [{"role": "assistant", "content": reply},
                            {"role": "user", "content": "That was not valid JSON. Reply with ONLY the JSON object."}]
        return parse_json(chat(retry))
