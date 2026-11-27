from __future__ import annotations

# Standard library imports
from enum import StrEnum, unique


@unique
class ContractChangeKind(StrEnum):
    """The kinds of breaking change the contract check reports (REQ-T05-05).

    Attributes:
        PATH_REMOVED (str): A path of the committed document is gone.
        OPERATION_REMOVED (str): An operation of a path is gone.
        PARAMETER_REMOVED (str): A parameter of an operation is gone.
        SCHEMA_REMOVED (str): A component schema is gone.
        PROPERTY_REMOVED (str): A property of a schema is gone.
        TYPE_CHANGED (str): The type of a property or a parameter changed.
    """

    PATH_REMOVED = "path_removed"
    OPERATION_REMOVED = "operation_removed"
    PARAMETER_REMOVED = "parameter_removed"
    SCHEMA_REMOVED = "schema_removed"
    PROPERTY_REMOVED = "property_removed"
    TYPE_CHANGED = "type_changed"
