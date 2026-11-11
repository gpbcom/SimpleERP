from __future__ import annotations

import logging

import pytest

from tests.builders.ticket_builder import TicketBuilder
from ticket_docs.models.checks.folder_rules import FolderRules
from ticket_docs.service.checks.markdown_tables import MarkdownTables
from ticket_docs.service.checks.progress.progress_table_check import ProgressTableCheck
from ticket_docs.service.checks.ticket_folder import TicketFolder


class TestProgressTableCheck:
    RUNNING = "| 1 — Customer storage (TDD) | 🔄 In progress | 2026-11-10 09:30 | — | 0h10 so far |"

    def check(self, rules: FolderRules, tables: MarkdownTables, logger: logging.Logger) -> ProgressTableCheck:
        return ProgressTableCheck(rules, tables, logger)

    def test_a_complete_table_has_no_problem(
        self, folder: TicketFolder, rules: FolderRules, tables: MarkdownTables, logger: logging.Logger
    ) -> None:
        assert self.check(rules, tables, logger).problems(folder) == []

    @pytest.mark.parametrize(
        ("row", "problem"),
        [
            (
                "| 1 — Customer storage (TDD) | In progress | 2026-11-10 09:30 | — | 0h10 so far |",
                "GH-7/PROGRESS.md: Status row '1 — Customer storage (TDD)' has no status icon",
            ),
            (
                "| 1 — Customer storage (TDD) | 🔄 In progress | — | — | 0h10 so far |",
                "GH-7/PROGRESS.md: Status row '1 — Customer storage (TDD)' has no valid Started time ('—')",
            ),
            (
                "| 1 — Customer storage (TDD) | 🔄 In progress | 2026-11-10 09:30 | — | 0h10 |",
                "GH-7/PROGRESS.md: Status row '1 — Customer storage (TDD)' has no valid Elapsed time ('0h10')",
            ),
            (
                "| 1 — Customer storage (TDD) | ✅ Done | 2026-11-10 09:30 | — | 1h00 |",
                "GH-7/PROGRESS.md: Status row '1 — Customer storage (TDD)' has no valid Finished time ('—')",
            ),
            (
                "| 1 — Customer storage (TDD) | ⏸️ Paused | — | — | — |",
                "GH-7/PROGRESS.md: Status row '1 — Customer storage (TDD)' has no valid Started time ('—')",
            ),
            (
                "| 1 — Customer storage (TDD) | 🔄 In progress | 2026-11-10 09:30 |",
                "GH-7/PROGRESS.md: Status row '1 — Customer storage (TDD)' misses time cells",
            ),
        ],
    )
    def test_each_status_row_has_its_icon_and_times(
        self,
        folder: TicketFolder,
        ticket: TicketBuilder,
        rules: FolderRules,
        tables: MarkdownTables,
        logger: logging.Logger,
        row: str,
        problem: str,
    ) -> None:
        ticket.edit("PROGRESS.md", self.RUNNING, row)
        assert self.check(rules, tables, logger).problems(folder) == [problem]

    def test_reconstructed_and_unknown_times_are_accepted(
        self,
        folder: TicketFolder,
        ticket: TicketBuilder,
        rules: FolderRules,
        tables: MarkdownTables,
        logger: logging.Logger,
    ) -> None:
        ticket.edit(
            "PROGRESS.md",
            self.RUNNING,
            "| 1 — Customer storage (TDD) | ✅ Done | 2026-11-10 09:30 (reconstructed) | unknown | 0h40 |",
        )
        assert self.check(rules, tables, logger).problems(folder) == []

    def test_the_time_columns_and_the_total_line_are_required(
        self,
        folder: TicketFolder,
        ticket: TicketBuilder,
        rules: FolderRules,
        tables: MarkdownTables,
        logger: logging.Logger,
    ) -> None:
        ticket.edit("PROGRESS.md", "| Step (PLAN.md) | Status | Started | Finished | Elapsed |", "| Step | Status |")
        ticket.edit("PROGRESS.md", "**Total time:**", "Total:")
        assert self.check(rules, tables, logger).problems(folder) == [
            "GH-7/PROGRESS.md: Status table lacks the Started / Finished / Elapsed columns",
            "GH-7/PROGRESS.md: '**Total time:**' line missing under the Status table",
        ]
