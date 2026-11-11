from __future__ import annotations

from typing import ClassVar, Dict

import pytest
from pydantic import JsonValue, ValidationError

from pr_watch.models.pull_requests.exceptions import (
    SEPullRequestStateInvalidAuthor,
    SEPullRequestStateInvalidBranches,
    SEPullRequestStateInvalidStatus,
    SEPullRequestStateInvalidTimeline,
    SEPullRequestStateInvalidTitle,
)
from pr_watch.models.pull_requests.pull_request_state import PullRequestState


class TestPullRequestState:
    REQUIRED: ClassVar[Dict[str, JsonValue]] = {
        "title": "[GH-12] Add customers",
        "status": "open",
        "author": "gpbcom",
        "branches": {
            "head_ref": "feature/GH-12-add-customers",
            "head_sha": "668501e0d3a1b2c3d4e5f60718293a4b5c6d7e8f",
            "base_ref": "develop",
        },
        "timeline": {"opened_on": "2026-11-09T17:00:00+01:00"},
    }
    FULL: ClassVar[Dict[str, JsonValue]] = {
        "title": "[GH-12] Add customers",
        "status": "open",
        "author": "gpbcom",
        "branches": {
            "head_ref": "feature/GH-12-add-customers",
            "head_sha": "668501e0d3a1b2c3d4e5f60718293a4b5c6d7e8f",
            "base_ref": "develop",
        },
        "timeline": {"opened_on": "2026-11-09T17:00:00+01:00"},
    }

    def test_defaults(self) -> None:
        model = PullRequestState(**self.REQUIRED)
        assert PullRequestState.model_validate(model.model_dump()) == model

    def test_full_valid_construction(self) -> None:
        model = PullRequestState(**self.FULL)
        assert model.branches.base_ref == "develop"

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("title", "", SEPullRequestStateInvalidTitle),
            ("title", None, SEPullRequestStateInvalidTitle),
            ("status", "OPEN", SEPullRequestStateInvalidStatus),
            ("status", None, SEPullRequestStateInvalidStatus),
            ("author", "", SEPullRequestStateInvalidAuthor),
            ("author", 1, SEPullRequestStateInvalidAuthor),
            ("branches", "develop", SEPullRequestStateInvalidBranches),
            ("branches", None, SEPullRequestStateInvalidBranches),
            ("timeline", 1, SEPullRequestStateInvalidTimeline),
            ("timeline", None, SEPullRequestStateInvalidTimeline),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            PullRequestState(**{**self.FULL, name: value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            PullRequestState(**self.FULL, surprise=1)

    def test_round_trip(self) -> None:
        model = PullRequestState(**self.FULL)
        assert PullRequestState.model_validate_json(model.model_dump_json()) == model
