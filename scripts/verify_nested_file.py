#!/usr/bin/env python3
"""Host-side verifier for the nested file test (Test 7).

Checks that cases/nested/subdir/NESTED_AGENT_FILE.txt exists and
contains exactly the expected sentence. If the file is missing, also
looks for strays with the same name elsewhere in the repo, which
indicates path confusion. Exits 0 on pass, nonzero on fail.
Standard library only.
"""

import sys
from pathlib import Path

EXPECTED = "Nested file creation test passed."
FILENAME = "NESTED_AGENT_FILE.txt"


def main():
    repo_root = Path(__file__).resolve().parent.parent
    target = repo_root / "cases" / "nested" / "subdir" / FILENAME

    if not target.is_file():
        print(f"FAIL: file not found: {target}")
        strays = [
            p for p in repo_root.rglob(FILENAME)
            if ".git" not in p.parts and p != target
        ]
        if strays:
            print("Found same-named file(s) at the wrong location (path confusion):")
            for stray in strays:
                print(f"  {stray}")
        else:
            print("No stray copies found in the repo either.")
            print("If the agent claimed success, suspect a workspace failure.")
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
