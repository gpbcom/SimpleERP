from __future__ import annotations

from typing import ClassVar, Dict

import pytest
from pydantic import JsonValue, ValidationError

from pr_watch.models.state.exceptions import (
    SEUnwatchedPullRequestInvalidNumber,
    SEUnwatchedPullRequestInvalidRepository,
    SEUnwatchedPullRequestInvalidTicket,
    SEUnwatchedPullRequestInvalidTitle,
    SEUnwatchedPullRequestInvalidUpdatedOn,
)
from pr_watch.models.state.unwatched_pull_request import UnwatchedPullRequest


class TestUnwatchedPullRequest:
    REQUIRED: ClassVar[Dict[str, JsonValue]] = {
        "repository": "gpbcom/simple-erp",
        "number": 8,
        "title": "[GH-13] Add invoices",
        "updated_on": "2026-11-10T08:00:00+01:00",
    }
    FULL: ClassVar[Dict[str, JsonValue]] = {
        "repository": "gpbcom/simple-erp",
        "number": 8,
        "title": "[GH-13] Add invoices",
        "ticket": "GH-13",
        "updated_on": "2026-11-10T08:00:00+01:00",
    }

    def test_defaults(self) -> None:
        model = UnwatchedPullRequest(**self.REQUIRED)
        assert model.ticket == UnwatchedPullRequest.model_fields["ticket"].get_default(call_default_factory=True)

    def test_full_valid_construction(self) -> None:
        model = UnwatchedPullRequest(**self.FULL)
        assert model.url == "https://github.com/gpbcom/simple-erp/pull/8"

    @pytest.mark.parametrize("name", ["ticket"])
    def test_none_becomes_the_default(self, name: str) -> None:
        model = UnwatchedPullRequest(**{**self.FULL, name: None})
        assert getattr(model, name) == UnwatchedPullRequest.model_fields[name].get_default(call_default_factory=True)

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("repository", "x", SEUnwatchedPullRequestInvalidRepository),
            ("repository", None, SEUnwatchedPullRequestInvalidRepository),
            ("number", 0, SEUnwatchedPullRequestInvalidNumber),
            ("number", None, SEUnwatchedPullRequestInvalidNumber),
            ("title", "", SEUnwatchedPullRequestInvalidTitle),
            ("title", None, SEUnwatchedPullRequestInvalidTitle),
            ("ticket", "13", SEUnwatchedPullRequestInvalidTicket),
            ("ticket", 1, SEUnwatchedPullRequestInvalidTicket),
            ("updated_on", "x", SEUnwatchedPullRequestInvalidUpdatedOn),
            ("updated_on", None, SEUnwatchedPullRequestInvalidUpdatedOn),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            UnwatchedPullRequest(**{**self.FULL, name: value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            UnwatchedPullRequest(**self.FULL, surprise=1)

    def test_round_trip(self) -> None:
        model = UnwatchedPullRequest(**self.FULL)
        assert UnwatchedPullRequest.model_validate_json(model.model_dump_json()) == model
