from __future__ import annotations

from typing import Dict

import pytest
from pydantic import JsonValue

from ticket_docs.models.evidence.exceptions import SERunCountsInvalidCount
from ticket_docs.models.evidence.run_counts import RunCounts


class TestRunCounts:
    def test_defaults(self) -> None:
        counts = RunCounts()
        assert (counts.tests, counts.failures, counts.errors, counts.passed) == (0, 0, 0, 0)

    def test_full_valid_construction(self) -> None:
        counts = RunCounts(tests=12, failures=2, errors=1)
        assert counts.passed == 9

    @pytest.mark.parametrize("name", ["tests", "failures", "errors"])
    def test_none_becomes_the_default(self, name: str) -> None:
        assert getattr(RunCounts.model_validate({name: None}), name) == 0

    @pytest.mark.parametrize(("name", "value"), [("tests", -1), ("failures", True), ("errors", "2"), ("tests", 1.5)])
    def test_rejects_bad_values(self, name: str, value: JsonValue) -> None:
        fields: Dict[str, JsonValue] = {name: value}
        with pytest.raises(SERunCountsInvalidCount):
            RunCounts.model_validate(fields)

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValueError, match="extra"):
            RunCounts.model_validate({"skipped": 1})

    def test_round_trip(self) -> None:
        counts = RunCounts(tests=3, failures=1)
        assert RunCounts.model_validate(counts.model_dump()) == counts

    def test_passed_never_goes_below_zero(self) -> None:
        assert RunCounts(tests=1, failures=1, errors=1).passed == 0
