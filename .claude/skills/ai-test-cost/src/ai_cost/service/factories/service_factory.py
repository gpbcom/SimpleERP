from __future__ import annotations

# Standard library imports
from abc import ABC, abstractmethod
from decimal import Decimal
from logging import Logger, getLogger
from typing import List, Optional

# First-party imports
from ai_cost.service.gate.command_gate import CommandGate
from ai_cost.service.ledgers.ledger_service import LedgerService
from ai_cost.service.runs.guarded_run import GuardedRun
from ai_cost.service.usage.usage_meter import UsageMeter


class ServiceFactory(ABC):
    """Builds the guard's services and its runnable, the guarded run.

    Attributes:
        logger (Logger): Logger instance.
    """

    def __init__(self, logger: Optional[Logger] = None) -> None:
        """Set the logger.

        Args:
            logger (Optional[Logger]): Logger instance.
        """
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Publicly Exposed Methods #
    ############################

    @abstractmethod
    def usage_meter(self) -> UsageMeter:
        """Build the meter of the configured usage source.

        Returns:
            UsageMeter: The meter.
        """

    @abstractmethod
    def ledger_service(self) -> LedgerService:
        """Build the ledger service.

        Returns:
            LedgerService: The service.
        """

    @abstractmethod
    def command_gate(self) -> CommandGate:
        """Build the gate of the PreToolUse hook.

        Returns:
            CommandGate: The gate.
        """

    @abstractmethod
    def guarded_run(
        self, ticket: str, label: str, command: List[str], estimate_usd: Decimal, soft: bool, on_kill: Optional[str]
    ) -> GuardedRun:
        """Build one guarded run.

        Args:
            ticket (str): The ticket the cost is charged to.
            label (str): What the run tests.
            command (List[str]): The command and its arguments.
            estimate_usd (Decimal): What the run is expected to cost.
            soft (bool): Whether the run is charged its estimate instead of being measured.
            on_kill (Optional[str]): The command that stops what the run started elsewhere.

        Returns:
            GuardedRun: The run, not started.
        """
