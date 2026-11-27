from __future__ import annotations

# Standard library imports
from typing import ClassVar

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from erp_testing.models.postgres.exceptions import (
    SEPostgresConnectionInvalidDatabase,
    SEPostgresConnectionInvalidHost,
    SEPostgresConnectionInvalidPort,
    SEPostgresConnectionInvalidUser,
)


class PostgresConnection(BaseModel):
    """Where and how to reach a running PostgreSQL test server.

    Attributes:
        model_config (ConfigDict): Refuses unknown keys and freezes the model.
        PORT_MIN (int): The lowest valid port.
        PORT_MAX (int): The highest valid port.
        host (str): The host the server listens on.
        port (int): The port the server listens on.
        database (str): The name of the database.
        user (str): The name of the user.

    Notes:
        **The connection holds no password**, so that no secret sits in a model or a log.
    """

    model_config = ConfigDict(extra="forbid", frozen=True)

    PORT_MIN: ClassVar[int] = 1
    PORT_MAX: ClassVar[int] = 65535

    host: str = Field(description="The host the server listens on.")
    port: int = Field(description="The port the server listens on.")
    database: str = Field(description="The name of the database.")
    user: str = Field(description="The name of the user.")

    @field_validator("host", mode="before")
    def validate_host(cls, value: JsonValue) -> JsonValue:
        """Validate ``host``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The host, stripped.

        Raises:
            SEPostgresConnectionInvalidHost: If it is not a non-empty string.
        """
        if not isinstance(value, str) or not value.strip():
            raise SEPostgresConnectionInvalidHost(
                f"Invalid host: {value!r}. "  # noqa: E501
                "Must be a non-empty string."
            )
        return value.strip()

    @field_validator("port", mode="before")
    def validate_port(cls, value: JsonValue) -> JsonValue:
        """Validate ``port``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The port.

        Raises:
            SEPostgresConnectionInvalidPort: If it is not an integer within the bounds.
        """
        if isinstance(value, bool) or not isinstance(value, int) or not cls.PORT_MIN <= value <= cls.PORT_MAX:
            raise SEPostgresConnectionInvalidPort(
                f"Invalid port: {value!r}. "  # noqa: E501
                f"Must be in [{cls.PORT_MIN}, {cls.PORT_MAX}]."
            )
        return value

    @field_validator("database", mode="before")
    def validate_database(cls, value: JsonValue) -> JsonValue:
        """Validate ``database``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The name, stripped.

        Raises:
            SEPostgresConnectionInvalidDatabase: If it is not a non-empty string.
        """
        if not isinstance(value, str) or not value.strip():
            raise SEPostgresConnectionInvalidDatabase(
                f"Invalid database: {value!r}. "  # noqa: E501
                "Must be a non-empty string."
            )
        return value.strip()

    @field_validator("user", mode="before")
    def validate_user(cls, value: JsonValue) -> JsonValue:
        """Validate ``user``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The name, stripped.

        Raises:
            SEPostgresConnectionInvalidUser: If it is not a non-empty string.
        """
        if not isinstance(value, str) or not value.strip():
            raise SEPostgresConnectionInvalidUser(
                f"Invalid user: {value!r}. "  # noqa: E501
                "Must be a non-empty string."
            )
        return value.strip()

    ############################
    # Publicly Exposed Methods #
    ############################

    @property
    def dsn(self) -> str:
        """Build the connection string, without a password.

        Returns:
            str: ``postgresql://<user>@<host>:<port>/<database>``.
        """
        return f"postgresql://{self.user}@{self.host}:{self.port}/{self.database}"
