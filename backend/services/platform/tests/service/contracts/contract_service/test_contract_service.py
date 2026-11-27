from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, Optional

import pytest
from erp_platform.models.contracts.enums import ContractChangeKind
from erp_platform.models.contracts.exceptions import SEOpenApiDocumentUnreadableError
from erp_platform.service.contracts.contract_service import ContractService
from pydantic import JsonValue


class TestContractService:
    def write(self, path: Path, document: Dict[str, JsonValue], indent: Optional[int] = 2) -> Path:
        path.write_text(json.dumps(document, indent=indent), encoding="utf-8")
        return path

    def test_an_up_to_date_document_without_baseline_passes(
        self, service: ContractService, generated: Dict[str, JsonValue], tmp_path: Path
    ) -> None:
        report = service.check(generated, self.write(tmp_path / "openapi.json", generated), None)
        assert report.stale is False
        assert report.breaking_changes == []
        assert report.passed is True

    def test_a_stale_document_fails(
        self,
        service: ContractService,
        generated: Dict[str, JsonValue],
        without_version_property: Dict[str, JsonValue],
        tmp_path: Path,
    ) -> None:
        report = service.check(generated, self.write(tmp_path / "openapi.json", without_version_property), None)
        assert report.stale is True
        assert report.passed is False

    def test_a_removed_property_is_one_breaking_change_and_fails(
        self,
        service: ContractService,
        generated: Dict[str, JsonValue],
        without_version_property: Dict[str, JsonValue],
        tmp_path: Path,
    ) -> None:
        committed = self.write(tmp_path / "openapi.json", without_version_property)
        baseline = self.write(tmp_path / "baseline.json", generated)
        report = service.check(without_version_property, committed, baseline)
        assert report.stale is False
        assert [change.kind for change in report.breaking_changes] == [ContractChangeKind.PROPERTY_REMOVED]
        assert report.passed is False

    def test_an_added_property_passes(
        self,
        service: ContractService,
        generated: Dict[str, JsonValue],
        without_version_property: Dict[str, JsonValue],
        tmp_path: Path,
    ) -> None:
        committed = self.write(tmp_path / "openapi.json", generated)
        baseline = self.write(tmp_path / "baseline.json", without_version_property)
        report = service.check(generated, committed, baseline)
        assert report.breaking_changes == []
        assert report.passed is True

    @pytest.mark.parametrize("indent", [None, 1, 4])
    def test_formatting_does_not_make_a_document_stale(
        self, service: ContractService, generated: Dict[str, JsonValue], tmp_path: Path, indent: Optional[int]
    ) -> None:
        report = service.check(generated, self.write(tmp_path / "openapi.json", generated, indent), None)
        assert report.stale is False
        assert report.passed is True

    def test_a_missing_document_is_refused(
        self, service: ContractService, generated: Dict[str, JsonValue], tmp_path: Path
    ) -> None:
        with pytest.raises(SEOpenApiDocumentUnreadableError):
            service.check(generated, tmp_path / "missing.json", None)

    def test_a_missing_baseline_is_refused(
        self, service: ContractService, generated: Dict[str, JsonValue], tmp_path: Path
    ) -> None:
        committed = self.write(tmp_path / "openapi.json", generated)
        with pytest.raises(SEOpenApiDocumentUnreadableError):
            service.check(generated, committed, tmp_path / "missing.json")

    def test_an_unreadable_document_is_refused(
        self, service: ContractService, generated: Dict[str, JsonValue], tmp_path: Path
    ) -> None:
        broken = tmp_path / "openapi.json"
        broken.write_text("{not json", encoding="utf-8")
        with pytest.raises(SEOpenApiDocumentUnreadableError):
            service.check(generated, broken, None)
