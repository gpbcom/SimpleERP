from __future__ import annotations

import logging
from typing import List

import pytest
from erp_context.models.refusals.refusal_catalog import RefusalCatalog
from erp_context.service.rights.policy import Policy
from fastapi.testclient import TestClient

from tests.api.rights.allow_action_policy import AllowActionPolicy
from tests.api.rights.helpers import (
    COMPANY_ID,
    OTHER_COMPANY_ID,
    a_record,
    a_user,
    build_app,
    build_rights,
    request_headers,
)


class TestDecisionParity:
    @pytest.mark.parametrize(
        ("policy_actions", "action", "company"),
        [
            pytest.param(["invoice.read"], "invoice.read", COMPANY_ID, id="allowed-by-the-policy"),
            pytest.param([], "invoice.read", COMPANY_ID, id="no-policy-denies-by-default"),
            pytest.param(["invoice.read"], "invoice.read", OTHER_COMPANY_ID, id="record-of-another-company"),
            pytest.param(["invoice.read"], "invoice.delete", COMPANY_ID, id="unknown-action"),
        ],
    )
    def test_http_and_a_direct_call_give_the_same_decision(
        self,
        catalog: RefusalCatalog,
        caplog: pytest.LogCaptureFixture,
        policy_actions: List[str],
        action: str,
        company: str,
    ) -> None:
        policies: List[Policy] = [AllowActionPolicy(name) for name in policy_actions]
        rights = build_rights(policies, catalog)
        client = TestClient(build_app(rights, catalog))
        decision = rights.decide(a_user(), action, a_record(company))
        direct = rights.allowed(a_user(), action, a_record(company))

        with caplog.at_level(logging.WARNING):
            response = client.get(
                "/records/invoice/R-1",
                params={"action": action, "company": company},
                headers=request_headers(),
            )

        assert direct == decision.allowed
        assert (response.status_code == 200) is direct
        if direct:
            return
        assert decision.reason is not None
        expected = catalog.code_for(decision.reason)
        assert response.status_code == expected.status
        assert response.headers["content-type"].startswith("application/problem+json")
        assert response.json()["code"] == expected.code
        assert expected.code in caplog.text
