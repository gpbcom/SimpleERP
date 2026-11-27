from __future__ import annotations

import logging
from pathlib import Path
from typing import Dict

import httpx
import pytest
from erp_platform.api.http.problem_handler import ProblemHandler
from erp_platform.service.problems.problem_service import ProblemService
from fastapi import FastAPI


class TestProblemHandler:
    CATALOG_PATH = Path(__file__).resolve().parents[3] / "conf" / "catalogs" / "error_codes.yaml"
    SECRETS = ("s3cr3t-value", "abc123")

    def read_only(self) -> Dict[str, str]:
        return {"ok": "yes"}

    def typed(self, count: int) -> Dict[str, int]:
        return {"count": count}

    def explode(self) -> Dict[str, str]:
        raise RuntimeError("password=s3cr3t-value token=abc123")

    def build_app(self) -> FastAPI:
        app = FastAPI()
        app.add_api_route("/read-only", self.read_only, methods=["GET"])
        app.add_api_route("/typed", self.typed, methods=["GET"])
        app.add_api_route("/explode", self.explode, methods=["GET"])
        ProblemHandler(ProblemService(self.CATALOG_PATH)).register(app)
        return app

    def build_client(self) -> httpx.AsyncClient:
        transport = httpx.ASGITransport(app=self.build_app(), raise_app_exceptions=False)
        return httpx.AsyncClient(transport=transport, base_url="http://test")

    def assert_problem(self, response: httpx.Response, status: int, code: str) -> None:
        assert response.status_code == status
        assert response.headers["content-type"].split(";")[0] == "application/problem+json"
        body = response.json()
        for key in ("title", "status", "detail", "code"):
            assert key in body
        assert body["status"] == status
        assert body["code"] == code

    async def test_an_unknown_path_answers_404_with_the_route_code(self) -> None:
        async with self.build_client() as client:
            response = await client.get("/nowhere")
        self.assert_problem(response, 404, "PLATFORM-ROUTE-01")

    async def test_a_wrong_method_answers_405_with_the_method_code(self) -> None:
        async with self.build_client() as client:
            response = await client.post("/read-only")
        self.assert_problem(response, 405, "PLATFORM-METHOD-01")

    async def test_a_bad_typed_query_parameter_answers_422_with_the_request_code(self) -> None:
        async with self.build_client() as client:
            response = await client.get("/typed", params={"count": "not-a-number"})
        self.assert_problem(response, 422, "PLATFORM-REQUEST-01")

    async def test_a_valid_request_is_left_untouched(self) -> None:
        async with self.build_client() as client:
            response = await client.get("/typed", params={"count": "3"})
        assert response.status_code == 200
        assert response.json() == {"count": 3}

    async def test_an_unexpected_exception_answers_500_with_the_internal_code(self) -> None:
        async with self.build_client() as client:
            response = await client.get("/explode")
        self.assert_problem(response, 500, "PLATFORM-INTERNAL-01")

    @pytest.mark.parametrize("secret", SECRETS)
    async def test_an_unexpected_exception_leaks_no_secret_in_the_body(self, secret: str) -> None:
        async with self.build_client() as client:
            response = await client.get("/explode")
        assert secret not in response.text

    @pytest.mark.parametrize("secret", SECRETS)
    async def test_an_unexpected_exception_leaks_no_secret_in_the_logs(
        self, secret: str, caplog: pytest.LogCaptureFixture
    ) -> None:
        with caplog.at_level(logging.DEBUG):
            async with self.build_client() as client:
                await client.get("/explode")
        assert caplog.records
        assert secret not in caplog.text
        assert all(secret not in record.getMessage() for record in caplog.records)
