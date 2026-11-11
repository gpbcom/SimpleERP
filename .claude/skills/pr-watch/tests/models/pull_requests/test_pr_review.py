from __future__ import annotations

from typing import ClassVar, Dict

import pytest
from pydantic import JsonValue, ValidationError

from pr_watch.models.pull_requests.exceptions import (
    SEPrReviewInvalidAuthor,
    SEPrReviewInvalidBody,
    SEPrReviewInvalidId,
    SEPrReviewInvalidLink,
    SEPrReviewInvalidState,
)
from pr_watch.models.pull_requests.pr_review import PrReview


class TestPrReview:
    REQUIRED: ClassVar[Dict[str, JsonValue]] = {
        "id": 301,
        "state": "CHANGES_REQUESTED",
        "author": "octocat",
        "link": "https://github.com/gpbcom/simple-erp/pull/7#pullrequestreview-301",
    }
    FULL: ClassVar[Dict[str, JsonValue]] = {
        "id": 301,
        "state": "CHANGES_REQUESTED",
        "author": "octocat",
        "body": "Please split this method.",
        "link": "https://github.com/gpbcom/simple-erp/pull/7#pullrequestreview-301",
    }

    def test_defaults(self) -> None:
        model = PrReview(**self.REQUIRED)
        assert model.body == PrReview.model_fields["body"].get_default(call_default_factory=True)

    def test_full_valid_construction(self) -> None:
        model = PrReview(**self.FULL)
        assert model.state == "CHANGES_REQUESTED"

    @pytest.mark.parametrize("name", ["body"])
    def test_none_becomes_the_default(self, name: str) -> None:
        model = PrReview(**{**self.FULL, name: None})
        assert getattr(model, name) == PrReview.model_fields[name].get_default(call_default_factory=True)

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("id", 0, SEPrReviewInvalidId),
            ("id", None, SEPrReviewInvalidId),
            ("state", "changes_requested", SEPrReviewInvalidState),
            ("state", None, SEPrReviewInvalidState),
            ("author", "", SEPrReviewInvalidAuthor),
            ("author", None, SEPrReviewInvalidAuthor),
            ("body", 1, SEPrReviewInvalidBody),
            ("body", [], SEPrReviewInvalidBody),
            ("link", "#301", SEPrReviewInvalidLink),
            ("link", None, SEPrReviewInvalidLink),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            PrReview(**{**self.FULL, name: value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            PrReview(**self.FULL, surprise=1)

    def test_round_trip(self) -> None:
        model = PrReview(**self.FULL)
        assert PrReview.model_validate_json(model.model_dump_json()) == model
