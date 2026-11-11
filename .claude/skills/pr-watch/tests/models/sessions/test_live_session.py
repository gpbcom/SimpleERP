from __future__ import annotations

from typing import ClassVar, Dict

import pytest
from pydantic import JsonValue, ValidationError

from pr_watch.models.sessions.exceptions import (
    SELiveSessionInvalidCwd,
    SELiveSessionInvalidEntrypoint,
    SELiveSessionInvalidPid,
    SELiveSessionInvalidSessionId,
    SELiveSessionInvalidStatus,
)
from pr_watch.models.sessions.live_session import LiveSession


class TestLiveSession:
    REQUIRED: ClassVar[Dict[str, JsonValue]] = {"session_id": "7a30c2c8-75fe-4e6a-8475-dc3d38910314", "pid": 22839}
    FULL: ClassVar[Dict[str, JsonValue]] = {
        "session_id": "7a30c2c8-75fe-4e6a-8475-dc3d38910314",
        "pid": 22839,
        "cwd": "/home/me/simple-erp",
        "entrypoint": "claude-vscode",
        "status": "idle",
    }

    def test_defaults(self) -> None:
        model = LiveSession(**self.REQUIRED)
        assert model.cwd == LiveSession.model_fields["cwd"].get_default(call_default_factory=True)
        assert model.entrypoint == LiveSession.model_fields["entrypoint"].get_default(call_default_factory=True)
        assert model.status == LiveSession.model_fields["status"].get_default(call_default_factory=True)

    def test_full_valid_construction(self) -> None:
        model = LiveSession(**self.FULL)
        assert model.in_vscode

    @pytest.mark.parametrize("name", ["cwd", "entrypoint", "status"])
    def test_none_becomes_the_default(self, name: str) -> None:
        model = LiveSession(**{**self.FULL, name: None})
        assert getattr(model, name) == LiveSession.model_fields[name].get_default(call_default_factory=True)

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("session_id", "", SELiveSessionInvalidSessionId),
            ("session_id", None, SELiveSessionInvalidSessionId),
            ("pid", -1, SELiveSessionInvalidPid),
            ("pid", None, SELiveSessionInvalidPid),
            ("cwd", "", SELiveSessionInvalidCwd),
            ("cwd", 1, SELiveSessionInvalidCwd),
            ("entrypoint", "", SELiveSessionInvalidEntrypoint),
            ("entrypoint", 1, SELiveSessionInvalidEntrypoint),
            ("status", "", SELiveSessionInvalidStatus),
            ("status", 2, SELiveSessionInvalidStatus),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            LiveSession(**{**self.FULL, name: value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            LiveSession(**self.FULL, surprise=1)

    def test_round_trip(self) -> None:
        model = LiveSession(**self.FULL)
        assert LiveSession.model_validate_json(model.model_dump_json()) == model
