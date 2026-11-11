from __future__ import annotations

from typing import ClassVar, Dict

import pytest
from pydantic import JsonValue, ValidationError

from pr_watch.models.watch.exceptions import (
    SETicketWatchInvalidHistory,
    SETicketWatchInvalidKey,
    SETicketWatchInvalidPullRequest,
    SETicketWatchInvalidSession,
)
from pr_watch.models.watch.ticket_watch import TicketWatch


class TestTicketWatch:
    REQUIRED: ClassVar[Dict[str, JsonValue]] = {
        "key": "GH-12",
        "pull_request": {"repository": "gpbcom/simple-erp", "number": 7, "root": "/home/me/simple-erp"},
        "history": {"status": "open", "registered_on": "2026-11-10T09:00:00+01:00"},
    }
    FULL: ClassVar[Dict[str, JsonValue]] = {
        "key": "GH-12",
        "pull_request": {"repository": "gpbcom/simple-erp", "number": 7, "root": "/home/me/simple-erp"},
        "session": {"session_id": "7a30c2c8-75fe-4e6a-8475-dc3d38910314", "cwd": "/home/me/simple-erp"},
        "history": {"status": "open", "registered_on": "2026-11-10T09:00:00+01:00"},
    }

    def test_defaults(self) -> None:
        model = TicketWatch(**self.REQUIRED)
        assert model.session == TicketWatch.model_fields["session"].get_default(call_default_factory=True)

    def test_full_valid_construction(self) -> None:
        model = TicketWatch(**self.FULL)
        assert model.id == "GH-12:gpbcom/simple-erp#7"
        assert model.is_open

    @pytest.mark.parametrize("name", ["session"])
    def test_none_becomes_the_default(self, name: str) -> None:
        model = TicketWatch(**{**self.FULL, name: None})
        assert getattr(model, name) == TicketWatch.model_fields[name].get_default(call_default_factory=True)

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("key", "ARE-1", SETicketWatchInvalidKey),
            ("key", None, SETicketWatchInvalidKey),
            ("pull_request", "gpbcom/simple-erp#7", SETicketWatchInvalidPullRequest),
            ("pull_request", None, SETicketWatchInvalidPullRequest),
            ("session", "7a30c2c8", SETicketWatchInvalidSession),
            ("session", 1, SETicketWatchInvalidSession),
            ("history", [], SETicketWatchInvalidHistory),
            ("history", None, SETicketWatchInvalidHistory),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            TicketWatch(**{**self.FULL, name: value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            TicketWatch(**self.FULL, surprise=1)

    def test_round_trip(self) -> None:
        model = TicketWatch(**self.FULL)
        assert TicketWatch.model_validate_json(model.model_dump_json()) == model
