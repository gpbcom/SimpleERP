from __future__ import annotations

import logging
import shutil
from pathlib import Path

from tests.builders.ticket_builder import TicketBuilder
from ticket_docs.service.checks.doc1.doc1_check import Doc1Check
from ticket_docs.service.checks.ticket_folder import TicketFolder
from ticket_docs.storage.processes.command_runner import CommandRunner


class TestDoc1Check:
    def rules_file(self, tmp_path: Path) -> Path:
        target = tmp_path / "ticket-documentation.md"
        shutil.copy(TicketBuilder.REPOSITORY / ".claude" / "rules" / "ticket-documentation.md", target)
        return target

    def test_the_rule_script_prints_nothing_for_a_complete_explain(
        self, folder: TicketFolder, tmp_path: Path, logger: logging.Logger
    ) -> None:
        assert Doc1Check(self.rules_file(tmp_path), CommandRunner(logger), logger).problems(folder) == []

    def test_what_the_rule_script_prints_is_reported(
        self, folder: TicketFolder, ticket: TicketBuilder, tmp_path: Path, logger: logging.Logger
    ) -> None:
        ticket.edit("EXPLAIN.md", "### 3.1 API changes", "### 3.2 Flow")
        problems = Doc1Check(self.rules_file(tmp_path), CommandRunner(logger), logger).problems(folder)
        assert problems == [
            "DOC-1: GH-7/EXPLAIN.md: sub-section 3.1 missing",
            "DOC-1: GH-7/EXPLAIN.md: '### 3.1 API changes' must be the first sub-section of section 3",
        ]

    def test_a_rules_file_without_the_script_is_named(
        self, folder: TicketFolder, tmp_path: Path, logger: logging.Logger
    ) -> None:
        rules = tmp_path / "rules.md"
        rules.write_text("# Rules\n\n## DOC-1 — x\n\nNo script.\n", encoding="utf-8")
        assert Doc1Check(rules, CommandRunner(logger), logger).problems(folder) == [
            f"{rules}: DOC-1 check script not found, run it by hand"
        ]
