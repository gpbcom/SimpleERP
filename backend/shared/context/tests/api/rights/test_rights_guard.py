from __future__ import annotations

import pytest
from erp_context.api.rights.rights_guard import RightsGuard
from erp_context.models.refusals.enums import RefusalReason
from erp_context.models.refusals.exceptions import SEAccessDeniedError, SEAccessNoCompanyError
from erp_context.models.refusals.refusal_catalog import RefusalCatalog
from erp_context.service.context.company_context_service import CompanyContextService

from tests.api.rights.allow_action_policy import AllowActionPolicy
from tests.api.rights.helpers import OTHER_COMPANY_ID, a_record, build_rights


class TestRightsGuard:
    def test_a_check_passes_when_the_action_is_allowed(
        self, catalog: RefusalCatalog, bound_context: CompanyContextService
    ) -> None:
        guard = RightsGuard(build_rights([AllowActionPolicy("invoice.read")], catalog), bound_context)
        assert guard.check("invoice.read", a_record()) is None

    def test_a_check_raises_access_denied_when_no_policy_allows(
        self, catalog: RefusalCatalog, bound_context: CompanyContextService
    ) -> None:
        guard = RightsGuard(build_rights([], catalog), bound_context)
        with pytest.raises(SEAccessDeniedError) as raised:
            guard.check("invoice.read", a_record())
        assert raised.value.reason == RefusalReason.NO_POLICY

    def test_a_check_raises_access_denied_for_a_record_of_another_company(
        self, catalog: RefusalCatalog, bound_context: CompanyContextService
    ) -> None:
        guard = RightsGuard(build_rights([AllowActionPolicy("invoice.read")], catalog), bound_context)
        with pytest.raises(SEAccessDeniedError) as raised:
            guard.check("invoice.read", a_record(OTHER_COMPANY_ID))
        assert raised.value.reason == RefusalReason.OTHER_COMPANY

    def test_a_check_without_a_bound_context_raises_no_company(
        self, catalog: RefusalCatalog, context_service: CompanyContextService
    ) -> None:
        guard = RightsGuard(build_rights([AllowActionPolicy("invoice.read")], catalog), context_service)
        with pytest.raises(SEAccessNoCompanyError):
            guard.check("invoice.read", a_record())
