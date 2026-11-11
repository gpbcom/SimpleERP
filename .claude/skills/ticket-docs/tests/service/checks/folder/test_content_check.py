from __future__ import annotations

import logging

import pytest

from tests.builders.ticket_builder import TicketBuilder
from ticket_docs.models.checks.folder_rules import FolderRules
from ticket_docs.service.checks.folder.content_check import ContentCheck
from ticket_docs.service.checks.markdown_tables import MarkdownTables
from ticket_docs.service.checks.ticket_folder import TicketFolder


class TestContentCheck:
    HANDED_OVER = "| 2 — Final acceptance run and hand-over | ✅ Done | 2026-11-10 10:00 | 2026-11-10 11:00 | 1h00 |"
    HANDOVER_ROW = "| 2 — Final acceptance run and hand-over | ⬜ To do | — | — | — |"

    def check(self, rules: FolderRules, tables: MarkdownTables, logger: logging.Logger) -> ContentCheck:
        return ContentCheck(rules, tables, logger)

    def test_a_complete_folder_has_no_problem(
        self, folder: TicketFolder, rules: FolderRules, tables: MarkdownTables, logger: logging.Logger
    ) -> None:
        assert self.check(rules, tables, logger).problems(folder) == []

    def test_placeholders_are_never_left(
        self,
        folder: TicketFolder,
        ticket: TicketBuilder,
        rules: FolderRules,
        tables: MarkdownTables,
        logger: logging.Logger,
    ) -> None:
        ticket.edit("TICKET.md", "# GH-7 — Customers", "# <KEY> — <TITLE>")
        assert self.check(rules, tables, logger).problems(folder) == [
            "GH-7/TICKET.md: template placeholder <KEY> left",
            "GH-7/TICKET.md: template placeholder <TITLE> left",
        ]

    @pytest.mark.parametrize(
        "secret",
        [
            "token eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9xx",
            "password: hunter22",
            "https://bucket/x?X-Amz-Signature=abc",
            "ghp_abcdefghijklmnopqrstuvwxyz0123",
        ],
    )
    def test_secrets_are_refused(
        self,
        folder: TicketFolder,
        ticket: TicketBuilder,
        rules: FolderRules,
        tables: MarkdownTables,
        logger: logging.Logger,
        secret: str,
    ) -> None:
        ticket.write("TESTS-NOTICE.md", f"# Notice\n\n{secret}\n")
        assert self.check(rules, tables, logger).problems(folder) == ["GH-7/TESTS-NOTICE.md: looks like a secret"]

    def test_broken_relative_links_are_named_outside_code_and_comments(
        self,
        folder: TicketFolder,
        ticket: TicketBuilder,
        rules: FolderRules,
        tables: MarkdownTables,
        logger: logging.Logger,
    ) -> None:
        ticket.write(
            "TESTS-NOTICE.md",
            "[ok](PLAN.md#x) [web](https://example.com) [anchor](#top) [gone](GONE.md)\n"
            "```text\n[fenced](NOPE.md)\n```\n<!-- [commented](NOPE.md) -->\n"
            "[note](RELEASE-NOTE.md)\n",
        )
        assert self.check(rules, tables, logger).problems(folder) == ["GH-7/TESTS-NOTICE.md: broken link GONE.md"]

    def test_once_handed_over_the_release_note_link_must_work_and_slots_must_be_filled(
        self,
        folder: TicketFolder,
        ticket: TicketBuilder,
        rules: FolderRules,
        tables: MarkdownTables,
        logger: logging.Logger,
    ) -> None:
        ticket.edit("PROGRESS.md", self.HANDOVER_ROW, self.HANDED_OVER)
        ticket.write("README.md", "# GH-7\n\n[note](RELEASE-NOTE.md) <what changed> `<code is fine>` <br>\n")
        ticket.write("RELEASE-NOTE.md", "# GH-7 — Release note\n\n<!-- release-note --> Ready.\n")
        problems = self.check(rules, tables, logger).problems(folder)
        assert problems == ["GH-7/README.md: template slots left: <what changed>"]
        (ticket.folder / "RELEASE-NOTE.md").unlink()
        assert "GH-7/README.md: broken link RELEASE-NOTE.md" in self.check(rules, tables, logger).problems(folder)
