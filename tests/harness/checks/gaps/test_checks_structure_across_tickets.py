"""The folder limit is checked on the code as it will be once every open ticket is merged (TKT-6, TKT-16).

Each ticket's checks run in a clean tree with its own files only, so two tickets that each kept a folder at five
Python files broke the limit together, and only CI saw it, on the shared pull request (T0.18 and T0.19).
"""

from __future__ import annotations

# Standard library imports
import json
import shutil
from pathlib import Path
from typing import Dict, List

# First-party imports
from tests.harness.checks.helpers import ROOT, call
from tests.harness.checks.test_checks import git

MINE = "T9.01"
THEIRS = "T9.02"
FOLDER = "backend/services/sales/tests/service"
NAME = "structure with open tickets"


def a_repo_with_open_tickets(tmp_path: Path, committed: List[str], tickets: Dict[str, List[str]]) -> Path:
    """Return a repository whose folder ``FOLDER`` holds ``committed``, with each ticket's paths open in its checkout.

    A path of a ticket is written in the working tree, unless it is committed (the ticket deletes it) or a folder.
    """
    repo = tmp_path / "repo"
    (repo / "tests" / "conventions").mkdir(parents=True)
    shutil.copy(ROOT / "tests" / "conventions" / "helpers.py", repo / "tests" / "conventions" / "helpers.py")
    (repo / FOLDER).mkdir(parents=True)
    for name in committed:
        (repo / FOLDER / name).write_text("x = 1\n", encoding="utf-8")
    git(repo, "init", "-q", "-b", "develop")
    git(repo, "add", "-A")
    git(repo, "commit", "-q", "-m", "base")
    for ticket, paths in tickets.items():
        for path in paths:
            if path.endswith("/") or path.removeprefix(f"{FOLDER}/") in committed:
                continue
            (repo / path).parent.mkdir(parents=True, exist_ok=True)
            (repo / path).write_text("x = 1\n", encoding="utf-8")
        state = repo / ".git" / "erp" / ticket
        state.mkdir(parents=True)
        recorded = [*paths, f"docs/tickets/{ticket}/"]
        (state / "state.json").write_text(json.dumps({"ticket": ticket, "paths": recorded}), encoding="utf-8")
    for name in committed:
        if any(f"{FOLDER}/{name}" in paths for paths in tickets.values()):
            (repo / FOLDER / name).unlink()
    return repo


def structure(tmp_path: Path, repo: Path) -> Dict[str, object]:
    """Run the check for ``MINE`` in its clean tree, as ``main`` does, and return its verdict."""
    evidence = tmp_path / "evidence"
    setup = (
        f"repo = Path({str(repo)!r}); checks.ROOT = Path({str(evidence)!r})\n"
        f"changed = checks.changed_files('develop', {MINE!r}, repo)\n"
        "tree = checks.isolated_tree(changed, repo)\n"
        f"c = checks.Checks({MINE!r}, tree, changed)\n"
        "try:\n    checks.structure_checks(c)\n"
        "finally:\n    checks.remove_tree(tree, repo)"
    )
    verdict = call("{'failures': c.failures, 'not_applicable': c.not_applicable, 'passed': c.passed}", setup)
    assert isinstance(verdict, dict)
    return verdict


def files(*names: str) -> List[str]:
    return [f"{FOLDER}/{name}" for name in names]


class TestChecksStructureAcrossTickets:
    def test_two_tickets_that_crowd_one_folder_together_fail_naming_the_folder_and_both_tickets(
        self, tmp_path: Path
    ) -> None:
        repo = a_repo_with_open_tickets(
            tmp_path,
            ["test_a.py", "test_b.py", "test_c.py"],
            {MINE: files("test_d.py"), THEIRS: files("test_e.py", "test_f.py")},
        )
        verdict = structure(tmp_path, repo)
        failures = verdict["failures"]
        assert isinstance(failures, list)
        assert [(f["check"], f["file"], f["environment"]) for f in failures] == [(NAME, f"{FOLDER}/test_d.py", False)]
        detail = failures[0]["detail"]
        assert f"{FOLDER} would hold 6 Python files" in detail
        assert f"{MINE} has test_d.py" in detail
        assert f"{THEIRS} has test_e.py, test_f.py" in detail
        assert "already committed: test_a.py, test_b.py, test_c.py" in detail

    def test_a_folder_another_ticket_recorded_is_expanded_from_the_main_checkout(self, tmp_path: Path) -> None:
        repo = a_repo_with_open_tickets(
            tmp_path, ["test_a.py", "test_b.py", "test_c.py"], {MINE: files("test_d.py"), THEIRS: [f"{FOLDER}/"]}
        )
        for name in ("test_e.py", "test_f.py"):
            (repo / FOLDER / name).write_text("x = 1\n", encoding="utf-8")
        verdict = structure(tmp_path, repo)
        failures = verdict["failures"]
        assert isinstance(failures, list)
        assert [f["file"] for f in failures] == [f"{FOLDER}/test_d.py"]
        assert THEIRS in failures[0]["detail"]

    def test_five_files_with_the_open_tickets_pass(self, tmp_path: Path) -> None:
        repo = a_repo_with_open_tickets(
            tmp_path, ["test_a.py", "test_b.py", "test_c.py"], {MINE: files("test_d.py"), THEIRS: files("test_e.py")}
        )
        verdict = structure(tmp_path, repo)
        assert verdict["failures"] == []
        assert verdict["passed"] == [NAME]

    def test_init_and_conftest_files_do_not_count(self, tmp_path: Path) -> None:
        repo = a_repo_with_open_tickets(
            tmp_path,
            ["test_a.py", "test_b.py", "test_c.py"],
            {MINE: files("test_d.py", "__init__.py"), THEIRS: files("test_e.py", "conftest.py")},
        )
        assert structure(tmp_path, repo)["failures"] == []

    def test_a_file_a_ticket_deletes_no_longer_counts(self, tmp_path: Path) -> None:
        repo = a_repo_with_open_tickets(
            tmp_path,
            ["test_a.py", "test_b.py", "test_c.py", "test_x.py"],
            {MINE: files("test_d.py", "test_x.py"), THEIRS: files("test_e.py")},
        )
        assert structure(tmp_path, repo)["failures"] == []

    def test_a_folder_outside_the_source_and_test_folders_is_not_counted(self, tmp_path: Path) -> None:
        scripts = [f"docs/scripts/s{n}.py" for n in range(6)]
        repo = a_repo_with_open_tickets(tmp_path, [], {MINE: scripts[:3], THEIRS: scripts[3:]})
        assert structure(tmp_path, repo)["failures"] == []

    def test_no_other_open_ticket_makes_the_check_not_applicable(self, tmp_path: Path) -> None:
        repo = a_repo_with_open_tickets(tmp_path, ["test_a.py"], {MINE: files("test_d.py")})
        verdict = structure(tmp_path, repo)
        assert verdict["not_applicable"] == [f"{NAME}: no other ticket is open"]
        assert verdict["passed"] == []

    def test_the_checks_of_a_ticket_include_the_folder_limit_across_tickets(self, tmp_path: Path) -> None:
        repo = a_repo_with_open_tickets(tmp_path, ["test_a.py"], {MINE: files("test_d.py")})
        setup = (
            f"repo = Path({str(repo)!r}); checks.ROOT = Path({str(tmp_path / 'evidence')!r})\n"
            f"verdict = checks.run_checks({MINE!r}, 'develop', [], repo)"
        )
        verdict = call("verdict", setup)
        assert isinstance(verdict, dict)
        assert f"{NAME}: no other ticket is open" in verdict["not_applicable"]
