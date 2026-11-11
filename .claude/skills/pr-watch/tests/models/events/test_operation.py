from __future__ import annotations

from typing import ClassVar, Dict

import pytest
from pydantic import JsonValue, ValidationError

from pr_watch.models.events.exceptions import (
    SEOperationInvalidAt,
    SEOperationInvalidDetail,
    SEOperationInvalidKind,
    SEOperationInvalidLink,
    SEOperationInvalidPrId,
)
from pr_watch.models.events.operation import Operation


class TestOperation:
    REQUIRED: ClassVar[Dict[str, JsonValue]] = {
        "at": "2026-11-10T09:10:00+01:00",
        "pr_id": "GH-12:gpbcom/simple-erp#7",
        "kind": "detected",
        "detail": "2 checks failed on 668501e0",
    }
    FULL: ClassVar[Dict[str, JsonValue]] = {
        "at": "2026-11-10T09:10:00+01:00",
        "pr_id": "GH-12:gpbcom/simple-erp#7",
        "kind": "detected",
        "detail": "2 checks failed on 668501e0",
        "link": "https://github.com/gpbcom/simple-erp/pull/7",
    }

    def test_defaults(self) -> None:
        model = Operation(**self.REQUIRED)
        assert model.link == Operation.model_fields["link"].get_default(call_default_factory=True)

    def test_full_valid_construction(self) -> None:
        model = Operation(**self.FULL)
        assert model.key == "GH-12"

    @pytest.mark.parametrize("name", ["link"])
    def test_none_becomes_the_default(self, name: str) -> None:
        model = Operation(**{**self.FULL, name: None})
        assert getattr(model, name) == Operation.model_fields[name].get_default(call_default_factory=True)

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("at", "now", SEOperationInvalidAt),
            ("at", None, SEOperationInvalidAt),
            ("pr_id", "", SEOperationInvalidPrId),
            ("pr_id", None, SEOperationInvalidPrId),
            ("kind", "testing_posted", SEOperationInvalidKind),
            ("kind", None, SEOperationInvalidKind),
            ("detail", "", SEOperationInvalidDetail),
            ("detail", 4, SEOperationInvalidDetail),
            ("link", "pull/7", SEOperationInvalidLink),
            ("link", 2, SEOperationInvalidLink),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            Operation(**{**self.FULL, name: value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            Operation(**self.FULL, surprise=1)

    def test_round_trip(self) -> None:
        model = Operation(**self.FULL)
        assert Operation.model_validate_json(model.model_dump_json()) == model
