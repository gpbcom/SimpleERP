from __future__ import annotations

from enum import StrEnum
from typing import List

import pytest

from ticket_docs.models.enums import Expectation, RunConclusion, RunKind, RunPlace, TicketDocsCommand


class TestEnums:
    @pytest.mark.parametrize(
        ("enum", "values"),
        [
            (RunKind, ["unit", "gui", "e2e", "check"]),
            (RunPlace, ["local", "ci", "dev", "qa"]),
            (Expectation, ["red", "green"]),
            (
                TicketDocsCommand,
                [
                    "record-run",
                    "check",
                    "report-index",
                    "history-bundle",
                    "archive",
                    "board",
                    "git-gate",
                    "time-reminder",
                    "allow-squash",
                    "file-gate",
                ],
            ),
        ],
    )
    def test_each_enum_holds_the_values_of_the_command_line(self, enum: type[StrEnum], values: List[str]) -> None:
        assert [member.value for member in enum] == values

    def test_a_conclusion_reads_every_value_github_gives(self) -> None:
        for value in ("success", "failure", "cancelled", "skipped", "timed_out", "action_required", "neutral", ""):
            assert RunConclusion(value).value == value
        assert RunConclusion("success") is RunConclusion.SUCCESS
