from __future__ import annotations

import logging
import sys
from pathlib import Path

from ticket_docs.models.evidence.command_outcome import CommandOutcome
from ticket_docs.storage.processes.command_runner import CommandRunner


class TestCommandRunner:
    def test_the_output_of_both_streams_and_the_exit_code_are_kept(
        self, tmp_path: Path, logger: logging.Logger
    ) -> None:
        script = "import sys; print('out'); print('err', file=sys.stderr); sys.exit(3)"
        outcome = CommandRunner(logger).run([sys.executable, "-c", script], tmp_path)
        assert outcome.exit_code == 3
        assert "out" in outcome.output
        assert "err" in outcome.output

    def test_the_command_runs_in_the_given_folder(self, tmp_path: Path, logger: logging.Logger) -> None:
        outcome = CommandRunner(logger).run([sys.executable, "-c", "import os; print(os.getcwd())"], tmp_path)
        assert outcome == CommandOutcome(exit_code=0, output=f"{tmp_path}\n")

    def test_a_command_can_read_its_standard_input(self, tmp_path: Path, logger: logging.Logger) -> None:
        script = "import sys; print(sys.stdin.read().upper())"
        assert CommandRunner(logger).run([sys.executable, "-c", script], tmp_path, "hello").output == "HELLO\n"

    def test_a_missing_program_exits_127(self, tmp_path: Path, logger: logging.Logger) -> None:
        outcome = CommandRunner(logger).run(["no-such-program-anywhere"], tmp_path)
        assert outcome.exit_code == 127
        assert "no-such-program-anywhere" in outcome.output
