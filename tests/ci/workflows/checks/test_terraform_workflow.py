from __future__ import annotations

# Standard library imports
import re
from typing import ClassVar, Dict, List, cast

# Third-party imports
import pytest
from pydantic import JsonValue

# First-party imports
from tests.ci.workflows.helpers import ROOT, jobs, runs, step_using, steps, triggers, with_of

NAME = "terraform.yml"


class TestTerraformWorkflow:
    ROOTS: ClassVar[List[str]] = ["ovhcloud", "scaleway"]
    EXACT_VERSION: ClassVar[re.Pattern[str]] = re.compile(r"^\d+\.\d+\.\d+$")
    REQUIRED: ClassVar[re.Pattern[str]] = re.compile(r'required_version\s*=\s*"=?\s*(\d+\.\d+\.\d+)"')
    INTERPOLATIONS: ClassVar[List[str]] = ["${{ inputs.", "${{ matrix."]
    COMMANDS: ClassVar[List[str]] = [
        "terraform fmt -check",
        "init -backend=false -input=false",
        "validate",
        "terraform test",
        "-junit-xml=",
    ]

    def test_it_is_a_reusable_workflow_taking_the_folders(self) -> None:
        assert list(triggers(NAME)) == ["workflow_call"]
        inputs = cast(Dict[str, Dict[str, JsonValue]], triggers(NAME)["workflow_call"]["inputs"])
        assert list(inputs) == ["folders"]
        assert inputs["folders"]["type"] == "string"
        assert inputs["folders"]["required"] is True

    def test_it_has_one_check_job_that_skips_an_empty_list(self) -> None:
        assert list(jobs(NAME)) == ["check"]
        assert jobs(NAME)["check"]["if"] == "inputs.folders != '[]'"

    def test_each_folder_is_its_own_matrix_entry_and_none_stops_the_others(self) -> None:
        strategy = cast(Dict[str, JsonValue], jobs(NAME)["check"]["strategy"])
        assert strategy["fail-fast"] is False
        assert cast(Dict[str, str], strategy["matrix"])["folder"] == "${{ fromJSON(inputs.folders) }}"

    def test_the_folder_reaches_the_scripts_through_the_environment(self) -> None:
        env = dict(cast(Dict[str, str], jobs(NAME)["check"].get("env", {})))
        for step in steps(NAME, "check"):
            env.update(cast(Dict[str, str], step.get("env", {})))
        assert env["FOLDER"] == "${{ matrix.folder }}"

    @pytest.mark.parametrize("interpolation", INTERPOLATIONS)
    def test_no_script_interpolates_an_input_or_a_matrix_value(self, interpolation: str) -> None:
        assert interpolation not in runs(NAME, "check")

    def test_the_checkout_keeps_no_credentials(self) -> None:
        assert with_of(step_using(NAME, "check", "actions/checkout"))["persist-credentials"] is False

    def test_terraform_is_installed_without_the_wrapper(self) -> None:
        assert with_of(step_using(NAME, "check", "hashicorp/setup-terraform"))["terraform_wrapper"] is False

    @pytest.mark.parametrize("root", ROOTS)
    def test_the_installed_version_is_the_one_each_root_requires(self, root: str) -> None:
        version = str(with_of(step_using(NAME, "check", "hashicorp/setup-terraform"))["terraform_version"])
        assert self.EXACT_VERSION.match(version)
        text = (ROOT / "infra" / "terraform" / root / "versions.tf").read_text(encoding="utf-8")
        found = self.REQUIRED.search(text)
        assert found is not None
        assert found.group(1) == version

    @pytest.mark.parametrize("command", COMMANDS)
    def test_the_scripts_run_each_terraform_command(self, command: str) -> None:
        assert command in runs(NAME, "check")

    def test_the_tests_run_only_when_the_folder_has_a_tests_folder(self) -> None:
        assert re.search(r'-d\s+"\$FOLDER/tests"', runs(NAME, "check")) is not None

    def test_the_test_report_is_kept_even_when_the_checks_fail(self) -> None:
        uploads = [step for step in steps(NAME, "check") if "upload-artifact" in str(step.get("uses", ""))]
        assert len(uploads) == 1
        assert uploads[0]["if"] == "always()"
        assert str(with_of(uploads[0])["name"]).startswith("test-report-terraform-")
