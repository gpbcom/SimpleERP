from __future__ import annotations

import json

import pytest
from pydantic import JsonValue

from progress_updates.models.hooks.exceptions import (
    SEToolCallInvalidBackground,
    SEToolCallInvalidToolName,
    SEToolCallUnreadable,
)
from progress_updates.models.hooks.tool_call import ToolCall


class TestToolCall:
    def test_full_valid_construction(self) -> None:
        call = ToolCall.model_validate({"tool_name": " Bash ", "background": True})
        assert (call.tool_name, call.background) == ("Bash", True)

    def test_defaults(self) -> None:
        assert ToolCall.model_validate({"tool_name": "Read"}).background is False

    def test_none_becomes_the_default(self) -> None:
        assert ToolCall.model_validate({"tool_name": "Read", "background": None}).background is False

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("tool_name", "", SEToolCallInvalidToolName),
            ("tool_name", 3, SEToolCallInvalidToolName),
            ("background", "yes", SEToolCallInvalidBackground),
            ("background", 1, SEToolCallInvalidBackground),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        fields: dict[str, JsonValue] = {"tool_name": "Bash", "background": False}
        fields[name] = value
        with pytest.raises(error):
            ToolCall.model_validate(fields)

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValueError, match="extra"):
            ToolCall.model_validate({"tool_name": "Bash", "other": 1})

    def test_round_trip(self) -> None:
        call = ToolCall.model_validate({"tool_name": "Agent", "background": True})
        assert ToolCall.model_validate(call.model_dump()) == call

    def test_a_hook_payload_is_read(self) -> None:
        payload = {"tool_name": "Bash", "tool_input": {"command": "sleep 300", "run_in_background": True}}
        assert ToolCall.from_json(json.dumps(payload)) == ToolCall(tool_name="Bash", background=True)

    @pytest.mark.parametrize("text", ["", "not json", "[]", '{"tool_input": {}}'])
    def test_a_payload_that_cannot_be_read_is_refused(self, text: str) -> None:
        with pytest.raises(SEToolCallUnreadable):
            ToolCall.from_json(text)
