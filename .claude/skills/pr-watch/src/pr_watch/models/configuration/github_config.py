from __future__ import annotations

# Standard library imports
from typing import List

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from pr_watch.models.configuration.exceptions import (
    SEGithubConfigInvalidApiUrl,
    SEGithubConfigInvalidApiVersion,
    SEGithubConfigInvalidEnvironments,
    SEGithubConfigInvalidQaEnvironment,
    SEGithubConfigInvalidStageWorkflow,
)
from pr_watch.models.validation.field_rules import FieldRules


class GithubConfig(BaseModel):
    """How the watcher reads GitHub.

    Attributes:
        api_url (str): The REST API root.
        api_version (str): The REST API version sent in ``X-GitHub-Api-Version``.
        stage_workflow (str): The file name of the workflow that deploys a stage.
        environments (List[str]): The deployment environments whose status is read.
        qa_environment (str): The environment whose pending approval can become a ``qa_waiting`` event.

    Notes:
        The token is never configured: it is read from ``GITHUB_TOKEN`` or ``gh auth token`` when it is needed.
    """

    model_config = ConfigDict(extra="forbid")

    api_url: str = Field(description="The REST API root.", examples=["https://api.github.com"])
    api_version: str = Field(
        description="The REST API version sent in ``X-GitHub-Api-Version``.", examples=["2022-11-28"]
    )
    stage_workflow: str = Field(
        description="The file name of the workflow that deploys a stage.", examples=["stage.yml"]
    )
    environments: List[str] = Field(
        description="The deployment environments whose status is read.", examples=[["dev", "qa"]]
    )
    qa_environment: str = Field(
        description="The environment whose pending approval can become a ``qa_waiting`` event.", examples=["qa"]
    )

    @field_validator("api_url", mode="before")
    def validate_api_url(cls, value: JsonValue) -> JsonValue:
        """Validate ``api_url``.

        Args:
            value (JsonValue): The raw api url.

        Returns:
            JsonValue: The api url.

        Raises:
            SEGithubConfigInvalidApiUrl: When the value is not an http or https link.
        """
        return FieldRules.link(value, SEGithubConfigInvalidApiUrl, "api_url")

    @field_validator("api_version", mode="before")
    def validate_api_version(cls, value: JsonValue) -> JsonValue:
        """Validate ``api_version``.

        Args:
            value (JsonValue): The raw api version.

        Returns:
            JsonValue: The api version.

        Raises:
            SEGithubConfigInvalidApiVersion: When the value is not a non-empty string.
        """
        return FieldRules.text(value, SEGithubConfigInvalidApiVersion, "api_version")

    @field_validator("stage_workflow", mode="before")
    def validate_stage_workflow(cls, value: JsonValue) -> JsonValue:
        """Validate ``stage_workflow``.

        Args:
            value (JsonValue): The raw stage workflow.

        Returns:
            JsonValue: The stage workflow.

        Raises:
            SEGithubConfigInvalidStageWorkflow: When the value is not a non-empty string.
        """
        return FieldRules.text(value, SEGithubConfigInvalidStageWorkflow, "stage_workflow")

    @field_validator("environments", mode="before")
    def validate_environments(cls, value: JsonValue) -> JsonValue:
        """Validate ``environments``.

        Args:
            value (JsonValue): The raw environments.

        Returns:
            JsonValue: The environments.

        Raises:
            SEGithubConfigInvalidEnvironments: When the value is not a list of non-empty strings.
        """
        return FieldRules.texts(value, SEGithubConfigInvalidEnvironments, "environments")

    @field_validator("qa_environment", mode="before")
    def validate_qa_environment(cls, value: JsonValue) -> JsonValue:
        """Validate ``qa_environment``.

        Args:
            value (JsonValue): The raw qa environment.

        Returns:
            JsonValue: The qa environment.

        Raises:
            SEGithubConfigInvalidQaEnvironment: When the value is not a non-empty string.
        """
        return FieldRules.text(value, SEGithubConfigInvalidQaEnvironment, "qa_environment")
