# Host-Visibility Test Case

This folder is the target of the host visibility test (Test 4), the most important test in this harness.

## What happens

The agent is asked to create `HOST_VISIBLE_AGENT_FILE.txt` in this folder, containing:

- the working directory the agent believes it is in
- the absolute path where the agent believes it created the file
- a one-sentence confirmation

Then a human verifies **from the host machine**:

```sh
sh scripts/verify_host_visibility.sh
```

## Why this matters

Dockerized and nested-sandbox agent runtimes can appear to succeed while writing files the host never sees. Common causes:

- The agent runs in a child container whose filesystem is not the host's.
- Files land in a Docker named volume instead of the bind-mounted project folder.
- The agent's `/workspace` is a copy or overlay, not a mount of the host project.
- The agent's working directory is simply not the project folder.

The agent will always report success in these cases — from inside its sandbox, the file really does exist. Only host-side verification catches the discrepancy.

## Reading the result

- File visible on host, paths match: **pass**.
- File visible, but the agent-reported paths differ from the host path: pass, but record the mapping (useful for diagnosing the runtime's mount setup).
- Agent reports success, file not visible on host: **workspace failure** or **path confusion**. The agent-reported paths inside the file (if you can retrieve it from the sandbox) tell you where the writes are actually going.

Delete `HOST_VISIBLE_AGENT_FILE.txt` to reset this test.
