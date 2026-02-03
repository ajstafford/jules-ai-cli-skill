# Jules CLI Usage Reference

## Core Philosophy: Manual & Intentional
The Jules CLI is for **asynchronous, complex tasks**. It must not be used for trivial edits. Direct CLI usage is required to maintain visibility and prevent "runaway" automation.

---

## Repository Format
**Critical:** Always use the GitHub organization/username format.
- **Correct:** `octocat/repo`
- **Incorrect:** `localuser/repo`

Verify available repos using the Python interface:
```bash
python3 jules-cli/jules_interface.py list-repos
```

---

## Workflow

### 1. New Session
```bash
python3 jules-cli/jules_interface.py new --repo <repo> --task "Detailed task description"
```
*Note the Session ID from the output.*

### 2. Status Monitoring
Use the interface to get the exact status for an ID:
```bash
python3 jules-cli/jules_interface.py status --id <SESSION_ID>
```

### 3. Applying Changes
```bash
python3 jules-cli/jules_interface.py pull --id <SESSION_ID>
```

---

## Troubleshooting

| Issue | Solution |
| :--- | :--- |
| **"repo doesn't exist"** | Use `list-repos` to check the exact name. |
| **Login failures** | Run `jules login` or ensure `HOME` is correctly exported. |
| **Script Errors** | Ensure `jules` is in your PATH and Python 3 is installed. |
