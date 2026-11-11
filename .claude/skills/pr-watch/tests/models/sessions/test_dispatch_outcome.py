from __future__ import annotations

from typing import ClassVar, Dict

import pytest
from pydantic import JsonValue, ValidationError

from pr_watch.models.sessions.dispatch_outcome import DispatchOutcome
from pr_watch.models.sessions.exceptions import (
    SEDispatchOutcomeInvalidAction,
    SEDispatchOutcomeInvalidDetail,
    SEDispatchOutcomeInvalidOk,
)


class TestDispatchOutcome:
    REQUIRED: ClassVar[Dict[str, JsonValue]] = {
        "action": "reopened_vscode",
        "ok": True,
        "detail": "session 7a30c2c8 opened in VS Code",
    }
    FULL: ClassVar[Dict[str, JsonValue]] = {
        "action": "reopened_vscode",
        "ok": True,
        "detail": "session 7a30c2c8 opened in VS Code",
    }

    def test_defaults(self) -> None:
        model = DispatchOutcome(**self.REQUIRED)
        assert DispatchOutcome.model_validate(model.model_dump()) == model

    def test_full_valid_construction(self) -> None:
        model = DispatchOutcome(**self.FULL)
        assert model.ok

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("action", "opened", SEDispatchOutcomeInvalidAction),
            ("action", None, SEDispatchOutcomeInvalidAction),
            ("ok", 1, SEDispatchOutcomeInvalidOk),
            ("ok", None, SEDispatchOutcomeInvalidOk),
            ("detail", "", SEDispatchOutcomeInvalidDetail),
            ("detail", None, SEDispatchOutcomeInvalidDetail),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            DispatchOutcome(**{**self.FULL, name: value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            DispatchOutcome(**self.FULL, surprise=1)

    def test_round_trip(self) -> None:
        model = DispatchOutcome(**self.FULL)
        assert DispatchOutcome.model_validate_json(model.model_dump_json()) == model
