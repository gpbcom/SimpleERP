from __future__ import annotations

# Standard library imports
from pathlib import Path

# Third-party imports
import pytest

# First-party imports
from erp_country_rules.models.config.country_rules_config import CountryRulesConfig
from erp_country_rules.service.rules.country_rules import CountryRules
from erp_country_rules.storage.packs.country_pack_repository import CountryPackRepository


@pytest.fixture
def country_rules() -> CountryRules:
    return CountryRules(CountryPackRepository(CountryRulesConfig(packs_dir=Path(__file__).parent / "packs")))
