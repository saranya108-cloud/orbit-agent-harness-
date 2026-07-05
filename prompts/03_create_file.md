# Test 3: Create File

Copy the prompt below into the agent.

---

Create a new file at exactly this path, relative to the project root:

```
cases/create_file/AGENT_CREATED_THIS_FILE.txt
```

The file must contain exactly this sentence and nothing else:

```
Agent file creation test passed.
```

Rules:

- Do not create the file anywhere else.
- Do not modify any existing file.
- After creating the file, state the absolute path where you created it.
