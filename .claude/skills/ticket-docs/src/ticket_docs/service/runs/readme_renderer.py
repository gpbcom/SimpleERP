from __future__ import annotations

# Standard library imports
from logging import Logger, getLogger
from typing import ClassVar, Dict, List, Optional, Tuple

# First-party imports
from ticket_docs.models.enums import Expectation
from ticket_docs.models.evidence.actions_run import ActionsRun
from ticket_docs.models.evidence.evidence_run import EvidenceRun
from ticket_docs.models.evidence.run_counts import RunCounts


class ReadmeRenderer:
    """Writes an evidence folder's README and its verdict line, in the format the bootstrap recorder started.

    Attributes:
        ARTEFACTS (Dict[str, Tuple[str, str]]): Each report a folder may hold: its link and what it holds, in order.
        EXPECTED_RED (str): What a red run's verdict adds.
        AS_EXPECTED (str): The end of a red run that failed.
        UNEXPECTED_GREEN (str): The end of a red run that passed.
        logger (Logger): Logger instance.

    Notes:
        - ``EvidenceRun.from_readme`` reads back exactly what ``readme`` writes, pipes in cells included.
        - The verdict counts ``passed/total`` from the report when there is one, and rests on the exit code alone
          when there is none.
    """

    ARTEFACTS: ClassVar[Dict[str, Tuple[str, str]]] = {
        "console.txt": ("console.txt", "The raw console output"),
        "report.xml": ("report.xml", "JUnit XML report"),
        "report.html": ("report.html", "HTML report (pytest-html)"),
        "playwright-report/": ("playwright-report/index.html", "Playwright HTML report"),
        "results.json": ("results.json", "Playwright JSON results"),
        "actions.log": ("actions.log", "The Actions run log"),
        "artifacts/": ("artifacts/", "The Actions run's artifacts, downloaded"),
    }
    EXPECTED_RED: ClassVar[str] = " — expected red (TDD), "
    AS_EXPECTED: ClassVar[str] = "as expected"
    UNEXPECTED_GREEN: ClassVar[str] = "UNEXPECTED GREEN"

    def __init__(self, logger: Optional[Logger] = None) -> None:
        """Set the logger.

        Args:
            logger (Optional[Logger]): Logger instance.
        """
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    def _expected(self, line: str, passed: bool, expectation: Expectation) -> str:
        """Add what a red run expected to its verdict.

        Args:
            line (str): The verdict.
            passed (bool): Whether the run passed.
            expectation (Expectation): How it was expected to end.

        Returns:
            str: The verdict, with ``— expected red (TDD), as expected`` or ``UNEXPECTED GREEN`` for a red run.
        """
        if expectation is not Expectation.RED:
            return line
        return f"{line}{self.EXPECTED_RED}{self.UNEXPECTED_GREEN if passed else self.AS_EXPECTED}"

    def _cell(self, text: str) -> str:
        """Make a text safe inside a table cell.

        Args:
            text (str): The text.

        Returns:
            str: The text on one line, its pipes escaped.
        """
        return " ".join(text.split()).replace("|", "\\|")

    ############################
    # Publicly Exposed Methods #
    ############################

    def result(self, counts: Optional[RunCounts], exit_code: int, expectation: Expectation) -> str:
        """Write the verdict of a command.

        Args:
            counts (Optional[RunCounts]): The counts of its report, ``None`` when it has none.
            exit_code (int): Its exit code.
            expectation (Expectation): How it was expected to end.

        Returns:
            str: Such as ``✅ PASS 5/5 (exit 0; 0 failures, 0 errors)`` or ``❌ FAIL (exit 4)``.
        """
        passed = exit_code == 0
        verdict = "✅ PASS" if passed else "❌ FAIL"
        if counts is None:
            line = f"{verdict} (exit {exit_code})"
        else:
            line = (
                f"{verdict} {counts.passed}/{counts.tests} "
                f"(exit {exit_code}; {counts.failures} failures, {counts.errors} errors)"
            )
        return self._expected(line, passed, expectation)

    def actions_result(self, run: ActionsRun, expectation: Expectation) -> str:
        """Write the verdict of an Actions run.

        Args:
            run (ActionsRun): The run.
            expectation (Expectation): How it was expected to end.

        Returns:
            str: Such as ``✅ PASS (Actions run <url> concluded success)``.
        """
        verdict = "✅ PASS" if run.succeeded else "❌ FAIL"
        line = f"{verdict} (Actions run {run.url} concluded {run.conclusion.value or 'nothing yet'})"
        return self._expected(line, run.succeeded, expectation)

    def readme(self, ticket: str, run: EvidenceRun, artefacts: List[str]) -> str:
        """Write an evidence folder's README.

        Args:
            ticket (str): The ticket.
            run (EvidenceRun): The run.
            artefacts (List[str]): What the folder holds, folders ending with a slash.

        Returns:
            str: The README.
        """
        date = run.date.strftime(EvidenceRun.DATE_FORMAT) if run.date else ""
        commit = ""
        if run.commit:
            dirty = f" ({EvidenceRun.DIRTY_NOTE})" if run.dirty else ""
            commit = f"`{run.commit}` on `{run.branch or ''}`{dirty}"
        rows = [
            ("What", self._cell(run.what or "")),
            ("Command", f"`{self._cell(run.command or '')}`"),
            ("Commit", commit),
            ("Kind", run.kind.value if run.kind else ""),
            ("Where", run.where.value if run.where else ""),
            ("Date", date),
            ("Result", self._cell(run.result or "")),
        ]
        lines = [
            f"# {ticket} — {run.where.value if run.where else ''} {date[:10]}: {run.folder}",
            "",
            "| | |",
            "|---|---|",
        ]
        lines += [f"| **{label}** | {value} |" for label, value in rows if value]
        lines += ["", "## Artefacts", "", "| File | Holds |", "|---|---|"]
        for name, (link, holds) in self.ARTEFACTS.items():
            if name in artefacts:
                lines.append(f"| [{link}]({link}) | {holds} |")
        self.logger.debug("Wrote the README of %s.", run.folder)
        return "\n".join(lines) + "\n"
