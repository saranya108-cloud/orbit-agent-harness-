# Nested File Test Case

This folder is the target of the nested file test (Test 7).

The agent is asked to create `NESTED_AGENT_FILE.txt` in this folder — two directory levels below `cases/` — containing exactly:

```
Nested file creation test passed.
```

Verify from the host shell:

```sh
python3 scripts/verify_nested_file.py
```

## Why this matters

Some runtimes handle top-level file creation fine but stumble on nested paths: they resolve relative paths against the wrong base directory, drop files at the repo root, or recreate the directory tree somewhere else. A file that lands at `cases/NESTED_AGENT_FILE.txt` or `subdir/NESTED_AGENT_FILE.txt` instead of here is path confusion, not model failure.

This README also ensures the directory exists in git before the test, so the agent only has to create a file, never a directory.

Delete `NESTED_AGENT_FILE.txt` to reset this test.
