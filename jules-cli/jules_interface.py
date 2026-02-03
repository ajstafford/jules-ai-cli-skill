#!/usr/bin/env python3
import argparse
import subprocess
import sys
import re
import shutil

def run_jules(args):
    """
    Runs the jules command with the given arguments.
    Uses stdin=subprocess.DEVNULL to avoid TTY issues.
    """
    if not shutil.which('jules'):
        print("Error: 'jules' command not found. Please ensure it is installed and in your PATH.", file=sys.stderr)
        sys.exit(1)

    try:
        # Use stdin=subprocess.DEVNULL to avoid TTY issues
        result = subprocess.run(
            ['jules'] + args,
            capture_output=True,
            text=True,
            stdin=subprocess.DEVNULL
        )
        if result.returncode != 0:
            print(f"Error running command: jules {' '.join(args)}", file=sys.stderr)
            print(result.stderr, file=sys.stderr)
            sys.exit(result.returncode)
        return result.stdout
    except Exception as e:
        print(f"Error executing jules: {e}", file=sys.stderr)
        sys.exit(1)

def list_repos(args):
    """Lists available repositories."""
    print(run_jules(['remote', 'list', '--repo']))

def new_session(args):
    """Creates a new session."""
    # Pass --session arg correctly (which is the task description)
    print(run_jules(['remote', 'new', '--repo', args.repo, '--session', args.task]))

def check_status(args):
    """Checks the status of a specific session ID."""
    output = run_jules(['remote', 'list', '--session'])
    found = False
    for line in output.splitlines():
        # Check if line starts with the ID (as per original SKILL.md logic)
        if line.strip().startswith(args.id):
             # Split by 2+ spaces
             parts = re.split(r'\s{2,}', line.strip())
             # Status is usually the last column based on SKILL.md one-liner
             if len(parts) >= 2:
                 status = parts[-1]
                 print(status)
                 found = True
                 break
    if not found:
        print("Session ID not found or status could not be parsed.", file=sys.stderr)
        sys.exit(1)

def pull_session(args):
    """Pulls changes from a completed session."""
    print(run_jules(['remote', 'pull', '--session', args.id, '--apply']))

def main():
    parser = argparse.ArgumentParser(description="Cross-platform wrapper for Jules CLI.")
    subparsers = parser.add_subparsers(dest='command', required=True)

    # list-repos
    parser_repos = subparsers.add_parser('list-repos', help='List available repositories')
    parser_repos.set_defaults(func=list_repos)

    # new
    parser_new = subparsers.add_parser('new', help='Create a new session')
    parser_new.add_argument('--repo', required=True, help='Repository name (user/repo)')
    parser_new.add_argument('--task', required=True, help='Task description')
    parser_new.set_defaults(func=new_session)

    # status
    parser_status = subparsers.add_parser('status', help='Check status of a session')
    parser_status.add_argument('--id', required=True, help='Session ID')
    parser_status.set_defaults(func=check_status)

    # pull
    parser_pull = subparsers.add_parser('pull', help='Pull changes from a completed session')
    parser_pull.add_argument('--id', required=True, help='Session ID')
    parser_pull.set_defaults(func=pull_session)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
