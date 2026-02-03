---
name: jules-cli
description: Interact with the Jules CLI to manage asynchronous coding sessions. Use this skill sparingly for complex, isolated tasks that benefit from a remote VM.
---

# Jules CLI Skill

## Overview
This skill enables the agent to interact with the `jules` CLI. It supports task assignment, session monitoring, and result integration.

## Usage Guidelines (CRITICAL)

To prevent excessive and inappropriate session creation, you **must** follow these rules:

1.  **Local First**: If you can solve the task locally within your current environment (e.g., editing files, running tests, small refactors), **do not** use Jules.
2.  **Complexity Threshold**: Only use Jules for tasks that are:
    *   **Large-scale**: Touching many files or requiring significant architectural changes.
    *   **Isolated**: Benefiting from a clean, remote environment to avoid local dependency issues.
    *   **Exploratory**: Tasks where the solution isn't immediately obvious and requires iteration in a VM.
3.  **No Proliferation (One at a Time)**: 
    *   **Never** create multiple sessions for the same task.
    *   **Never** use a loop or parallel execution to spin up several sessions at once.
    *   Wait for a session to complete and inspect the results before deciding if another session is needed.
4.  **No "Small" Tasks**: Do not submit tasks like "Add a comment", "Change a variable name", or "Fix a typo".

---

## Safety Controls
*   **Approval Required**: If you are unsure if a task is "complex enough" for Jules, ask the user for permission before running `new`.
*   **Verification**: Always list sessions before creating a new one to ensure you don't already have a pending session for the same repository.

---

## Core Workflow

Use the provided Python interface script to interact with Jules in a cross-platform, safe manner.

### 1. Pre-flight Check
Verify repository access and format.
```bash
python3 jules-cli/jules_interface.py list-repos
```
*Note: Ensure the repo format is `GITHUB_USERNAME/REPO`.*

### 2. Submit Task
Create a session and capture the Session ID from the output.
```bash
# Capture the output to get the ID
python3 jules-cli/jules_interface.py new --repo <repo> --task "Detailed task description"
```

### 3. Monitor Progress
Check the status of your specific session. The script parses the output and returns the status (e.g., "In Progress", "Completed").

**Check Status:**
```bash
python3 jules-cli/jules_interface.py status --id <SESSION_ID>
```

### 4. Integrate Results
Once the status is **Completed**, pull and apply the changes.
```bash
python3 jules-cli/jules_interface.py pull --id <SESSION_ID>
```

---

## Error Handling & Troubleshooting

*   **Repository Not Found**: Verify format with `list-repos`. It must match the GitHub path.
*   **Credentials**: If you see login errors, ensure `HOME` is set correctly or run `jules login`.
*   **Script Errors**: Ensure `jules` is in your PATH and you are using Python 3.

---

## Command Reference

| Command | Purpose |
| :--- | :--- |
| `python3 jules-cli/jules_interface.py list-repos` | Verify available repositories and their exact names. |
| `python3 jules-cli/jules_interface.py status --id <ID>` | Check status of a specific session. |
| `python3 jules-cli/jules_interface.py new --repo <R> --task <T>` | Create a new coding task. |
| `python3 jules-cli/jules_interface.py pull --id <ID>` | Apply changes from a completed session. |
