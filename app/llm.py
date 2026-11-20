"""
llm.py - the ONLY place in the app that talks to an AI model.

Every other file calls `chat()` or `chat_json()`. Because all providers here speak the
same OpenAI-compatible format, swapping Gemini -> Groq -> GPT -> Claude is a change in
config.yaml, not in code. (Decision D3 / ADR-010.)
"""
import json
import os
import re
import time
from pathlib import Path

import yaml
from dotenv import load_dotenv
from openai import OpenAI

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")                       # reads API keys from .env into the environment
CONFIG = yaml.safe_load((ROOT / "config.yaml").read_text(encoding="utf-8"))
CALLS: list[str] = []          # which model answered each call (main or fallback) - read by the test harness


def _client(cfg: dict) -> OpenAI:
    """Build a client for one provider from its config block."""
    key = os.getenv(cfg["api_key_env"])
    if not key:
        raise RuntimeError(f"Missing API key: set {cfg['api_key_env']} in your .env file")
    # timeout: give up after N seconds instead of hanging (the default is 10 minutes!)
    # max_retries=1: one quick retry, then move on to the fallback model
    return OpenAI(base_url=cfg["base_url"], api_key=key,
                  timeout=CONFIG.get("timeout_seconds", 30), max_retries=1)


# F54: when a model says "rate limited", remember it for a while instead of hitting it on every call.
_COOLDOWN: dict[str, float] = {}       # model name -> time.time() until which we skip it
MAX_WAIT_SECONDS = 65                  # a per-minute limit ("try again in 40s") is worth waiting for


def _retry_after(err: Exception) -> float | None:
    """How long the provider asks us to wait. Groq says "try again in 0.7s";
    Gemini says "Please retry in 41.2s" or "retryDelay": "41s" (F60: the old pattern missed Gemini's wording,
    so a one-minute Gemini limit was treated as "quota used up" and the model was skipped for 5 minutes)."""
    m = re.search(r"(?:try again|retry) in ([\d.]+)\s*(ms|s)\b", str(err)) or \
        re.search(r"retryDelay\W+([\d.]+)(s)", str(err))
    if not m:
        return None
    return float(m.group(1)) / (1000 if m.group(2) == "ms" else 1)


def chat(messages: list[dict], temperature: float | None = None) -> str:
    """Send a list of {"role": ..., "content": ...} messages; return the reply text.
    Tries the main model first, then the fallback model. Rate limits (F54):
      - "try again in 0.7s" (per-minute limit) -> wait that long and retry the same model, up to 3 times
      - a 429 with no wait time (e.g. daily quota used up) -> skip that model for 5 minutes"""
    temp = CONFIG.get("temperature", 0.2) if temperature is None else temperature
    attempts = [CONFIG] + ([CONFIG["fallback"]] if CONFIG.get("fallback", {}).get("model") else [])
    attempts = [c for i, c in enumerate(attempts) if i == 0 or os.getenv(c["api_key_env"])]
    usable = [c for c in attempts if _COOLDOWN.get(c["model"], 0) <= time.time()] or attempts
    last_error = None
    for cfg in usable:
        for _ in range(3):
            try:
                resp = _client(cfg).chat.completions.create(
                    model=cfg["model"], messages=messages, temperature=temp)
                CALLS.append(cfg["model"])
                return resp.choices[0].message.content or ""
            except Exception as err:            # rate limit, outage, missing key...
                last_error, text = err, str(err)
                if "429" in text:
                    wait = _retry_after(err)
                    if wait is not None and wait <= MAX_WAIT_SECONDS:
                        print(f"[llm] {cfg['model']} rate-limited, waiting {wait:.1f}s and retrying")
                        time.sleep(wait + 0.5)
                        continue
                    _COOLDOWN[cfg["model"]] = time.time() + 300
                    print(f"[llm] {cfg['model']} quota used up -> skipping it for 5 minutes")
                    break
                hint = ""
                if "404" in text:
                    hint = " -> model name not found (renamed or shut down?). Run: py scripts\\test_llm.py --list"
                elif "503" in text or "500" in text:
                    hint = " -> provider's servers busy/down. Try a -lite model or set up the fallback."
                elif "401" in text or "403" in text:
                    hint = " -> API key rejected. Check the key in .env."
                print(f"[llm] {cfg['model']} failed: {err}{hint}")
                break
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
