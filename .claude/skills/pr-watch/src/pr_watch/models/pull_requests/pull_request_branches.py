from __future__ import annotations

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from pr_watch.models.enums import MergeableState
from pr_watch.models.pull_requests.exceptions import (
    SEPullRequestBranchesInvalidBaseRef,
    SEPullRequestBranchesInvalidHeadRef,
    SEPullRequestBranchesInvalidHeadSha,
    SEPullRequestBranchesInvalidMergeable,
)
from pr_watch.models.validation.field_rules import FieldRules


class PullRequestBranches(BaseModel):
    """The branches of a pull request, and whether its head merges into its base.

    Attributes:
        head_ref (str): The head branch.
        head_sha (str): The head commit.
        base_ref (str): The branch the pull request merges into, ``develop`` or ``master``.
        mergeable (MergeableState): What GitHub says of the merge, ``dirty`` when it conflicts.
    """

    model_config = ConfigDict(extra="forbid")

    head_ref: str = Field(description="The head branch.", examples=["feature/GH-12-add-customers"])
    head_sha: str = Field(description="The head commit.", examples=["668501e0d3a1b2c3d4e5f60718293a4b5c6d7e8f"])
    base_ref: str = Field(
        description="The branch the pull request merges into, ``develop`` or ``master``.", examples=["develop"]
    )
    mergeable: MergeableState = Field(
        default=MergeableState.UNKNOWN,
        description="What GitHub says of the merge, ``dirty`` when it conflicts.",
        examples=["dirty"],
    )

    @field_validator("head_ref", mode="before")
    def validate_head_ref(cls, value: JsonValue) -> JsonValue:
        """Validate ``head_ref``.

        Args:
            value (JsonValue): The raw head ref.

        Returns:
            JsonValue: The head ref.

        Raises:
            SEPullRequestBranchesInvalidHeadRef: When the value is not a non-empty string.
        """
        return FieldRules.text(value, SEPullRequestBranchesInvalidHeadRef, "head_ref")

    @field_validator("head_sha", mode="before")
    def validate_head_sha(cls, value: JsonValue) -> JsonValue:
        """Validate ``head_sha``.

        Args:
            value (JsonValue): The raw head sha.

        Returns:
            JsonValue: The head sha.

        Raises:
            SEPullRequestBranchesInvalidHeadSha: When the value is not a non-empty string.
        """
        return FieldRules.text(value, SEPullRequestBranchesInvalidHeadSha, "head_sha")

    @field_validator("base_ref", mode="before")
    def validate_base_ref(cls, value: JsonValue) -> JsonValue:
        """Validate ``base_ref``.

        Args:
            value (JsonValue): The raw base ref.

        Returns:
            JsonValue: The base ref.

        Raises:
            SEPullRequestBranchesInvalidBaseRef: When the value is not a non-empty string.
        """
        return FieldRules.text(value, SEPullRequestBranchesInvalidBaseRef, "base_ref")

    @field_validator("mergeable", mode="before")
    def validate_mergeable(cls, value: JsonValue) -> JsonValue:
        """Validate ``mergeable``.

        Args:
            value (JsonValue): The raw mergeable, or ``None``.

        Returns:
            JsonValue: The mergeable, or its default.

        Raises:
            SEPullRequestBranchesInvalidMergeable: When the value is not a ``MergeableState``.
        """
        if value is None:
            return cls.model_fields["mergeable"].get_default(call_default_factory=True)
        return FieldRules.member(value, SEPullRequestBranchesInvalidMergeable, "mergeable", MergeableState)
