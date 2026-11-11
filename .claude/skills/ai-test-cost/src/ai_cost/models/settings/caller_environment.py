from __future__ import annotations

# Standard library imports
from pathlib import Path
from typing import Optional

# Third-party imports
from pydantic import Field, JsonValue, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

# First-party imports
from ai_cost.models.settings.exceptions import (
    SECallerEnvironmentInvalidApiKeyId,
    SECallerEnvironmentInvalidCallerCwd,
)


class CallerEnvironment(BaseSettings):
    """The harmless values the caller's environment may set, through ``AI_COST_`` variables.

    Attributes:
        caller_cwd (Path): The folder ``ai-cost`` was called from, where a guarded command runs.
        api_key_id (Optional[str]): The id of the API key whose usage is measured, ``None`` for the whole organisation.

    Notes:
        - Nothing here can loosen the guard: the cap, the kill ratio, the usage source and the files are in
          ``GuardSettings``, which never reads the environment.
        - ``caller_cwd`` is set by ``bin/ai-cost`` (``AI_COST_CALLER_CWD``), because ``uv run --project`` may run the
          tool from another folder.
        - The admin key is a secret: the usage client reads it from ``ANTHROPIC_ADMIN_KEY`` itself.
    """

    model_config = SettingsConfigDict(env_prefix="AI_COST_", extra="forbid", validate_default=True)

    caller_cwd: Path = Field(
        default_factory=Path.cwd,
        description="The folder ai-cost was called from, where a guarded command runs.",
        examples=["/home/dev/simple-erp"],
    )
    api_key_id: Optional[str] = Field(
        default=None,
        description="The id of the API key whose usage is measured, None for the whole organisation.",
        examples=["apikey_01Rj2N8SVvo6BePZj99NhmiT"],
    )

    @field_validator("caller_cwd", mode="before")
    def validate_caller_cwd(cls, value: JsonValue) -> JsonValue:
        """Validate ``caller_cwd``.

        Args:
            value (JsonValue): The raw folder: a ``Path`` or a string.

        Returns:
            JsonValue: The folder, ``~`` expanded, as a string, or the current folder for ``None``.

        Raises:
            SECallerEnvironmentInvalidCallerCwd: When the value is not a non-empty path.
        """
        if value is None:
            return str(Path.cwd())
        text = str(value) if isinstance(value, Path) else value
        if not isinstance(text, str) or not text.strip():
            raise SECallerEnvironmentInvalidCallerCwd(
                f"Invalid caller_cwd: {value!r}. "  # noqa: E501
                "Must be a non-empty path."
            )
        return str(Path(text.strip()).expanduser())

    @field_validator("api_key_id", mode="before")
    def validate_api_key_id(cls, value: JsonValue) -> JsonValue:
        """Validate ``api_key_id``.

        Args:
            value (JsonValue): The raw API key id, or ``None``.

        Returns:
            JsonValue: The id, stripped, or ``None``.

        Raises:
            SECallerEnvironmentInvalidApiKeyId: When the value is not a non-empty string.
        """
        if value is None:
            return None
        if not isinstance(value, str) or not value.strip():
            raise SECallerEnvironmentInvalidApiKeyId(
                f"Invalid api_key_id: {value!r}. "  # noqa: E501
                "Must be an API key id such as apikey_01Rj2N8SVvo6BePZj99NhmiT."
            )
        return value.strip()
