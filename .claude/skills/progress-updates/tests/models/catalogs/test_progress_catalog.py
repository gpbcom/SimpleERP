from __future__ import annotations

from pathlib import Path
from typing import ClassVar

import pytest
from pydantic import JsonValue

from progress_updates.models.catalogs.exceptions import (
    SEProgressCatalogInvalidEvidenceMax,
    SEProgressCatalogInvalidHealthIcons,
    SEProgressCatalogInvalidIntervalS,
    SEProgressCatalogInvalidLineMaxChars,
    SEProgressCatalogInvalidStateIcons,
    SEProgressCatalogUnreadable,
)
from progress_updates.models.catalogs.progress_catalog import ProgressCatalog
from progress_updates.models.enums import TaskState


class TestProgressCatalog:
    ICONS: ClassVar[dict[str, str]] = {"done": "✅", "running": "🔄", "waiting": "⏳", "failed": "❌", "warning": "⚠️"}
    HEALTH: ClassVar[dict[str, str]] = {"done": "🟢", "running": "🟢", "waiting": "🟡", "failed": "🔴", "warning": "🟡"}

    @pytest.fixture
    def catalog(self, skill_root: Path) -> ProgressCatalog:
        return ProgressCatalog.load(skill_root / "conf" / "progress-updates.yaml")

    def _valid(self) -> dict[str, JsonValue]:
        return {
            "interval_s": 120,
            "line_max_chars": 160,
            "evidence_max": 5,
            "state_icons": dict(self.ICONS),
            "health_icons": dict(self.HEALTH),
        }

    def test_the_shipped_catalogue_reports_every_2_minutes(self, catalog: ProgressCatalog) -> None:
        assert catalog.interval_s == 120

    def test_the_shipped_catalogue_has_an_icon_and_a_health_per_state(self, catalog: ProgressCatalog) -> None:
        assert set(catalog.state_icons) == {state.value for state in TaskState}
        assert set(catalog.health_icons) == {state.value for state in TaskState}

    def test_full_valid_construction(self) -> None:
        catalog = ProgressCatalog.model_validate(self._valid())
        assert catalog.state_icons["failed"] == "❌"
        assert catalog.health_icons["failed"] == "🔴"

    def test_defaults(self) -> None:
        catalog = ProgressCatalog.model_validate({"state_icons": dict(self.ICONS), "health_icons": dict(self.HEALTH)})
        assert (catalog.interval_s, catalog.line_max_chars, catalog.evidence_max) == (120, 160, 5)

    @pytest.mark.parametrize("name", ["interval_s", "line_max_chars", "evidence_max"])
    def test_none_becomes_the_default(self, name: str) -> None:
        fields = self._valid()
        fields[name] = None
        assert getattr(ProgressCatalog.model_validate(fields), name) == self._valid()[name]

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("interval_s", 60, SEProgressCatalogInvalidIntervalS),
            ("interval_s", 119, SEProgressCatalogInvalidIntervalS),
            ("interval_s", True, SEProgressCatalogInvalidIntervalS),
            ("interval_s", "120", SEProgressCatalogInvalidIntervalS),
            ("line_max_chars", 10, SEProgressCatalogInvalidLineMaxChars),
            ("evidence_max", -1, SEProgressCatalogInvalidEvidenceMax),
            ("state_icons", {"done": "✅"}, SEProgressCatalogInvalidStateIcons),
            ("state_icons", {"done": "✅", "running": " "}, SEProgressCatalogInvalidStateIcons),
            ("health_icons", None, SEProgressCatalogInvalidHealthIcons),
            ("health_icons", {"other": "🟣"}, SEProgressCatalogInvalidHealthIcons),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        fields = self._valid()
        fields[name] = value
        with pytest.raises(error):
            ProgressCatalog.model_validate(fields)

    def test_a_blank_icon_is_refused(self) -> None:
        with pytest.raises(SEProgressCatalogInvalidStateIcons):
            ProgressCatalog.model_validate({**self._valid(), "state_icons": {**self.ICONS, "running": " "}})

    def test_an_icon_for_an_unknown_state_is_refused(self) -> None:
        with pytest.raises(SEProgressCatalogInvalidHealthIcons):
            ProgressCatalog.model_validate({**self._valid(), "health_icons": {**self.HEALTH, "other": "🟣"}})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValueError, match="extra"):
            ProgressCatalog.model_validate({**self._valid(), "other": 1})

    def test_a_missing_file_is_unreadable(self, tmp_path: Path) -> None:
        with pytest.raises(SEProgressCatalogUnreadable):
            ProgressCatalog.load(tmp_path / "missing.yaml")

    def test_round_trip(self) -> None:
        catalog = ProgressCatalog.model_validate(self._valid())
        assert ProgressCatalog.model_validate(catalog.model_dump()) == catalog
