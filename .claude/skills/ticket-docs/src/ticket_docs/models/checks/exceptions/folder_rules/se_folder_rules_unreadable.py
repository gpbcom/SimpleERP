from __future__ import annotations

from ticket_docs.models.checks.exceptions.folder_rules.se_invalid_folder_rules_exception import (
    SEInvalidFolderRulesException,
)


class SEFolderRulesUnreadable(SEInvalidFolderRulesException):
    """Exception raised when the folder rules file cannot be read."""
