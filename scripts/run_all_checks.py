"""
run_all_checks.py - runs every OFFLINE check in one go (no API key needed) and saves the output.

Run:  py scripts\\run_all_checks.py
Then, for the real-model test cases:  py scripts\\run_tests.py
"""
import subprocess
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.stdout.reconfigure(encoding="utf-8")
SCRIPTS = ["check_kb.py", "test_stage4.py", "test_stage5.py", "test_packs.py"]

log, ok_all = [f"Offline checks - {datetime.now().isoformat(timespec='seconds')}\n"], True
for name in SCRIPTS:
    r = subprocess.run([sys.executable, str(ROOT / "scripts" / name)], capture_output=True, text=True,
                       encoding="utf-8", env={**__import__("os").environ, "PYTHONIOENCODING": "utf-8"})
    last = (r.stdout.strip().splitlines() or ["(no output)"])[-1]
    status = "OK  " if r.returncode == 0 else "FAIL"
    ok_all &= r.returncode == 0
    print(f"{status} {name:<18} {last}")
    log += [f"\n===== {name} ({status.strip()}) =====\n", r.stdout, r.stderr]

out = ROOT / "raw_outputs" / f"offline_checks_{datetime.now().strftime('%Y%m%d_%H%M')}.txt"
out.parent.mkdir(exist_ok=True)
out.write_text("".join(log), encoding="utf-8")
print(f"\n{'ALL OFFLINE CHECKS PASSED' if ok_all else 'SOME CHECKS FAILED'} - full output saved to {out.relative_to(ROOT)}")
sys.exit(0 if ok_all else 1)
