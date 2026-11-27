from __future__ import annotations

# Standard library imports
from typing import ClassVar, List, Self, Type

# Third-party imports
from erp_models.catalogs.yaml_catalog import YamlCatalog
from pydantic import Field, model_validator

# First-party imports
from erp_context.models.refusals.enums import RefusalReason
from erp_context.models.refusals.exceptions import SERefusalCatalogInvalidEntries, SERefusalCatalogUnreadable
from erp_context.models.refusals.refusal_code import RefusalCode


class RefusalCatalog(YamlCatalog):
    """The refusal catalogue: the code, status and message keys of every reason a request is refused.

    Attributes:
        UNREADABLE (Type[Exception]): The exception ``load`` raises when the file cannot be read.
        entries (List[RefusalCode]): One entry per ``RefusalReason``.

    Notes:
        - A reason without an entry, or with two, is refused, so that every refusal has one code.
        - ``entries`` has no field validator: a value that is not a list is refused by Pydantic, and the rules
          across entries are checked once in ``validate_entries``.
    """

    UNREADABLE: ClassVar[Type[Exception]] = SERefusalCatalogUnreadable

    entries: List[RefusalCode] = Field(description="One entry per reason a request is refused.")

    @model_validator(mode="after")
    def validate_entries(self) -> Self:
        """Check the entries across each other.

        Returns:
            Self: The catalogue, unchanged.

        Raises:
            SERefusalCatalogInvalidEntries: When a reason has no entry or several, or a code is repeated.
        """
        reasons = sorted(entry.reason.value for entry in self.entries)
        if reasons != sorted(reason.value for reason in RefusalReason):
            raise SERefusalCatalogInvalidEntries(
                f"Invalid entries: {reasons!r}. "  # noqa: E501
                "Must hold exactly one entry per reason."
            )
        codes = [entry.code for entry in self.entries]
        if len(codes) != len(set(codes)):
            raise SERefusalCatalogInvalidEntries(
                "Invalid entries: a code is repeated. "  # noqa: E501
                "Must hold distinct codes."
            )
        return self

    ############################
    # Publicly Exposed Methods #
    ############################

    def code_for(self, reason: RefusalReason) -> RefusalCode:
        """Return the entry of one reason.

        Args:
            reason (RefusalReason): Why the request was refused.

        Returns:
            RefusalCode: The entry of the reason.
        """
        return next(entry for entry in self.entries if entry.reason is reason)
