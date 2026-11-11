from __future__ import annotations

import logging

import pytest

from tests.builders.evidence_builder import EvidenceBuilder
from tests.builders.ticket_builder import TicketBuilder
from ticket_docs.models.checks.folder_rules import FolderRules
from ticket_docs.service.checks.evidence.claims_check import ClaimsCheck
from ticket_docs.service.checks.markdown_tables import MarkdownTables
from ticket_docs.service.checks.ticket_folder import TicketFolder


class TestClaimsCheck:
    LINK = "[local-2026-11-10-unit-storage](tests-evidences/local-2026-11-10-unit-storage/README.md)"
    LOCAL = "| 💻 Local | ⬜ To do | — | — | — | — |"
    SUB_STEPS = "- **Sub-steps:** ✅ tests commit · ⬜ 🔴 red run · ⬜ code · ⬜ 🟢 green run · ⬜ checks"
    RUNNING = "| 1 — Customer storage (TDD) | 🔄 In progress | 2026-11-10 09:30 | — | 0h10 so far |"

    def check(self, rules: FolderRules, tables: MarkdownTables, logger: logging.Logger) -> ClaimsCheck:
        return ClaimsCheck(rules, tables, logger)

    def test_the_legend_template_rows_and_non_test_steps_are_not_claims(
        self, folder: TicketFolder, rules: FolderRules, tables: MarkdownTables, logger: logging.Logger
    ) -> None:
        assert self.check(rules, tables, logger).problems(folder) == []

    @pytest.mark.parametrize(
        ("file", "old", "new"),
        [
            ("PROGRESS.md", LOCAL, "| 💻 Local | ✅ Done | — | `abc` | ✅ PASS 3/3 | — |"),
            ("PROGRESS.md", SUB_STEPS, "- **Sub-steps:** ✅ tests commit · ✅ 🟢 green run · ⬜ checks"),
            ("PROGRESS.md", RUNNING, "| 1 — Customer storage (TDD) | ✅ Done | 2026-11-10 09:30 | — | 0h30 |"),
            ("PROGRESS.md", "## Log\n", "## Log\n\nAll tests are green ✅ now.\n"),
            ("EXPLAIN.md", "| Local | — | — | — | Not verified yet | — |", "| Local | — | — | `a` | PASS 3/3 | — |"),
            ("EXPLAIN.md", "Not verified yet.\n", "| AC | Status |\n|---|---|\n| AC1 | ✅ |\n"),
        ],
    )  # fmt: skip
    def test_a_pass_without_its_evidence_link_is_refused(
        self,
        folder: TicketFolder,
        ticket: TicketBuilder,
        rules: FolderRules,
        tables: MarkdownTables,
        logger: logging.Logger,
        file: str,
        old: str,
        new: str,
    ) -> None:
        ticket.edit(file, old, new)
        problems = self.check(rules, tables, logger).problems(folder)
        assert len(problems) == 1
        assert problems[0].startswith(f"GH-7/{file}:")
        assert problems[0].endswith("claims a pass without a link to its tests-evidences folder (TEST-8)")

    def test_a_pass_with_a_link_to_an_existing_folder_is_proven(
        self,
        folder: TicketFolder,
        ticket: TicketBuilder,
        rules: FolderRules,
        tables: MarkdownTables,
        logger: logging.Logger,
    ) -> None:
        EvidenceBuilder(ticket.tickets, "GH-7").folder("local-2026-11-10-unit-storage")
        ticket.edit("PROGRESS.md", self.LOCAL, f"| 💻 Local | ✅ Done | — | `abc` | ✅ PASS 3/3 | {self.LINK} |")
        ticket.edit("PROGRESS.md", self.SUB_STEPS, f"- **Sub-steps:** ✅ 🟢 green run ({self.LINK})")
        assert self.check(rules, tables, logger).problems(folder) == []

    def test_a_link_to_a_missing_folder_proves_nothing(
        self,
        folder: TicketFolder,
        ticket: TicketBuilder,
        rules: FolderRules,
        tables: MarkdownTables,
        logger: logging.Logger,
    ) -> None:
        ticket.edit("PROGRESS.md", self.LOCAL, f"| 💻 Local | ✅ Done | — | `abc` | ✅ PASS 3/3 | {self.LINK} |")
        problems = self.check(rules, tables, logger).problems(folder)
        assert len(problems) == 1
        assert "GH-7/PROGRESS.md:" in problems[0]

    def test_claims_in_code_blocks_and_comments_are_ignored(
        self,
        folder: TicketFolder,
        ticket: TicketBuilder,
        rules: FolderRules,
        tables: MarkdownTables,
        logger: logging.Logger,
    ) -> None:
        ticket.edit(
            "PROGRESS.md",
            "## Log\n",
            "## Log\n\n```text\n✅ PASS 3/3\n```\n<!-- Example:\n- **Sub-steps:** ✅ 🟢 green run\n-->\n",
        )
        assert self.check(rules, tables, logger).problems(folder) == []
