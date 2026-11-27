from __future__ import annotations

from typing import Dict, List

import pytest
from erp_platform.models.contracts.contract_change import ContractChange
from erp_platform.models.contracts.contract_report import ContractReport
from erp_platform.models.contracts.enums import ContractChangeKind
from erp_platform.models.contracts.exceptions import (
    SEContractReportInvalidBreakingChanges,
    SEContractReportInvalidStale,
    SEInvalidContractReportException,
)
from pydantic import JsonValue, ValidationError


class TestContractReport:
    CHANGE = ContractChange(kind=ContractChangeKind.PATH_REMOVED, location="#/paths/~1v1~1health")

    def test_defaults(self) -> None:
        report = ContractReport()
        assert report.stale is False
        assert report.breaking_changes == []

    def test_full_valid_construction(self) -> None:
        report = ContractReport(stale=True, breaking_changes=[self.CHANGE])
        assert report.stale is True
        assert report.breaking_changes == [self.CHANGE]
        parsed = ContractReport.model_validate(
            {"stale": False, "breaking_changes": [{"kind": "path_removed", "location": "#/paths/~1v1~1health"}]}
        )
        assert parsed.breaking_changes == [self.CHANGE]

    @pytest.mark.parametrize("name", ["stale", "breaking_changes"])
    def test_none_becomes_the_default(self, name: str) -> None:
        report = ContractReport.model_validate({name: None})
        assert report == ContractReport()

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("stale", 0, SEContractReportInvalidStale),
            ("stale", 1, SEContractReportInvalidStale),
            ("stale", "yes", SEContractReportInvalidStale),
            ("stale", "", SEContractReportInvalidStale),
            ("stale", [], SEContractReportInvalidStale),
            ("breaking_changes", "path_removed", SEContractReportInvalidBreakingChanges),
            ("breaking_changes", 1, SEContractReportInvalidBreakingChanges),
            ("breaking_changes", True, SEContractReportInvalidBreakingChanges),
            ("breaking_changes", {"kind": "path_removed"}, SEContractReportInvalidBreakingChanges),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            ContractReport.model_validate({name: value})

    @pytest.mark.parametrize("error", [SEContractReportInvalidStale, SEContractReportInvalidBreakingChanges])
    def test_the_field_exceptions_have_the_model_base(self, error: type[Exception]) -> None:
        assert issubclass(error, SEInvalidContractReportException)

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            ContractReport.model_validate({"unknown": 1})

    @pytest.mark.parametrize(
        ("stale", "count", "expected"),
        [(False, 0, True), (True, 0, False), (False, 1, False), (True, 1, False), (False, 2, False)],
    )
    def test_it_passes_only_when_not_stale_and_without_a_breaking_change(
        self, stale: bool, count: int, expected: bool
    ) -> None:
        changes: List[ContractChange] = [self.CHANGE] * count
        assert ContractReport(stale=stale, breaking_changes=changes).passed is expected

    def test_it_is_frozen(self) -> None:
        report = ContractReport()
        with pytest.raises(ValidationError):
            report.stale = True

    def test_round_trip(self) -> None:
        report = ContractReport(stale=True, breaking_changes=[self.CHANGE])
        data: Dict[str, object] = report.model_dump()
        assert ContractReport.model_validate(data) == report
        assert ContractReport.model_validate_json(report.model_dump_json()) == report
