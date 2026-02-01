# Jules CLI Skill

## Overview

This skill enables agents to interact with the Jules CLI for task assignment, session monitoring, and pulling patches from completed remote sessions. Built based on real-world automation pain points and tested with live Jules sessions.

**Key Features:**
- **Automated task submission and monitoring** - Fire-and-forget or wait-for-completion modes
- **Session lifecycle management** - Complete workflow: create → wait → pull → apply
- **TTY-safe automation** - Handles terminal interaction issues common in CI/CD pipelines
- **Error handling** - Built-in retry logic and prerequisite validation
- **Session parsing utilities** - Converts Jules tabular output to structured JSON

## Installation

1. **Clone or download** this repository
2. **Make scripts executable:**
   ```bash
   chmod +x jules-cli/scripts/*
   ```
3. **Install Jules CLI** and authenticate:
   ```bash
   npm install -g @google/jules
   jules login
   ```
4. **Verify setup:**
   ```bash
   jules remote list --repo
   ```
5. **Ask your agent (opencode, openclaw, etc.) to install into your agent's skills directory**

  ```
   Please install the skill from ajstafford/jules-cli-skill. You can find the instructions in the SKILL.md file within that repository. Ensure it's placed in your active skills path so you can invoke it when I ask about Jules tasks.
  ```
   
## Quick Start

```bash
# 1. Verify your repositories
jules remote list --repo

# 2. Submit a task and wait for completion
./jules-cli/scripts/jules_submit.py --repo username/repo "Your task description"
```

**Note:** Use your GitHub username/org format (e.g., `octocat/Hello-World`), not your local system username.

## Documentation

- **[SKILL.md](jules-cli/SKILL.md)** - Complete skill documentation with workflows, examples, and troubleshooting
- **[usage.md](jules-cli/references/usage.md)** - Command reference for all Jules CLI commands
- **[jules_submit.py](jules-cli/scripts/jules_submit.py)** - Main automation script (118 lines, production-ready)

## Project Structure

```
jules-cli/
├── SKILL.md              # Main skill documentation (157 lines)
├── references/
│   └── usage.md          # Detailed command reference (107 lines)
└── scripts/
    ├── jules_submit.py   # Automated workflow script (Python)
    ├── wait_for_session.sh   # Session polling script (Bash)
    └── parse_sessions.py     # Output parsing utility (Python)
```

**Total:** 551 lines of documentation and code

## Testing & Validation

This skill has been tested with live Jules sessions including:
- Session creation and monitoring
- TTY/authentication error scenarios
- Repository format validation workflows
- Edge case handling (missing HOME, credential issues)

See [jules-cli/SKILL.md](jules-cli/SKILL.md) Common Error Patterns section for documented issues and solutions discovered during testing.

## Prerequisites

1. **Jules CLI** - Install and authenticate with `jules login`
2. **Python 3** - Required for wrapper scripts
3. **GitHub Account** - Jules works with GitHub repositories

## License

This project is provided for educational and demonstration purposes. Feel free to use, modify, and distribute with attribution.

---

**Built for:** Automation engineers, CI/CD pipelines, and developers using Google Jules
**Tech Stack:** Python 3, Bash, Jules CLI, GitHub integration
