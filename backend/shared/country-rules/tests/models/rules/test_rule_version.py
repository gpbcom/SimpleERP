from __future__ import annotations

import datetime
from decimal import Decimal
from typing import Dict, Union

import pytest
from erp_country_rules.models.exceptions import (
    SERuleVersionEndsBeforeStart,
    SERuleVersionInvalidValidFrom,
    SERuleVersionInvalidValidTo,
    SERuleVersionInvalidValue,
)
from erp_country_rules.models.rules.rule_version import RuleVersion
from erp_models.money.money import Money
from pydantic import ValidationError


class TestRuleVersion:
    def test_defaults(self) -> None:
        version = RuleVersion(valid_from=datetime.date(2026, 1, 1), value=Decimal("20"))
        assert version.valid_from == datetime.date(2026, 1, 1)
        assert version.valid_to is None
        assert version.value == Decimal("20")

    def test_full_valid_construction(self) -> None:
        version = RuleVersion(
            valid_from=datetime.date(2026, 1, 1),
            valid_to=datetime.date(2026, 12, 31),
            value=Money(amount=Decimal("5.50"), currency="EUR"),
        )
        assert version.valid_from == datetime.date(2026, 1, 1)
        assert version.valid_to == datetime.date(2026, 12, 31)
        assert version.value == Money(amount=Decimal("5.50"), currency="EUR")

    def test_none_becomes_the_default(self) -> None:
        version = RuleVersion.model_validate({"valid_from": "2026-01-01", "valid_to": None, "value": "20"})
        assert version.valid_to is None

    @pytest.mark.parametrize(
        ("field", "value", "error"),
        [
            ("valid_from", 20260101, SERuleVersionInvalidValidFrom),
            ("valid_from", True, SERuleVersionInvalidValidFrom),
            ("valid_from", datetime.datetime(2026, 1, 1, 12, 0), SERuleVersionInvalidValidFrom),
            ("valid_from", "not a date", SERuleVersionInvalidValidFrom),
            ("valid_to", 20261231, SERuleVersionInvalidValidTo),
            ("valid_to", True, SERuleVersionInvalidValidTo),
            ("valid_to", datetime.datetime(2026, 12, 31, 12, 0), SERuleVersionInvalidValidTo),
            ("valid_to", "not a date", SERuleVersionInvalidValidTo),
            ("value", 19.6, SERuleVersionInvalidValue),
            ("value", True, SERuleVersionInvalidValue),
            ("value", "", SERuleVersionInvalidValue),
            ("value", "   ", SERuleVersionInvalidValue),
            ("value", "abc", SERuleVersionInvalidValue),
            ("value", "NaN", SERuleVersionInvalidValue),
            ("value", "Infinity", SERuleVersionInvalidValue),
            ("value", [1, 2], SERuleVersionInvalidValue),
            ("value", {"amount": "5"}, SERuleVersionInvalidValue),
        ],
    )
    def test_rejects_bad_values(self, field: str, value: object, error: type[Exception]) -> None:
        data: Dict[str, object] = {"valid_from": "2026-01-01", "valid_to": "2026-12-31", "value": "20"}
        data[field] = value
        with pytest.raises(error):
            RuleVersion.model_validate(data)

    @pytest.mark.parametrize("value", [datetime.date(2026, 1, 1), "2026-01-01"])
    def test_valid_from_is_accepted_as_a_date_or_an_iso_string(self, value: Union[datetime.date, str]) -> None:
        version = RuleVersion.model_validate({"valid_from": value, "value": "20"})
        assert version.valid_from == datetime.date(2026, 1, 1)

    @pytest.mark.parametrize("value", [datetime.date(2026, 12, 31), "2026-12-31"])
    def test_valid_to_is_accepted_as_a_date_or_an_iso_string(self, value: Union[datetime.date, str]) -> None:
        version = RuleVersion.model_validate({"valid_from": "2026-01-01", "valid_to": value, "value": "20"})
        assert version.valid_to == datetime.date(2026, 12, 31)

    @pytest.mark.parametrize(
        ("value", "expected"),
        [("20", Decimal("20")), (" 19.6 ", Decimal("19.6")), (20, Decimal("20")), (Decimal("7.5"), Decimal("7.5"))],
    )
    def test_a_value_is_an_exact_decimal(self, value: Union[str, int, Decimal], expected: Decimal) -> None:
        version = RuleVersion.model_validate({"valid_from": "2026-01-01", "value": value})
        assert isinstance(version.value, Decimal)
        assert version.value == expected
        assert str(version.value) == str(expected)

    def test_a_money_mapping_gives_a_money(self) -> None:
        version = RuleVersion.model_validate(
            {"valid_from": "2026-01-01", "value": {"amount": "5.50", "currency": "EUR"}}
        )
        assert isinstance(version.value, Money)
        assert isinstance(version.value.amount, Decimal)
        assert version.value.amount == Decimal("5.50")
        assert version.value.currency == "EUR"

    def test_a_valid_to_before_valid_from_is_refused(self) -> None:
        with pytest.raises(SERuleVersionEndsBeforeStart):
            RuleVersion.model_validate({"valid_from": "2026-06-01", "valid_to": "2026-05-31", "value": "20"})

    def test_a_valid_to_equal_to_valid_from_is_one_day_in_force(self) -> None:
        version = RuleVersion.model_validate({"valid_from": "2026-06-01", "valid_to": "2026-06-01", "value": "20"})
        assert version.valid_to == version.valid_from

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            RuleVersion.model_validate({"valid_from": "2026-01-01", "value": "20", "unknown": 1})

    def test_valid_from_is_required(self) -> None:
        with pytest.raises(ValidationError):
            RuleVersion.model_validate({"value": "20"})

    def test_a_version_cannot_be_changed_because_it_is_frozen(self) -> None:
        version = RuleVersion(valid_from=datetime.date(2026, 1, 1), value=Decimal("20"))
        with pytest.raises(ValidationError):
            version.valid_to = datetime.date(2026, 12, 31)

    @pytest.mark.parametrize(
        "value",
        [Decimal("19.6"), Money(amount=Decimal("5.50"), currency="EUR")],
        ids=["decimal", "money"],
    )
    def test_round_trip(self, value: Union[Money, Decimal]) -> None:
        version = RuleVersion(valid_from=datetime.date(2026, 1, 1), valid_to=datetime.date(2026, 12, 31), value=value)
        python_data: Dict[str, object] = version.model_dump()
        json_data: Dict[str, object] = version.model_dump(mode="json")
        assert RuleVersion.model_validate(python_data) == version
        assert RuleVersion.model_validate(json_data) == version
        assert RuleVersion.model_validate_json(version.model_dump_json()) == version
