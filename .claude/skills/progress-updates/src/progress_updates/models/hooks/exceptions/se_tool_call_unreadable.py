from __future__ import annotations

from progress_updates.models.hooks.exceptions.se_invalid_tool_call_exception import SEInvalidToolCallException


class SEToolCallUnreadable(SEInvalidToolCallException):
    """Exception raised when a hook payload is not the JSON of a tool call."""
