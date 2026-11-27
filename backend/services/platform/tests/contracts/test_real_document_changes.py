from __future__ import annotations

import copy
import json
from pathlib import Path
from typing import Dict, List, Tuple

from erp_platform.models.contracts.enums import ContractChangeKind
from erp_platform.service.contracts.contract_service import ContractService
from pydantic import JsonValue


class TestRealDocumentChanges:
    def write(self, path: Path, content: Dict[str, JsonValue]) -> Path:
        path.write_text(json.dumps(content, indent=2), encoding="utf-8")
        return path

    def a_schema_with_properties(self, document: Dict[str, JsonValue]) -> Tuple[str, Dict[str, JsonValue]]:
        components = document["components"]
        assert isinstance(components, dict)
        schemas = components["schemas"]
        assert isinstance(schemas, dict)
        for name, schema in schemas.items():
            if isinstance(schema, dict) and isinstance(schema.get("properties"), dict):
                return name, schema
        raise AssertionError("The real document holds no component schema with properties.")

    def test_a_field_removed_from_the_real_document_breaks_the_contract(
        self, contract_service: ContractService, document: Dict[str, JsonValue], tmp_path: Path
    ) -> None:
        baseline = copy.deepcopy(document)
        name, schema = self.a_schema_with_properties(baseline)
        properties = schema["properties"]
        assert isinstance(properties, dict)
        properties["removed_field"] = {"type": "string"}
        report = contract_service.check(
            document, self.write(tmp_path / "committed.json", document), self.write(tmp_path / "base.json", baseline)
        )
        assert not report.passed
        assert [(change.kind, change.location) for change in report.breaking_changes] == [
            (ContractChangeKind.PROPERTY_REMOVED, f"#/components/schemas/{name}/properties/removed_field")
        ]

    def test_a_field_added_to_the_real_document_keeps_the_contract(
        self, contract_service: ContractService, document: Dict[str, JsonValue], tmp_path: Path
    ) -> None:
        baseline = copy.deepcopy(document)
        _, schema = self.a_schema_with_properties(baseline)
        properties = schema["properties"]
        assert isinstance(properties, dict)
        del properties[next(iter(properties))]
        report = contract_service.check(
            document, self.write(tmp_path / "committed.json", document), self.write(tmp_path / "base.json", baseline)
        )
        changes: List[str] = [change.location for change in report.breaking_changes]
        assert report.passed, changes
