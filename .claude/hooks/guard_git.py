#!/usr/bin/env python3
"""The PreToolUse hook of SimpleERP on Bash commands: git as GitFlow and the ticket harness allow it (TKT-5, TKT-15).

It refuses ``--no-verify`` everywhere, a rebase, reset, forced push or deletion of ``develop`` or ``master`` (TKT-25),
and the git writes of an agent on a ticket's branch or a worker's; it asks the person before a group approval
(TKT-20), a release (TKT-26) or a push to ``develop`` or ``master`` (TKT-15). The person's own bypass of the git hooks,
``ERP_GITFLOW_BYPASS=1`` (the first push of ``develop`` and ``master``, a release tag), is theirs to type in their
terminal: an agent never sets it.
"""

from __future__ import annotations

import json
import re
import shlex
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

HEREDOC = re.compile(r"<<-?\s*['\"]?(\w+)['\"]?")
SEGMENTS = re.compile(r"&&|\|\||;|\n")
QUOTED = re.compile(r"'[^']*'|\"(?:[^\"\\]|\\.)*\"")
TICKET_CONTEXT = re.compile(r"^(feature/tickets|feature/T\d+\.\d{2}|ticket/T\d+\.\d{2}|worktree-.*)$")
APPROVE = re.compile(r"\btickets\.py\s+approve\b")
RELEASE = re.compile(r"\bgh\s+workflow\s+run\s+release(?:\.yml)?\b")
WRITES = re.compile(
    r"\bgit\s+(?:-C\s+\S+\s+|-c\s+\S+\s+)*(commit|merge|rebase|reset|stash|push|cherry-pick|revert)\b(?!-)"
)
PR_MERGE = re.compile(r"\bgh\s+pr\s+merge\b")
NO_VERIFY = re.compile(r"\bgit\b[^|;&]*\s(--no-verify|commit\s+(?:[^|;&]*\s)?-n\b)")
PROTECTED = ("develop", "master", "main")
REBASE = re.compile(r"\bgit\s+(?:-C\s+\S+\s+|-c\s+\S+\s+)*rebase\b([^|;&]*)")
RESET = re.compile(r"\bgit\s+(?:-C\s+\S+\s+|-c\s+\S+\s+)*reset\b")
PUSH = re.compile(r"\bgit\s+(?:-C\s+\S+\s+)*push\b([^|;&]*)")
FORCE = re.compile(r"(?:^|\s)(?:--force(?:-with-lease)?(?:=\S*)?|-f|--delete|-d)(?=\s|$)")
REWRITE_REASON = (
    "{target} is never rebased, reset, force-pushed or deleted (TKT-25): develop changes through pull requests, "
    "master through a release or a hotfix pull request (TKT-15). Only a live branch is rebased onto develop: "
    "`python3 .claude/scripts/tickets/tickets.py branches` says which."
)
PUSH_PROTECTED = re.compile(r"\bgit\s+(?:-C\s+\S+\s+)*push\b[^|;&]*?(?:\s|:)(develop|master|main)\b")


def branch_of(cwd: str) -> str:
    result = subprocess.run(["git", "-C", cwd, "branch", "--show-current"], capture_output=True, text=True, check=False)
    return result.stdout.strip()


def folder_of(command: str, cwd: str) -> str:
    """Return the folder the first git write of a command runs in: its ``git -C``, else the last ``cd`` before it.

    A folder that cannot be resolved (a variable, a path that does not exist) leaves the folder unchanged, so that a
    write is never judged on a branch the guard could not see.
    """
    current = Path(cwd)
    for segment in SEGMENTS.split(command):
        try:
            words = shlex.split(segment)
        except ValueError:
            continue
        if len(words) == 2 and words[0] == "cd":
            candidate = current / Path(words[1]).expanduser()
            current = candidate.resolve() if "$" not in words[1] and candidate.is_dir() else current
        if WRITES.search(code_of(segment)) or PR_MERGE.search(segment):
            for index, word in enumerate(words[:-1]):
                if word == "-C" and index > 0 and words[index - 1] == "git":
                    candidate = current / Path(words[index + 1]).expanduser()
                    return str(candidate.resolve()) if candidate.is_dir() else str(current)
            return str(current)
    return str(current)


def code_of(command: str) -> str:
    """Return the command without heredoc bodies and quoted strings: they are text (a message, a script), not options."""
    lines: List[str] = []
    ending = ""
    for line in command.splitlines():
        if ending:
            if line.strip() == ending:
                ending = ""
            continue
        heredoc = HEREDOC.search(line)
        if heredoc:
            ending = heredoc.group(1)
        lines.append(line)
    return QUOTED.sub("''", "\n".join(lines))


def rewritten_protected(command: str, branch: str) -> str:
    """Return the protected branch a command would rebase, reset, force-push or delete, or an empty string."""
    for rebase in REBASE.finditer(command):
        words = rebase.group(1).split()
        positional = [w for i, w in enumerate(words) if not w.startswith("-") and (i == 0 or words[i - 1] != "--onto")]
        if len(positional) >= 2 and positional[1] in PROTECTED:
            return positional[1]
        if len(positional) < 2 and branch in PROTECTED:
            return branch
    if RESET.search(command) and branch == "master":
        return branch
    for push in PUSH.finditer(command):
        words = push.group(1).split()
        forced = FORCE.search(push.group(1)) is not None
        for word in words:
            name = word.lstrip("+").split(":")[-1]
            if name in PROTECTED and (forced or word.startswith(("+", ":"))):
                return name
    return ""


def decide(command: str, cwd: str) -> Optional[Tuple[str, str]]:
    """Return (decision, reason) for a Bash command, or None to let it run.

    The branch judged is the one of the folder the git write runs in (``folder_of``), not only the session's: a
    harness branch's worktree may commit while the main checkout is on the tickets' branch, and a ``cd`` into a
    ticket's checkout is refused as if the session were there.
    """
    folder = folder_of(command, cwd)
    command = code_of(command)
    if NO_VERIFY.search(command):
        return "deny", "Skipping the git hooks (--no-verify) is not allowed: they hold the GitFlow rules (TKT-15)."
    branch = branch_of(folder)
    protected = rewritten_protected(command, branch)
    if protected:
        return "deny", REWRITE_REASON.format(target=protected)
    context = TICKET_CONTEXT.match(branch)
    write = WRITES.search(command) or PR_MERGE.search(command)
    if context and write:
        return "deny", (
            f"`{write.group(0)}` is not run by hand in a ticket's or a worker's worktree (TKT-5): "
            "workers hand off with `python3 .claude/scripts/tickets/ticket_tree.py handoff`, the integrator integrates with "
            "`ticket_tree.py integrate`, and only `ticket_tree.py finish` commits, pushes and opens the pull request."
        )
    if APPROVE.search(command):
        return (
            "ask",
            "This approves the plans of a group of tickets: the approval is the person's (TKT-3, TKT-20). Approve?",
        )
    if RELEASE.search(command):
        return "ask", "This starts a release, which ends merged into master and published (TKT-26). Release?"
    target = PUSH_PROTECTED.search(command)
    if target:
        return "ask", (
            f"This pushes to {target.group(1)}, which changes through pull requests (TKT-15). Only the person's first "
            "push or a release tag goes there by hand. Push anyway?"
        )
    return None


def main() -> int:
    payload: Dict[str, object] = json.loads(sys.stdin.read() or "{}")
    tool_input = payload.get("tool_input")
    command = str(tool_input.get("command", "")) if isinstance(tool_input, dict) else ""
    found = decide(command, str(payload.get("cwd") or "."))
    if found:
        decision, reason = found
        output = {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": decision,
                "permissionDecisionReason": reason,
            }
        }
        print(json.dumps(output))
    return 0


if __name__ == "__main__":
    sys.exit(main())
