from __future__ import annotations

import logging
from pathlib import Path
from typing import Optional

import pytest

from harness_core.git.exceptions import SEGitError
from tests.builders.git_sandbox import GitSandbox
from ticket_docs.models.checks.folder_rules import FolderRules
from ticket_docs.models.evidence.run_request import RunRequest
from ticket_docs.models.github.github_catalog import GithubCatalog
from ticket_docs.service.checks.ticket_checker import TicketChecker
from ticket_docs.service.factories.default.default_service_factory import DefaultServiceFactory
from ticket_docs.service.github.board_mover import BoardMover
from ticket_docs.service.github.evidence_archiver import EvidenceArchiver
from ticket_docs.service.history.history_bundler import HistoryBundler
from ticket_docs.service.hooks.git_gate import GitGate
from ticket_docs.service.hooks.time_reminder import TimeReminder
from ticket_docs.service.index.report_index import ReportIndex
from ticket_docs.service.runs.run_recorder import RunRecorder


class TestDefaultServiceFactory:
    def factory(self, cwd: Path, logger: logging.Logger, root: Optional[Path] = None) -> DefaultServiceFactory:
        rules = FolderRules.load(FolderRules.SKILL_DIR / "conf" / "folder-rules.yaml")
        catalog = GithubCatalog.load(GithubCatalog.SKILL_DIR / "conf" / "github.yaml")
        return DefaultServiceFactory(cwd, root, rules, catalog, logger)

    def test_the_tickets_folder_comes_from_the_callers_repository_or_the_root_option(
        self, tmp_path: Path, logger: logging.Logger
    ) -> None:
        sandbox = GitSandbox(tmp_path / "repo")
        (sandbox.root / "sub").mkdir()
        assert self.factory(sandbox.root / "sub", logger).tickets_root() == sandbox.root.resolve() / "docs" / "tickets"
        assert self.factory(sandbox.root, logger, tmp_path / "elsewhere").tickets_root() == tmp_path / "elsewhere"

    def test_every_service_is_built(self, tmp_path: Path, logger: logging.Logger) -> None:
        sandbox = GitSandbox(tmp_path / "repo")
        factory = self.factory(sandbox.root, logger)
        request = RunRequest(ticket="GH-1", kind="unit", where="local", check="x", what="x", command=["true"])
        assert isinstance(factory.run_recorder(request), RunRecorder)
        assert isinstance(factory.ticket_checker("GH-1", True), TicketChecker)
        assert isinstance(factory.report_index(), ReportIndex)
        assert isinstance(factory.history_bundler(), HistoryBundler)
        archiver = factory.evidence_archiver(True)
        assert isinstance(archiver, EvidenceArchiver)
        assert archiver.gh.dry_run
        assert isinstance(factory.board_mover(), BoardMover)
        assert isinstance(factory.git_gate(), GitGate)
        assert isinstance(factory.time_reminder(), TimeReminder)

    def test_a_folder_outside_any_repository_has_no_tickets_folder(
        self, tmp_path: Path, logger: logging.Logger
    ) -> None:
        with pytest.raises(SEGitError):
            self.factory(tmp_path, logger).tickets_root()
        assert self.factory(tmp_path, logger, tmp_path).tickets_root() == tmp_path
