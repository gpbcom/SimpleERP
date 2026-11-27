from __future__ import annotations

# Standard library imports
from typing import ClassVar, Type

# First-party imports
from erp_models.base.opaque_id import OpaqueId
from erp_models.ids.exceptions import SERecordIdInvalidValue


class RecordId(OpaqueId):
    """The opaque identifier of any record.

    Attributes:
        INVALID_VALUE (Type[Exception]): The exception raised for an invalid ``value``.
        value (str): The identifier, stripped of surrounding spaces.
    """

    INVALID_VALUE: ClassVar[Type[Exception]] = SERecordIdInvalidValue
