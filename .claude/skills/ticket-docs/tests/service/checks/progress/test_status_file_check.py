from __future__ import annotations

import logging

from tests.builders.ticket_builder import TicketBuilder
from ticket_docs.models.checks.folder_rules import FolderRules
from ticket_docs.service.checks.markdown_tables import MarkdownTables
from ticket_docs.service.checks.progress.status_file_check import StatusFileCheck
from ticket_docs.service.checks.ticket_folder import TicketFolder


class TestStatusFileCheck:
    SECTIONS = "".join(
        f"\n### {name}\n\ntext\n"
        for name in ("In short", "Conflict", "Resolution", "Verification", "State left behind", "How to resume")
    )

    def check(self, rules: FolderRules, tables: MarkdownTables, logger: logging.Logger) -> StatusFileCheck:
        return StatusFileCheck(rules, tables, logger)

    def test_without_status_file_or_conflict_there_is_nothing_to_say(
        self, folder: TicketFolder, rules: FolderRules, tables: MarkdownTables, logger: logging.Logger
    ) -> None:
        assert self.check(rules, tables, logger).problems(folder) == []

    def test_every_entry_starts_with_an_icon(
        self,
        folder: TicketFolder,
        ticket: TicketBuilder,
        rules: FolderRules,
        tables: MarkdownTables,
        logger: logging.Logger,
    ) -> None:
        ticket.write("STATUS.md", "# GH-7\n\n**Legend:** x\n\n## 2026-11-10: paused\n\n### How to resume\n")
        assert self.check(rules, tables, logger).problems(folder) == [
            "GH-7/STATUS.md: entry '2026-11-10: paused' does not start with a status icon"
        ]

    def test_a_rebase_conflict_mentioned_in_progress_needs_its_entry(
        self,
        folder: TicketFolder,
        ticket: TicketBuilder,
        rules: FolderRules,
        tables: MarkdownTables,
        logger: logging.Logger,
    ) -> None:
        ticket.edit("PROGRESS.md", "## Log\n", "## Log\n\nThe dev run hit a rebase conflict on develop.\n")
        assert self.check(rules, tables, logger).problems(folder) == [
            "GH-7/STATUS.md: PROGRESS.md mentions a rebase conflict, STATUS.md has no rebase-conflict entry"
        ]

    def test_a_rebase_conflict_entry_has_every_part(
        self,
        folder: TicketFolder,
        ticket: TicketBuilder,
        rules: FolderRules,
        tables: MarkdownTables,
        logger: logging.Logger,
    ) -> None:
        ticket.edit("PROGRESS.md", "## Log\n", "## Log\n\nThe dev run hit a rebase conflict on develop.\n")
        ticket.write(
            "STATUS.md",
            "# GH-7\n\n## ❌ 2026-11-10: rebase conflict on develop in `a.py` (local)\n"
            + self.SECTIONS
            + "\n## ❌ 2026-11-11: rebase conflict on develop in `b.py` (local)\n\n### In short\n\nx\n",
        )
        problems = self.check(rules, tables, logger).problems(folder)
        assert problems == [
            f"GH-7/STATUS.md: entry '❌ 2026-11-11: rebase conflict on develop in `b.py` (local)' misses '### {name}'"
            for name in ("Conflict", "Resolution", "Verification", "State left behind", "How to resume")
        ]
