from __future__ import annotations

import httpx
import pytest
from erp_platform.api.http.health_router import HealthRouter
from erp_platform.service.health.health_service import HealthService
from fastapi import FastAPI


class TestHealthRouter:
    def a_client(self) -> httpx.AsyncClient:
        app = FastAPI()
        app.include_router(HealthRouter(HealthService()).router)
        return httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://test")

    async def test_health_answers_ok_as_json(self) -> None:
        async with self.a_client() as client:
            response = await client.get("/health")

        assert response.status_code == 200
        assert response.headers["content-type"].startswith("application/json")
        assert response.json() == {"status": "ok"}

    @pytest.mark.parametrize("method", ["POST", "PUT", "PATCH", "DELETE"])
    async def test_health_accepts_only_get(self, method: str) -> None:
        async with self.a_client() as client:
            response = await client.request(method, "/health")

        assert response.status_code == 405
