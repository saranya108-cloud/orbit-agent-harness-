# Runtime Summary

One summary per runtime after running the full test batch. For per-test detail, use `result_template.md`.

- **Date:**
- **Runtime:** (e.g. Codex, OpenClaw, Hermes Agent, Ollama-backed, Dockerized agent, VM-based)
- **Runtime version:**
- **Model:**
- **Environment:** (local / Docker / nested container / VM; include mount details if Dockerized)
- **Host machine:** (e.g. Mac Mini M2, Ubuntu desktop)
- **Repo path:** (the disposable folder the tests ran in)

## Overall result

(e.g. 8/8 pass, 6/8 pass with permission issues, unusable — no host-visible writes)

## Test summary

| # | Test | Result (pass/fail/partial) | Failure category | Notes |
|---|------|----------------------------|------------------|-------|
| 1 | Read-only | | | |
| 2 | Python bugfix | | | |
| 3 | Create file | | | |
| 4 | Host visibility | | | |
| 5 | Shutdown trap | | | |
| 6 | Path report | | | |
| 7 | Nested file | | | |
| 8 | Permissions observation | | | |

## Blocking issues

(Anything that makes this runtime unusable as-is: invisible writes, root-owned files, no shell access, etc.)

## Suitable for

(What you would trust this runtime to do today, based on these results.)

## Not suitable for

(What you would not trust it with yet.)

## Notes

## Next runtime to compare
