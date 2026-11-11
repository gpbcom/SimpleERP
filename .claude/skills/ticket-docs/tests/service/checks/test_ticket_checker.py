from __future__ import annotations

import logging
from pathlib import Path

from harness_core.git.git_repository import GitRepository
from tests.builders.git_sandbox import GitSandbox
from tests.builders.ticket_builder import TicketBuilder
from ticket_docs.models.checks.folder_rules import FolderRules
from ticket_docs.models.github.github_catalog import GithubCatalog
from ticket_docs.service.checks.doc1.doc1_check import Doc1Check
from ticket_docs.service.checks.evidence.audit_check import AuditCheck
from ticket_docs.service.checks.evidence.claims_check import ClaimsCheck
from ticket_docs.service.checks.evidence.readme_fields_check import ReadmeFieldsCheck
from ticket_docs.service.checks.evidence.reports_check import ReportsCheck
from ticket_docs.service.checks.evidence.tdd_check import TddCheck
from ticket_docs.service.checks.folder.content_check import ContentCheck
from ticket_docs.service.checks.folder.evidence_index_check import EvidenceIndexCheck
from ticket_docs.service.checks.folder.required_files_check import RequiredFilesCheck
from ticket_docs.service.checks.markdown_tables import MarkdownTables
from ticket_docs.service.checks.progress.handover_check import HandoverCheck
from ticket_docs.service.checks.progress.progress_table_check import ProgressTableCheck
from ticket_docs.service.checks.progress.pull_request_check import PullRequestCheck
from ticket_docs.service.checks.progress.stage_check import StageCheck
from ticket_docs.service.checks.progress.status_file_check import StatusFileCheck
from ticket_docs.service.checks.ticket_checker import TicketChecker
from ticket_docs.service.checks.ticket_folder import TicketFolder
from ticket_docs.service.index.report_index import ReportIndex
from ticket_docs.service.paths.code_paths import CodePaths
from ticket_docs.storage.evidence.evidence_repository import EvidenceRepository
from ticket_docs.storage.github.gh_client import GhClient
from ticket_docs.storage.processes.command_runner import CommandRunner
from ticket_docs.storage.tickets.ticket_repository import TicketRepository


class TestTicketChecker:
    def checker(
        self, key: str, tickets: Path, rules: FolderRules, catalog: GithubCatalog, logger: logging.Logger
    ) -> TicketChecker:
        tables = MarkdownTables(logger)
        evidence = EvidenceRepository(tickets, logger)
        repository = TicketRepository(tickets, logger)
        index = ReportIndex(evidence, repository, logger)
        folder = TicketFolder(key, repository, evidence, tables, logger)
        rules_file = tickets.parents[1] / ".claude" / "rules" / "ticket-documentation.md"
        checks = [
            RequiredFilesCheck(rules, logger),
            ContentCheck(rules, tables, logger),
            EvidenceIndexCheck(logger),
            ProgressTableCheck(rules, tables, logger),
            StageCheck(rules, tables, logger),
            PullRequestCheck(catalog, tables, logger),
            HandoverCheck(tables, logger),
            StatusFileCheck(rules, tables, logger),
            ReadmeFieldsCheck(logger),
            ClaimsCheck(rules, tables, logger),
            ReportsCheck(
                index, repository, evidence, GhClient(catalog.full_name, logger=logger), catalog, True, logger
            ),
            TddCheck(GitRepository(tickets.parents[1], logger), CodePaths(rules, logger), tables, logger),
            AuditCheck(tables, logger),
            Doc1Check(rules_file, CommandRunner(logger), logger),
        ]
        checker = TicketChecker(folder, checks, logger)
        checker.execute()
        return checker

    def test_a_folder_made_from_the_templates_passes_every_check(
        self, tickets: Path, rules: FolderRules, catalog: GithubCatalog, logger: logging.Logger
    ) -> None:
        GitSandbox(tickets.parents[1])
        TicketBuilder(tickets).from_templates()
        TicketRepository(tickets, logger).write_index(
            ReportIndex(EvidenceRepository(tickets, logger), TicketRepository(tickets, logger), logger).text()
        )
        assert self.checker("GH-7", tickets, rules, catalog, logger).problems == []

    def test_every_check_reports_into_one_list(
        self, tickets: Path, rules: FolderRules, catalog: GithubCatalog, logger: logging.Logger
    ) -> None:
        GitSandbox(tickets.parents[1])
        builder = TicketBuilder(tickets)
        builder.from_templates()
        (builder.folder / "PLAN.md").unlink()
        builder.edit("EXPLAIN.md", "## 7. References", "## 7. Links")
        problems = self.checker("GH-7", tickets, rules, catalog, logger).problems
        assert "GH-7/PLAN.md: missing" in problems
        assert "docs/tickets/README.md: out of date, run ticket-docs report-index (TEST-9)" in problems
        assert any(problem.startswith("DOC-1: ") and "references" in problem for problem in problems)

    def test_a_missing_folder_is_the_only_problem(
        self, tickets: Path, rules: FolderRules, catalog: GithubCatalog, logger: logging.Logger
    ) -> None:
        assert self.checker("GH-404", tickets, rules, catalog, logger).problems == [
            f"{tickets / 'GH-404'}: no such folder"
        ]
