from __future__ import annotations

# Standard library imports
from abc import ABC, abstractmethod
from logging import Logger, getLogger
from typing import Optional, Union

# First-party imports
from erp_lifecycle.runnables.async_runnable import AsyncRunnable
from erp_lifecycle.runnables.runnable import Runnable


class RunnableFactory[RunnableT: Union[Runnable, AsyncRunnable]](ABC):
    """Abstract factory that builds one kind of runnable.

    Attributes:
        logger (Logger): Logger instance.

    Notes:
        - **The factory is the only place in ``src/`` where a runnable's constructor is called.**
        - A concrete factory receives the inputs of the runnable at its own constructor, so ``create()`` takes no
          argument.
    """

    def __init__(self, logger: Optional[Logger] = None) -> None:
        """Create the factory.

        Args:
            logger (Optional[Logger]): Logger to use. A logger named after the module is created when it is ``None``.
        """
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Publicly Exposed Methods #
    ############################

    @abstractmethod
    def create(self) -> RunnableT:
        """Build a new runnable.

        Returns:
            RunnableT: A new runnable, not yet initialised.
        """
