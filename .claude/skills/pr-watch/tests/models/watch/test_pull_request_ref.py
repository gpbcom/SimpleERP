from __future__ import annotations

from typing import ClassVar, Dict

import pytest
from pydantic import JsonValue, ValidationError

from pr_watch.models.watch.exceptions import (
    SEPullRequestRefInvalidNumber,
    SEPullRequestRefInvalidRepository,
    SEPullRequestRefInvalidRoot,
)
from pr_watch.models.watch.pull_request_ref import PullRequestRef


class TestPullRequestRef:
    REQUIRED: ClassVar[Dict[str, JsonValue]] = {
        "repository": "gpbcom/simple-erp",
        "number": 7,
        "root": "/home/me/simple-erp",
    }
    FULL: ClassVar[Dict[str, JsonValue]] = {
        "repository": "gpbcom/simple-erp",
        "number": 7,
        "root": "/home/me/simple-erp",
    }

    def test_defaults(self) -> None:
        model = PullRequestRef(**self.REQUIRED)
        assert PullRequestRef.model_validate(model.model_dump()) == model

    def test_full_valid_construction(self) -> None:
        model = PullRequestRef(**self.FULL)
        assert model.url == "https://github.com/gpbcom/simple-erp/pull/7"
        assert model.label == "gpbcom/simple-erp#7"

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("repository", "simple-erp", SEPullRequestRefInvalidRepository),
            ("repository", None, SEPullRequestRefInvalidRepository),
            ("number", 0, SEPullRequestRefInvalidNumber),
            ("number", "7", SEPullRequestRefInvalidNumber),
            ("number", True, SEPullRequestRefInvalidNumber),
            ("root", "", SEPullRequestRefInvalidRoot),
            ("root", 3, SEPullRequestRefInvalidRoot),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            PullRequestRef(**{**self.FULL, name: value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            PullRequestRef(**self.FULL, surprise=1)

    def test_round_trip(self) -> None:
        model = PullRequestRef(**self.FULL)
        assert PullRequestRef.model_validate_json(model.model_dump_json()) == model
