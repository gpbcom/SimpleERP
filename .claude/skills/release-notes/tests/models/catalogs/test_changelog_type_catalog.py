from __future__ import annotations

from pathlib import Path
from typing import Dict

import pytest
from pydantic import JsonValue, ValidationError

from release_notes.models.catalogs.changelog_type_catalog import ChangelogTypeCatalog
from release_notes.models.catalogs.exceptions import (
    SEChangelogTypeCatalogInvalidBreakingMarker,
    SEChangelogTypeCatalogInvalidTypes,
    SEChangelogTypeCatalogUnreadable,
    SEChangelogTypeInvalidName,
)
from release_notes.models.enums import VersionBump
from tests.helpers import TYPES_FILE


class TestChangelogTypeCatalog:
    def valid(self) -> Dict[str, JsonValue]:
        return {
            "types": [
                {"name": "added", "heading": "Added", "bump": "minor"},
                {"name": "fixed", "heading": "Fixed", "bump": "patch"},
            ],
            "breaking_marker": "**Breaking:**",
        }

    def test_defaults(self) -> None:
        catalog = ChangelogTypeCatalog.model_validate(self.valid())
        assert catalog.names() == ["added", "fixed"]

    def test_full_valid_construction(self) -> None:
        catalog = ChangelogTypeCatalog.model_validate(self.valid())
        fixed = catalog.named("fixed")
        assert fixed is not None
        assert fixed.bump == VersionBump.PATCH
        assert catalog.named("security") is None
        assert catalog.breaking_marker == "**Breaking:**"

    @pytest.mark.parametrize("name", ["types", "breaking_marker"])
    def test_none_becomes_the_default(self, name: str) -> None:
        with pytest.raises((SEChangelogTypeCatalogInvalidTypes, SEChangelogTypeCatalogInvalidBreakingMarker)):
            ChangelogTypeCatalog.model_validate({**self.valid(), name: None})

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("types", [], SEChangelogTypeCatalogInvalidTypes),
            ("types", "added", SEChangelogTypeCatalogInvalidTypes),
            (
                "types",
                [
                    {"name": "added", "heading": "Added", "bump": "minor"},
                    {"name": "added", "heading": "A", "bump": "patch"},
                ],
                SEChangelogTypeCatalogInvalidTypes,
            ),
            ("types", [{"name": "Added", "heading": "Added", "bump": "minor"}], SEChangelogTypeInvalidName),
            ("breaking_marker", "", SEChangelogTypeCatalogInvalidBreakingMarker),
            ("breaking_marker", 1, SEChangelogTypeCatalogInvalidBreakingMarker),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            ChangelogTypeCatalog.model_validate({**self.valid(), name: value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            ChangelogTypeCatalog.model_validate({**self.valid(), "order": []})

    def test_round_trip(self) -> None:
        catalog = ChangelogTypeCatalog.model_validate(self.valid())
        assert ChangelogTypeCatalog.model_validate(catalog.model_dump()) == catalog

    def test_the_versioned_catalogue_loads_in_keep_a_changelog_order(self) -> None:
        catalog = ChangelogTypeCatalog.load(TYPES_FILE)
        assert catalog.names() == ["added", "changed", "deprecated", "removed", "fixed", "security"]
        assert catalog.breaking_marker == "**Breaking:**"

    def test_a_missing_file_is_unreadable(self, tmp_path: Path) -> None:
        with pytest.raises(SEChangelogTypeCatalogUnreadable):
            ChangelogTypeCatalog.load(tmp_path / "changelog-types.yaml")
