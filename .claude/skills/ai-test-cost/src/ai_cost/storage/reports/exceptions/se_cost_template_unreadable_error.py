from __future__ import annotations

from ai_cost.storage.reports.exceptions.se_cost_file_error import SECostFileError


class SECostTemplateUnreadableError(SECostFileError):
    """Raised when the COST.md template cannot be read."""
