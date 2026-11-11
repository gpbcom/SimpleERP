from __future__ import annotations

from typing import ClassVar, Dict

import pytest
from pydantic import JsonValue, ValidationError

from pr_watch.models.checks.exceptions import (
    SEWorkflowRunInvalidConclusion,
    SEWorkflowRunInvalidId,
    SEWorkflowRunInvalidLink,
    SEWorkflowRunInvalidSuiteId,
    SEWorkflowRunInvalidWorkflow,
)
from pr_watch.models.checks.workflow_run import WorkflowRun


class TestWorkflowRun:
    REQUIRED: ClassVar[Dict[str, JsonValue]] = {
        "id": 601,
        "workflow": "stage.yml",
        "link": "https://github.com/gpbcom/simple-erp/actions/runs/601",
    }
    FULL: ClassVar[Dict[str, JsonValue]] = {
        "id": 601,
        "workflow": "stage.yml",
        "conclusion": "failure",
        "link": "https://github.com/gpbcom/simple-erp/actions/runs/601",
        "suite_id": 77,
    }

    def test_defaults(self) -> None:
        model = WorkflowRun(**self.REQUIRED)
        assert model.conclusion == WorkflowRun.model_fields["conclusion"].get_default(call_default_factory=True)
        assert model.suite_id == WorkflowRun.model_fields["suite_id"].get_default(call_default_factory=True)

    def test_full_valid_construction(self) -> None:
        model = WorkflowRun(**self.FULL)
        assert model.workflow == "stage.yml"

    @pytest.mark.parametrize("name", ["conclusion", "suite_id"])
    def test_none_becomes_the_default(self, name: str) -> None:
        model = WorkflowRun(**{**self.FULL, name: None})
        assert getattr(model, name) == WorkflowRun.model_fields[name].get_default(call_default_factory=True)

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("id", 0, SEWorkflowRunInvalidId),
            ("id", None, SEWorkflowRunInvalidId),
            ("workflow", "", SEWorkflowRunInvalidWorkflow),
            ("workflow", None, SEWorkflowRunInvalidWorkflow),
            ("conclusion", "broken", SEWorkflowRunInvalidConclusion),
            ("conclusion", 2, SEWorkflowRunInvalidConclusion),
            ("link", "runs/601", SEWorkflowRunInvalidLink),
            ("link", None, SEWorkflowRunInvalidLink),
            ("suite_id", -3, SEWorkflowRunInvalidSuiteId),
            ("suite_id", "x", SEWorkflowRunInvalidSuiteId),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            WorkflowRun(**{**self.FULL, name: value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            WorkflowRun(**self.FULL, surprise=1)

    def test_round_trip(self) -> None:
        model = WorkflowRun(**self.FULL)
        assert WorkflowRun.model_validate_json(model.model_dump_json()) == model
