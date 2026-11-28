from __future__ import annotations

import shutil
import subprocess
from pathlib import Path
from typing import ClassVar, Dict, List

import pytest
import yaml


@pytest.mark.skipif(shutil.which("helm") is None, reason="helm is not on the PATH")
class TestBackofficePlatformUrl:
    HELM: ClassVar[Path] = Path(__file__).resolve().parents[3] / "infra" / "helm"
    RELEASE: ClassVar[str] = "acme"
    NAMESPACE: ClassVar[str] = "erp"
    VARIABLE: ClassVar[str] = "ERP_PLATFORM_URL"

    def render(self, *options: str) -> List[Dict[str, object]]:
        result = subprocess.run(
            ["helm", "template", self.RELEASE, str(self.HELM), "--namespace", self.NAMESPACE, *options],
            capture_output=True,
            text=True,
            check=False,
        )
        assert result.returncode == 0, result.stderr
        return [document for document in yaml.safe_load_all(result.stdout) if document]

    def named(self, documents: List[Dict[str, object]], kind: str, name: str) -> Dict[str, object]:
        found = [
            document
            for document in documents
            if document["kind"] == kind and document["metadata"]["name"] == name  # type: ignore[index]
        ]
        assert len(found) == 1, f"No single {kind} named {name}."
        return found[0]

    def backoffice_env(self, documents: List[Dict[str, object]]) -> Dict[str, str]:
        deployment = self.named(documents, "Deployment", f"{self.RELEASE}-backoffice")
        container = deployment["spec"]["template"]["spec"]["containers"][0]  # type: ignore[index]
        names = [str(entry["name"]) for entry in container.get("env", [])]
        assert len(names) == len(set(names)), f"A variable is set twice: {names}."
        return {str(entry["name"]): str(entry["value"]) for entry in container.get("env", [])}

    def test_the_back_office_points_at_the_platform_service_of_its_release(self) -> None:
        documents = self.render()
        service = self.named(documents, "Service", f"{self.RELEASE}-platform")
        port = service["spec"]["ports"][0]["port"]  # type: ignore[index]
        expected = f"http://{self.RELEASE}-platform.{self.NAMESPACE}.svc.cluster.local:{port}"
        assert port == 8000
        assert self.backoffice_env(documents)[self.VARIABLE] == expected

    def test_the_platform_port_and_the_cluster_domain_are_values(self) -> None:
        documents = self.render(
            "--set", "backoffice.platformPort=9000", "--set", "backoffice.clusterDomain=example.org"
        )
        expected = f"http://{self.RELEASE}-platform.{self.NAMESPACE}.svc.example.org:9000"
        assert self.backoffice_env(documents)[self.VARIABLE] == expected

    def test_a_set_platform_url_overrides_the_derived_one(self) -> None:
        documents = self.render("--set", "backoffice.platformUrl=http://gateway.example.org:8443")
        assert self.backoffice_env(documents)[self.VARIABLE] == "http://gateway.example.org:8443"

    def test_the_env_map_still_adds_its_variables(self) -> None:
        documents = self.render("--set", "backoffice.env.TZ=Europe/Paris")
        env = self.backoffice_env(documents)
        assert env["TZ"] == "Europe/Paris"
        assert env[self.VARIABLE].startswith(f"http://{self.RELEASE}-platform.")

    def test_the_env_map_wins_over_the_derived_url(self) -> None:
        documents = self.render("--set", f"backoffice.env.{self.VARIABLE}=http://elsewhere:8000")
        assert self.backoffice_env(documents)[self.VARIABLE] == "http://elsewhere:8000"
