from __future__ import annotations

import logging
from decimal import Decimal
from typing import Optional

import pytest

from ai_cost.models.commands.paid_command_catalog import PaidCommandCatalog
from ai_cost.models.enums import CostSource
from ai_cost.models.settings.guard_settings import GuardSettings
from ai_cost.service.gate.command_gate import CommandGate
from ai_cost.service.gate.pytest_invocation import PytestInvocation
from ai_cost.service.usage.estimate_usage_meter import EstimateUsageMeter
from harness_core.shell.shell_command_splitter import ShellCommandSplitter
from tests.service.ledgers.ledger_service_builder import LedgerServiceBuilder


class TestCommandGate:
    @pytest.mark.parametrize(
        ("command", "refused"),
        [
            ("cd app && pytest tests -m llm", "calls a paid AI"),
            ("ai-cost run --ticket GH-1 --estimate-usd 2 -- pytest -m llm", None),
            (".claude/skills/ai-test-cost/bin/ai-cost run --ticket=GH-1 --estimate-usd 2 -- pytest -m llm", None),
            ("ai-cost run --estimate-usd 2 -- pytest -m llm", "needs `--ticket <KEY>`"),
            ("ai-cost run --ticket GH-2 --estimate-usd 2 -- pytest -m llm", "blocked"),
            ("ai-cost run --ticket ARE-1 --estimate-usd 2 -- pytest -m llm", "ticket key such as GH-12"),
            ("ai-cost run --ticket GH-1 --estimate-usd 1 -- true; pytest -m llm", "calls a paid AI"),
            ("ai-cost raise-cap GH-1 40", "Only the human"),
            ("cd /tmp && ~/.local/bin/ai-cost -v raise-cap GH-1 40", "Only the human"),
            ("python3 -m ai_cost raise-cap GH-1 40", "Only the human"),
            ('ai-cost "raise-cap" GH-1 40', "Only the human"),
            ("ai-cost 'raise'-cap GH-1 40", "Only the human"),
            ("x=1 ai-cost raise-cap GH-1 40", "Only the human"),
            ("env FOO=1 ai-cost raise-cap GH-1 40", "Only the human"),
            ("uv run --project .claude/skills ai-cost raise-cap GH-1 40", "Only the human"),
            (".claude/skills/ai-test-cost/bin/ai-cost raise-cap GH-1 40", "Only the human"),
            ("bash -c 'ai-cost raise-cap GH-1 40'", "Only the human"),
            ("sh -c \"cd /tmp; ai-cost 'raise-cap' GH-1 40\"", "Only the human"),
            ("env FOO=1 bash -c 'ai-cost raise-cap GH-1 40'", "Only the human"),
            ("nohup sh -c 'ai-cost raise-cap GH-1 40'", "Only the human"),
            ("ai-cost run --ticket GH-1 --estimate-usd 1 -- bash -c 'ai-cost raise-cap GH-1 40'", "Only the human"),
            ("ai-cost run --ticket GH-1 --estimate-usd 1 -- ai-cost raise-cap GH-1 40", "Only the human"),
            ('git commit -m "only the human runs ai-cost raise-cap"', None),
            ("grep -n raise-cap SKILL.md", None),
            ("echo 'Only the human runs `ai-cost raise-cap`'", None),
            ("python3 - <<'PY'\ntext = 'run pytest -m llm or ai-cost raise-cap'\nPY", None),
            ("cat > notes.md <<EOF\npytest -m llm\nEOF\ngit add notes.md", None),
            ("bash <<'EOF'\ncd app\npytest -m llm\nEOF", "calls a paid AI"),
            ("grep -c \"ai-cost run\" SKILL.md && grep -n 'pytest -m llm' Makefile", None),
            ('git commit -m "run pytest -m llm through the guard"', None),
            ("bash -c 'cd app && pytest -m llm'", "calls a paid AI"),
            ('pytest -m "llm"', "calls a paid AI"),
            ("pytest -m 'not slow and llm'", "calls a paid AI"),
            ("pytest -m 'not llm'", None),
            ("PYTEST_ADDOPTS='-m llm' pytest tests", "calls a paid AI"),
            ("env PYTEST_ADDOPTS='--llm' uv run pytest", "calls a paid AI"),
            ("export PYTEST_ADDOPTS='-m llm'; pytest", "calls a paid AI"),
            ("pytest \\\n  -m llm tests", "calls a paid AI"),
            ("uv run pytest --markexpr=llm", "calls a paid AI"),
            ("python -m pytest -qm llm", "calls a paid AI"),
            ("pytest tests -q", None),
            ("git status", None),
            ("cd front && npm run judge", "front-end AI judge"),
            ("ai-cost run --ticket GH-1 --estimate-usd 1 -- npm run judge", None),
            (
                "AI_COST_STATE_DIR=/tmp/x ai-cost run --ticket GH-1 --estimate-usd 1 -- pytest -m llm",
                "AI_COST_STATE_DIR",
            ),
            ("export AI_COST_DEFAULT_CAP_USD=1000", "AI_COST_DEFAULT_CAP_USD"),
            ("export AI_COST_USAGE_SOURCE", "AI_COST_USAGE_SOURCE"),
            ("env AI_COST_API_KEY_ID=apikey_01 ai-cost status GH-1", "AI_COST_API_KEY_ID"),
            ("declare -x AI_COST_KILL_RATIO=1", "AI_COST_KILL_RATIO"),
            ("bash -c 'AI_COST_KILL_RATIO=1 ai-cost status GH-1'", "AI_COST_KILL_RATIO"),
            ("AI_COST_CALLER_CWD=/tmp ai-cost status GH-1", None),
            ("echo $AI_COST_RUN_ID", None),
        ],
    )
    def test_each_command_gets_its_decision(
        self,
        builder: LedgerServiceBuilder,
        settings: GuardSettings,
        logger: logging.Logger,
        command: str,
        refused: Optional[str],
    ) -> None:
        ledgers = builder.build(EstimateUsageMeter(logger))
        blocked = ledgers.new_run("GH-2", "x", "x", Decimal("0"), CostSource.ESTIMATE)
        ledgers.record("GH-2", blocked, "killed at $18.20")
        gate = CommandGate(
            PaidCommandCatalog.load(settings.paid_commands_file),
            ledgers,
            ShellCommandSplitter(logger),
            PytestInvocation(logger),
            logger,
        )
        refusal = gate.refusal(command)
        if refused is None:
            assert refusal is None
        else:
            assert refusal is not None
            assert refused in refusal

    def test_an_unreadable_ledger_refuses_the_run(
        self, builder: LedgerServiceBuilder, settings: GuardSettings, logger: logging.Logger
    ) -> None:
        settings.state_dir.mkdir(parents=True)
        (settings.state_dir / "GH-3.json").write_text("[]", encoding="utf-8")
        gate = CommandGate(
            PaidCommandCatalog.load(settings.paid_commands_file),
            builder.build(EstimateUsageMeter(logger)),
            ShellCommandSplitter(logger),
            PytestInvocation(logger),
            logger,
        )
        assert "cannot be read" in str(gate.refusal("ai-cost run --ticket GH-3 --estimate-usd 1 -- pytest -m llm"))
