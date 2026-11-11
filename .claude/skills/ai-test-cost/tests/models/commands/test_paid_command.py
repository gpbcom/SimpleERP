from __future__ import annotations

from typing import Dict

import pytest
from pydantic import JsonValue

from ai_cost.models.commands.exceptions import SEPaidCommandInvalidName, SEPaidCommandInvalidPattern
from ai_cost.models.commands.paid_command import PaidCommand


class TestPaidCommand:
    def test_defaults(self) -> None:
        assert PaidCommand(name="judge", pattern=r"\bjudge\b").pattern == r"\bjudge\b"

    def test_full_valid_construction(self) -> None:
        command = PaidCommand.model_validate({"name": " pytest llm ", "pattern": r"\bpytest\b.*-m\s*llm\b"})
        assert command.name == "pytest llm"

    def test_none_becomes_the_default(self) -> None:
        with pytest.raises(SEPaidCommandInvalidName):
            PaidCommand.model_validate({"name": None, "pattern": "x"})

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("name", "", SEPaidCommandInvalidName),
            ("pattern", "", SEPaidCommandInvalidPattern),
            ("pattern", "(unclosed", SEPaidCommandInvalidPattern),
            ("pattern", 3, SEPaidCommandInvalidPattern),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        fields: Dict[str, JsonValue] = {"name": "judge", "pattern": "judge"}
        fields[name] = value
        with pytest.raises(error):
            PaidCommand.model_validate(fields)

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValueError, match="extra"):
            PaidCommand.model_validate({"name": "judge", "pattern": "judge", "cost": 1})

    def test_round_trip(self) -> None:
        command = PaidCommand(name="judge", pattern="judge")
        assert PaidCommand.model_validate_json(command.model_dump_json()) == command
