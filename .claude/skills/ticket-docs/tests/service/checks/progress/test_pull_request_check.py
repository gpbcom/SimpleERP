from __future__ import annotations

import logging

from tests.builders.ticket_builder import TicketBuilder
from ticket_docs.models.github.github_catalog import GithubCatalog
from ticket_docs.service.checks.markdown_tables import MarkdownTables
from ticket_docs.service.checks.progress.pull_request_check import PullRequestCheck
from ticket_docs.service.checks.ticket_folder import TicketFolder


class TestPullRequestCheck:
    ROW = "| Pull request (GIT-5) | ⬜ To do | — |\n"

    def description(self, lines: int, closes: str = "Closes #7") -> str:
        body = "\n".join([closes, *[f"line {number}" for number in range(lines - 1)]])
        return f"\n### Description — 2026-11-10 ({lines} / 10 lines)\n\n```text\n{body}\n```\n"

    def check(self, catalog: GithubCatalog, tables: MarkdownTables, logger: logging.Logger) -> PullRequestCheck:
        return PullRequestCheck(catalog, tables, logger)

    def test_a_short_description_that_closes_the_issue_is_fine(
        self,
        folder: TicketFolder,
        ticket: TicketBuilder,
        catalog: GithubCatalog,
        tables: MarkdownTables,
        logger: logging.Logger,
    ) -> None:
        ticket.edit("PROGRESS.md", self.ROW, self.ROW + self.description(10))
        assert self.check(catalog, tables, logger).problems(folder) == []

    def test_a_long_description_or_one_without_closes_is_refused(
        self,
        folder: TicketFolder,
        ticket: TicketBuilder,
        catalog: GithubCatalog,
        tables: MarkdownTables,
        logger: logging.Logger,
    ) -> None:
        ticket.edit("PROGRESS.md", self.ROW, self.ROW + self.description(11) + self.description(3, "Fixes #7"))
        assert self.check(catalog, tables, logger).problems(folder) == [
            "GH-7/PROGRESS.md: pull request description #1 has 11 lines, 10 at most (GIT-5)",
            "GH-7/PROGRESS.md: pull request description #2 does not contain 'Closes #7' (GIT-5)",
        ]

    def test_the_template_description_is_not_checked(
        self,
        folder: TicketFolder,
        ticket: TicketBuilder,
        catalog: GithubCatalog,
        tables: MarkdownTables,
        logger: logging.Logger,
    ) -> None:
        slot = "\n```text\n<the pull request description, 10 lines at most, with Closes #<n>>\n```\n"
        ticket.edit("PROGRESS.md", self.ROW, self.ROW + slot)
        assert self.check(catalog, tables, logger).problems(folder) == []

    def test_an_open_pull_request_needs_the_review_section(
        self,
        folder: TicketFolder,
        ticket: TicketBuilder,
        catalog: GithubCatalog,
        tables: MarkdownTables,
        logger: logging.Logger,
    ) -> None:
        ticket.edit(
            "PROGRESS.md",
            self.ROW,
            "| Pull request (GIT-5) | ✅ Done | https://github.com/gpbcom/simple-erp/pull/12, 2026-11-10 |\n",
        )
        assert self.check(catalog, tables, logger).problems(folder) == []
        ticket.edit("PROGRESS.md", "## PR review\n", "## Reviews\n")
        assert self.check(catalog, tables, logger).problems(folder) == [
            "GH-7/PROGRESS.md: the pull request is open but there is no '## PR review' section "
            "(pr-review-followup skill)"
        ]
