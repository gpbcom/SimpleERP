from __future__ import annotations

from pathlib import Path

import pytest

from pr_watch.storage.git.exceptions import SECloneNotOnGithubError
from pr_watch.storage.git.pull_request_clone import PullRequestClone
from tests.stand_ins.git_sandbox import GitSandbox
from tests.stand_ins.helpers import HEAD_REF


class TestPullRequestClone:
    def test_a_conflict_with_the_base_is_found_in_memory(self, tmp_path: Path) -> None:
        sandbox = GitSandbox(tmp_path)
        clone = sandbox.build(conflict=True)
        result = PullRequestClone(clone).probe("develop", HEAD_REF)
        assert result.error is None
        assert result.conflict_files == ["a.txt"]
        assert "CONFLICT" in result.messages
        assert result.head_sha == sandbox.git(clone, "rev-parse", f"origin/{HEAD_REF}")
        assert (clone / "a.txt").read_text(encoding="utf-8") == "develop\n"
        assert sandbox.git(clone, "status", "--porcelain") == ""

    def test_a_clean_merge_has_no_conflict(self, tmp_path: Path) -> None:
        clone = GitSandbox(tmp_path).build(conflict=False)
        result = PullRequestClone(clone).probe("develop", HEAD_REF)
        assert (result.error, result.conflict_files) == (None, [])

    def test_the_remote_tracking_refs_never_move(self, tmp_path: Path) -> None:
        sandbox = GitSandbox(tmp_path)
        clone = sandbox.build(conflict=False)
        before = sandbox.git(clone, "rev-parse", "origin/develop")
        work = tmp_path / "work"
        (work / "c.txt").write_text("later\n", encoding="utf-8")
        sandbox.git(work, "add", ".")
        sandbox.git(work, "commit", "-q", "-m", "later")
        sandbox.git(work, "push", "-q", str(tmp_path / "origin.git"), "develop")
        result = PullRequestClone(clone).probe("develop", HEAD_REF)
        assert result.base_sha == sandbox.git(work, "rev-parse", "develop")
        assert sandbox.git(clone, "rev-parse", "origin/develop") == before
        assert sandbox.git(clone, "rev-parse", "refs/pr-watch/develop") == result.base_sha

    def test_a_missing_branch_is_an_error_in_the_result(self, tmp_path: Path) -> None:
        clone = GitSandbox(tmp_path).build(conflict=False)
        result = PullRequestClone(clone).probe("develop", "feature/GH-99-gone")
        assert result.error is not None
        assert result.error.startswith("git fetch exited")
        assert result.conflict_files == []

    @pytest.mark.parametrize(
        "url",
        [
            "https://github.com/gpbcom/simple-erp.git",
            "git@github.com:gpbcom/simple-erp.git",
            "https://github.com/gpbcom/simple-erp",
        ],
    )
    def test_the_origin_names_the_github_repository(self, tmp_path: Path, url: str) -> None:
        sandbox = GitSandbox(tmp_path)
        clone = sandbox.build(conflict=False)
        sandbox.git(clone, "remote", "set-url", "origin", url)
        assert PullRequestClone(clone).origin_slug() == "gpbcom/simple-erp"

    def test_an_origin_off_github_is_refused(self, tmp_path: Path) -> None:
        clone = GitSandbox(tmp_path).build(conflict=False)
        with pytest.raises(SECloneNotOnGithubError):
            PullRequestClone(clone).origin_slug()

    def test_the_main_working_tree_is_found_from_a_worktree(self, tmp_path: Path) -> None:
        sandbox = GitSandbox(tmp_path)
        clone = sandbox.build(conflict=False)
        sandbox.git(clone, "worktree", "add", "-q", str(tmp_path / "tree"), f"origin/{HEAD_REF}")
        assert PullRequestClone(tmp_path / "tree").main_root() == clone.resolve()
