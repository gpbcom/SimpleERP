from __future__ import annotations

import pytest
from erp_metering.models.calls.budget_check import BudgetCheck
from erp_metering.models.calls.exceptions import SEBudgetCheckInvalidWithinBudget, SEInvalidBudgetCheckException
from pydantic import JsonValue, ValidationError


class TestBudgetCheck:
    def test_defaults(self) -> None:
        check = BudgetCheck.model_validate({})
        assert check.within_budget is False

    def test_full_valid_construction(self) -> None:
        assert BudgetCheck(within_budget=True).within_budget is True

    def test_none_becomes_the_default(self) -> None:
        assert BudgetCheck.model_validate({"within_budget": None}).within_budget is False

    @pytest.mark.parametrize("value", ["true", "", 1, 0, 1.5, ["x"], {"a": 1}])
    def test_rejects_bad_values(self, value: JsonValue) -> None:
        with pytest.raises(SEBudgetCheckInvalidWithinBudget):
            BudgetCheck.model_validate({"within_budget": value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            BudgetCheck.model_validate({"within_budget": True, "other": "x"})

    def test_round_trip(self) -> None:
        check = BudgetCheck(within_budget=True)
        assert BudgetCheck.model_validate(check.model_dump(mode="json")) == check
        assert BudgetCheck.model_validate_json(check.model_dump_json()) == check

    def test_the_field_exception_belongs_to_the_model_hierarchy(self) -> None:
        assert issubclass(SEBudgetCheckInvalidWithinBudget, SEInvalidBudgetCheckException)

    def test_assignment_is_refused(self) -> None:
        check = BudgetCheck(within_budget=True)
        with pytest.raises(ValidationError):
            check.within_budget = False
