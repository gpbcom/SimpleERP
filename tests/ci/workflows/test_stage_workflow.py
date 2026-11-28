from __future__ import annotations

# Standard library imports
import re
from typing import ClassVar, Dict, List, cast

# Third-party imports
from pydantic import JsonValue

# First-party imports
from tests.ci.workflows.helpers import jobs, runs, steps, triggers

NAME = "stage.yml"
STAGE = "${{ inputs.stage || (github.ref_name == 'develop' && 'dev' || 'qa') }}"


class TestStageWorkflow:
    PUSH_BRANCHES: ClassVar[List[str]] = ["develop", "release/**", "hotfix/**"]
    PERMISSIONS: ClassVar[Dict[str, str]] = {"contents": "read", "packages": "read", "deployments": "write"}

    def job(self) -> Dict[str, JsonValue]:
        return jobs(NAME)["stage"]

    def step(self, name: str) -> Dict[str, JsonValue]:
        [found] = [step for step in steps(NAME, "stage") if step.get("name") == name]
        return found

    def test_a_push_to_develop_runs_dev_and_a_release_or_hotfix_runs_qa(self) -> None:
        assert triggers(NAME)["push"]["branches"] == self.PUSH_BRANCHES
        assert cast(Dict[str, str], self.job()["env"])["STAGE"] == STAGE

    def test_a_stage_can_be_started_by_hand_on_any_commit(self) -> None:
        inputs = cast(Dict[str, Dict[str, JsonValue]], triggers(NAME)["workflow_dispatch"]["inputs"])
        assert inputs["stage"]["options"] == ["dev", "qa"]
        assert inputs["ref"]["required"] is True

    def test_each_run_records_a_deployment_on_its_environment(self) -> None:
        environment = cast(Dict[str, str], self.job()["environment"])
        assert environment["name"] == STAGE
        assert self.job()["permissions"] == self.PERMISSIONS

    def test_the_ref_is_resolved_to_a_full_commit_before_the_checkout(self) -> None:
        resolve, checkout = steps(NAME, "stage")[:2]
        assert 'gh api "repos/$REPO/commits/$REF" --jq .sha' in str(resolve["run"])
        assert str(checkout["uses"]).startswith("actions/checkout@")
        assert cast(Dict[str, str], checkout["with"])["ref"] == "${{ steps.ref.outputs.sha }}"

    def test_without_compose_e2e_the_stage_says_there_are_no_images_yet_and_succeeds(self) -> None:
        run = str(self.step("Record what runs")["run"])
        assert "if [ -f compose.e2e.yaml ]" in run
        assert "No images yet" in run
        for name in ("Start the commit's images", "Smoke test", "Bruno collection (TEST-1)", "Playwright (TEST-6)"):
            assert "steps.compose.outputs.present == 'true'" in str(self.step(name)["if"])

    def test_the_images_start_from_the_commit_and_are_checked_healthy(self) -> None:
        start = str(self.step("Start the commit's images")["run"])
        assert "up --detach --wait" in start
        smoke = str(self.step("Smoke test")["run"])
        assert '$2 != "running"' in smoke
        assert "healthy" in smoke

    def test_dev_runs_the_smoke_playwright_tests_and_qa_the_whole_suite(self) -> None:
        run = str(self.step("Playwright (TEST-6)")["run"])
        assert "playwright.sh --grep @smoke" in run
        assert 'if [ "$STAGE" = dev ]' in run

    def test_the_bruno_collections_run_on_dev_and_on_qa_once_the_images_and_a_collection_exist(self) -> None:
        condition = str(self.step("Bruno collection (TEST-1)")["if"])
        assert "steps.compose.outputs.present == 'true'" in condition
        assert "hashFiles('bruno/**') != ''" in condition
        assert "STAGE" not in condition

    def test_each_bruno_collection_runs_headless_with_a_pinned_cli_and_reports_without_secrets(self) -> None:
        run = str(self.step("Bruno collection (TEST-1)")["run"])
        assert "bruno/*/" in run
        assert re.search(r"@usebruno/cli@\d+\.\d+\.\d+(?![\d.])", run)
        for part in (
            " run ",
            "--env stage",
            '--reporter-junit "$REPORTS/bruno-$name.xml"',
            '--reporter-json "$REPORTS/bruno-$name.json"',
            "--reporter-skip-all-headers",
            "--reporter-skip-body",
        ):
            assert part in run

    def test_a_failing_bruno_collection_fails_the_job_after_every_collection_ran(self) -> None:
        run = str(self.step("Bruno collection (TEST-1)")["run"])
        assert 'exit "$status"' in run
        assert run.index("done") < run.index('exit "$status"')

    def test_node_22_is_set_up_before_the_bruno_step_when_compose_and_a_collection_exist(self) -> None:
        all_steps = steps(NAME, "stage")
        bruno = next(i for i, step in enumerate(all_steps) if step.get("name") == "Bruno collection (TEST-1)")
        setups = [
            step
            for step in all_steps[:bruno]
            if str(step.get("uses", "")).startswith("actions/setup-node@")
            and cast(Dict[str, JsonValue], step.get("with", {})).get("node-version") == "22"
        ]
        assert len(setups) == 1
        condition = str(setups[0]["if"])
        assert "steps.compose.outputs.present == 'true'" in condition
        assert "hashFiles('bruno/**') != ''" in condition

    def test_qa_checks_that_the_lock_file_resolves(self) -> None:
        step = self.step("Dependency resolution (DEP-1)")
        assert step["if"] == "env.STAGE == 'qa'"
        assert "uv lock --check" in str(step["run"])

    def test_every_report_is_kept_even_when_the_stage_fails(self) -> None:
        upload = self.step("Keep the reports (TEST-9)")
        assert upload["if"] == "always()"
        assert cast(Dict[str, str], upload["with"])["path"] == "stage-reports/"
        assert "down --volumes" in str(self.step("Service logs, then stop the stack")["run"])

    def test_no_script_reads_the_inputs_directly(self) -> None:
        assert "${{ inputs" not in runs(NAME, "stage")
