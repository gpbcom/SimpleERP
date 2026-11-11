from __future__ import annotations

# Standard library imports
from typing import ClassVar

# Third-party imports
from pydantic import Field, JsonValue, field_validator

# First-party imports
from harness_core.models.catalogs.yaml_catalog import YamlCatalog
from pr_watch.models.configuration.commands_config import CommandsConfig
from pr_watch.models.configuration.exceptions import (
    SEWatchCatalogInvalidCommands,
    SEWatchCatalogInvalidGithub,
    SEWatchCatalogInvalidTiming,
    SEWatchCatalogUnreadable,
)
from pr_watch.models.configuration.github_config import GithubConfig
from pr_watch.models.configuration.timing_config import TimingConfig
from pr_watch.models.validation.field_rules import FieldRules


class WatchCatalog(YamlCatalog):
    """The watcher's configuration, kept in ``conf/watch.yaml``.

    Attributes:
        UNREADABLE (type[Exception]): Raised when the file cannot be read.
        timing (TimingConfig): How often the watcher runs and how long it waits.
        github (GithubConfig): How the watcher reads GitHub.
        commands (CommandsConfig): The desktop programs the watcher starts.

    Notes:
        Every value is written out in the file, so that nothing the watcher decides on is hidden in code.
    """

    UNREADABLE: ClassVar[type[Exception]] = SEWatchCatalogUnreadable

    timing: TimingConfig = Field(
        description="How often the watcher runs and how long it waits.",
        examples=[{"interval_minutes": 10, "renotify_minutes": 60, "qa_wait_minutes": 30, "operations_shown": 60}],
    )
    github: GithubConfig = Field(
        description="How the watcher reads GitHub.",
        examples=[
            {
                "api_url": "https://api.github.com",
                "api_version": "2022-11-28",
                "stage_workflow": "stage.yml",
                "environments": ["dev", "qa"],
                "qa_environment": "qa",
            }
        ],
    )
    commands: CommandsConfig = Field(
        description="The desktop programs the watcher starts.",
        examples=[
            {
                "claude": "claude",
                "vscode": "code",
                "opener": "xdg-open",
                "notifier": "notify-send",
                "terminal": "gnome-terminal",
            }
        ],
    )

    @field_validator("timing", mode="before")
    def validate_timing(cls, value: JsonValue) -> JsonValue:
        """Validate ``timing``.

        Args:
            value (JsonValue): The raw section.

        Returns:
            JsonValue: The section.

        Raises:
            SEWatchCatalogInvalidTiming: When the value is not a mapping of the section's fields.
        """
        return FieldRules.nested(value, SEWatchCatalogInvalidTiming, "timing")

    @field_validator("github", mode="before")
    def validate_github(cls, value: JsonValue) -> JsonValue:
        """Validate ``github``.

        Args:
            value (JsonValue): The raw section.

        Returns:
            JsonValue: The section.

        Raises:
            SEWatchCatalogInvalidGithub: When the value is not a mapping of the section's fields.
        """
        return FieldRules.nested(value, SEWatchCatalogInvalidGithub, "github")

    @field_validator("commands", mode="before")
    def validate_commands(cls, value: JsonValue) -> JsonValue:
        """Validate ``commands``.

        Args:
            value (JsonValue): The raw section.

        Returns:
            JsonValue: The section.

        Raises:
            SEWatchCatalogInvalidCommands: When the value is not a mapping of the section's fields.
        """
        return FieldRules.nested(value, SEWatchCatalogInvalidCommands, "commands")
