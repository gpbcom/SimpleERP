from __future__ import annotations

import logging
import subprocess
from decimal import Decimal
from pathlib import Path

import pytest

from ai_cost.models.enums import UsageSource
from ai_cost.models.pricing.price_table import PriceTable
from ai_cost.models.settings.caller_environment import CallerEnvironment
from ai_cost.models.settings.guard_settings import GuardSettings
from ai_cost.service.pricing.price_book import PriceBook
from tests.service.ledgers.ledger_service_builder import LedgerServiceBuilder


@pytest.fixture
def logger() -> logging.Logger:
    return logging.getLogger("ai_cost.tests")


@pytest.fixture
def repo(tmp_path: Path) -> Path:
    folder = tmp_path / "repo"
    folder.mkdir()
    subprocess.run(["git", "-C", str(folder), "init", "-q", "-b", "develop"], check=True)
    return folder


@pytest.fixture
def paid_commands_file(tmp_path: Path) -> Path:
    path = tmp_path / "paid-commands.yaml"
    path.write_text(
        "paid_commands:\n  - name: front-end AI judge\n    pattern: '\\bnpm\\s+run\\s+judge\\b'\n", encoding="utf-8"
    )
    return path


@pytest.fixture
def settings(tmp_path: Path, paid_commands_file: Path) -> GuardSettings:
    return GuardSettings(
        state_dir=tmp_path / "state",
        prices_file=Path("conf/prices.yaml"),
        paid_commands_file=paid_commands_file,
        cost_template_file=Path("templates/COST.md"),
        default_cap_usd=Decimal("20"),
        kill_ratio=Decimal("0.9"),
        poll_interval_s=1,
        settle_s=0,
        max_unmeasured=3,
        usage_source=UsageSource.ANTHROPIC,
    )


@pytest.fixture
def environment(repo: Path) -> CallerEnvironment:
    return CallerEnvironment(caller_cwd=repo, api_key_id=None)


@pytest.fixture
def prices(settings: GuardSettings, logger: logging.Logger) -> PriceBook:
    return PriceBook(PriceTable.load(settings.prices_file), logger)


@pytest.fixture
def builder(settings: GuardSettings, environment: CallerEnvironment, logger: logging.Logger) -> LedgerServiceBuilder:
    return LedgerServiceBuilder(settings, environment, logger)
