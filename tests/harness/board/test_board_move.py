"""Moving a card never changes a tracked file: the card columns are a local cache, not the board's state (TKT-17)."""

from __future__ import annotations

# Standard library imports
import json
from pathlib import Path
from typing import Dict, List, Tuple

# First-party imports
from tests.harness.board.test_board_refresh import expected_issues
from tests.harness.roadmap_gantt.helpers import make_roadmap_repo, run_script

STATUSES = ("backlog", "ready", "planned", "running", "review", "done")


def board_state(repo: Path, items: Dict[str, Dict[str, str]]) -> Tuple[str, str]:
    """Write a bootstrapped board's ``.claude/github.json`` and return a ticket and the file's text."""
    expected = expected_issues(repo)
    issues = {ident: {"number": n, "node": f"node{n}", "db": n} for n, ident in enumerate(sorted(expected), start=1)}
    state = {
        "repo": "o/r",
        "project": {"id": "project", "status_field": "field", "status": {s: f"option-{s}" for s in STATUSES}},
        "milestones": {},
        "issues": issues,
        "subissues": [],
        "blocked": [],
        "items": {ident: {"id": f"item-{ident}", **items.get(ident, {})} for ident in issues},
        "closed": [],
    }
    (repo / ".claude").mkdir(exist_ok=True)
    text = json.dumps(state, indent=1, ensure_ascii=False, sort_keys=True) + "\n"
    (repo / ".claude" / "github.json").write_text(text, encoding="utf-8")
    return next(i for i in sorted(expected) if i.startswith("T")), text


def recording_gh(tmp_path: Path) -> Tuple[str, Path]:
    """Write a ``gh`` stand-in that records every request it is sent and answers an empty GraphQL result."""
    folder = tmp_path / "bin"
    folder.mkdir()
    calls = tmp_path / "calls.log"
    gh = folder / "gh"
    gh.write_text(f"#!/bin/sh\ncat >> {calls}\necho >> {calls}\necho '{{\"data\": {{}}}}'\n", encoding="utf-8")
    gh.chmod(0o755)
    return str(folder), calls


def updates(calls: Path) -> List[str]:
    """Return the card moves the stand-in received."""
    if not calls.is_file():
        return []
    return [line for line in calls.read_text(encoding="utf-8").splitlines() if "updateProjectV2ItemFieldValue" in line]


class TestBoardMove:
    def test_a_move_leaves_the_tracked_board_state_unchanged(self, tmp_path: Path) -> None:
        repo = make_roadmap_repo(tmp_path)
        ticket, before = board_state(repo, {})
        path, _ = recording_gh(tmp_path)
        result = run_script("github/board.py", repo, "move", "--ticket", ticket, "--status", "running", path=path)
        assert result.returncode == 0, result.stderr
        assert (repo / ".claude" / "github.json").read_text(encoding="utf-8") == before

    def test_a_card_already_in_its_column_is_not_moved_again(self, tmp_path: Path) -> None:
        repo = make_roadmap_repo(tmp_path)
        ticket, _ = board_state(repo, {})
        path, calls = recording_gh(tmp_path)
        assert (
            run_script("github/board.py", repo, "move", "--ticket", ticket, "--status", "running", path=path).returncode
            == 0
        )
        first = len(updates(calls))
        assert (
            run_script("github/board.py", repo, "move", "--ticket", ticket, "--status", "running", path=path).returncode
            == 0
        )
        assert first > 0
        assert len(updates(calls)) == first

    def test_a_column_recorded_by_an_older_board_state_is_still_known(self, tmp_path: Path) -> None:
        repo = make_roadmap_repo(tmp_path)
        expected = expected_issues(repo)
        ticket = next(i for i in sorted(expected) if i.startswith("T"))
        board_state(repo, {ident: {"status": "running"} for ident in expected})
        path, calls = recording_gh(tmp_path)
        assert (
            run_script("github/board.py", repo, "move", "--ticket", ticket, "--status", "running", path=path).returncode
            == 0
        )
        assert all("item-" + ticket not in line for line in updates(calls))
        state = json.loads((repo / ".claude" / "github.json").read_text(encoding="utf-8"))
        assert all("status" not in item for item in state["items"].values())
