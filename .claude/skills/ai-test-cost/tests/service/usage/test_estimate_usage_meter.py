from __future__ import annotations

import logging
from datetime import UTC, datetime

from ai_cost.service.usage.estimate_usage_meter import EstimateUsageMeter


class TestEstimateUsageMeter:
    def test_nothing_is_measured(self, logger: logging.Logger) -> None:
        meter = EstimateUsageMeter(logger)
        moment = datetime(2026, 11, 10, tzinfo=UTC)
        assert (meter.measurable, meter.ready(), meter.measure(moment, moment)) == (False, True, {})
