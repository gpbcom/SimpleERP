from __future__ import annotations

from typing import ClassVar, Dict

import pytest
from pydantic import JsonValue, ValidationError

from pr_watch.models.checks.exceptions import (
    SEStageDeploymentInvalidDeploymentId,
    SEStageDeploymentInvalidEnvironment,
    SEStageDeploymentInvalidLink,
    SEStageDeploymentInvalidState,
)
from pr_watch.models.checks.stage_deployment import StageDeployment


class TestStageDeployment:
    REQUIRED: ClassVar[Dict[str, JsonValue]] = {"environment": "dev", "deployment_id": 701}
    FULL: ClassVar[Dict[str, JsonValue]] = {
        "environment": "dev",
        "deployment_id": 701,
        "state": "failure",
        "link": "https://github.com/gpbcom/simple-erp/actions/runs/601",
    }

    def test_defaults(self) -> None:
        model = StageDeployment(**self.REQUIRED)
        assert model.state == StageDeployment.model_fields["state"].get_default(call_default_factory=True)
        assert model.link == StageDeployment.model_fields["link"].get_default(call_default_factory=True)

    def test_full_valid_construction(self) -> None:
        model = StageDeployment(**self.FULL)
        assert model.state == "failure"

    @pytest.mark.parametrize("name", ["state", "link"])
    def test_none_becomes_the_default(self, name: str) -> None:
        model = StageDeployment(**{**self.FULL, name: None})
        assert getattr(model, name) == StageDeployment.model_fields[name].get_default(call_default_factory=True)

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("environment", "", SEStageDeploymentInvalidEnvironment),
            ("environment", None, SEStageDeploymentInvalidEnvironment),
            ("deployment_id", 0, SEStageDeploymentInvalidDeploymentId),
            ("deployment_id", None, SEStageDeploymentInvalidDeploymentId),
            ("state", "failed", SEStageDeploymentInvalidState),
            ("state", 1, SEStageDeploymentInvalidState),
            ("link", "x", SEStageDeploymentInvalidLink),
            ("link", 1, SEStageDeploymentInvalidLink),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            StageDeployment(**{**self.FULL, name: value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            StageDeployment(**self.FULL, surprise=1)

    def test_round_trip(self) -> None:
        model = StageDeployment(**self.FULL)
        assert StageDeployment.model_validate_json(model.model_dump_json()) == model
