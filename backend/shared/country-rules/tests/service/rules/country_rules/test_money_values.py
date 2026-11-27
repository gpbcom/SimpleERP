from __future__ import annotations

from datetime import date
from decimal import Decimal

import pytest
from erp_country_rules.service.rules.country_rules import CountryRules
from erp_models.money.money import Money


class TestMoneyValues:
    def test_a_money_rule_is_read_as_an_exact_decimal_with_its_currency(self, country_rules: CountryRules) -> None:
        value = country_rules.value("stamp-duty", "ZZ", date(2026, 3, 1))

        assert isinstance(value, Money)
        assert isinstance(value.amount, Decimal)
        assert value.amount == Decimal("0.10")
        assert value.currency == "EUR"

    def test_the_value_of_2027_is_twenty_cents_in_euros(self, country_rules: CountryRules) -> None:
        value = country_rules.value("stamp-duty", "ZZ", date(2027, 3, 1))

        assert isinstance(value, Money)
        assert value.amount == Decimal("0.20")
        assert value.currency == "EUR"

    def test_two_values_sum_exactly_where_floats_do_not(self, country_rules: CountryRules) -> None:
        first = country_rules.value("stamp-duty", "ZZ", date(2026, 3, 1))
        second = country_rules.value("stamp-duty", "ZZ", date(2027, 3, 1))
        assert isinstance(first, Money)
        assert isinstance(second, Money)

        total = first.add(second)

        assert 0.1 + 0.2 != 0.3
        assert total.amount == Decimal("0.30")
        assert total.currency == "EUR"

    def test_three_lines_of_ten_cents_sum_exactly_to_thirty_cents(self, country_rules: CountryRules) -> None:
        line = country_rules.value("stamp-duty", "ZZ", date(2026, 3, 1))
        assert isinstance(line, Money)

        total = Money.total("EUR", [line, line, line])

        assert total == Money(amount="0.30", currency="EUR")

    @pytest.mark.parametrize("on", [date(2024, 6, 1), date(2026, 3, 1), date(2027, 8, 1)])
    def test_a_decimal_rule_is_a_decimal_never_a_float_or_money(self, country_rules: CountryRules, on: date) -> None:
        value = country_rules.value("standard-rate", "ZZ", on)

        assert isinstance(value, Decimal)
        assert not isinstance(value, (float, Money))
