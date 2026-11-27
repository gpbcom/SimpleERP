from __future__ import annotations

# Standard library imports
import subprocess
import sys
from typing import ClassVar, Dict, List, Set, cast

# Third-party imports
import pytest
from pydantic import JsonValue

# First-party imports
from tests.ci.workflows.helpers import ROOT, SCRIPTS, jobs, steps, triggers, with_of, workflow

NAME = "ci.yml"


class TestCiWorkflow:
    OUTPUT_KEYS: ClassVar[Set[str]] = {
        "services",
        "packages",
        "typescript",
        "repository",
        "terraform",
        "helm",
        "images",
    }
    JOBS: ClassVar[Set[str]] = {"changes", "python", "typescript", "terraform", "helm", "images", "result"}
    PUSH_BRANCHES: ClassVar[List[str]] = ["master", "develop", "release/**", "hotfix/**"]
    PULL_REQUEST_BASES: ClassVar[List[str]] = ["develop", "master", "release/**"]
    CHECK_JOBS: ClassVar[Set[str]] = {"changes", "python", "typescript", "terraform"}
    IMAGES_PERMISSIONS: ClassVar[Dict[str, str]] = {"contents": "read", "packages": "write", "id-token": "write"}
    IMAGES_CONDITIONS: ClassVar[List[str]] = [
        "!cancelled()",
        "!contains(needs.*.result, 'failure')",
        "needs.changes.outputs.images != '[]'",
    ]
    PUBLISH_CONDITIONS: ClassVar[List[str]] = ["github.event_name == 'push'", "refs/heads/develop", "refs/heads/master"]

    def test_pushes_run_only_on_the_gitflow_branches(self) -> None:
        assert triggers(NAME)["push"]["branches"] == self.PUSH_BRANCHES

    def test_pull_requests_run_against_the_gitflow_bases(self) -> None:
        assert triggers(NAME)["pull_request"]["branches"] == self.PULL_REQUEST_BASES

    def test_a_newer_pull_request_run_cancels_the_older_one(self) -> None:
        concurrency = cast(Dict[str, JsonValue], workflow(NAME)["concurrency"])
        assert "github.ref" in str(concurrency["group"])
        assert "github.event_name == 'pull_request'" in str(concurrency["cancel-in-progress"])

    def test_it_has_exactly_the_expected_jobs(self) -> None:
        assert set(jobs(NAME)) == self.JOBS

    def test_the_changes_job_compares_with_the_full_history(self) -> None:
        checkout = steps(NAME, "changes")[0]
        assert str(checkout["uses"]).startswith("actions/checkout@")
        assert with_of(checkout)["fetch-depth"] == 0

    def test_the_detect_step_runs_the_detector_and_writes_the_outputs(self) -> None:
        [detect] = [step for step in steps(NAME, "changes") if step.get("id") == "detect"]
        run = str(detect["run"])
        assert ".github/scripts/detect_changes.py --all" in run
        assert "| python3 .github/scripts/detect_changes.py" in run
        assert "GITHUB_OUTPUT" in run

    def test_the_changes_job_outputs_are_the_keys_the_detector_prints(self) -> None:
        result = subprocess.run(
            [sys.executable, str(SCRIPTS / "detect_changes.py"), "--all", "--root", str(ROOT)],
            capture_output=True,
            text=True,
            check=True,
        )
        printed = {line.split("=", 1)[0] for line in result.stdout.splitlines()}
        outputs = cast(Dict[str, str], jobs(NAME)["changes"]["outputs"])
        assert set(outputs) == printed == self.OUTPUT_KEYS
        for key, value in outputs.items():
            assert value == "${{ steps.detect.outputs." + key + " }}"

    @pytest.mark.parametrize(
        ("job", "called", "conditions"),
        [
            (
                "python",
                "python.yml",
                [
                    "needs.changes.outputs.services",
                    "needs.changes.outputs.packages",
                    "needs.changes.outputs.repository",
                ],
            ),
            ("typescript", "typescript.yml", ["needs.changes.outputs.typescript"]),
            ("terraform", "terraform.yml", ["needs.changes.outputs.terraform"]),
            ("helm", "helm.yml", ["needs.changes.outputs.helm == 'true'"]),
        ],
    )
    def test_each_language_job_calls_its_workflow_under_its_condition(
        self, job: str, called: str, conditions: List[str]
    ) -> None:
        assert jobs(NAME)[job]["needs"] == "changes"
        assert jobs(NAME)[job]["uses"] == f"./.github/workflows/{called}"
        for condition in conditions:
            assert condition in str(jobs(NAME)[job]["if"])

    def test_the_python_job_receives_the_services_the_packages_and_the_repository_flag(self) -> None:
        inputs = cast(Dict[str, str], jobs(NAME)["python"]["with"])
        assert inputs["services"] == "${{ needs.changes.outputs.services }}"
        assert inputs["packages"] == "${{ needs.changes.outputs.packages }}"
        assert "needs.changes.outputs.repository == 'true'" in inputs["repository"]

    def test_the_terraform_job_receives_the_folders_to_check(self) -> None:
        assert jobs(NAME)["terraform"]["with"] == {"folders": "${{ needs.changes.outputs.terraform }}"}

    def test_the_images_job_waits_for_every_check_and_runs_only_when_none_failed(self) -> None:
        images = jobs(NAME)["images"]
        assert images["uses"] == "./.github/workflows/images.yml"
        assert set(cast(List[str], images["needs"])) == self.CHECK_JOBS
        condition = str(images["if"]).replace(" ", "")
        for expected in self.IMAGES_CONDITIONS:
            assert expected.replace(" ", "") in condition

    def test_images_are_published_from_develop_and_master_pushes_only(self) -> None:
        publish = str(cast(Dict[str, str], jobs(NAME)["images"]["with"])["publish"])
        for expected in self.PUBLISH_CONDITIONS:
            assert expected in publish

    def test_the_images_job_may_write_packages_and_sign(self) -> None:
        assert jobs(NAME)["images"]["permissions"] == self.IMAGES_PERMISSIONS

    def test_the_result_job_is_the_single_gate_of_the_run(self) -> None:
        result = jobs(NAME)["result"]
        assert set(cast(List[str], result["needs"])) == self.JOBS - {"result"}
        assert result["if"] == "always()"
        run = " ".join(str(step.get("run", "")) for step in steps(NAME, "result"))
        assert "failure|cancelled" in run
        assert "exit 1" in run
