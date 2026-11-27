from __future__ import annotations

from typing import Dict, Type

import pytest
from erp_testing.models.stand_in.exceptions import (
    SEStandInAnswerInvalidBody,
    SEStandInAnswerInvalidHeaders,
    SEStandInAnswerInvalidStatus,
)
from erp_testing.models.stand_in.stand_in_answer import StandInAnswer
from pydantic import JsonValue, ValidationError


class TestStandInAnswer:
    def test_defaults(self) -> None:
        answer = StandInAnswer()
        assert answer.status == 200
        assert answer.body is None
        assert answer.headers == {}

    def test_full_valid_construction(self) -> None:
        answer = StandInAnswer(status=201, body={"id": 1, "tags": ["a"]}, headers={"X-Id": "1"})
        assert answer.status == 201
        assert answer.body == {"id": 1, "tags": ["a"]}
        assert answer.headers == {"X-Id": "1"}

    @pytest.mark.parametrize(("name", "expected"), [("status", 200), ("body", None), ("headers", {})])
    def test_none_becomes_the_default(self, name: str, expected: JsonValue) -> None:
        answer = StandInAnswer.model_validate({name: None})
        assert getattr(answer, name) == expected

    @pytest.mark.parametrize("status", [StandInAnswer.STATUS_MIN, StandInAnswer.STATUS_MAX])
    def test_the_status_bounds_are_accepted(self, status: int) -> None:
        assert StandInAnswer(status=status).status == status

    def test_the_status_bounds_are_the_http_ones(self) -> None:
        assert StandInAnswer.STATUS_MIN == 100
        assert StandInAnswer.STATUS_MAX == 599

    @pytest.mark.parametrize(
        ("field", "value", "error"),
        [
            ("status", 99, SEStandInAnswerInvalidStatus),
            ("status", 600, SEStandInAnswerInvalidStatus),
            ("status", -1, SEStandInAnswerInvalidStatus),
            ("status", True, SEStandInAnswerInvalidStatus),
            ("status", "200", SEStandInAnswerInvalidStatus),
            ("status", 200.5, SEStandInAnswerInvalidStatus),
            ("body", object(), SEStandInAnswerInvalidBody),
            ("body", {1, 2}, SEStandInAnswerInvalidBody),
            ("body", b"raw", SEStandInAnswerInvalidBody),
            ("body", {"a": object()}, SEStandInAnswerInvalidBody),
            ("headers", "X: 1", SEStandInAnswerInvalidHeaders),
            ("headers", ["X"], SEStandInAnswerInvalidHeaders),
            ("headers", {"X": 1}, SEStandInAnswerInvalidHeaders),
            ("headers", {1: "a"}, SEStandInAnswerInvalidHeaders),
        ],
    )
    def test_rejects_bad_values(self, field: str, value: object, error: Type[Exception]) -> None:
        data: Dict[str, object] = {field: value}
        with pytest.raises(error):
            StandInAnswer.model_validate(data)

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            StandInAnswer.model_validate({"unknown": 1})

    def test_round_trip(self) -> None:
        answer = StandInAnswer(status=404, body={"detail": "missing"}, headers={"X-Id": "1"})
        assert StandInAnswer.model_validate(answer.model_dump()) == answer
        assert StandInAnswer.model_validate_json(answer.model_dump_json()) == answer

    def test_assignment_is_refused_because_the_model_is_frozen(self) -> None:
        answer = StandInAnswer()
        with pytest.raises(ValidationError):
            answer.status = 500
