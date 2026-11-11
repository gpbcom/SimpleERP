from __future__ import annotations

import logging
import zipfile
from pathlib import Path

from ticket_docs.storage.tickets.ticket_repository import TicketRepository


class TestTicketRepository:
    def test_a_ticket_folder_and_its_files_are_read(self, tickets: Path, logger: logging.Logger) -> None:
        folder = tickets / "GH-3"
        (folder / "tests-evidences" / "run").mkdir(parents=True)
        (folder / "PLAN.md").write_text("# Plan\n", encoding="utf-8")
        (folder / "tests-evidences" / "run" / "README.md").write_text("# Run\n", encoding="utf-8")
        repository = TicketRepository(tickets, logger)
        assert repository.exists("GH-3")
        assert not repository.exists("GH-4")
        assert repository.folder("GH-3") == folder
        assert repository.read("GH-3", "PLAN.md") == "# Plan\n"
        assert repository.read("GH-3", "TICKET.md") is None
        assert repository.markdown("GH-3") == [folder / "PLAN.md", folder / "tests-evidences" / "run" / "README.md"]

    def test_the_index_is_written_at_the_root_or_elsewhere(
        self, tickets: Path, tmp_path: Path, logger: logging.Logger
    ) -> None:
        repository = TicketRepository(tickets, logger)
        assert repository.index() is None
        assert repository.write_index("# Index\n") == tickets / "README.md"
        assert repository.index() == "# Index\n"
        other = tmp_path / "out" / "index.md"
        assert repository.write_index("# Elsewhere\n", other) == other
        assert repository.index() == "# Index\n"

    def test_a_ticket_folder_is_zipped_under_its_key(
        self, tickets: Path, tmp_path: Path, logger: logging.Logger
    ) -> None:
        (tickets / "GH-3" / "attachments").mkdir(parents=True)
        (tickets / "GH-3" / "PLAN.md").write_text("# Plan\n", encoding="utf-8")
        archive = TicketRepository(tickets, logger).archive("GH-3", tmp_path / "out" / "GH-3-20261110-1200.zip")
        assert archive == tmp_path / "out" / "GH-3-20261110-1200.zip"
        with zipfile.ZipFile(archive) as zipped:
            assert "GH-3/PLAN.md" in zipped.namelist()
