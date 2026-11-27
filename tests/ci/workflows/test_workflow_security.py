from __future__ import annotations

# Standard library imports
import re
from typing import ClassVar, Dict, List, cast

# Third-party imports
import pytest
import yaml

# First-party imports
from tests.ci.workflows.helpers import ROOT, every_uses, jobs, steps, workflow, workflow_paths

NAMES = [path.name for path in workflow_paths()]


class TestWorkflowSecurity:
    PINNED: ClassVar[re.Pattern[str]] = re.compile(r"^[\w.-]+/[\w./-]+@[0-9a-f]{40}$")
    VERSION_COMMENT: ClassVar[re.Pattern[str]] = re.compile(r"uses:\s*\S+@[0-9a-f]{40} # v\d+(\.\d+)*$")
    READ_ONLY: ClassVar[Dict[str, str]] = {"contents": "read"}
    WRITE_SCOPES: ClassVar[List[str]] = ["write", "write-all"]
    EXPECTED: ClassVar[List[str]] = [
        "automerge.yml",
        "ci.yml",
        "gitflow.yml",
        "images.yml",
        "python.yml",
        "release.yml",
        "stage.yml",
        "terraform.yml",
        "typescript.yml",
    ]
    INJECTABLE: ClassVar[List[str]] = ["${{ github.event", "${{ inputs.", "${{ github.head_ref"]

    def test_the_pipeline_has_exactly_the_expected_workflows(self) -> None:
        assert NAMES == self.EXPECTED

    @pytest.mark.parametrize("name", NAMES)
    def test_every_third_party_action_is_pinned_to_a_full_commit_sha(self, name: str) -> None:
        for uses in every_uses(name):
            if uses.startswith("./"):
                continue
            assert self.PINNED.match(uses), f"{name}: {uses} is not pinned to a 40-character commit SHA (DEP-4)."

    @pytest.mark.parametrize("name", NAMES)
    def test_every_pinned_action_names_its_version_in_a_comment(self, name: str) -> None:
        text = (ROOT / ".github" / "workflows" / name).read_text(encoding="utf-8")
        for line in text.splitlines():
            if re.search(r"uses:\s*[^.\s]\S*@", line):
                assert self.VERSION_COMMENT.search(line), f"{name}: {line.strip()} has no '# v<version>' comment."

    @pytest.mark.parametrize("name", NAMES)
    def test_the_workflow_level_permissions_are_read_only(self, name: str) -> None:
        assert workflow(name).get("permissions") == self.READ_ONLY

    @pytest.mark.parametrize("name", NAMES)
    def test_write_permissions_are_granted_per_job_only(self, name: str) -> None:
        for job, body in jobs(name).items():
            permissions = body.get("permissions")
            assert permissions != "write-all", f"{name} {job}"
            if isinstance(permissions, dict):
                assert set(cast(Dict[str, str], permissions).values()) <= {"read", "write", "none"}

    @pytest.mark.parametrize("name", NAMES)
    def test_no_script_interpolates_a_value_an_author_controls(self, name: str) -> None:
        for job in jobs(name):
            for step in steps(name, job):
                for expression in self.INJECTABLE:
                    assert expression not in str(step.get("run", "")), f"{name} {job}: {step.get('name')}"

    def test_dependabot_updates_the_pinned_actions(self) -> None:
        config = yaml.safe_load((ROOT / ".github" / "dependabot.yml").read_text(encoding="utf-8"))
        ecosystems = {update["package-ecosystem"] for update in config["updates"]}
        assert "github-actions" in ecosystems

    def test_the_osv_scanner_image_is_pinned_by_digest(self) -> None:
        env = cast(Dict[str, str], workflow("images.yml")["env"])
        assert re.search(r"@sha256:[0-9a-f]{64}$", env["OSV_SCANNER"])

    def test_every_workflow_ends_in_yml_so_that_none_escapes_these_checks(self) -> None:
        assert not list((ROOT / ".github" / "workflows").glob("*.yaml"))
