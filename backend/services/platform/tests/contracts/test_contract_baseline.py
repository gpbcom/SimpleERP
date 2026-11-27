from __future__ import annotations

import os
from pathlib import Path
from typing import Dict

import pytest
from erp_platform.service.contracts.contract_service import ContractService
from pydantic import JsonValue


class TestContractBaseline:
    def test_the_api_keeps_the_contract_of_the_base_document(
        self,
        contract_service: ContractService,
        document: Dict[str, JsonValue],
        committed_path: Path,
    ) -> None:
        baseline = os.environ.get("ERP_CONTRACT_BASELINE", "").strip()
        if not baseline:
            pytest.skip("No base document: only the stale check runs.")
        report = contract_service.check(document, committed_path, Path(baseline))
        lines = [f"{change.kind.value} at {change.location}" for change in report.breaking_changes]
        assert report.passed, "The API breaks the base document:\n" + "\n".join(lines)
