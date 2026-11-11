from __future__ import annotations

# Standard library imports
from datetime import datetime
from logging import Logger, getLogger
from pathlib import Path
from typing import ClassVar, Optional

# First-party imports
from harness_core.git.git_repository import GitRepository
from ticket_docs.models.github.github_catalog import GithubCatalog
from ticket_docs.service.github.exceptions import SETicketFolderMissingError
from ticket_docs.storage.github.gh_client import GhClient
from ticket_docs.storage.tickets.ticket_repository import TicketRepository


class EvidenceArchiver:
    """Keeps a ticket folder on GitHub: zipped, uploaded to the pre-release ``evidence-<KEY>`` (TEST-9).

    Attributes:
        TITLE (str): The pre-release's title, followed by the ticket.
        NOTES (str): The pre-release's description, with the ticket.
        COMMENT (str): The issue comment, with the asset's link.
        DOWNLOAD (str): A release asset's download link on GitHub.
        tickets (TicketRepository): The ticket folders.
        gh (GhClient): Talks to GitHub.
        catalog (GithubCatalog): The repository and the pre-release's tag.
        repository (GitRepository): The caller's repository, whose commit the tag points at.
        scratch (Path): Where the zip is written before its upload.
        logger (Logger): Logger instance.

    Notes:
        - **Assets are only added**: an upload never replaces one (no ``--clobber``) and none is deleted.
        - The asset is named ``<KEY>-<YYYYMMDD-HHMM>.zip``, so every archive stays.
        - The issue gets a comment with the link, so that the archive is found from the issue.
    """

    TITLE: ClassVar[str] = "Evidence {key}"
    NOTES: ClassVar[str] = "Test evidence and ticket folder of {key} (TEST-9). Not a release."
    COMMENT: ClassVar[str] = "Ticket folder archived: {url} (TEST-9)."
    DOWNLOAD: ClassVar[str] = "https://github.com/{repository}/releases/download/{tag}/{name}"

    def __init__(
        self,
        tickets: TicketRepository,
        gh: GhClient,
        catalog: GithubCatalog,
        repository: GitRepository,
        scratch: Path,
        logger: Optional[Logger] = None,
    ) -> None:
        """Set the folders, GitHub and the scratch folder.

        Args:
            tickets (TicketRepository): The ticket folders.
            gh (GhClient): Talks to GitHub.
            catalog (GithubCatalog): The repository and the pre-release's tag.
            repository (GitRepository): The caller's repository, whose commit the tag points at.
            scratch (Path): Where the zip is written before its upload.
            logger (Optional[Logger]): Logger instance.
        """
        self.tickets = tickets
        self.gh = gh
        self.catalog = catalog
        self.repository = repository
        self.scratch = scratch
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Publicly Exposed Methods #
    ############################

    def archive(self, key: str) -> str:
        """Zip the ticket folder, upload it to its pre-release and comment the link on the issue.

        Args:
            key (str): The ticket, ``GH-<n>``.

        Returns:
            str: The uploaded asset's link.

        Raises:
            SETicketFolderMissingError: When the ticket has no folder.
        """
        if not self.tickets.exists(key):
            self.logger.error("%s has no folder to archive.", key)
            raise SETicketFolderMissingError(
                f"{self.tickets.folder(key)} does not exist, so there is nothing to archive."
            )
        name = f"{key}-{datetime.now():%Y%m%d-%H%M}.zip"
        archive = self.tickets.archive(key, self.scratch / name)
        tag = self.catalog.release_tag(key)
        if not self.gh.release_exists(tag):
            self.gh.release_create(tag, self.repository.head(), self.TITLE.format(key=key), self.NOTES.format(key=key))
        self.gh.release_upload(tag, archive)
        url = self.gh.release_asset_url(tag, archive.name) or self.DOWNLOAD.format(
            repository=self.catalog.full_name, tag=tag, name=archive.name
        )
        self.gh.issue_comment(int(key.split("-", 1)[1]), self.COMMENT.format(url=url))
        self.logger.info("Archived %s as %s.", key, archive.name)
        return url
