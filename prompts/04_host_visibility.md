# Test 4: Host Visibility

Copy the prompt below into the agent.

---

Create a new file at exactly this path, relative to the project root:

```
cases/host_visibility/HOST_VISIBLE_AGENT_FILE.txt
```

The file must contain the following diagnostic information, one item per line:

1. Your current working directory, exactly as reported by your environment (for example, the output of `pwd`).
2. The absolute path where you created this file, as you see it.
3. One sentence confirming that you created this file as part of the host visibility test.

Example format:

```
CWD: /path/agent/sees
CREATED_AT: /path/agent/sees/cases/host_visibility/HOST_VISIBLE_AGENT_FILE.txt
CONFIRMATION: I created this file for the host visibility test.
```

Rules:

- Do not modify any existing file.
- Report the paths exactly as your tools show them, even if they look unusual (for example `/workspace/...`). Do not guess what the host path might be.

After this test, a human will check from the host machine whether this file is actually visible. The paths you report will be compared against the host's real project path.
