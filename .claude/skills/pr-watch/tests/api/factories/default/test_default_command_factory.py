from __future__ import annotations

from typing import List

import pytest

from pr_watch.api.cli.command import Command
from pr_watch.api.cli.command_line import CommandLine
from pr_watch.api.cli.commands.inbox_command import InboxCommand
from pr_watch.api.cli.commands.report_command import ReportCommand
from pr_watch.api.cli.commands.session_command import SessionCommand
from pr_watch.api.cli.commands.setup_command import SetupCommand
from pr_watch.api.cli.commands.watch_command import WatchCommand
from pr_watch.api.factories.default.default_command_factory import DefaultCommandFactory
from pr_watch.models.configuration.watch_catalog import WatchCatalog
from pr_watch.models.configuration.watch_settings import WatchSettings
from pr_watch.service.factories.default.default_service_factory import DefaultServiceFactory


class TestDefaultCommandFactory:
    @pytest.mark.parametrize(
        ("arguments", "kind"),
        [
            (["once"], WatchCommand),
            (["register", "GH-1"], SessionCommand),
            (["backfill"], SessionCommand),
            (["show", "GH-1"], InboxCommand),
            (["ack", "GH-1"], InboxCommand),
            (["log", "GH-1", "note", "x"], InboxCommand),
            (["status"], ReportCommand),
            (["render"], ReportCommand),
            (["install-units"], SetupCommand),
        ],
    )
    def test_each_command_gets_its_class(
        self, settings: WatchSettings, catalog: WatchCatalog, arguments: List[str], kind: type[Command]
    ) -> None:
        factory = DefaultCommandFactory(DefaultServiceFactory(settings, catalog))
        command = factory.command(CommandLine().parse(arguments))
        assert type(command) is kind
        assert command.exit_code == 0
