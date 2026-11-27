from __future__ import annotations

from datetime import date
from decimal import Decimal
from pathlib import Path
from typing import Dict, List, Type

import pytest
from erp_country_rules.models.exceptions import (
    SECountryPackInvalidCountry,
    SECountryPackInvalidRules,
    SECountryPackInvalidVersion,
    SECountryPackUnreadable,
)
from erp_country_rules.models.packs.country_pack import CountryPack
from erp_models.money.money import Money
from pydantic import JsonValue, ValidationError


class TestCountryPack:
    def rule(self, name: str = "standard-rate", value: JsonValue = "20") -> Dict[str, JsonValue]:
        return {"rule": name, "versions": [{"valid_from": "2026-01-01", "value": value}]}

    def valid(self) -> Dict[str, JsonValue]:
        rules: List[JsonValue] = [
            self.rule("standard-rate", "20"),
            self.rule("minimum-wage", {"amount": "11.88", "currency": "EUR"}),
        ]
        return {"country": "ZZ", "version": "2026.11", "rules": rules}

    def test_full_valid_construction(self) -> None:
        pack = CountryPack.model_validate(self.valid())
        assert pack.country == "ZZ"
        assert pack.version == "2026.11"
        assert [rule.rule for rule in pack.rules] == ["standard-rate", "minimum-wage"]

    def test_country_and_version_are_stripped(self) -> None:
        pack = CountryPack.model_validate({**self.valid(), "country": " ZZ ", "version": " 2026.11 "})
        assert (pack.country, pack.version) == ("ZZ", "2026.11")

    @pytest.mark.parametrize(
        ("name", "error"),
        [
            ("country", SECountryPackInvalidCountry),
            ("version", SECountryPackInvalidVersion),
            ("rules", SECountryPackInvalidRules),
        ],
    )
    def test_every_required_field_is_refused_when_none(self, name: str, error: Type[Exception]) -> None:
        with pytest.raises(error):
            CountryPack.model_validate({**self.valid(), name: None})

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("country", 12, SECountryPackInvalidCountry),
            ("country", True, SECountryPackInvalidCountry),
            ("country", ["ZZ"], SECountryPackInvalidCountry),
            ("country", "", SECountryPackInvalidCountry),
            ("country", "   ", SECountryPackInvalidCountry),
            ("country", "Z", SECountryPackInvalidCountry),
            ("country", "F", SECountryPackInvalidCountry),
            ("country", "FRA", SECountryPackInvalidCountry),
            ("country", "fr", SECountryPackInvalidCountry),
            ("country", "1A", SECountryPackInvalidCountry),
            ("version", 2026.11, SECountryPackInvalidVersion),
            ("version", 2026, SECountryPackInvalidVersion),
            ("version", True, SECountryPackInvalidVersion),
            ("version", ["2026.11"], SECountryPackInvalidVersion),
            ("version", "", SECountryPackInvalidVersion),
            ("version", "   ", SECountryPackInvalidVersion),
            ("rules", "standard-rate", SECountryPackInvalidRules),
            ("rules", {"rule": "standard-rate"}, SECountryPackInvalidRules),
            ("rules", [], SECountryPackInvalidRules),
            ("rules", [1], SECountryPackInvalidRules),
            (
                "rules",
                [
                    {"rule": "standard-rate", "versions": [{"valid_from": "2026-01-01", "value": "20"}]},
                    {"rule": "standard-rate", "versions": [{"valid_from": "2026-01-01", "value": "21"}]},
                ],
                SECountryPackInvalidRules,
            ),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: Type[Exception]) -> None:
        with pytest.raises(error):
            CountryPack.model_validate({**self.valid(), name: value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            CountryPack.model_validate({**self.valid(), "unknown": 1})

    def test_is_frozen(self) -> None:
        pack = CountryPack.model_validate(self.valid())
        with pytest.raises(ValidationError):
            pack.country = "YY"

    def test_round_trip(self) -> None:
        pack = CountryPack.model_validate(self.valid())
        assert CountryPack.model_validate(pack.model_dump()) == pack
        assert CountryPack.model_validate(pack.model_dump(mode="json")) == pack

    def test_a_yaml_file_loads_into_the_expected_pack(self, tmp_path: Path) -> None:
        path = tmp_path / "zz.yaml"
        path.write_text(
            "country: ZZ\n"
            'version: "2026.11"\n'
            "rules:\n"
            "  - rule: standard-rate\n"
            "    versions:\n"
            "      - valid_from: 2024-01-01\n"
            "        valid_to: 2025-12-31\n"
            '        value: "19.6"\n'
            "      - valid_from: 2026-01-01\n"
            '        value: "20"\n'
            "  - rule: minimum-wage\n"
            "    versions:\n"
            "      - valid_from: 2026-01-01\n"
            "        value:\n"
            '          amount: "11.88"\n'
            "          currency: EUR\n",
            encoding="utf-8",
        )
        pack = CountryPack.load(path)
        assert (pack.country, pack.version) == ("ZZ", "2026.11")
        standard, wage = pack.rules
        assert standard.versions[0].valid_from == date(2024, 1, 1)
        assert standard.versions[0].valid_to == date(2025, 12, 31)
        assert standard.versions[0].value == Decimal("19.6")
        assert standard.versions[1].valid_to is None
        assert wage.versions[0].value == Money(amount=Decimal("11.88"), currency="EUR")

    def test_a_numeric_version_in_a_file_is_refused(self, tmp_path: Path) -> None:
        path = tmp_path / "zz.yaml"
        path.write_text(
            "country: ZZ\nversion: 2026.11\nrules:\n"
            "  - rule: standard-rate\n    versions:\n      - valid_from: 2026-01-01\n        value: '20'\n",
            encoding="utf-8",
        )
        with pytest.raises(SECountryPackInvalidVersion):
            CountryPack.load(path)

    def test_a_missing_file_is_unreadable(self, tmp_path: Path) -> None:
        with pytest.raises(SECountryPackUnreadable):
            CountryPack.load(tmp_path / "missing.yaml")

    def test_a_malformed_yaml_file_is_unreadable(self, tmp_path: Path) -> None:
        path = tmp_path / "bad.yaml"
        path.write_text("country: [ZZ\nrules: {", encoding="utf-8")
        with pytest.raises(SECountryPackUnreadable):
            CountryPack.load(path)
