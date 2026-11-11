from __future__ import annotations

from tests.builders.evidence_builder import EvidenceBuilder
from tests.builders.ticket_builder import TicketBuilder
from ticket_docs.service.checks.ticket_folder import TicketFolder


class TestTicketFolder:
    def test_files_are_read_and_labelled(self, folder: TicketFolder, ticket: TicketBuilder) -> None:
        assert folder.path == ticket.folder
        assert str(folder.text("PLAN.md")).startswith("# Plan — GH-7")
        assert folder.text("STATUS.md") is None
        assert folder.label("PLAN.md") == "GH-7/PLAN.md"

    def test_the_hand_over_row_tells_whether_the_ticket_is_handed_over(
        self, folder: TicketFolder, ticket: TicketBuilder
    ) -> None:
        assert not folder.handed_over()
        ticket.edit(
            "PROGRESS.md",
            "| 2 — Final acceptance run and hand-over | ⬜ To do | — | — | — |",
            "| 2 — Final acceptance run and hand-over | ✅ Done | 2026-11-10 10:00 | 2026-11-10 11:00 | 1h00 |",
        )
        assert folder.handed_over()

    def test_runs_are_read_and_unreadable_ones_are_kept_apart(
        self, folder: TicketFolder, evidence: EvidenceBuilder
    ) -> None:
        builder = EvidenceBuilder(evidence.root, "GH-7")
        builder.folder("local-2026-11-10-unit-b")
        builder.folder("local-2026-11-10-tdd-red-b", {"Commit": "`abc` on `x`"})
        assert [run.folder for run in folder.runs()] == ["local-2026-11-10-unit-b"]
        assert list(folder.unreadable()) == ["local-2026-11-10-tdd-red-b"]
        assert "Invalid commit" in folder.unreadable()["local-2026-11-10-tdd-red-b"]
        assert folder.run_folder("local-2026-11-10-unit-b").is_dir()
