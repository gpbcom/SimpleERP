from __future__ import annotations

import logging
from datetime import date
from typing import List, Tuple

import pytest
from erp_country_rules.models.exceptions import (
    SECountryPackNotFoundError,
    SECountryRuleNotFoundError,
    SECountryRuleNotInForceError,
    SECountryRulesError,
)


class TestRefusals:
    REFUSALS: List[Tuple[str, str, date, type[SECountryRulesError]]] = [
        ("standard-rate", "YY", date(2025, 1, 1), SECountryPackNotFoundError),
        ("standard-rate", "ZZZ", date(2025, 1, 1), SECountryPackNotFoundError),
        ("standard-rate", "../zz", date(2025, 1, 1), SECountryPackNotFoundError),
        ("no-such-rule", "ZZ", date(2025, 1, 1), SECountryRuleNotFoundError),
        ("standard-rate", "ZZ", date(2023, 12, 31), SECountryRuleNotInForceError),
        ("stamp-duty", "ZZ", date(2023, 12, 31), SECountryRuleNotInForceError),
    ]
    RULE_VALUES: List[str] = ["19.6", "20", "21", "0.10", "0.20"]

    @pytest.mark.parametrize("country", ["YY", "ZZZ", "../zz"])
    def test_an_unknown_or_malformed_country_is_refused(self, country_rules, country: str) -> None:
        with pytest.raises(SECountryPackNotFoundError):
            country_rules.value("standard-rate", country, date(2025, 1, 1))

    def test_a_rule_missing_from_the_pack_is_refused(self, country_rules) -> None:
        with pytest.raises(SECountryRuleNotFoundError):
            country_rules.value("no-such-rule", "ZZ", date(2025, 1, 1))

    @pytest.mark.parametrize("rule", ["standard-rate", "stamp-duty"])
    def test_a_date_before_the_first_version_is_refused(self, country_rules, rule: str) -> None:
        with pytest.raises(SECountryRuleNotInForceError):
            country_rules.value(rule, "ZZ", date(2023, 12, 31))

    @pytest.mark.parametrize(("rule", "country", "on", "error"), REFUSALS)
    def test_each_refusal_is_a_country_rules_error(
        self, country_rules, rule: str, country: str, on: date, error: type[SECountryRulesError]
    ) -> None:
        with pytest.raises(SECountryRulesError) as raised:
            country_rules.value(rule, country, on)
        assert isinstance(raised.value, error)

    @pytest.mark.parametrize(("rule", "country", "on", "error"), REFUSALS)
    def test_each_refusal_is_logged_at_error_without_a_rule_value(
        self,
        country_rules,
        caplog: pytest.LogCaptureFixture,
        rule: str,
        country: str,
        on: date,
        error: type[SECountryRulesError],
    ) -> None:
        with caplog.at_level(logging.DEBUG), pytest.raises(error):
            country_rules.value(rule, country, on)
        errors = [record for record in caplog.records if record.levelno == logging.ERROR]
        assert errors
        for record in errors:
            message = record.getMessage()
            assert not any(value in message for value in self.RULE_VALUES)
