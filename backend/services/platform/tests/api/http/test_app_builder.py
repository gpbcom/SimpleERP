from __future__ import annotations

from pathlib import Path
from typing import Dict

import httpx
import pytest
from erp_context.models.refusals.enums import RefusalReason
from erp_context.models.refusals.refusal_catalog import RefusalCatalog
from erp_platform.api.http.app_builder import AppBuilder
from erp_platform.models.config.platform_config import PlatformConfig
from fastapi import FastAPI

PLATFORM_FOLDER = Path(__file__).resolve().parents[3]
ERROR_CODES_PATH = PLATFORM_FOLDER / "conf" / "catalogs" / "error_codes.yaml"
REFUSAL_CODES_PATH = PLATFORM_FOLDER.parents[1] / "shared" / "context" / "conf" / "catalogs" / "refusal_codes.yaml"
COMPANY_HEADERS = {"X-Company-Id": "C-12", "X-User-Id": "U-7", "Authorization": "Bearer s3cr3t-token-value"}
BODY_MEMBERS = {"type", "title", "status", "detail", "code", "action", "reference", "instance"}
SECRETS = ("s3cr3t-token-value", "Bearer")


class TestAppBuilder:
    def app(self) -> FastAPI:
        config = PlatformConfig(error_codes_path=str(ERROR_CODES_PATH))
        return AppBuilder(config).build()

    def test_the_api_prefix_is_v1(self) -> None:
        assert AppBuilder.API_PREFIX == "/v1"

    def test_build_returns_a_fastapi_application(self) -> None:
        assert isinstance(self.app(), FastAPI)

    async def get(self, path: str, headers: Dict[str, str]) -> httpx.Response:
        transport = httpx.ASGITransport(app=self.app(), raise_app_exceptions=False)
        async with httpx.AsyncClient(transport=transport, base_url="http://platform") as client:
            return await client.get(path, headers=headers)

    async def test_health_answers_ok_without_a_company(self) -> None:
        response = await self.get("/v1/health", {})
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}

    async def test_a_request_without_a_company_is_refused_with_the_context_refusal(self) -> None:
        expected = RefusalCatalog.load(REFUSAL_CODES_PATH).code_for(RefusalReason.NO_COMPANY)
        response = await self.get("/v1/anything", {})
        assert response.status_code == expected.status
        assert response.headers["content-type"].startswith("application/problem+json")
        assert response.json()["code"] == expected.code

    async def test_an_unknown_route_with_a_company_is_a_404_problem(self) -> None:
        response = await self.get("/v1/anything", COMPANY_HEADERS)
        assert response.status_code == 404
        assert response.headers["content-type"].startswith("application/problem+json")
        assert response.json()["code"] == "PLATFORM-ROUTE-01"

    async def test_routes_are_served_under_v1_only(self) -> None:
        response = await self.get("/health", COMPANY_HEADERS)
        assert response.status_code == 404
        assert response.headers["content-type"].startswith("application/problem+json")
        assert response.json()["code"] == "PLATFORM-ROUTE-01"

    @pytest.mark.parametrize(
        ("path", "headers"),
        [("/v1/anything", {}), ("/v1/anything", COMPANY_HEADERS), ("/health", COMPANY_HEADERS)],
    )
    async def test_a_refusal_body_holds_only_problem_members_and_no_secret(
        self, path: str, headers: Dict[str, str]
    ) -> None:
        response = await self.get(path, headers)
        body = response.json()
        assert {"title", "status", "detail", "code"} <= set(body)
        assert set(body) <= BODY_MEMBERS
        assert not any(secret in response.text for secret in SECRETS)
