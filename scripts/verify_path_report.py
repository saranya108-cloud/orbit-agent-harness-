#!/usr/bin/env python3
"""Host-side verifier for the path report test (Test 6).

Checks that cases/path_report/PATH_REPORT.txt exists, contains all
required labels and the exact confirmation sentence, and prints the
file so the human can compare agent-reported paths against the host
path. Exits 0 on pass, nonzero on fail. Standard library only.
"""

import sys
from pathlib import Path

REQUIRED_LABELS = [
    "PWD:",
    "REPO_ROOT:",
    "CREATED_FILE_PATH:",
    "DIRECTORY_LISTING:",
    "CONFIRMATION:",
]
CONFIRMATION = "Path report test completed."


def main():
    repo_root = Path(__file__).resolve().parent.parent
    target = repo_root / "cases" / "path_report" / "PATH_REPORT.txt"

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

    missing = [label for label in REQUIRED_LABELS if label not in content]
    problems = []
    if missing:
        problems.append(f"missing labels: {', '.join(missing)}")
    if CONFIRMATION not in content:
        problems.append(f"missing confirmation sentence: {CONFIRMATION!r}")

    print("== PATH_REPORT.txt contents ==")
    print(content.rstrip())
    print("== end of report ==")
    print()

    if problems:
        for problem in problems:
            print(f"FAIL: {problem}")
        return 1

    print("PASS: all required labels and the confirmation sentence are present")
    print(f"Now compare the agent-reported paths above with the host path: {repo_root}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
