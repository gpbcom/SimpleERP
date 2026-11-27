from __future__ import annotations

import logging
from typing import Dict, Optional

import pytest
from erp_context.models.refusals.enums import RefusalReason
from erp_context.models.refusals.refusal_catalog import RefusalCatalog
from erp_context.storage.context.request_context_store import RequestContextStore
from fastapi import FastAPI
from fastapi.testclient import TestClient

from tests.api.middleware.helpers import (
    COMPANY_HEADER,
    LOGGER_NAME,
    PROTECTED_PATH,
    PUBLIC_PATH,
    REQUEST_HEADER,
    SECRET,
    USER_HEADER,
    valid_headers,
)

INVALID_COMPANY = " \t "


class TestCompanyContextMiddleware:
    def test_a_request_without_a_company_is_refused_with_the_catalogue_status(
        self, client: TestClient, catalog: RefusalCatalog
    ) -> None:
        headers = valid_headers()
        del headers[COMPANY_HEADER]
        response = client.get(PROTECTED_PATH, headers=headers)
        expected = catalog.code_for(RefusalReason.NO_COMPANY)
        assert response.status_code == expected.status
        assert response.headers["content-type"].startswith("application/problem+json")
        assert response.json()["code"] == expected.code

    def test_an_invalid_company_is_refused_like_a_missing_one(
        self, client: TestClient, catalog: RefusalCatalog
    ) -> None:
        response = client.get(PROTECTED_PATH, headers=valid_headers(company=INVALID_COMPANY))
        expected = catalog.code_for(RefusalReason.NO_COMPANY)
        assert response.status_code == expected.status
        assert response.headers["content-type"].startswith("application/problem+json")
        assert response.json()["code"] == expected.code

    def test_a_request_without_a_user_is_refused_with_no_user(
        self, client: TestClient, catalog: RefusalCatalog
    ) -> None:
        headers = valid_headers()
        del headers[USER_HEADER]
        response = client.get(PROTECTED_PATH, headers=headers)
        expected = catalog.code_for(RefusalReason.NO_USER)
        assert response.status_code == expected.status
        assert response.headers["content-type"].startswith("application/problem+json")
        assert response.json()["code"] == expected.code

    def test_a_refused_request_never_reaches_the_application(self, app: FastAPI, client: TestClient) -> None:
        client.get(PROTECTED_PATH)
        assert app.state.calls == []

    def test_both_headers_give_the_same_company_and_user_to_the_service_and_storage_layers(
        self, client: TestClient
    ) -> None:
        response = client.get(PROTECTED_PATH, headers=valid_headers(company="C-12", user="U-7"))
        assert response.status_code == 200
        body = response.json()
        assert body["service_company"] == body["storage_company"] == "C-12"
        assert body["service_user"] == body["storage_user"] == "U-7"

    def test_nothing_stays_bound_after_the_response(self, client: TestClient, store: RequestContextStore) -> None:
        client.get(PROTECTED_PATH, headers=valid_headers())
        assert store.get() is None

    def test_nothing_stays_bound_after_a_refusal(self, client: TestClient, store: RequestContextStore) -> None:
        client.get(PROTECTED_PATH)
        assert store.get() is None

    def test_the_instance_is_the_request_id_header(self, client: TestClient) -> None:
        response = client.get(PROTECTED_PATH, headers=valid_headers(request_id="req-42"))
        assert response.json()["service_request"] == "req-42"
        refused = client.get(PROTECTED_PATH, headers={REQUEST_HEADER: "req-43"})
        assert refused.json()["instance"] == "req-43"

    def test_a_missing_request_id_is_replaced_by_a_generated_one(self, client: TestClient) -> None:
        response = client.get(PROTECTED_PATH)
        assert response.json()["instance"]
        accepted = client.get(PROTECTED_PATH, headers=valid_headers(request_id=None))
        assert accepted.json()["service_request"]

    def test_a_public_path_passes_without_a_context(self, app: FastAPI, client: TestClient) -> None:
        response = client.get(PUBLIC_PATH)
        assert response.status_code == 200
        assert response.json() == {"status": "ok", "bound": None}
        assert app.state.calls == [PUBLIC_PATH]

    def test_lifespan_passes_through_unchanged(self, app: FastAPI) -> None:
        with TestClient(app) as started:
            assert started.get(PUBLIC_PATH).status_code == 200

    @pytest.mark.parametrize("company", [None, INVALID_COMPANY])
    def test_the_body_and_the_logs_never_hold_a_secret_or_the_raw_company(
        self, client: TestClient, caplog: pytest.LogCaptureFixture, company: Optional[str]
    ) -> None:
        caplog.set_level(logging.DEBUG)
        headers: Dict[str, str] = {"Authorization": SECRET, USER_HEADER: "U-7"}
        if company is not None:
            headers[COMPANY_HEADER] = company
        response = client.get(PROTECTED_PATH, headers=headers)
        logs = "\n".join(record.getMessage() for record in caplog.records)
        assert SECRET not in response.text
        assert SECRET not in logs
        assert "s3cr3t" not in logs
        if company is not None:
            assert repr(company) not in logs
            assert repr(company) not in response.text

    def test_the_refusal_log_line_holds_the_code_the_reason_the_method_and_the_path(
        self, client: TestClient, catalog: RefusalCatalog, caplog: pytest.LogCaptureFixture
    ) -> None:
        caplog.set_level(logging.DEBUG, logger=LOGGER_NAME)
        client.get(PROTECTED_PATH, headers={USER_HEADER: "U-7"})
        records = [r for r in caplog.records if r.name == LOGGER_NAME and r.levelno == logging.WARNING]
        assert len(records) == 1
        line = records[0].getMessage()
        expected = catalog.code_for(RefusalReason.NO_COMPANY)
        assert expected.code in line
        assert RefusalReason.NO_COMPANY.value in line
        assert "GET" in line
        assert PROTECTED_PATH in line
        assert "U-7" in line
