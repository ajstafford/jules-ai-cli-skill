# Jules CLI Usage Reference

For the complete command/flag surface and authoritative reference, see `jules-cli/SKILL.md`.

## Core Philosophy: Manual & Intentional
The Jules CLI is for **asynchronous, complex tasks**. It must not be used for trivial edits. Direct CLI usage is required to maintain visibility and prevent "runaway" automation.

---

## Repository Format
**Critical:** Prefer explicit GitHub `owner/repo` format when targeting a remote repository.
- **Correct:** `octocat/repo`
- **Also valid:** `.`
- **Incorrect:** `localuser/repo`

Verify available repos:
```bash
jules remote list --repo
```

---

## Manual Workflow

### 1. New Session
Choose the command based on where you want execution to happen.
```bash
# Remote VM workflow
jules remote new --repo "<repo>" --session "Detailed task description" < /dev/null

# Local workflow (current repo by default)
jules new "Detailed task description" < /dev/null

# Optional: run a small bounded fan-out when explicitly needed
jules remote new --repo "<repo>" --session "Detailed task description" --parallel 3 < /dev/null
```

### 2. Status Monitoring
The `jules remote list --session` command returns a table. Use this Python one-liner to get the exact status safely:
```bash
export JULES_SESSION_ID="<SESSION_ID>"
jules remote list --session | python3 -c "
import sys, re, os
session_id = os.environ.get('JULES_SESSION_ID', '')
if not session_id: sys.exit(0)
for line in sys.stdin:
    line = line.strip()
    if line.startswith(session_id):
        print(re.split(r'\s{2,}', line)[-1])
"
unset JULES_SESSION_ID
```

### 3. Applying Changes
```bash
jules remote pull --session "<SESSION_ID>" --apply < /dev/null
```

---

## Troubleshooting

| Issue | Solution |
| :--- | :--- |
| **"repo doesn't exist"** | Use `jules remote list --repo` to check the exact name. |
| **TTY errors** | Append `< /dev/null` to your `jules` commands. |
| **Login failures** | Run `jules login` or ensure `HOME` is correctly exported. |
