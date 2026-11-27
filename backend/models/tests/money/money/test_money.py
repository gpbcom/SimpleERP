from __future__ import annotations

from decimal import Decimal
from typing import Dict

import pytest
from erp_models.money.exceptions import (
    SEInvalidMoneyException,
    SEMoneyCurrencyMismatch,
    SEMoneyInvalidAmount,
    SEMoneyInvalidCurrency,
)
from erp_models.money.money import Money
from pydantic import ValidationError


class TestMoney:
    def test_defaults(self) -> None:
        with pytest.raises(ValidationError):
            Money.model_validate({})
        with pytest.raises(ValidationError):
            Money.model_validate({"amount": "1.00"})
        with pytest.raises(ValidationError):
            Money.model_validate({"currency": "EUR"})

    def test_full_valid_construction(self) -> None:
        money = Money.model_validate({"amount": Decimal("12.50"), "currency": "EUR"})

        assert money.amount == Decimal("12.50")
        assert money.currency == "EUR"
        assert isinstance(money.amount, Decimal)

    @pytest.mark.parametrize(
        ("value", "expected"),
        [
            (Decimal("12.50"), Decimal("12.50")),
            (12, Decimal("12")),
            ("12.50", Decimal("12.50")),
            (" 12.50 ", Decimal("12.50")),
            ("-3.75", Decimal("-3.75")),
            (Decimal("0.00"), Decimal("0.00")),
        ],
    )
    def test_an_amount_is_kept_exactly_as_a_decimal(self, value: object, expected: Decimal) -> None:
        money = Money.model_validate({"amount": value, "currency": "EUR"})

        assert isinstance(money.amount, Decimal)
        assert money.amount == expected
        assert money.amount.as_tuple() == expected.as_tuple()

    def test_a_currency_is_stripped(self) -> None:
        assert Money.model_validate({"amount": "1", "currency": " EUR "}).currency == "EUR"

    @pytest.mark.parametrize(
        ("name", "error"),
        [("amount", SEMoneyInvalidAmount), ("currency", SEMoneyInvalidCurrency)],
    )
    def test_none_becomes_the_default(self, name: str, error: type[Exception]) -> None:
        values: Dict[str, object] = {"amount": "1.00", "currency": "EUR"}
        values[name] = None

        with pytest.raises(error):
            Money.model_validate(values)

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("amount", 0.1, SEMoneyInvalidAmount),
            ("amount", 1.0, SEMoneyInvalidAmount),
            ("amount", True, SEMoneyInvalidAmount),
            ("amount", False, SEMoneyInvalidAmount),
            ("amount", None, SEMoneyInvalidAmount),
            ("amount", "", SEMoneyInvalidAmount),
            ("amount", "   ", SEMoneyInvalidAmount),
            ("amount", "abc", SEMoneyInvalidAmount),
            ("amount", "1.2.3", SEMoneyInvalidAmount),
            ("amount", "NaN", SEMoneyInvalidAmount),
            ("amount", "Infinity", SEMoneyInvalidAmount),
            ("amount", "-Infinity", SEMoneyInvalidAmount),
            ("amount", Decimal("NaN"), SEMoneyInvalidAmount),
            ("amount", Decimal("Infinity"), SEMoneyInvalidAmount),
            ("amount", [1], SEMoneyInvalidAmount),
            ("amount", {"value": 1}, SEMoneyInvalidAmount),
            ("currency", "eur", SEMoneyInvalidCurrency),
            ("currency", "EURO", SEMoneyInvalidCurrency),
            ("currency", "EU", SEMoneyInvalidCurrency),
            ("currency", "", SEMoneyInvalidCurrency),
            ("currency", "   ", SEMoneyInvalidCurrency),
            ("currency", "E1R", SEMoneyInvalidCurrency),
            ("currency", None, SEMoneyInvalidCurrency),
            ("currency", 978, SEMoneyInvalidCurrency),
            ("currency", True, SEMoneyInvalidCurrency),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: object, error: type[Exception]) -> None:
        values: Dict[str, object] = {"amount": "1.00", "currency": "EUR"}
        values[name] = value

        with pytest.raises(error):
            Money.model_validate(values)

    @pytest.mark.parametrize("error", [SEMoneyInvalidAmount, SEMoneyInvalidCurrency, SEMoneyCurrencyMismatch])
    def test_the_exceptions_share_a_base_and_are_not_value_errors(self, error: type[Exception]) -> None:
        assert issubclass(error, SEInvalidMoneyException)
        assert not issubclass(error, ValueError)

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            Money.model_validate({"amount": "1.00", "currency": "EUR", "extra": 1})

    def test_a_money_cannot_be_changed(self) -> None:
        money = Money.model_validate({"amount": "1.00", "currency": "EUR"})

        with pytest.raises(ValidationError):
            money.amount = Decimal("2.00")

    def test_round_trip(self) -> None:
        money = Money.model_validate({"amount": "12345678901234.56", "currency": "EUR"})

        dumped = money.model_dump(mode="json")
        assert dumped == {"amount": "12345678901234.56", "currency": "EUR"}
        assert Money.model_validate(dumped) == money
        again = Money.model_validate_json(money.model_dump_json())
        assert again == money
        assert again.amount == Decimal("12345678901234.56")
