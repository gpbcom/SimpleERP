from __future__ import annotations

import pytest
from erp_context.storage.context.request_context_store import RequestContextStore
from erp_models.ids.company_id import CompanyId
from erp_models.ids.record_id import RecordId
from erp_testing.context.synthetic_company_context import SyntheticCompanyContext
from erp_testing.models.synthetic import SyntheticCompany, SyntheticUser


class TestSyntheticCompanyContext:
    def a_company(self, number: int = 1) -> SyntheticCompany:
        return SyntheticCompany(id=CompanyId(value=f"C-{number}"), name=f"Synthetic Company {number}", sector="sc03")

    def a_user(self, company: SyntheticCompany, number: int = 1) -> SyntheticUser:
        return SyntheticUser(
            id=RecordId(value=f"U-{number}"),
            company_id=company.id,
            name=f"Synthetic User {number}",
            email=f"user{number}@simpleerp.test",
        )

    def test_inside_the_block_the_reader_returns_the_company_and_the_user(self) -> None:
        company = self.a_company()
        user = self.a_user(company)
        with SyntheticCompanyContext(company, user):
            current = RequestContextStore().get()
        assert current is not None
        assert current.user.company_id == company.id
        assert current.user.user_id == user.id.value

    def test_outside_the_block_the_reader_is_back_to_its_previous_state(self) -> None:
        company = self.a_company()
        before = RequestContextStore().get()
        with SyntheticCompanyContext(company, self.a_user(company)):
            pass
        assert RequestContextStore().get() == before

    def test_an_exception_in_the_block_still_restores_the_context(self) -> None:
        company = self.a_company()
        before = RequestContextStore().get()
        with pytest.raises(RuntimeError), SyntheticCompanyContext(company, self.a_user(company)):
            raise RuntimeError("boom")
        assert RequestContextStore().get() == before

    def test_nested_contexts_restore_the_outer_one(self) -> None:
        outer_company = self.a_company(1)
        inner_company = self.a_company(2)
        with SyntheticCompanyContext(outer_company, self.a_user(outer_company, 1)):
            with SyntheticCompanyContext(inner_company, self.a_user(inner_company, 2)):
                inner = RequestContextStore().get()
                assert inner is not None
                assert inner.user.company_id == inner_company.id
            outer = RequestContextStore().get()
        assert outer is not None
        assert outer.user.company_id == outer_company.id
        assert outer.user.user_id == "U-1"

    def test_the_context_property_matches_the_company_id_and_the_user_id(self) -> None:
        company = self.a_company()
        user = self.a_user(company)
        context = SyntheticCompanyContext(company, user).context
        assert context.user.company_id == company.id
        assert context.user.user_id == user.id.value
