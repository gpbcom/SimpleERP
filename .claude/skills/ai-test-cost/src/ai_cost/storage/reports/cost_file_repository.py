from __future__ import annotations

# Standard library imports
import os
import tempfile
from logging import Logger, getLogger
from pathlib import Path
from typing import Optional

# First-party imports
from ai_cost.storage.reports.exceptions import SECostTemplateUnreadableError
from harness_core.git.exceptions import SEGitCommandFailedError
from harness_core.git.git_repository import GitRepository


class CostFileRepository:
    """Writes a ticket's ``COST.md`` in the evidence folder of the caller's repository.

    Attributes:
        caller_cwd (Path): The folder ``ai-cost`` was called from.
        template_file (Path): The layout of a ``COST.md``.
        logger (Logger): Logger instance.

    Notes:
        - The file goes to ``<repository>/docs/tickets/<KEY>/tests-evidences/COST.md``, the repository being the git
          working tree that holds the caller's folder. That folder is local: it is archived at hand-over.
        - ``COST.md`` mirrors the ledger, so failing to write it never stops a run: ``write`` reports it as ``None``
          and logs why.
    """

    def __init__(self, caller_cwd: Path, template_file: Path, logger: Optional[Logger] = None) -> None:
        """Set the caller's folder and the template.

        Args:
            caller_cwd (Path): The folder ``ai-cost`` was called from.
            template_file (Path): The layout of a ``COST.md``.
            logger (Optional[Logger]): Logger instance.
        """
        self.caller_cwd = caller_cwd
        self.template_file = template_file
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Publicly Exposed Methods #
    ############################

    def path(self, ticket: str) -> Optional[Path]:
        """Give where a ticket's ``COST.md`` goes.

        Args:
            ticket (str): The ticket.

        Returns:
            Optional[Path]: The file, ``None`` when the caller's folder is not in a git working tree.
        """
        try:
            root = GitRepository.discover(self.caller_cwd, self.logger).root
        except (SEGitCommandFailedError, OSError) as error:
            self.logger.warning(
                "%s is not in a git repository: no COST.md (%s).", self.caller_cwd, type(error).__name__
            )
            return None
        return root / "docs" / "tickets" / ticket / "tests-evidences" / "COST.md"

    def template(self) -> str:
        """Read the layout of a ``COST.md``.

        Returns:
            str: The template, with ``string.Template`` placeholders.

        Raises:
            SECostTemplateUnreadableError: When the template cannot be read.
        """
        try:
            return self.template_file.read_text(encoding="utf-8")
        except OSError as error:
            self.logger.error("The COST.md template %s cannot be read.", self.template_file)
            raise SECostTemplateUnreadableError(
                f"The COST.md template {self.template_file} cannot be read. "  # noqa: E501
                f"The error was {type(error).__name__}."
            ) from error

    def write(self, ticket: str, content: str) -> Optional[Path]:
        """Write a ticket's ``COST.md`` at once.

        Args:
            ticket (str): The ticket.
            content (str): The file's text.

        Returns:
            Optional[Path]: The file written, ``None`` when it could not be.
        """
        path = self.path(ticket)
        if path is None:
            return None
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            descriptor, temporary = tempfile.mkstemp(dir=path.parent, prefix=f".{path.name}.")
            with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
                handle.write(content)
            os.replace(temporary, path)
        except OSError as error:
            self.logger.warning("COST.md of %s not written to %s: %s.", ticket, path, type(error).__name__)
            return None
        self.logger.info("Wrote the COST.md of %s to %s.", ticket, path)
        return path
