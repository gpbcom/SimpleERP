from __future__ import annotations

# Standard library imports
from pathlib import Path

# Third-party imports
import pytest

# First-party imports
from tests.ci.detect_changes.helpers import (
    ALL_TERRAFORM,
    REPOSITORY_KEY,
    SALES,
    TERRAFORM_KEY,
    compact,
    detect,
    everything,
    nothing,
    outputs,
    run_detector,
)


class TestTerraformChanges:
    @pytest.mark.parametrize(
        "path",
        [
            "infra/terraform/ovhcloud/main.tf",
            "infra/terraform/modules/network/main.tf",
            "infra/terraform/modules/clouds/ovhcloud/variables.tf",
            "infra/terraform/README.md",
        ],
    )
    def test_any_change_under_infra_terraform_selects_every_terraform_folder(self, tmp_path: Path, path: str) -> None:
        assert detect(tmp_path, [path]) == {**nothing(), REPOSITORY_KEY: "true", TERRAFORM_KEY: compact(ALL_TERRAFORM)}

    def test_all_lists_the_terraform_folders_sorted_at_any_depth(self, tmp_path: Path) -> None:
        assert detect(tmp_path, [], "--all")[TERRAFORM_KEY] == compact(ALL_TERRAFORM)

    def test_hidden_and_tests_folders_are_never_listed(self, tmp_path: Path) -> None:
        folders = detect(tmp_path, ["infra/terraform/scaleway/main.tf"])[TERRAFORM_KEY]
        assert ".terraform" not in folders
        assert "/tests" not in folders

    def test_a_folder_without_a_tf_file_is_never_listed(self, tmp_path: Path) -> None:
        folders = detect(tmp_path, ["infra/terraform/README.md"])[TERRAFORM_KEY]
        assert folders == compact(ALL_TERRAFORM)

    def test_the_terraform_workflow_is_a_shared_path(self, tmp_path: Path) -> None:
        assert detect(tmp_path, [".github/workflows/terraform.yml"]) == everything()

    def test_a_change_outside_infra_terraform_selects_no_terraform_folder(self, tmp_path: Path) -> None:
        assert detect(tmp_path, [f"{SALES}/src/sales/x.py"])[TERRAFORM_KEY] == "[]"

    def test_a_repository_without_infra_terraform_gives_an_empty_list(self, tmp_path: Path) -> None:
        result = run_detector(tmp_path, ["infra/terraform/ovhcloud/main.tf"])
        assert result.returncode == 0, result.stderr
        assert outputs(result)[TERRAFORM_KEY] == "[]"
