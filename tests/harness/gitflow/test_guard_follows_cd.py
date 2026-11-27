"""The guard judges the branch of the folder a git write runs in: a ``cd`` before it or ``git -C`` (TKT-5, TKT-15)."""

from __future__ import annotations

# Standard library imports
from pathlib import Path
from typing import Tuple

# Third-party imports
import pytest

# First-party imports
from tests.harness.gitflow.helpers import git, guard, make_repo


def tickets_and_harness(tmp_path: Path) -> Tuple[Path, Path]:
    """Return a main checkout on the tickets' branch and a worktree of it on a harness branch."""
    main = make_repo(tmp_path)
    git(main, "checkout", "-b", "feature/tickets")
    harness = tmp_path / "harness"
    git(main, "worktree", "add", "-b", "feature/harness-guard", str(harness))
    return main, harness


class TestGuardFollowsCd:
    @pytest.mark.parametrize(
        "command",
        [
            "cd {harness} && git commit -m x",
            "cd {harness}; git add -A && git commit -m x",
            "git -C {harness} commit -m x",
            "cd /tmp && cd {harness} && git push -u origin feature/harness-guard",
            'cd "{harness}" && git commit -m "x"',
        ],
    )
    def test_a_write_in_a_harness_worktree_is_judged_on_its_branch(self, tmp_path: Path, command: str) -> None:
        main, harness = tickets_and_harness(tmp_path)
        assert guard(command.format(harness=harness), main) == {}

    @pytest.mark.parametrize(
        "command",
        [
            "cd {main} && git commit -m x",
            "git -C {main} commit -m x",
            "cd {harness} && cd {main} && git commit -m x",
        ],
    )
    def test_a_write_moved_into_the_tickets_checkout_is_still_refused(self, tmp_path: Path, command: str) -> None:
        main, harness = tickets_and_harness(tmp_path)
        decision = guard(command.format(harness=harness, main=main), harness)
        assert decision["permissionDecision"] == "deny"

    @pytest.mark.parametrize("command", ["cd $SOMEWHERE && git commit -m x", "cd /no/such/folder && git commit -m x"])
    def test_a_folder_it_cannot_resolve_keeps_the_session_s_folder(self, tmp_path: Path, command: str) -> None:
        main, _ = tickets_and_harness(tmp_path)
        assert guard(command, main)["permissionDecision"] == "deny"

    def test_a_cd_after_the_write_does_not_change_where_the_write_ran(self, tmp_path: Path) -> None:
        main, harness = tickets_and_harness(tmp_path)
        assert guard(f"git commit -m x && cd {harness}", main)["permissionDecision"] == "deny"
