from __future__ import annotations

import logging

from tests.builders.evidence_builder import EvidenceBuilder
from tests.builders.ticket_builder import TicketBuilder
from ticket_docs.service.checks.folder.evidence_index_check import EvidenceIndexCheck
from ticket_docs.service.checks.ticket_folder import TicketFolder


class TestEvidenceIndexCheck:
    def test_every_run_folder_is_in_the_ticket_index(
        self, folder: TicketFolder, ticket: TicketBuilder, logger: logging.Logger
    ) -> None:
        builder = EvidenceBuilder(ticket.tickets, "GH-7")
        builder.folder("local-2026-11-10-unit-a")
        builder.folder("local-2026-11-10-unit-b")
        (ticket.folder / "tests-evidences" / "history").mkdir()
        (ticket.folder / "tests-evidences" / "local-2026-11-10-empty").mkdir()
        ticket.edit(
            "tests-evidences/README.md",
            "|---|---|\n",
            "|---|---|\n| [local-2026-11-10-unit-a](local-2026-11-10-unit-a/README.md) | ✅ |\n",
        )
        assert EvidenceIndexCheck(logger).problems(folder) == [
            "GH-7/tests-evidences/local-2026-11-10-empty: README.md missing",
            "GH-7/tests-evidences/README.md: local-2026-11-10-empty not in the index",
            "GH-7/tests-evidences/README.md: local-2026-11-10-unit-b not in the index",
        ]

    def test_without_an_index_there_is_nothing_to_compare(
        self, folder: TicketFolder, ticket: TicketBuilder, logger: logging.Logger
    ) -> None:
        (ticket.folder / "tests-evidences" / "README.md").unlink()
        EvidenceBuilder(ticket.tickets, "GH-7").folder("local-2026-11-10-unit-a")
        assert EvidenceIndexCheck(logger).problems(folder) == []
