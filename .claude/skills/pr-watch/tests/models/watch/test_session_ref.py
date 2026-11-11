from __future__ import annotations

from typing import ClassVar, Dict

import pytest
from pydantic import JsonValue, ValidationError

from pr_watch.models.watch.exceptions import (
    SESessionRefInvalidCwd,
    SESessionRefInvalidSessionId,
)
from pr_watch.models.watch.session_ref import SessionRef


class TestSessionRef:
    REQUIRED: ClassVar[Dict[str, JsonValue]] = {"session_id": "7a30c2c8-75fe-4e6a-8475-dc3d38910314"}
    FULL: ClassVar[Dict[str, JsonValue]] = {
        "session_id": "7a30c2c8-75fe-4e6a-8475-dc3d38910314",
        "cwd": "/home/me/simple-erp",
    }

    def test_defaults(self) -> None:
        model = SessionRef(**self.REQUIRED)
        assert model.cwd == SessionRef.model_fields["cwd"].get_default(call_default_factory=True)

    def test_full_valid_construction(self) -> None:
        model = SessionRef(**self.FULL)
        assert model.short == "7a30c2c8"

    @pytest.mark.parametrize("name", ["cwd"])
    def test_none_becomes_the_default(self, name: str) -> None:
        model = SessionRef(**{**self.FULL, name: None})
        assert getattr(model, name) == SessionRef.model_fields[name].get_default(call_default_factory=True)

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("session_id", "", SESessionRefInvalidSessionId),
            ("session_id", None, SESessionRefInvalidSessionId),
            ("cwd", "", SESessionRefInvalidCwd),
            ("cwd", 5, SESessionRefInvalidCwd),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            SessionRef(**{**self.FULL, name: value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            SessionRef(**self.FULL, surprise=1)

    def test_round_trip(self) -> None:
        model = SessionRef(**self.FULL)
        assert SessionRef.model_validate_json(model.model_dump_json()) == model
