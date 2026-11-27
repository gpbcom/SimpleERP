from __future__ import annotations

# Standard library imports
import re
from typing import ClassVar, Dict, Type

# Third-party imports
from pydantic import ConfigDict, Field, JsonValue, field_validator

# First-party imports
from erp_models.catalogs.yaml_catalog import YamlCatalog
from erp_models.errors.catalogs.exceptions import (
    SEErrorCatalogInvalidCodes,
    SEErrorCatalogUnknownCode,
    SEErrorCatalogUnreadable,
)
from erp_models.errors.entries.error_code_entry import ErrorCodeEntry


class ErrorCatalog(YamlCatalog):
    """The error code catalogue: every code with its title, why and action keys and its support reference.

    Attributes:
        UNREADABLE (Type[Exception]): The exception ``load`` raises when the file cannot be read.
        CODE_PATTERN (str): The pattern of a code, such as ``SITE-CLOSE-01``.
        codes (Dict[str, ErrorCodeEntry]): The entries, by code.

    Notes:
        - An unknown code is refused, never replaced by a generic message (REQ-T05-03).
        - The entries are validated by ``ErrorCodeEntry``.
    """

    model_config = ConfigDict(extra="forbid", frozen=True)

    UNREADABLE: ClassVar[Type[Exception]] = SEErrorCatalogUnreadable
    CODE_PATTERN: ClassVar[str] = r"^[A-Z][A-Z0-9]*(-[A-Z0-9]+)*-[0-9]{2}$"

    codes: Dict[str, ErrorCodeEntry] = Field(description="The entries of the catalogue, by code.")

    @field_validator("codes", mode="before")
    def validate_codes(cls, value: JsonValue) -> JsonValue:
        """Validate ``codes``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The mapping, unchanged.

        Raises:
            SEErrorCatalogInvalidCodes: When it is not a mapping, is empty, or has a key that is not a code.
        """
        if not isinstance(value, dict) or not value:
            raise SEErrorCatalogInvalidCodes(
                f"Invalid codes: {type(value).__name__}. "  # noqa: E501
                "Must be a non-empty mapping of codes to entries."
            )
        for code in value:
            if not isinstance(code, str) or re.fullmatch(cls.CODE_PATTERN, code) is None:
                raise SEErrorCatalogInvalidCodes(
                    f"Invalid code: {code!r}. "  # noqa: E501
                    "Must be a code such as SITE-CLOSE-01."
                )
        return value

    ############################
    # Publicly Exposed Methods #
    ############################

    def resolve(self, code: str) -> ErrorCodeEntry:
        """Resolve one code to its entry.

        Args:
            code (str): The code to look up.

        Returns:
            ErrorCodeEntry: The entry of the code.

        Raises:
            SEErrorCatalogUnknownCode: When the code is not in the catalogue.
        """
        entry = self.codes.get(code)
        if entry is None:
            raise SEErrorCatalogUnknownCode(
                f"Unknown error code: {code!r}. "  # noqa: E501
                "Must be a code of the error catalogue."
            )
        return entry
