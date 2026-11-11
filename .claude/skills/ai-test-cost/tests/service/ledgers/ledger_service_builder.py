from __future__ import annotations

import logging

from ai_cost.models.settings.caller_environment import CallerEnvironment
from ai_cost.models.settings.guard_settings import GuardSettings
from ai_cost.service.ledgers.ledger_service import LedgerService
from ai_cost.service.reports.cost_report import CostReport
from ai_cost.service.usage.usage_meter import UsageMeter
from ai_cost.storage.ledgers.ledger_repository import LedgerRepository
from ai_cost.storage.reports.cost_file_repository import CostFileRepository


class LedgerServiceBuilder:
    """Builds the ledger service of a test's state folder and repository, with the meter the test chooses."""

    PRICE_SOURCE = "Anthropic pricing page, read 2026-11-10"

    def __init__(self, settings: GuardSettings, environment: CallerEnvironment, logger: logging.Logger) -> None:
        self.settings = settings
        self.environment = environment
        self.logger = logger

    def build(self, meter: UsageMeter) -> LedgerService:
        return LedgerService(
            self.settings,
            LedgerRepository(self.settings.state_dir, self.logger),
            CostFileRepository(self.environment.caller_cwd, self.settings.cost_template_file, self.logger),
            meter,
            CostReport(self.logger),
            self.PRICE_SOURCE,
            self.logger,
        )
