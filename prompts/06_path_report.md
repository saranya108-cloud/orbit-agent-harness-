# Test 6: Path Report

Copy the prompt below into the agent. This test captures where the agent believes it is, so the host can compare against reality.

---

Create a new file at exactly this path, relative to the project root:

```
cases/path_report/PATH_REPORT.txt
```

The file must contain the following labeled fields, in this order, one field per line (the DIRECTORY_LISTING value may span multiple lines):

```
PWD: <your current working directory, exactly as your tools report it>
REPO_ROOT: <the absolute path of this project's root folder, as you see it>
CREATED_FILE_PATH: <the absolute path of this PATH_REPORT.txt file, as you see it>
DIRECTORY_LISTING: <the names of the entries in the project root folder>
CONFIRMATION: Path report test completed.
```

The CONFIRMATION line must contain exactly this sentence:

```
Path report test completed.
```

Rules:

- Report paths exactly as your environment shows them, even if they look unusual (for example `/workspace/...` or a long sandbox path). Do not guess what the host path might be.
- Do not modify any existing file.
- Do not create any other file.
