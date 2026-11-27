from __future__ import annotations

import json

import pytest
from erp_context.api.problems.problem_response import ProblemResponse
from erp_context.models.refusals.problem import Problem
from starlette.responses import JSONResponse


class TestProblemResponse:
    @pytest.fixture
    def problem(self) -> Problem:
        return Problem(
            title="errors.no_company.title",
            status=401,
            detail="errors.no_company.why",
            code="CONTEXT-COMPANY-01",
            action="errors.no_company.action",
            reference="CONTEXT-COMPANY-01",
            instance="req-1",
        )

    def test_it_is_a_json_response(self, problem: Problem) -> None:
        assert isinstance(ProblemResponse.of(problem), JSONResponse)

    def test_the_media_type_is_problem_json(self, problem: Problem) -> None:
        response = ProblemResponse.of(problem)
        assert ProblemResponse.media_type == "application/problem+json"
        assert response.headers["content-type"].startswith("application/problem+json")

    def test_the_status_is_the_status_of_the_problem(self, problem: Problem) -> None:
        assert ProblemResponse.of(problem).status_code == problem.status

    def test_the_body_holds_each_field_of_the_problem(self, problem: Problem) -> None:
        body = json.loads(ProblemResponse.of(problem).body)
        assert body == problem.model_dump(exclude_none=True)
        assert body["type"] == "about:blank"
        assert body["code"] == "CONTEXT-COMPANY-01"
        assert body["instance"] == "req-1"

    def test_an_absent_instance_is_left_out_of_the_body(self, problem: Problem) -> None:
        body = json.loads(ProblemResponse.of(problem.model_copy(update={"instance": None})).body)
        assert "instance" not in body
