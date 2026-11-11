from __future__ import annotations

# Standard library imports
from enum import StrEnum, unique


@unique
class FormField(StrEnum):
    """The fields of the issue forms that ``ticket-docs apply-form`` turns into labels and links.

    Attributes:
        COMPONENT (str): The ticket's component label, such as ``BACKEND``.
        FEATURE (str): The number of the ticket's parent feature.
        FAMILY (str): The feature's family label, such as ``PRODUCT``.
        TYPE (str): The ticket's type, such as ``bug``.
        PRIORITY (str): The issue's priority, such as ``high``.

    Notes:
        Each value is the field's label in ``.github/ISSUE_TEMPLATE/``: a form writes it as a ``### <label>``
        heading in the issue body, above the answer.
    """

    COMPONENT = "Component"
    FEATURE = "Feature"
    FAMILY = "Family"
    TYPE = "Type"
    PRIORITY = "Priority"
