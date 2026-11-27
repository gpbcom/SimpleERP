from __future__ import annotations

from datetime import date, timedelta
from decimal import Decimal
from pathlib import Path
from typing import List, Union

import pytest
from erp_country_rules.models.packs.country_pack import CountryPack
from erp_country_rules.service.rules.country_rules import CountryRules
from erp_models.money.money import Money

from tests.service.rules.country_rules.helpers import CASE_DAYS, VALUE_CASES


class TestValuesByDate:
    def test_an_invoice_of_last_year_gets_last_years_rate(self, country_rules: CountryRules) -> None:
        assert country_rules.value("standard-rate", "ZZ", date(2025, 6, 15)) == Decimal("19.6")

    @pytest.mark.parametrize(
        ("day", "expected"),
        [
            (date(2027, 6, 30), Decimal("20")),
            (date(2027, 7, 1), Decimal("21")),
            (date(2035, 1, 1), Decimal("21")),
        ],
    )
    def test_a_future_dated_rule_applies_from_its_date(
        self, country_rules: CountryRules, day: date, expected: Decimal
    ) -> None:
        assert country_rules.value("standard-rate", "ZZ", day) == expected

    @pytest.mark.parametrize(("rule", "day", "expected"), VALUE_CASES)
    def test_the_value_in_force_on_each_boundary_day(
        self, country_rules: CountryRules, rule: str, day: date, expected: Union[Money, Decimal]
    ) -> None:
        assert country_rules.value(rule, "ZZ", day) == expected

    def test_every_rate_change_has_a_case_before_and_on_its_date(self) -> None:
        pack = CountryPack.load(Path(__file__).parent / "packs" / "zz" / "rules.yaml")
        missing: List[str] = []
        for rule in pack.rules:
            for version in rule.versions[1:]:
                for day in (version.valid_from - timedelta(days=1), version.valid_from):
                    if day not in CASE_DAYS[rule.rule]:
                        missing.append(f"{rule.rule} {day}")
        assert missing == []

    def test_the_country_is_accepted_in_lower_case(self, country_rules: CountryRules) -> None:
        assert country_rules.value("standard-rate", "zz", date(2026, 1, 1)) == Decimal("20")

    def test_a_percentage_is_a_decimal_never_a_float(self, country_rules: CountryRules) -> None:
        value = country_rules.value("standard-rate", "ZZ", date(2025, 6, 15))
        assert isinstance(value, Decimal)
        assert not isinstance(value, float)
