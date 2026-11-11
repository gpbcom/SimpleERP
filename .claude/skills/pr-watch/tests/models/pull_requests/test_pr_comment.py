from __future__ import annotations

from typing import ClassVar, Dict

import pytest
from pydantic import JsonValue, ValidationError

from pr_watch.models.pull_requests.exceptions import (
    SEPrCommentInvalidAuthor,
    SEPrCommentInvalidBody,
    SEPrCommentInvalidId,
    SEPrCommentInvalidLink,
    SEPrCommentInvalidSource,
)
from pr_watch.models.pull_requests.pr_comment import PrComment


class TestPrComment:
    REQUIRED: ClassVar[Dict[str, JsonValue]] = {
        "id": 9001,
        "source": "inline",
        "author": "octocat",
        "body": "This name is misleading.",
        "link": "https://github.com/gpbcom/simple-erp/pull/7#discussion_r9001",
    }
    FULL: ClassVar[Dict[str, JsonValue]] = {
        "id": 9001,
        "source": "inline",
        "author": "octocat",
        "body": "This name is misleading.",
        "link": "https://github.com/gpbcom/simple-erp/pull/7#discussion_r9001",
    }

    def test_defaults(self) -> None:
        model = PrComment(**self.REQUIRED)
        assert PrComment.model_validate(model.model_dump()) == model

    def test_full_valid_construction(self) -> None:
        model = PrComment(**self.FULL)
        assert model.source == "inline"

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("id", -1, SEPrCommentInvalidId),
            ("id", None, SEPrCommentInvalidId),
            ("source", "diff", SEPrCommentInvalidSource),
            ("source", None, SEPrCommentInvalidSource),
            ("author", "", SEPrCommentInvalidAuthor),
            ("author", None, SEPrCommentInvalidAuthor),
            ("body", 1, SEPrCommentInvalidBody),
            ("body", None, SEPrCommentInvalidBody),
            ("link", "r9001", SEPrCommentInvalidLink),
            ("link", None, SEPrCommentInvalidLink),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            PrComment(**{**self.FULL, name: value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            PrComment(**self.FULL, surprise=1)

    def test_round_trip(self) -> None:
        model = PrComment(**self.FULL)
        assert PrComment.model_validate_json(model.model_dump_json()) == model
