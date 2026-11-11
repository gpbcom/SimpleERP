from __future__ import annotations

import json
import logging
from pathlib import Path

import pytest

from tests.builders.evidence_builder import EvidenceBuilder
from tests.builders.fake_gh import FakeGh
from tests.builders.ticket_builder import TicketBuilder
from ticket_docs.models.github.github_catalog import GithubCatalog
from ticket_docs.service.checks.evidence.reports_check import ReportsCheck
from ticket_docs.service.checks.ticket_folder import TicketFolder
from ticket_docs.service.index.report_index import ReportIndex
from ticket_docs.storage.evidence.evidence_repository import EvidenceRepository
from ticket_docs.storage.github.gh_client import GhClient
from ticket_docs.storage.tickets.ticket_repository import TicketRepository


class TestReportsCheck:
    HANDED_OVER = "| 2 — Final acceptance run and hand-over | ✅ Done | 2026-11-10 10:00 | 2026-11-10 11:00 | 1h00 |"
    HANDOVER_ROW = "| 2 — Final acceptance run and hand-over | ⬜ To do | — | — | — |"

    def check(self, tickets: Path, catalog: GithubCatalog, logger: logging.Logger, offline: bool) -> ReportsCheck:
        evidence = EvidenceRepository(tickets, logger)
        repository = TicketRepository(tickets, logger)
        index = ReportIndex(evidence, repository, logger)
        return ReportsCheck(
            index, repository, evidence, GhClient(catalog.full_name, logger=logger), catalog, offline, logger
        )

    def index(self, tickets: Path, logger: logging.Logger) -> None:
        evidence = EvidenceRepository(tickets, logger)
        repository = TicketRepository(tickets, logger)
        ReportIndex(evidence, repository, logger).write()

    def test_complete_reports_and_a_current_index_have_no_problem(
        self,
        folder: TicketFolder,
        ticket: TicketBuilder,
        catalog: GithubCatalog,
        logger: logging.Logger,
    ) -> None:
        builder = EvidenceBuilder(ticket.tickets, "GH-7")
        builder.folder("local-2026-11-10-unit-a")
        builder.folder("local-2026-11-10-gui-a", {"Kind": "gui"}, files=("console.txt", "playwright-report/"))
        builder.folder("dev-2026-11-10-stage", {"Kind": "e2e", "Where": "dev"}, files=("actions.log", "artifacts/"))
        builder.folder("local-2026-11-10-lint", {"Kind": "check"}, files=("console.txt",))
        builder.folder("local-2026-11-10-bad-env", {"Result": "⚠️ INVALID: no disk"}, files=("console.txt",))
        self.index(ticket.tickets, logger)
        assert self.check(ticket.tickets, catalog, logger, offline=True).problems(folder) == []

    def test_missing_reports_big_files_and_a_stale_index_are_named(
        self,
        folder: TicketFolder,
        ticket: TicketBuilder,
        catalog: GithubCatalog,
        logger: logging.Logger,
    ) -> None:
        builder = EvidenceBuilder(ticket.tickets, "GH-7")
        builder.folder("local-2026-11-10-unit-a", files=("report.xml",))
        builder.folder("local-2026-11-10-gui-a", {"Kind": "gui"}, files=("console.txt",))
        builder.folder("qa-2026-11-10-stage", {"Kind": "e2e", "Where": "qa"}, files=("console.txt", "artifacts/"))
        builder.folder("ci-2026-11-10-checks", {"Kind": "check", "Where": "ci"}, files=("console.txt",))
        big = builder.folder("local-2026-11-10-unit-b")
        (big / "trace.zip").write_bytes(b"x" * (5 * 1024 * 1024 + 1))
        assert self.check(ticket.tickets, catalog, logger, offline=True).problems(folder) == [
            "GH-7/tests-evidences/ci-2026-11-10-checks: ci run without actions.log or artifacts/ (TEST-9)",
            "GH-7/tests-evidences/local-2026-11-10-gui-a: gui run without a Playwright report, "
            "a Bruno report or artifacts/ (TEST-9)",
            "GH-7/tests-evidences/local-2026-11-10-unit-a: unit run without console.txt (TEST-9)",
            "GH-7/tests-evidences/local-2026-11-10-unit-b/trace.zip: 5.0 MB, over the 5 MB limit (TEST-9)",
            "docs/tickets/README.md: out of date, run ticket-docs report-index (TEST-9)",
        ]

    @pytest.mark.parametrize("code", [2, 4, 5])
    def test_a_unit_run_that_pytest_stopped_before_its_tests_needs_only_its_console(
        self, folder: TicketFolder, ticket: TicketBuilder, catalog: GithubCatalog, logger: logging.Logger, code: int
    ) -> None:
        builder = EvidenceBuilder(ticket.tickets, "GH-7")
        result = f"❌ FAIL 0/0 (exit {code}; 0 failures, 0 errors) — expected red (TDD), as expected"
        builder.folder("local-2026-11-10-tdd-red-a", {"Result": result}, files=("console.txt",))
        builder.folder("local-2026-11-10-tdd-red-b", {"Result": result}, files=())
        builder.folder(
            "local-2026-11-10-unit-c", {"Result": "❌ FAIL 1/2 (exit 1; 1 failures, 0 errors)"}, files=("console.txt",)
        )
        problems = self.check(ticket.tickets, catalog, logger, offline=True).problems(folder)
        assert [line for line in problems if "unit run without" in line] == [
            "GH-7/tests-evidences/local-2026-11-10-tdd-red-b: unit run without console.txt (TEST-9)",
            "GH-7/tests-evidences/local-2026-11-10-unit-c: unit run without report.xml (TEST-9)",
        ]

    def test_once_handed_over_the_archive_must_be_newer_than_the_evidence(
        self,
        folder: TicketFolder,
        ticket: TicketBuilder,
        catalog: GithubCatalog,
        logger: logging.Logger,
        gh: FakeGh,
    ) -> None:
        ticket.edit("PROGRESS.md", self.HANDOVER_ROW, self.HANDED_OVER)
        EvidenceBuilder(ticket.tickets, "GH-7").folder("local-2026-11-10-unit-a", {"Date": "2026-11-10 10:17"})
        self.index(ticket.tickets, logger)
        old = {"assets": [{"name": "GH-7-a.zip", "url": "u", "createdAt": "2026-11-09T09:00:00Z"}]}
        gh.answer(["release", "view", "evidence-GH-7"], stdout=json.dumps(old))
        assert self.check(ticket.tickets, catalog, logger, offline=False).problems(folder) == [
            "evidence-GH-7: no asset newer than the evidence folder local-2026-11-10-unit-a, "
            "run ticket-docs archive GH-7 (TEST-9)"
        ]
        assert self.check(ticket.tickets, catalog, logger, offline=True).problems(folder) == []

    def test_a_missing_pre_release_is_named(
        self,
        folder: TicketFolder,
        ticket: TicketBuilder,
        catalog: GithubCatalog,
        logger: logging.Logger,
        gh: FakeGh,
    ) -> None:
        ticket.edit("PROGRESS.md", self.HANDOVER_ROW, self.HANDED_OVER)
        self.index(ticket.tickets, logger)
        gh.answer(["release", "view"], exit_code=1, stderr="release not found")
        assert self.check(ticket.tickets, catalog, logger, offline=False).problems(folder) == [
            "evidence-GH-7: no pre-release, run ticket-docs archive GH-7 (TEST-9)"
        ]

    def test_a_new_archive_satisfies_the_check(
        self,
        folder: TicketFolder,
        ticket: TicketBuilder,
        catalog: GithubCatalog,
        logger: logging.Logger,
        gh: FakeGh,
    ) -> None:
        ticket.edit("PROGRESS.md", self.HANDOVER_ROW, self.HANDED_OVER)
        EvidenceBuilder(ticket.tickets, "GH-7").folder("local-2026-11-10-unit-a", {"Date": "2026-11-10 10:17"})
        self.index(ticket.tickets, logger)
        new = {"assets": [{"name": "GH-7-b.zip", "url": "u", "createdAt": "2026-11-12T09:00:00Z"}]}
        gh.answer(["release", "view", "evidence-GH-7"], stdout=json.dumps(new))
        assert self.check(ticket.tickets, catalog, logger, offline=False).problems(folder) == []
