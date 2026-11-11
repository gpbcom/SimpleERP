from __future__ import annotations

# Standard library imports
from typing import List, Optional

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from pr_watch.models.checks.stage_deployment import StageDeployment
from pr_watch.models.enums import ChecksStatus, ReviewState
from pr_watch.models.state.exceptions import (
    SECiSummaryInvalidChecks,
    SECiSummaryInvalidChecksLink,
    SECiSummaryInvalidReview,
    SECiSummaryInvalidStages,
)
from pr_watch.models.validation.field_rules import FieldRules


class CiSummary(BaseModel):
    """What the checks, the stages and the reviews of a pull request's head say, as the summary page shows it.

    Attributes:
        checks (ChecksStatus): The checks of the head commit as a whole.
        checks_link (Optional[str]): A failed check, when any.
        stages (List[StageDeployment]): The latest deployment of the head commit to each stage.
        review (Optional[ReviewState]): The reviewers' standing decision, ``CHANGES_REQUESTED`` when one asks for
            changes.
    """

    model_config = ConfigDict(extra="forbid")

    checks: ChecksStatus = Field(
        default=ChecksStatus.NONE, description="The checks of the head commit as a whole.", examples=["failed"]
    )
    checks_link: Optional[str] = Field(
        default=None,
        description="A failed check, when any.",
        examples=["https://github.com/gpbcom/simple-erp/runs/501"],
    )
    stages: List[StageDeployment] = Field(
        default_factory=list,
        description="The latest deployment of the head commit to each stage.",
        examples=[[{"environment": "dev", "deployment_id": 701, "state": "success"}]],
    )
    review: Optional[ReviewState] = Field(
        default=None,
        description="The reviewers' standing decision, ``CHANGES_REQUESTED`` when one asks for changes.",
        examples=["APPROVED"],
    )

    @field_validator("checks", mode="before")
    def validate_checks(cls, value: JsonValue) -> JsonValue:
        """Validate ``checks``.

        Args:
            value (JsonValue): The raw checks, or ``None``.

        Returns:
            JsonValue: The checks, or its default.

        Raises:
            SECiSummaryInvalidChecks: When the value is not a ``ChecksStatus``.
        """
        if value is None:
            return cls.model_fields["checks"].get_default(call_default_factory=True)
        return FieldRules.member(value, SECiSummaryInvalidChecks, "checks", ChecksStatus)

    @field_validator("checks_link", mode="before")
    def validate_checks_link(cls, value: JsonValue) -> JsonValue:
        """Validate ``checks_link``.

        Args:
            value (JsonValue): The raw checks link, or ``None``.

        Returns:
            JsonValue: The checks link, or ``None``.

        Raises:
            SECiSummaryInvalidChecksLink: When the value is not an http or https link.
        """
        if value is None:
            return None
        return FieldRules.link(value, SECiSummaryInvalidChecksLink, "checks_link")

    @field_validator("stages", mode="before")
    def validate_stages(cls, value: JsonValue) -> JsonValue:
        """Validate ``stages``.

        Args:
            value (JsonValue): The raw stages, or ``None``.

        Returns:
            JsonValue: The stages, or its default.

        Raises:
            SECiSummaryInvalidStages: When the value is not a list.
        """
        if value is None:
            return cls.model_fields["stages"].get_default(call_default_factory=True)
        return FieldRules.sequence(value, SECiSummaryInvalidStages, "stages")

    @field_validator("review", mode="before")
    def validate_review(cls, value: JsonValue) -> JsonValue:
        """Validate ``review``.

        Args:
            value (JsonValue): The raw review, or ``None``.

        Returns:
            JsonValue: The review, or ``None``.

        Raises:
            SECiSummaryInvalidReview: When the value is not a ``ReviewState``.
        """
        if value is None:
            return None
        return FieldRules.member(value, SECiSummaryInvalidReview, "review", ReviewState)
