from __future__ import annotations

import json
from typing import Dict, Union

import pytest
from erp_platform.models.problems.exceptions import (
    SEInvalidProblemDetailsException,
    SEProblemDetailsInvalidCode,
    SEProblemDetailsInvalidDetail,
    SEProblemDetailsInvalidStatus,
    SEProblemDetailsInvalidTitle,
)
from erp_platform.models.problems.problem_details import ProblemDetails
from pydantic import JsonValue, ValidationError


class TestProblemDetails:
    def a_problem(self) -> ProblemDetails:
        return ProblemDetails(
            title="errors.site_close_01.title",
            status=404,
            detail="errors.site_close_01.why",
            code="SITE-CLOSE-01",
        )

    def valid_data(self) -> Dict[str, JsonValue]:
        return {"title": "errors.a.title", "status": 400, "detail": "errors.a.why", "code": "A-01"}

    def test_defaults(self) -> None:
        assert ProblemDetails.STATUS_MIN == 400
        assert ProblemDetails.STATUS_MAX == 599
        assert "type" not in ProblemDetails.model_fields
        assert all(field.is_required() for field in ProblemDetails.model_fields.values())

    def test_full_valid_construction(self) -> None:
        problem = ProblemDetails(
            title="  errors.site_close_01.title  ",
            status=404,
            detail=" errors.site_close_01.why ",
            code=" SITE-CLOSE-01 ",
        )
        assert problem.title == "errors.site_close_01.title"
        assert problem.status == 404
        assert problem.detail == "errors.site_close_01.why"
        assert problem.code == "SITE-CLOSE-01"

    @pytest.mark.parametrize(
        ("name", "error"),
        [
            ("title", SEProblemDetailsInvalidTitle),
            ("status", SEProblemDetailsInvalidStatus),
            ("detail", SEProblemDetailsInvalidDetail),
            ("code", SEProblemDetailsInvalidCode),
        ],
    )
    def test_none_becomes_the_default(self, name: str, error: type[Exception]) -> None:
        """No field has a default to become, so ``None`` is refused with the field's own exception."""
        data = self.valid_data()
        data[name] = None
        with pytest.raises(error):
            ProblemDetails.model_validate(data)

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("title", "", SEProblemDetailsInvalidTitle),
            ("title", "   ", SEProblemDetailsInvalidTitle),
            ("title", 3, SEProblemDetailsInvalidTitle),
            ("status", 399, SEProblemDetailsInvalidStatus),
            ("status", 600, SEProblemDetailsInvalidStatus),
            ("status", True, SEProblemDetailsInvalidStatus),
            ("status", "404", SEProblemDetailsInvalidStatus),
            ("status", 404.0, SEProblemDetailsInvalidStatus),
            ("detail", "", SEProblemDetailsInvalidDetail),
            ("detail", "   ", SEProblemDetailsInvalidDetail),
            ("detail", 3, SEProblemDetailsInvalidDetail),
            ("code", "", SEProblemDetailsInvalidCode),
            ("code", "   ", SEProblemDetailsInvalidCode),
            ("code", 3, SEProblemDetailsInvalidCode),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        data = self.valid_data()
        data[name] = value
        with pytest.raises(error):
            ProblemDetails.model_validate(data)

    @pytest.mark.parametrize("status", [400, 599])
    def test_the_bounds_of_status_are_accepted(self, status: int) -> None:
        data = self.valid_data()
        data["status"] = status
        assert ProblemDetails.model_validate(data).status == status

    @pytest.mark.parametrize(
        "error",
        [
            SEProblemDetailsInvalidTitle,
            SEProblemDetailsInvalidStatus,
            SEProblemDetailsInvalidDetail,
            SEProblemDetailsInvalidCode,
        ],
    )
    def test_the_field_exceptions_share_the_model_base(self, error: type[Exception]) -> None:
        assert issubclass(error, SEInvalidProblemDetailsException)

    def test_rejects_unknown_keys(self) -> None:
        data = self.valid_data()
        data["type"] = "https://example.org/x"
        with pytest.raises(ValidationError):
            ProblemDetails.model_validate(data)

    def test_it_serialises_without_a_type_member(self) -> None:
        body = json.loads(self.a_problem().model_dump_json())
        assert set(body) == {"title", "status", "detail", "code"}

    def test_round_trip(self) -> None:
        problem = self.a_problem()
        data: Dict[str, Union[str, int]] = problem.model_dump()
        assert ProblemDetails.model_validate(data) == problem
        assert ProblemDetails.model_validate_json(problem.model_dump_json()) == problem
