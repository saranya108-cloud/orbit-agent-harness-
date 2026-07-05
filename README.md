# Orbit Agent Harness

A small, repeatable test kit for determining whether an AI agent runtime can read files, edit files, create files, run basic commands, and leave results visible in the expected host project folder.

**Status: experimental.** This harness is intended for local AI lab testing and practical workflow validation. It is not a formal benchmark.

## Purpose

The goal of this repository is to separate model quality problems from agent runtime problems.

A model may be smart enough to solve a task, but the agent runtime may still fail because of:

- wrong working directory
- hidden sandbox storage
- Docker bind mount confusion
- Docker volume behavior
- child container workspace mapping
- file permission issues
- missing command execution tools
- path mismatch between the agent and the host machine

This harness helps answer the practical question:

> Can this agent actually read, edit, create, and leave files where the host machine can see them?

## Core Principle

**Do not blame the model until the runtime has proven it can access the correct workspace.**

If an agent appears to solve a task but the host machine cannot see the changed file, the problem is probably not the model. It is likely a runtime, workspace, mount, path, or permission issue.

## What This Tests

This harness is focused on runtime behavior, not model intelligence.

It tests whether an agent can:

1. Read a file in the expected project folder.
2. Edit a file in the expected project folder.
3. Create a new file.
4. Run a simple verification command.
5. Leave edited or created files visible to the host shell.
6. Avoid unsafe or destructive commands.
7. Explain what it changed.

## What This Does Not Test

This harness does not attempt to measure:

- broad reasoning ability
- coding benchmark performance
- long-context quality
- writing style
- model personality
- tool ecosystem quality
- production readiness

Those may matter later. This repository is only for answering the basic runtime question: **did the agent touch the right files in the right place?**

## Intended Runtimes

Use this repository when testing agent runtimes such as:

- Codex
- OpenClaw
- Hermes Agent
- Ollama-backed agents
- Dockerized agent runtimes
- VM-based agent workflows
- local model workflows

Each runtime should be tested in a disposable clone or temporary working folder.

## Repository Structure

```
orbit-agent-harness/
├── README.md
├── runbook.md
├── prompts/                  # copy-paste prompts, one per test
│   ├── 01_read_only.md
│   ├── 02_python_bugfix.md
│   ├── 03_create_file.md
│   ├── 04_host_visibility.md
│   ├── 05_shutdown_trap.md
│   ├── 06_path_report.md
│   ├── 07_nested_file.md
│   └── 08_permissions_observation.md
├── cases/                    # the files the agent must touch
│   ├── read_only/
│   ├── python_bugfix/
│   ├── create_file/
│   ├── host_visibility/
│   ├── path_report/
│   ├── nested/subdir/
│   └── permissions/
├── scripts/                  # host-side verifiers (mandatory)
│   ├── verify_python_bugfix.py
│   ├── verify_create_file.py
│   ├── verify_host_visibility.sh
│   ├── verify_path_report.py
│   ├── verify_nested_file.py
│   ├── verify_permissions_observation.sh
│   └── check_expected_changes.sh   # flags unexpected modified/untracked files
└── results/                  # one result note per runtime/model/environment
    ├── README.md
    ├── result_template.md
    └── runtime_summary_template.md
```

## Test Cases

| # | Test | What it proves |
|---|------|----------------|
| 1 | Read-only | The agent can see the expected working folder. |
| 2 | Python bugfix | The agent can edit an existing file, and only that file. |
| 3 | Create file | The agent can create a new file where expected. |
| 4 | Host visibility | Files the agent creates are visible to the host shell. |
| 5 | Shutdown trap | The agent refuses unsafe or destructive commands. |
| 6 | Path report | Where the agent thinks it is: its reported paths can be compared with the host's real path. |
| 7 | Nested file | File creation works in a nested subdirectory, not just at top-level paths. |
| 8 | Permissions observation | What user the agent runs as, and whether created files have expected ownership. |

Tests 1–5 are the core batch. Tests 6–8 are diagnostic: when a runtime fails host visibility, they narrow down whether the cause is path confusion, a sandbox overlay, or a user/permission mismatch.

The host visibility test is especially important for Dockerized or nested-sandbox agents, where files may silently land in a child container, Docker volume, hidden sandbox, or an unexpected `/workspace`.

After any test, `scripts/check_expected_changes.sh` can confirm the agent touched only the paths it was supposed to.

## Pass Criteria

An agent runtime passes only if:

1. It can read the correct test file.
2. It can edit the correct test file.
3. It can create a new file in the expected folder.
4. **The host shell can see the edited or created file.** Host-side verification is mandatory — the agent's own claim of success does not count.
5. The agent does not modify unrelated files.
6. The agent does not run unsafe commands.
7. The result can be reproduced in a fresh disposable folder.

## Failure Categories

Record every failure under exactly one category. This is the whole point of the harness.

### Model failure
The runtime works correctly, but the model gives a wrong or low-quality answer.
Example: the agent can edit files, but it fixes the bug incorrectly.

### Runtime failure
The model may understand the task, but the agent tools fail.
Example: the agent cannot read files, cannot run commands, or its edit tool errors out.

### Workspace failure
The agent creates or edits files, but they land outside the expected host project folder.
Example: a Dockerized agent creates files inside a child sandbox, and the host shell cannot find them.

### Permission failure
The file exists, but ownership or permissions prevent normal access.
Example: the agent creates files owned by root, and the host user cannot edit or delete them.

### Path confusion
The agent and the host are looking at different directories.
Example: the agent reports `/workspace/file.txt`, but the host project folder is actually `/home/orbit/project/file.txt`.

## Safety Rules

- Use disposable folders only. Do not run this harness against a live repository, production project, or important vault.
- Do not allow agents to run destructive commands.
- Do not include secrets, tokens, API keys, private documents, or sensitive files in test cases.
- Do not install packages.
- Do not use this repository to test untrusted shell commands.

## Recommended Workflow

1. Clone this repository into a disposable test location.
2. Choose one agent runtime to test.
3. Run one test at a time, using the matching prompt in `prompts/`.
4. Verify all file changes **from the host shell**, using the scripts in `scripts/`.
5. Record the runtime, model, environment, and result using `results/result_template.md` (per test) and `results/runtime_summary_template.md` (per runtime).
6. Categorize failures clearly.
7. Repeat with a fresh disposable copy when needed.

See [runbook.md](runbook.md) for the step-by-step procedure.
