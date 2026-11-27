from __future__ import annotations

from pathlib import Path
from typing import Dict

import pytest
from erp_country_rules.models.config.country_rules_config import CountryRulesConfig
from erp_country_rules.models.exceptions import SECountryRulesConfigInvalidPacksDir
from pydantic import JsonValue, ValidationError


class TestCountryRulesConfig:
    def test_defaults(self) -> None:
        assert CountryRulesConfig().packs_dir == Path("packs/countries")

    @pytest.mark.parametrize(
        ("value", "expected"),
        [
            ("/srv/packs", Path("/srv/packs")),
            (Path("/srv/packs"), Path("/srv/packs")),
            ("  /srv/packs  ", Path("/srv/packs")),
        ],
    )
    def test_full_valid_construction(self, value: object, expected: Path) -> None:
        config = CountryRulesConfig.model_validate({"packs_dir": value})
        assert config.packs_dir == expected
        assert isinstance(config.packs_dir, Path)

    @pytest.mark.parametrize("name", ["packs_dir"])
    def test_none_becomes_the_default(self, name: str) -> None:
        config = CountryRulesConfig.model_validate({name: None})
        assert getattr(config, name) == CountryRulesConfig.model_fields[name].get_default()

    @pytest.mark.parametrize("value", ["", "   ", True, False, 42, ["packs"]])
    def test_rejects_bad_values(self, value: JsonValue) -> None:
        with pytest.raises(SECountryRulesConfigInvalidPacksDir):
            CountryRulesConfig.model_validate({"packs_dir": value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            CountryRulesConfig.model_validate({"unknown": 1})

    def test_assignment_is_refused_because_the_model_is_frozen(self) -> None:
        config = CountryRulesConfig()
        with pytest.raises(ValidationError):
            config.packs_dir = Path("other")

    def test_round_trip(self) -> None:
        config = CountryRulesConfig(packs_dir=Path("/srv/packs"))
        data: Dict[str, Path] = config.model_dump()
        assert CountryRulesConfig.model_validate(data) == config
        json_data = config.model_dump(mode="json")
        assert json_data == {"packs_dir": "/srv/packs"}
        assert CountryRulesConfig.model_validate(json_data) == config
        assert CountryRulesConfig.model_validate_json(config.model_dump_json()) == config
