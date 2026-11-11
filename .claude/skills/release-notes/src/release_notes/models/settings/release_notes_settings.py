from __future__ import annotations

# Standard library imports
from pathlib import Path
from typing import ClassVar

# Third-party imports
from pydantic import Field, JsonValue, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

# First-party imports
from release_notes.models.settings.exceptions import (
    SEReleaseNotesSettingsInvalidCallerCwd,
    SEReleaseNotesSettingsInvalidSkillDir,
)


class ReleaseNotesSettings(BaseSettings):
    """Where the release notes tool reads, each folder overridable by an environment variable.

    Attributes:
        SKILL_DIR (Path): The skill's folder, which holds ``conf/`` and ``templates/``.
        caller_cwd (Path): The folder the command was typed in (``RELEASE_NOTES_CALLER_CWD``, set by
            ``bin/release-notes``).
        skill_dir (Path): The skill's folder (``RELEASE_NOTES_SKILL_DIR``).

    Notes:
        - ``bin/release-notes`` runs the tool from the skills' uv project, so the folder the person typed the
          command in comes through ``RELEASE_NOTES_CALLER_CWD``. The repository is the git top level of that folder.
        - The repository's owner and name are the ticket-docs skill's, in the sibling ``ticket-docs/conf/``.
    """

    SKILL_DIR: ClassVar[Path] = Path(__file__).resolve().parents[4]

    model_config = SettingsConfigDict(env_prefix="RELEASE_NOTES_", extra="forbid", validate_default=True)

    caller_cwd: Path = Field(
        default_factory=Path.cwd, description="The folder the command was typed in.", examples=["/home/me/simple-erp"]
    )
    skill_dir: Path = Field(
        default=SKILL_DIR,
        description="The skill's folder, which holds conf and templates.",
        examples=["/home/me/simple-erp/.claude/skills/release-notes"],
    )

    @field_validator("caller_cwd", mode="before")
    def validate_caller_cwd(cls, value: JsonValue) -> JsonValue:
        """Validate ``caller_cwd``.

        Args:
            value (JsonValue): The raw folder, or ``None``.

        Returns:
            JsonValue: The folder, or the current folder.

        Raises:
            SEReleaseNotesSettingsInvalidCallerCwd: When the value is not a non-empty path.
        """
        if value is None:
            return str(Path.cwd())
        if isinstance(value, Path):
            return str(value)
        if not isinstance(value, str) or not value.strip():
            raise SEReleaseNotesSettingsInvalidCallerCwd(
                f"Invalid caller_cwd: {value!r}. "  # noqa: E501
                "Must be a non-empty folder path."
            )
        return value.strip()

    @field_validator("skill_dir", mode="before")
    def validate_skill_dir(cls, value: JsonValue) -> JsonValue:
        """Validate ``skill_dir``.

        Args:
            value (JsonValue): The raw folder, or ``None``.

        Returns:
            JsonValue: The folder, or the skill's own.

        Raises:
            SEReleaseNotesSettingsInvalidSkillDir: When the value is not a non-empty path.
        """
        if value is None:
            return str(cls.SKILL_DIR)
        if isinstance(value, Path):
            return str(value)
        if not isinstance(value, str) or not value.strip():
            raise SEReleaseNotesSettingsInvalidSkillDir(
                f"Invalid skill_dir: {value!r}. "  # noqa: E501
                "Must be a non-empty folder path."
            )
        return value.strip()

    ############################
    # Publicly Exposed Methods #
    ############################

    @property
    def changelog_types_file(self) -> Path:
        """The changelog fragment types, ``conf/changelog-types.yaml``."""
        return self.skill_dir / "conf" / "changelog-types.yaml"

    @property
    def github_api_file(self) -> Path:
        """How GitHub's REST API is read, ``conf/github-api.yaml``."""
        return self.skill_dir / "conf" / "github-api.yaml"

    @property
    def github_file(self) -> Path:
        """Where simple-erp lives on GitHub, the ticket-docs skill's ``conf/github.yaml``."""
        return self.skill_dir.parent / "ticket-docs" / "conf" / "github.yaml"

    @property
    def release_note_template(self) -> Path:
        """The release note template, ``templates/RELEASE-NOTE.md``."""
        return self.skill_dir / "templates" / "RELEASE-NOTE.md"
