from __future__ import annotations

import asyncio
from pathlib import Path
from typing import Iterator

import pytest

from harness_core.testing.github_fake import GithubFake
from pr_watch.models.configuration.commands_config import CommandsConfig
from pr_watch.models.configuration.watch_catalog import WatchCatalog
from pr_watch.models.configuration.watch_settings import WatchSettings
from tests.stand_ins.helpers import recording_body, write_program


@pytest.fixture
def catalog() -> WatchCatalog:
    return WatchCatalog.load(WatchSettings().catalog_file)


@pytest.fixture
def fake() -> GithubFake:
    return GithubFake()


@pytest.fixture
def runner() -> Iterator[asyncio.Runner]:
    with asyncio.Runner() as runner:
        yield runner


@pytest.fixture
def calls_log(tmp_path: Path) -> Path:
    return tmp_path / "calls.log"


@pytest.fixture
def commands(tmp_path: Path, calls_log: Path) -> CommandsConfig:
    """Desktop programs that record their calls instead of opening anything."""
    folder = tmp_path / "bin"
    return CommandsConfig(
        claude=str(write_program(folder, "claude", recording_body(calls_log, stdout="[]"))),
        vscode=str(write_program(folder, "code", recording_body(calls_log))),
        opener=str(write_program(folder, "xdg-open", recording_body(calls_log))),
        notifier=str(write_program(folder, "notify-send", recording_body(calls_log))),
        terminal=str(write_program(folder, "gnome-terminal", recording_body(calls_log))),
    )


@pytest.fixture
def faked_catalog(catalog: WatchCatalog, commands: CommandsConfig) -> WatchCatalog:
    return catalog.model_copy(update={"commands": commands})


@pytest.fixture
def settings(tmp_path: Path) -> WatchSettings:
    return WatchSettings(
        state_dir=tmp_path / "state",
        cost_state_dir=tmp_path / "costs",
        claude_home=tmp_path / "claude",
        caller_cwd=tmp_path,
    )
