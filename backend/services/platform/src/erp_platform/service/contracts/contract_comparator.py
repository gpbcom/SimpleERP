from __future__ import annotations

# Standard library imports
from logging import Logger, getLogger
from typing import ClassVar, Dict, List, Optional, Tuple

# Third-party imports
from pydantic import JsonValue

# First-party imports
from erp_platform.models.contracts.contract_change import ContractChange
from erp_platform.models.contracts.enums import ContractChangeKind


class ContractComparator:
    """Find the breaking changes between two OpenAPI documents.

    Attributes:
        PATHS (str): The key of the paths section.
        COMPONENTS (str): The key of the components section.
        SCHEMAS (str): The key of the schemas of the components.
        PROPERTIES (str): The key of the properties of a schema.
        ITEMS (str): The key of the items of an array schema.
        PARAMETERS (str): The key of the parameters of an operation.
        TYPE_KEYWORDS (Tuple[str, ...]): The keywords whose change breaks a schema or a property.
        HTTP_METHODS (Tuple[str, ...]): The keys of a path that are operations.
        logger (Logger): Logger instance.

    Notes:
        - **Additions pass**, because a client written for the committed document still works with more of it
          (REQ-T05-05 criterion 2). Only what the baseline has and the live document lacks, or has changed, is reported.
        - A missing section counts as empty, and the inputs are never mutated, so the rules stay pure functions over
          data (D406).
        - A location is a JSON pointer, so ``~`` is written ``~0`` and ``/`` is written ``~1``.
    """

    PATHS: ClassVar[str] = "paths"
    COMPONENTS: ClassVar[str] = "components"
    SCHEMAS: ClassVar[str] = "schemas"
    PROPERTIES: ClassVar[str] = "properties"
    ITEMS: ClassVar[str] = "items"
    PARAMETERS: ClassVar[str] = "parameters"
    TYPE_KEYWORDS: ClassVar[Tuple[str, ...]] = ("type", "$ref")
    HTTP_METHODS: ClassVar[Tuple[str, ...]] = ("get", "put", "post", "delete", "options", "head", "patch", "trace")

    def __init__(self, logger: Optional[Logger] = None) -> None:
        """Create the comparator.

        Args:
            logger (Optional[Logger]): Logger instance, a module logger when omitted.
        """
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    def _dict_of(self, value: JsonValue) -> Dict[str, JsonValue]:
        """Read a value as an object.

        Args:
            value (JsonValue): Any JSON value, or ``None`` for a missing one.

        Returns:
            Dict[str, JsonValue]: The object, or an empty one when the value is not an object.
        """
        return value if isinstance(value, dict) else {}

    def _child(self, node: Dict[str, JsonValue], key: str) -> Dict[str, JsonValue]:
        """Read one child of a node as an object.

        Args:
            node (Dict[str, JsonValue]): The parent.
            key (str): The key of the child.

        Returns:
            Dict[str, JsonValue]: The child, empty when missing.
        """
        return self._dict_of(node.get(key))

    def _pointer(self, parent: str, key: str) -> str:
        """Append one escaped key to a JSON pointer.

        Args:
            parent (str): The pointer of the parent.
            key (str): The raw key.

        Returns:
            str: The pointer of the child.
        """
        return f"{parent}/{key.replace('~', '~0').replace('/', '~1')}"

    def _parameters_of(self, operation: Dict[str, JsonValue]) -> Dict[str, Dict[str, JsonValue]]:
        """Index the parameters of an operation by place and name.

        Args:
            operation (Dict[str, JsonValue]): The operation.

        Returns:
            Dict[str, Dict[str, JsonValue]]: The parameters, keyed ``<in>/<name>`` with each part escaped.
        """
        raw = operation.get(self.PARAMETERS)
        indexed: Dict[str, Dict[str, JsonValue]] = {}
        for item in raw if isinstance(raw, list) else []:
            parameter = self._dict_of(item)
            place, name = parameter.get("in"), parameter.get("name")
            if isinstance(place, str) and isinstance(name, str):
                indexed[self._pointer(self._pointer("", place), name)[1:]] = parameter
        return indexed

    def _compare_operation(
        self, before: Dict[str, JsonValue], after: Dict[str, JsonValue], location: str, found: List[ContractChange]
    ) -> None:
        """Compare the parameters of an operation present on both sides.

        Args:
            before (Dict[str, JsonValue]): The operation of the committed document.
            after (Dict[str, JsonValue]): The operation of the live document.
            location (str): The pointer of the operation.
            found (List[ContractChange]): Where the changes are added.
        """
        new_parameters = self._parameters_of(after)
        for key in self._parameters_of(before):
            if key not in new_parameters:
                found.append(
                    ContractChange(
                        kind=ContractChangeKind.PARAMETER_REMOVED,
                        location=f"{location}/{self.PARAMETERS}/{key}",
                    )
                )

    def _compare_path_item(
        self, before: Dict[str, JsonValue], after: Dict[str, JsonValue], location: str, found: List[ContractChange]
    ) -> None:
        """Compare the operations of a path present on both sides.

        Args:
            before (Dict[str, JsonValue]): The path item of the committed document.
            after (Dict[str, JsonValue]): The path item of the live document.
            location (str): The pointer of the path.
            found (List[ContractChange]): Where the changes are added.
        """
        for method in self.HTTP_METHODS:
            if method not in before:
                continue
            operation = self._pointer(location, method)
            if method in after:
                self._compare_operation(self._dict_of(before[method]), self._dict_of(after[method]), operation, found)
            else:
                found.append(ContractChange(kind=ContractChangeKind.OPERATION_REMOVED, location=operation))

    def _compare_paths(
        self, baseline: Dict[str, JsonValue], current: Dict[str, JsonValue], found: List[ContractChange]
    ) -> None:
        """Compare the paths, their operations and their parameters.

        Args:
            baseline (Dict[str, JsonValue]): The committed document.
            current (Dict[str, JsonValue]): The live document.
            found (List[ContractChange]): Where the changes are added.
        """
        before, after = self._child(baseline, self.PATHS), self._child(current, self.PATHS)
        root = self._pointer("#", self.PATHS)
        for path, item in before.items():
            location = self._pointer(root, path)
            if path in after:
                self._compare_path_item(self._dict_of(item), self._dict_of(after[path]), location, found)
            else:
                found.append(ContractChange(kind=ContractChangeKind.PATH_REMOVED, location=location))

    def _compare_node(
        self, before: Dict[str, JsonValue], after: Dict[str, JsonValue], location: str, found: List[ContractChange]
    ) -> None:
        """Compare a schema or a property present on both sides, then recurse.

        Args:
            before (Dict[str, JsonValue]): The node of the committed document.
            after (Dict[str, JsonValue]): The node of the live document.
            location (str): The pointer of the node.
            found (List[ContractChange]): Where the changes are added.
        """
        if any(before.get(keyword) != after.get(keyword) for keyword in self.TYPE_KEYWORDS):
            found.append(ContractChange(kind=ContractChangeKind.TYPE_CHANGED, location=location))
        new_properties = self._child(after, self.PROPERTIES)
        for name, node in self._child(before, self.PROPERTIES).items():
            where = self._pointer(self._pointer(location, self.PROPERTIES), name)
            if name in new_properties:
                self._compare_node(self._dict_of(node), self._dict_of(new_properties[name]), where, found)
            else:
                found.append(ContractChange(kind=ContractChangeKind.PROPERTY_REMOVED, location=where))
        if self.ITEMS in before and self.ITEMS in after:
            self._compare_node(
                self._child(before, self.ITEMS),
                self._child(after, self.ITEMS),
                self._pointer(location, self.ITEMS),
                found,
            )

    def _compare_schemas(
        self, baseline: Dict[str, JsonValue], current: Dict[str, JsonValue], found: List[ContractChange]
    ) -> None:
        """Compare the component schemas.

        Args:
            baseline (Dict[str, JsonValue]): The committed document.
            current (Dict[str, JsonValue]): The live document.
            found (List[ContractChange]): Where the changes are added.
        """
        before = self._child(self._child(baseline, self.COMPONENTS), self.SCHEMAS)
        after = self._child(self._child(current, self.COMPONENTS), self.SCHEMAS)
        root = self._pointer(self._pointer("#", self.COMPONENTS), self.SCHEMAS)
        for name, schema in before.items():
            location = self._pointer(root, name)
            if name in after:
                self._compare_node(self._dict_of(schema), self._dict_of(after[name]), location, found)
            else:
                found.append(ContractChange(kind=ContractChangeKind.SCHEMA_REMOVED, location=location))

    ############################
    # Publicly Exposed Methods #
    ############################

    def compare(self, baseline: Dict[str, JsonValue], current: Dict[str, JsonValue]) -> List[ContractChange]:
        """Find the breaking changes of the live document against the committed one.

        Args:
            baseline (Dict[str, JsonValue]): The committed OpenAPI document.
            current (Dict[str, JsonValue]): The live OpenAPI document.

        Returns:
            List[ContractChange]: The breaking changes, sorted by location.
        """
        found: List[ContractChange] = []
        self._compare_paths(baseline, current, found)
        self._compare_schemas(baseline, current, found)
        found.sort(key=lambda change: (change.location, change.kind.value))
        self.logger.debug("Compared two contracts and found %d breaking changes.", len(found))
        return found
