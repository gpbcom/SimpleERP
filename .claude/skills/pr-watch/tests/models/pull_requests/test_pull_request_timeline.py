from __future__ import annotations

from typing import ClassVar, Dict

import pytest
from pydantic import JsonValue, ValidationError

from pr_watch.models.pull_requests.exceptions import (
    SEPullRequestTimelineInvalidClosedOn,
    SEPullRequestTimelineInvalidMergeCommit,
    SEPullRequestTimelineInvalidOpenedOn,
)
from pr_watch.models.pull_requests.pull_request_timeline import PullRequestTimeline


class TestPullRequestTimeline:
    REQUIRED: ClassVar[Dict[str, JsonValue]] = {"opened_on": "2026-11-09T17:00:00+01:00"}
    FULL: ClassVar[Dict[str, JsonValue]] = {
        "opened_on": "2026-11-09T17:00:00+01:00",
        "closed_on": "2026-11-11T10:00:00+01:00",
        "merge_commit": "9f1c2b3a",
    }

    def test_defaults(self) -> None:
        model = PullRequestTimeline(**self.REQUIRED)
        assert model.closed_on == PullRequestTimeline.model_fields["closed_on"].get_default(call_default_factory=True)
        assert model.merge_commit == PullRequestTimeline.model_fields["merge_commit"].get_default(
            call_default_factory=True
        )

    def test_full_valid_construction(self) -> None:
        model = PullRequestTimeline(**self.FULL)
        assert model.merge_commit == "9f1c2b3a"

    @pytest.mark.parametrize("name", ["closed_on", "merge_commit"])
    def test_none_becomes_the_default(self, name: str) -> None:
        model = PullRequestTimeline(**{**self.FULL, name: None})
        assert getattr(model, name) == PullRequestTimeline.model_fields[name].get_default(call_default_factory=True)

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("opened_on", "x", SEPullRequestTimelineInvalidOpenedOn),
            ("opened_on", None, SEPullRequestTimelineInvalidOpenedOn),
            ("closed_on", "2026", SEPullRequestTimelineInvalidClosedOn),
            ("closed_on", 1, SEPullRequestTimelineInvalidClosedOn),
            ("merge_commit", "", SEPullRequestTimelineInvalidMergeCommit),
            ("merge_commit", 3, SEPullRequestTimelineInvalidMergeCommit),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            PullRequestTimeline(**{**self.FULL, name: value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            PullRequestTimeline(**self.FULL, surprise=1)

    def test_round_trip(self) -> None:
        model = PullRequestTimeline(**self.FULL)
        assert PullRequestTimeline.model_validate_json(model.model_dump_json()) == model
