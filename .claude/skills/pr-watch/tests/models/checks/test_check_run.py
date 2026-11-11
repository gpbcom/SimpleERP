from __future__ import annotations

from typing import ClassVar, Dict

import pytest
from pydantic import JsonValue, ValidationError

from pr_watch.models.checks.check_run import CheckRun
from pr_watch.models.checks.exceptions import (
    SECheckRunInvalidConclusion,
    SECheckRunInvalidId,
    SECheckRunInvalidLink,
    SECheckRunInvalidName,
    SECheckRunInvalidSuiteId,
)


class TestCheckRun:
    REQUIRED: ClassVar[Dict[str, JsonValue]] = {"id": 501, "name": "unit"}
    FULL: ClassVar[Dict[str, JsonValue]] = {
        "id": 501,
        "name": "unit",
        "conclusion": "failure",
        "link": "https://github.com/gpbcom/simple-erp/runs/501",
        "suite_id": 77,
    }

    def test_defaults(self) -> None:
        model = CheckRun(**self.REQUIRED)
        assert model.conclusion == CheckRun.model_fields["conclusion"].get_default(call_default_factory=True)
        assert model.link == CheckRun.model_fields["link"].get_default(call_default_factory=True)
        assert model.suite_id == CheckRun.model_fields["suite_id"].get_default(call_default_factory=True)

    def test_full_valid_construction(self) -> None:
        model = CheckRun(**self.FULL)
        assert model.conclusion == "failure"

    @pytest.mark.parametrize("name", ["conclusion", "link", "suite_id"])
    def test_none_becomes_the_default(self, name: str) -> None:
        model = CheckRun(**{**self.FULL, name: None})
        assert getattr(model, name) == CheckRun.model_fields[name].get_default(call_default_factory=True)

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("id", 0, SECheckRunInvalidId),
            ("id", None, SECheckRunInvalidId),
            ("name", "", SECheckRunInvalidName),
            ("name", None, SECheckRunInvalidName),
            ("conclusion", "FAILED", SECheckRunInvalidConclusion),
            ("conclusion", 1, SECheckRunInvalidConclusion),
            ("link", "runs/501", SECheckRunInvalidLink),
            ("link", 1, SECheckRunInvalidLink),
            ("suite_id", 0, SECheckRunInvalidSuiteId),
            ("suite_id", "77", SECheckRunInvalidSuiteId),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            CheckRun(**{**self.FULL, name: value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            CheckRun(**self.FULL, surprise=1)

    def test_round_trip(self) -> None:
        model = CheckRun(**self.FULL)
        assert CheckRun.model_validate_json(model.model_dump_json()) == model
