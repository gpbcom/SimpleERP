from __future__ import annotations

import logging
from pathlib import Path

from harness_core.git.git_repository import GitRepository
from tests.builders.git_sandbox import GitSandbox
from ticket_docs.service.paths.tickets_root import TicketsRoot


class TestTicketsRoot:
    def test_the_tickets_live_in_the_repository(self, tmp_path: Path, logger: logging.Logger) -> None:
        sandbox = GitSandbox(tmp_path / "repo")
        (sandbox.root / "docs" / "tickets").mkdir(parents=True)
        assert TicketsRoot(logger).of(GitRepository(sandbox.root)) == sandbox.root.resolve() / "docs" / "tickets"

    def test_a_linked_worktree_without_tickets_uses_the_main_checkout(
        self, tmp_path: Path, logger: logging.Logger
    ) -> None:
        sandbox = GitSandbox(tmp_path / "repo")
        (sandbox.root / "docs" / "tickets").mkdir(parents=True)
        linked = tmp_path / "linked"
        sandbox.git("worktree", "add", "-q", "-b", "other", str(linked))
        assert TicketsRoot(logger).of(GitRepository(linked)) == sandbox.root.resolve() / "docs" / "tickets"

    def test_a_new_repository_gets_its_own_folder(self, tmp_path: Path, logger: logging.Logger) -> None:
        sandbox = GitSandbox(tmp_path / "repo")
        assert TicketsRoot(logger).of(GitRepository(sandbox.root)) == sandbox.root.resolve() / "docs" / "tickets"
