from __future__ import annotations

# Standard library imports
from typing import Type

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from erp_testing.models.stand_in.enums import HttpMethod
from erp_testing.models.stand_in.exceptions import (
    SEStandInRouteInvalidMany,
    SEStandInRouteInvalidMethod,
    SEStandInRouteInvalidModel,
    SEStandInRouteInvalidPath,
)


class StandInRoute(BaseModel):
    """One route a stand-in server answers, with the real model of its answer.

    Attributes:
        method (HttpMethod): The HTTP method of the route.
        path (str): The path of the route, starting with ``/``.
        model (Type[BaseModel]): The real model whose valid empty value is the default answer.
        many (bool): Whether the route answers a list of the model.
    """

    model_config = ConfigDict(extra="forbid", frozen=True, validate_default=True)

    method: HttpMethod = Field(description="The HTTP method of the route.")
    path: str = Field(description="The path of the route, starting with a slash.")
    model: Type[BaseModel] = Field(description="The real model whose valid empty value is the default answer.")
    many: bool = Field(default=False, description="Whether the route answers a list of the model.")

    @field_validator("method", mode="before")
    def validate_method(cls, value: JsonValue) -> JsonValue:
        """Validate ``method``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The method, as it is when it names an ``HttpMethod``.

        Raises:
            SEStandInRouteInvalidMethod: When it is not one of the HTTP methods.
        """
        if isinstance(value, HttpMethod):
            return value
        if not isinstance(value, str) or value not in HttpMethod.__members__:
            raise SEStandInRouteInvalidMethod(
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
            JsonValue: The path, stripped.

        Raises:
            SEStandInRouteInvalidPath: When it is not a text starting with ``/``.
        """
        if not isinstance(value, str) or not value.strip().startswith("/"):
            raise SEStandInRouteInvalidPath(
                f"Invalid path: {value!r}. "  # noqa: E501
                "Must be a text starting with a slash."
            )
        return value.strip()

    @field_validator("model", mode="before")
    def validate_model(cls, value: object) -> object:
        """Validate ``model``.

        Args:
            value (object): The raw input.

        Returns:
            object: The model class, as it is.

        Raises:
            SEStandInRouteInvalidModel: When it is not a Pydantic model class.
        """
        if not isinstance(value, type) or not issubclass(value, BaseModel):
            raise SEStandInRouteInvalidModel(
                f"Invalid model: {value!r}. "  # noqa: E501
                "Must be a Pydantic model class."
            )
        return value

    @field_validator("many", mode="before")
    def validate_many(cls, value: JsonValue) -> JsonValue:
        """Validate ``many``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The flag, or the default when it is ``None``.

        Raises:
            SEStandInRouteInvalidMany: When it is not a boolean.
        """
        if value is None:
            return cls.model_fields["many"].get_default(call_default_factory=True)
        if not isinstance(value, bool):
            raise SEStandInRouteInvalidMany(
                f"Invalid many: {value!r}. "  # noqa: E501
                "Must be a boolean."
            )
        return value
