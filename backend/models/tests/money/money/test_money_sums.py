from __future__ import annotations

from decimal import Decimal
from typing import List

import pytest
from erp_models.money.exceptions import SEMoneyCurrencyMismatch, SEMoneyInvalidCurrency
from erp_models.money.money import Money


class TestMoneySums:
    def a_line(self, amount: str, currency: str = "EUR") -> Money:
        return Money.model_validate({"amount": amount, "currency": currency})

    def test_ten_lines_of_ten_cents_total_exactly_one(self) -> None:
        lines: List[Money] = [self.a_line("0.10") for _ in range(10)]

        assert Money.total("EUR", lines).amount == Decimal("1.00")

    def test_a_decimal_sum_has_no_float_error(self) -> None:
        total = self.a_line("0.1").add(self.a_line("0.2"))

        assert total.amount == Decimal("0.3")
        assert 0.1 + 0.2 != 0.3

    def test_a_credit_note_sums_exactly(self) -> None:
        lines = [self.a_line("100.10"), self.a_line("-0.30"), self.a_line("-99.80")]

        assert Money.total("EUR", lines).amount == Decimal("0.00")

    def test_large_amounts_sum_exactly(self) -> None:
        lines = [self.a_line("12345678901234.56") for _ in range(3)]

        assert Money.total("EUR", lines).amount == Decimal("37037036703703.68")

    def test_add_leaves_both_operands_unchanged(self) -> None:
        left = self.a_line("1.10")
        right = self.a_line("2.20")

        result = left.add(right)

        assert result.amount == Decimal("3.30")
        assert result is not left
        assert result is not right
        assert left.amount == Decimal("1.10")
        assert right.amount == Decimal("2.20")

    def test_add_refuses_another_currency(self) -> None:
        with pytest.raises(SEMoneyCurrencyMismatch):
            self.a_line("1").add(self.a_line("1", "USD"))

    def test_total_refuses_a_line_in_another_currency(self) -> None:
        lines = [self.a_line("1"), self.a_line("1", "USD")]

        with pytest.raises(SEMoneyCurrencyMismatch):
            Money.total("EUR", lines)

    def test_total_of_no_line_is_zero_in_that_currency(self) -> None:
        total = Money.total("EUR", [])

        assert total == Money.zero("EUR")
        assert total.amount == Decimal("0")
        assert total.currency == "EUR"

    @pytest.mark.parametrize("currency", ["eur", "EURO", "", "EU"])
    def test_zero_with_a_bad_currency_is_refused(self, currency: str) -> None:
        with pytest.raises(SEMoneyInvalidCurrency):
            Money.zero(currency)
