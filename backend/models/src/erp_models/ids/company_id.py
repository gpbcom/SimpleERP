from __future__ import annotations

# Standard library imports
from typing import ClassVar, Type

# First-party imports
from erp_models.base.opaque_id import OpaqueId
from erp_models.ids.exceptions import SECompanyIdInvalidValue


class CompanyId(OpaqueId):
    """The opaque identifier of a company.

    Attributes:
        INVALID_VALUE (Type[Exception]): The exception raised for an invalid ``value``.
        value (str): The identifier, stripped of surrounding spaces.

    Notes:
        - E-T01-01 gives the id only as a record (example ``C-12``), so the text is kept as given and **never
          parsed** by a service.
        - A ``CompanyId`` never equals a ``RecordId`` of the same text, because Pydantic compares the model types.
    """

    INVALID_VALUE: ClassVar[Type[Exception]] = SECompanyIdInvalidValue
