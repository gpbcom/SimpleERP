from __future__ import annotations

# Third-party imports
from erp_models.base.frozen_erp_model import FrozenErpModel
from pydantic import Field, JsonValue, field_validator

# First-party imports
from erp_context.models.context.exceptions import SERequestContextInvalidRequestId, SERequestContextInvalidUser
from erp_context.models.context.user_context import UserContext


class RequestContext(FrozenErpModel):
    """What every request carries to the service and storage layers.

    Attributes:
        user (UserContext): The user and company the request acts for.
        request_id (str): The identifier of the request, stripped of surrounding spaces.
    """

    user: UserContext = Field(description="The user and company the request acts for.")
    request_id: str = Field(description="The identifier of the request, a non-empty text.")

    @field_validator("user", mode="before")
    def validate_user(cls, value: JsonValue | UserContext) -> JsonValue | UserContext:
        """Validate ``user``.

        Args:
            value (JsonValue | UserContext): The raw input.

        Returns:
            JsonValue | UserContext: The user context, or its raw form for Pydantic to build.

        Raises:
            SERequestContextInvalidUser: When it is neither a ``UserContext`` nor its mapping.
        """
        if not isinstance(value, (UserContext, dict)):
            raise SERequestContextInvalidUser(
                f"Invalid user: {value!r}. "  # noqa: E501
                "Must be a UserContext."
            )
        return value

    @field_validator("request_id", mode="before")
    def validate_request_id(cls, value: JsonValue) -> JsonValue:
        """Validate ``request_id``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The text, stripped.

        Raises:
            SERequestContextInvalidRequestId: When it is not a text, or is empty.
        """
        if not isinstance(value, str) or not value.strip():
            raise SERequestContextInvalidRequestId(
                f"Invalid request_id: {value!r}. "  # noqa: E501
                "Must be a non-empty text."
            )
        return value.strip()
