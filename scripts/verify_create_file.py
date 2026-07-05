#!/usr/bin/env python3
"""Host-side verifier for the create-file test (Test 3).

Checks that cases/create_file/AGENT_CREATED_THIS_FILE.txt exists and
contains exactly the expected sentence. Exits 0 on pass, nonzero on fail.
Standard library only.
"""

import sys
from pathlib import Path

EXPECTED = "Agent file creation test passed."


def main():
    repo_root = Path(__file__).resolve().parent.parent
    target = repo_root / "cases" / "create_file" / "AGENT_CREATED_THIS_FILE.txt"

    if not target.is_file():
        print(f"FAIL: file not found: {target}")
        print("If the agent claimed success, suspect a workspace or path failure.")
        return 1

    try:
        content = target.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"FAIL: file exists but could not be read: {exc}")
        print("Suspect a permission failure.")
        return 1

    if content.strip() == EXPECTED:
        print(f"PASS: {target} exists with the exact expected content")
        return 0

    print("FAIL: file exists but content does not match")
    print(f"  expected: {EXPECTED!r}")
    print(f"  got:      {content.strip()!r}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
