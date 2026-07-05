# Runtime Summary — Codex Mac Harness Tests 6–8

Date: 2026-07-05
Machine: Amy’s Mac Mini
Agent: Codex v0.142.3
Model shown: gpt-5.5
Repo path: /Users/aclab/agent-harness-tests/orbit-agent-harness-

## Results

- Test 6 Path Report: PASS
- Test 7 Nested File: PASS
- Test 8 Permissions Observation: PASS

## Key Findings

Codex wrote files into the visible host repo path:

/Users/aclab/agent-harness-tests/orbit-agent-harness-

Codex reported user:

aclab

Host reported user:

uid=501(aclab) gid=20(staff)

Generated file ownership observed on host:

aclab staff

## Conclusion

Codex on the Mac behaves as expected:
- no hidden workspace mismatch
- no root-owned output files
- no container path issue
- nested file creation works
- visible host write behavior confirmed

This is a known-good baseline for comparing Hermes, OpenClaw, Docker, and Acer-hosted agent runs.
