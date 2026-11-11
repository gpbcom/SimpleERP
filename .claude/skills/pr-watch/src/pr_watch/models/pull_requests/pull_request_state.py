from __future__ import annotations

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from pr_watch.models.enums import PullRequestStatus
from pr_watch.models.pull_requests.exceptions import (
    SEPullRequestStateInvalidAuthor,
    SEPullRequestStateInvalidBranches,
    SEPullRequestStateInvalidStatus,
    SEPullRequestStateInvalidTimeline,
    SEPullRequestStateInvalidTitle,
)
from pr_watch.models.pull_requests.pull_request_branches import PullRequestBranches
from pr_watch.models.pull_requests.pull_request_timeline import PullRequestTimeline
from pr_watch.models.validation.field_rules import FieldRules


class PullRequestState(BaseModel):
    """A pull request as GitHub describes it now.

    Attributes:
        title (str): Its title.
        status (PullRequestStatus): Open, merged or closed without merge.
        author (str): The login of its author, whose own comments are not events.
        branches (PullRequestBranches): Its branches.
        timeline (PullRequestTimeline): When it was opened and closed.
    """

    model_config = ConfigDict(extra="forbid")

    title: str = Field(description="Its title.", examples=["[GH-12] Add customers"])
    status: PullRequestStatus = Field(description="Open, merged or closed without merge.", examples=["open"])
    author: str = Field(description="The login of its author, whose own comments are not events.", examples=["gpbcom"])
    branches: PullRequestBranches = Field(
        description="Its branches.",
        examples=[
            {
                "head_ref": "feature/GH-12-add-customers",
                "head_sha": "668501e0d3a1b2c3d4e5f60718293a4b5c6d7e8f",
                "base_ref": "develop",
            }
        ],
    )
    timeline: PullRequestTimeline = Field(
        description="When it was opened and closed.", examples=[{"opened_on": "2026-11-09T17:00:00+01:00"}]
    )

    @field_validator("title", mode="before")
    def validate_title(cls, value: JsonValue) -> JsonValue:
        """Validate ``title``.

        Args:
            value (JsonValue): The raw title.

        Returns:
            JsonValue: The title.

        Raises:
            SEPullRequestStateInvalidTitle: When the value is not a non-empty string.
        """
        return FieldRules.text(value, SEPullRequestStateInvalidTitle, "title")

    @field_validator("status", mode="before")
    def validate_status(cls, value: JsonValue) -> JsonValue:
        """Validate ``status``.

        Args:
            value (JsonValue): The raw status.

        Returns:
            JsonValue: The status.

        Raises:
            SEPullRequestStateInvalidStatus: When the value is not a ``PullRequestStatus``.
        """
        return FieldRules.member(value, SEPullRequestStateInvalidStatus, "status", PullRequestStatus)

    @field_validator("author", mode="before")
    def validate_author(cls, value: JsonValue) -> JsonValue:
        """Validate ``author``.

        Args:
            value (JsonValue): The raw author.

        Returns:
            JsonValue: The author.

        Raises:
            SEPullRequestStateInvalidAuthor: When the value is not a non-empty string.
        """
        return FieldRules.text(value, SEPullRequestStateInvalidAuthor, "author")

    @field_validator("branches", mode="before")
    def validate_branches(cls, value: JsonValue) -> JsonValue:
        """Validate ``branches``.

        Args:
            value (JsonValue): The raw branches.

        Returns:
            JsonValue: The branches.

        Raises:
            SEPullRequestStateInvalidBranches: When the value is not a model or a mapping of its fields.
        """
        return FieldRules.nested(value, SEPullRequestStateInvalidBranches, "branches")

    @field_validator("timeline", mode="before")
    def validate_timeline(cls, value: JsonValue) -> JsonValue:
        """Validate ``timeline``.

        Args:
            value (JsonValue): The raw timeline.

        Returns:
            JsonValue: The timeline.

        Raises:
            SEPullRequestStateInvalidTimeline: When the value is not a model or a mapping of its fields.
        """
        return FieldRules.nested(value, SEPullRequestStateInvalidTimeline, "timeline")
