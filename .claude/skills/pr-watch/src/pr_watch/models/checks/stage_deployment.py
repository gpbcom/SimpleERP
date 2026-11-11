from __future__ import annotations

# Standard library imports
from typing import Optional

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from pr_watch.models.checks.exceptions import (
    SEStageDeploymentInvalidDeploymentId,
    SEStageDeploymentInvalidEnvironment,
    SEStageDeploymentInvalidLink,
    SEStageDeploymentInvalidState,
)
from pr_watch.models.enums import DeploymentState
from pr_watch.models.validation.field_rules import FieldRules


class StageDeployment(BaseModel):
    """The latest deployment of a commit to a stage environment.

    Attributes:
        environment (str): The environment, ``dev`` or ``qa``.
        deployment_id (int): The deployment's identifier.
        state (Optional[DeploymentState]): Its latest status, ``None`` before the first one.
        link (Optional[str]): The log or page of its latest status.
    """

    model_config = ConfigDict(extra="forbid")

    environment: str = Field(description="The environment, ``dev`` or ``qa``.", examples=["dev"])
    deployment_id: int = Field(description="The deployment's identifier.", examples=[701])
    state: Optional[DeploymentState] = Field(
        default=None, description="Its latest status, ``None`` before the first one.", examples=["failure"]
    )
    link: Optional[str] = Field(
        default=None,
        description="The log or page of its latest status.",
        examples=["https://github.com/gpbcom/simple-erp/actions/runs/601"],
    )

    @field_validator("environment", mode="before")
    def validate_environment(cls, value: JsonValue) -> JsonValue:
        """Validate ``environment``.

        Args:
            value (JsonValue): The raw environment.

        Returns:
            JsonValue: The environment.

        Raises:
            SEStageDeploymentInvalidEnvironment: When the value is not a non-empty string.
        """
        return FieldRules.text(value, SEStageDeploymentInvalidEnvironment, "environment")

    @field_validator("deployment_id", mode="before")
    def validate_deployment_id(cls, value: JsonValue) -> JsonValue:
        """Validate ``deployment_id``.

        Args:
            value (JsonValue): The raw deployment id.

        Returns:
            JsonValue: The deployment id.

        Raises:
            SEStageDeploymentInvalidDeploymentId: When the value is not a positive integer.
        """
        return FieldRules.identifier(value, SEStageDeploymentInvalidDeploymentId, "deployment_id")

    @field_validator("state", mode="before")
    def validate_state(cls, value: JsonValue) -> JsonValue:
        """Validate ``state``.

        Args:
            value (JsonValue): The raw state, or ``None``.

        Returns:
            JsonValue: The state, or ``None``.

        Raises:
            SEStageDeploymentInvalidState: When the value is not a ``DeploymentState``.
        """
        if value is None:
            return None
        return FieldRules.member(value, SEStageDeploymentInvalidState, "state", DeploymentState)

    @field_validator("link", mode="before")
    def validate_link(cls, value: JsonValue) -> JsonValue:
        """Validate ``link``.

        Args:
            value (JsonValue): The raw link, or ``None``.

        Returns:
            JsonValue: The link, or ``None``.

        Raises:
            SEStageDeploymentInvalidLink: When the value is not an http or https link.
        """
        if value is None:
            return None
        return FieldRules.link(value, SEStageDeploymentInvalidLink, "link")
