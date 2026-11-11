from __future__ import annotations

# Standard library imports
from typing import ClassVar

# Third-party imports
from pydantic import Field, JsonValue, field_validator

# First-party imports
from harness_core.models.catalogs.yaml_catalog import YamlCatalog
from release_notes.models.catalogs.exceptions import (
    SEGithubApiInvalidApiUrl,
    SEGithubApiInvalidApiVersion,
    SEGithubApiUnreadable,
)


class GithubApi(YamlCatalog):
    """How the tool reads GitHub's REST API, read from ``conf/github-api.yaml``.

    Attributes:
        UNREADABLE (type[Exception]): The exception raised when the file cannot be read.
        api_url (str): The REST API root.
        api_version (str): The REST API version sent in ``X-GitHub-Api-Version``.

    Notes:
        The token is never configured: it is read from ``GITHUB_TOKEN`` or ``gh auth token`` when it is needed.
    """

    UNREADABLE: ClassVar[type[Exception]] = SEGithubApiUnreadable

    api_url: str = Field(description="The REST API root.", examples=["https://api.github.com"])
    api_version: str = Field(
        description="The REST API version sent in ``X-GitHub-Api-Version``.", examples=["2022-11-28"]
    )

    @field_validator("api_url", mode="before")
    def validate_api_url(cls, value: JsonValue) -> JsonValue:
        """Validate ``api_url``.

        Args:
            value (JsonValue): The raw link.

        Returns:
            JsonValue: The link, stripped.

        Raises:
            SEGithubApiInvalidApiUrl: When the value is not an http or https link.
        """
        if not isinstance(value, str) or not value.strip().startswith(("http://", "https://")):
            raise SEGithubApiInvalidApiUrl(
                f"Invalid api_url: {value!r}. "  # noqa: E501
                "Must be an http or https link."
            )
        return value.strip()

    @field_validator("api_version", mode="before")
    def validate_api_version(cls, value: JsonValue) -> JsonValue:
        """Validate ``api_version``.

        Args:
            value (JsonValue): The raw version.

        Returns:
            JsonValue: The version, stripped.

        Raises:
            SEGithubApiInvalidApiVersion: When the value is not a non-empty string.
        """
        if not isinstance(value, str) or not value.strip():
            raise SEGithubApiInvalidApiVersion(
                f"Invalid api_version: {value!r}. "  # noqa: E501
                "Must be a non-empty string."
            )
        return value.strip()
