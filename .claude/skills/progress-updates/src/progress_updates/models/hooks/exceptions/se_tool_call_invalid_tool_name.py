from __future__ import annotations

from progress_updates.models.hooks.exceptions.se_invalid_tool_call_exception import SEInvalidToolCallException


class SEToolCallInvalidToolName(SEInvalidToolCallException):
    """Exception raised when an invalid ``tool_name`` is provided."""
