from __future__ import annotations

# Standard library imports
from pathlib import Path
from typing import ClassVar

# Third-party imports
from pydantic import Field, JsonValue, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

# First-party imports
from project_docs.models.settings.exceptions import (
    SEProjectDocsSettingsInvalidCallerCwd,
    SEProjectDocsSettingsInvalidSkillDir,
)


class ProjectDocsSettings(BaseSettings):
    """Where the project documentation tool reads, each folder overridable by an environment variable.

    Attributes:
        SKILL_DIR (Path): The skill's folder, which holds ``conf/`` and ``templates/``.
        caller_cwd (Path): The folder the command was typed in (``PROJECT_DOCS_CALLER_CWD``, set by
            ``bin/project-docs``).
        skill_dir (Path): The skill's folder (``PROJECT_DOCS_SKILL_DIR``).

    Notes:
        ``bin/project-docs`` runs the tool from the skills' uv project, so the folder the person typed the command in
        comes through ``PROJECT_DOCS_CALLER_CWD``. The repository is the git top level of that folder.
    """

    SKILL_DIR: ClassVar[Path] = Path(__file__).resolve().parents[4]

    model_config = SettingsConfigDict(env_prefix="PROJECT_DOCS_", extra="forbid", validate_default=True)

    caller_cwd: Path = Field(
        default_factory=Path.cwd, description="The folder the command was typed in.", examples=["/home/me/simple-erp"]
    )
    skill_dir: Path = Field(
        default=SKILL_DIR,
        description="The skill's folder, which holds conf and templates.",
        examples=["/home/me/simple-erp/.claude/skills/project-docs"],
    )

    @field_validator("caller_cwd", mode="before")
    def validate_caller_cwd(cls, value: JsonValue) -> JsonValue:
        """Validate ``caller_cwd``.

        Args:
            value (JsonValue): The raw folder, or ``None``.

        Returns:
            JsonValue: The folder, or the current folder.

        Raises:
            SEProjectDocsSettingsInvalidCallerCwd: When the value is not a non-empty path.
        """
        if value is None:
            return str(Path.cwd())
        if isinstance(value, Path):
            return str(value)
        if not isinstance(value, str) or not value.strip():
            raise SEProjectDocsSettingsInvalidCallerCwd(
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
            SEProjectDocsSettingsInvalidSkillDir: When the value is not a non-empty path.
        """
        if value is None:
            return str(cls.SKILL_DIR)
        if isinstance(value, Path):
            return str(value)
        if not isinstance(value, str) or not value.strip():
            raise SEProjectDocsSettingsInvalidSkillDir(
                f"Invalid skill_dir: {value!r}. "  # noqa: E501
                "Must be a non-empty folder path."
            )
        return value.strip()

    ############################
    # Publicly Exposed Methods #
    ############################

    @property
    def doc_map_file(self) -> Path:
        """The doc map, ``conf/doc-map.yaml`` in the skill's folder."""
        return self.skill_dir / "conf" / "doc-map.yaml"
