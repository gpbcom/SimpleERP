from __future__ import annotations

from typing import ClassVar, Dict

import pytest
from pydantic import JsonValue, ValidationError

from pr_watch.models.configuration.exceptions import (
    SETimingConfigInvalidIntervalMinutes,
    SETimingConfigInvalidOperationsShown,
    SETimingConfigInvalidQaWaitMinutes,
    SETimingConfigInvalidRenotifyMinutes,
)
from pr_watch.models.configuration.timing_config import TimingConfig


class TestTimingConfig:
    REQUIRED: ClassVar[Dict[str, JsonValue]] = {
        "interval_minutes": 10,
        "renotify_minutes": 60,
        "qa_wait_minutes": 30,
        "operations_shown": 60,
    }
    FULL: ClassVar[Dict[str, JsonValue]] = {
        "interval_minutes": 10,
        "renotify_minutes": 60,
        "qa_wait_minutes": 30,
        "operations_shown": 60,
    }

    def test_defaults(self) -> None:
        model = TimingConfig(**self.REQUIRED)
        assert TimingConfig.model_validate(model.model_dump()) == model

    def test_full_valid_construction(self) -> None:
        model = TimingConfig(**self.FULL)
        assert model.qa_wait_minutes == 30

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("interval_minutes", 0, SETimingConfigInvalidIntervalMinutes),
            ("interval_minutes", True, SETimingConfigInvalidIntervalMinutes),
            ("interval_minutes", "10", SETimingConfigInvalidIntervalMinutes),
            ("renotify_minutes", -1, SETimingConfigInvalidRenotifyMinutes),
            ("renotify_minutes", None, SETimingConfigInvalidRenotifyMinutes),
            ("qa_wait_minutes", 0, SETimingConfigInvalidQaWaitMinutes),
            ("qa_wait_minutes", 2.5, SETimingConfigInvalidQaWaitMinutes),
            ("operations_shown", 0, SETimingConfigInvalidOperationsShown),
            ("operations_shown", "x", SETimingConfigInvalidOperationsShown),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            TimingConfig(**{**self.FULL, name: value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            TimingConfig(**self.FULL, surprise=1)

    def test_round_trip(self) -> None:
        model = TimingConfig(**self.FULL)
        assert TimingConfig.model_validate_json(model.model_dump_json()) == model
