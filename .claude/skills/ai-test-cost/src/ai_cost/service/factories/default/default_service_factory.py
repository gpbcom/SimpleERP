from __future__ import annotations

# Standard library imports
from decimal import Decimal
from logging import Logger
from typing import List, Optional

# Third-party imports
import httpx

# First-party imports
from ai_cost.models.commands.paid_command_catalog import PaidCommandCatalog
from ai_cost.models.enums import UsageSource
from ai_cost.models.pricing.price_table import PriceTable
from ai_cost.models.settings.caller_environment import CallerEnvironment
from ai_cost.models.settings.guard_settings import GuardSettings
from ai_cost.service.factories.service_factory import ServiceFactory
from ai_cost.service.gate.command_gate import CommandGate
from ai_cost.service.gate.pytest_invocation import PytestInvocation
from ai_cost.service.ledgers.ledger_service import LedgerService
from ai_cost.service.pricing.price_book import PriceBook
from ai_cost.service.reports.cost_report import CostReport
from ai_cost.service.runs.guarded_run import GuardedRun
from ai_cost.service.usage.anthropic_usage_meter import AnthropicUsageMeter
from ai_cost.service.usage.estimate_usage_meter import EstimateUsageMeter
from ai_cost.service.usage.usage_meter import UsageMeter
from ai_cost.storage.ledgers.ledger_repository import LedgerRepository
from ai_cost.storage.reports.cost_file_repository import CostFileRepository
from ai_cost.storage.usage.anthropic_usage_client import AnthropicUsageClient
from harness_core.shell.shell_command_splitter import ShellCommandSplitter


class DefaultServiceFactory(ServiceFactory):
    """Builds the guard's services from its settings and the caller's environment.

    Attributes:
        settings (GuardSettings): The enforcing settings.
        environment (CallerEnvironment): The caller's folder and API key id.
        transport (Optional[httpx.BaseTransport]): The HTTP transport of the usage report, the network by default.
        logger (Logger): Logger instance.

    Notes:
        The gate's ledger service never measures, so it is built with the estimate meter: answering the hook needs
        neither the prices nor the network.
    """

    def __init__(
        self,
        settings: GuardSettings,
        environment: CallerEnvironment,
        logger: Optional[Logger] = None,
        transport: Optional[httpx.BaseTransport] = None,
    ) -> None:
        """Set the settings and the caller's environment.

        Args:
            settings (GuardSettings): The enforcing settings.
            environment (CallerEnvironment): The caller's folder and API key id.
            logger (Optional[Logger]): Logger instance.
            transport (Optional[httpx.BaseTransport]): The HTTP transport of the usage report.
        """
        super().__init__(logger)
        self.settings = settings
        self.environment = environment
        self.transport = transport

    ############################
    # Internal Helpers Methods #
    ############################

    def _prices(self) -> PriceBook:
        """Load the prices.

        Returns:
            PriceBook: The prices of ``prices_file``.
        """
        return PriceBook(PriceTable.load(self.settings.prices_file), self.logger)

    def _ledgers(self, meter: UsageMeter, price_source: str) -> LedgerService:
        """Build a ledger service around a meter.

        Args:
            meter (UsageMeter): Measures an ended run again when it settles.
            price_source (str): Where the prices come from, for ``COST.md``.

        Returns:
            LedgerService: The service.
        """
        return LedgerService(
            self.settings,
            LedgerRepository(self.settings.state_dir, self.logger),
            CostFileRepository(self.environment.caller_cwd, self.settings.cost_template_file, self.logger),
            meter,
            CostReport(self.logger),
            price_source,
            self.logger,
        )

    ############################
    # Publicly Exposed Methods #
    ############################

    def usage_meter(self) -> UsageMeter:
        """Build the meter of the configured usage source.

        Returns:
            UsageMeter: The Anthropic usage report meter, or the estimate meter.
        """
        self.logger.debug("Building the %s meter.", self.settings.usage_source)
        match self.settings.usage_source:
            case UsageSource.ANTHROPIC:
                client = AnthropicUsageClient(self.environment.api_key_id, self.logger, self.transport)
                return AnthropicUsageMeter(client, self._prices(), self.logger)
            case UsageSource.ESTIMATE:
                return EstimateUsageMeter(self.logger)

    def ledger_service(self) -> LedgerService:
        """Build the ledger service, with the configured meter.

        Returns:
            LedgerService: The service.
        """
        prices = self._prices()
        return self._ledgers(self.usage_meter(), prices.source)

    def command_gate(self) -> CommandGate:
        """Build the gate of the PreToolUse hook.

        Returns:
            CommandGate: The gate.
        """
        return CommandGate(
            PaidCommandCatalog.load(self.settings.paid_commands_file),
            self._ledgers(EstimateUsageMeter(self.logger), "not read by the gate"),
            ShellCommandSplitter(self.logger),
            PytestInvocation(self.logger),
            self.logger,
        )

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
        meter = self.usage_meter()
        prices = self._prices()
        self.logger.debug("Building a guarded run for %s.", ticket)
        return GuardedRun(
            ticket,
            label,
            command,
            estimate_usd,
            soft,
            on_kill,
            self.settings,
            self.environment,
            self._ledgers(meter, prices.source),
            meter,
            self.logger,
        )
