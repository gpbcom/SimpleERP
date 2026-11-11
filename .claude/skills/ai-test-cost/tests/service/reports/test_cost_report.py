from __future__ import annotations

import logging
from datetime import UTC, datetime
from decimal import Decimal
from pathlib import Path

from ai_cost.models.enums import CostSource, RunStatus
from ai_cost.models.ledger.cost_run import CostRun
from ai_cost.models.ledger.ledger import Ledger
from ai_cost.models.ledger.model_usage import ModelUsage
from ai_cost.service.reports.cost_report import CostReport


class TestCostReport:
    TEMPLATE = (Path(__file__).resolve().parents[3] / "templates" / "COST.md").read_text(encoding="utf-8")

    def run(self, run_id: str, cost: str, status: RunStatus, settled: bool) -> CostRun:
        return CostRun(
            id=run_id,
            label="invoice | summary",
            command="uv run pytest -m llm",
            started_on=datetime(2026, 11, 10, 9, 0, tzinfo=UTC),
            finished_on=datetime(2026, 11, 10, 9, 5, tzinfo=UTC),
            estimate_usd=Decimal("1"),
            cost_usd=Decimal(cost),
            status=status,
            source=CostSource.USAGE_REPORT,
            usage={"claude-haiku-5-5": ModelUsage(input_tokens=10, cost_usd=Decimal(cost))},
            settled=settled,
        )

    def test_each_run_is_a_row_with_its_cumulative_spend(self, logger: logging.Logger) -> None:
        ledger = Ledger(
            ticket="GH-1",
            cap_usd=Decimal("20"),
            runs=[self.run("r1", "1.5", RunStatus.DONE, True), self.run("r2", "2.25", RunStatus.FAILED, False)],
        )
        text = CostReport(logger).render(ledger, self.TEMPLATE, "Anthropic pricing page, read 2026-11-10")
        assert text.startswith("# AI test cost: GH-1")
        assert "**Cap:** $20.00 · **Spent:** $3.7500 · **Left:** $16.2500 · **Status:** within the cap" in text
        assert "| `r1` | done | usage_report | invoice \\| summary |" in text
        assert "| $1.5000 | $1.5000 | $18.5000 |" in text
        assert "| `r2` | failed (not final) |" in text
        assert "| $2.2500 | $3.7500 | $16.2500 | claude-haiku-5-5 $2.2500 |" in text
        assert text.rstrip().endswith("Prices: Anthropic pricing page, read 2026-11-10.")

    def test_a_blocked_ticket_says_why(self, logger: logging.Logger) -> None:
        ledger = Ledger(ticket="GH-1", cap_usd=Decimal("20"), block_reason="killed at $18.20")
        text = CostReport(logger).render(ledger, self.TEMPLATE, "prices")
        assert "**Status:** blocked: killed at $18.20" in text
        assert "| no run yet |" in text

    def test_a_ticket_near_its_cap_is_flagged(self, logger: logging.Logger) -> None:
        ledger = Ledger(ticket="GH-1", cap_usd=Decimal("20"), runs=[self.run("r1", "17", RunStatus.DONE, True)])
        assert "**Status:** above 80 % of the cap" in CostReport(logger).render(ledger, self.TEMPLATE, "prices")
