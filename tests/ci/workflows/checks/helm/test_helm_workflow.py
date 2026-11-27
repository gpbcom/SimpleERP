from __future__ import annotations

# Standard library imports
import re
from typing import ClassVar, Dict, List, cast

# Third-party imports
import pytest
from pydantic import JsonValue

# First-party imports
from tests.ci.workflows.helpers import jobs, runs, step_using, steps, triggers, with_of, workflow

NAME = "helm.yml"


class TestHelmWorkflow:
    SHA256: ClassVar[re.Pattern[str]] = re.compile(r"^[0-9a-f]{64}$")
    VERSION: ClassVar[re.Pattern[str]] = re.compile(r"^v\d+\.\d+\.\d+$")

    def test_it_is_a_reusable_workflow_named_helm(self) -> None:
        assert workflow(NAME)["name"] == "helm"
        assert list(triggers(NAME)) == ["workflow_call"]

    def test_it_can_only_read_the_repository(self) -> None:
        assert workflow(NAME)["permissions"] == {"contents": "read"}

    def test_kubeconform_is_pinned_by_version_and_checksum(self) -> None:
        env = cast(Dict[str, JsonValue], workflow(NAME)["env"])
        assert self.VERSION.match(str(env["KUBECONFORM_VERSION"]))
        assert self.SHA256.match(str(env["KUBECONFORM_SHA256"]))

    def test_it_has_one_job_named_check_with_a_timeout(self) -> None:
        assert list(jobs(NAME)) == ["check"]
        assert isinstance(jobs(NAME)["check"]["timeout-minutes"], int)

    def test_the_checkout_keeps_no_credentials(self) -> None:
        checkout = step_using(NAME, "check", "actions/checkout")
        assert with_of(checkout)["persist-credentials"] is False

    def test_helm_is_installed_at_a_pinned_version(self) -> None:
        setup = step_using(NAME, "check", "azure/setup-helm")
        assert self.VERSION.match(str(with_of(setup)["version"]))

    def test_the_kubeconform_download_is_checked_against_its_checksum(self) -> None:
        downloads = [
            str(step["run"])
            for step in steps(NAME, "check")
            if "KUBECONFORM_VERSION" in str(step.get("run", "")) and "sha256sum" in str(step.get("run", ""))
        ]
        assert len(downloads) == 1
        assert "KUBECONFORM_SHA256" in downloads[0]
        assert re.search(r"sha256sum\s+(-c|--check)\b", downloads[0])

    def test_the_check_script_runs_on_the_charts_with_the_commit_as_image_tag(self) -> None:
        assert 'bash .github/scripts/check_helm.sh infra/helm "$IMAGE_TAG" reports' in runs(NAME, "check")
        script_step = next(step for step in steps(NAME, "check") if "check_helm.sh" in str(step.get("run", "")))
        assert cast(Dict[str, JsonValue], script_step["env"])["IMAGE_TAG"] == "${{ github.sha }}"

    def test_the_steps_run_in_order(self) -> None:
        names: List[str] = []
        for step in steps(NAME, "check"):
            if "uses" in step:
                names.append(str(step["uses"]).split("@")[0])
            elif "sha256sum" in str(step.get("run", "")):
                names.append("download")
            else:
                names.append("check")
        assert names == ["actions/checkout", "azure/setup-helm", "download", "check", "actions/upload-artifact"]

    def test_the_report_is_kept_even_when_the_check_fails(self) -> None:
        uploads = [
            step for step in steps(NAME, "check") if str(step.get("uses", "")).startswith("actions/upload-artifact@")
        ]
        assert len(uploads) == 1
        assert uploads[0]["if"] == "always()"
        assert with_of(uploads[0]) == {"name": "test-report-helm", "path": "reports/", "if-no-files-found": "ignore"}

    @pytest.mark.parametrize("key", ["KUBECONFORM_VERSION", "KUBECONFORM_SHA256"])
    def test_the_pins_are_workflow_level_variables(self, key: str) -> None:
        assert key in cast(Dict[str, JsonValue], workflow(NAME)["env"])
