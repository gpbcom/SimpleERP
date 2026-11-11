from __future__ import annotations

import logging
from datetime import timedelta
from decimal import Decimal
from pathlib import Path
from typing import Optional

import pytest

from ai_cost.models.enums import CostSource, RunStatus
from ai_cost.models.ledger.cost_run import CostRun
from ai_cost.models.ledger.exceptions import SELedgerInvalidTicket
from ai_cost.service.ledgers.exceptions import SELedgerReadFailedError
from ai_cost.service.ledgers.ledger_service import LedgerService
from tests.service.ledgers.ledger_service_builder import LedgerServiceBuilder
from tests.service.usage.scripted_usage_meter import ScriptedUsageMeter


class TestLedgerService:
    def service(
        self, builder: LedgerServiceBuilder, logger: logging.Logger, *costs: Optional[Decimal]
    ) -> LedgerService:
        return builder.build(ScriptedUsageMeter(list(costs) or [Decimal("0")], logger))

    def running(self, service: LedgerService, estimate: str, source: CostSource = CostSource.USAGE_REPORT) -> CostRun:
        return service.new_run("GH-1", "invoice summary", "uv run pytest -m llm", Decimal(estimate), source)

    def cost_md(self, repo: Path) -> str:
        return (repo / "docs" / "tickets" / "GH-1" / "tests-evidences" / "COST.md").read_text(encoding="utf-8")

    def test_a_new_ticket_has_the_default_cap_and_nothing_written(
        self, builder: LedgerServiceBuilder, logger: logging.Logger, tmp_path: Path
    ) -> None:
        ledger = self.service(builder, logger).ledger("GH-1")
        assert (ledger.cap_usd, ledger.spent_usd, ledger.blocked) == (Decimal("20"), Decimal("0"), False)
        assert not (tmp_path / "state" / "GH-1.json").exists()

    def test_an_admitted_run_is_recorded_and_mirrored(
        self, builder: LedgerServiceBuilder, logger: logging.Logger, repo: Path
    ) -> None:
        service = self.service(builder, logger)
        admitted = service.admit("GH-1", self.running(service, "2"))
        assert admitted.status is RunStatus.RUNNING
        assert [run.id for run in service.ledger("GH-1").runs] == [admitted.id]
        assert admitted.id in self.cost_md(repo)

    def test_a_run_whose_estimate_does_not_fit_is_refused(
        self, builder: LedgerServiceBuilder, logger: logging.Logger
    ) -> None:
        service = self.service(builder, logger)
        service.charge("GH-1", Decimal("19.5"), "earlier runs", "read from the console")
        refused = service.admit("GH-1", self.running(service, "1"))
        assert refused.status is RunStatus.REFUSED
        assert "above the $0.50 left" in str(refused.note)
        assert refused.settled is True

    def test_a_run_of_a_blocked_ticket_is_refused(self, builder: LedgerServiceBuilder, logger: logging.Logger) -> None:
        service = self.service(builder, logger)
        service.record("GH-1", self.running(service, "1"), "killed at $18.20")
        refused = service.admit("GH-1", self.running(service, "0.1"))
        assert refused.status is RunStatus.REFUSED
        assert "blocked" in str(refused.note)

    def test_a_charge_is_recorded_as_charged_and_settled(
        self, builder: LedgerServiceBuilder, logger: logging.Logger, repo: Path
    ) -> None:
        charge = self.service(builder, logger).charge("GH-1", Decimal("0.42"), "soft run", "read from the logs")
        assert (charge.source, charge.settled, charge.cost_usd, charge.status) == (
            CostSource.CHARGED,
            True,
            Decimal("0.42"),
            RunStatus.DONE,
        )
        assert "soft run" in self.cost_md(repo)

    def test_an_ended_run_is_settled_by_a_late_measure_and_blocks_a_ticket_over_its_cap(
        self, builder: LedgerServiceBuilder, logger: logging.Logger
    ) -> None:
        meter = ScriptedUsageMeter([Decimal("21")], logger)
        service = builder.build(meter)
        started = self.running(service, "1")
        run = started.model_copy(update={"started_on": started.started_on - timedelta(minutes=10)})
        ended = run.model_copy(
            update={"status": RunStatus.DONE, "finished_on": run.started_on + timedelta(minutes=2), "cost_usd": 1}
        )
        service.record("GH-1", ended)
        ledger = service.settle("GH-1")
        assert (ledger.runs[0].settled, ledger.spent_usd, ledger.blocked) == (True, Decimal("21"), True)
        assert meter.windows[0] == (run.started_on, ended.finished_on + timedelta(seconds=LedgerService.MARGIN_S))

    def test_a_failed_late_measure_leaves_the_run_unsettled(
        self, builder: LedgerServiceBuilder, logger: logging.Logger
    ) -> None:
        service = self.service(builder, logger, None)
        run = self.running(service, "1")
        service.record("GH-1", run.model_copy(update={"status": RunStatus.DONE, "finished_on": run.started_on}))
        assert service.settle("GH-1").runs[0].settled is False

    def test_an_estimated_run_is_never_measured_again(
        self, builder: LedgerServiceBuilder, logger: logging.Logger
    ) -> None:
        meter = ScriptedUsageMeter([Decimal("5")], logger)
        service = builder.build(meter)
        run = self.running(service, "1", CostSource.ESTIMATE)
        service.record("GH-1", run.model_copy(update={"status": RunStatus.DONE, "finished_on": run.started_on}))
        service.settle("GH-1")
        assert meter.measures == 0

    def test_raising_the_cap_unblocks_only_with_room_below_the_kill_threshold(
        self, builder: LedgerServiceBuilder, logger: logging.Logger
    ) -> None:
        service = self.service(builder, logger)
        service.charge("GH-1", Decimal("19"), "earlier runs", None)
        service.record("GH-1", self.running(service, "1"), "killed at $19.00")
        assert service.raise_cap("GH-1", Decimal("21")).blocked is True
        raised = service.raise_cap("GH-1", Decimal("30"))
        assert (raised.blocked, raised.cap_usd) == (False, Decimal("30"))

    def test_a_key_that_is_not_a_ticket_is_refused(self, builder: LedgerServiceBuilder, logger: logging.Logger) -> None:
        with pytest.raises(SELedgerInvalidTicket):
            self.service(builder, logger).ledger("../etc")

    def test_a_corrupt_ledger_fails_the_read(
        self, builder: LedgerServiceBuilder, logger: logging.Logger, tmp_path: Path
    ) -> None:
        (tmp_path / "state").mkdir()
        (tmp_path / "state" / "GH-1.json").write_text("[]", encoding="utf-8")
        with pytest.raises(SELedgerReadFailedError):
            self.service(builder, logger).ledger("GH-1")
