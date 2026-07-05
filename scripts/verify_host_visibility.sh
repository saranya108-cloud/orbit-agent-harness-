#!/bin/sh
# Host-side verifier for the host visibility test (Test 4).
# Run this from the HOST machine, not from inside the agent or its container.
# Exits 0 if the agent-created file is visible, nonzero if it is missing.

REPO_ROOT=$(dirname "$0")/..
TARGET="$REPO_ROOT/cases/host_visibility/HOST_VISIBLE_AGENT_FILE.txt"

echo "== Host working directory =="
pwd
echo

echo "== Files changed in the last 10 minutes under the repo =="
find "$REPO_ROOT" -type f -mmin -10 -not -path "*/.git/*" 2>/dev/null
echo

echo "== Checking for $TARGET =="
if [ -f "$TARGET" ]; then
    echo "PASS: file is visible from the host"
    echo
    echo "== File contents (agent-reported paths) =="
    cat "$TARGET"
    echo
    echo "Compare the agent-reported paths above with the host path of this repo."
    echo "If they differ, record the mapping in your result note."
    exit 0
else
    echo "FAIL: file not visible from the host"
    echo "If the agent claimed success, the file likely landed in a child"
    echo "container, Docker volume, hidden sandbox, or wrong directory."
    echo "Classify as workspace failure or path confusion."
    exit 1
fi
