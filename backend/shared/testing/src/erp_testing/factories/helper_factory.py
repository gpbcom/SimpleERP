from __future__ import annotations

# Standard library imports
from typing import Union

# First-party imports
from erp_lifecycle.factories.runnable_factory import RunnableFactory
from erp_lifecycle.runnables.async_runnable import AsyncRunnable
from erp_lifecycle.runnables.runnable import Runnable


class HelperFactory[RunnableT: Union[Runnable, AsyncRunnable]](RunnableFactory[RunnableT]):
    """Abstract factory base of the runnables of the test helpers library.

    Attributes:
        logger (Logger): Logger instance.

    Notes:
        - It adds nothing to ``RunnableFactory``: it names the family, so that the stand-in server and the PostgreSQL
          test server have concrete factories in ``factories/stand_in/`` and ``factories/postgres/``.
        - **A helper's constructor is called only by its factory.**
    """
