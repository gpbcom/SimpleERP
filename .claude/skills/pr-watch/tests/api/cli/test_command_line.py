from __future__ import annotations

import pytest

from pr_watch.api.cli.command_line import CommandLine


class TestCommandLine:
    def test_register_collects_its_links(self) -> None:
        options = CommandLine().parse(["register", "GH-12", "--link", "a", "--link", "b", "--no-session"])
        assert (options.command, options.key, options.link, options.no_session) == (
            "register",
            "GH-12",
            ["a", "b"],
            True,
        )

    def test_ack_takes_any_number_of_events(self) -> None:
        assert CommandLine().parse(["ack", "GH-12"]).event_ids == []
        assert CommandLine().parse(["ack", "GH-12", "e1", "e2"]).event_ids == ["e1", "e2"]

    @pytest.mark.parametrize("kind", ["rebased", "fixed", "waiting_push", "pushed", "qa_started", "note"])
    def test_log_takes_the_operations_of_a_session(self, kind: str) -> None:
        assert CommandLine().parse(["log", "GH-12", kind, "done", "--pr", "gpbcom/simple-erp#7"]).pr == (
            "gpbcom/simple-erp#7"
        )

    def test_a_command_is_required(self) -> None:
        with pytest.raises(SystemExit):
            CommandLine().parse([])
