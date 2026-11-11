from __future__ import annotations

import json
from pathlib import Path

import pytest
from pydantic import JsonValue

from ticket_docs.models.hooks.exceptions import SEHookPayloadInvalidCommand, SEHookPayloadInvalidCwd
from ticket_docs.models.hooks.hook_payload import HookPayload


class TestHookPayload:
    def test_defaults(self) -> None:
        assert HookPayload(command="git status").cwd is None

    def test_full_valid_construction(self, tmp_path: Path) -> None:
        payload = HookPayload(command=" git commit -m x ", cwd=str(tmp_path))
        assert (payload.command, payload.cwd) == ("git commit -m x", tmp_path)

    @pytest.mark.parametrize("name", ["cwd"])
    def test_none_becomes_the_default(self, name: str) -> None:
        assert getattr(HookPayload.model_validate({"command": "ls", name: None}), name) is None

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("command", "", SEHookPayloadInvalidCommand),
            ("command", ["git"], SEHookPayloadInvalidCommand),
            ("cwd", "", SEHookPayloadInvalidCwd),
            ("cwd", 3, SEHookPayloadInvalidCwd),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            HookPayload.model_validate({"command": "ls", name: value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValueError, match="extra"):
            HookPayload.model_validate({"command": "ls", "tool_name": "Bash"})

    def test_round_trip(self) -> None:
        payload = HookPayload(command="ls", cwd="/tmp")
        assert HookPayload.model_validate(payload.model_dump()) == payload

    def test_the_hook_input_is_read_from_claude_codes_json(self, tmp_path: Path) -> None:
        text = json.dumps(
            {"session_id": "s", "tool_name": "Bash", "tool_input": {"command": "git push"}, "cwd": str(tmp_path)}
        )
        assert HookPayload.from_json(text) == HookPayload(command="git push", cwd=str(tmp_path))

    @pytest.mark.parametrize(
        "text", ["not json", "[]", "{}", '{"tool_input": {"command": "  "}}', '{"tool_input": "git push"}']
    )
    def test_an_input_without_a_command_gives_nothing(self, text: str) -> None:
        assert HookPayload.from_json(text) is None
