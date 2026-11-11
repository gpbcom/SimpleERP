"""GitHub payloads in the shapes the REST API answers with, and the names the tests share."""

from __future__ import annotations

import stat
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Dict, List, Optional

from pydantic import JsonValue

from pr_watch.models.enums import EventKind
from pr_watch.models.events.pr_event import PrEvent
from pr_watch.models.watch.ticket_watch import TicketWatch

REPOSITORY = "gpbcom/simple-erp"
API = f"/repos/{REPOSITORY}"
HEAD_SHA = "668501e0d3a1b2c3d4e5f60718293a4b5c6d7e8f"
HEAD_REF = "feature/GH-12-add-customers"
PR_URL = f"https://github.com/{REPOSITORY}/pull/7"
SESSION_ID = "7a30c2c8-75fe-4e6a-8475-dc3d38910314"
NOW = datetime(2026, 11, 10, 9, 0, tzinfo=timezone(timedelta(hours=1)))


def pull_request_payload(
    state: str = "open", merged: bool = False, head_sha: str = HEAD_SHA, mergeable: Optional[str] = "clean"
) -> Dict[str, JsonValue]:
    return {
        "number": 7,
        "title": "[GH-12] Add customers",
        "state": state,
        "merged": merged,
        "merged_at": "2026-11-11T09:00:00Z" if merged else None,
        "closed_at": "2026-11-11T09:00:00Z" if state == "closed" else None,
        "merge_commit_sha": "9f1c2b3a" + "0" * 32,
        "mergeable_state": mergeable,
        "created_at": "2026-11-09T16:00:00Z",
        "updated_at": "2026-11-10T08:00:00Z",
        "user": {"login": "gpbcom"},
        "body": "Closes #12",
        "head": {"ref": HEAD_REF, "sha": head_sha},
        "base": {"ref": "develop"},
        "html_url": PR_URL,
    }


def check_run_payload(identifier: int, name: str, conclusion: Optional[str], suite: int = 77) -> Dict[str, JsonValue]:
    return {
        "id": identifier,
        "name": name,
        "status": "completed" if conclusion else "in_progress",
        "conclusion": conclusion,
        "html_url": f"https://github.com/{REPOSITORY}/runs/{identifier}",
        "check_suite": {"id": suite},
    }


def workflow_run_payload(
    identifier: int, workflow: str, conclusion: Optional[str], suite: int = 88, status: str = "completed"
) -> Dict[str, JsonValue]:
    return {
        "id": identifier,
        "name": workflow.removesuffix(".yml"),
        "path": f".github/workflows/{workflow}",
        "status": status,
        "conclusion": conclusion,
        "html_url": f"https://github.com/{REPOSITORY}/actions/runs/{identifier}",
        "check_suite_id": suite,
        "updated_at": "2026-11-10T08:00:00Z",
    }


def review_payload(identifier: int, state: str, author: str = "octocat", body: str = "") -> Dict[str, JsonValue]:
    return {
        "id": identifier,
        "state": state,
        "user": {"login": author},
        "body": body,
        "html_url": f"{PR_URL}#pullrequestreview-{identifier}",
    }


def comment_payload(identifier: int, body: str, author: str = "octocat") -> Dict[str, JsonValue]:
    return {
        "id": identifier,
        "user": {"login": author},
        "body": body,
        "html_url": f"{PR_URL}#discussion_r{identifier}",
    }


def deployment_routes(environment: str, deployment_id: int, state: str) -> Dict[str, JsonValue]:
    return {
        f"{API}/deployments?environment={environment}&sha={HEAD_SHA}": [
            {"id": deployment_id, "environment": environment}
        ],
        f"{API}/deployments/{deployment_id}/statuses": [
            {"state": state, "log_url": f"https://github.com/{REPOSITORY}/actions/runs/{deployment_id}"}
        ],
    }


def write_program(folder: Path, name: str, body: str) -> Path:
    """Write an executable shell script that stands for a program."""
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / name
    path.write_text("#!/usr/bin/env bash\n" + body + "\n", encoding="utf-8")
    path.chmod(path.stat().st_mode | stat.S_IXUSR)
    return path


def recorded_calls(log: Path) -> List[List[str]]:
    """Read the calls a recording program wrote, ended by a record separator, arguments split by a unit separator."""
    if not log.exists():
        return []
    return [record.split("\x1f") for record in log.read_text(encoding="utf-8").split("\x1e") if record]


def recording_body(log: Path, stdout: str = "", exit_code: int = 0) -> str:
    """Give the body of a program that records its name and arguments, prints a text and exits with a code."""
    return (
        '{ printf "%s" "$(basename "$0")"; for a in "$@"; do printf "\\x1f%s" "$a"; done; printf "\\x1e"; }'
        f' >> "{log}"\n'
        f"printf '%s' '{stdout}'\n"
        f"exit {exit_code}"
    )


def a_watch(root: Path, session: bool = True, number: int = 7, key: str = "GH-12") -> TicketWatch:
    """Build the watch of a pull request of the repository, owned by a session or not."""
    return TicketWatch(
        key=key,
        pull_request={"repository": REPOSITORY, "number": number, "root": str(root)},
        session={"session_id": SESSION_ID, "cwd": str(root)} if session else None,
        history={"registered_on": NOW - timedelta(days=1), "opened_on": NOW - timedelta(days=1, hours=2)},
    )


def an_event(
    watch: TicketWatch, suffix: str = "checks:668501e0d3a1", kind: EventKind = EventKind.CHECKS_FAILED
) -> PrEvent:
    """Build an event of a watched pull request."""
    return PrEvent(
        id=f"{watch.id}|{suffix}",
        kind=kind,
        detail={"title": "2 checks failed on 668501e0", "link": f"{PR_URL}/checks", "excerpt": "- unit: failure"},
        detected_on=NOW,
    )


def open_pull_request_routes(
    checks: Optional[List[Dict[str, JsonValue]]] = None,
    reviews: Optional[List[Dict[str, JsonValue]]] = None,
    comments: Optional[List[Dict[str, JsonValue]]] = None,
) -> Dict[str, JsonValue]:
    """Give the answers of every endpoint the watcher reads for the open pull request #7."""
    check_list: List[JsonValue] = [*(checks or [])]
    review_list: List[JsonValue] = [*(reviews or [])]
    comment_list: List[JsonValue] = [*(comments or [])]
    return {
        f"{API}/pulls/7": pull_request_payload(),
        f"{API}/commits/{HEAD_SHA}/check-runs": {"total_count": len(check_list), "check_runs": check_list},
        f"{API}/actions/runs?branch={HEAD_REF}&head_sha={HEAD_SHA}": {"total_count": 0, "workflow_runs": []},
        f"{API}/actions/runs?head_sha={HEAD_SHA}&status=waiting": {"total_count": 0, "workflow_runs": []},
        f"{API}/deployments?environment=dev&sha={HEAD_SHA}": [],
        f"{API}/deployments?environment=qa&sha={HEAD_SHA}": [],
        f"{API}/pulls/7/reviews": review_list,
        f"{API}/pulls/7/comments": comment_list,
        f"{API}/issues/7/comments": [],
        f"{API}/pulls?state=open": [pull_request_payload()],
    }
