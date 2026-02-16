# Jules CLI Usage Reference

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

## Command And Flag Matrix

### Top-Level Commands
| Command | Purpose | Key Options |
| :--- | :--- | :--- |
| `jules` | Launch TUI. | `--theme <dark|light>` |
| `jules new "<task>"` | Create session from cwd or explicit repo. | `--repo <owner/repo|.>`, `--parallel <1-5>` |
| `jules remote` | Remote session namespace. | `list`, `new`, `pull` |
| `jules teleport "<session_id>"` | Clone/apply patch or apply in matching repo. | none |
| `jules login` | Authenticate to Jules. | none |
| `jules logout` | Clear auth state. | none |
| `jules version` | Print CLI version. | none |
| `jules completion <shell>` | Generate shell completion script. | shell target |
| `jules help [command]` | Show help. | optional command |

### Remote Subcommands
| Command | Purpose | Key Options |
| :--- | :--- | :--- |
| `jules remote list` | List repos or sessions. | `--repo`, `--session` |
| `jules remote new` | Create remote VM session. | `--repo <owner/repo|.>`, `--session "<task>"`, `--parallel <1-5>` |
| `jules remote pull` | Pull result and optionally apply patch. | `--session <id>`, `--apply` |

### Global Flags
| Flag | Purpose |
| :--- | :--- |
| `--theme <dark|light>` | Choose CLI theme. |

---

## Troubleshooting

| Issue | Solution |
| :--- | :--- |
| **"repo doesn't exist"** | Use `jules remote list --repo` to check the exact name. |
| **TTY errors** | Append `< /dev/null` to your `jules` commands. |
| **Login failures** | Run `jules login` or ensure `HOME` is correctly exported. |
