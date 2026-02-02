# Jules CLI Skill

## Overview

This skill enables agents to interact with the Jules CLI for task assignment, session monitoring, and pulling patches from completed remote sessions. It is designed with a **Manual & Intentional** philosophy to prevent runaway automation and ensure resources are used only for complex, appropriate tasks.

**Key Features:**
- **Intent-Driven Workflow** - Explicit steps for session creation and monitoring.
- **Safety Controls** - Built-in complexity thresholds and anti-proliferation rules.
- **Direct CLI Control** - Leverages the raw `jules` CLI for maximum transparency.
- **One-liner Utilities** - Robust Python/Shell one-liners for status parsing without external scripts.
- **Error Handling Documentation** - Extensive guides for common Jules edge cases (TTY, login, repository formats).

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
4. **Point your agent** (OpenClaw, etc.) to the `jules-cli` directory. The agent will read `SKILL.md` to understand its operating boundaries.

## Usage Guidelines (CRITICAL)

To prevent inappropriate resource usage, the following rules are enforced:
- **Local First**: Use local tools for small refactors, comments, or typos.
- **Complexity Threshold**: Only use Jules for large-scale, isolated, or exploratory tasks.
- **No Proliferation**: One session at a time. Never bulk-create or loop over session creation.

## Documentation

- **[SKILL.md](jules-cli/SKILL.md)** - Main skill documentation with safety rules, workflows, and monitoring one-liners.
- **[usage.md](jules-cli/references/usage.md)** - Detailed command reference for all native Jules CLI commands.

## Project Structure

```
jules-cli/
├── SKILL.md              # Safety guidelines, workflows, and CLI monitoring
├── references/
│   └── usage.md          # Comprehensive command reference
└── assets/               # Supporting documentation assets
```

## Testing & Validation

This skill has been validated through live Jules sessions, specifically focusing on:
- Intentional session lifecycle (Create -> Poll -> Apply).
- Handling TTY and authentication scenarios in non-interactive environments.
- Correct repository format validation (`GITHUB_USERNAME/REPO`).

## Prerequisites

1. **Jules CLI** - Must be installed and authenticated.
2. **GitHub Account** - Required for Jules remote sessions.
3. **Standard Unix Tools** - `grep`, `awk`, and `python3` for status parsing one-liners.

## License

This project is provided for educational and demonstration purposes. Feel free to use, modify, and distribute with attribution.