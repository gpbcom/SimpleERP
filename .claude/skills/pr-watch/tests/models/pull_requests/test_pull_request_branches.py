from __future__ import annotations

from typing import ClassVar, Dict

import pytest
from pydantic import JsonValue, ValidationError

from pr_watch.models.pull_requests.exceptions import (
    SEPullRequestBranchesInvalidBaseRef,
    SEPullRequestBranchesInvalidHeadRef,
    SEPullRequestBranchesInvalidHeadSha,
    SEPullRequestBranchesInvalidMergeable,
)
from pr_watch.models.pull_requests.pull_request_branches import PullRequestBranches


class TestPullRequestBranches:
    REQUIRED: ClassVar[Dict[str, JsonValue]] = {
        "head_ref": "feature/GH-12-add-customers",
        "head_sha": "668501e0d3a1b2c3d4e5f60718293a4b5c6d7e8f",
        "base_ref": "develop",
    }
    FULL: ClassVar[Dict[str, JsonValue]] = {
        "head_ref": "feature/GH-12-add-customers",
        "head_sha": "668501e0d3a1b2c3d4e5f60718293a4b5c6d7e8f",
        "base_ref": "develop",
        "mergeable": "dirty",
    }

    def test_defaults(self) -> None:
        model = PullRequestBranches(**self.REQUIRED)
        assert model.mergeable == PullRequestBranches.model_fields["mergeable"].get_default(call_default_factory=True)

    def test_full_valid_construction(self) -> None:
        model = PullRequestBranches(**self.FULL)
        assert model.mergeable == "dirty"

    @pytest.mark.parametrize("name", ["mergeable"])
    def test_none_becomes_the_default(self, name: str) -> None:
        model = PullRequestBranches(**{**self.FULL, name: None})
        assert getattr(model, name) == PullRequestBranches.model_fields[name].get_default(call_default_factory=True)

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("head_ref", "", SEPullRequestBranchesInvalidHeadRef),
            ("head_ref", None, SEPullRequestBranchesInvalidHeadRef),
            ("head_sha", "", SEPullRequestBranchesInvalidHeadSha),
            ("head_sha", 1, SEPullRequestBranchesInvalidHeadSha),
            ("base_ref", " ", SEPullRequestBranchesInvalidBaseRef),
            ("base_ref", None, SEPullRequestBranchesInvalidBaseRef),
            ("mergeable", "conflict", SEPullRequestBranchesInvalidMergeable),
            ("mergeable", 2, SEPullRequestBranchesInvalidMergeable),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            PullRequestBranches(**{**self.FULL, name: value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            PullRequestBranches(**self.FULL, surprise=1)

    def test_round_trip(self) -> None:
        model = PullRequestBranches(**self.FULL)
        assert PullRequestBranches.model_validate_json(model.model_dump_json()) == model
