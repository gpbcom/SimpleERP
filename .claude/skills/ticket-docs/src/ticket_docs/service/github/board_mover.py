from __future__ import annotations

# Standard library imports
from logging import Logger, getLogger
from typing import ClassVar, Optional

# Third-party imports
from pydantic import JsonValue

# First-party imports
from ticket_docs.models.github.github_catalog import GithubCatalog
from ticket_docs.service.github.exceptions import SEBoardAnswerError, SEBoardStatusUnknownError
from ticket_docs.storage.github.gh_client import GhClient


class BoardMover:
    """Moves a ticket's issue on the GitHub project board of ``conf/github.yaml``.

    Attributes:
        ITEMS_QUERY (str): Reads the issue's node id and its items on every project.
        ADD_MUTATION (str): Adds the issue to the board.
        UPDATE_MUTATION (str): Sets the item's single-select status.
        gh (GhClient): Talks to GitHub.
        catalog (GithubCatalog): The repository, the board and its status options.
        logger (Logger): Logger instance.

    Notes:
        The issue's item is the one among its project items whose project is the board; an issue that is not on the
        board yet is added first.
    """

    ITEMS_QUERY: ClassVar[str] = (
        "query($owner: String!, $repo: String!, $number: Int!) { repository(owner: $owner, name: $repo) "
        "{ issue(number: $number) { id projectItems(first: 50) { nodes { id project { id } } } } } }"
    )
    ADD_MUTATION: ClassVar[str] = (
        "mutation($project: ID!, $content: ID!) { addProjectV2ItemById(input: {projectId: $project, "
        "contentId: $content}) { item { id } } }"
    )
    UPDATE_MUTATION: ClassVar[str] = (
        "mutation($project: ID!, $item: ID!, $field: ID!, $option: String!) { updateProjectV2ItemFieldValue("
        "input: {projectId: $project, itemId: $item, fieldId: $field, value: {singleSelectOptionId: $option}}) "
        "{ projectV2Item { id } } }"
    )

    def __init__(self, gh: GhClient, catalog: GithubCatalog, logger: Optional[Logger] = None) -> None:
        """Set GitHub and the board.

        Args:
            gh (GhClient): Talks to GitHub.
            catalog (GithubCatalog): The repository, the board and its status options.
            logger (Optional[Logger]): Logger instance.
        """
        self.gh = gh
        self.catalog = catalog
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    def _dig(self, value: JsonValue, *keys: str) -> JsonValue:
        """Follow keys down a GraphQL answer.

        Args:
            value (JsonValue): The answer.
            *keys (str): The keys, outermost first.

        Returns:
            JsonValue: What they lead to, ``None`` when one is missing.
        """
        for key in keys:
            value = value.get(key) if isinstance(value, dict) else None
        return value

    ############################
    # Publicly Exposed Methods #
    ############################

    def move(self, key: str, status: str) -> str:
        """Set the status of a ticket's issue on the board, adding it to the board first when needed.

        Args:
            key (str): The ticket, ``GH-<n>``.
            status (str): The status, one of the board's options, such as ``In progress``.

        Returns:
            str: The board item's node id.

        Raises:
            SEBoardStatusUnknownError: When the status is not one of the board's.
            SEBoardAnswerError: When GitHub does not know the issue or does not give the item.
        """
        field = self.catalog.status_field()
        if status not in field.options:
            self.logger.error("%r is not a status of the board.", status)
            raise SEBoardStatusUnknownError(
                f"Unknown status {status!r}. "  # noqa: E501
                f"Valid statuses: {', '.join(field.options)}."
            )
        project = self.catalog.project.id
        answer = self.gh.graphql(
            self.ITEMS_QUERY,
            {"owner": self.catalog.owner, "repo": self.catalog.repository, "number": int(key.split("-", 1)[1])},
        )
        issue = self._dig(answer, "data", "repository", "issue")
        issue_id = self._dig(issue, "id")
        if not isinstance(issue_id, str):
            self.logger.error("GitHub does not know the issue of %s.", key)
            raise SEBoardAnswerError(f"GitHub does not know the issue of {key} in {self.catalog.full_name}.")
        nodes = self._dig(issue, "projectItems", "nodes")
        items = [
            node.get("id")
            for node in (nodes if isinstance(nodes, list) else [])
            if isinstance(node, dict) and self._dig(node, "project", "id") == project
        ]
        item = items[0] if items else None
        if not isinstance(item, str):
            added = self.gh.graphql(self.ADD_MUTATION, {"project": project, "content": issue_id})
            item = self._dig(added, "data", "addProjectV2ItemById", "item", "id")
            if not isinstance(item, str):
                self.logger.error("GitHub did not add %s to the board.", key)
                raise SEBoardAnswerError(f"GitHub did not add the issue of {key} to the board.")
            self.logger.info("Added %s to the board.", key)
        self.gh.graphql(
            self.UPDATE_MUTATION,
            {"project": project, "item": item, "field": field.id, "option": field.options[status]},
        )
        self.logger.info("Moved %s to %s.", key, status)
        return item
