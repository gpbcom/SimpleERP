from __future__ import annotations

import logging
from pathlib import Path

import pytest

from tests.builders.evidence_builder import EvidenceBuilder
from ticket_docs.models.evidence.exceptions import SEEvidenceRunInvalidKind
from ticket_docs.storage.evidence.evidence_repository import EvidenceRepository
from ticket_docs.storage.evidence.exceptions import SEEvidenceReadmeMissingError


class TestEvidenceRepository:
    def test_tickets_and_run_folders_are_listed_in_order(
        self, tickets: Path, evidence: EvidenceBuilder, logger: logging.Logger
    ) -> None:
        evidence.folder("local-2026-11-10-unit-b")
        evidence.folder("local-2026-11-10-tdd-red-b")
        (tickets / "GH-1" / "tests-evidences" / "history").mkdir()
        EvidenceBuilder(tickets, "GH-12").folder("dev-2026-11-11-stage")
        (tickets / "notes").mkdir()
        repository = EvidenceRepository(tickets, logger)
        assert repository.tickets() == ["GH-1", "GH-12"]
        assert [folder.name for folder in repository.folders("GH-1")] == [
            "local-2026-11-10-tdd-red-b",
            "local-2026-11-10-unit-b",
        ]
        assert repository.folders("GH-99") == []

    def test_a_folder_is_read_from_its_readme(
        self, tickets: Path, evidence: EvidenceBuilder, logger: logging.Logger
    ) -> None:
        folder = evidence.folder("local-2026-11-10-unit-b")
        run = EvidenceRepository(tickets, logger).read(folder)
        assert (run.folder, run.counts) == ("local-2026-11-10-unit-b", "3/3")

    def test_a_folder_without_readme_or_with_a_bad_row_is_refused(
        self, tickets: Path, evidence: EvidenceBuilder, logger: logging.Logger
    ) -> None:
        repository = EvidenceRepository(tickets, logger)
        empty = tickets / "GH-1" / "tests-evidences" / "local-2026-11-10-empty"
        empty.mkdir(parents=True)
        with pytest.raises(SEEvidenceReadmeMissingError):
            repository.read(empty)
        bad = evidence.folder("local-2026-11-10-bad", {"Kind": "<unit | gui>"})
        with pytest.raises(SEEvidenceRunInvalidKind):
            repository.read(bad)

    def test_a_new_folder_never_overwrites_an_old_one(self, tickets: Path, logger: logging.Logger) -> None:
        repository = EvidenceRepository(tickets, logger)
        first = repository.create("GH-1", "local-2026-11-10-unit-x")
        second = repository.create("GH-1", "local-2026-11-10-unit-x")
        third = repository.create("GH-1", "local-2026-11-10-unit-x")
        assert [first.name, second.name, third.name] == [
            "local-2026-11-10-unit-x",
            "local-2026-11-10-unit-x-2",
            "local-2026-11-10-unit-x-3",
        ]
        assert first.parent == tickets / "GH-1" / "tests-evidences"

    def test_files_are_written_copied_and_listed(self, tickets: Path, tmp_path: Path, logger: logging.Logger) -> None:
        repository = EvidenceRepository(tickets, logger)
        folder = repository.create("GH-1", "local-2026-11-10-gui-x")
        repository.write(folder, "console.txt", "ok\n")
        report = tmp_path / "playwright-report"
        report.mkdir()
        (report / "index.html").write_text("<html/>", encoding="utf-8")
        assert repository.copy_in(report, folder, "playwright-report")
        assert not repository.copy_in(tmp_path / "missing.json", folder, "results.json")
        assert (folder / "console.txt").read_text(encoding="utf-8") == "ok\n"
        assert repository.files(folder) == ["console.txt", "playwright-report/"]

    def test_files_over_the_limit_are_found(
        self, tickets: Path, evidence: EvidenceBuilder, logger: logging.Logger
    ) -> None:
        folder = evidence.folder("local-2026-11-10-unit-x")
        (folder / "big.log").write_bytes(b"x" * 2048)
        large = EvidenceRepository(tickets, logger).large_files("GH-1", 1024)
        assert large == [folder / "big.log"]
