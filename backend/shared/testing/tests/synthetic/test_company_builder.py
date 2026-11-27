from __future__ import annotations

from typing import List

import pytest
from erp_testing.models.synthetic.exceptions import SESyntheticDataError, SESyntheticSectorUnknownError
from erp_testing.models.synthetic.synthetic_catalog import SyntheticCatalog
from erp_testing.synthetic.company_builder import CompanyBuilder
from erp_testing.synthetic.synthetic_builder import SyntheticBuilder


def small_catalog() -> SyntheticCatalog:
    return SyntheticCatalog(
        sectors=["sc01", "sc02", "sc03"],
        company_words=["Alpha", "Beta", "Gamma", "Delta", "Omega"],
        first_names=["Ada", "Bo", "Cy"],
        last_names=["Stone", "Reed", "Hale"],
        email_domain="example.test",
    )


class TestCompanyBuilder:
    def test_it_is_a_synthetic_builder(self) -> None:
        assert isinstance(CompanyBuilder(small_catalog(), "sc01"), SyntheticBuilder)

    @pytest.mark.parametrize("sector", ["sc01", "sc02", "sc03"])
    def test_the_same_catalog_sector_and_seed_give_the_same_sequence(self, sector: str) -> None:
        first = CompanyBuilder(small_catalog(), sector, seed=7)
        second = CompanyBuilder(small_catalog(), sector, seed=7)
        assert [first.build() for _ in range(5)] == [second.build() for _ in range(5)]

    def test_another_seed_gives_other_ids(self) -> None:
        one = CompanyBuilder(small_catalog(), "sc01", seed=1).build()
        other = CompanyBuilder(small_catalog(), "sc01", seed=2).build()
        assert one.id != other.id

    def test_another_sector_gives_other_ids(self) -> None:
        one = CompanyBuilder(small_catalog(), "sc01", seed=1).build()
        other = CompanyBuilder(small_catalog(), "sc02", seed=1).build()
        assert one.id != other.id

    def test_successive_builds_have_distinct_ids(self) -> None:
        builder = CompanyBuilder(small_catalog(), "sc01")
        ids: List[str] = [str(builder.build().id) for _ in range(20)]
        assert len(set(ids)) == 20

    @pytest.mark.parametrize("sector", ["sc01", "sc02", "sc03"])
    def test_the_company_carries_its_sector(self, sector: str) -> None:
        assert CompanyBuilder(small_catalog(), sector).build().sector == sector

    def test_the_name_is_made_only_of_catalog_words(self) -> None:
        catalog = small_catalog()
        builder = CompanyBuilder(catalog, "sc01")
        for _ in range(10):
            words = builder.build().name.split()
            assert words
            assert set(words) <= set(catalog.company_words)

    @pytest.mark.parametrize("sector", ["sc01", "sc02", "sc03"])
    def test_an_unknown_sector_is_refused(self, sector: str) -> None:
        with pytest.raises(SESyntheticSectorUnknownError):
            CompanyBuilder(small_catalog(), f"not-{sector}").build()

    def test_the_unknown_sector_error_is_a_synthetic_data_error(self) -> None:
        with pytest.raises(SESyntheticDataError):
            CompanyBuilder(small_catalog(), "nothing").build()

    def test_every_sector_of_the_default_catalog_builds_companies(self) -> None:
        catalog = SyntheticCatalog.load(SyntheticCatalog.DEFAULT_PATH)
        assert catalog.sectors
        for sector in catalog.sectors:
            company = CompanyBuilder(catalog, sector).build()
            assert company.sector == sector
            assert set(company.name.split()) <= set(catalog.company_words)
