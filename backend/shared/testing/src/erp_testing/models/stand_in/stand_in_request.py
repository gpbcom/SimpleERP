from __future__ import annotations

# Standard library imports
from typing import Dict

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from erp_testing.models.stand_in.enums import HttpMethod
from erp_testing.models.stand_in.exceptions import (
    SEStandInRequestInvalidBody,
    SEStandInRequestInvalidHeaders,
    SEStandInRequestInvalidMethod,
    SEStandInRequestInvalidPath,
)


class StandInRequest(BaseModel):
    """One request a stand-in server received.

    Attributes:
        method (HttpMethod): The HTTP method of the request.
        path (str): The path with its query string, starting with ``/``.
        headers (Dict[str, str]): The request headers.
        body (str): The request body, empty when there is none.
    """

    model_config = ConfigDict(extra="forbid", frozen=True, validate_default=True)

    method: HttpMethod = Field(description="The HTTP method of the request.")
    path: str = Field(description="The path with its query string, starting with a slash.")
    headers: Dict[str, str] = Field(default_factory=dict, description="The request headers.")
    body: str = Field(default="", description="The request body, empty when there is none.")

    @field_validator("method", mode="before")
    def validate_method(cls, value: JsonValue) -> JsonValue:
        """Validate ``method``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The method, as it is when it names an ``HttpMethod``.

        Raises:
            SEStandInRequestInvalidMethod: When it is not one of the HTTP methods.
        """
        if isinstance(value, HttpMethod):
            return value
        if not isinstance(value, str) or value not in HttpMethod.__members__:
            raise SEStandInRequestInvalidMethod(
                f"Invalid method: {value!r}. "  # noqa: E501
                f"Must be one of {sorted(HttpMethod.__members__)}."
            )
        return value

    @field_validator("path", mode="before")
    def validate_path(cls, value: JsonValue) -> JsonValue:
        """Validate ``path``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The path.

        Raises:
            SEStandInRequestInvalidPath: When it is not a text starting with ``/``.
        """
        if not isinstance(value, str) or not value.startswith("/"):
            raise SEStandInRequestInvalidPath(
                f"Invalid path: {value!r}. "  # noqa: E501
                "Must be a text starting with a slash."
            )
        return value

    @field_validator("headers", mode="before")
    def validate_headers(cls, value: JsonValue) -> JsonValue:
        """Validate ``headers``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The headers, or the default when it is ``None``.

        Raises:
            SEStandInRequestInvalidHeaders: When it is not a mapping of texts to texts.
        """
        if value is None:
            return cls.model_fields["headers"].get_default(call_default_factory=True)
        if not isinstance(value, dict) or not all(
            isinstance(key, str) and isinstance(item, str) for key, item in value.items()
        ):
            raise SEStandInRequestInvalidHeaders(
                f"Invalid headers: {value!r}. "  # noqa: E501
                "Must be a mapping of texts to texts."
            )
        return value

    @field_validator("body", mode="before")
    def validate_body(cls, value: JsonValue) -> JsonValue:
        """Validate ``body``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The body, or the default when it is ``None``.

        Raises:
            SEStandInRequestInvalidBody: When it is not a text.
        """
        if value is None:
            return cls.model_fields["body"].get_default(call_default_factory=True)
        if not isinstance(value, str):
            raise SEStandInRequestInvalidBody(
                f"Invalid body: {value!r}. "  # noqa: E501
                "Must be a text."
            )
        return value
