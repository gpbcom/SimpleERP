"""The checks clean up after themselves, even after a run that was killed (TKT-27)."""

from __future__ import annotations

# Standard library imports
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path
from typing import Iterator, List

# Third-party imports
import pytest

# First-party imports
from tests.harness.checks.test_checks import MINE, ROOT, TICKET, git, two_tickets_at_work

SCRIPTS = ROOT / ".claude" / "scripts" / "tickets"


def call(code: str) -> object:
    """Run ``code`` with the checks module imported as ``checks``, and return what it prints as JSON."""
    script = f"import sys, json; sys.path.insert(0, {str(SCRIPTS)!r}); import checks; from pathlib import Path; {code}"
    result = subprocess.run([sys.executable, "-c", script], capture_output=True, text=True, check=True)
    return json.loads(result.stdout)


def a_repo(tmp_path: Path) -> Path:
    """Return two tickets at work in a repository of its own folder, beside the temporary folder of the test."""
    (tmp_path / "repo").mkdir()
    return two_tickets_at_work(tmp_path / "repo", [MINE, f"docs/tickets/{TICKET}/"])


def worktrees(repo: Path) -> List[str]:
    listed = subprocess.run(["git", "worktree", "list", "--porcelain"], cwd=repo, capture_output=True, text=True)
    return [line.removeprefix("worktree ") for line in listed.stdout.splitlines() if line.startswith("worktree ")]


def a_left_tree(repo: Path, temp: Path, name: str) -> Path:
    """Make a clean tree in ``temp`` the way a killed run of the checks leaves it: a registered worktree."""
    tree = temp / name
    git(repo, "worktree", "add", "--detach", str(tree), "HEAD")
    return tree


def sweep(repo: Path, temp: Path) -> object:
    return call(
        f"print(json.dumps([p.name for p in checks.sweep_stale_trees(Path({str(repo)!r}), Path({str(temp)!r}))]))"
    )


def gone_pid() -> int:
    process = subprocess.Popen([sys.executable, "-c", "pass"])
    process.wait()
    return process.pid


@pytest.fixture
def running_pid() -> Iterator[int]:
    process = subprocess.Popen([sys.executable, "-c", "import time; time.sleep(60)"])
    yield process.pid
    process.kill()
    process.wait()


class TestChecksCleanup:
    def test_a_clean_tree_left_by_a_run_that_is_gone_is_removed(self, tmp_path: Path) -> None:
        repo = a_repo(tmp_path)
        temp = tmp_path / "tmp"
        temp.mkdir()
        tree = a_left_tree(repo, temp, f"erp-checks-{gone_pid()}-abc")
        assert sweep(repo, temp) == [tree.name]
        assert not tree.exists()
        assert str(tree) not in worktrees(repo)

    def test_the_clean_tree_of_a_run_still_going_is_kept(self, tmp_path: Path, running_pid: int) -> None:
        repo = a_repo(tmp_path)
        temp = tmp_path / "tmp"
        temp.mkdir()
        tree = a_left_tree(repo, temp, f"erp-checks-{running_pid}-abc")
        assert sweep(repo, temp) == []
        assert tree.is_dir()

    @pytest.mark.parametrize(("age_s", "removed"), [(2 * 3600, True), (60, False)])
    def test_a_tree_named_before_the_process_ids_is_removed_once_an_hour_old(
        self, tmp_path: Path, age_s: int, removed: bool
    ) -> None:
        repo = a_repo(tmp_path)
        temp = tmp_path / "tmp"
        temp.mkdir()
        tree = a_left_tree(repo, temp, "erp-checks-tvssessb")
        then = time.time() - age_s
        os.utime(tree, (then, then))
        assert (sweep(repo, temp) == [tree.name]) is removed
        assert tree.exists() is not removed

    def test_a_tree_that_cannot_be_made_leaves_no_folder_and_no_worktree(self, tmp_path: Path) -> None:
        repo = tmp_path / "empty"
        repo.mkdir()
        git(repo, "init", "-q")
        temp = tmp_path / "tmp"
        temp.mkdir()
        script = (
            f"import sys; sys.path.insert(0, {str(SCRIPTS)!r}); import checks; from pathlib import Path; "
            f"checks.isolated_tree([], Path({str(repo)!r}), Path({str(temp)!r}))"
        )
        result = subprocess.run([sys.executable, "-c", script], capture_output=True, text=True)
        assert result.returncode != 0
        assert "Could not make the clean worktree" in result.stderr
        assert list(temp.iterdir()) == []
        assert worktrees(repo) == [str(repo)]

    def test_a_clean_tree_goes_with_the_temporary_files_of_pytest_beside_it(self, tmp_path: Path) -> None:
        repo = a_repo(tmp_path)
        temp = tmp_path / "tmp"
        temp.mkdir()
        made = call(
            f"repo = Path({str(repo)!r}); changed = checks.changed_files('develop', {TICKET!r}, repo); "
            f"tree = checks.isolated_tree(changed, repo, Path({str(temp)!r})); "
            f"side = checks.pytest_temp(tree); side.mkdir(); (side / 'f').write_text('x'); "
            f"checks.remove_tree(tree, repo); print(json.dumps({{'tree': tree.exists(), 'side': side.exists(), "
            f"'name': tree.name}}))"
        )
        assert isinstance(made, dict)
        assert re.fullmatch(r"erp-checks-\d+-\w+", made["name"])
        assert made["tree"] is False
        assert made["side"] is False
        assert list(temp.iterdir()) == []

    def test_pytest_keeps_its_temporary_files_beside_the_clean_tree(self, tmp_path: Path) -> None:
        tree = tmp_path / "erp-checks-123-abc"
        command = call(f"print(json.dumps(checks.pytest_command('backend/models/tests', Path({str(tree)!r}))))")
        assert isinstance(command, list)
        assert command[command.index("--basetemp") + 1] == str(
            tmp_path / "erp-checks-123-abc-pytest" / "backend-models-tests"
        )
        # A checkout that is no clean tree keeps pytest's default. The repository's root is no example: the checks
        # run these very tests inside a clean tree named erp-checks-<pid>-.
        checkout = tmp_path / "checkout"
        command = call(f"print(json.dumps(checks.pytest_command('tests', Path({str(checkout)!r}))))")
        assert isinstance(command, list)
        assert "--basetemp" not in command
        assert not checkout.exists()

    def test_pytest_runs_with_the_temporary_folder_it_is_given_beside_the_clean_tree(self, tmp_path: Path) -> None:
        tree = tmp_path / "erp-checks-123-abc"
        (tree / "tests").mkdir(parents=True)
        (tree / "tests" / "test_one.py").write_text("def test_one(tmp_path):\n    assert tmp_path.is_dir()\n")
        command = call(f"print(json.dumps(checks.pytest_command('tests', Path({str(tree)!r}))))")
        assert isinstance(command, list)
        basetemp = command[command.index("--basetemp") + 1]
        result = subprocess.run(
            [sys.executable, "-m", "pytest", "tests", "-q", "-p", "no:cacheprovider", "--basetemp", basetemp],
            cwd=tree,
            capture_output=True,
            text=True,
            check=False,
        )
        assert result.returncode == 0, result.stdout + result.stderr
