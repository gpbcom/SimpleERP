from __future__ import annotations

import logging

from tests.builders.ticket_builder import TicketBuilder
from ticket_docs.models.checks.folder_rules import FolderRules
from ticket_docs.service.checks.folder.required_files_check import RequiredFilesCheck
from ticket_docs.service.checks.ticket_folder import TicketFolder


class TestRequiredFilesCheck:
    HANDED_OVER = "| 2 — Final acceptance run and hand-over | ✅ Done | 2026-11-10 10:00 | 2026-11-10 11:00 | 1h00 |"
    HANDOVER_ROW = "| 2 — Final acceptance run and hand-over | ⬜ To do | — | — | — |"

    def test_a_complete_folder_has_no_problem(
        self, folder: TicketFolder, rules: FolderRules, logger: logging.Logger
    ) -> None:
        assert RequiredFilesCheck(rules, logger).problems(folder) == []

    def test_missing_files_and_headings_are_named(
        self, folder: TicketFolder, ticket: TicketBuilder, rules: FolderRules, logger: logging.Logger
    ) -> None:
        (ticket.folder / "PLAN.md").unlink()
        (ticket.folder / "attachments").rmdir()
        ticket.edit("IMPLEMENTATION.md", "## 1. Implementation choices", "## 1. Choices")
        ticket.write("STATUS.md", "# GH-7 — Status\n\n## ⏸️ 2026-11-10: paused\n")
        assert RequiredFilesCheck(rules, logger).problems(folder) == [
            "GH-7/PLAN.md: missing",
            "GH-7/attachments: missing",
            "GH-7/IMPLEMENTATION.md: heading '## 1. Implementation choices' missing",
            "GH-7/STATUS.md: heading '**Legend:**' missing",
            "GH-7/STATUS.md: heading '### How to resume' missing",
        ]

    def test_the_release_note_is_required_once_handed_over(
        self, folder: TicketFolder, ticket: TicketBuilder, rules: FolderRules, logger: logging.Logger
    ) -> None:
        ticket.edit("PROGRESS.md", self.HANDOVER_ROW, self.HANDED_OVER)
        assert RequiredFilesCheck(rules, logger).problems(folder) == ["GH-7/RELEASE-NOTE.md: missing"]
        ticket.write("RELEASE-NOTE.md", "# GH-7 — Release note\n")
        assert RequiredFilesCheck(rules, logger).problems(folder) == []
