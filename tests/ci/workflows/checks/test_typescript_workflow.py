from __future__ import annotations

# Standard library imports
from typing import ClassVar, Dict, List, cast

# Third-party imports
import pytest
from pydantic import JsonValue

# First-party imports
from tests.ci.workflows.helpers import jobs, runs, step_using, steps, triggers, with_of

NAME = "typescript.yml"


class TestTypescriptWorkflow:
    SCRIPTS: ClassVar[List[str]] = ["lint", "typecheck", "test"]

    def test_it_is_a_reusable_workflow_taking_the_projects(self) -> None:
        assert list(triggers(NAME)) == ["workflow_call"]
        assert list(cast(Dict[str, JsonValue], triggers(NAME)["workflow_call"]["inputs"])) == ["projects"]

    def test_each_project_is_its_own_matrix_entry(self) -> None:
        matrix = cast(Dict[str, Dict[str, str]], jobs(NAME)["check"]["strategy"])["matrix"]
        assert matrix["project"] == "${{ fromJSON(inputs.projects) }}"

    def test_node_22_and_pnpm_install_the_frozen_lock_file(self) -> None:
        step_using(NAME, "check", "pnpm/action-setup")
        node = with_of(step_using(NAME, "check", "actions/setup-node"))
        assert node["node-version"] == "22"
        assert node["cache"] == "pnpm"
        assert "pnpm install --frozen-lockfile" in runs(NAME, "check")

    @pytest.mark.parametrize("script", SCRIPTS)
    def test_each_script_runs_only_when_the_project_has_it(self, script: str) -> None:
        assert f'pnpm --filter "./$PROJECT" run --if-present {script}' in runs(NAME, "check")

    def test_the_test_log_is_kept_even_when_it_fails(self) -> None:
        assert 'tee "reports/$name.log"' in runs(NAME, "check")
        uploads = [step for step in steps(NAME, "check") if "upload-artifact" in str(step.get("uses", ""))]
        assert len(uploads) == 1
        assert uploads[0]["if"] == "always()"
        assert str(with_of(uploads[0])["name"]).startswith("test-report-ts-")
