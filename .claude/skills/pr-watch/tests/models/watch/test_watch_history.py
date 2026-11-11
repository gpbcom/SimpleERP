from __future__ import annotations

from typing import ClassVar, Dict

import pytest
from pydantic import JsonValue, ValidationError

from pr_watch.models.enums import PullRequestStatus
from pr_watch.models.watch.exceptions import (
    SEWatchHistoryInvalidClosedOn,
    SEWatchHistoryInvalidOpenedOn,
    SEWatchHistoryInvalidRegisteredOn,
    SEWatchHistoryInvalidStatus,
)
from pr_watch.models.watch.watch_history import WatchHistory


class TestWatchHistory:
    REQUIRED: ClassVar[Dict[str, JsonValue]] = {"registered_on": "2026-11-10T09:00:00+01:00"}
    FULL: ClassVar[Dict[str, JsonValue]] = {
        "status": "merged",
        "registered_on": "2026-11-10T09:00:00+01:00",
        "opened_on": "2026-11-09T17:00:00+01:00",
        "closed_on": "2026-11-11T10:00:00+01:00",
    }

    def test_defaults(self) -> None:
        model = WatchHistory(**self.REQUIRED)
        assert model.status == WatchHistory.model_fields["status"].get_default(call_default_factory=True)
        assert model.opened_on == WatchHistory.model_fields["opened_on"].get_default(call_default_factory=True)
        assert model.closed_on == WatchHistory.model_fields["closed_on"].get_default(call_default_factory=True)

    def test_full_valid_construction(self) -> None:
        model = WatchHistory(**self.FULL)
        assert model.status == PullRequestStatus.MERGED

    @pytest.mark.parametrize("name", ["status", "opened_on", "closed_on"])
    def test_none_becomes_the_default(self, name: str) -> None:
        model = WatchHistory(**{**self.FULL, name: None})
        assert getattr(model, name) == WatchHistory.model_fields[name].get_default(call_default_factory=True)

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("status", "declined", SEWatchHistoryInvalidStatus),
            ("status", 1, SEWatchHistoryInvalidStatus),
            ("registered_on", "2026-11-10T09:00:00", SEWatchHistoryInvalidRegisteredOn),
            ("registered_on", "soon", SEWatchHistoryInvalidRegisteredOn),
            ("registered_on", None, SEWatchHistoryInvalidRegisteredOn),
            ("opened_on", "x", SEWatchHistoryInvalidOpenedOn),
            ("opened_on", 3, SEWatchHistoryInvalidOpenedOn),
            ("closed_on", "2026-11-11", SEWatchHistoryInvalidClosedOn),
            ("closed_on", [], SEWatchHistoryInvalidClosedOn),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            WatchHistory(**{**self.FULL, name: value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            WatchHistory(**self.FULL, surprise=1)

    def test_round_trip(self) -> None:
        model = WatchHistory(**self.FULL)
        assert WatchHistory.model_validate_json(model.model_dump_json()) == model
