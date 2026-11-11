from __future__ import annotations

# Standard library imports
import re
from logging import Logger
from pathlib import Path
from typing import ClassVar, List, Optional, Pattern, Tuple

# First-party imports
from ticket_docs.models.checks.folder_rules import FolderRules
from ticket_docs.models.evidence.evidence_run import EvidenceRun
from ticket_docs.service.checks.markdown_tables import MarkdownTables
from ticket_docs.service.checks.ticket_check import TicketCheck
from ticket_docs.service.checks.ticket_folder import TicketFolder


class ClaimsCheck(TicketCheck):
    """Checks that every pass claimed in PROGRESS.md and EXPLAIN.md links its evidence folder (TEST-8).

    Attributes:
        FILES (Tuple[str, ...]): The files whose claims are checked.
        STATUS_SECTION (str): PROGRESS.md's Status section, whose test-run steps claim a pass when done.
        DONE (str): The icon of a pass.
        PASS_WORDS (Pattern[str]): The words that claim a pass: ``PASS`` and ``green``.
        PASS_CELL (Pattern[str]): A table cell that starts with ``PASS``.
        LEGEND (str): The start of the legend line, which names the icons without claiming anything.
        ITEM_SPLIT (Pattern[str]): What separates the items of a line: table pipes and `` · ``.
        HEADING (Pattern[str]): A section heading, whose text is kept to know the section.
        LINK (Pattern[str]): A Markdown link.
        EVIDENCE_DIR (str): The evidence folder's name.
        rules (FolderRules): The result sections and the words of a test-run step.
        tables (MarkdownTables): Blanks code and comments, splits table rows.
        logger (Logger): Logger instance.

    Notes:
        A line claims a pass when one of its items holds ✅ together with ``PASS`` or ``green``, when a table cell
        starts with ``PASS``, when a ✅ cell sits in a result section (stage validation, final verification, last
        results, acceptance criteria), or when a test-run step of the Status table is ✅. ``⬜ 🟢 green run`` is a
        plan, not a claim. The claiming line must link a run folder that exists under ``tests-evidences/``.
    """

    FILES: ClassVar[Tuple[str, ...]] = ("PROGRESS.md", "EXPLAIN.md")
    STATUS_SECTION: ClassVar[str] = "Status"
    DONE: ClassVar[str] = "✅"
    PASS_WORDS: ClassVar[Pattern[str]] = re.compile(r"\bPASS\b|\b[Gg]reen\b")
    PASS_CELL: ClassVar[Pattern[str]] = re.compile(r"^PASS\b")
    LEGEND: ClassVar[str] = "**Legend:**"
    ITEM_SPLIT: ClassVar[Pattern[str]] = re.compile(r"(?<!\\)\||\s·\s")
    HEADING: ClassVar[Pattern[str]] = re.compile(r"^#{1,6}\s+(?P<title>.+?)\s*$")
    LINK: ClassVar[Pattern[str]] = re.compile(r"\]\(([^)\s]+)\)")
    EVIDENCE_DIR: ClassVar[str] = "tests-evidences"

    def __init__(self, rules: FolderRules, tables: MarkdownTables, logger: Optional[Logger] = None) -> None:
        """Set the rules and the text reader.

        Args:
            rules (FolderRules): The result sections and the words of a test-run step.
            tables (MarkdownTables): Blanks code and comments, splits table rows.
            logger (Optional[Logger]): Logger instance.
        """
        super().__init__(logger)
        self.rules = rules
        self.tables = tables

    ############################
    # Internal Helpers Methods #
    ############################

    def _run_step(self, step: str) -> bool:
        """Tell whether a Status step is a test run.

        Args:
            step (str): The step's name.

        Returns:
            bool: ``True`` when it holds one of the words of a test-run step.
        """
        return any(re.search(rf"\b{re.escape(word)}", step, re.I) for word in self.rules.run_steps)

    def _claims(self, line: str, section: str) -> bool:
        """Tell whether a line claims a pass.

        Args:
            line (str): The line, without inline code.
            section (str): The title of the section it is in.

        Returns:
            bool: ``True`` for a claim.
        """
        if any(self.DONE in item and self.PASS_WORDS.search(item) for item in self.ITEM_SPLIT.split(line)):
            return True
        if not line.lstrip().startswith("|"):
            return False
        cells = self.tables.cells(line)
        if any(self.PASS_CELL.match(cell) for cell in cells):
            return True
        if any(section.startswith(name) for name in self.rules.result_sections):
            return any(cell.startswith(self.DONE) for cell in cells[1:])
        if section == self.STATUS_SECTION and len(cells) > 1:
            return cells[1].startswith(self.DONE) and self._run_step(cells[0])
        return False

    def _proven(self, path: Path, line: str) -> bool:
        """Tell whether a line links a run folder that exists.

        Args:
            path (Path): The file the line is in.
            line (str): The line.

        Returns:
            bool: ``True`` when one of its links leads into an existing run folder.
        """
        for link in self.LINK.findall(line):
            parts = Path(link.split("#", 1)[0]).parts
            if self.EVIDENCE_DIR not in parts:
                continue
            index = parts.index(self.EVIDENCE_DIR)
            run = parts[index + 1 : index + 2]
            if run and EvidenceRun.FOLDER_NAME.match(run[0]) and (path.parent / Path(*parts[: index + 2])).is_dir():
                return True
        return False

    ############################
    # Publicly Exposed Methods #
    ############################

    def problems(self, folder: TicketFolder) -> List[str]:
        """List the lines that claim a pass without a link to its evidence folder.

        Args:
            folder (TicketFolder): The ticket folder.

        Returns:
            List[str]: One line per unproven claim, with its file and line number.
        """
        problems: List[str] = []
        for name in self.FILES:
            text = folder.text(name)
            if text is None:
                continue
            section = ""
            raw_lines = text.splitlines()
            for number, line in enumerate(self.tables.without_blocks(text).splitlines(), start=1):
                heading = self.HEADING.match(line)
                if heading:
                    section = heading.group("title")
                    continue
                if line.startswith(self.LEGEND) or not self._claims(self.tables.INLINE_CODE.sub("", line), section):
                    continue
                if not self._proven(folder.path / name, line):
                    excerpt = raw_lines[number - 1].strip()[:80]
                    problems.append(
                        f"{folder.label(name)}:{number}: '{excerpt}' claims a pass without a link to its "
                        "tests-evidences folder (TEST-8)"
                    )
        self.logger.debug("%s has %d unproven claims.", folder.key, len(problems))
        return problems
