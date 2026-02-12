# Jules CLI Skill

## Overview

This skill enables agents to interact with the Jules CLI for task assignment, session monitoring, and pulling patches from completed remote sessions. It is designed with a **Security-First & Manual** philosophy to prevent runaway automation and ensure resources are used only for complex, appropriate tasks.

**Key Features:**
- **Security-First Design** - Mandatory input validation and shell injection prevention (via quoting and environment variables).
- **Mandatory Approvals** - Explicit user confirmation required for session creation and code modifications.
- **Safety Controls** - Built-in complexity thresholds and anti-proliferation rules.
- **Direct CLI Control** - Leverages the raw `jules` CLI for maximum transparency.
- **Robust Parsing** - Safe Python one-liners for status parsing without external scripts.

## Installation

1. **Clone or download** this repository.
2. **Install Jules CLI** and authenticate:
   ```bash
   npm install -g @google/jules
   jules login
   ```
3. **Verify setup:**
   ```bash
   jules remote list --repo
   ```
4. **Point your agent** to the `jules-cli` directory. The agent will read `SKILL.md` to understand its security and operating boundaries.

## Usage Guidelines (CRITICAL)

To prevent inappropriate resource usage, the following rules are enforced:
- **Local First**: Use local tools for small refactors, comments, or typos.
- **Complexity Threshold**: Only use Jules for large-scale, isolated, or exploratory tasks.
- **No Proliferation**: One session at a time. Never bulk-create or loop over session creation.
- **Mandatory Approval**: The agent **must** ask for permission before creating remote VMs or applying code changes.

## Documentation

- **[SKILL.md](jules-cli/SKILL.md)** - Main skill definition with security rules, mandatory safety controls, and metadata.
- **[usage.md](jules-cli/references/usage.md)** - Secure command reference for native Jules CLI commands.

## Project Structure

```
jules-cli/
├── SKILL.md              # Security guidelines, safety controls, and metadata
├── references/
│   └── usage.md          # Secure command usage reference
```

## Security & Prerequisites

1. **Jules CLI** - Must be installed (`jules`) and authenticated.
2. **Python 3** - Required for safe status parsing utilities.
3. **Environment** - The skill requires `HOME` access for credential management.
4. **GitHub Account** - Required for Jules remote sessions.

## License

This project is provided for educational and demonstration purposes. Feel free to use, modify, and distribute with attribution.
