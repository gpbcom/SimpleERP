from __future__ import annotations

# Standard library imports
from pathlib import Path
from typing import ClassVar

# Third-party imports
from pydantic import AliasChoices, Field, JsonValue, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

# First-party imports
from pr_watch.models.configuration.exceptions import (
    SEWatchSettingsInvalidCallerCwd,
    SEWatchSettingsInvalidClaudeHome,
    SEWatchSettingsInvalidCostStateDir,
    SEWatchSettingsInvalidSkillDir,
    SEWatchSettingsInvalidStateDir,
)
from pr_watch.models.validation.field_rules import FieldRules


class WatchSettings(BaseSettings):
    """Where the pull request watcher reads and writes, each folder overridable by an environment variable.

    Attributes:
        SKILL_DIR (Path): The skill's folder, which holds ``conf/``, ``templates/`` and ``systemd/``.
        state_dir (Path): The watcher's state: registry, memory, inboxes, operations and log (``PR_WATCH_STATE_DIR``).
        cost_state_dir (Path): The ai-test-cost ledgers, read for the cost column (``AI_COST_STATE_DIR``).
        claude_home (Path): Claude Code's folder, with its ``sessions/`` and ``projects/`` (``PR_WATCH_CLAUDE_HOME``).
        caller_cwd (Path): The folder the command was typed in (``PR_WATCH_CALLER_CWD``, set by ``bin/pr-watch``).
        skill_dir (Path): The skill's folder (``PR_WATCH_SKILL_DIR``).

    Notes:
        - ``bin/pr-watch`` runs the tool from the skills' uv project, so the folder the person typed the command in
          comes through ``PR_WATCH_CALLER_CWD``.
        - The cost ledgers belong to the ai-test-cost skill, hence its own variable name.
    """

    SKILL_DIR: ClassVar[Path] = Path(__file__).resolve().parents[4]

    model_config = SettingsConfigDict(env_prefix="PR_WATCH_", extra="forbid", validate_default=True)

    state_dir: Path = Field(
        default_factory=lambda: Path.home() / ".local" / "state" / "claude-pr-watch",
        description="The watcher's state: registry, memory, inboxes, operations and log.",
        examples=["/home/me/.local/state/claude-pr-watch"],
    )
    cost_state_dir: Path = Field(
        default_factory=lambda: Path.home() / ".local" / "state" / "ai-test-cost",
        validation_alias=AliasChoices("cost_state_dir", "AI_COST_STATE_DIR"),
        description="The ai-test-cost ledgers, read for the cost column.",
        examples=["/home/me/.local/state/ai-test-cost"],
    )
    claude_home: Path = Field(
        default_factory=lambda: Path.home() / ".claude",
        description="Claude Code's folder, with its sessions and projects.",
        examples=["/home/me/.claude"],
    )
    caller_cwd: Path = Field(
        default_factory=Path.cwd,
        description="The folder the command was typed in.",
        examples=["/home/me/simple-erp"],
    )
    skill_dir: Path = Field(
        default=SKILL_DIR,
        description="The skill's folder, which holds conf, templates and systemd.",
        examples=["/home/me/simple-erp/.claude/skills/pr-watch"],
    )

    @field_validator("state_dir", mode="before")
    def validate_state_dir(cls, value: JsonValue) -> JsonValue:
        """Validate ``state_dir``.

        Args:
            value (JsonValue): The raw folder, or ``None``.

        Returns:
            JsonValue: The folder, or its default.

        Raises:
            SEWatchSettingsInvalidStateDir: When the value is not a path.
        """
        if value is None:
            return str(cls.model_fields["state_dir"].get_default(call_default_factory=True))
        return FieldRules.path(value, SEWatchSettingsInvalidStateDir, "state_dir")

    @field_validator("cost_state_dir", mode="before")
    def validate_cost_state_dir(cls, value: JsonValue) -> JsonValue:
        """Validate ``cost_state_dir``.

        Args:
            value (JsonValue): The raw folder, or ``None``.

        Returns:
            JsonValue: The folder, or its default.

        Raises:
            SEWatchSettingsInvalidCostStateDir: When the value is not a path.
        """
        if value is None:
            return str(cls.model_fields["cost_state_dir"].get_default(call_default_factory=True))
        return FieldRules.path(value, SEWatchSettingsInvalidCostStateDir, "cost_state_dir")

    @field_validator("claude_home", mode="before")
    def validate_claude_home(cls, value: JsonValue) -> JsonValue:
        """Validate ``claude_home``.

        Args:
            value (JsonValue): The raw folder, or ``None``.

        Returns:
            JsonValue: The folder, or its default.

        Raises:
            SEWatchSettingsInvalidClaudeHome: When the value is not a path.
        """
        if value is None:
            return str(cls.model_fields["claude_home"].get_default(call_default_factory=True))
        return FieldRules.path(value, SEWatchSettingsInvalidClaudeHome, "claude_home")

    @field_validator("caller_cwd", mode="before")
    def validate_caller_cwd(cls, value: JsonValue) -> JsonValue:
        """Validate ``caller_cwd``.

        Args:
            value (JsonValue): The raw folder, or ``None``.

        Returns:
            JsonValue: The folder, or its default.

        Raises:
            SEWatchSettingsInvalidCallerCwd: When the value is not a path.
        """
        if value is None:
            return str(cls.model_fields["caller_cwd"].get_default(call_default_factory=True))
        return FieldRules.path(value, SEWatchSettingsInvalidCallerCwd, "caller_cwd")

    @field_validator("skill_dir", mode="before")
    def validate_skill_dir(cls, value: JsonValue) -> JsonValue:
        """Validate ``skill_dir``.

        Args:
            value (JsonValue): The raw folder, or ``None``.

        Returns:
            JsonValue: The folder, or its default.

        Raises:
            SEWatchSettingsInvalidSkillDir: When the value is not a path.
        """
        if value is None:
            return str(cls.SKILL_DIR)
        return FieldRules.path(value, SEWatchSettingsInvalidSkillDir, "skill_dir")

    ############################
    # Publicly Exposed Methods #
    ############################

    @property
    def catalog_file(self) -> Path:
        """The watcher's catalogue, ``conf/watch.yaml`` in the skill's folder."""
        return self.skill_dir / "conf" / "watch.yaml"

    @property
    def template_file(self) -> Path:
        """The template of the summary page."""
        return self.skill_dir / "templates" / "PR-SUMMARY.md"

    @property
    def units_dir(self) -> Path:
        """The folder of the systemd unit templates."""
        return self.skill_dir / "systemd"
