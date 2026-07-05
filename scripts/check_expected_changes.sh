#!/bin/sh
# Checks that the agent only changed what it was supposed to change.
# Run from the repo root, after a test, with the expected paths as arguments:
#
#   sh scripts/check_expected_changes.sh cases/path_report/PATH_REPORT.txt
#
# Any modified or untracked path NOT listed as an argument is flagged.
# Exits 0 if all changes are expected, nonzero otherwise.

echo "== git status --short =="
git status --short
echo

STATUS=$(git status --short)

if [ -z "$STATUS" ]; then
    echo "PASS: working tree is clean (no modified or untracked files)"
    exit 0
fi

if [ $# -eq 0 ]; then
    echo "WARNING: there are modified or untracked files, and no expected paths were given."
    echo "Usage: sh scripts/check_expected_changes.sh <expected-path> [more-paths...]"
    echo "FAIL: unexpected changes present"
    exit 1
fi

# git status --short prints "XY path"; the path starts at column 4.
UNEXPECTED=$(
    echo "$STATUS" | cut -c4- | while read -r changed; do
        ok=0
        for expected in "$@"; do
            if [ "$changed" = "$expected" ]; then
                ok=1
                break
            fi
        done
        if [ "$ok" -eq 0 ]; then
            echo "$changed"
        fi
    done
)

if [ -n "$UNEXPECTED" ]; then
    echo "WARNING: the agent touched paths outside the expected list:"
    echo "$UNEXPECTED" | while read -r path; do
        echo "  UNEXPECTED: $path"
    done
    echo
    echo "FAIL: unexpected modified or untracked files present"
    exit 1
fi

echo "PASS: all changed/untracked paths are within the expected list:"
for expected in "$@"; do
    echo "  $expected"
done
exit 0
