from __future__ import annotations

import subprocess
from pathlib import Path

from harness_core.testing.git_sandbox import GitSandbox


class TestGitSandbox:
    def test_a_sandbox_starts_on_its_branch_with_one_commit(self, tmp_path: Path) -> None:
        sandbox = GitSandbox(tmp_path / "repo")
        root = sandbox.create()
        assert root == (tmp_path / "repo").resolve()
        assert sandbox.git("branch", "--show-current") == "develop"
        assert sandbox.git("rev-list", "--count", "HEAD") == "1"

    def test_commit_writes_the_files_and_returns_the_commit(self, tmp_path: Path) -> None:
        sandbox = GitSandbox(tmp_path / "repo", branch="master")
        sandbox.create()
        commit = sandbox.commit("add docs", {"docs/a.md": "hello\n", "b.txt": "b\n"})
        assert (sandbox.root / "docs" / "a.md").read_text(encoding="utf-8") == "hello\n"
        assert sandbox.git("rev-parse", "HEAD") == commit
        assert sandbox.git("show", "--format=", "--name-only", commit).splitlines() == ["b.txt", "docs/a.md"]

    def test_commit_can_delete_a_file(self, tmp_path: Path) -> None:
        sandbox = GitSandbox(tmp_path / "repo")
        sandbox.create()
        sandbox.commit("add", {"a.txt": "a\n"})
        sandbox.commit("remove", {"a.txt": None})
        assert not (sandbox.root / "a.txt").exists()
        listed = subprocess.run(
            ["git", "-C", str(sandbox.root), "ls-files"], capture_output=True, text=True, check=True
        ).stdout
        assert "a.txt" not in listed

    def test_write_leaves_the_file_uncommitted(self, tmp_path: Path) -> None:
        sandbox = GitSandbox(tmp_path / "repo")
        sandbox.create()
        sandbox.write("notes/new.md", "draft\n")
        assert sandbox.git("status", "--porcelain", "-uall") == "?? notes/new.md"
