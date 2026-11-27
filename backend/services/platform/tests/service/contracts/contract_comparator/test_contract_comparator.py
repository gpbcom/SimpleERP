from __future__ import annotations

import copy
import logging
from typing import Dict, List

import pytest
from erp_platform.models.contracts.contract_change import ContractChange
from erp_platform.models.contracts.enums import ContractChangeKind
from erp_platform.service.contracts.contract_comparator import ContractComparator
from pydantic import JsonValue

from tests.service.contracts.contract_comparator.helpers import (
    HEALTH_POINTER,
    a_baseline,
    with_additions,
    with_link_ref,
    with_property_type,
    without_operation,
    without_parameter,
    without_path,
    without_property,
    without_schema,
)

SCHEMA = "#/components/schemas/Health"


class TestContractComparator:
    def compare(self, baseline: Dict[str, JsonValue], current: Dict[str, JsonValue]) -> List[ContractChange]:
        return ContractComparator().compare(baseline, current)

    def test_identical_documents_give_no_change(self) -> None:
        assert self.compare(a_baseline(), a_baseline()) == []

    def test_a_removed_path_breaks_the_contract(self) -> None:
        changes = self.compare(a_baseline(), without_path("/v1/health"))

        assert [(c.kind, c.location) for c in changes] == [(ContractChangeKind.PATH_REMOVED, HEALTH_POINTER)]

    @pytest.mark.parametrize("method", ["get", "post"])
    def test_a_removed_operation_breaks_the_contract(self, method: str) -> None:
        changes = self.compare(a_baseline(), without_operation("/v1/health", method))

        assert [(c.kind, c.location) for c in changes] == [
            (ContractChangeKind.OPERATION_REMOVED, f"{HEALTH_POINTER}/{method}")
        ]

    @pytest.mark.parametrize("method", ["get", "put", "post", "delete", "options", "head", "patch", "trace"])
    def test_every_http_method_counts_as_an_operation(self, method: str) -> None:
        baseline = a_baseline()
        baseline["paths"]["/v1/other"] = {method: {"responses": {}}, "x-kept": {}}  # type: ignore[index]
        current = a_baseline()
        current["paths"]["/v1/other"] = {"x-kept": {}}  # type: ignore[index]

        changes = self.compare(baseline, current)

        assert [(c.kind, c.location) for c in changes] == [
            (ContractChangeKind.OPERATION_REMOVED, f"#/paths/~1v1~1other/{method}")
        ]

    def test_a_removed_parameter_is_identified_by_location_and_name(self) -> None:
        changes = self.compare(a_baseline(), without_parameter())

        assert [(c.kind, c.location) for c in changes] == [
            (ContractChangeKind.PARAMETER_REMOVED, f"{HEALTH_POINTER}/get/parameters/query/verbose")
        ]

    def test_a_parameter_with_the_same_name_in_another_place_is_another_parameter(self) -> None:
        current = a_baseline()
        current["paths"]["/v1/health"]["get"]["parameters"][0]["in"] = "header"  # type: ignore[index, call-overload]

        changes = self.compare(a_baseline(), current)

        assert [(c.kind, c.location) for c in changes] == [
            (ContractChangeKind.PARAMETER_REMOVED, f"{HEALTH_POINTER}/get/parameters/query/verbose")
        ]

    def test_a_removed_schema_breaks_the_contract(self) -> None:
        changes = self.compare(a_baseline(), without_schema("Link"))

        assert [(c.kind, c.location) for c in changes] == [
            (ContractChangeKind.SCHEMA_REMOVED, "#/components/schemas/Link")
        ]

    @pytest.mark.parametrize(
        ("trail", "location"),
        [
            (["properties", "status"], f"{SCHEMA}/properties/status"),
            (["properties", "detail", "properties", "code"], f"{SCHEMA}/properties/detail/properties/code"),
            (
                ["properties", "checks", "items", "properties", "ok"],
                f"{SCHEMA}/properties/checks/items/properties/ok",
            ),
        ],
    )
    def test_a_removed_property_breaks_the_contract_at_any_depth(self, trail: List[str], location: str) -> None:
        changes = self.compare(a_baseline(), without_property(trail))

        assert [(c.kind, c.location) for c in changes] == [(ContractChangeKind.PROPERTY_REMOVED, location)]

    @pytest.mark.parametrize(
        ("trail", "value", "location"),
        [
            (["properties", "status"], "integer", f"{SCHEMA}/properties/status"),
            (["properties", "detail", "properties", "code"], "string", f"{SCHEMA}/properties/detail/properties/code"),
            ([], "array", SCHEMA),
            (["properties", "status"], None, f"{SCHEMA}/properties/status"),
        ],
    )
    def test_a_changed_type_breaks_the_contract(self, trail: List[str], value: JsonValue, location: str) -> None:
        changes = self.compare(a_baseline(), with_property_type(trail, value))

        assert [(c.kind, c.location) for c in changes] == [(ContractChangeKind.TYPE_CHANGED, location)]

    def test_a_type_added_to_a_property_that_had_none_is_a_change(self) -> None:
        baseline = with_property_type(["properties", "status"], None)

        changes = self.compare(baseline, a_baseline())

        assert [(c.kind, c.location) for c in changes] == [
            (ContractChangeKind.TYPE_CHANGED, f"{SCHEMA}/properties/status")
        ]

    def test_a_changed_reference_breaks_the_contract(self) -> None:
        changes = self.compare(a_baseline(), with_link_ref("#/components/schemas/Health"))

        assert [(c.kind, c.location) for c in changes] == [
            (ContractChangeKind.TYPE_CHANGED, f"{SCHEMA}/properties/link")
        ]

    def test_additions_never_break_the_contract(self) -> None:
        assert self.compare(a_baseline(), with_additions()) == []

    def test_a_document_without_paths_and_components_counts_as_empty(self) -> None:
        empty: Dict[str, JsonValue] = {"openapi": "3.1.0"}

        assert self.compare(empty, a_baseline()) == []
        removed = self.compare(a_baseline(), empty)
        assert {c.kind for c in removed} == {ContractChangeKind.PATH_REMOVED, ContractChangeKind.SCHEMA_REMOVED}

    def test_a_pointer_escapes_tilde_and_slash(self) -> None:
        baseline = a_baseline()
        baseline["paths"]["/v1/a~b"] = {"get": {"responses": {}}}  # type: ignore[index]

        changes = self.compare(baseline, a_baseline())

        assert [c.location for c in changes] == ["#/paths/~1v1~1a~0b"]

    def test_changes_are_sorted_by_location(self) -> None:
        current = without_schema("Link")
        del current["paths"]["/v1/problems"]  # type: ignore[attr-defined, index]
        del current["paths"]["/v1/health"]  # type: ignore[attr-defined, index]

        changes = self.compare(a_baseline(), current)
        locations = [c.location for c in changes]

        assert len(locations) == 3
        assert locations == sorted(locations)

    def test_the_inputs_are_left_untouched(self) -> None:
        baseline, current = a_baseline(), without_property(["properties", "status"])
        baseline_copy, current_copy = copy.deepcopy(baseline), copy.deepcopy(current)

        self.compare(baseline, current)

        assert (baseline, current) == (baseline_copy, current_copy)

    def test_the_comparison_logs_through_the_given_logger(self, caplog: pytest.LogCaptureFixture) -> None:
        logger = logging.getLogger("tests.contract_comparator")

        with caplog.at_level(logging.DEBUG, logger=logger.name):
            ContractComparator(logger=logger).compare(a_baseline(), without_path("/v1/health"))

        assert any(record.name == logger.name for record in caplog.records)
