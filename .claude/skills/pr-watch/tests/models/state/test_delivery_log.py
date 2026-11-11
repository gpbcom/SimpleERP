from __future__ import annotations

from typing import ClassVar, Dict

import pytest
from pydantic import JsonValue, ValidationError

from pr_watch.models.state.delivery_log import DeliveryLog
from pr_watch.models.state.exceptions import (
    SEDeliveryLogInvalidDispatched,
    SEDeliveryLogInvalidNotified,
)


class TestDeliveryLog:
    REQUIRED: ClassVar[Dict[str, JsonValue]] = {}
    FULL: ClassVar[Dict[str, JsonValue]] = {
        "dispatched": {"GH-12:gpbcom/simple-erp#7|checks:668501e0d3a1": "2026-11-10T09:10:00+01:00"},
        "notified": {"GH-12": "2026-11-10T09:10:00+01:00"},
    }

    def test_defaults(self) -> None:
        model = DeliveryLog(**self.REQUIRED)
        assert model.dispatched == DeliveryLog.model_fields["dispatched"].get_default(call_default_factory=True)
        assert model.notified == DeliveryLog.model_fields["notified"].get_default(call_default_factory=True)

    def test_full_valid_construction(self) -> None:
        model = DeliveryLog(**self.FULL)
        assert list(model.notified) == ["GH-12"]

    @pytest.mark.parametrize("name", ["dispatched", "notified"])
    def test_none_becomes_the_default(self, name: str) -> None:
        model = DeliveryLog(**{**self.FULL, name: None})
        assert getattr(model, name) == DeliveryLog.model_fields[name].get_default(call_default_factory=True)

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("dispatched", [], SEDeliveryLogInvalidDispatched),
            ("dispatched", "x", SEDeliveryLogInvalidDispatched),
            ("notified", [], SEDeliveryLogInvalidNotified),
            ("notified", 1, SEDeliveryLogInvalidNotified),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            DeliveryLog(**{**self.FULL, name: value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            DeliveryLog(**self.FULL, surprise=1)

    def test_round_trip(self) -> None:
        model = DeliveryLog(**self.FULL)
        assert DeliveryLog.model_validate_json(model.model_dump_json()) == model
