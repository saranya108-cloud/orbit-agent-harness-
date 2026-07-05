#!/bin/sh
# Host-side verifier for the permissions observation test (Test 8).
# Run this from the HOST machine, not from inside the agent or its container.
# Exits 0 if the report exists and contains the confirmation sentence,
# nonzero otherwise.

REPO_ROOT=$(dirname "$0")/..
TARGET="$REPO_ROOT/cases/permissions/PERMISSION_REPORT.txt"
CONFIRMATION="Permissions observation test completed."

echo "== Host working directory =="
pwd
echo

echo "== Host user =="
id
echo

echo "== Host view of cases/permissions =="
ls -la "$REPO_ROOT/cases/permissions"
echo

echo "== Checking for $TARGET =="
if [ ! -f "$TARGET" ]; then
    echo "FAIL: PERMISSION_REPORT.txt not visible from the host"
    echo "If the agent claimed success, classify as workspace failure or path confusion."
    exit 1
fi

echo "== Report contents (agent-reported user and listings) =="
cat "$TARGET"
echo

if grep -q "$CONFIRMATION" "$TARGET"; then
    echo "PASS: report exists and contains the confirmation sentence"
    echo
    echo "Now compare by hand:"
    echo "  - agent WHOAMI_OR_ID vs host id above"
    echo "  - agent listings vs host ls -la above"
    echo "  - owner of PERMISSION_REPORT.txt in the host listing"
    exit 0
else
    echo "FAIL: report exists but the confirmation sentence is missing"
    echo "Expected: $CONFIRMATION"
    exit 1
fi
