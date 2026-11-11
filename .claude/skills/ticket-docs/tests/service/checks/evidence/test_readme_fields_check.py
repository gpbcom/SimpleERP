from __future__ import annotations

import logging

from tests.builders.evidence_builder import EvidenceBuilder
from tests.builders.ticket_builder import TicketBuilder
from ticket_docs.service.checks.evidence.readme_fields_check import ReadmeFieldsCheck
from ticket_docs.service.checks.ticket_folder import TicketFolder


class TestReadmeFieldsCheck:
    def test_a_complete_readme_has_no_problem(
        self, folder: TicketFolder, ticket: TicketBuilder, logger: logging.Logger
    ) -> None:
        EvidenceBuilder(ticket.tickets, "GH-7").folder("local-2026-11-10-unit-a")
        assert ReadmeFieldsCheck(logger).problems(folder) == []

    def test_missing_rows_and_raw_output_are_named(
        self, folder: TicketFolder, ticket: TicketBuilder, logger: logging.Logger
    ) -> None:
        builder = EvidenceBuilder(ticket.tickets, "GH-7")
        builder.folder("local-2026-11-10-unit-a", {"Command": None, "Kind": None}, files=())
        builder.folder("local-2026-11-10-unit-b", {"Commit": "`ef0211f` on `x`"})
        (ticket.folder / "tests-evidences" / "local-2026-11-10-unit-c").mkdir()
        problems = ReadmeFieldsCheck(logger).problems(folder)
        assert problems[:3] == [
            "GH-7/tests-evidences/local-2026-11-10-unit-a: README.md has no Command (TEST-8)",
            "GH-7/tests-evidences/local-2026-11-10-unit-a: README.md has no Kind (TEST-8)",
            "GH-7/tests-evidences/local-2026-11-10-unit-a: no raw output file next to README.md (TEST-8)",
        ]
        assert problems[3].startswith("GH-7/tests-evidences/local-2026-11-10-unit-b: README.md cannot be read: ")
        assert "Invalid commit" in problems[3]
        assert problems[4:] == [
            "GH-7/tests-evidences/local-2026-11-10-unit-c: README.md cannot be read: "
            + ("The evidence folder local-2026-11-10-unit-c has no README.md. (TEST-8)")
        ]
