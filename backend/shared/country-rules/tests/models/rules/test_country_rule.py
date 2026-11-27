from __future__ import annotations

from datetime import date
from decimal import Decimal
from typing import Dict, List

import pytest
from erp_country_rules.models.exceptions import (
    SECountryRuleInvalidRule,
    SECountryRuleInvalidVersions,
    SECountryRuleOverlappingVersions,
    SEInvalidCountryRuleException,
)
from erp_country_rules.models.rules.country_rule import CountryRule
from pydantic import ValidationError


class TestCountryRule:
    def test_full_valid_construction(self) -> None:
        rule = CountryRule.model_validate(
            {
                "rule": "standard-rate",
                "versions": [
                    {"valid_from": "2024-01-01", "valid_to": "2025-12-31", "value": "19.6"},
                    {"valid_from": "2026-01-01", "valid_to": "2027-06-30", "value": "20"},
                    {"valid_from": "2027-07-01", "valid_to": None, "value": "21"},
                ],
            }
        )

        assert rule.rule == "standard-rate"
        assert [version.valid_from for version in rule.versions] == [
            date(2024, 1, 1),
            date(2026, 1, 1),
            date(2027, 7, 1),
        ]
        assert [version.valid_to for version in rule.versions] == [date(2025, 12, 31), date(2027, 6, 30), None]
        assert [version.value for version in rule.versions] == [Decimal("19.6"), Decimal("20"), Decimal("21")]

    def test_a_rule_name_is_stripped(self) -> None:
        rule = CountryRule.model_validate(
            {"rule": "  standard-rate  ", "versions": [{"valid_from": "2024-01-01", "value": "20"}]}
        )

        assert rule.rule == "standard-rate"

    @pytest.mark.parametrize(
        ("name", "error"),
        [("rule", SECountryRuleInvalidRule), ("versions", SECountryRuleInvalidVersions)],
    )
    def test_none_is_refused_with_its_own_exception(self, name: str, error: type[Exception]) -> None:
        values: Dict[str, object] = {
            "rule": "standard-rate",
            "versions": [{"valid_from": "2024-01-01", "value": "20"}],
        }
        values[name] = None

        with pytest.raises(error):
            CountryRule.model_validate(values)

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("rule", 12, SECountryRuleInvalidRule),
            ("rule", True, SECountryRuleInvalidRule),
            ("rule", ["standard-rate"], SECountryRuleInvalidRule),
            ("rule", "", SECountryRuleInvalidRule),
            ("rule", "   ", SECountryRuleInvalidRule),
            ("versions", "2024-01-01", SECountryRuleInvalidVersions),
            ("versions", 3, SECountryRuleInvalidVersions),
            ("versions", {"valid_from": "2024-01-01", "value": "20"}, SECountryRuleInvalidVersions),
            ("versions", [], SECountryRuleInvalidVersions),
            ("versions", ["2024-01-01"], SECountryRuleInvalidVersions),
            ("versions", [None], SECountryRuleInvalidVersions),
            ("versions", [{"valid_from": "2024-01-01", "value": "20"}, 5], SECountryRuleInvalidVersions),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: object, error: type[Exception]) -> None:
        values: Dict[str, object] = {
            "rule": "standard-rate",
            "versions": [{"valid_from": "2024-01-01", "value": "20"}],
        }
        values[name] = value

        with pytest.raises(error):
            CountryRule.model_validate(values)

    @pytest.mark.parametrize(
        "versions",
        [
            [
                {"valid_from": "2024-01-01", "valid_to": "2025-12-31", "value": "19"},
                {"valid_from": "2025-12-31", "valid_to": "2026-12-31", "value": "20"},
            ],
            [
                {"valid_from": "2024-01-01", "valid_to": "2026-12-31", "value": "19"},
                {"valid_from": "2025-06-01", "valid_to": "2025-12-31", "value": "20"},
            ],
            [
                {"valid_from": "2026-01-01", "valid_to": "2026-12-31", "value": "20"},
                {"valid_from": "2024-01-01", "valid_to": "2025-12-31", "value": "19"},
            ],
            [
                {"valid_from": "2024-01-01", "valid_to": None, "value": "19"},
                {"valid_from": "2026-01-01", "valid_to": None, "value": "20"},
            ],
            [
                {"valid_from": "2024-01-01", "value": "19"},
                {"valid_from": "2026-01-01", "valid_to": "2026-12-31", "value": "20"},
            ],
        ],
        ids=["same day", "contained", "not ascending", "open-ended then open-ended", "open-ended then later"],
    )
    def test_versions_that_overlap_are_refused(self, versions: List[Dict[str, object]]) -> None:
        with pytest.raises(SECountryRuleOverlappingVersions):
            CountryRule.model_validate({"rule": "standard-rate", "versions": versions})

    @pytest.mark.parametrize(
        "versions",
        [
            [
                {"valid_from": "2024-01-01", "valid_to": "2025-12-31", "value": "19"},
                {"valid_from": "2026-01-01", "valid_to": None, "value": "20"},
            ],
            [
                {"valid_from": "2024-01-01", "valid_to": "2024-12-31", "value": "19"},
                {"valid_from": "2026-01-01", "valid_to": None, "value": "20"},
            ],
        ],
        ids=["adjacent", "gap"],
    )
    def test_adjacent_versions_and_gaps_are_accepted(self, versions: List[Dict[str, object]]) -> None:
        rule = CountryRule.model_validate({"rule": "standard-rate", "versions": versions})

        assert len(rule.versions) == 2

    @pytest.mark.parametrize(
        "error",
        [SECountryRuleInvalidRule, SECountryRuleInvalidVersions, SECountryRuleOverlappingVersions],
    )
    def test_the_exceptions_share_the_model_base(self, error: type[Exception]) -> None:
        assert issubclass(error, SEInvalidCountryRuleException)

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            CountryRule.model_validate(
                {
                    "rule": "standard-rate",
                    "versions": [{"valid_from": "2024-01-01", "value": "20"}],
                    "extra": 1,
                }
            )

    def test_a_country_rule_cannot_be_changed(self) -> None:
        rule = CountryRule.model_validate(
            {"rule": "standard-rate", "versions": [{"valid_from": "2024-01-01", "value": "20"}]}
        )

        with pytest.raises(ValidationError):
            rule.rule = "reduced-rate"

    def test_round_trip(self) -> None:
        rule = CountryRule.model_validate(
            {
                "rule": "standard-rate",
                "versions": [
                    {"valid_from": "2024-01-01", "valid_to": "2025-12-31", "value": "19.6"},
                    {"valid_from": "2026-01-01", "valid_to": None, "value": {"amount": "20.00", "currency": "EUR"}},
                ],
            }
        )

        dumped = rule.model_dump(mode="json")
        assert CountryRule.model_validate(dumped) == rule
        assert CountryRule.model_validate_json(rule.model_dump_json()) == rule
