from __future__ import annotations

import re
import subprocess
from pathlib import Path
from typing import List

import pytest

from tests.infra.terraform.helpers import ROOT, committed_files


class TestTerraformStateAndCredentials:
    CREDENTIAL = re.compile(
        r"\b(access_key|secret_key|application_key|application_secret|consumer_key|client_secret|password|token"
        r'|api_key)\s*=\s*"',
        re.IGNORECASE,
    )
    BACKEND = re.compile(r"^\s*backend\s+\"?\w+\"?\s*\{", re.MULTILINE)
    VARIABLE = re.compile(r'^variable\s+"[^"]+"\s*\{.*?^\}', re.MULTILINE | re.DOTALL)

    def with_suffix(self, suffixes: List[str]) -> List[Path]:
        return [path for path in committed_files() if path.suffix in suffixes]

    def ignored(self, relative: str) -> bool:
        result = subprocess.run(["git", "-C", str(ROOT), "check-ignore", "-q", relative], check=False)
        return result.returncode == 0

    def test_no_state_variable_file_or_provider_cache_would_be_committed(self) -> None:
        for path in committed_files():
            name = path.name
            assert not name.endswith(".tfstate"), path
            assert ".tfstate." not in name, path
            assert not name.endswith((".tfvars", ".tfvars.json")), path
            assert ".terraform" not in path.relative_to(ROOT).parts[:-1], path

    def test_no_terraform_file_declares_a_state_backend(self) -> None:
        for path in self.with_suffix([".tf"]):
            assert not self.BACKEND.search(path.read_text(encoding="utf-8")), path

    @pytest.mark.parametrize(
        "relative",
        [
            "infra/terraform/ovhcloud/terraform.tfstate",
            "infra/terraform/scaleway/terraform.tfstate.backup",
            "infra/terraform/ovhcloud/.terraform/providers/x",
            "infra/terraform/scaleway/secrets.tfvars",
            "infra/terraform/modules/clouds/ovhcloud/.terraform.lock.hcl",
        ],
    )
    def test_state_secrets_and_provider_caches_are_ignored(self, relative: str) -> None:
        assert self.ignored(relative)

    def test_the_lock_file_of_a_root_is_not_ignored(self) -> None:
        assert not self.ignored("infra/terraform/ovhcloud/.terraform.lock.hcl")

    def test_no_file_assigns_a_literal_string_to_a_credential(self) -> None:
        for path in self.with_suffix([".tf", ".tfvars", ".hcl"]):
            assert not self.CREDENTIAL.search(path.read_text(encoding="utf-8")), path

    def test_no_sensitive_variable_has_a_default(self) -> None:
        for path in self.with_suffix([".tf"]):
            for block in self.VARIABLE.findall(path.read_text(encoding="utf-8")):
                if re.search(r"^\s*sensitive\s*=\s*true", block, re.MULTILINE):
                    assert not re.search(r"^\s*default\s*=", block, re.MULTILINE), path
