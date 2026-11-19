"""
test_llm.py - checks that your API key and model work.

Run:   py scripts\test_llm.py          -> sends one test message
       py scripts\test_llm.py --list   -> lists model names your key can use
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))   # so "import app" works
from app import llm

if "--list" in sys.argv:
    client = llm._client(llm.CONFIG)
    for m in client.models.list():
        print(m.id)
else:
    print("Model:", llm.CONFIG["model"])
    print("Reply:", llm.chat([{"role": "user", "content": "Reply with exactly: OK, connected."}]))
    print("JSON :", llm.chat_json([{"role": "user", "content":
          'Reply with only this JSON: {"status": "ok", "language": "Hinglish"}'}]))
