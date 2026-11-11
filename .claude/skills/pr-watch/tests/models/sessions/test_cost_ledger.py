from __future__ import annotations

from typing import ClassVar, Dict

import pytest
from pydantic import JsonValue, ValidationError

from pr_watch.models.sessions.cost_ledger import CostLedger
from pr_watch.models.sessions.exceptions import (
    SECostLedgerInvalidBlocked,
    SECostLedgerInvalidCapUsd,
    SECostLedgerInvalidSpentUsd,
    SECostLedgerInvalidTicket,
)


class TestCostLedger:
    REQUIRED: ClassVar[Dict[str, JsonValue]] = {"ticket": "GH-12", "cap_usd": 20.0, "spent_usd": 3.25, "blocked": False}
    FULL: ClassVar[Dict[str, JsonValue]] = {"ticket": "GH-12", "cap_usd": 20.0, "spent_usd": 3.25, "blocked": False}

    def test_defaults(self) -> None:
        model = CostLedger(**self.REQUIRED)
        assert CostLedger.model_validate(model.model_dump()) == model

    def test_full_valid_construction(self) -> None:
        model = CostLedger(**self.FULL)
        assert model.spent_usd == 3.25

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("ticket", "", SECostLedgerInvalidTicket),
            ("ticket", None, SECostLedgerInvalidTicket),
            ("cap_usd", -1, SECostLedgerInvalidCapUsd),
            ("cap_usd", True, SECostLedgerInvalidCapUsd),
            ("cap_usd", None, SECostLedgerInvalidCapUsd),
            ("spent_usd", "3", SECostLedgerInvalidSpentUsd),
            ("spent_usd", None, SECostLedgerInvalidSpentUsd),
            ("blocked", 0, SECostLedgerInvalidBlocked),
            ("blocked", None, SECostLedgerInvalidBlocked),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            CostLedger(**{**self.FULL, name: value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            CostLedger(**self.FULL, surprise=1)

    def test_round_trip(self) -> None:
        model = CostLedger(**self.FULL)
        assert CostLedger.model_validate_json(model.model_dump_json()) == model
