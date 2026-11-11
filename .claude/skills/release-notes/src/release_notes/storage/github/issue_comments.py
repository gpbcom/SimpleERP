from __future__ import annotations

# Standard library imports
from logging import Logger, getLogger
from typing import List, Optional

# First-party imports
from harness_core.github.github_connection import GithubConnection
from harness_core.github.json_payload import JsonPayload
from release_notes.models.catalogs.github_coordinates import GithubCoordinates


class IssueComments:
    """Reads the comments of the repository's issues through GitHub's REST API.

    Attributes:
        connection (GithubConnection): The HTTP client.
        coordinates (GithubCoordinates): The repository on GitHub.
        logger (Logger): Logger instance.

    Notes:
        Nothing retries here: a failed request is reported for that issue only, by the caller.
    """

    def __init__(
        self, connection: GithubConnection, coordinates: GithubCoordinates, logger: Optional[Logger] = None
    ) -> None:
        """Set the client and the repository.

        Args:
            connection (GithubConnection): The HTTP client.
            coordinates (GithubCoordinates): The repository on GitHub.
            logger (Optional[Logger]): Logger instance.
        """
        self.connection = connection
        self.coordinates = coordinates
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Publicly Exposed Methods #
    ############################

    async def bodies(self, number: int) -> List[str]:
        """Read the body of every comment of one issue.

        Args:
            number (int): The issue number.

        Returns:
            List[str]: The bodies, oldest first, empty for a comment without one.

        Raises:
            SEGithubRequestFailedError: When GitHub cannot be reached or answers with an error.
        """
        items = await self.connection.pages(f"{self.coordinates.issues_path(number)}/comments")
        self.logger.debug("Read %d comments of issue #%d.", len(items), number)
        return [JsonPayload.text(item, "body") for item in items]
