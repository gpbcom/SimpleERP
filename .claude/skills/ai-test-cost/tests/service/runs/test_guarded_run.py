from __future__ import annotations

import json
import logging
import os
import sys
from decimal import Decimal
from pathlib import Path
from typing import List, Optional

import pytest

from ai_cost.models.enums import CostSource, RunStatus
from ai_cost.models.settings.caller_environment import CallerEnvironment
from ai_cost.models.settings.guard_settings import GuardSettings
from ai_cost.service.ledgers.ledger_service import LedgerService
from ai_cost.service.runs.guarded_run import GuardedRun
from ai_cost.service.usage.estimate_usage_meter import EstimateUsageMeter
from ai_cost.service.usage.usage_meter import UsageMeter
from tests.service.ledgers.ledger_service_builder import LedgerServiceBuilder
from tests.service.usage.scripted_usage_meter import ScriptedUsageMeter


class TestGuardedRun:
    def guarded(
        self,
        command: List[str],
        estimate: str,
        meter: UsageMeter,
        builder: LedgerServiceBuilder,
        settings: GuardSettings,
        environment: CallerEnvironment,
        logger: logging.Logger,
        soft: bool = False,
        on_kill: Optional[str] = None,
    ) -> GuardedRun:
        ledgers = builder.build(meter)
        return GuardedRun(
            "GH-1",
            "invoice summary",
            command,
            Decimal(estimate),
            soft,
            on_kill,
            settings,
            environment,
            ledgers,
            meter,
            logger,
        )

    def ledgers(self, builder: LedgerServiceBuilder, logger: logging.Logger) -> LedgerService:
        return builder.build(EstimateUsageMeter(logger))

    def test_a_run_that_ends_by_itself_is_measured_recorded_and_mirrored(
        self,
        builder: LedgerServiceBuilder,
        settings: GuardSettings,
        environment: CallerEnvironment,
        logger: logging.Logger,
        repo: Path,
    ) -> None:
        meter = ScriptedUsageMeter([Decimal("0.25")], logger)
        run = self.guarded([sys.executable, "-c", "pass"], "1", meter, builder, settings, environment, logger)
        run.execute()
        assert run.result is not None
        assert (run.result.status, run.result.cost_usd, run.result.exit_code, run.exit_code) == (
            RunStatus.DONE,
            Decimal("0.25"),
            0,
            0,
        )
        cost = (repo / "docs" / "tickets" / "GH-1" / "tests-evidences" / "COST.md").read_text(encoding="utf-8")
        assert "invoice summary" in cost
        assert "$0.2500" in cost

    @pytest.mark.parametrize(
        ("spent", "block"), [("19.5", None), ("1", "killed at $18.20")], ids=["too-dear", "blocked"]
    )
    def test_a_refused_run_never_starts(
        self,
        builder: LedgerServiceBuilder,
        settings: GuardSettings,
        environment: CallerEnvironment,
        logger: logging.Logger,
        tmp_path: Path,
        spent: str,
        block: Optional[str],
    ) -> None:
        ledgers = self.ledgers(builder, logger)
        ledgers.charge("GH-1", Decimal(spent), "earlier runs", None)
        if block is not None:
            ledgers.record("GH-1", ledgers.new_run("GH-1", "x", "x", Decimal("0"), CostSource.ESTIMATE), block)
        marker = tmp_path / "ran"
        command = [sys.executable, "-c", f"open({str(marker)!r}, 'w')"]
        meter = ScriptedUsageMeter([Decimal("0")], logger)
        run = self.guarded(command, "1", meter, builder, settings, environment, logger)
        run.execute()
        assert run.result is not None
        assert (run.result.status, run.exit_code, marker.exists()) == (RunStatus.REFUSED, 3, False)

    def test_a_run_reaching_the_kill_threshold_is_killed_with_its_children_and_blocks_the_ticket(
        self,
        builder: LedgerServiceBuilder,
        settings: GuardSettings,
        environment: CallerEnvironment,
        logger: logging.Logger,
        tmp_path: Path,
    ) -> None:
        pid_file = tmp_path / "child.pid"
        stopped = tmp_path / "stopped"
        script = (
            "import subprocess, time; child = subprocess.Popen(['sleep', '60']); "
            f"open({str(pid_file)!r}, 'w').write(str(child.pid)); time.sleep(60)"
        )
        on_kill = f"{sys.executable} -c \"open('{stopped}', 'w')\""
        meter = ScriptedUsageMeter([Decimal("2"), Decimal("18.5")], logger)
        run = self.guarded(
            [sys.executable, "-c", script], "5", meter, builder, settings, environment, logger, on_kill=on_kill
        )
        run.execute()
        ledger = self.ledgers(builder, logger).ledger("GH-1")
        assert run.result is not None
        assert (run.result.status, run.exit_code, ledger.blocked, stopped.exists()) == (
            RunStatus.KILLED_AT_CAP,
            3,
            True,
            True,
        )
        with pytest.raises(ProcessLookupError):
            os.kill(int(pid_file.read_text(encoding="utf-8")), 0)

    def test_a_run_that_cannot_be_measured_is_stopped(
        self,
        builder: LedgerServiceBuilder,
        settings: GuardSettings,
        environment: CallerEnvironment,
        logger: logging.Logger,
    ) -> None:
        meter = ScriptedUsageMeter([None], logger)
        command = [sys.executable, "-c", "import time; time.sleep(60)"]
        run = self.guarded(command, "1", meter, builder, settings, environment, logger)
        run.execute()
        assert run.result is not None
        assert run.result.status is RunStatus.FAILED
        assert "could not be measured 3 times in a row" in str(run.result.note)
        assert run.exit_code != 0

    def test_a_soft_run_is_charged_its_estimate(
        self,
        builder: LedgerServiceBuilder,
        settings: GuardSettings,
        environment: CallerEnvironment,
        logger: logging.Logger,
    ) -> None:
        meter = ScriptedUsageMeter([None], logger)
        run = self.guarded(
            [sys.executable, "-c", "pass"], "0.4", meter, builder, settings, environment, logger, soft=True
        )
        run.execute()
        assert run.result is not None
        assert (run.result.status, run.result.source, run.result.cost_usd, run.result.settled, meter.measures) == (
            RunStatus.DONE,
            CostSource.ESTIMATE,
            Decimal("0.4"),
            True,
            0,
        )

    def test_the_child_sees_its_run_id_and_ticket_and_runs_in_the_callers_folder(
        self,
        builder: LedgerServiceBuilder,
        settings: GuardSettings,
        environment: CallerEnvironment,
        logger: logging.Logger,
        tmp_path: Path,
    ) -> None:
        seen = tmp_path / "seen.json"
        script = (
            "import json, os; json.dump({'run': os.environ.get('AI_COST_RUN_ID'), "
            f"'ticket': os.environ.get('AI_COST_TICKET'), 'cwd': os.getcwd()}}, open({str(seen)!r}, 'w'))"
        )
        meter = EstimateUsageMeter(logger)
        run = self.guarded([sys.executable, "-c", script], "0.1", meter, builder, settings, environment, logger)
        run.execute()
        assert run.result is not None
        child = json.loads(seen.read_text(encoding="utf-8"))
        assert (child["run"], child["ticket"], Path(child["cwd"])) == (
            run.result.id,
            "GH-1",
            environment.caller_cwd.resolve(),
        )

    def test_the_commands_own_failure_is_kept(
        self,
        builder: LedgerServiceBuilder,
        settings: GuardSettings,
        environment: CallerEnvironment,
        logger: logging.Logger,
    ) -> None:
        meter = ScriptedUsageMeter([Decimal("0.1")], logger)
        run = self.guarded(
            [sys.executable, "-c", "raise SystemExit(4)"], "1", meter, builder, settings, environment, logger
        )
        run.execute()
        assert run.result is not None
        assert (run.result.status, run.result.exit_code, run.exit_code) == (RunStatus.FAILED, 4, 4)

    def test_a_command_that_cannot_start_is_recorded_as_failed(
        self,
        builder: LedgerServiceBuilder,
        settings: GuardSettings,
        environment: CallerEnvironment,
        logger: logging.Logger,
    ) -> None:
        meter = ScriptedUsageMeter([Decimal("0")], logger)
        run = self.guarded(["/no/such/program"], "1", meter, builder, settings, environment, logger)
        run.execute()
        assert run.result is not None
        assert (run.result.status, run.exit_code) == (RunStatus.FAILED, 127)
        assert "could not start" in str(run.result.note)
