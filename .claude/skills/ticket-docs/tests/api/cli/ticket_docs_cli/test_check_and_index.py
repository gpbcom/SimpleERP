from __future__ import annotations

from pathlib import Path

from tests.api.cli.ticket_docs_cli.helpers import call
from tests.builders.evidence_builder import EvidenceBuilder
from tests.builders.git_sandbox import GitSandbox
from tests.builders.ticket_builder import TicketBuilder


class TestCheckAndIndex:
    def test_a_complete_folder_prints_nothing_once_indexed(self, tmp_path: Path) -> None:
        sandbox = GitSandbox(tmp_path / "repo")
        tickets = sandbox.root / "docs" / "tickets"
        TicketBuilder(tickets).from_templates()
        code, out, _ = call(["report-index"], sandbox.root)
        assert (code, out) == (0, f"{tickets.resolve() / 'README.md'}\n")
        assert call(["check", "GH-7", "--offline"], sandbox.root) == (0, "", "")

    def test_problems_are_printed_one_per_line(self, tmp_path: Path) -> None:
        sandbox = GitSandbox(tmp_path / "repo")
        tickets = sandbox.root / "docs" / "tickets"
        TicketBuilder(tickets).minimal()
        (tickets / "GH-7" / "PLAN.md").unlink()
        code, out, _ = call(["check", "GH-7", "--offline", "--root", str(tickets)], tmp_path)
        assert code == 1
        assert "GH-7/PLAN.md: missing\n" in out

    def test_the_index_can_be_written_elsewhere_without_touching_the_root(self, tmp_path: Path) -> None:
        tickets = tmp_path / "tickets"
        EvidenceBuilder(tickets, "GH-1").folder("local-2026-11-10-unit-x")
        output = tmp_path / "out" / "index.md"
        code, out, _ = call(["report-index", "--root", str(tickets), "--output", str(output)], tmp_path)
        assert (code, out) == (0, f"{output}\n")
        assert "local-2026-11-10-unit-x" in output.read_text(encoding="utf-8")
        assert not (tickets / "README.md").exists()

    def test_a_missing_ticket_folder_is_one_problem(self, tmp_path: Path) -> None:
        code, out, _ = call(["check", "GH-9", "--offline", "--root", str(tmp_path)], tmp_path)
        assert (code, out) == (1, f"{tmp_path / 'GH-9'}: no such folder\n")
