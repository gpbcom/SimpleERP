from __future__ import annotations

import logging
from decimal import Decimal

from ai_cost.models.enums import UsageSource
from ai_cost.models.settings.caller_environment import CallerEnvironment
from ai_cost.models.settings.guard_settings import GuardSettings
from ai_cost.service.factories.default.default_service_factory import DefaultServiceFactory
from ai_cost.service.gate.command_gate import CommandGate
from ai_cost.service.ledgers.ledger_service import LedgerService
from ai_cost.service.runs.guarded_run import GuardedRun
from ai_cost.service.usage.anthropic_usage_meter import AnthropicUsageMeter
from ai_cost.service.usage.estimate_usage_meter import EstimateUsageMeter


class TestDefaultServiceFactory:
    def test_each_usage_source_gets_its_meter(
        self, settings: GuardSettings, environment: CallerEnvironment, logger: logging.Logger
    ) -> None:
        estimate = settings.model_copy(update={"usage_source": UsageSource.ESTIMATE})
        assert isinstance(DefaultServiceFactory(settings, environment, logger).usage_meter(), AnthropicUsageMeter)
        assert isinstance(DefaultServiceFactory(estimate, environment, logger).usage_meter(), EstimateUsageMeter)

    def test_the_services_and_the_guarded_run_are_built(
        self, settings: GuardSettings, environment: CallerEnvironment, logger: logging.Logger
    ) -> None:
        factory = DefaultServiceFactory(settings, environment, logger)
        assert isinstance(factory.ledger_service(), LedgerService)
        assert isinstance(factory.command_gate(), CommandGate)
        run = factory.guarded_run("GH-1", "x", ["true"], Decimal("1"), True, None)
        assert isinstance(run, GuardedRun)
        assert (run.ticket, run.soft, run.environment) == ("GH-1", True, environment)
