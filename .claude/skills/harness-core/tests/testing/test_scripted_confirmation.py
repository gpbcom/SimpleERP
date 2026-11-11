from __future__ import annotations

import logging

import pytest

from harness_core.terminal.human_confirmation import HumanConfirmation
from harness_core.testing.scripted_confirmation import ScriptedConfirmation


class TestScriptedConfirmation:
    @pytest.mark.parametrize("confirmed", [True, False])
    def test_the_answer_follows_the_script(self, confirmed: bool) -> None:
        human = ScriptedConfirmation(confirmed, logging.getLogger("harness_core.tests"))
        assert isinstance(human, HumanConfirmation)
        assert human.confirm("Raise the cap of GH-1?") is confirmed
        assert human.questions == ["Raise the cap of GH-1?"]
