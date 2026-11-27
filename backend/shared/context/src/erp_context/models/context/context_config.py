from __future__ import annotations

# Standard library imports
from typing import List

# Third-party imports
from erp_models.base.erp_model import ErpModel
from pydantic import ConfigDict, Field, JsonValue, field_validator

# First-party imports
from erp_context.models.context.exceptions import (
    SEContextConfigInvalidCompanyHeader,
    SEContextConfigInvalidPublicPaths,
    SEContextConfigInvalidRequestHeader,
    SEContextConfigInvalidUserHeader,
)


class ContextConfig(ErpModel):
    """The configuration of the company context.

    Attributes:
        company_header (str): The request header that carries the company.
        user_header (str): The request header that carries the user.
        request_header (str): The request header that carries the request identifier.
        public_paths (List[str]): The paths served without a company context, each starting with ``/``.
    """

    model_config = ConfigDict(extra="forbid", validate_default=True)

    company_header: str = Field(default="X-Company-Id", description="The request header that carries the company.")
    user_header: str = Field(default="X-User-Id", description="The request header that carries the user.")
    request_header: str = Field(default="X-Request-Id", description="The request header that carries the request id.")
    public_paths: List[str] = Field(
        default_factory=list, description="The paths served without a company context, each starting with ``/``."
    )

    @field_validator("company_header", mode="before")
    def validate_company_header(cls, value: JsonValue) -> JsonValue:
        """Validate ``company_header``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The header name, stripped, or the default for ``None``.

        Raises:
            SEContextConfigInvalidCompanyHeader: When it is not a text, or is empty.
        """
        if value is None:
            return cls.model_fields["company_header"].get_default(call_default_factory=True)
        if not isinstance(value, str) or not value.strip():
            raise SEContextConfigInvalidCompanyHeader(
                f"Invalid company_header: {value!r}. "  # noqa: E501
                "Must be a non-empty text."
            )
        return value.strip()

    @field_validator("user_header", mode="before")
    def validate_user_header(cls, value: JsonValue) -> JsonValue:
        """Validate ``user_header``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The header name, stripped, or the default for ``None``.

        Raises:
            SEContextConfigInvalidUserHeader: When it is not a text, or is empty.
        """
        if value is None:
            return cls.model_fields["user_header"].get_default(call_default_factory=True)
        if not isinstance(value, str) or not value.strip():
            raise SEContextConfigInvalidUserHeader(
                f"Invalid user_header: {value!r}. "  # noqa: E501
                "Must be a non-empty text."
            )
        return value.strip()

    @field_validator("request_header", mode="before")
    def validate_request_header(cls, value: JsonValue) -> JsonValue:
        """Validate ``request_header``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The header name, stripped, or the default for ``None``.

        Raises:
            SEContextConfigInvalidRequestHeader: When it is not a text, or is empty.
        """
        if value is None:
            return cls.model_fields["request_header"].get_default(call_default_factory=True)
        if not isinstance(value, str) or not value.strip():
            raise SEContextConfigInvalidRequestHeader(
                f"Invalid request_header: {value!r}. "  # noqa: E501
                "Must be a non-empty text."
            )
        return value.strip()

    @field_validator("public_paths", mode="before")
    def validate_public_paths(cls, value: JsonValue) -> JsonValue:
        """Validate ``public_paths``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The paths, stripped, or an empty list for ``None``.

        Raises:
            SEContextConfigInvalidPublicPaths: When it is not a list of texts that start with ``/``.
        """
        if value is None:
            return cls.model_fields["public_paths"].get_default(call_default_factory=True)
        if not isinstance(value, list):
            raise SEContextConfigInvalidPublicPaths(
                f"Invalid public_paths: {value!r}. "  # noqa: E501
                "Must be a list of paths."
            )
        paths: List[JsonValue] = []
        for path in value:
            if not isinstance(path, str) or not path.strip().startswith("/"):
                raise SEContextConfigInvalidPublicPaths(
                    f"Invalid public_paths: {value!r}. "  # noqa: E501
                    "Must hold only texts that start with '/'."
                )
            paths.append(path.strip())
        return paths
