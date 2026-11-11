from __future__ import annotations

import logging

from tests.builders.ticket_builder import TicketBuilder
from ticket_docs.service.checks.markdown_tables import MarkdownTables
from ticket_docs.service.checks.progress.handover_check import HandoverCheck
from ticket_docs.service.checks.ticket_folder import TicketFolder


class TestHandoverCheck:
    HANDED_OVER = "| 2 — Final acceptance run and hand-over | ✅ Done | 2026-11-10 10:00 | 2026-11-10 11:00 | 1h00 |"
    HANDOVER_ROW = "| 2 — Final acceptance run and hand-over | ⬜ To do | — | — | — |"

    def test_before_the_hand_over_nothing_is_required(
        self, folder: TicketFolder, tables: MarkdownTables, logger: logging.Logger
    ) -> None:
        assert HandoverCheck(tables, logger).problems(folder) == []

    def test_the_hand_over_needs_the_documentation_and_the_release_note(
        self, folder: TicketFolder, ticket: TicketBuilder, tables: MarkdownTables, logger: logging.Logger
    ) -> None:
        ticket.edit("PROGRESS.md", self.HANDOVER_ROW, self.HANDED_OVER)
        assert HandoverCheck(tables, logger).problems(folder) == [
            "GH-7/PROGRESS.md: handed over but Documentation row 'docs/technical/README.md' is not ✅ (DOC-2)",
            "GH-7/PROGRESS.md: handed over but Release note row 'RELEASE-NOTE.md' is not ✅ (DOC-3)",
            "GH-7/PROGRESS.md: handed over but Release note row 'Changelog fragment' is not ✅ (DOC-3)",
        ]

    def test_done_rows_and_waived_chapters_pass(
        self, folder: TicketFolder, ticket: TicketBuilder, tables: MarkdownTables, logger: logging.Logger
    ) -> None:
        ticket.edit("PROGRESS.md", self.HANDOVER_ROW, self.HANDED_OVER)
        ticket.edit(
            "PROGRESS.md",
            "| docs/technical/README.md | ⬜ To do | — |",
            "| docs/technical/README.md | 🚫 Waived | no doc impact: harness only |\n| README.md | ✅ Done | x |",
        )
        ticket.edit("PROGRESS.md", "| RELEASE-NOTE.md | ⬜ To do |", "| RELEASE-NOTE.md | ✅ Done |")
        ticket.edit("PROGRESS.md", "| Changelog fragment | ⬜ To do |", "| Changelog fragment | ✅ Done |")
        assert HandoverCheck(tables, logger).problems(folder) == []
