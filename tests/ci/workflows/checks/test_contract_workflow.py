from __future__ import annotations

# Standard library imports
from typing import ClassVar, Dict, List, cast

# Third-party imports
from pydantic import JsonValue

# First-party imports
from tests.ci.workflows.helpers import jobs, step_using, steps, with_of

NAME = "python.yml"


class TestContractWorkflow:
    COMMAND: ClassVar[str] = 'bash .github/scripts/check_contract.sh "$FOLDER" "$CONTRACT_BASE"'

    def names(self, job: str) -> List[str]:
        return [str(step.get("name", "")) for step in steps(NAME, job)]

    def contract_step(self) -> Dict[str, JsonValue]:
        found = [step for step in steps(NAME, "services") if step.get("name") == "Contract check"]
        assert len(found) == 1, "The services job needs one step named Contract check."
        return cast(Dict[str, JsonValue], found[0])

    def test_the_services_job_checks_out_the_whole_history_to_reach_the_base_commit(self) -> None:
        assert with_of(step_using(NAME, "services", "actions/checkout"))["fetch-depth"] == 0

    def test_the_repository_job_stays_shallow(self) -> None:
        assert "fetch-depth" not in with_of(step_using(NAME, "repository", "actions/checkout"))
        assert "repository" in jobs(NAME)

    def test_the_contract_check_comes_after_the_project_check_and_before_the_reports_upload(self) -> None:
        ids = [step.get("id") for step in steps(NAME, "services")]
        position = self.names("services").index("Contract check")
        assert position > ids.index("check")
        uploads = [str(step.get("uses", "")).startswith("actions/upload-artifact@") for step in steps(NAME, "services")]
        assert position < uploads.index(True)

    def test_the_contract_check_runs_the_script_with_the_folder_and_the_base(self) -> None:
        assert self.contract_step()["run"] == self.COMMAND

    def test_the_base_is_set_in_env_from_the_pull_request_base_or_the_push_before(self) -> None:
        env = cast(Dict[str, str], self.contract_step()["env"])
        assert "github.event.pull_request.base.sha" in env["CONTRACT_BASE"]
        assert "github.event.before" in env["CONTRACT_BASE"]

    def test_no_event_expression_is_written_inside_the_run(self) -> None:
        assert "${{" not in str(self.contract_step()["run"])
