from __future__ import annotations

from typing import ClassVar, Dict

import pytest
from pydantic import JsonValue, ValidationError

from pr_watch.models.state.ci_summary import CiSummary
from pr_watch.models.state.exceptions import (
    SECiSummaryInvalidChecks,
    SECiSummaryInvalidChecksLink,
    SECiSummaryInvalidReview,
    SECiSummaryInvalidStages,
)


class TestCiSummary:
    REQUIRED: ClassVar[Dict[str, JsonValue]] = {}
    FULL: ClassVar[Dict[str, JsonValue]] = {
        "checks": "failed",
        "checks_link": "https://github.com/gpbcom/simple-erp/runs/501",
        "stages": [{"environment": "dev", "deployment_id": 701, "state": "success"}],
        "review": "APPROVED",
    }

    def test_defaults(self) -> None:
        model = CiSummary(**self.REQUIRED)
        assert model.checks == CiSummary.model_fields["checks"].get_default(call_default_factory=True)
        assert model.checks_link == CiSummary.model_fields["checks_link"].get_default(call_default_factory=True)
        assert model.stages == CiSummary.model_fields["stages"].get_default(call_default_factory=True)
        assert model.review == CiSummary.model_fields["review"].get_default(call_default_factory=True)

    def test_full_valid_construction(self) -> None:
        model = CiSummary(**self.FULL)
        assert model.stages[0].environment == "dev"

    @pytest.mark.parametrize("name", ["checks", "checks_link", "stages", "review"])
    def test_none_becomes_the_default(self, name: str) -> None:
        model = CiSummary(**{**self.FULL, name: None})
        assert getattr(model, name) == CiSummary.model_fields[name].get_default(call_default_factory=True)

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("checks", "red", SECiSummaryInvalidChecks),
            ("checks", 1, SECiSummaryInvalidChecks),
            ("checks_link", "runs", SECiSummaryInvalidChecksLink),
            ("checks_link", 1, SECiSummaryInvalidChecksLink),
            ("stages", {}, SECiSummaryInvalidStages),
            ("stages", "dev", SECiSummaryInvalidStages),
            ("review", "ok", SECiSummaryInvalidReview),
            ("review", 1, SECiSummaryInvalidReview),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            CiSummary(**{**self.FULL, name: value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            CiSummary(**self.FULL, surprise=1)

    def test_round_trip(self) -> None:
        model = CiSummary(**self.FULL)
        assert CiSummary.model_validate_json(model.model_dump_json()) == model
