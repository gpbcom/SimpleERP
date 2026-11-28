"""The guard follows the variables and the lines of a command to the folder a git write runs in (TKT-5, TKT-15)."""

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


class TestGuardVariables:
    @pytest.mark.parametrize(
        "command",
        [
            "W={harness} && git -C $W commit -F msg",
            "W={harness} && cd $W && git commit -m x",
            'export W="{harness}"; git -C "${{W}}" commit -m x',
            "ROOT={root}; W=$ROOT/harness && git -C $W commit -m x",
            "W='{harness}'\ngit -C $W add -A\ngit -C $W commit -m x",
        ],
    )
    def test_a_write_through_a_variable_is_judged_on_its_folder(self, tmp_path: Path, command: str) -> None:
        main, harness = tickets_and_harness(tmp_path)
        assert guard(command.format(harness=harness, root=tmp_path), main) == {}

    @pytest.mark.parametrize("command", ["W={main} && git -C $W commit -m x", "W={main} && cd $W && git commit -m x"])
    def test_a_write_into_the_tickets_checkout_through_a_variable_is_refused(
        self, tmp_path: Path, command: str
    ) -> None:
        main, harness = tickets_and_harness(tmp_path)
        assert guard(command.format(main=main), harness)["permissionDecision"] == "deny"

    @pytest.mark.parametrize(
        "command",
        [
            "git -C $NOWHERE commit -m x",
            "W={harness} && W=$(pwd) && git -C $W commit -m x",
            "W={harness} git -C $W commit -m x",
            "W={harness} | true; git -C $W commit -m x",
        ],
    )
    def test_a_variable_it_cannot_follow_keeps_the_session_s_folder(self, tmp_path: Path, command: str) -> None:
        main, harness = tickets_and_harness(tmp_path)
        assert guard(command.format(harness=harness), main)["permissionDecision"] == "deny"

    def test_a_cd_on_an_earlier_line_is_followed(self, tmp_path: Path) -> None:
        main, harness = tickets_and_harness(tmp_path)
        assert guard(f"cd {harness}\ngit add -A\ngit commit -m x", main) == {}
        assert guard(f"cd {main}\ngit add -A\ngit commit -m x", harness)["permissionDecision"] == "deny"

    @pytest.mark.parametrize("command", ["cd \\\n  {harness} && git commit -m x", "git -C \\\n  {harness} commit -m x"])
    def test_a_line_continued_by_a_backslash_is_one_line(self, tmp_path: Path, command: str) -> None:
        main, harness = tickets_and_harness(tmp_path)
        assert guard(command.format(harness=harness), main) == {}

    def test_a_write_split_over_two_lines_is_still_seen(self, tmp_path: Path) -> None:
        main, harness = tickets_and_harness(tmp_path)
        assert guard(f"git -C {main} \\\n  commit -m x", harness)["permissionDecision"] == "deny"

    def test_a_heredoc_body_is_text_and_not_a_command(self, tmp_path: Path) -> None:
        main, harness = tickets_and_harness(tmp_path)
        command = f"cat > msg <<'EOF'\ngit commit -m \"in the body\"\ncd {main}\nEOF\ncd {harness} && git commit -F msg"
        assert guard(command, main) == {}

    def test_a_message_over_several_lines_does_not_hide_where_the_write_ran(self, tmp_path: Path) -> None:
        main, harness = tickets_and_harness(tmp_path)
        command = f'git commit -m "first line\nsecond line" && cd {harness}'
        assert guard(command, main)["permissionDecision"] == "deny"

    @pytest.mark.parametrize("command", ["cd {harness} | true && git commit -m x", "cd {harness} & git commit -m x"])
    def test_a_cd_in_a_pipe_or_in_the_background_does_not_move_the_session(self, tmp_path: Path, command: str) -> None:
        main, harness = tickets_and_harness(tmp_path)
        assert guard(command.format(harness=harness), main)["permissionDecision"] == "deny"

    def test_an_option_on_another_line_is_not_an_option_of_git(self, tmp_path: Path) -> None:
        main = make_repo(tmp_path)
        git(main, "checkout", "-b", "feature/harness-guard")
        assert guard("git status\necho the hooks refuse --no-verify", main) == {}
