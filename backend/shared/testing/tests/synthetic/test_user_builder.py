from __future__ import annotations

from typing import List

import pytest
from erp_testing.models.synthetic.synthetic_catalog import SyntheticCatalog
from erp_testing.models.synthetic.synthetic_company import SyntheticCompany
from erp_testing.synthetic.company_builder import CompanyBuilder
from erp_testing.synthetic.synthetic_builder import SyntheticBuilder
from erp_testing.synthetic.user_builder import UserBuilder


def small_catalog() -> SyntheticCatalog:
    return SyntheticCatalog(
        sectors=["sc01", "sc02", "sc03"],
        company_words=["Alpha", "Beta", "Gamma", "Delta", "Omega"],
        first_names=["Ada", "Bo", "Cy"],
        last_names=["Stone", "Reed", "Hale"],
        email_domain="example.test",
    )


def a_company(catalog: SyntheticCatalog, sector: str = "sc01") -> SyntheticCompany:
    return CompanyBuilder(catalog, sector).build()


class TestUserBuilder:
    def test_it_is_a_synthetic_builder(self) -> None:
        catalog = small_catalog()
        assert isinstance(UserBuilder(catalog, a_company(catalog)), SyntheticBuilder)

    @pytest.mark.parametrize("sector", ["sc01", "sc02", "sc03"])
    def test_the_same_catalog_company_and_seed_give_the_same_sequence(self, sector: str) -> None:
        catalog = small_catalog()
        company = a_company(catalog, sector)
        first = UserBuilder(catalog, company, seed=3)
        second = UserBuilder(catalog, company, seed=3)
        assert [first.build() for _ in range(5)] == [second.build() for _ in range(5)]

    def test_another_seed_gives_other_ids(self) -> None:
        catalog = small_catalog()
        company = a_company(catalog)
        assert UserBuilder(catalog, company, seed=1).build().id != UserBuilder(catalog, company, seed=2).build().id

    def test_another_company_gives_other_ids(self) -> None:
        catalog = small_catalog()
        one = UserBuilder(catalog, a_company(catalog, "sc01")).build()
        other = UserBuilder(catalog, a_company(catalog, "sc02")).build()
        assert one.id != other.id

    def test_successive_builds_have_distinct_ids(self) -> None:
        catalog = small_catalog()
        builder = UserBuilder(catalog, a_company(catalog))
        ids: List[str] = [str(builder.build().id) for _ in range(20)]
        assert len(set(ids)) == 20

    def test_the_company_id_is_the_companys_id(self) -> None:
        catalog = small_catalog()
        company = a_company(catalog)
        assert UserBuilder(catalog, company).build().company_id == company.id

    def test_the_name_is_made_only_of_catalog_names(self) -> None:
        catalog = small_catalog()
        builder = UserBuilder(catalog, a_company(catalog))
        allowed = set(catalog.first_names) | set(catalog.last_names)
        for _ in range(10):
            words = builder.build().name.split()
            assert words
            assert set(words) <= allowed

    def test_the_email_is_on_the_catalog_domain(self) -> None:
        catalog = small_catalog()
        builder = UserBuilder(catalog, a_company(catalog))
        for _ in range(5):
            assert builder.build().email.endswith(f"@{catalog.email_domain}")

    def test_successive_emails_are_distinct(self) -> None:
        catalog = small_catalog()
        builder = UserBuilder(catalog, a_company(catalog))
        emails: List[str] = [builder.build().email for _ in range(20)]
        assert len(set(emails)) == 20

    def test_every_sector_of_the_default_catalog_builds_users(self) -> None:
        catalog = SyntheticCatalog.load(SyntheticCatalog.DEFAULT_PATH)
        for sector in catalog.sectors:
            company = a_company(catalog, sector)
            user = UserBuilder(catalog, company).build()
            assert user.company_id == company.id
            assert user.email.endswith(f"@{catalog.email_domain}")
