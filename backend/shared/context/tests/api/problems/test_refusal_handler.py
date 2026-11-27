from __future__ import annotations

from typing import Tuple

import pytest
from erp_context.models.refusals.enums import RefusalReason
from fastapi.testclient import TestClient

from tests.api.rights.helpers import (
    COMPANY_ID,
    REQUEST_ID,
    SECRET_TOKEN,
    USER_ID,
    build_app,
    build_rights,
    load_catalog,
    request_headers,
)


class TestRefusalHandler:
    def refused(self) -> Tuple[TestClient, int, str]:
        catalog = load_catalog()
        client = TestClient(build_app(build_rights([], catalog), catalog))
        expected = catalog.code_for(RefusalReason.NO_POLICY)
        return client, expected.status, expected.code

    def test_a_refusal_answers_with_the_catalogue_status(self) -> None:
        client, status, _ = self.refused()
        response = client.get(
            "/records/invoice/R-1", params={"action": "invoice.read", "company": COMPANY_ID}, headers=request_headers()
        )
        assert response.status_code == status

    def test_a_refusal_is_problem_json_with_its_code(self) -> None:
        client, _, code = self.refused()
        response = client.get(
            "/records/invoice/R-1", params={"action": "invoice.read", "company": COMPANY_ID}, headers=request_headers()
        )
        assert response.headers["content-type"].startswith("application/problem+json")
        assert response.json()["code"] == code

    def test_the_instance_is_the_request_id(self) -> None:
        client, _, _ = self.refused()
        response = client.get(
            "/records/invoice/R-1", params={"action": "invoice.read", "company": COMPANY_ID}, headers=request_headers()
        )
        assert response.json()["instance"] == REQUEST_ID

    @pytest.mark.parametrize("secret", [SECRET_TOKEN, USER_ID, COMPANY_ID])
    def test_the_body_holds_no_header_value_of_the_request(self, secret: str) -> None:
        client, _, _ = self.refused()
        response = client.get(
            "/records/invoice/R-1",
            params={"action": "invoice.read", "company": "company-0000"},
            headers=request_headers(),
        )
        assert secret not in response.text
