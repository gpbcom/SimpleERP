from __future__ import annotations

import pytest
from pydantic import JsonValue

from ticket_docs.models.evidence.command_outcome import CommandOutcome
from ticket_docs.models.evidence.exceptions import SECommandOutcomeInvalidExitCode, SECommandOutcomeInvalidOutput


class TestCommandOutcome:
    def test_defaults(self) -> None:
        assert CommandOutcome(exit_code=0).output == ""

    def test_full_valid_construction(self) -> None:
        outcome = CommandOutcome(exit_code=2, output="1 failed\n")
        assert (outcome.exit_code, outcome.output) == (2, "1 failed\n")

    @pytest.mark.parametrize("name", ["output"])
    def test_none_becomes_the_default(self, name: str) -> None:
        assert getattr(CommandOutcome.model_validate({"exit_code": 0, name: None}), name) == ""

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("exit_code", True, SECommandOutcomeInvalidExitCode),
            ("exit_code", "1", SECommandOutcomeInvalidExitCode),
            ("output", 3, SECommandOutcomeInvalidOutput),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            CommandOutcome.model_validate({"exit_code": 0, name: value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValueError, match="extra"):
            CommandOutcome.model_validate({"exit_code": 0, "pid": 1})

    def test_round_trip(self) -> None:
        outcome = CommandOutcome(exit_code=-9, output="killed")
        assert CommandOutcome.model_validate(outcome.model_dump()) == outcome
