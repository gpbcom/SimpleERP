from __future__ import annotations

import logging
from pathlib import Path

import pytest

from harness_core.git.exceptions import SEGitCommandFailedError
from harness_core.git.git_repository import GitRepository
from tests.builders.git_sandbox import GitSandbox
from ticket_docs.models.github.github_catalog import GithubCatalog
from ticket_docs.service.history.history_bundler import HistoryBundler
from ticket_docs.storage.evidence.evidence_repository import EvidenceRepository


class TestHistoryBundler:
    def bundler(self, sandbox: GitSandbox, logger: logging.Logger) -> HistoryBundler:
        catalog = GithubCatalog.load(GithubCatalog.SKILL_DIR / "conf" / "github.yaml")
        evidence = EvidenceRepository(sandbox.root / "docs" / "tickets", logger)
        return HistoryBundler(GitRepository(sandbox.root, logger), evidence, catalog, logger)

    def test_a_feature_branch_is_saved_from_develop(self, tmp_path: Path, logger: logging.Logger) -> None:
        sandbox = GitSandbox(tmp_path / "repo")
        base = sandbox.head()
        tests = sandbox.commit("tests/test_a.py", message="[GH-1] test: a")
        code = sandbox.commit("src/a.py", message="[GH-1] feat: a")
        bundle = self.bundler(sandbox, logger).bundle("GH-1")
        assert bundle.parent == sandbox.root / "docs" / "tickets" / "GH-1" / "tests-evidences" / "history"
        assert bundle.name.startswith("pre-squash-")
        assert bundle.suffix == ".bundle"
        assert bundle.with_suffix(".txt").read_text(encoding="utf-8") == (
            f"{tests} [GH-1] test: a\n{code} [GH-1] feat: a\n"
        )
        assert bundle.with_suffix(".base").read_text(encoding="utf-8") == f"{base}\n"
        sandbox.git("bundle", "verify", "-q", str(bundle))

    def test_a_hotfix_branch_is_saved_from_master(self, tmp_path: Path, logger: logging.Logger) -> None:
        sandbox = GitSandbox(tmp_path / "repo", branch="develop")
        sandbox.git("switch", "-q", "-c", "master")
        released = sandbox.commit("CHANGELOG.md", message="release 1.0.0")
        sandbox.git("update-ref", "refs/remotes/origin/master", "HEAD")
        sandbox.git("switch", "-q", "-c", "hotfix/1.0.1-GH-5-crash")
        fix = sandbox.commit("src/fix.py", message="[GH-5] fix: crash")
        bundle = self.bundler(sandbox, logger).bundle("GH-5")
        assert bundle.with_suffix(".txt").read_text(encoding="utf-8") == f"{fix} [GH-5] fix: crash\n"
        assert bundle.with_suffix(".base").read_text(encoding="utf-8") == f"{released}\n"

    def test_a_second_bundle_in_the_same_minute_does_not_replace_the_first(
        self, tmp_path: Path, logger: logging.Logger
    ) -> None:
        sandbox = GitSandbox(tmp_path / "repo")
        sandbox.commit("src/a.py")
        bundler = self.bundler(sandbox, logger)
        first = bundler.bundle("GH-1")
        second = bundler.bundle("GH-1")
        assert first != second
        assert first.is_file()
        assert second.is_file()

    def test_a_branch_without_commits_cannot_be_saved(self, tmp_path: Path, logger: logging.Logger) -> None:
        sandbox = GitSandbox(tmp_path / "repo")
        with pytest.raises(SEGitCommandFailedError):
            self.bundler(sandbox, logger).bundle("GH-1")
