from __future__ import annotations

# Standard library imports
from pathlib import Path
from typing import ClassVar, List

# Third-party imports
from pydantic import Field, JsonValue, field_validator

# First-party imports
from harness_core.models.catalogs.yaml_catalog import YamlCatalog
from ticket_docs.models.github.board_field import BoardField
from ticket_docs.models.github.board_project import BoardProject
from ticket_docs.models.github.exceptions import (
    SEGithubCatalogInvalidEnvironments,
    SEGithubCatalogInvalidProject,
    SEGithubCatalogInvalidText,
    SEGithubCatalogUnreadable,
)


class GithubCatalog(YamlCatalog):
    """Where simple-erp lives on GitHub: ``conf/github.yaml``.

    Attributes:
        UNREADABLE (type[Exception]): Raised when the file cannot be read.
        SKILL_DIR (Path): The ticket-docs skill folder, which holds ``conf/``.
        STATUS_FIELD (str): The name of the board's status field.
        owner (str): The repository's owner.
        repository (str): The repository's name.
        default_branch (str): The integration branch.
        production_branch (str): The released branch.
        project (BoardProject): The project board.
        environments (List[str]): The deployment environments.
        evidence_release_prefix (str): The tag prefix of a ticket's evidence pre-release.
    """

    UNREADABLE: ClassVar[type[Exception]] = SEGithubCatalogUnreadable
    SKILL_DIR: ClassVar[Path] = Path(__file__).resolve().parents[4]
    STATUS_FIELD: ClassVar[str] = "status"

    owner: str = Field(description="The repository's owner.", examples=["gpbcom"])
    repository: str = Field(description="The repository's name.", examples=["simple-erp"])
    default_branch: str = Field(description="The integration branch.", examples=["develop"])
    production_branch: str = Field(description="The released branch.", examples=["master"])
    project: BoardProject = Field(description="The project board.")
    environments: List[str] = Field(
        default_factory=list, description="The deployment environments.", examples=[["dev", "qa"]]
    )
    evidence_release_prefix: str = Field(
        description="The tag prefix of a ticket's evidence pre-release.", examples=["evidence-"]
    )

    @field_validator(
        "owner", "repository", "default_branch", "production_branch", "evidence_release_prefix", mode="before"
    )
    def validate_text(cls, value: JsonValue) -> JsonValue:
        """Validate ``owner``, ``repository``, the two branches and ``evidence_release_prefix``.

        Args:
            value (JsonValue): The raw text.

        Returns:
            JsonValue: The text, stripped.

        Raises:
            SEGithubCatalogInvalidText: When the value is not a non-empty string.
        """
        if not isinstance(value, str) or not value.strip():
            raise SEGithubCatalogInvalidText(
                f"Invalid text: {value!r}. "  # noqa: E501
                "Must be a non-empty string."
            )
        return value.strip()

    @field_validator("project", mode="before")
    def validate_project(cls, value: JsonValue) -> JsonValue:
        """Validate ``project``.

        Args:
            value (JsonValue): The raw project.

        Returns:
            JsonValue: The project.

        Raises:
            SEGithubCatalogInvalidProject: When the value is not a mapping or a ``BoardProject``.
        """
        if not isinstance(value, (dict, BoardProject)):
            raise SEGithubCatalogInvalidProject(
                f"Invalid project: {value!r}. "  # noqa: E501
                "Must give the board's number, url, id and fields."
            )
        return value

    @field_validator("environments", mode="before")
    def validate_environments(cls, value: JsonValue) -> JsonValue:
        """Validate ``environments``.

        Args:
            value (JsonValue): The raw environments, or ``None``.

        Returns:
            JsonValue: The environments, empty for ``None``.

        Raises:
            SEGithubCatalogInvalidEnvironments: When the value is not a list of non-empty names.
        """
        if value is None:
            return []
        if not isinstance(value, list) or not all(isinstance(name, str) and name.strip() for name in value):
            raise SEGithubCatalogInvalidEnvironments(
                f"Invalid environments: {value!r}. "  # noqa: E501
                "Must be a list of environment names."
            )
        return value

    ############################
    # Publicly Exposed Methods #
    ############################

    @property
    def full_name(self) -> str:
        """The repository as ``owner/name``."""
        return f"{self.owner}/{self.repository}"

    def release_tag(self, ticket: str) -> str:
        """Give the tag of a ticket's evidence pre-release.

        Args:
            ticket (str): The ticket, ``GH-<n>``.

        Returns:
            str: The tag, such as ``evidence-GH-12``.
        """
        return f"{self.evidence_release_prefix}{ticket}"

    def status_field(self) -> BoardField:
        """Give the board's status field.

        Returns:
            BoardField: The field, with no option and an empty id when the catalogue does not name one.
        """
        return self.project.fields.get(self.STATUS_FIELD) or BoardField(id="-")
