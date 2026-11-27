from __future__ import annotations

from datetime import UTC, datetime, timedelta, timezone
from typing import Dict

import pytest
from erp_models.base.frozen_erp_model import FrozenErpModel
from erp_models.times.exceptions import SEInvalidUtcTimestampException, SEUtcTimestampInvalidInstant
from erp_models.times.utc_timestamp import UtcTimestamp
from pydantic import JsonValue, ValidationError


class TestUtcTimestamp:
    def test_defaults(self) -> None:
        with pytest.raises(ValidationError):
            UtcTimestamp.model_validate({})

    def test_full_valid_construction(self) -> None:
        stamp = UtcTimestamp(instant=datetime(2026, 12, 7, 9, 0, tzinfo=UTC))
        assert stamp.instant == datetime(2026, 12, 7, 9, 0, tzinfo=UTC)
        assert issubclass(UtcTimestamp, FrozenErpModel)

    def test_none_becomes_the_default(self) -> None:
        with pytest.raises(SEUtcTimestampInvalidInstant):
            UtcTimestamp.model_validate({"instant": None})

    @pytest.mark.parametrize(
        "value",
        [
            datetime(2026, 12, 7, 9, 0),
            "2026-12-07T09:00:00",
            "2026-12-07",
            "not a date",
            "",
            "   ",
            True,
            False,
            1796634000,
            1796634000.5,
            [],
            {},
            b"2026-12-07T09:00:00Z",
        ],
    )
    def test_rejects_bad_values(self, value: object) -> None:
        with pytest.raises(SEUtcTimestampInvalidInstant):
            UtcTimestamp.model_validate({"instant": value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            UtcTimestamp.model_validate({"instant": "2026-12-07T09:00:00Z", "extra": 1})

    def test_round_trip(self) -> None:
        stamp = UtcTimestamp(instant=datetime(2026, 12, 7, 9, 0, 1, 500, tzinfo=UTC))
        dumped: Dict[str, JsonValue] = stamp.model_dump(mode="json")
        assert UtcTimestamp.model_validate(dumped) == stamp
        assert UtcTimestamp.model_validate_json(stamp.model_dump_json()) == stamp

    def test_an_offset_text_is_converted_to_utc(self) -> None:
        stamp = UtcTimestamp.model_validate({"instant": "2026-12-07T10:00:00+01:00"})
        assert stamp.instant == datetime(2026, 12, 7, 9, 0, tzinfo=UTC)
        assert stamp.instant.tzinfo is UTC
        assert stamp.instant.utcoffset() == timedelta(0)

    def test_a_text_ending_in_z_is_accepted(self) -> None:
        stamp = UtcTimestamp.model_validate({"instant": "2026-12-07T09:00:00Z"})
        assert stamp.instant == datetime(2026, 12, 7, 9, 0, tzinfo=UTC)

    def test_a_text_is_stripped_before_parsing(self) -> None:
        stamp = UtcTimestamp.model_validate({"instant": "  2026-12-07T09:00:00Z  "})
        assert stamp.instant == datetime(2026, 12, 7, 9, 0, tzinfo=UTC)

    def test_an_aware_datetime_is_converted_to_utc(self) -> None:
        paris = timezone(timedelta(hours=1))
        stamp = UtcTimestamp(instant=datetime(2026, 12, 7, 10, 0, tzinfo=paris))
        assert stamp.instant.tzinfo is UTC
        assert stamp.instant == datetime(2026, 12, 7, 9, 0, tzinfo=UTC)

    def test_now_is_aware_and_in_utc(self) -> None:
        before = datetime.now(UTC)
        stamp = UtcTimestamp.now()
        assert stamp.instant.tzinfo is UTC
        assert stamp.instant.utcoffset() == timedelta(0)
        assert abs(stamp.instant - before) < timedelta(seconds=5)

    def test_assignment_is_refused(self) -> None:
        stamp = UtcTimestamp.now()
        with pytest.raises(ValidationError):
            stamp.instant = datetime(2026, 1, 1, tzinfo=UTC)

    def test_equal_timestamps_hash_alike(self) -> None:
        first = UtcTimestamp.model_validate({"instant": "2026-12-07T10:00:00+01:00"})
        second = UtcTimestamp.model_validate({"instant": "2026-12-07T09:00:00Z"})
        assert first == second
        assert hash(first) == hash(second)

    def test_the_exception_belongs_to_the_model_family(self) -> None:
        assert issubclass(SEUtcTimestampInvalidInstant, SEInvalidUtcTimestampException)
        assert not issubclass(SEUtcTimestampInvalidInstant, ValueError)
