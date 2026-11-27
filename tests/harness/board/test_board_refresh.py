from __future__ import annotations

# Standard library imports
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Dict, List

# First-party imports
from tests.harness.roadmap_gantt.helpers import make_roadmap_repo, run_script

ROOT = Path(__file__).resolve().parents[3]
SCRIPTS = ROOT / ".claude" / "scripts" / "github"
EXPECTED = (
    "import json, sys; sys.path.insert(0, {scripts!r}); import board; "
    "b = board.Board(dry_run=True); print(json.dumps(b.expected_issues()))"
)


def expected_issues(repo: Path) -> Dict[str, List[object]]:
    """Return what the board would write for each phase, epic and ticket of ``repo``."""
    result = subprocess.run(
        [sys.executable, "-c", EXPECTED.format(scripts=str(SCRIPTS))],
        capture_output=True,
        text=True,
        check=True,
        env={**os.environ, "ERP_REPOSITORY": str(repo)},
        cwd=repo,
    )
    return json.loads(result.stdout.strip().splitlines()[-1])


def github_as_it_is(repo: Path, tmp_path: Path, changes: Dict[str, Dict[str, object]]) -> Path:
    """Write the state of a bootstrapped board and a ``gh`` stand-in that lists its issues, ``changes`` applied."""
    expected = expected_issues(repo)
    issues, listed = {}, []
    for number, (ident, (title, body, labels)) in enumerate(sorted(expected.items()), start=1):
        issues[ident] = {"number": number, "node": f"node{number}", "db": number}
        listed.append({"number": number, "title": title, "body": body, "labels": [{"name": n} for n in labels]})
        listed[-1].update(changes.get(ident, {}))
    state = {
        "repo": "o/r",
        "milestones": {},
        "issues": issues,
        "subissues": [],
        "blocked": [],
        "items": {},
        "closed": [],
    }
    (repo / ".claude").mkdir(exist_ok=True)
    (repo / ".claude" / "github.json").write_text(json.dumps(state), encoding="utf-8")
    listing = tmp_path / "issues.json"
    listing.write_text(json.dumps(listed), encoding="utf-8")
    folder = tmp_path / "bin"
    folder.mkdir()
    gh = folder / "gh"
    gh.write_text(
        f'#!/bin/sh\ncase "$*" in *"issues?state=all"*) cat {listing} ;; *) echo "[]" ;; esac\n', encoding="utf-8"
    )
    gh.chmod(0o755)
    return folder


class TestBoardRefresh:
    def test_the_dry_run_names_only_the_issues_whose_text_changed(self, tmp_path: Path) -> None:
        repo = make_roadmap_repo(tmp_path)
        expected = expected_issues(repo)
        ticket = next(i for i in sorted(expected) if i.startswith("T"))
        epic = next(i for i in sorted(expected) if i.startswith("E"))
        phase = next(i for i in sorted(expected) if i.startswith("P"))
        changes = {
            ticket: {"body": "An older text of the ticket."},
            epic: {"title": "E0.1: An older name"},
            phase: {"labels": [{"name": n} for n in expected[phase][2]] + [{"name": "a person's label"}]},
        }
        path = github_as_it_is(repo, tmp_path, changes)
        result = run_script("github/board.py", repo, "refresh", "--dry-run", path=str(path))
        assert result.returncode == 0, result.stderr
        assert f"{ticket}" in result.stdout
        assert f"{epic}" in result.stdout
        assert phase not in [line.split()[-1] for line in result.stdout.splitlines() if "would update" in line]
        assert "2 issues to update" in result.stdout

    def test_a_missing_roadmap_label_is_put_back(self, tmp_path: Path) -> None:
        repo = make_roadmap_repo(tmp_path)
        expected = expected_issues(repo)
        ticket = next(i for i in sorted(expected) if i.startswith("T"))
        changes = {ticket: {"labels": [{"name": n} for n in expected[ticket][2][1:]]}}
        path = github_as_it_is(repo, tmp_path, changes)
        result = run_script("github/board.py", repo, "refresh", "--dry-run", path=str(path))
        assert result.returncode == 0, result.stderr
        assert "1 issues to update" in result.stdout

    def test_an_unchanged_board_needs_no_update(self, tmp_path: Path) -> None:
        repo = make_roadmap_repo(tmp_path)
        path = github_as_it_is(repo, tmp_path, {})
        result = run_script("github/board.py", repo, "refresh", "--dry-run", path=str(path))
        assert result.returncode == 0, result.stderr
        assert "0 issues to update" in result.stdout
