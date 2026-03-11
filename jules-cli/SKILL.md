---
name: jules-cli
description: Interact with the Jules CLI to manage asynchronous coding sessions. Use this skill sparingly for complex, isolated tasks that benefit from a remote VM.
binaries:
  - jules
  - python3
env:
  - HOME
---

# Jules CLI Skill

## Overview
This skill enables the agent to interact with the full `jules` CLI surface, including local session creation (`jules new`), remote session workflows (`jules remote ...`), and integration flows (`jules remote pull`, `jules teleport`).

## Usage Guidelines (CRITICAL)

To prevent excessive and inappropriate session creation, you **must** follow these rules:

1.  **Local First**: If you can solve the task locally within your current environment (e.g., editing files, running tests, small refactors), **do not** use Jules.
2.  **Complexity Threshold**: Only use Jules for tasks that are:
    *   **Large-scale**: Touching many files or requiring significant architectural changes.
    *   **Isolated**: Benefiting from a clean, remote environment to avoid local dependency issues.
    *   **Exploratory**: Tasks where the solution isn't immediately obvious and requires iteration in a VM.
3.  **No Proliferation (One at a Time by Default)**:
    *   Default to one session per task and inspect results before creating another.
    *   Use `--parallel` only when explicitly justified by the task and user intent.
    *   Never use unbounded loops to create sessions.
4.  **No "Small" Tasks**: Do not submit tasks like "Add a comment", "Change a variable name", or "Fix a typo".

---

## Security Guidelines

To ensure safe execution of CLI commands, you **must** adhere to the following security practices:

1.  **Input Validation**: Before running any command, validate that:
    *   **Repository names** are either `owner/repo` (alphanumeric, dots, hyphens, and underscores) or `.` when intentionally targeting the current working repository.
    *   **Session IDs** are alphanumeric (typically hyphens and underscores are also allowed).
2.  **Quoting**: Always wrap shell placeholders in double quotes (e.g., `"<repo>"`).
3.  **No Inline Injection**: Never embed user-provided data directly into script strings (like `python3 -c`). Use environment variables to pass such data safely.
4.  **Sanitization**: Ensure task descriptions do not contain malicious shell characters if passed directly to the shell.

---

## Safety Controls
*   **Approval Required (MANDATORY)**: You **must** ask for explicit user approval before running any of the following commands:
    *   `jules new`: Since this creates one or more sessions.
    *   `jules remote new`: Since this creates a remote session/VM.
    *   `jules remote pull --apply`: Since this modifies the local codebase.
    *   `jules teleport`: Since this clones and modifies the environment.
*   **Verification**: Always run `jules remote list --session` before creating a new one to ensure you don't already have a pending session for the same repository.
*   **Credentials**: If `jules login` is required, explain *why* to the user and wait for their confirmation before proceeding.

---

## Core Workflow (Manual Control)

Prefer using the CLI directly to maintain situational awareness.

### 1. Pre-flight Check
Verify repository access and format.
```bash
jules remote list --repo
```
*Note: Ensure the repo format is `GITHUB_USERNAME/REPO`.*

### 2. Submit Task
Create a session and capture the Session ID.
```bash
# Remote VM workflow (explicit remote execution)
jules remote new --repo "<repo>" --session "Detailed task description" < /dev/null

# Local workflow (defaults to cwd repo, can also pass --repo "<repo>" or --repo .)
jules new --repo "<repo>" "Detailed task description" < /dev/null
```

### 3. Monitor Progress
List sessions and look for your ID. Use this robust one-liner to check the status (it handles statuses with spaces like "In Progress"):

**Check Status (Safe Method):**
```bash
# Use an environment variable to pass the Session ID safely to Python
export JULES_SESSION_ID="<SESSION_ID>"
jules remote list --session | python3 -c "
import sys, re, os
session_id = os.environ.get('JULES_SESSION_ID', '')
if not session_id: sys.exit(0)
for line in sys.stdin:
    line = line.strip()
    if line.startswith(session_id):
        # Extract status (the last column after multiple spaces)
        print(re.split(r'\s{2,}', line)[-1])
"
unset JULES_SESSION_ID
```

### 4. Integrate Results
Once the status is **Completed**, pull and apply the changes.
```bash
# Replace <SESSION_ID> with the validated Session ID
jules remote pull --session "<SESSION_ID>" --apply < /dev/null
```

---

## Error Handling & Troubleshooting

*   **Repository Not Found**: Verify format with `jules remote list --repo`. It must match the GitHub path.
*   **TTY Errors**: Always use `< /dev/null` for non-interactive automation with the raw `jules` command.
*   **Credentials**: If you see login errors, ensure `HOME` is set correctly or run `jules login`.

---

## Command Reference

### Top-Level Commands
| Command | Purpose | Key Options |
| :--- | :--- | :--- |
| `jules` | Launch TUI. | `--theme <dark|light>` |
| `jules new "<task>"` | Create session from current repo or explicit repo. | `--repo <owner/repo|.>`, `--parallel <1-5>` |
| `jules remote` | Remote session namespace. | `list`, `new`, `pull` |
| `jules teleport "<session_id>"` | Clone/apply patch or apply in matching repo. | none |
| `jules login` | Authenticate CLI with Google account. | none |
| `jules logout` | Remove local auth state. | none |
| `jules version` | Show CLI version. | none |
| `jules completion <shell>` | Generate shell completions. | shell target |
| `jules help [command]` | Show command help. | optional command |

### Remote Subcommands
| Command | Purpose | Key Options |
| :--- | :--- | :--- |
| `jules remote list` | List repos or sessions. | `--repo`, `--session` |
| `jules remote new` | Create remote VM coding session. | `--repo <owner/repo|.>`, `--session "<task>"`, `--parallel <1-5>` |
| `jules remote pull` | Pull session result locally. | `--session <id>`, `--apply` |

### Global Flags
| Flag | Purpose |
| :--- | :--- |
| `--theme <dark|light>` | Choose CLI theme. |
