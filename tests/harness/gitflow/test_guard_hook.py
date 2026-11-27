from __future__ import annotations

# Standard library imports
from pathlib import Path

# Third-party imports
import pytest

# First-party imports
from tests.harness.gitflow.helpers import git, guard, make_repo


class TestGuardHook:
    @pytest.mark.parametrize(
        "command",
        [
            "git commit -m wip",
            "git merge develop",
            "git push origin feature/T0.09",
            "git reset --hard HEAD~1",
            "git stash",
            "git rebase develop",
            "gh pr merge 12",
        ],
    )
    def test_agents_in_a_ticket_worktree_leave_git_to_ticket_tree(self, tmp_path: Path, command: str) -> None:
        main = make_repo(tmp_path)
        git(main, "checkout", "-b", "feature/T0.09")
        decision = guard(command, main)
        assert decision["permissionDecision"] == "deny"
        assert "ticket_tree.py" in str(decision["permissionDecisionReason"])

    def test_agents_on_the_shared_branch_leave_git_to_ticket_tree(self, tmp_path: Path) -> None:
        main = make_repo(tmp_path)
        git(main, "checkout", "-b", "feature/tickets")
        assert guard("git commit -m wip", main)["permissionDecision"] == "deny"
        assert guard("git push origin feature/tickets", main)["permissionDecision"] == "deny"

    def test_approving_a_group_of_plans_asks_the_person(self, tmp_path: Path) -> None:
        main = make_repo(tmp_path)
        decision = guard("python3 .claude/scripts/tickets/tickets.py approve '#12'", main)
        assert decision["permissionDecision"] == "ask"
        assert "TKT-3" in str(decision["permissionDecisionReason"])

    def test_starting_a_release_asks_the_person(self, tmp_path: Path) -> None:
        main = make_repo(tmp_path)
        decision = guard("gh workflow run release.yml --ref develop -f version=0.1.0", main)
        assert decision["permissionDecision"] == "ask"
        assert "TKT-26" in str(decision["permissionDecisionReason"])

    def test_a_worker_cannot_commit_either(self, tmp_path: Path) -> None:
        main = make_repo(tmp_path)
        git(main, "checkout", "-b", "worktree-wf_3")
        assert guard("git add -A && git commit -m x", main)["permissionDecision"] == "deny"

    @pytest.mark.parametrize(
        "command",
        [
            "git status",
            "git diff develop",
            "python3 .claude/scripts/tickets/ticket_tree.py finish --ticket T0.09",
            "git log --oneline",
        ],
    )
    def test_reading_git_and_the_harness_scripts_are_allowed(self, tmp_path: Path, command: str) -> None:
        main = make_repo(tmp_path)
        git(main, "checkout", "-b", "feature/T0.09")
        assert guard(command, main) == {}

    def test_skipping_the_hooks_is_refused_everywhere(self, tmp_path: Path) -> None:
        main = make_repo(tmp_path)
        assert guard("git commit --no-verify -m x", main)["permissionDecision"] == "deny"

    def test_words_in_a_message_or_a_script_are_not_options(self, tmp_path: Path) -> None:
        main = make_repo(tmp_path)
        git(main, "checkout", "-b", "feature/harness-gitflow")
        heredoc = "git commit -q -F - <<'EOF'\nThe hooks refuse --no-verify and git push origin develop.\nEOF"
        assert guard(heredoc, main) == {}
        assert guard('git commit -m "the hooks refuse --no-verify"', main) == {}

    def test_a_push_to_develop_from_the_main_checkout_asks_the_person(self, tmp_path: Path) -> None:
        main = make_repo(tmp_path)
        assert guard("git push origin develop", main)["permissionDecision"] == "ask"

    @pytest.mark.parametrize(
        ("branch", "command"),
        [
            ("master", "git rebase develop"),
            ("master", "git reset --hard origin/develop"),
            ("develop", "git rebase origin/develop"),
            ("feature/live", "git rebase develop master"),
            ("feature/live", "git push --force origin master"),
            ("feature/live", "git push -f origin develop"),
            ("feature/live", "git push origin +master"),
            ("feature/live", "git push origin --delete develop"),
        ],
    )
    def test_develop_and_master_are_never_rebased_reset_or_forced(
        self, tmp_path: Path, branch: str, command: str
    ) -> None:
        main = make_repo(tmp_path)
        git(main, "checkout", "-b", branch)
        decision = guard(command, main)
        assert decision["permissionDecision"] == "deny"
        assert "TKT-25" in str(decision["permissionDecisionReason"])

    def test_a_live_branch_is_rebased_onto_develop(self, tmp_path: Path) -> None:
        main = make_repo(tmp_path)
        git(main, "checkout", "-b", "feature/live")
        assert guard("git rebase origin/develop", main) == {}
        assert guard("git push --force-with-lease origin feature/live", main) == {}

    def test_the_person_s_own_git_work_in_the_main_checkout_is_left_alone(self, tmp_path: Path) -> None:
        main = make_repo(tmp_path)
        git(main, "checkout", "-b", "feature/harness-gitflow")
        assert guard("git commit -m 'harness: gitflow'", main) == {}
