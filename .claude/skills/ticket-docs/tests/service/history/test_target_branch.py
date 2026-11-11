from __future__ import annotations

import logging
from pathlib import Path

import pytest

from harness_core.git.git_repository import GitRepository
from tests.builders.git_sandbox import GitSandbox
from ticket_docs.models.github.github_catalog import GithubCatalog
from ticket_docs.service.history.target_branch import TargetBranch


class TestTargetBranch:
    @pytest.mark.parametrize(
        ("branch", "target"),
        [
            ("feature/GH-1-thing", "origin/develop"),
            ("bugfix/GH-1-thing", "origin/develop"),
            ("hotfix/1.0.1-GH-5-crash", "origin/master"),
            ("release/1.0.0", "origin/master"),
            ("worktree-agent-x", "origin/develop"),
            ("feature/not-a-ticket", "origin/develop"),
        ],
    )
    def test_the_target_follows_gitflow(self, tmp_path: Path, logger: logging.Logger, branch: str, target: str) -> None:
        sandbox = GitSandbox(tmp_path / "repo", branch=branch)
        catalog = GithubCatalog.load(GithubCatalog.SKILL_DIR / "conf" / "github.yaml")
        assert TargetBranch(catalog, logger).of(GitRepository(sandbox.root, logger)) == target
