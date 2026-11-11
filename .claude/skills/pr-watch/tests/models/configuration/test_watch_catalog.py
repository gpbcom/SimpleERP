from __future__ import annotations

from pathlib import Path
from typing import ClassVar, Dict

import pytest
from pydantic import JsonValue, ValidationError

from pr_watch.models.configuration.exceptions import (
    SEWatchCatalogInvalidCommands,
    SEWatchCatalogInvalidGithub,
    SEWatchCatalogInvalidTiming,
    SEWatchCatalogUnreadable,
)
from pr_watch.models.configuration.watch_catalog import WatchCatalog
from pr_watch.models.configuration.watch_settings import WatchSettings


class TestWatchCatalog:
    FULL: ClassVar[Dict[str, JsonValue]] = {
        "timing": {"interval_minutes": 10, "renotify_minutes": 60, "qa_wait_minutes": 30, "operations_shown": 60},
        "github": {
            "api_url": "https://api.github.com",
            "api_version": "2022-11-28",
            "stage_workflow": "stage.yml",
            "environments": ["dev", "qa"],
            "qa_environment": "qa",
        },
        "commands": {
            "claude": "claude",
            "vscode": "code",
            "opener": "xdg-open",
            "notifier": "notify-send",
            "terminal": "gnome-terminal",
        },
    }

    def test_defaults(self) -> None:
        catalog = WatchCatalog.load(WatchSettings().catalog_file)
        assert catalog.timing.interval_minutes == 10
        assert catalog.github.stage_workflow == "stage.yml"
        assert catalog.github.environments == ["dev", "qa"]
        assert catalog.commands.opener == "xdg-open"

    def test_full_valid_construction(self) -> None:
        assert WatchCatalog(**self.FULL) == WatchCatalog.load(WatchSettings().catalog_file)

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("timing", None, SEWatchCatalogInvalidTiming),
            ("github", "github", SEWatchCatalogInvalidGithub),
            ("commands", [], SEWatchCatalogInvalidCommands),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            WatchCatalog(**{**self.FULL, name: value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            WatchCatalog(**self.FULL, surprise=1)

    def test_round_trip(self) -> None:
        catalog = WatchCatalog(**self.FULL)
        assert WatchCatalog.model_validate_json(catalog.model_dump_json()) == catalog

    def test_a_missing_file_raises_the_catalogues_own_error(self, tmp_path: Path) -> None:
        with pytest.raises(SEWatchCatalogUnreadable):
            WatchCatalog.load(tmp_path / "missing.yaml")
