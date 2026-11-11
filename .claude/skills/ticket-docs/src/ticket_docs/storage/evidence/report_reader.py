from __future__ import annotations

# Standard library imports
import json
import xml.etree.ElementTree as ElementTree
from logging import Logger, getLogger
from pathlib import Path
from typing import ClassVar, Optional, Tuple

# Third-party imports
from pydantic import JsonValue

# First-party imports
from ticket_docs.models.evidence.run_counts import RunCounts


class ReportReader:
    """Reads the test counts of the reports a run leaves.

    Attributes:
        JUNIT_COUNTS (Tuple[str, ...]): The ``testsuite`` attributes read from a JUnit report.
        PLAYWRIGHT_TESTS (Tuple[str, ...]): The ``stats`` of Playwright's JSON results that count as tests run.
        PLAYWRIGHT_FAILED (str): The ``stats`` entry of the tests that failed.
        logger (Logger): Logger instance.

    Notes:
        A report that is missing or cannot be read gives ``None``: the run's verdict then rests on its exit code.
    """

    JUNIT_COUNTS: ClassVar[Tuple[str, ...]] = ("tests", "failures", "errors")
    PLAYWRIGHT_TESTS: ClassVar[Tuple[str, ...]] = ("expected", "unexpected", "flaky", "skipped")
    PLAYWRIGHT_FAILED: ClassVar[str] = "unexpected"

    def __init__(self, logger: Optional[Logger] = None) -> None:
        """Set the logger.

        Args:
            logger (Optional[Logger]): Logger instance.
        """
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Publicly Exposed Methods #
    ############################

    def junit(self, path: Path) -> Optional[RunCounts]:
        """Read a JUnit XML report, such as pytest's ``--junitxml``.

        Args:
            path (Path): The report.

        Returns:
            Optional[RunCounts]: The counts summed over every test suite, ``None`` when there is no readable report.
        """
        if not path.is_file():
            self.logger.debug("No JUnit report at %s.", path)
            return None
        try:
            root = ElementTree.parse(path).getroot()
        except ElementTree.ParseError:
            self.logger.warning("The JUnit report %s cannot be read.", path)
            return None
        totals = dict.fromkeys(self.JUNIT_COUNTS, 0)
        for suite in root.iter("testsuite"):
            for name in self.JUNIT_COUNTS:
                totals[name] += int(suite.get(name, "0") or 0)
        self.logger.debug("Read %d tests from %s.", totals["tests"], path.name)
        return RunCounts(tests=totals["tests"], failures=totals["failures"], errors=totals["errors"])

    def playwright(self, path: Path) -> Optional[RunCounts]:
        """Read Playwright's JSON results.

        Args:
            path (Path): The ``results.json`` file.

        Returns:
            Optional[RunCounts]: The counts of its ``stats``, ``None`` when there are no readable results.
        """
        if not path.is_file():
            self.logger.debug("No Playwright results at %s.", path)
            return None
        try:
            results: JsonValue = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            self.logger.warning("The Playwright results %s cannot be read.", path)
            return None
        stats = results.get("stats") if isinstance(results, dict) else None
        if not isinstance(stats, dict):
            self.logger.warning("The Playwright results %s have no stats.", path)
            return None
        numbers = {name: stats.get(name) for name in self.PLAYWRIGHT_TESTS}
        tests = sum(value for value in numbers.values() if isinstance(value, int))
        failed = numbers[self.PLAYWRIGHT_FAILED]
        return RunCounts(tests=tests, failures=failed if isinstance(failed, int) else 0)
