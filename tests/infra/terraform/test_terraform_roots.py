from __future__ import annotations

import re
from typing import List

import pytest

from tests.infra.terraform.helpers import CLOUDS, INTERFACE, MODULE_FILES, TERRAFORM, module_sources


class TestTerraformRoots:
    def root_files(self, cloud: str) -> List[str]:
        return sorted(path.name for path in (TERRAFORM / cloud).glob("*.tf"))

    def normalised(self, cloud: str, name: str) -> List[str]:
        text = (TERRAFORM / cloud / name).read_text(encoding="utf-8")
        return [
            self.provider_normalised(
                re.sub(r"\.\./modules/clouds/(ovhcloud|scaleway)", "../modules/clouds/CLOUD", line)
            )
            for line in text.splitlines()
        ]

    def provider_normalised(self, line: str) -> str:
        line = re.sub(r"^(\s*)(ovh|scaleway) = \{$", r"\1PROVIDER = {", line)
        line = re.sub(r'^(\s*source\s*=\s*)"(ovh/ovh|scaleway/scaleway)"$', r'\1"PROVIDER_SOURCE"', line)
        if line.strip().startswith("version") and "versions" not in line:
            return re.sub(r'"[^"]*"$', '"PROVIDER_VERSION"', line)
        return line

    @pytest.mark.parametrize("cloud", CLOUDS)
    def test_each_root_exists_and_holds_terraform_files(self, cloud: str) -> None:
        assert (TERRAFORM / cloud).is_dir()
        assert self.root_files(cloud)

    def test_both_roots_hold_the_same_file_names(self) -> None:
        assert self.root_files(CLOUDS[0]) == self.root_files(CLOUDS[1])

    def test_the_roots_are_identical_once_the_provider_module_is_normalised(self) -> None:
        for name in self.root_files(CLOUDS[0]):
            assert self.normalised(CLOUDS[0], name) == self.normalised(CLOUDS[1], name), name

    def test_only_the_cloud_source_and_the_provider_entry_differ_between_the_roots(self) -> None:
        differing = 0
        for name in self.root_files(CLOUDS[0]):
            first = (TERRAFORM / CLOUDS[0] / name).read_text(encoding="utf-8").splitlines()
            second = (TERRAFORM / CLOUDS[1] / name).read_text(encoding="utf-8").splitlines()
            assert len(first) == len(second), name
            differing += sum(1 for one, two in zip(first, second, strict=True) if one != two)
        assert differing == 4

    @pytest.mark.parametrize("cloud", CLOUDS)
    def test_a_root_calls_its_own_cloud_and_the_interface_once_each_and_nothing_else(self, cloud: str) -> None:
        expected = sorted([f"../modules/clouds/{cloud}", *[f"../modules/{name}" for name in INTERFACE]])
        assert sorted(module_sources(cloud)) == expected

    @pytest.mark.parametrize("cloud", CLOUDS)
    def test_every_called_module_holds_its_four_files(self, cloud: str) -> None:
        for source in module_sources(cloud):
            folder = (TERRAFORM / cloud / source).resolve()
            assert folder.is_dir(), source
            for name in MODULE_FILES:
                assert (folder / name).is_file(), f"{source}/{name}"

    @pytest.mark.parametrize("cloud", CLOUDS)
    def test_each_root_locks_its_provider_versions(self, cloud: str) -> None:
        assert (TERRAFORM / cloud / ".terraform.lock.hcl").is_file()
