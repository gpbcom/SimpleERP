from __future__ import annotations

import logging
from pathlib import Path

import pytest

from ai_cost.storage.reports.cost_file_repository import CostFileRepository
from ai_cost.storage.reports.exceptions import SECostTemplateUnreadableError


class TestCostFileRepository:
    TEMPLATE = Path(__file__).resolve().parents[3] / "templates" / "COST.md"

    def test_cost_md_goes_to_the_ticket_evidence_folder_of_the_callers_repository(
        self, repo: Path, logger: logging.Logger
    ) -> None:
        nested = repo / "src" / "api"
        nested.mkdir(parents=True)
        path = CostFileRepository(nested, self.TEMPLATE, logger).write("GH-1", "# AI test cost\n")
        assert path == repo.resolve() / "docs" / "tickets" / "GH-1" / "tests-evidences" / "COST.md"
        assert path.read_text(encoding="utf-8") == "# AI test cost\n"

    def test_a_caller_outside_a_repository_writes_nothing(self, tmp_path: Path, logger: logging.Logger) -> None:
        outside = tmp_path / "outside"
        outside.mkdir()
        assert CostFileRepository(outside, self.TEMPLATE, logger).write("GH-1", "x") is None
        assert not list(outside.rglob("COST.md"))

    def test_the_template_is_read(self, repo: Path, logger: logging.Logger) -> None:
        assert "${rows}" in CostFileRepository(repo, self.TEMPLATE, logger).template()

    def test_a_missing_template_is_unreadable(self, repo: Path, logger: logging.Logger) -> None:
        with pytest.raises(SECostTemplateUnreadableError):
            CostFileRepository(repo, repo / "missing.md", logger).template()
