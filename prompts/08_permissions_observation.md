# Test 8: Permissions Observation

Copy the prompt below into the agent. This test records what user the agent runs as and what it can see, so the host can spot ownership and permission mismatches (for example, files created as root inside a container).

---

Create a new file at exactly this path, relative to the project root:

```
cases/permissions/PERMISSION_REPORT.txt
```

The file must contain the following labeled sections, in this order:

```
PWD: <your current working directory, exactly as your tools report it>
WHOAMI_OR_ID: <the output of `whoami` or `id`, whichever your environment provides>
REPO_ROOT_LISTING: <the output of `ls -la` on the project root folder>
CASES_LISTING: <the output of `ls -la` on the cases/ folder>
CONFIRMATION: Permissions observation test completed.
```

The CONFIRMATION line must contain exactly this sentence:

```
Permissions observation test completed.
```

Rules:

- Only run read-only commands (`pwd`, `whoami`, `id`, `ls -la`). Do not run anything that modifies the system.
- Report the output exactly as you see it, even if the user or paths look unusual.
- Do not modify any existing file.
- Do not create any other file.

After this test, a human will compare the user and file ownership you report against what the host machine sees.
