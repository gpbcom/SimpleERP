from __future__ import annotations

from typing import ClassVar, Dict

import pytest
from pydantic import JsonValue, ValidationError

from pr_watch.models.events.event_detail import EventDetail
from pr_watch.models.events.exceptions import (
    SEEventDetailInvalidExcerpt,
    SEEventDetailInvalidLink,
    SEEventDetailInvalidTitle,
)


class TestEventDetail:
    REQUIRED: ClassVar[Dict[str, JsonValue]] = {"title": "2 checks failed on 668501e0"}
    FULL: ClassVar[Dict[str, JsonValue]] = {
        "title": "2 checks failed on 668501e0",
        "link": "https://github.com/gpbcom/simple-erp/actions/runs/1",
        "excerpt": "ci / unit: failure",
    }

    def test_defaults(self) -> None:
        model = EventDetail(**self.REQUIRED)
        assert model.link == EventDetail.model_fields["link"].get_default(call_default_factory=True)
        assert model.excerpt == EventDetail.model_fields["excerpt"].get_default(call_default_factory=True)

    def test_full_valid_construction(self) -> None:
        model = EventDetail(**self.FULL)
        assert model.title.startswith("2 checks")

    @pytest.mark.parametrize("name", ["link", "excerpt"])
    def test_none_becomes_the_default(self, name: str) -> None:
        model = EventDetail(**{**self.FULL, name: None})
        assert getattr(model, name) == EventDetail.model_fields[name].get_default(call_default_factory=True)

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("title", "", SEEventDetailInvalidTitle),
            ("title", None, SEEventDetailInvalidTitle),
            ("link", "runs/1", SEEventDetailInvalidLink),
            ("link", 3, SEEventDetailInvalidLink),
            ("excerpt", 7, SEEventDetailInvalidExcerpt),
            ("excerpt", [], SEEventDetailInvalidExcerpt),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            EventDetail(**{**self.FULL, name: value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            EventDetail(**self.FULL, surprise=1)

    def test_round_trip(self) -> None:
        model = EventDetail(**self.FULL)
        assert EventDetail.model_validate_json(model.model_dump_json()) == model
