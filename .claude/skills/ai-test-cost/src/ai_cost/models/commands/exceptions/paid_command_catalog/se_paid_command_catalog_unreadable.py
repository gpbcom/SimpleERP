from __future__ import annotations

from ai_cost.models.commands.exceptions.paid_command_catalog.se_invalid_paid_command_catalog_exception import (
    SEInvalidPaidCommandCatalogException,
)


class SEPaidCommandCatalogUnreadable(SEInvalidPaidCommandCatalogException):
    """Exception raised when the paid command file cannot be read or parsed."""
