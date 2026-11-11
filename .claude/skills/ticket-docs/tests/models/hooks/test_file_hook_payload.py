from __future__ import annotations

import json
from pathlib import Path
from typing import Optional

import pytest
from pydantic import JsonValue

from ticket_docs.models.hooks.exceptions import SEFileHookPayloadInvalidCwd, SEFileHookPayloadInvalidPath
from ticket_docs.models.hooks.file_hook_payload import FileHookPayload


class TestFileHookPayload:
    def test_defaults(self) -> None:
        assert FileHookPayload(path="src/a.py").cwd is None

    def test_full_valid_construction(self, tmp_path: Path) -> None:
        payload = FileHookPayload(path=" src/a.py ", cwd=str(tmp_path))
        assert (payload.path, payload.cwd) == ("src/a.py", tmp_path)

    @pytest.mark.parametrize("name", ["cwd"])
    def test_none_becomes_the_default(self, name: str) -> None:
        assert getattr(FileHookPayload.model_validate({"path": "a", name: None}), name) is None

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("path", "", SEFileHookPayloadInvalidPath),
            ("path", ["a"], SEFileHookPayloadInvalidPath),
            ("cwd", "", SEFileHookPayloadInvalidCwd),
            ("cwd", 3, SEFileHookPayloadInvalidCwd),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            FileHookPayload.model_validate({"path": "a", name: value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValueError, match="extra"):
            FileHookPayload.model_validate({"path": "a", "other": 1})

    def test_round_trip(self) -> None:
        payload = FileHookPayload(path="a", cwd="/repo")
        assert FileHookPayload.model_validate(payload.model_dump()) == payload

    @pytest.mark.parametrize(
        ("tool_input", "path"),
        [
            ({"file_path": "/repo/a.py", "content": "x"}, "/repo/a.py"),
            ({"notebook_path": "/repo/n.ipynb"}, "/repo/n.ipynb"),
            ({"command": "ls"}, None),
            ({"file_path": ""}, None),
        ],
    )
    def test_the_file_of_a_file_tool_is_read_from_the_hook_input(
        self, tool_input: JsonValue, path: Optional[str]
    ) -> None:
        payload = FileHookPayload.from_json(json.dumps({"tool_input": tool_input, "cwd": "/repo"}))
        assert (payload.path if payload else None) == path

    @pytest.mark.parametrize("text", ["", "not json", "[]", "{}"])
    def test_an_input_without_a_file_gives_nothing(self, text: str) -> None:
        assert FileHookPayload.from_json(text) is None
