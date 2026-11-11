from __future__ import annotations

# Standard library imports
from datetime import datetime
from typing import Optional

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from pr_watch.models.checks.rebase_probe_result import RebaseProbeResult
from pr_watch.models.pull_requests.pull_request_branches import PullRequestBranches
from pr_watch.models.state.ci_summary import CiSummary
from pr_watch.models.state.exceptions import (
    SEPrSnapshotInvalidBranches,
    SEPrSnapshotInvalidCheckedOn,
    SEPrSnapshotInvalidCi,
    SEPrSnapshotInvalidError,
    SEPrSnapshotInvalidRebase,
)
from pr_watch.models.validation.field_rules import FieldRules


class PrSnapshot(BaseModel):
    """What the last run saw of a pull request, shown on the summary page.

    Attributes:
        branches (Optional[PullRequestBranches]): Its branches and head commit.
        rebase (Optional[RebaseProbeResult]): The merge of its head into its base, tried in memory.
        ci (CiSummary): What its checks, stages and reviews say.
        error (Optional[str]): Why the last run could not read it, ``None`` when it could.
        checked_on (datetime): When it was seen.
    """

    model_config = ConfigDict(extra="forbid")

    branches: Optional[PullRequestBranches] = Field(
        default=None,
        description="Its branches and head commit.",
        examples=[
            {
                "head_ref": "feature/GH-12-add-customers",
                "head_sha": "668501e0d3a1b2c3d4e5f60718293a4b5c6d7e8f",
                "base_ref": "develop",
            }
        ],
    )
    rebase: Optional[RebaseProbeResult] = Field(
        default=None,
        description="The merge of its head into its base, tried in memory.",
        examples=[{"conflict_files": ["src/a.py"]}],
    )
    ci: CiSummary = Field(
        default_factory=CiSummary,
        description="What its checks, stages and reviews say.",
        examples=[{"checks": "passed"}],
    )
    error: Optional[str] = Field(
        default=None,
        description="Why the last run could not read it, ``None`` when it could.",
        examples=["GitHub answered 503"],
    )
    checked_on: datetime = Field(description="When it was seen.", examples=["2026-11-10T09:10:00+01:00"])

    @field_validator("branches", mode="before")
    def validate_branches(cls, value: JsonValue) -> JsonValue:
        """Validate ``branches``.

        Args:
            value (JsonValue): The raw branches, or ``None``.

        Returns:
            JsonValue: The branches, or ``None``.

        Raises:
            SEPrSnapshotInvalidBranches: When the value is not a model or a mapping of its fields.
        """
        if value is None:
            return None
        return FieldRules.nested(value, SEPrSnapshotInvalidBranches, "branches")

    @field_validator("rebase", mode="before")
    def validate_rebase(cls, value: JsonValue) -> JsonValue:
        """Validate ``rebase``.

        Args:
            value (JsonValue): The raw rebase, or ``None``.

        Returns:
            JsonValue: The rebase, or ``None``.

        Raises:
            SEPrSnapshotInvalidRebase: When the value is not a model or a mapping of its fields.
        """
        if value is None:
            return None
        return FieldRules.nested(value, SEPrSnapshotInvalidRebase, "rebase")

    @field_validator("ci", mode="before")
    def validate_ci(cls, value: JsonValue) -> JsonValue:
        """Validate ``ci``.

        Args:
            value (JsonValue): The raw ci, or ``None``.

        Returns:
            JsonValue: The ci, or its default.

        Raises:
            SEPrSnapshotInvalidCi: When the value is not a model or a mapping of its fields.
        """
        if value is None:
            return cls.model_fields["ci"].get_default(call_default_factory=True)
        return FieldRules.nested(value, SEPrSnapshotInvalidCi, "ci")

    @field_validator("error", mode="before")
    def validate_error(cls, value: JsonValue) -> JsonValue:
        """Validate ``error``.

        Args:
            value (JsonValue): The raw error, or ``None``.

        Returns:
            JsonValue: The error, or ``None``.

        Raises:
            SEPrSnapshotInvalidError: When the value is not a non-empty string.
        """
        if value is None:
            return None
        return FieldRules.text(value, SEPrSnapshotInvalidError, "error")

    @field_validator("checked_on", mode="before")
    def validate_checked_on(cls, value: JsonValue) -> JsonValue:
        """Validate ``checked_on``.

        Args:
            value (JsonValue): The raw checked on.

        Returns:
            JsonValue: The checked on.

        Raises:
            SEPrSnapshotInvalidCheckedOn: When the value is not a time with its time zone.
        """
        return FieldRules.moment(value, SEPrSnapshotInvalidCheckedOn, "checked_on")
