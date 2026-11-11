from __future__ import annotations

# Standard library imports
import re
from datetime import datetime
from typing import ClassVar, Pattern

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from ticket_docs.models.enums import RunConclusion
from ticket_docs.models.evidence.exceptions import (
    SEActionsRunInvalidConclusion,
    SEActionsRunInvalidCreatedAt,
    SEActionsRunInvalidHeadSha,
    SEActionsRunInvalidText,
)


class ActionsRun(BaseModel):
    """A GitHub Actions run, as ``gh run view --json`` gives it.

    Attributes:
        SHA_PATTERN (Pattern[str]): A full commit hash.
        conclusion (RunConclusion): How the run ended.
        head_sha (str): The commit it ran on.
        head_branch (str): The branch it ran on.
        url (str): Its page on GitHub.
        display_title (str): Its title.
        created_at (datetime): When it started.

    Notes:
        The fields carry gh's camel-case names as aliases, so ``model_validate`` reads gh's JSON as it is.
    """

    SHA_PATTERN: ClassVar[Pattern[str]] = re.compile(r"^[0-9a-f]{40}$")

    model_config = ConfigDict(extra="forbid", frozen=True, populate_by_name=True)

    conclusion: RunConclusion = Field(
        default=RunConclusion.PENDING, description="How the run ended.", examples=["success"]
    )
    head_sha: str = Field(alias="headSha", description="The commit it ran on.", examples=["c" * 40])
    head_branch: str = Field(alias="headBranch", description="The branch it ran on.", examples=["feature/GH-1-x"])
    url: str = Field(description="Its page on GitHub.", examples=["https://github.com/o/r/actions/runs/1"])
    display_title: str = Field(alias="displayTitle", description="Its title.", examples=["stage dev"])
    created_at: datetime = Field(alias="createdAt", description="When it started.")

    @field_validator("conclusion", mode="before")
    def validate_conclusion(cls, value: JsonValue) -> JsonValue:
        """Validate ``conclusion``.

        Args:
            value (JsonValue): The raw conclusion, or ``None``.

        Returns:
            JsonValue: The conclusion, empty while the run goes on.

        Raises:
            SEActionsRunInvalidConclusion: When the value is not a ``RunConclusion``.
        """
        if value is None:
            return RunConclusion.PENDING.value
        if value not in {conclusion.value for conclusion in RunConclusion}:
            raise SEActionsRunInvalidConclusion(
                f"Invalid conclusion: {value!r}. "  # noqa: E501
                f"Must be one of {[conclusion.value for conclusion in RunConclusion]}."
            )
        return value

    @field_validator("head_sha", mode="before")
    def validate_head_sha(cls, value: JsonValue) -> JsonValue:
        """Validate ``head_sha``.

        Args:
            value (JsonValue): The raw commit hash.

        Returns:
            JsonValue: The hash.

        Raises:
            SEActionsRunInvalidHeadSha: When the value is not a full 40-character hash.
        """
        if not isinstance(value, str) or not cls.SHA_PATTERN.match(value):
            raise SEActionsRunInvalidHeadSha(
                f"Invalid head_sha: {value!r}. "  # noqa: E501
                "Must be a full 40-character commit hash."
            )
        return value

    @field_validator("head_branch", "url", "display_title", mode="before")
    def validate_text(cls, value: JsonValue) -> JsonValue:
        """Validate ``head_branch``, ``url`` and ``display_title``.

        Args:
            value (JsonValue): The raw text.

        Returns:
            JsonValue: The text, stripped.

        Raises:
            SEActionsRunInvalidText: When the value is not a non-empty string.
        """
        if not isinstance(value, str) or not value.strip():
            raise SEActionsRunInvalidText(
                f"Invalid text: {value!r}. "  # noqa: E501
                "Must be a non-empty string."
            )
        return value.strip()

    @field_validator("created_at", mode="before")
    def validate_created_at(cls, value: JsonValue) -> JsonValue:
        """Validate ``created_at``.

        Args:
            value (JsonValue): The raw moment, ISO 8601 as gh writes it, or a ``datetime``.

        Returns:
            JsonValue: The moment.

        Raises:
            SEActionsRunInvalidCreatedAt: When the value is not an ISO 8601 moment.
        """
        if isinstance(value, datetime):
            return value
        if isinstance(value, str):
            try:
                return datetime.fromisoformat(value.strip().replace("Z", "+00:00")).isoformat()
            except ValueError:
                pass
        raise SEActionsRunInvalidCreatedAt(
            f"Invalid created_at: {value!r}. "  # noqa: E501
            "Must be an ISO 8601 moment."
        )

    ############################
    # Publicly Exposed Methods #
    ############################

    @property
    def succeeded(self) -> bool:
        """Whether every job of the run passed."""
        return self.conclusion is RunConclusion.SUCCESS
