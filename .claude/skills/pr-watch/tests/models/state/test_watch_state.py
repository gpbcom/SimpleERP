from __future__ import annotations

from typing import ClassVar, Dict

import pytest
from pydantic import JsonValue, ValidationError

from pr_watch.models.state.exceptions import (
    SEWatchStateInvalidCursors,
    SEWatchStateInvalidDelivery,
    SEWatchStateInvalidLastChecked,
    SEWatchStateInvalidSnapshots,
    SEWatchStateInvalidUnwatched,
)
from pr_watch.models.state.watch_state import WatchState


class TestWatchState:
    REQUIRED: ClassVar[Dict[str, JsonValue]] = {}
    FULL: ClassVar[Dict[str, JsonValue]] = {
        "last_checked": "2026-11-10T09:10:00+01:00",
        "delivery": {"notified": {"GH-12": "2026-11-10T09:10:00+01:00"}},
        "cursors": {"GH-12:gpbcom/simple-erp#7|inline": 9001},
        "snapshots": {},
        "unwatched": {},
    }

    def test_defaults(self) -> None:
        model = WatchState(**self.REQUIRED)
        assert model.last_checked == WatchState.model_fields["last_checked"].get_default(call_default_factory=True)
        assert model.delivery == WatchState.model_fields["delivery"].get_default(call_default_factory=True)
        assert model.cursors == WatchState.model_fields["cursors"].get_default(call_default_factory=True)
        assert model.snapshots == WatchState.model_fields["snapshots"].get_default(call_default_factory=True)
        assert model.unwatched == WatchState.model_fields["unwatched"].get_default(call_default_factory=True)

    def test_full_valid_construction(self) -> None:
        model = WatchState(**self.FULL)
        assert model.cursors == {"GH-12:gpbcom/simple-erp#7|inline": 9001}

    @pytest.mark.parametrize("name", ["last_checked", "delivery", "cursors", "snapshots", "unwatched"])
    def test_none_becomes_the_default(self, name: str) -> None:
        model = WatchState(**{**self.FULL, name: None})
        assert getattr(model, name) == WatchState.model_fields[name].get_default(call_default_factory=True)

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("last_checked", "x", SEWatchStateInvalidLastChecked),
            ("last_checked", 1, SEWatchStateInvalidLastChecked),
            ("delivery", [], SEWatchStateInvalidDelivery),
            ("delivery", "x", SEWatchStateInvalidDelivery),
            ("cursors", [], SEWatchStateInvalidCursors),
            ("cursors", 1, SEWatchStateInvalidCursors),
            ("snapshots", [], SEWatchStateInvalidSnapshots),
            ("snapshots", "x", SEWatchStateInvalidSnapshots),
            ("unwatched", [], SEWatchStateInvalidUnwatched),
            ("unwatched", 1, SEWatchStateInvalidUnwatched),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            WatchState(**{**self.FULL, name: value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            WatchState(**self.FULL, surprise=1)

    def test_round_trip(self) -> None:
        model = WatchState(**self.FULL)
        assert WatchState.model_validate_json(model.model_dump_json()) == model
