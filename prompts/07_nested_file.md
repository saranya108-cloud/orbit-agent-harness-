# Test 7: Nested File

Copy the prompt below into the agent. This test checks that file creation works in a nested subdirectory, not just at convenient top-level paths.

---

Create a new file at exactly this path, relative to the project root:

```
cases/nested/subdir/NESTED_AGENT_FILE.txt
```

The file must contain exactly this sentence and nothing else:

```
Nested file creation test passed.
```

Rules:

- The directory `cases/nested/subdir/` already exists. Do not create any new directories.
- Do not create the file anywhere else.
- Do not modify any existing file.
- After creating the file, state the absolute path where you created it.
