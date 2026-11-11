from __future__ import annotations

# Standard library imports
import re
from logging import Logger, getLogger
from typing import ClassVar, List, Optional

# First-party imports
from harness_core.markdown.markdown_text import MarkdownText
from harness_core.models.branches.branch_name import BranchName
from release_notes.service.exceptions import SETicketKeyInvalidError
from release_notes.storage.files.text_files import TextFiles


class ReleaseNoteCheck:
    """Checks a ticket's release note against the template: marker, headings, and no placeholder left.

    Attributes:
        NOTE (str): The release note, with ``{key}`` for the ticket.
        PLACEHOLDER_PATTERN (re.Pattern[str]): A ``<...>`` placeholder, which is not a comment, a link or a tag.
        files (TextFiles): The repository's files.
        template (str): The release note template.
        marker (str): The template's first line, which the note and its issue comment start with.
        headings (List[str]): The template's ``##`` headings, which the note keeps.
        logger (Logger): Logger instance.

    Notes:
        - ``<...>`` inside code is an example, not a placeholder, and ``<https://...>`` is a link.
        - The marker and the headings come from the template, so a change of the template changes the check.
    """

    NOTE: ClassVar[str] = "docs/tickets/{key}/RELEASE-NOTE.md"
    PLACEHOLDER_PATTERN: ClassVar[re.Pattern[str]] = re.compile(r"<(?!!--)(?![A-Za-z][A-Za-z0-9+.-]*:)(?!/)[^<>\n]+>")

    def __init__(self, files: TextFiles, template: str, logger: Optional[Logger] = None) -> None:
        """Set the files and read the template.

        Args:
            files (TextFiles): The repository's files.
            template (str): The release note template.
            logger (Optional[Logger]): Logger instance.
        """
        self.files = files
        self.template = template
        self.marker = template.splitlines()[0].strip() if template.strip() else ""
        self.headings = MarkdownText.headings(template, 2)
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Publicly Exposed Methods #
    ############################

    def problems(self, key: str) -> List[str]:
        """List what is wrong with a ticket's release note.

        Args:
            key (str): The ticket, such as ``GH-12``.

        Returns:
            List[str]: One line per problem, none when the note is ready.

        Raises:
            SETicketKeyInvalidError: When the key is not ``GH-<n>``.
        """
        if not BranchName.TICKET_PATTERN.match(key):
            self.logger.error("The ticket key %r is not GH-<n>.", key)
            raise SETicketKeyInvalidError(
                f"Invalid ticket: {key!r}. "  # noqa: E501
                "Must look like GH-12."
            )
        path = self.NOTE.format(key=key)
        if not self.files.exists(path):
            return [f"{path}: missing."]
        text = self.files.read(path)
        problems: List[str] = []
        if not text.startswith(self.marker):
            problems.append(f"{path}: does not start with {self.marker}.")
        present = MarkdownText.headings(text, 2)
        problems.extend(f'{path}: no "## {heading}" heading.' for heading in self.headings if heading not in present)
        for number, line in enumerate(MarkdownText.prose(text).splitlines(), start=1):
            problems.extend(
                f"{path}:{number}: placeholder {match.group(0)} left."
                for match in self.PLACEHOLDER_PATTERN.finditer(line)
            )
        self.logger.info("The release note of %s has %d problems.", key, len(problems))
        return problems
