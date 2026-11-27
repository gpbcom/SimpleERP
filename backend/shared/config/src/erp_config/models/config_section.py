from __future__ import annotations

# Standard library imports
import re
from typing import ClassVar, Iterator, Optional, Tuple

# Third-party imports
from pydantic import BaseModel, ConfigDict, JsonValue, model_validator

# First-party imports
from erp_config.models.exceptions import SEConfigSectionInvalidKey


class ConfigSection(BaseModel):
    """The base of every section of a service's configuration.

    Attributes:
        model_config (ConfigDict): Refuses unknown keys, validates defaults and freezes the section.
        KEY_SUFFIX (str): The ending of a field name that names a vault entry.
        KEY_PATTERN (str): The characters a vault entry name is made of.
        KEY_LENGTH_MAX (int): The longest vault entry name, in characters.

    Notes:
        - **A field ending in ``_key`` holds only the name of a vault entry, never a secret.** The secret itself lives
          in the credential vault (D240) and never appears in configuration or logs.
        - The check runs before the field types, so that a number or a boolean raises ``SEConfigSectionInvalidKey``
          rather than a generic validation error.
        - The error message names the field and never quotes the value.
        - ``__repr_args__`` masks each ``_key`` value, so ``repr`` and ``str`` never show it.
    """

    model_config = ConfigDict(extra="forbid", validate_default=True, frozen=True)

    KEY_SUFFIX: ClassVar[str] = "_key"
    KEY_PATTERN: ClassVar[str] = r"^[A-Za-z0-9][A-Za-z0-9._/-]*$"
    KEY_LENGTH_MAX: ClassVar[int] = 128

    @model_validator(mode="before")
    @classmethod
    def validate_key_fields(cls, data: JsonValue) -> JsonValue:
        """Validate every field whose name ends in ``_key``.

        Args:
            data (JsonValue): The raw input of the section.

        Returns:
            JsonValue: The input, unchanged.

        Raises:
            SEConfigSectionInvalidKey: If a ``_key`` value is neither ``None`` nor a valid vault entry name.
        """
        if not isinstance(data, dict):
            return data
        for name, value in data.items():
            if not name.endswith(cls.KEY_SUFFIX) or value is None:
                continue
            if (
                not isinstance(value, str)
                or len(value) > cls.KEY_LENGTH_MAX
                or re.match(cls.KEY_PATTERN, value) is None
            ):
                raise SEConfigSectionInvalidKey(
                    f"Invalid {name}. "  # noqa: E501
                    f"Must be the name of a vault entry of at most {cls.KEY_LENGTH_MAX} characters "
                    f"matching {cls.KEY_PATTERN}."
                )
        return data

    ############################
    # Publicly Exposed Methods #
    ############################

    def __repr_args__(self) -> Iterator[Tuple[Optional[str], object]]:
        """Yield the fields to show, with each ``_key`` value masked.

        Returns:
            Iterator[Tuple[Optional[str], object]]: The name and value of each field, ``"***"`` for a ``_key``.
        """
        for name, value in super().__repr_args__():
            yield (name, "***" if name is not None and name.endswith(self.KEY_SUFFIX) else value)
