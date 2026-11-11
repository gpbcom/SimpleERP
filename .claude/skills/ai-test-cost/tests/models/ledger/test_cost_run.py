from __future__ import annotations

from decimal import Decimal

import pytest
from pydantic import JsonValue

from ai_cost.models.enums import CostSource, RunStatus
from ai_cost.models.ledger.cost_run import CostRun
from ai_cost.models.ledger.exceptions import (
    SECostRunInvalidAmount,
    SECostRunInvalidChoice,
    SECostRunInvalidExitCode,
    SECostRunInvalidMoment,
    SECostRunInvalidSettled,
    SECostRunInvalidText,
    SECostRunInvalidUsage,
)
from tests.models.ledger.helpers import FINISHED_ON, STARTED_ON, run_fields


class TestCostRun:
    def test_defaults(self) -> None:
        run = CostRun(
            id="r1",
            label="x",
            command="pytest",
            started_on=STARTED_ON,
            estimate_usd=Decimal("1"),
            status=RunStatus.RUNNING,
            source=CostSource.ESTIMATE,
        )
        assert (run.finished_on, run.cost_usd, run.usage, run.settled, run.exit_code, run.note) == (
            None,
            Decimal("0"),
            {},
            False,
            None,
            None,
        )

    def test_full_valid_construction(self) -> None:
        run = CostRun.model_validate(run_fields())
        assert run.status is RunStatus.DONE
        assert run.source is CostSource.USAGE_REPORT
        assert run.finished_on == FINISHED_ON
        assert run.usage["claude-haiku-5-5"].input_tokens == 1000
        assert run.estimate_usd == Decimal("0.50")

    @pytest.mark.parametrize(
        ("name", "default"),
        [
            ("finished_on", None),
            ("cost_usd", Decimal("0")),
            ("usage", {}),
            ("settled", False),
            ("exit_code", None),
            ("note", None),
        ],
    )
    def test_none_becomes_the_default(self, name: str, default: JsonValue) -> None:
        fields = run_fields()
        fields[name] = None
        assert getattr(CostRun.model_validate(fields), name) == default

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("id", " ", SECostRunInvalidText),
            ("label", None, SECostRunInvalidText),
            ("command", 3, SECostRunInvalidText),
            ("note", "", SECostRunInvalidText),
            ("started_on", "yesterday", SECostRunInvalidMoment),
            ("started_on", "2026-11-10T09:00:00", SECostRunInvalidMoment),
            ("finished_on", 12, SECostRunInvalidMoment),
            ("estimate_usd", "-1", SECostRunInvalidAmount),
            ("cost_usd", True, SECostRunInvalidAmount),
            ("status", "lost", SECostRunInvalidChoice),
            ("source", "bedrock", SECostRunInvalidChoice),
            ("usage", ["claude-haiku-5-5"], SECostRunInvalidUsage),
            ("settled", "yes", SECostRunInvalidSettled),
            ("exit_code", "0", SECostRunInvalidExitCode),
            ("exit_code", False, SECostRunInvalidExitCode),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        fields = run_fields()
        fields[name] = value
        with pytest.raises(error):
            CostRun.model_validate(fields)

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValueError, match="extra"):
            CostRun.model_validate({**run_fields(), "identities": []})

    def test_round_trip(self) -> None:
        run = CostRun.model_validate(run_fields())
        assert CostRun.model_validate_json(run.model_dump_json()) == run

    def test_amounts_are_json_numbers(self) -> None:
        dumped = CostRun.model_validate(run_fields()).model_dump_json()
        assert '"estimate_usd":0.5' in dumped
        assert '"cost_usd":0.25' in dumped
