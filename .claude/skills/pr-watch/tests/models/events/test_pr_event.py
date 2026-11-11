from __future__ import annotations

from typing import ClassVar, Dict

import pytest
from pydantic import JsonValue, ValidationError

from pr_watch.models.events.exceptions import (
    SEPrEventInvalidAckedOn,
    SEPrEventInvalidDetail,
    SEPrEventInvalidDetectedOn,
    SEPrEventInvalidId,
    SEPrEventInvalidKind,
)
from pr_watch.models.events.pr_event import PrEvent


class TestPrEvent:
    REQUIRED: ClassVar[Dict[str, JsonValue]] = {
        "id": "GH-12:gpbcom/simple-erp#7|checks:668501e0d3a1",
        "kind": "checks_failed",
        "detail": {"title": "2 checks failed on 668501e0"},
        "detected_on": "2026-11-10T09:10:00+01:00",
    }
    FULL: ClassVar[Dict[str, JsonValue]] = {
        "id": "GH-12:gpbcom/simple-erp#7|checks:668501e0d3a1",
        "kind": "checks_failed",
        "detail": {"title": "2 checks failed on 668501e0"},
        "detected_on": "2026-11-10T09:10:00+01:00",
        "acked_on": "2026-11-10T09:30:00+01:00",
    }

    def test_defaults(self) -> None:
        model = PrEvent(**self.REQUIRED)
        assert model.acked_on == PrEvent.model_fields["acked_on"].get_default(call_default_factory=True)

    def test_full_valid_construction(self) -> None:
        model = PrEvent(**self.FULL)
        assert model.pr_id == "GH-12:gpbcom/simple-erp#7"
        assert model.key == "GH-12"
        assert not model.is_pending

    @pytest.mark.parametrize("name", ["acked_on"])
    def test_none_becomes_the_default(self, name: str) -> None:
        model = PrEvent(**{**self.FULL, name: None})
        assert getattr(model, name) == PrEvent.model_fields[name].get_default(call_default_factory=True)

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("id", "", SEPrEventInvalidId),
            ("id", None, SEPrEventInvalidId),
            ("kind", "jenkins_failed", SEPrEventInvalidKind),
            ("kind", None, SEPrEventInvalidKind),
            ("detail", "x", SEPrEventInvalidDetail),
            ("detail", None, SEPrEventInvalidDetail),
            ("detected_on", "2026-11-10", SEPrEventInvalidDetectedOn),
            ("detected_on", None, SEPrEventInvalidDetectedOn),
            ("acked_on", "later", SEPrEventInvalidAckedOn),
            ("acked_on", 1, SEPrEventInvalidAckedOn),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            PrEvent(**{**self.FULL, name: value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            PrEvent(**self.FULL, surprise=1)

    def test_round_trip(self) -> None:
        model = PrEvent(**self.FULL)
        assert PrEvent.model_validate_json(model.model_dump_json()) == model
