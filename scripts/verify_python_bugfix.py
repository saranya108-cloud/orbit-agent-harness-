#!/usr/bin/env python3
"""Host-side verifier for the Python bugfix test (Test 2).

Runs cases/python_bugfix/score.py and checks that it prints 90.0.
Exits 0 on pass, nonzero on fail. Standard library only.
"""

import subprocess
import sys
from pathlib import Path

EXPECTED = "90.0"


def main():
    repo_root = Path(__file__).resolve().parent.parent
    script = repo_root / "cases" / "python_bugfix" / "score.py"

    if not script.is_file():
        print(f"FAIL: script not found: {script}")
        return 1

    try:
        proc = subprocess.run(
            [sys.executable, str(script)],
            capture_output=True,
            text=True,
            timeout=30,
        )
    except subprocess.TimeoutExpired:
        print("FAIL: score.py timed out after 30 seconds")
        return 1

    output = proc.stdout.strip()

    if proc.returncode != 0:
        print("FAIL: score.py exited with an error (bug likely not fixed yet)")
        print("--- stderr ---")
        print(proc.stderr.strip())
        return 1

    if output == EXPECTED:
        print(f"PASS: score.py printed {output!r} as expected")
        return 0

    print(f"FAIL: expected output {EXPECTED!r}, got {output!r}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
