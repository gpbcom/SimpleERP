from __future__ import annotations

# Standard library imports
from datetime import datetime
from typing import ClassVar, Optional

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from pr_watch.models.state.exceptions import (
    SEUnwatchedPullRequestInvalidNumber,
    SEUnwatchedPullRequestInvalidRepository,
    SEUnwatchedPullRequestInvalidTicket,
    SEUnwatchedPullRequestInvalidTitle,
    SEUnwatchedPullRequestInvalidUpdatedOn,
)
from pr_watch.models.validation.field_rules import FieldRules


class UnwatchedPullRequest(BaseModel):
    """An open pull request of a watched repository that no ticket session watches.

    Attributes:
        URL_PATTERN (str): The web link of a pull request.
        repository (str): The GitHub repository.
        number (int): The pull request number.
        title (str): Its title.
        ticket (Optional[str]): The ticket it names, from its branch or a ``Closes #<n>`` line.
        updated_on (datetime): Its last change.
    """

    URL_PATTERN: ClassVar[str] = "https://github.com/{repository}/pull/{number}"

    model_config = ConfigDict(extra="forbid")

    repository: str = Field(description="The GitHub repository.", examples=["gpbcom/simple-erp"])
    number: int = Field(description="The pull request number.", examples=[8])
    title: str = Field(description="Its title.", examples=["[GH-13] Add invoices"])
    ticket: Optional[str] = Field(
        default=None, description="The ticket it names, from its branch or a ``Closes #<n>`` line.", examples=["GH-13"]
    )
    updated_on: datetime = Field(description="Its last change.", examples=["2026-11-10T08:00:00+01:00"])

    @field_validator("repository", mode="before")
    def validate_repository(cls, value: JsonValue) -> JsonValue:
        """Validate ``repository``.

        Args:
            value (JsonValue): The raw repository.

        Returns:
            JsonValue: The repository.

        Raises:
            SEUnwatchedPullRequestInvalidRepository: When the value is not an ``<owner>/<name>`` repository.
        """
        return FieldRules.slug(value, SEUnwatchedPullRequestInvalidRepository, "repository")

    @field_validator("number", mode="before")
    def validate_number(cls, value: JsonValue) -> JsonValue:
        """Validate ``number``.

        Args:
            value (JsonValue): The raw number.

        Returns:
            JsonValue: The number.

        Raises:
            SEUnwatchedPullRequestInvalidNumber: When the value is not a positive integer.
        """
        return FieldRules.identifier(value, SEUnwatchedPullRequestInvalidNumber, "number")

    @field_validator("title", mode="before")
    def validate_title(cls, value: JsonValue) -> JsonValue:
        """Validate ``title``.

        Args:
            value (JsonValue): The raw title.

        Returns:
            JsonValue: The title.

        Raises:
            SEUnwatchedPullRequestInvalidTitle: When the value is not a non-empty string.
        """
        return FieldRules.text(value, SEUnwatchedPullRequestInvalidTitle, "title")

    @field_validator("ticket", mode="before")
    def validate_ticket(cls, value: JsonValue) -> JsonValue:
        """Validate ``ticket``.

        Args:
            value (JsonValue): The raw ticket, or ``None``.

        Returns:
            JsonValue: The ticket, or ``None``.

        Raises:
            SEUnwatchedPullRequestInvalidTicket: When the value is not a ``GH-<n>`` key.
        """
        if value is None:
            return None
        return FieldRules.ticket(value, SEUnwatchedPullRequestInvalidTicket, "ticket")

    @field_validator("updated_on", mode="before")
    def validate_updated_on(cls, value: JsonValue) -> JsonValue:
        """Validate ``updated_on``.

        Args:
            value (JsonValue): The raw updated on.

        Returns:
            JsonValue: The updated on.

        Raises:
            SEUnwatchedPullRequestInvalidUpdatedOn: When the value is not a time with its time zone.
        """
        return FieldRules.moment(value, SEUnwatchedPullRequestInvalidUpdatedOn, "updated_on")

    ############################
    # Publicly Exposed Methods #
    ############################

    @property
    def url(self) -> str:
        """The pull request's web link."""
        return self.URL_PATTERN.format(repository=self.repository, number=self.number)
