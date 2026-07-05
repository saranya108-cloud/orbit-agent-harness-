# Create-File Test Case

This folder is the target of the create-file test (Test 3).

The agent is asked to create a file named `AGENT_CREATED_THIS_FILE.txt` in this folder, containing exactly this sentence:

```
Agent file creation test passed.
```

Before the test runs, that file must not exist. After the test, verify from the host shell:

```sh
python3 scripts/verify_create_file.py
```

If the agent reports success but the verifier cannot find the file, the file probably landed somewhere else — a child container, a Docker volume, a hidden sandbox, or the wrong working directory. That is a workspace or path failure, not a model failure.

Delete `AGENT_CREATED_THIS_FILE.txt` to reset this test.
