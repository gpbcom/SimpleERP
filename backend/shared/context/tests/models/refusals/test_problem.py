from __future__ import annotations

from typing import Dict, Type

import pytest
from erp_context.models.refusals.exceptions import (
    SEProblemInvalidAction,
    SEProblemInvalidCode,
    SEProblemInvalidDetail,
    SEProblemInvalidInstance,
    SEProblemInvalidReference,
    SEProblemInvalidStatus,
    SEProblemInvalidTitle,
    SEProblemInvalidType,
)
from erp_context.models.refusals.problem import Problem
from pydantic import JsonValue, ValidationError


class TestProblem:
    VALID: Dict[str, JsonValue] = {
        "title": "errors.access_company_01.title",
        "status": 400,
        "detail": "errors.access_company_01.why",
        "code": "ACCESS-COMPANY-01",
        "action": "errors.access_company_01.action",
        "reference": "ACCESS-COMPANY-01",
    }

    ERRORS: Dict[str, Type[Exception]] = {
        "type": SEProblemInvalidType,
        "title": SEProblemInvalidTitle,
        "status": SEProblemInvalidStatus,
        "detail": SEProblemInvalidDetail,
        "code": SEProblemInvalidCode,
        "action": SEProblemInvalidAction,
        "reference": SEProblemInvalidReference,
        "instance": SEProblemInvalidInstance,
    }

    def test_defaults(self) -> None:
        problem = Problem.model_validate(self.VALID)

        assert problem.type == "about:blank"
        assert problem.instance is None
        for name in self.VALID:
            partial = {key: value for key, value in self.VALID.items() if key != name}
            with pytest.raises(ValidationError):
                Problem.model_validate(partial)

    def test_full_valid_construction(self) -> None:
        problem = Problem.model_validate({**self.VALID, "type": " about:blank ", "instance": " req-123 "})

        assert problem.type == "about:blank"
        assert problem.title == "errors.access_company_01.title"
        assert problem.status == 400
        assert problem.detail == "errors.access_company_01.why"
        assert problem.code == "ACCESS-COMPANY-01"
        assert problem.action == "errors.access_company_01.action"
        assert problem.reference == "ACCESS-COMPANY-01"
        assert problem.instance == "req-123"

    @pytest.mark.parametrize("name", ["type", "instance"])
    def test_none_becomes_the_default(self, name: str) -> None:
        problem = Problem.model_validate({**self.VALID, name: None})

        assert getattr(problem, name) == ("about:blank" if name == "type" else None)

    @pytest.mark.parametrize("name", ["title", "status", "detail", "code", "action", "reference"])
    def test_none_is_refused_where_there_is_no_default(self, name: str) -> None:
        with pytest.raises(self.ERRORS[name]):
            Problem.model_validate({**self.VALID, name: None})

    @pytest.mark.parametrize(
        ("name", "value"),
        [
            *[("type", value) for value in ("", "   ", 3, True, ["about:blank"])],
            *[("instance", value) for value in ("", "   ", 3, True, ["req"])],
            *[("code", value) for value in ("", 12, True, "SITE-CLOSE", "site-close-01")],
            *[("reference", value) for value in ("", 12, True, "SITE-CLOSE-1", "site close 01")],
            *[(name, value) for name in ("title", "detail", "action") for value in ("", 12, True, "Close it.", "A.b")],
            *[("status", value) for value in (True, "403", 403.0, 399, 600, [403])],
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue) -> None:
        with pytest.raises(self.ERRORS[name]):
            Problem.model_validate({**self.VALID, name: value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            Problem.model_validate({**self.VALID, "other": "x"})

    def test_round_trip(self) -> None:
        problem = Problem.model_validate({**self.VALID, "instance": "req-123"})

        assert Problem.model_validate(problem.model_dump()) == problem
        assert Problem.model_validate_json(problem.model_dump_json()) == problem

    def test_the_body_holds_the_rfc_9457_members(self) -> None:
        body = Problem.model_validate(self.VALID).model_dump()

        assert set(body) == {"type", "title", "status", "detail", "code", "action", "reference", "instance"}

    def test_the_problem_is_frozen(self) -> None:
        problem = Problem.model_validate(self.VALID)

        with pytest.raises(ValidationError):
            problem.status = 403
