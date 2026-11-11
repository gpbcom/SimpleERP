from __future__ import annotations

from typing import ClassVar, Dict

import pytest
from pydantic import JsonValue, ValidationError

from pr_watch.models.configuration.commands_config import CommandsConfig
from pr_watch.models.configuration.exceptions import (
    SECommandsConfigInvalidClaude,
    SECommandsConfigInvalidNotifier,
    SECommandsConfigInvalidOpener,
    SECommandsConfigInvalidTerminal,
    SECommandsConfigInvalidVscode,
)


class TestCommandsConfig:
    REQUIRED: ClassVar[Dict[str, JsonValue]] = {
        "claude": "claude",
        "vscode": "code",
        "opener": "xdg-open",
        "notifier": "notify-send",
        "terminal": "gnome-terminal",
    }
    FULL: ClassVar[Dict[str, JsonValue]] = {
        "claude": "claude",
        "vscode": "code",
        "opener": "xdg-open",
        "notifier": "notify-send",
        "terminal": "gnome-terminal",
    }

    def test_defaults(self) -> None:
        model = CommandsConfig(**self.REQUIRED)
        assert CommandsConfig.model_validate(model.model_dump()) == model

    def test_full_valid_construction(self) -> None:
        model = CommandsConfig(**self.FULL)
        assert model.opener == "xdg-open"

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("claude", "", SECommandsConfigInvalidClaude),
            ("claude", None, SECommandsConfigInvalidClaude),
            ("vscode", " ", SECommandsConfigInvalidVscode),
            ("vscode", 1, SECommandsConfigInvalidVscode),
            ("opener", "", SECommandsConfigInvalidOpener),
            ("opener", [], SECommandsConfigInvalidOpener),
            ("notifier", "", SECommandsConfigInvalidNotifier),
            ("notifier", None, SECommandsConfigInvalidNotifier),
            ("terminal", "", SECommandsConfigInvalidTerminal),
            ("terminal", False, SECommandsConfigInvalidTerminal),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            CommandsConfig(**{**self.FULL, name: value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            CommandsConfig(**self.FULL, surprise=1)

    def test_round_trip(self) -> None:
        model = CommandsConfig(**self.FULL)
        assert CommandsConfig.model_validate_json(model.model_dump_json()) == model
