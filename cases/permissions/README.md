# Permissions Observation Test Case

This folder is the target of the permissions observation test (Test 8).

The agent is asked to create `PERMISSION_REPORT.txt` here, recording its working directory, the user it runs as (`whoami` / `id`), `ls -la` listings of the repo root and `cases/`, and a `CONFIRMATION:` line.

Verify from the host shell:

```sh
sh scripts/verify_permissions_observation.sh
```

## Why this matters

Containerized agents often run as a different user than the host user — commonly root. That can produce files the host user cannot edit or delete, or reveal that the agent sees different ownership than the host does. After the test, compare:

- the user in the agent's `WHOAMI_OR_ID:` section against your host `id`
- the ownership shown in the agent's listings against the host's `ls -la cases/permissions`
- the ownership of `PERMISSION_REPORT.txt` itself on the host

A file owned by root in your project folder is a permission failure worth recording even if the test otherwise passes.

Delete `PERMISSION_REPORT.txt` to reset this test (you may need elevated rights if the agent created it as another user — that is itself a finding).
