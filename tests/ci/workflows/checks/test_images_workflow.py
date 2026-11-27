from __future__ import annotations

# Standard library imports
from typing import ClassVar, Dict, List, cast

# Third-party imports
import pytest
from pydantic import JsonValue

# First-party imports
from tests.ci.workflows.helpers import Step, jobs, runs, step_using, steps, triggers, with_of, workflow

NAME = "images.yml"


class TestImagesWorkflow:
    JOBS: ClassVar[List[str]] = ["scan-dependencies", "image", "e2e", "publish"]
    PUSH_PERMISSIONS: ClassVar[Dict[str, str]] = {"contents": "read", "packages": "write", "id-token": "write"}
    SIGNER: ClassVar[str] = r"^https://github\.com/gpbcom/SimpleERP/\.github/workflows/images\.yml@"

    def index(self, job: str, text: str) -> int:
        """Return the index of the first step of ``job`` whose ``uses`` or ``run`` holds ``text``."""
        found = [
            i for i, step in enumerate(steps(NAME, job)) if text in f"{step.get('uses', '')} {step.get('run', '')}"
        ]
        assert found, f"No step of {job} holds {text}."
        return found[0]

    def step_named(self, job: str, name: str) -> Step:
        [found] = [step for step in steps(NAME, job) if step.get("name") == name]
        return found

    def test_it_is_a_reusable_workflow_taking_the_images_and_the_publish_switch(self) -> None:
        assert list(triggers(NAME)) == ["workflow_call"]
        inputs = cast(Dict[str, Dict[str, JsonValue]], triggers(NAME)["workflow_call"]["inputs"])
        assert set(inputs) == {"images", "publish"}
        assert inputs["publish"]["default"] is False

    def test_the_jobs_run_in_order(self) -> None:
        assert list(jobs(NAME)) == self.JOBS
        for before, after in zip(self.JOBS, self.JOBS[1:], strict=False):
            assert jobs(NAME)[after]["needs"] == before

    def test_the_jobs_that_push_and_sign_have_the_permissions_to_do_so(self) -> None:
        assert jobs(NAME)["image"]["permissions"] == self.PUSH_PERMISSIONS
        assert jobs(NAME)["e2e"]["permissions"] == {"contents": "read", "packages": "read"}
        assert jobs(NAME)["publish"]["permissions"] == {"contents": "read", "packages": "write"}

    def test_the_dependency_scan_reads_only_the_lock_files_that_exist(self) -> None:
        script = runs(NAME, "scan-dependencies")
        assert "for lockfile in uv.lock pnpm-lock.yaml" in script
        assert 'scan source "${lockfiles[@]}"' in script

    @pytest.mark.parametrize("job", ["image", "publish"])
    def test_each_image_is_its_own_matrix_entry(self, job: str) -> None:
        matrix = cast(Dict[str, Dict[str, str]], jobs(NAME)[job]["strategy"])["matrix"]
        assert matrix["include"] == "${{ fromJSON(inputs.images) }}"

    def test_the_image_is_named_after_the_repository_and_its_folder(self) -> None:
        assert 'echo "IMAGE=ghcr.io/${GITHUB_REPOSITORY,,}-${NAME}"' in runs(NAME, "image")

    def test_the_build_uses_the_repository_root_and_the_actions_cache(self) -> None:
        options = with_of(step_using(NAME, "image", "docker/build-push-action"))
        assert options["context"] == "."
        assert options["file"] == "${{ matrix.folder }}/Dockerfile"
        assert "type=gha" in str(options["cache-from"])
        assert "mode=max" in str(options["cache-to"])

    def test_the_image_is_built_scanned_pushed_signed_attested_and_verified_in_order(self) -> None:
        order = [
            self.index("image", "docker/build-push-action"),
            self.index("image", "trivy image --severity HIGH,CRITICAL --ignore-unfixed --exit-code 1"),
            self.index("image", "--format cyclonedx"),
            self.index("image", "docker push"),
            self.index("image", "cosign sign --yes"),
            self.index("image", "cosign attest --yes --type cyclonedx"),
            self.index("image", "cosign verify"),
        ]
        assert order == sorted(order)

    def test_signatures_are_checked_against_this_repository_keyless_identity(self) -> None:
        env = cast(Dict[str, str], workflow(NAME)["env"])
        assert env["SIGNER"] == self.SIGNER
        assert env["OIDC_ISSUER"] == "https://token.actions.githubusercontent.com"
        for job in ("image", "publish"):
            assert '--certificate-identity-regexp "$SIGNER"' in runs(NAME, job)

    def test_no_image_job_step_tags_with_the_commit_sha(self) -> None:
        assert "GITHUB_SHA" not in runs(NAME, "image")

    def test_e2e_runs_only_when_compose_e2e_exists(self) -> None:
        assert "if [ -f compose.e2e.yaml ]" in runs(NAME, "e2e")
        for step in steps(NAME, "e2e")[2:]:
            if step.get("name") != "Keep the Playwright reports":
                assert "steps.compose.outputs.present == 'true'" in str(step.get("if")), step

    def test_e2e_starts_the_real_images_then_runs_playwright_then_always_stops_them(self) -> None:
        start = self.index("e2e", "up --detach --wait")
        assert start < self.index("e2e", "bash .github/scripts/playwright.sh")
        stop = self.step_named("e2e", "Stop the stack")
        assert "always()" in str(stop["if"])
        assert "down --volumes" in str(stop["run"])

    def test_e2e_keeps_the_playwright_reports_of_a_failed_run(self) -> None:
        upload = step_using(NAME, "e2e", "actions/upload-artifact")
        assert upload["if"] == "failure()"
        assert "frontend/**/playwright-report/" in str(with_of(upload)["path"])

    def test_publish_adds_the_commit_sha_tag_to_the_tested_digest(self) -> None:
        assert jobs(NAME)["publish"]["if"] == "inputs.publish"
        script = runs(NAME, "publish")
        assert 'imagetools create --tag "${image}:${GITHUB_SHA}" "${image}:${RUN_TAG}"' in script
        assert 'test "$before" = "$after"' in script
