from __future__ import annotations

import json
import logging
from pathlib import Path

from tests.builders.evidence_builder import EvidenceBuilder
from ticket_docs.models.evidence.run_counts import RunCounts
from ticket_docs.storage.evidence.report_reader import ReportReader


class TestReportReader:
    def test_a_junit_report_gives_its_counts(self, tmp_path: Path, logger: logging.Logger) -> None:
        report = tmp_path / "report.xml"
        report.write_text(EvidenceBuilder(tmp_path).junit(tests=9, failures=2, errors=1), encoding="utf-8")
        assert ReportReader(logger).junit(report) == RunCounts(tests=9, failures=2, errors=1)

    def test_a_single_testsuite_root_is_read_too(self, tmp_path: Path, logger: logging.Logger) -> None:
        report = tmp_path / "report.xml"
        report.write_text('<testsuite tests="4" failures="0" errors="1"/>', encoding="utf-8")
        assert ReportReader(logger).junit(report) == RunCounts(tests=4, errors=1)

    def test_a_missing_or_broken_junit_report_gives_nothing(self, tmp_path: Path, logger: logging.Logger) -> None:
        broken = tmp_path / "broken.xml"
        broken.write_text("<testsuites", encoding="utf-8")
        reader = ReportReader(logger)
        assert reader.junit(tmp_path / "missing.xml") is None
        assert reader.junit(broken) is None

    def test_playwright_results_give_their_counts(self, tmp_path: Path, logger: logging.Logger) -> None:
        results = tmp_path / "results.json"
        results.write_text(
            json.dumps({"stats": {"expected": 5, "unexpected": 2, "flaky": 1, "skipped": 1}}), encoding="utf-8"
        )
        assert ReportReader(logger).playwright(results) == RunCounts(tests=9, failures=2)

    def test_missing_or_broken_playwright_results_give_nothing(self, tmp_path: Path, logger: logging.Logger) -> None:
        broken = tmp_path / "results.json"
        broken.write_text("{", encoding="utf-8")
        reader = ReportReader(logger)
        assert reader.playwright(tmp_path / "none.json") is None
        assert reader.playwright(broken) is None
