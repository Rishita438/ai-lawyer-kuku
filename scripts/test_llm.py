"""
test_llm.py - checks that your API key and model work.

Run:   py scripts\test_llm.py               -> tests the main model (config.yaml: model)
       py scripts\test_llm.py --fallback    -> tests ONLY the fallback model (config.yaml: fallback)
       py scripts\test_llm.py --list        -> lists model names the main key can use
       py scripts\test_llm.py --list --fallback -> lists model names the fallback key can use
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))   # so "import app" works
from app import llm

use_fallback = "--fallback" in sys.argv
cfg = llm.CONFIG["fallback"] if use_fallback else llm.CONFIG
client = llm._client(cfg)

if "--list" in sys.argv:
    for m in client.models.list():
        print(m.id)
else:
    print("Testing:", "FALLBACK" if use_fallback else "MAIN", "->", cfg["model"])
    resp = client.chat.completions.create(
        model=cfg["model"], temperature=0.2,
        messages=[{"role": "user", "content": "Reply with exactly: OK, connected."}])
    print("Reply:", resp.choices[0].message.content)
    if not use_fallback:
        print("JSON :", llm.chat_json([{"role": "user", "content":
              'Reply with only this JSON: {"status": "ok", "language": "Hinglish"}'}]))
