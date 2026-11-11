from __future__ import annotations

# Standard library imports
from typing import ClassVar

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from pr_watch.models.validation.field_rules import FieldRules
from pr_watch.models.watch.exceptions import (
    SEPullRequestRefInvalidNumber,
    SEPullRequestRefInvalidRepository,
    SEPullRequestRefInvalidRoot,
)


class PullRequestRef(BaseModel):
    """Where a watched pull request lives.

    Attributes:
        URL_PATTERN (str): The web link of a pull request.
        repository (str): The GitHub repository, ``<owner>/<name>``.
        number (int): The pull request number.
        root (str): The main working tree of the local clone.

    Notes:
        ``root`` is the main working tree of the clone, so that a worktree removed later does not lose the ticket
        folders.
    """

    URL_PATTERN: ClassVar[str] = "https://github.com/{repository}/pull/{number}"

    model_config = ConfigDict(extra="forbid")

    repository: str = Field(description="The GitHub repository, ``<owner>/<name>``.", examples=["gpbcom/simple-erp"])
    number: int = Field(description="The pull request number.", examples=[7])
    root: str = Field(description="The main working tree of the local clone.", examples=["/home/me/simple-erp"])

    @field_validator("repository", mode="before")
    def validate_repository(cls, value: JsonValue) -> JsonValue:
        """Validate ``repository``.

        Args:
            value (JsonValue): The raw repository.

        Returns:
            JsonValue: The repository.

        Raises:
            SEPullRequestRefInvalidRepository: When the value is not an ``<owner>/<name>`` repository.
        """
        return FieldRules.slug(value, SEPullRequestRefInvalidRepository, "repository")

    @field_validator("number", mode="before")
    def validate_number(cls, value: JsonValue) -> JsonValue:
        """Validate ``number``.

        Args:
            value (JsonValue): The raw number.

        Returns:
            JsonValue: The number.

        Raises:
            SEPullRequestRefInvalidNumber: When the value is not a positive integer.
        """
        return FieldRules.identifier(value, SEPullRequestRefInvalidNumber, "number")

    @field_validator("root", mode="before")
    def validate_root(cls, value: JsonValue) -> JsonValue:
        """Validate ``root``.

        Args:
            value (JsonValue): The raw root.

        Returns:
            JsonValue: The root.

        Raises:
            SEPullRequestRefInvalidRoot: When the value is not a path.
        """
        return FieldRules.path(value, SEPullRequestRefInvalidRoot, "root")

    ############################
    # Publicly Exposed Methods #
    ############################

    @property
    def url(self) -> str:
        """The pull request's web link."""
        return self.URL_PATTERN.format(repository=self.repository, number=self.number)

    @property
    def label(self) -> str:
        """The short name of the pull request, ``<repository>#<number>``."""
        return f"{self.repository}#{self.number}"
