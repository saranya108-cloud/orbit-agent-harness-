# Path Report Test Case

This folder is the target of the path report test (Test 6).

The agent is asked to create `PATH_REPORT.txt` here, containing labeled fields for its working directory (`PWD:`), the repo root it sees (`REPO_ROOT:`), the absolute path of the created file (`CREATED_FILE_PATH:`), a listing of the project root (`DIRECTORY_LISTING:`), and a `CONFIRMATION:` line.

Verify from the host shell:

```sh
python3 scripts/verify_path_report.py
```

## Why this matters

When a Dockerized or sandboxed agent writes files the host cannot find, the agent-reported paths in this report are the main diagnostic clue. Comparing `PWD:` and `REPO_ROOT:` against the host's real project path tells you whether the agent is in a bind mount (paths differ but files appear), a copy or overlay (files never appear), or simply the wrong directory.

Delete `PATH_REPORT.txt` to reset this test.
