#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Dict, List, Optional

sys.path[:0] = [str(Path(__file__).resolve().parents[1] / "tickets")]

from ticket_tree import (  # noqa: E402
    AUTOMERGE_LABEL,
    DEVELOP,
    ISSUES_API,
    REMOTE,
    SHARED_BRANCH,
    current_branch,
    git,
    run_tool,
)

USAGE = """Push the current branch and open or update its pull request, always labelled automerge (TKT-28).

Usage, from the branch's own checkout or worktree:
    python3 .claude/scripts/github/publish.py --title "<title>" --body-file <file>

Every branch of the person's work that is not a ticket's (``feature/harness-*``, other ``feature/``, ``bugfix/``,
``hotfix/``) goes to GitHub the same way: pushed, its pull request opened to ``develop`` (``master`` for a hotfix)
with the ``automerge`` label, so that ``automerge.yml`` merges it once every check passes. Nobody asks before the push
and nobody merges by hand, except a pull request that changes ``.github/workflows/``, which ``automerge.yml`` leaves
to the person (``needs-person``). An open pull request of the branch is updated: it gets the label if it lacks it.
``develop``, ``master`` and ``main`` are refused, and so is ``feature/tickets``: the tickets' commits are published by
``ticket_tree.py finish`` only (TKT-5). Prints ``{"pushed", "branch", "base", "pull_request"}`` as JSON.
"""

REFUSED = ("develop", "master", "main")
PREFIXES = ("feature/", "bugfix/", "hotfix/")
LABEL_COLOUR = "0e8a16"
LABEL_DESCRIPTION = "Merged into develop once CI passes"


def base_of(branch: str) -> str:
    """Return the branch a pull request of ``branch`` goes to under GitFlow (TKT-15)."""
    return "master" if branch.startswith("hotfix/") else DEVELOP


def refusal(branch: str) -> Optional[str]:
    """Say why ``branch`` cannot be published here, or return None."""
    if branch in REFUSED:
        return f"{branch} changes only through pull requests (TKT-15)."
    if branch == SHARED_BRANCH:
        return f"{SHARED_BRANCH} is published by `ticket_tree.py finish` only (TKT-5)."
    if not branch.startswith(PREFIXES):
        return f"{branch} is not a GitFlow branch of the person's work ({', '.join(PREFIXES)})."
    return None


def open_pull_request(home: Path, branch: str, title: str, body: str) -> str:
    """Open the pull request of ``branch`` with the automerge label, or label the open one; return its address."""
    run_tool(
        home,
        "gh",
        "label",
        "create",
        AUTOMERGE_LABEL,
        "--color",
        LABEL_COLOUR,
        "--force",
        "--description",
        LABEL_DESCRIPTION,
    )
    code, listed = run_tool(home, "gh", "pr", "list", "--head", branch, "--state", "open", "--json", "number,url")
    try:
        found = json.loads(listed) if code == 0 and listed else []
    except json.JSONDecodeError:
        found = []
    if isinstance(found, list) and found and isinstance(found[0], dict):
        number, url = found[0].get("number"), str(found[0].get("url") or "")
        code, output = run_tool(
            home, "gh", "api", "-X", "POST", f"{ISSUES_API}/{number}/labels", "-f", f"labels[]={AUTOMERGE_LABEL}"
        )
        if code != 0:
            raise RuntimeError(f"The branch is pushed but its pull request could not be labelled: {output}")
        return url
    args: List[str] = ["pr", "create", "--base", base_of(branch), "--head", branch, "--title", title, "--body", body]
    code, url = run_tool(home, "gh", *args, "--label", AUTOMERGE_LABEL)
    if code != 0:
        raise RuntimeError(f"The branch is pushed but the pull request could not be opened: {url}")
    return url.splitlines()[-1]


def publish(home: Path, title: str, body: str) -> Dict[str, object]:
    """Push the branch checked out in ``home`` and open or label its pull request (TKT-28)."""
    branch = current_branch(home)
    reason = refusal(branch)
    if reason:
        raise RuntimeError(reason)
    code, output = git(home, "push", "--quiet", "--set-upstream", REMOTE, branch, check=False)
    if code != 0:
        raise RuntimeError(f"git push {REMOTE} {branch} failed: {output}")
    url = open_pull_request(home, branch, title, body)
    return {"pushed": True, "branch": branch, "base": base_of(branch), "pull_request": url}


def main() -> int:
    args = sys.argv[1:]
    if "--title" not in args or "--body-file" not in args:
        print(USAGE, file=sys.stderr)
        return 2
    title = args[args.index("--title") + 1]
    body = Path(args[args.index("--body-file") + 1]).read_text(encoding="utf-8")
    try:
        result = publish(Path.cwd(), title, body)
    except RuntimeError as error:
        print(f"Not published: {error}", file=sys.stderr)
        return 1
    print(json.dumps(result))
    return 0


if __name__ == "__main__":
    sys.exit(main())
