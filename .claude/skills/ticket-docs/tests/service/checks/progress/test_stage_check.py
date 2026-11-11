from __future__ import annotations

import logging

from tests.builders.ticket_builder import TicketBuilder
from ticket_docs.models.checks.folder_rules import FolderRules
from ticket_docs.service.checks.markdown_tables import MarkdownTables
from ticket_docs.service.checks.progress.stage_check import StageCheck
from ticket_docs.service.checks.ticket_folder import TicketFolder


class TestStageCheck:
    def test_a_complete_table_has_no_problem(
        self, folder: TicketFolder, rules: FolderRules, tables: MarkdownTables, logger: logging.Logger
    ) -> None:
        assert StageCheck(rules, tables, logger).problems(folder) == []

    def test_each_place_has_its_row_with_a_status_icon(
        self,
        folder: TicketFolder,
        ticket: TicketBuilder,
        rules: FolderRules,
        tables: MarkdownTables,
        logger: logging.Logger,
    ) -> None:
        ticket.edit("PROGRESS.md", "| 🟪 QA | ⬜ To do | — | — | — | — |\n", "")
        ticket.edit("PROGRESS.md", "| 🟦 Dev | ⬜ To do |", "| 🟦 Dev | To do |")
        assert StageCheck(rules, tables, logger).problems(folder) == [
            "GH-7/PROGRESS.md: Stage validation has no 🟪 row",
            "GH-7/PROGRESS.md: Stage validation row '🟦 Dev' has no status icon",
        ]
