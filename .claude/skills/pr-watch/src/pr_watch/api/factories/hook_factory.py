from __future__ import annotations

# Standard library imports
from abc import ABC, abstractmethod

# First-party imports
from pr_watch.api.cli.hooks.hook_command import HookCommand


class HookFactory(ABC):
    """Builds the prompt hook.

    Notes:
        The hook has its own factory, apart from ``CommandFactory``, so that building it imports none of the other
        commands and their services.
    """

    @abstractmethod
    def __init__(self) -> None:
        """Set what the hook is built with."""

    ############################
    # Publicly Exposed Methods #
    ############################

    @abstractmethod
    def hook(self) -> HookCommand:
        """Build the prompt hook.

        Returns:
            HookCommand: The hook, ready to ``execute``.
        """
