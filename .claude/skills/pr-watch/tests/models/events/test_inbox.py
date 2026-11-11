from __future__ import annotations

from typing import ClassVar, Dict

import pytest
from pydantic import JsonValue, ValidationError

from pr_watch.models.events.exceptions import (
    SEInboxInvalidEvents,
)
from pr_watch.models.events.inbox import Inbox


class TestInbox:
    REQUIRED: ClassVar[Dict[str, JsonValue]] = {}
    FULL: ClassVar[Dict[str, JsonValue]] = {"events": []}

    def test_defaults(self) -> None:
        model = Inbox(**self.REQUIRED)
        assert model.events == Inbox.model_fields["events"].get_default(call_default_factory=True)

    def test_full_valid_construction(self) -> None:
        model = Inbox(**self.FULL)
        assert model.pending == []

    @pytest.mark.parametrize("name", ["events"])
    def test_none_becomes_the_default(self, name: str) -> None:
        model = Inbox(**{**self.FULL, name: None})
        assert getattr(model, name) == Inbox.model_fields[name].get_default(call_default_factory=True)

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("events", {}, SEInboxInvalidEvents),
            ("events", "x", SEInboxInvalidEvents),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            Inbox(**{**self.FULL, name: value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            Inbox(**self.FULL, surprise=1)

    def test_round_trip(self) -> None:
        model = Inbox(**self.FULL)
        assert Inbox.model_validate_json(model.model_dump_json()) == model
