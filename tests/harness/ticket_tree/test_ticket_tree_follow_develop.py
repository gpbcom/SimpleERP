"""The shared branch follows develop while tickets run, keeping their uncommitted work (TKT-5, TKT-16)."""

from __future__ import annotations

# Standard library imports
from pathlib import Path
from typing import Tuple

# First-party imports
from tests.harness.ticket_tree.helpers import SHARED_BRANCH, TICKET_FOLDER, git, make_repo, run, run_json


def develop_moves(tmp_path: Path, main: Path, files: dict) -> str:
    """Commit ``files`` on develop in another clone, push it, and return the new develop commit."""
    other = tmp_path / "other"
    git(tmp_path, "clone", "-q", "-b", "develop", str(tmp_path / "remote.git"), str(other))
    for name, text in files.items():
        (other / name).parent.mkdir(parents=True, exist_ok=True)
        (other / name).write_text(text, encoding="utf-8")
    git(other, "add", "-A")
    git(other, "commit", "-q", "-m", "a harness fix on develop")
    git(other, "push", "-q", "origin", "develop")
    return git(other, "rev-parse", "HEAD")


def tickets_at_work(tmp_path: Path) -> Tuple[Path, str]:
    """Return a main checkout on the shared branch, from origin/develop, with the ticket's uncommitted work."""
    main = make_repo(tmp_path)
    git(tmp_path, "init", "-q", "--bare", "-b", "develop", str(tmp_path / "remote.git"))
    git(main, "remote", "add", "origin", str(tmp_path / "remote.git"))
    git(main, "push", "-q", "origin", "develop")
    assert run(main, "prepare").returncode == 0
    (main / "a.txt").write_text("A\nb\nc\n", encoding="utf-8")
    (main / "mine.txt").write_text("the ticket's new file\n", encoding="utf-8")
    return main, git(main, "rev-parse", "HEAD")


class TestTicketTreeFollowDevelop:
    def test_the_shared_branch_moves_to_develop_and_keeps_the_tickets_work(self, tmp_path: Path) -> None:
        main, _ = tickets_at_work(tmp_path)
        target = develop_moves(tmp_path, main, {"a.txt": "a\nb\nC\n", "harness.txt": "fixed\n"})
        result = run_json(main, "follow-develop")
        assert result["moved"] is True
        assert git(main, "rev-parse", "HEAD") == target
        assert git(main, "branch", "--show-current") == SHARED_BRANCH
        assert (main / "a.txt").read_text(encoding="utf-8") == "A\nb\nC\n"
        assert (main / "harness.txt").read_text(encoding="utf-8") == "fixed\n"
        assert (main / "mine.txt").is_file()
        assert (main / TICKET_FOLDER / "TICKET.md").is_file()
        assert git(main, "diff", "--name-only", "HEAD", "--", "a.txt") == "a.txt"

    def test_a_conflict_changes_nothing(self, tmp_path: Path) -> None:
        main, before = tickets_at_work(tmp_path)
        develop_moves(tmp_path, main, {"a.txt": "X\nb\nc\n", "harness.txt": "fixed\n"})
        result = run(main, "follow-develop")
        assert result.returncode == 1
        assert "a.txt" in result.stderr
        assert git(main, "rev-parse", "HEAD") == before
        assert (main / "a.txt").read_text(encoding="utf-8") == "A\nb\nc\n"
        assert not (main / "harness.txt").exists()

    def test_a_shared_branch_with_its_own_commits_is_left_alone(self, tmp_path: Path) -> None:
        main, _ = tickets_at_work(tmp_path)
        (main / "committed.txt").write_text("finished ticket\n", encoding="utf-8")
        git(main, "add", "committed.txt")
        git(main, "commit", "-q", "-m", "T9.01: a finished ticket not merged yet")
        before = git(main, "rev-parse", "HEAD")
        develop_moves(tmp_path, main, {"harness.txt": "fixed\n"})
        result = run(main, "follow-develop")
        assert result.returncode == 1
        assert "develop" in result.stderr
        assert git(main, "rev-parse", "HEAD") == before

    def test_run_again_when_up_to_date_does_nothing(self, tmp_path: Path) -> None:
        main, before = tickets_at_work(tmp_path)
        assert run_json(main, "follow-develop")["moved"] is False
        assert git(main, "rev-parse", "HEAD") == before
        assert (main / "a.txt").read_text(encoding="utf-8") == "A\nb\nc\n"
