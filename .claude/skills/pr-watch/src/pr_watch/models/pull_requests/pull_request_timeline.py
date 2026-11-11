from __future__ import annotations

# Standard library imports
from datetime import datetime
from typing import Optional

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from pr_watch.models.pull_requests.exceptions import (
    SEPullRequestTimelineInvalidClosedOn,
    SEPullRequestTimelineInvalidMergeCommit,
    SEPullRequestTimelineInvalidOpenedOn,
)
from pr_watch.models.validation.field_rules import FieldRules


class PullRequestTimeline(BaseModel):
    """When a pull request was opened and closed.

    Attributes:
        opened_on (datetime): When it was opened.
        closed_on (Optional[datetime]): When it was merged or closed.
        merge_commit (Optional[str]): The merge commit, once merged.
    """

    model_config = ConfigDict(extra="forbid")

    opened_on: datetime = Field(description="When it was opened.", examples=["2026-11-09T17:00:00+01:00"])
    closed_on: Optional[datetime] = Field(
        default=None, description="When it was merged or closed.", examples=["2026-11-11T10:00:00+01:00"]
    )
    merge_commit: Optional[str] = Field(
        default=None, description="The merge commit, once merged.", examples=["9f1c2b3a"]
    )

    @field_validator("opened_on", mode="before")
    def validate_opened_on(cls, value: JsonValue) -> JsonValue:
        """Validate ``opened_on``.

        Args:
            value (JsonValue): The raw opened on.

        Returns:
            JsonValue: The opened on.

        Raises:
            SEPullRequestTimelineInvalidOpenedOn: When the value is not a time with its time zone.
        """
        return FieldRules.moment(value, SEPullRequestTimelineInvalidOpenedOn, "opened_on")

    @field_validator("closed_on", mode="before")
    def validate_closed_on(cls, value: JsonValue) -> JsonValue:
        """Validate ``closed_on``.

        Args:
            value (JsonValue): The raw closed on, or ``None``.

        Returns:
            JsonValue: The closed on, or ``None``.

        Raises:
            SEPullRequestTimelineInvalidClosedOn: When the value is not a time with its time zone.
        """
        if value is None:
            return None
        return FieldRules.moment(value, SEPullRequestTimelineInvalidClosedOn, "closed_on")

    @field_validator("merge_commit", mode="before")
    def validate_merge_commit(cls, value: JsonValue) -> JsonValue:
        """Validate ``merge_commit``.

        Args:
            value (JsonValue): The raw merge commit, or ``None``.

        Returns:
            JsonValue: The merge commit, or ``None``.

        Raises:
            SEPullRequestTimelineInvalidMergeCommit: When the value is not a non-empty string.
        """
        if value is None:
            return None
        return FieldRules.text(value, SEPullRequestTimelineInvalidMergeCommit, "merge_commit")
