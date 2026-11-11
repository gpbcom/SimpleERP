from __future__ import annotations

# Standard library imports
from logging import Logger, getLogger
from pathlib import Path
from typing import List, Optional

# First-party imports
from ticket_docs.models.checks.folder_rules import FolderRules


class FileGate:
    """Decides whether a file tool of Claude (Write, Edit, MultiEdit, NotebookEdit) may write a file.

    Attributes:
        rules (FolderRules): The folders of the guards' state.
        logger (Logger): Logger instance.

    Notes:
        - A file inside a folder of ``guard_state_folders`` is refused: the squash permits (GIT-4) and the AI test
          ledgers (TEST-5) are written only by their own tools, from the human's terminal.
        - ``~``, symbolic links and ``..`` are resolved on both sides before comparing, and a relative path is read
          from the session's folder.
        - **A guard against mistakes, not a security boundary**: a process of the same user can still write there.
    """

    def __init__(self, rules: FolderRules, logger: Optional[Logger] = None) -> None:
        """Set the folders.

        Args:
            rules (FolderRules): The folders of the guards' state.
            logger (Optional[Logger]): Logger instance.
        """
        self.rules = rules
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    def _folders(self) -> List[Path]:
        """Give the folders of the guards' state, resolved.

        Returns:
            List[Path]: Each folder of ``guard_state_folders``.
        """
        return [Path(folder).expanduser().resolve() for folder in self.rules.guard_state_folders]

    ############################
    # Publicly Exposed Methods #
    ############################

    def refusal(self, path: str, cwd: Path) -> Optional[str]:
        """Decide on the file a tool writes.

        Args:
            path (str): The file, as Claude gave it.
            cwd (Path): The session's folder, for a relative path.

        Returns:
            Optional[str]: Why the tool must not write it, ``None`` when it may.
        """
        target = (cwd / Path(path).expanduser()).resolve()
        for folder in self._folders():
            if target == folder or target.is_relative_to(folder):
                self.logger.warning("Refused a file tool in %s.", folder.name)
                return (
                    f"TEST-5/TEST-7: {folder} holds the guards' own state (squash permits, AI test ledgers). "  # noqa: E501
                    "Only their tools write there, run by the human in their own terminal."
                )
        self.logger.debug("The file tool writes outside the guards' state.")
        return None
