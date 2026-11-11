from __future__ import annotations

# Standard library imports
from typing import Optional

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from pr_watch.models.checks.exceptions import (
    SEWorkflowRunInvalidConclusion,
    SEWorkflowRunInvalidId,
    SEWorkflowRunInvalidLink,
    SEWorkflowRunInvalidSuiteId,
    SEWorkflowRunInvalidWorkflow,
)
from pr_watch.models.enums import CheckConclusion
from pr_watch.models.validation.field_rules import FieldRules


class WorkflowRun(BaseModel):
    """A GitHub Actions workflow run of a commit.

    Attributes:
        id (int): The run's identifier.
        workflow (str): The file name of its workflow.
        conclusion (Optional[CheckConclusion]): How it ended, ``None`` while it runs.
        link (str): The run on GitHub.
        suite_id (Optional[int]): The check suite of its jobs.
    """

    model_config = ConfigDict(extra="forbid")

    id: int = Field(description="The run's identifier.", examples=[601])
    workflow: str = Field(description="The file name of its workflow.", examples=["stage.yml"])
    conclusion: Optional[CheckConclusion] = Field(
        default=None, description="How it ended, ``None`` while it runs.", examples=["failure"]
    )
    link: str = Field(
        description="The run on GitHub.", examples=["https://github.com/gpbcom/simple-erp/actions/runs/601"]
    )
    suite_id: Optional[int] = Field(default=None, description="The check suite of its jobs.", examples=[77])

    @field_validator("id", mode="before")
    def validate_id(cls, value: JsonValue) -> JsonValue:
        """Validate ``id``.

        Args:
            value (JsonValue): The raw id.

        Returns:
            JsonValue: The id.

        Raises:
            SEWorkflowRunInvalidId: When the value is not a positive integer.
        """
        return FieldRules.identifier(value, SEWorkflowRunInvalidId, "id")

    @field_validator("workflow", mode="before")
    def validate_workflow(cls, value: JsonValue) -> JsonValue:
        """Validate ``workflow``.

        Args:
            value (JsonValue): The raw workflow.

        Returns:
            JsonValue: The workflow.

        Raises:
            SEWorkflowRunInvalidWorkflow: When the value is not a non-empty string.
        """
        return FieldRules.text(value, SEWorkflowRunInvalidWorkflow, "workflow")

    @field_validator("conclusion", mode="before")
    def validate_conclusion(cls, value: JsonValue) -> JsonValue:
        """Validate ``conclusion``.

        Args:
            value (JsonValue): The raw conclusion, or ``None``.

        Returns:
            JsonValue: The conclusion, or ``None``.

        Raises:
            SEWorkflowRunInvalidConclusion: When the value is not a ``CheckConclusion``.
        """
        if value is None:
            return None
        return FieldRules.member(value, SEWorkflowRunInvalidConclusion, "conclusion", CheckConclusion)

    @field_validator("link", mode="before")
    def validate_link(cls, value: JsonValue) -> JsonValue:
        """Validate ``link``.

        Args:
            value (JsonValue): The raw link.

        Returns:
            JsonValue: The link.

        Raises:
            SEWorkflowRunInvalidLink: When the value is not an http or https link.
        """
        return FieldRules.link(value, SEWorkflowRunInvalidLink, "link")

    @field_validator("suite_id", mode="before")
    def validate_suite_id(cls, value: JsonValue) -> JsonValue:
        """Validate ``suite_id``.

        Args:
            value (JsonValue): The raw suite id, or ``None``.

        Returns:
            JsonValue: The suite id, or ``None``.

        Raises:
            SEWorkflowRunInvalidSuiteId: When the value is not a positive integer.
        """
        if value is None:
            return None
        return FieldRules.identifier(value, SEWorkflowRunInvalidSuiteId, "suite_id")
