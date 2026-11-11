from __future__ import annotations

# Standard library imports
from typing import ClassVar, List, Optional

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from ticket_docs.models.issues.enums import IssueState
from ticket_docs.models.issues.exceptions import (
    SEGithubIssueInvalidBody,
    SEGithubIssueInvalidLabels,
    SEGithubIssueInvalidNumber,
    SEGithubIssueInvalidParent,
    SEGithubIssueInvalidState,
    SEGithubIssueInvalidSubIssues,
    SEGithubIssueInvalidTitle,
)


class GithubIssue(BaseModel):
    """A GitHub issue as the GIT-10 checks read it: a feature or a ticket.

    Attributes:
        KEY_PREFIX (str): The prefix of a ticket key, ``GH-``.
        number (int): The issue's number in the repository.
        id (int): The issue's REST id, which links it as a sub-issue.
        title (str): The issue's title.
        body (str): The issue's Markdown body.
        state (IssueState): Whether the issue is open or closed.
        labels (List[str]): The names of its labels.
        parent (Optional[int]): The number of its parent issue, ``None`` when it has none.
        sub_issues (int): How many sub-issues it has.
    """

    KEY_PREFIX: ClassVar[str] = "GH-"

    model_config = ConfigDict(extra="forbid", frozen=True)

    number: int = Field(description="The issue's number in the repository.", examples=[13])
    id: int = Field(description="The issue's REST id, which links it as a sub-issue.", examples=[6328695016])
    title: str = Field(description="The issue's title.", examples=["[INFRA] Accept a short SHA as ref in stage.yml"])
    body: str = Field(default="", description="The issue's Markdown body.", examples=["## Description\n"])
    state: IssueState = Field(description="Whether the issue is open or closed.", examples=["open"])
    labels: List[str] = Field(default_factory=list, description="The names of its labels.", examples=[["INFRA"]])
    parent: Optional[int] = Field(default=None, description="The number of its parent issue.", examples=[17])
    sub_issues: int = Field(default=0, description="How many sub-issues it has.", examples=[5])

    @field_validator("number", "id", mode="before")
    def validate_number(cls, value: JsonValue) -> JsonValue:
        """Validate ``number`` and ``id``.

        Args:
            value (JsonValue): The raw number.

        Returns:
            JsonValue: The number.

        Raises:
            SEGithubIssueInvalidNumber: When the value is not a positive whole number.
        """
        if isinstance(value, bool) or not isinstance(value, int) or value < 1:
            raise SEGithubIssueInvalidNumber(
                f"Invalid number: {value!r}. "  # noqa: E501
                "Must be a positive whole number."
            )
        return value

    @field_validator("title", mode="before")
    def validate_title(cls, value: JsonValue) -> JsonValue:
        """Validate ``title``.

        Args:
            value (JsonValue): The raw title.

        Returns:
            JsonValue: The title, stripped.

        Raises:
            SEGithubIssueInvalidTitle: When the value is not a non-empty string.
        """
        if not isinstance(value, str) or not value.strip():
            raise SEGithubIssueInvalidTitle(
                f"Invalid title: {value!r}. "  # noqa: E501
                "Must be a non-empty string."
            )
        return value.strip()

    @field_validator("body", mode="before")
    def validate_body(cls, value: JsonValue) -> JsonValue:
        """Validate ``body``.

        Args:
            value (JsonValue): The raw body, or ``None`` for an issue written without one.

        Returns:
            JsonValue: The body, empty for ``None``.

        Raises:
            SEGithubIssueInvalidBody: When the value is not a string.
        """
        if value is None:
            return ""
        if not isinstance(value, str):
            raise SEGithubIssueInvalidBody(
                f"Invalid body: {value!r}. "  # noqa: E501
                "Must be Markdown text."
            )
        return value

    @field_validator("state", mode="before")
    def validate_state(cls, value: JsonValue) -> JsonValue:
        """Validate ``state``.

        Args:
            value (JsonValue): The raw state.

        Returns:
            JsonValue: The state.

        Raises:
            SEGithubIssueInvalidState: When the value is not one of the issue states.
        """
        if isinstance(value, IssueState):
            return value
        if not isinstance(value, str) or value not in {state.value for state in IssueState}:
            raise SEGithubIssueInvalidState(
                f"Invalid state: {value!r}. "  # noqa: E501
                f"Must be one of {', '.join(state.value for state in IssueState)}."
            )
        return value

    @field_validator("labels", mode="before")
    def validate_labels(cls, value: JsonValue) -> JsonValue:
        """Validate ``labels``.

        Args:
            value (JsonValue): The raw labels: names, or the REST API's label objects, or ``None``.

        Returns:
            JsonValue: The label names, empty for ``None``.

        Raises:
            SEGithubIssueInvalidLabels: When the value is not a list of non-empty names or of objects with one.
        """
        if value is None:
            return []
        if not isinstance(value, list):
            raise SEGithubIssueInvalidLabels(
                f"Invalid labels: {value!r}. "  # noqa: E501
                "Must be a list of label names."
            )
        names = [item.get("name") if isinstance(item, dict) else item for item in value]
        if not all(isinstance(name, str) and name.strip() for name in names):
            raise SEGithubIssueInvalidLabels(
                f"Invalid labels: {value!r}. "  # noqa: E501
                "Each label must have a non-empty name."
            )
        return names

    @field_validator("parent", mode="before")
    def validate_parent(cls, value: JsonValue) -> JsonValue:
        """Validate ``parent``.

        Args:
            value (JsonValue): The raw parent number, or ``None``.

        Returns:
            JsonValue: The number, or ``None``.

        Raises:
            SEGithubIssueInvalidParent: When the value is neither ``None`` nor a positive whole number.
        """
        if value is None:
            return None
        if isinstance(value, bool) or not isinstance(value, int) or value < 1:
            raise SEGithubIssueInvalidParent(
                f"Invalid parent: {value!r}. "  # noqa: E501
                "Must be the number of an issue."
            )
        return value

    @field_validator("sub_issues", mode="before")
    def validate_sub_issues(cls, value: JsonValue) -> JsonValue:
        """Validate ``sub_issues``.

        Args:
            value (JsonValue): The raw count, or ``None``.

        Returns:
            JsonValue: The count, 0 for ``None``.

        Raises:
            SEGithubIssueInvalidSubIssues: When the value is not a whole number of zero or more.
        """
        if value is None:
            return cls.model_fields["sub_issues"].get_default(call_default_factory=True)
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise SEGithubIssueInvalidSubIssues(
                f"Invalid sub_issues: {value!r}. "  # noqa: E501
                "Must be a whole number of zero or more."
            )
        return value

    ############################
    # Publicly Exposed Methods #
    ############################

    @property
    def key(self) -> str:
        """The ticket key of the issue, such as ``GH-13``."""
        return f"{self.KEY_PREFIX}{self.number}"
