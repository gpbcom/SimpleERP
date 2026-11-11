from __future__ import annotations

from pathlib import Path

from pr_watch.storage.desktop.command_runner import CommandRunner
from tests.stand_ins.helpers import recorded_calls, recording_body, write_program


class TestCommandRunner:
    def test_a_program_that_succeeds_has_no_failure(self, tmp_path: Path) -> None:
        program = write_program(tmp_path, "notify", recording_body(tmp_path / "calls.log"))
        assert CommandRunner().failure_of([str(program), "Title", "two words"]) is None
        assert recorded_calls(tmp_path / "calls.log") == [["notify", "Title", "two words"]]

    def test_a_failure_comes_back_as_a_value(self, tmp_path: Path) -> None:
        program = write_program(tmp_path, "opener", "echo 'no display' >&2; exit 3")
        failure = CommandRunner().failure_of([str(program)])
        assert failure is not None
        assert "exited 3" in failure
        assert "no display" in failure
        missing = CommandRunner().failure_of([str(tmp_path / "missing")])
        assert missing is not None
        assert missing.endswith("FileNotFoundError")

    def test_the_output_is_given_only_on_success(self, tmp_path: Path) -> None:
        good = write_program(tmp_path, "good", "printf '[]'")
        bad = write_program(tmp_path, "bad", "printf '[]'; exit 1")
        assert CommandRunner().output_of([str(good)]) == "[]"
        assert CommandRunner().output_of([str(bad)]) is None
        assert CommandRunner().output_of([str(tmp_path / "missing")]) is None

    def test_a_program_is_available_when_it_can_be_found(self, tmp_path: Path) -> None:
        assert CommandRunner().available(str(write_program(tmp_path, "code", "exit 0")))
        assert not CommandRunner().available(str(tmp_path / "missing"))
