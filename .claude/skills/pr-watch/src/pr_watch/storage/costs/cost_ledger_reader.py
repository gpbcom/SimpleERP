from __future__ import annotations

# Standard library imports
import json
from logging import Logger, getLogger
from pathlib import Path
from typing import ClassVar, List, Optional

# Third-party imports
from pydantic import JsonValue, ValidationError

# First-party imports
from pr_watch.models.exceptions import SEPrWatchError
from pr_watch.models.sessions.cost_ledger import CostLedger


class CostLedgerReader:
    """Reads what a ticket's AI tests cost, from the ledgers the ai-test-cost skill writes.

    Attributes:
        KEYS (List[str]): The keys of a ledger this reader uses.
        state_dir (Path): The folder of the ledgers, one ``<KEY>.json`` per ticket.
        logger (Logger): Logger instance.

    Notes:
        - The ledger belongs to the ai-test-cost skill: only its four keys this page shows are read, so that the
          ledger may grow without breaking the summary page.
        - A ledger that cannot be read shows as no cost, with a warning, rather than stopping the page.
    """

    KEYS: ClassVar[List[str]] = ["ticket", "cap_usd", "spent_usd", "blocked"]

    def __init__(self, state_dir: Path, logger: Optional[Logger] = None) -> None:
        """Set the folder of the ledgers.

        Args:
            state_dir (Path): The folder of the ledgers.
            logger (Optional[Logger]): Logger instance.
        """
        self.state_dir = state_dir
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Publicly Exposed Methods #
    ############################

    def read(self, key: str) -> Optional[CostLedger]:
        """Read the ledger of a ticket.

        Args:
            key (str): The ticket.

        Returns:
            Optional[CostLedger]: Its spend and cap, ``None`` when it has no readable ledger.
        """
        path = self.state_dir / f"{key}.json"
        if not path.exists():
            return None
        try:
            data: JsonValue = json.loads(path.read_text(encoding="utf-8"))
            entry = data if isinstance(data, dict) else {}
            return CostLedger(**{name: entry.get(name) for name in self.KEYS})
        except (OSError, ValueError, ValidationError, SEPrWatchError) as error:
            self.logger.warning("The cost ledger of %s cannot be read: %s.", key, type(error).__name__)
            return None
