from __future__ import annotations

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from harness_core.models.git.change_status import ChangeStatus
from harness_core.models.git.exceptions import SEFileChangeInvalidPath, SEFileChangeInvalidStatus


class FileChange(BaseModel):
    """One file of a git change, with how it changed.

    Attributes:
        path (str): The file's path, relative to the repository root.
        status (ChangeStatus): How the file changed.
    """

    model_config = ConfigDict(extra="forbid", frozen=True)

    path: str = Field(description="The file's path, relative to the repository root.", examples=["src/api/cli/main.py"])
    status: ChangeStatus = Field(description="How the file changed.", examples=["M"])

    @field_validator("path", mode="before")
    def validate_path(cls, value: JsonValue) -> JsonValue:
        """Validate ``path``.

        Args:
            value (JsonValue): The raw path.

        Returns:
            JsonValue: The path, stripped.

        Raises:
            SEFileChangeInvalidPath: When the path is not a non-empty string.
        """
        if not isinstance(value, str) or not value.strip():
            raise SEFileChangeInvalidPath(
                f"Invalid path: {value!r}. "  # noqa: E501
                "Must be a non-empty string."
            )
        return value.strip()

    @field_validator("status", mode="before")
    def validate_status(cls, value: JsonValue) -> JsonValue:
        """Validate ``status``.

        Args:
            value (JsonValue): The raw status letter, such as ``M`` or ``R100``.

        Returns:
            JsonValue: The status letter alone.

        Raises:
            SEFileChangeInvalidStatus: When the value is not one of git's status letters.

        Notes:
            Renames and copies carry a similarity score (``R100``): only the letter is kept.
        """
        letters = {status.value for status in ChangeStatus}
        if not isinstance(value, str) or not value or value[0] not in letters:
            raise SEFileChangeInvalidStatus(
                f"Invalid status: {value!r}. "  # noqa: E501
                f"Must start with one of {sorted(letters)}."
            )
        return value[0]
