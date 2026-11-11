from __future__ import annotations

from pathlib import Path

import pytest
from pydantic import JsonValue, ValidationError

from pr_watch.models.configuration.exceptions import (
    SEWatchSettingsInvalidCallerCwd,
    SEWatchSettingsInvalidClaudeHome,
    SEWatchSettingsInvalidCostStateDir,
    SEWatchSettingsInvalidSkillDir,
    SEWatchSettingsInvalidStateDir,
)
from pr_watch.models.configuration.watch_settings import WatchSettings


class TestWatchSettings:
    @pytest.fixture(autouse=True)
    def clean_environment(self, monkeypatch: pytest.MonkeyPatch) -> None:
        for name in ("STATE_DIR", "CLAUDE_HOME", "CALLER_CWD", "SKILL_DIR"):
            monkeypatch.delenv(f"PR_WATCH_{name}", raising=False)
        monkeypatch.delenv("AI_COST_STATE_DIR", raising=False)

    def test_defaults(self) -> None:
        settings = WatchSettings()
        assert settings.state_dir == Path.home() / ".local" / "state" / "claude-pr-watch"
        assert settings.cost_state_dir == Path.home() / ".local" / "state" / "ai-test-cost"
        assert settings.claude_home == Path.home() / ".claude"
        assert settings.caller_cwd == Path.cwd()
        assert settings.catalog_file.exists()
        assert settings.catalog_file.name == "watch.yaml"
        assert settings.template_file.name == "PR-SUMMARY.md"
        assert settings.units_dir.name == "systemd"

    def test_full_valid_construction(self, tmp_path: Path) -> None:
        settings = WatchSettings(
            state_dir=tmp_path / "state",
            cost_state_dir=str(tmp_path / "costs"),
            claude_home=tmp_path / "claude",
            caller_cwd=tmp_path,
            skill_dir=tmp_path / "skill",
        )
        assert settings.cost_state_dir == tmp_path / "costs"
        assert settings.catalog_file == tmp_path / "skill" / "conf" / "watch.yaml"

    def test_the_environment_overrides_the_defaults(self, monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
        monkeypatch.setenv("PR_WATCH_STATE_DIR", str(tmp_path / "state"))
        monkeypatch.setenv("AI_COST_STATE_DIR", str(tmp_path / "costs"))
        monkeypatch.setenv("PR_WATCH_CALLER_CWD", str(tmp_path))
        settings = WatchSettings()
        assert (settings.state_dir, settings.cost_state_dir, settings.caller_cwd) == (
            tmp_path / "state",
            tmp_path / "costs",
            tmp_path,
        )

    @pytest.mark.parametrize("name", ["state_dir", "cost_state_dir", "claude_home", "caller_cwd", "skill_dir"])
    def test_none_becomes_the_default(self, name: str) -> None:
        assert getattr(WatchSettings(**{name: None}), name) == getattr(WatchSettings(), name)

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("state_dir", "", SEWatchSettingsInvalidStateDir),
            ("cost_state_dir", 3, SEWatchSettingsInvalidCostStateDir),
            ("claude_home", " ", SEWatchSettingsInvalidClaudeHome),
            ("caller_cwd", [], SEWatchSettingsInvalidCallerCwd),
            ("skill_dir", True, SEWatchSettingsInvalidSkillDir),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            WatchSettings(**{name: value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            WatchSettings(surprise=1)

    def test_round_trip(self, tmp_path: Path) -> None:
        settings = WatchSettings(state_dir=tmp_path)
        assert WatchSettings.model_validate_json(settings.model_dump_json()) == settings
