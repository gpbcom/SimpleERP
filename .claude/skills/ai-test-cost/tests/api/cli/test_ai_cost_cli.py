from __future__ import annotations

import io
import json
import logging
import sys
from decimal import Decimal
from pathlib import Path
from typing import List, Optional, Tuple

import pytest

from ai_cost.api.factories.cli.cli_command_factory import CliCommandFactory
from ai_cost.models.enums import RunStatus, UsageSource
from ai_cost.models.ledger.ledger import Ledger
from ai_cost.models.settings.caller_environment import CallerEnvironment
from ai_cost.models.settings.guard_settings import GuardSettings
from harness_core.terminal.human_confirmation import HumanConfirmation
from harness_core.testing.scripted_confirmation import ScriptedConfirmation


class TestAiCostCli:
    def call(
        self,
        arguments: List[str],
        settings: Optional[GuardSettings],
        environment: CallerEnvironment,
        logger: logging.Logger,
        tmp_path: Path,
        stdin: str = "",
        confirmation: Optional[HumanConfirmation] = None,
    ) -> Tuple[int, str, str]:
        stdout, stderr = io.StringIO(), io.StringIO()
        cli = CliCommandFactory(tmp_path / "missing-settings.yaml", logger).cli(
            arguments, io.StringIO(stdin), stdout, stderr, settings, environment, confirmation
        )
        cli.execute()
        return cli.exit_code, stdout.getvalue(), stderr.getvalue()

    def ledger(self, settings: GuardSettings) -> Ledger:
        return Ledger.model_validate_json((settings.state_dir / "GH-1.json").read_text(encoding="utf-8"))

    def estimate(self, settings: GuardSettings) -> GuardSettings:
        return settings.model_copy(update={"usage_source": UsageSource.ESTIMATE})

    def test_the_gate_refuses_an_unguarded_paid_test_as_the_hook_expects(
        self, settings: GuardSettings, environment: CallerEnvironment, logger: logging.Logger, tmp_path: Path
    ) -> None:
        hook = json.dumps({"tool_name": "Bash", "tool_input": {"command": "uv run pytest -m llm"}})
        code, out, _ = self.call(["gate"], settings, environment, logger, tmp_path, hook)
        answer = json.loads(out)
        assert code == 0
        assert answer["hookSpecificOutput"]["hookEventName"] == "PreToolUse"
        assert answer["hookSpecificOutput"]["permissionDecision"] == "deny"
        assert "calls a paid AI" in answer["hookSpecificOutput"]["permissionDecisionReason"]

    @pytest.mark.parametrize("hook", ['{"tool_input": {"command": "git status"}}', "not json", "{}", "[]"])
    def test_the_gate_says_nothing_when_it_allows(
        self,
        settings: GuardSettings,
        environment: CallerEnvironment,
        logger: logging.Logger,
        tmp_path: Path,
        hook: str,
    ) -> None:
        assert self.call(["gate"], settings, environment, logger, tmp_path, hook) == (0, "", "")

    def test_the_gate_refuses_when_its_settings_cannot_be_read(
        self, environment: CallerEnvironment, logger: logging.Logger, tmp_path: Path
    ) -> None:
        hook = json.dumps({"tool_input": {"command": "git status"}})
        code, out, _ = self.call(["gate"], None, environment, logger, tmp_path, hook)
        assert code == 0
        assert "settings" in json.loads(out)["hookSpecificOutput"]["permissionDecisionReason"]

    def test_a_soft_run_is_charged_and_recorded(
        self,
        settings: GuardSettings,
        environment: CallerEnvironment,
        logger: logging.Logger,
        tmp_path: Path,
        repo: Path,
    ) -> None:
        arguments = ["run", "--ticket", "GH-1", "--estimate-usd", "0.4", "--label", "summary", "--soft", "--"]
        code, _, err = self.call([*arguments, sys.executable, "-c", "pass"], settings, environment, logger, tmp_path)
        ledger = self.ledger(settings)
        assert code == 0
        assert (ledger.runs[0].status, ledger.spent_usd) == (RunStatus.DONE, Decimal("0.4"))
        assert ledger.runs[0].id in err
        assert (repo / "docs" / "tickets" / "GH-1" / "tests-evidences" / "COST.md").is_file()

    def test_a_run_of_the_estimate_source_needs_no_key(
        self, settings: GuardSettings, environment: CallerEnvironment, logger: logging.Logger, tmp_path: Path
    ) -> None:
        arguments = ["run", "--ticket", "GH-1", "--estimate-usd", "1", "--", sys.executable, "-c", "pass"]
        code, _, _ = self.call(arguments, self.estimate(settings), environment, logger, tmp_path)
        assert code == 0

    def test_a_run_that_does_not_fit_is_refused_with_exit_code_3(
        self, settings: GuardSettings, environment: CallerEnvironment, logger: logging.Logger, tmp_path: Path
    ) -> None:
        arguments = ["run", "--ticket", "GH-1", "--estimate-usd", "25", "--soft", "--", sys.executable, "-c", "pass"]
        code, _, err = self.call(arguments, settings, environment, logger, tmp_path)
        assert code == 3
        assert "refused" in err

    def test_a_measured_run_without_the_admin_key_is_a_usage_error(
        self,
        settings: GuardSettings,
        environment: CallerEnvironment,
        logger: logging.Logger,
        tmp_path: Path,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        monkeypatch.delenv("ANTHROPIC_ADMIN_KEY", raising=False)
        arguments = ["run", "--ticket", "GH-1", "--estimate-usd", "1", "--", sys.executable, "-c", "pass"]
        code, _, err = self.call(arguments, settings, environment, logger, tmp_path)
        assert code == 2
        assert "ANTHROPIC_ADMIN_KEY" in err
        assert not (settings.state_dir / "GH-1.json").exists()

    @pytest.mark.parametrize(
        "arguments",
        [
            ["run", "--ticket", "GH-1", "--estimate-usd", "1", "--soft", "--"],
            ["run", "--ticket", "ARE-1", "--estimate-usd", "1", "--soft", "--", "true"],
            ["run", "--ticket", "GH-1", "--estimate-usd", "a lot", "--soft", "--", "true"],
            ["run", "--estimate-usd", "1", "--", "true"],
            ["charge", "GH-1", "-1", "--label", "x"],
            ["status", "../GH-1"],
            ["unknown"],
        ],
    )
    def test_a_usage_error_exits_with_2(
        self,
        settings: GuardSettings,
        environment: CallerEnvironment,
        logger: logging.Logger,
        tmp_path: Path,
        arguments: List[str],
    ) -> None:
        assert self.call(arguments, settings, environment, logger, tmp_path)[0] == 2

    def test_status_remaining_charge_and_raise_cap(
        self, settings: GuardSettings, environment: CallerEnvironment, logger: logging.Logger, tmp_path: Path
    ) -> None:
        charged = self.call(
            ["charge", "GH-1", "1.25", "--label", "console", "--note", "read on the Cost page"],
            settings,
            environment,
            logger,
            tmp_path,
        )
        assert charged[0] == 0
        assert "$1.2500" in charged[1]
        status = self.call(["status", "GH-1"], settings, environment, logger, tmp_path)[1]
        assert "GH-1: $1.2500 of $20.00, $18.7500 left" in status
        assert "console" in status
        assert self.call(["remaining", "GH-1"], settings, environment, logger, tmp_path)[1].strip() == "18.7500"
        human = ScriptedConfirmation(True, logger)
        raised = self.call(["raise-cap", "GH-1", "30"], settings, environment, logger, tmp_path, confirmation=human)
        assert (raised[0], self.ledger(settings).cap_usd) == (0, Decimal("30"))
        assert len(human.questions) == 1
        assert "GH-1" in human.questions[0]

    def test_raise_cap_without_a_terminal_is_refused_with_exit_code_3(
        self, settings: GuardSettings, environment: CallerEnvironment, logger: logging.Logger, tmp_path: Path
    ) -> None:
        self.call(["charge", "GH-1", "1", "--label", "x"], settings, environment, logger, tmp_path)
        no_terminal = HumanConfirmation(tmp_path / "no-tty", logger)
        code, _, err = self.call(
            ["raise-cap", "GH-1", "30"], settings, environment, logger, tmp_path, confirmation=no_terminal
        )
        assert code == 3
        assert "Only the human, in their own terminal" in err
        assert self.ledger(settings).cap_usd == Decimal("20")

    def test_raise_cap_needs_the_code_shown_on_the_terminal_typed_back(
        self, settings: GuardSettings, environment: CallerEnvironment, logger: logging.Logger, tmp_path: Path
    ) -> None:
        self.call(["charge", "GH-1", "1", "--label", "x"], settings, environment, logger, tmp_path)
        human = ScriptedConfirmation(False, logger)
        code, _, err = self.call(
            ["raise-cap", "GH-1", "30"], settings, environment, logger, tmp_path, confirmation=human
        )
        assert code == 3
        assert "Only the human, in their own terminal" in err
        assert self.ledger(settings).cap_usd == Decimal("20")

    def test_a_confirmed_raise_cap_with_a_bad_amount_is_a_usage_error(
        self, settings: GuardSettings, environment: CallerEnvironment, logger: logging.Logger, tmp_path: Path
    ) -> None:
        human = ScriptedConfirmation(True, logger)
        assert (
            self.call(["raise-cap", "GH-1", "0"], settings, environment, logger, tmp_path, confirmation=human)[0] == 2
        )
