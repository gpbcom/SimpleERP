from __future__ import annotations

import json
import logging
from decimal import Decimal
from pathlib import Path

import pytest

from ai_cost.models.ledger.ledger import Ledger
from ai_cost.storage.ledgers.exceptions import SELedgerTicketRefusedError, SELedgerUnreadableError
from ai_cost.storage.ledgers.ledger_repository import LedgerRepository


class TestLedgerRepository:
    def test_a_ticket_without_a_ledger_reads_as_none(self, tmp_path: Path, logger: logging.Logger) -> None:
        repository = LedgerRepository(tmp_path / "state", logger)
        assert (repository.read("GH-1"), repository.exists("GH-1")) == (None, False)

    def test_a_saved_ledger_reads_back_and_keeps_the_file_contract(
        self, tmp_path: Path, logger: logging.Logger
    ) -> None:
        repository = LedgerRepository(tmp_path / "state", logger)
        ledger = Ledger(ticket="GH-1", cap_usd=Decimal("20"), block_reason="killed at the cap")
        path = repository.save(ledger)
        assert path == tmp_path / "state" / "GH-1.json"
        assert repository.read("GH-1") == ledger
        document = json.loads(path.read_text(encoding="utf-8"))
        assert (document["ticket"], document["cap_usd"], document["spent_usd"], document["blocked"]) == (
            "GH-1",
            20,
            0,
            True,
        )

    @pytest.mark.parametrize("ticket", ["../GH-1", "ARE-1", "", "GH-1/../x"])
    def test_a_key_that_is_not_a_ticket_is_refused(self, tmp_path: Path, logger: logging.Logger, ticket: str) -> None:
        with pytest.raises(SELedgerTicketRefusedError):
            LedgerRepository(tmp_path, logger).read(ticket)

    def test_a_corrupt_ledger_is_unreadable(self, tmp_path: Path, logger: logging.Logger) -> None:
        (tmp_path / "GH-1.json").write_text("{not json", encoding="utf-8")
        with pytest.raises(SELedgerUnreadableError):
            LedgerRepository(tmp_path, logger).read("GH-1")

    def test_the_lock_is_held_then_released(self, tmp_path: Path, logger: logging.Logger) -> None:
        repository = LedgerRepository(tmp_path, logger)
        with repository.lock("GH-1"):
            assert (tmp_path / "GH-1.lock").exists()
        with repository.lock("GH-1"):
            repository.save(Ledger(ticket="GH-1", cap_usd=Decimal("20")))
        assert repository.exists("GH-1")
