from __future__ import annotations

# Standard library imports
from pathlib import Path

# Third-party imports
import pytest

# First-party imports
from tests.harness.gitflow.helpers import BYPASS_ENV, commit, git, make_repo


class TestGitflowHooks:
    def test_a_commit_on_develop_is_refused(self, tmp_path: Path) -> None:
        main = make_repo(tmp_path)
        result = commit(main, "straight on develop")
        assert result.returncode != 0
        assert "pull request" in result.stderr

    def test_the_bypass_lets_the_person_commit_on_develop(self, tmp_path: Path) -> None:
        main = make_repo(tmp_path)
        assert commit(main, "a release fix", **{BYPASS_ENV: "1"}).returncode == 0

    @pytest.mark.parametrize("branch", ["feature/harness-gitflow", "release/0.1.0", "hotfix/fix-login", "bugfix/x"])
    def test_a_commit_on_a_gitflow_branch_is_accepted(self, tmp_path: Path, branch: str) -> None:
        main = make_repo(tmp_path)
        git(main, "checkout", "-b", branch)
        assert commit(main, "work").returncode == 0

    def test_a_branch_outside_gitflow_is_refused(self, tmp_path: Path) -> None:
        main = make_repo(tmp_path)
        git(main, "checkout", "-b", "my-stuff")
        result = commit(main, "work")
        assert result.returncode != 0
        assert "feature/" in result.stderr

    def test_a_worker_never_commits(self, tmp_path: Path) -> None:
        main = make_repo(tmp_path)
        git(main, "checkout", "-b", "worktree-wf_1")
        result = commit(main, "a task")
        assert result.returncode != 0
        assert "TKT-5" in result.stderr

    def test_a_ticket_commit_starts_with_its_id(self, tmp_path: Path) -> None:
        main = make_repo(tmp_path)
        git(main, "checkout", "-b", "feature/T0.09")
        assert commit(main, "Customer records").returncode != 0
        assert commit(main, "T0.09: Customer records with their VAT number").returncode == 0

    def test_a_commit_on_the_shared_branch_starts_with_a_ticket_id(self, tmp_path: Path) -> None:
        main = make_repo(tmp_path)
        git(main, "checkout", "-b", "feature/tickets")
        assert commit(main, "some work").returncode != 0
        assert commit(main, "T0.10: Observability base").returncode == 0

    def test_a_push_to_develop_is_refused_and_a_feature_branch_is_pushed(self, tmp_path: Path) -> None:
        main = make_repo(tmp_path)
        remote = tmp_path / "remote.git"
        git(tmp_path, "init", "--bare", str(remote))
        git(main, "remote", "add", "origin", str(remote))
        refused = git(main, "push", "origin", "develop")
        assert refused.returncode != 0
        assert "pull request" in refused.stderr
        git(main, "checkout", "-b", "feature/x")
        assert git(main, "push", "origin", "feature/x").returncode == 0

    def test_develop_and_master_are_never_deleted_on_github_and_a_merged_branch_is(self, tmp_path: Path) -> None:
        main = make_repo(tmp_path)
        remote = tmp_path / "remote.git"
        git(tmp_path, "init", "--bare", str(remote))
        git(main, "remote", "add", "origin", str(remote))
        git(main, "branch", "master")
        git(main, "branch", "feature/merged")
        assert git(main, "push", "origin", "develop", "master", "feature/merged", **{BYPASS_ENV: "1"}).returncode == 0
        for protected in ("develop", "master"):
            refused = git(main, "push", "origin", "--delete", protected)
            assert refused.returncode != 0
            assert "TKT-25" in refused.stderr
        assert git(main, "push", "origin", "--delete", "feature/merged").returncode == 0

    def test_a_ticket_of_phase_p10_commits_with_its_id(self, tmp_path: Path) -> None:
        main = make_repo(tmp_path)
        git(main, "checkout", "-b", "feature/T10.03")
        assert commit(main, "T1.03: wrong ticket").returncode != 0
        assert commit(main, "T10.03: Hosted backups").returncode == 0

    def test_the_bypass_lets_the_person_make_the_first_push_of_develop(self, tmp_path: Path) -> None:
        main = make_repo(tmp_path)
        remote = tmp_path / "remote.git"
        git(tmp_path, "init", "--bare", str(remote))
        git(main, "remote", "add", "origin", str(remote))
        assert git(main, "push", "origin", "develop").returncode != 0
        assert git(main, "push", "origin", "develop", **{BYPASS_ENV: "1"}).returncode == 0
