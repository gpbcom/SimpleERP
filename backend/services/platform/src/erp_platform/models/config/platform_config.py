from __future__ import annotations

# Standard library imports
from typing import List

# First-party imports
from erp_config.models.config_section import ConfigSection

# Third-party imports
from pydantic import Field, JsonValue, field_validator

from erp_platform.models.config.exceptions import (
    SEPlatformConfigInvalidErrorCodesPath,
    SEPlatformConfigInvalidPublicPaths,
)


class PlatformConfig(ConfigSection):
    """The configuration of the platform service, read from ``conf/app.yaml``.

    Attributes:
        public_paths (List[str]): The paths served without a bearer token, each starting with ``/``.
        error_codes_path (str): The error catalogue file, relative to the working folder.

    Notes:
        **There is no ``host`` and no ``port``**: they are uvicorn's options, never the service's (D406).
    """

    public_paths: List[str] = Field(
        default_factory=lambda: ["/v1/health"], description="The paths served without a bearer token."
    )
    error_codes_path: str = Field(
        default="conf/catalogs/error_codes.yaml",
        description="The error catalogue file, relative to the working folder.",
    )

    @field_validator("public_paths", mode="before")
    def validate_public_paths(cls, value: JsonValue) -> JsonValue:
        """Validate ``public_paths``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The paths, each stripped.

        Raises:
            SEPlatformConfigInvalidPublicPaths: When it is not a list of texts that start with ``/``.
        """
        if value is None:
            return cls.model_fields["public_paths"].get_default(call_default_factory=True)
        if not isinstance(value, list):
            raise SEPlatformConfigInvalidPublicPaths(
                f"Invalid public_paths: {value!r}. "  # noqa: E501
                "Must be a list of paths that start with a slash."
            )
        paths: List[JsonValue] = []
        for path in value:
            if not isinstance(path, str) or not path.strip().startswith("/"):
                raise SEPlatformConfigInvalidPublicPaths(
                    f"Invalid public_paths: {value!r}. "  # noqa: E501
                    "Must be a list of paths that start with a slash."
                )
            paths.append(path.strip())
        return paths

    @field_validator("error_codes_path", mode="before")
    def validate_error_codes_path(cls, value: JsonValue) -> JsonValue:
        """Validate ``error_codes_path``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The path, stripped.

        Raises:
            SEPlatformConfigInvalidErrorCodesPath: When it is not a non-empty text.
        """
        if value is None:
            return cls.model_fields["error_codes_path"].get_default(call_default_factory=True)
        if not isinstance(value, str) or not value.strip():
            raise SEPlatformConfigInvalidErrorCodesPath(
                f"Invalid error_codes_path: {value!r}. "  # noqa: E501
                "Must be a non-empty path."
            )
        return value.strip()
