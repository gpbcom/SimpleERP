from __future__ import annotations

# Standard library imports
import json
import sys

# First-party imports
from progress_updates.api.cli.command import Command
from progress_updates.models.hooks.exceptions import SEInvalidToolCallException
from progress_updates.models.hooks.tool_call import ToolCall


class HookCommand(Command):
    """``progress-updates hook``: Claude Code's ``PostToolUse`` hook, which reminds Claude to report progress.

    Notes:
        **The hook never fails and never blocks**: a payload it cannot read is logged and answered with nothing.
    """

    ############################
    # Internal Helpers Methods #
    ############################

    def _perform(self) -> None:
        """Read the tool call on the standard input and print the reminder, if any, as the hook's answer."""
        try:
            call = ToolCall.from_json(sys.stdin.read())
        except SEInvalidToolCallException as error:
            self.logger.warning("The hook payload was not read: %s.", type(error).__name__)
            return
        reason = self.services.reminder().reminder(call)
        if reason is None:
            return
        answer = {"hookEventName": "PostToolUse", "additionalContext": reason}
        print(json.dumps({"hookSpecificOutput": answer}))
