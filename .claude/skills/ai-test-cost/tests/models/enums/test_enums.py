from __future__ import annotations

from enum import StrEnum
from typing import Set

import pytest

from ai_cost.models.enums import AiCostCommand, CostSource, RunStatus, UsageSource


class TestEnums:
    @pytest.mark.parametrize(
        ("enum", "values"),
        [
            (RunStatus, {"running", "done", "failed", "killed_at_cap", "refused"}),
            (CostSource, {"usage_report", "estimate", "charged"}),
            (UsageSource, {"anthropic", "estimate"}),
            (AiCostCommand, {"run", "status", "remaining", "charge", "raise-cap", "gate"}),
        ],
    )
    def test_each_enum_lists_its_values(self, enum: type[StrEnum], values: Set[str]) -> None:
        assert {member.value for member in enum} == values
