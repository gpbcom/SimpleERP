from __future__ import annotations

# Standard library imports
import re
from typing import ClassVar

# Third-party imports
from pydantic import ConfigDict, Field, JsonValue, field_validator

# First-party imports
from harness_core.models.catalogs.yaml_catalog import YamlCatalog
from release_notes.models.catalogs.exceptions import (
    SEGithubCoordinatesInvalidOwner,
    SEGithubCoordinatesInvalidRepository,
    SEGithubCoordinatesUnreadable,
)


class GithubCoordinates(YamlCatalog):
    """Where simple-erp lives on GitHub, read from the shared ``ticket-docs/conf/github.yaml``.

    Attributes:
        UNREADABLE (type[Exception]): The exception raised when the file cannot be read.
        NAME_PATTERN (re.Pattern[str]): An owner or repository name.
        ISSUE_LINK (str): The web link of an issue.
        ISSUES_PATH (str): The REST API path of an issue.
        owner (str): The repository's owner.
        repository (str): The repository's name.

    Notes:
        **The other keys of the file are ignored**: the file belongs to the ticket-docs skill, which keeps its
        project board there, and this tool only needs the repository.
    """

    UNREADABLE: ClassVar[type[Exception]] = SEGithubCoordinatesUnreadable
    NAME_PATTERN: ClassVar[re.Pattern[str]] = re.compile(r"^[A-Za-z0-9_.-]+$")
    ISSUE_LINK: ClassVar[str] = "https://github.com/{owner}/{repository}/issues/{number}"
    ISSUES_PATH: ClassVar[str] = "/repos/{owner}/{repository}/issues/{number}"

    model_config = ConfigDict(extra="ignore", frozen=True)

    owner: str = Field(description="The repository's owner.", examples=["gpbcom"])
    repository: str = Field(description="The repository's name.", examples=["simple-erp"])

    @field_validator("owner", mode="before")
    def validate_owner(cls, value: JsonValue) -> JsonValue:
        """Validate ``owner``.

        Args:
            value (JsonValue): The raw owner.

        Returns:
            JsonValue: The owner, stripped.

        Raises:
            SEGithubCoordinatesInvalidOwner: When the value is not a GitHub name.
        """
        if not isinstance(value, str) or not cls.NAME_PATTERN.match(value.strip()):
            raise SEGithubCoordinatesInvalidOwner(
                f"Invalid owner: {value!r}. "  # noqa: E501
                "Must be a GitHub name."
            )
        return value.strip()

    @field_validator("repository", mode="before")
    def validate_repository(cls, value: JsonValue) -> JsonValue:
        """Validate ``repository``.

        Args:
            value (JsonValue): The raw repository name.

        Returns:
            JsonValue: The name, stripped.

        Raises:
            SEGithubCoordinatesInvalidRepository: When the value is not a GitHub name.
        """
        if not isinstance(value, str) or not cls.NAME_PATTERN.match(value.strip()):
            raise SEGithubCoordinatesInvalidRepository(
                f"Invalid repository: {value!r}. "  # noqa: E501
                "Must be a GitHub name."
            )
        return value.strip()

    ############################
    # Publicly Exposed Methods #
    ############################

    def issue_link(self, number: int) -> str:
        """Give the web link of an issue.

        Args:
            number (int): The issue number.

        Returns:
            str: The link, such as ``https://github.com/gpbcom/simple-erp/issues/12``.
        """
        return self.ISSUE_LINK.format(owner=self.owner, repository=self.repository, number=number)

    def issues_path(self, number: int) -> str:
        """Give the REST API path of an issue.

        Args:
            number (int): The issue number.

        Returns:
            str: The path, such as ``/repos/gpbcom/simple-erp/issues/12``.
        """
        return self.ISSUES_PATH.format(owner=self.owner, repository=self.repository, number=number)
