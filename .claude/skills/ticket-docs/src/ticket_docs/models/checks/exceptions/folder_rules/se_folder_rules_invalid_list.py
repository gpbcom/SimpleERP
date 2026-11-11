from __future__ import annotations

from ticket_docs.models.checks.exceptions.folder_rules.se_invalid_folder_rules_exception import (
    SEInvalidFolderRulesException,
)


class SEFolderRulesInvalidList(SEInvalidFolderRulesException):
    """Exception raised when an invalid list of names, icons or paths is provided."""
