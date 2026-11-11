from __future__ import annotations

import re
from pathlib import Path

import pytest
from pydantic import JsonValue

from ai_cost.models.commands.exceptions import (
    SEPaidCommandCatalogInvalidPaidCommands,
    SEPaidCommandCatalogUnreadable,
)
from ai_cost.models.commands.paid_command_catalog import PaidCommandCatalog


class TestPaidCommandCatalog:
    SKILL_DIR = Path(__file__).resolve().parents[3]

    def test_defaults(self) -> None:
        assert PaidCommandCatalog().paid_commands == []

    def test_full_valid_construction(self) -> None:
        catalog = PaidCommandCatalog.model_validate({"paid_commands": [{"name": "judge", "pattern": "judge"}]})
        assert catalog.paid_commands[0].name == "judge"

    def test_none_becomes_the_default(self) -> None:
        assert PaidCommandCatalog.model_validate({"paid_commands": None}).paid_commands == []

    @pytest.mark.parametrize("value", ["judge", {"name": "judge"}, 3])
    def test_rejects_bad_values(self, value: JsonValue) -> None:
        with pytest.raises(SEPaidCommandCatalogInvalidPaidCommands):
            PaidCommandCatalog.model_validate({"paid_commands": value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValueError, match="extra"):
            PaidCommandCatalog.model_validate({"paid_commands": [], "free_commands": []})

    def test_round_trip(self) -> None:
        catalog = PaidCommandCatalog.model_validate({"paid_commands": [{"name": "judge", "pattern": "judge"}]})
        assert PaidCommandCatalog.model_validate_json(catalog.model_dump_json()) == catalog

    def test_the_checked_in_catalogue_loads_and_leaves_pytest_to_the_gate(self) -> None:
        catalog = PaidCommandCatalog.load(self.SKILL_DIR / "conf" / "paid-commands.yaml")
        assert not any(re.search(r"pytest", entry.pattern) for entry in catalog.paid_commands)

    def test_a_missing_file_is_unreadable(self, tmp_path: Path) -> None:
        with pytest.raises(SEPaidCommandCatalogUnreadable):
            PaidCommandCatalog.load(tmp_path / "missing.yaml")
