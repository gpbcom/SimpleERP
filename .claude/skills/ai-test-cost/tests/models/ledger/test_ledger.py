from __future__ import annotations

import json
from decimal import Decimal
from typing import Dict

import pytest
from pydantic import JsonValue

from ai_cost.models.ledger.exceptions import (
    SELedgerInvalidBlockReason,
    SELedgerInvalidCapUsd,
    SELedgerInvalidRuns,
    SELedgerInvalidTicket,
)
from ai_cost.models.ledger.ledger import Ledger
from tests.models.ledger.helpers import run_fields


class TestLedger:
    def ledger_fields(self) -> Dict[str, JsonValue]:
        second = {**run_fields(), "id": "20261110-091000-ef34ab", "cost_usd": "1.75"}
        return {"ticket": "GH-1", "cap_usd": "20", "block_reason": None, "runs": [run_fields(), second]}

    def test_defaults(self) -> None:
        ledger = Ledger(ticket="GH-7", cap_usd=Decimal("20"))
        assert (ledger.runs, ledger.blocked, ledger.spent_usd, ledger.remaining_usd) == (
            [],
            False,
            Decimal("0"),
            Decimal("20"),
        )

    def test_full_valid_construction(self) -> None:
        ledger = Ledger.model_validate(self.ledger_fields())
        assert ledger.spent_usd == Decimal("2.00")
        assert ledger.remaining_usd == Decimal("18.00")
        assert ledger.blocked is False

    @pytest.mark.parametrize(("name", "default"), [("block_reason", None), ("runs", [])])
    def test_none_becomes_the_default(self, name: str, default: JsonValue) -> None:
        fields = self.ledger_fields()
        fields[name] = None
        assert getattr(Ledger.model_validate(fields), name) == default

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("ticket", "ARE-1", SELedgerInvalidTicket),
            ("ticket", "../GH-1", SELedgerInvalidTicket),
            ("ticket", None, SELedgerInvalidTicket),
            ("cap_usd", "0", SELedgerInvalidCapUsd),
            ("cap_usd", True, SELedgerInvalidCapUsd),
            ("block_reason", " ", SELedgerInvalidBlockReason),
            ("runs", {"a": 1}, SELedgerInvalidRuns),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        fields = self.ledger_fields()
        fields[name] = value
        with pytest.raises(error):
            Ledger.model_validate(fields)

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValueError, match="extra"):
            Ledger.model_validate({**self.ledger_fields(), "key": "GH-1"})

    def test_round_trip(self) -> None:
        ledger = Ledger.model_validate(self.ledger_fields())
        assert Ledger.model_validate_json(ledger.model_dump_json()) == ledger

    def test_a_block_reason_blocks_the_ticket(self) -> None:
        ledger = Ledger(ticket="GH-1", cap_usd=Decimal("20"), block_reason="killed at the cap")
        assert ledger.blocked is True

    def test_nothing_is_left_once_the_cap_is_passed(self) -> None:
        fields = self.ledger_fields()
        fields["cap_usd"] = "1"
        assert Ledger.model_validate(fields).remaining_usd == Decimal("0")

    def test_the_json_file_keeps_the_contract_other_tools_read(self) -> None:
        document = json.loads(Ledger.model_validate(self.ledger_fields()).model_dump_json())
        assert document["ticket"] == "GH-1"
        assert document["cap_usd"] == 20
        assert document["spent_usd"] == 2
        assert document["blocked"] is False
        assert len(document["runs"]) == 2
