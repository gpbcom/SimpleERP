from __future__ import annotations

import logging
from datetime import datetime
from decimal import Decimal
from typing import Dict, List, Optional, Tuple

from ai_cost.models.ledger.model_usage import ModelUsage
from ai_cost.service.usage.exceptions import SEUsageMeasureFailedError
from ai_cost.service.usage.usage_meter import UsageMeter


class ScriptedUsageMeter(UsageMeter):
    """A real meter whose measures follow a script: each measure gives the next cost, ``None`` fails, the last repeats.

    Attributes:
        costs (List[Optional[Decimal]]): The cost of each measure.
        measures (int): The measures taken.
        windows (List[Tuple[datetime, datetime]]): The window of each measure.
    """

    def __init__(self, costs: List[Optional[Decimal]], logger: logging.Logger) -> None:
        super().__init__(logger)
        self.costs = costs
        self.measures = 0
        self.windows: List[Tuple[datetime, datetime]] = []

    @property
    def measurable(self) -> bool:
        return True

    def ready(self) -> bool:
        return True

    def measure(self, start: datetime, end: datetime) -> Dict[str, ModelUsage]:
        cost = self.costs[min(self.measures, len(self.costs) - 1)]
        self.measures += 1
        self.windows.append((start, end))
        if cost is None:
            raise SEUsageMeasureFailedError("The scripted measure failed.")
        return {"claude-haiku-5-5": ModelUsage(input_tokens=1000, output_tokens=100, cost_usd=cost)}
