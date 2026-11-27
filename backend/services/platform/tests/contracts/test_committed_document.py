from __future__ import annotations

import json
from pathlib import Path
from typing import Dict

from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import JsonValue


class TestCommittedDocument:
    def test_the_application_serves_its_openapi_document(self, app: FastAPI, client: TestClient) -> None:
        response = client.get(str(app.openapi_url))
        assert response.status_code == 200
        assert response.headers["content-type"].startswith("application/json")

    def test_the_served_document_is_the_generated_one(
        self, app: FastAPI, client: TestClient, document: Dict[str, JsonValue]
    ) -> None:
        response = client.get(str(app.openapi_url))
        assert response.json() == document

    def test_the_committed_document_is_the_served_one(
        self, app: FastAPI, client: TestClient, committed_path: Path
    ) -> None:
        served = client.get(str(app.openapi_url)).json()
        assert committed_path.is_file(), f"{committed_path} does not exist. {self.regenerate_hint()}"
        committed = json.loads(committed_path.read_text(encoding="utf-8"))
        assert committed == served, f"The committed OpenAPI document is stale. {self.regenerate_hint()}"

    def test_the_document_declares_the_health_path_under_v1(self, document: Dict[str, JsonValue]) -> None:
        paths = document["paths"]
        assert isinstance(paths, dict)
        assert "/v1/health" in paths

    def regenerate_hint(self) -> str:
        return (
            "Regenerate it with: "
            "uv run --package platform python .github/scripts/export_openapi.py backend/services/platform"
        )
