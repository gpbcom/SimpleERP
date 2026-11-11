from __future__ import annotations

from decimal import Decimal
from pathlib import Path
from typing import Dict

import pytest
from pydantic import JsonValue

from ai_cost.models.enums import UsageSource
from ai_cost.models.settings.exceptions import (
    SEGuardSettingsInvalidNumber,
    SEGuardSettingsInvalidPath,
    SEGuardSettingsInvalidUsageSource,
    SEGuardSettingsUnreadable,
)
from ai_cost.models.settings.guard_settings import GuardSettings


class TestGuardSettings:
    SKILL_DIR = Path(__file__).resolve().parents[3]

    def settings_fields(self, tmp_path: Path) -> Dict[str, JsonValue]:
        return {
            "state_dir": str(tmp_path / "state"),
            "prices_file": "conf/prices.yaml",
            "paid_commands_file": str(tmp_path / "paid.yaml"),
            "cost_template_file": "templates/COST.md",
            "default_cap_usd": "15",
            "kill_ratio": "0.8",
            "poll_interval_s": 5,
            "settle_s": 0,
            "max_unmeasured": 3,
            "usage_source": "estimate",
        }

    def test_defaults(self) -> None:
        settings = GuardSettings.load(self.SKILL_DIR / "conf" / "settings.yaml")
        assert settings.state_dir == Path.home() / ".local" / "state" / "ai-test-cost"
        assert settings.prices_file == self.SKILL_DIR / "conf" / "prices.yaml"
        assert settings.paid_commands_file == self.SKILL_DIR / "conf" / "paid-commands.yaml"
        assert settings.cost_template_file == self.SKILL_DIR / "templates" / "COST.md"
        assert (settings.default_cap_usd, settings.kill_ratio) == (Decimal("20"), Decimal("0.9"))
        assert (settings.poll_interval_s, settings.settle_s, settings.max_unmeasured) == (60, 300, 3)
        assert settings.usage_source is UsageSource.ANTHROPIC

    def test_full_valid_construction(self, tmp_path: Path) -> None:
        settings = GuardSettings.model_validate(self.settings_fields(tmp_path))
        assert settings.state_dir == tmp_path / "state"
        assert settings.prices_file == self.SKILL_DIR / "conf" / "prices.yaml"
        assert settings.default_cap_usd == Decimal("15")
        assert settings.usage_source is UsageSource.ESTIMATE

    def test_the_environment_cannot_loosen_the_guard(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("AI_COST_DEFAULT_CAP_USD", "1000")
        monkeypatch.setenv("AI_COST_KILL_RATIO", "1")
        monkeypatch.setenv("AI_COST_USAGE_SOURCE", "estimate")
        monkeypatch.setenv("AI_COST_STATE_DIR", str(tmp_path))
        settings = GuardSettings.load(self.SKILL_DIR / "conf" / "settings.yaml")
        assert (settings.default_cap_usd, settings.kill_ratio, settings.usage_source) == (
            Decimal("20"),
            Decimal("0.9"),
            UsageSource.ANTHROPIC,
        )
        assert settings.state_dir != tmp_path

    @pytest.mark.parametrize("name", ["state_dir", "default_cap_usd", "usage_source", "max_unmeasured"])
    def test_none_becomes_the_default(self, tmp_path: Path, name: str) -> None:
        fields = self.settings_fields(tmp_path)
        fields[name] = None
        with pytest.raises(
            (SEGuardSettingsInvalidPath, SEGuardSettingsInvalidNumber, SEGuardSettingsInvalidUsageSource)
        ):
            GuardSettings.model_validate(fields)

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("state_dir", "", SEGuardSettingsInvalidPath),
            ("prices_file", 3, SEGuardSettingsInvalidPath),
            ("default_cap_usd", "0", SEGuardSettingsInvalidNumber),
            ("kill_ratio", "1.5", SEGuardSettingsInvalidNumber),
            ("kill_ratio", True, SEGuardSettingsInvalidNumber),
            ("poll_interval_s", 0, SEGuardSettingsInvalidNumber),
            ("settle_s", "soon", SEGuardSettingsInvalidNumber),
            ("settle_s", 1.5, SEGuardSettingsInvalidNumber),
            ("max_unmeasured", 0, SEGuardSettingsInvalidNumber),
            ("usage_source", "bedrock", SEGuardSettingsInvalidUsageSource),
        ],
    )
    def test_rejects_bad_values(self, tmp_path: Path, name: str, value: JsonValue, error: type[Exception]) -> None:
        fields = self.settings_fields(tmp_path)
        fields[name] = value
        with pytest.raises(error):
            GuardSettings.model_validate(fields)

    def test_rejects_unknown_keys(self, tmp_path: Path) -> None:
        with pytest.raises(ValueError, match="extra"):
            GuardSettings.model_validate({**self.settings_fields(tmp_path), "aws_profile": "test"})

    def test_round_trip(self, tmp_path: Path) -> None:
        settings = GuardSettings.model_validate(self.settings_fields(tmp_path))
        assert GuardSettings.model_validate(settings.model_dump()) == settings

    def test_a_missing_file_is_unreadable(self, tmp_path: Path) -> None:
        with pytest.raises(SEGuardSettingsUnreadable):
            GuardSettings.load(tmp_path / "missing.yaml")
