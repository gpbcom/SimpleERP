from __future__ import annotations

import logging
import os
import re
import select
import threading
import time
from pathlib import Path
from typing import List, Tuple

import pytest

from harness_core.terminal.human_confirmation import HumanConfirmation


class TestHumanConfirmation:
    @pytest.fixture
    def logger(self) -> logging.Logger:
        return logging.getLogger("harness_core.tests")

    def confirm_into(self, confirmation: HumanConfirmation, result: List[bool]) -> None:
        result.append(confirmation.confirm("Raise the cap of GH-1?"))

    def answer_on_a_terminal(self, logger: logging.Logger, typed: str) -> Tuple[bool, str]:
        master, slave = os.openpty()
        confirmation = HumanConfirmation(Path(os.ttyname(slave)), logger)
        result: List[bool] = []
        worker = threading.Thread(target=self.confirm_into, args=(confirmation, result), daemon=True)
        worker.start()
        shown = b""
        deadline = time.monotonic() + 10
        while b"to confirm: " not in shown and time.monotonic() < deadline and worker.is_alive():
            if select.select([master], [], [], 0.1)[0]:
                shown += os.read(master, 1024)
        code = re.search(rb"Type ([A-Z0-9]{6}) to confirm", shown)
        if code is not None:
            os.write(master, (typed or code.group(1).decode()).encode() + b"\n")
        worker.join(timeout=10)
        os.close(master)
        os.close(slave)
        assert code is not None, f"no code was shown on the terminal: {shown!r}"
        return result[0], shown.decode()

    def test_the_code_shown_on_the_terminal_and_typed_back_confirms(self, logger: logging.Logger) -> None:
        confirmed, shown = self.answer_on_a_terminal(logger, "")
        assert confirmed is True
        assert "Raise the cap of GH-1?" in shown

    def test_another_answer_does_not_confirm(self, logger: logging.Logger) -> None:
        assert self.answer_on_a_terminal(logger, "GH-1")[0] is False

    def test_the_code_changes_every_time(self, logger: logging.Logger) -> None:
        confirmation = HumanConfirmation(logger=logger)
        codes = {confirmation.code() for _ in range(20)}
        assert len(codes) > 1
        assert all(re.fullmatch(r"[A-Z0-9]{6}", code) for code in codes)

    def test_without_a_terminal_nothing_is_confirmed(self, logger: logging.Logger, tmp_path: Path) -> None:
        assert HumanConfirmation(tmp_path / "no-tty", logger).confirm("Raise?") is False

    def test_the_default_terminal_is_the_controlling_one(self, logger: logging.Logger) -> None:
        assert HumanConfirmation(logger=logger).tty == Path("/dev/tty")
