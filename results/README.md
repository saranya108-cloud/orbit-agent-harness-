# Results

Each runtime/model/environment combination gets its own result note in this folder.

Create a note by copying the template:

```sh
cp results/result_template.md results/YYYY-MM-DD_runtime_environment.md
```

Naming examples:

- `2026-07-05_codex_local.md`
- `2026-07-05_openclaw_docker.md`
- `2026-07-06_ollama-qwen_vm.md`

Guidelines:

- One note per combination — if you test the same runtime with a different model or a different environment (local vs. Docker vs. VM), that is a new note.
- Fill in the host verification section with the actual commands you ran and their actual output. A result without host verification does not count.
- Assign exactly one failure category to each failed test. The categories are defined in the top-level [README.md](../README.md).
- Keep notes even for passes — a reproducible pass is data too.
