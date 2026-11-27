from __future__ import annotations

import shutil
import subprocess
from pathlib import Path
from typing import ClassVar, Dict, List

import pytest
import yaml


@pytest.mark.skipif(shutil.which("helm") is None, reason="helm is not on the PATH")
class TestRendering:
    HELM: ClassVar[Path] = Path(__file__).resolve().parents[3] / "infra" / "helm"
    CHARTS: ClassVar[List[str]] = ["platform", "backoffice"]
    REGISTRY: ClassVar[str] = "ghcr.io/gpbcom/simpleerp-"
    TAG: ClassVar[str] = "abc1234"
    APP_VERSION: ClassVar[str] = "0.1.0"

    def render(self, path: Path, *options: str) -> List[Dict[str, object]]:
        result = subprocess.run(
            ["helm", "template", "simpleerp", str(path), *options],
            capture_output=True,
            text=True,
            check=False,
        )
        assert result.returncode == 0, result.stderr
        return [document for document in yaml.safe_load_all(result.stdout) if document]

    def umbrella(self, *options: str) -> List[Dict[str, object]]:
        return self.render(self.HELM, *options)

    def of_kind(self, documents: List[Dict[str, object]], kind: str) -> List[Dict[str, object]]:
        return [document for document in documents if document["kind"] == kind]

    def names(self, documents: List[Dict[str, object]], kind: str) -> List[str]:
        return sorted(str(document["metadata"]["name"]) for document in self.of_kind(documents, kind))  # type: ignore[index]

    def images(self, documents: List[Dict[str, object]]) -> List[str]:
        return sorted(
            str(container["image"])
            for deployment in self.of_kind(documents, "Deployment")
            for container in deployment["spec"]["template"]["spec"]["containers"]  # type: ignore[index]
        )

    def test_the_umbrella_renders_one_deployment_and_one_service_per_chart(self) -> None:
        documents = self.umbrella("--set", f"global.image.tag={self.TAG}")
        expected = sorted(f"simpleerp-{chart}" for chart in self.CHARTS)
        assert self.names(documents, "Deployment") == expected
        assert self.names(documents, "Service") == expected

    def test_every_image_carries_the_commit_tag(self) -> None:
        documents = self.umbrella("--set", f"global.image.tag={self.TAG}")
        expected = sorted(f"{self.REGISTRY}{chart}:{self.TAG}" for chart in self.CHARTS)
        assert self.images(documents) == expected

    def test_the_tag_falls_back_to_the_app_version(self) -> None:
        expected = sorted(f"{self.REGISTRY}{chart}:{self.APP_VERSION}" for chart in self.CHARTS)
        assert self.images(self.umbrella()) == expected

    def test_every_service_is_cluster_ip(self) -> None:
        documents = self.umbrella("--set", f"global.image.tag={self.TAG}")
        services = self.of_kind(documents, "Service")
        assert services
        assert {service["spec"]["type"] for service in services} == {"ClusterIP"}  # type: ignore[index]

    @pytest.mark.parametrize("kind", ["Ingress", "Secret"])
    def test_no_ingress_and_no_secret_is_rendered(self, kind: str) -> None:
        documents = self.umbrella("--set", f"global.image.tag={self.TAG}")
        assert self.of_kind(documents, kind) == []

    def test_disabling_the_platform_drops_its_resources(self) -> None:
        documents = self.umbrella("--set", "platform.enabled=false")
        assert self.names(documents, "Deployment") == ["simpleerp-backoffice"]
        assert self.names(documents, "Service") == ["simpleerp-backoffice"]

    @pytest.mark.parametrize("chart", ["platform", "backoffice"])
    def test_each_chart_renders_alone(self, chart: str) -> None:
        documents = self.render(self.HELM / "charts" / chart, "--set", f"global.image.tag={self.TAG}")
        assert len(self.of_kind(documents, "Deployment")) == 1
        assert len(self.of_kind(documents, "Service")) == 1
        assert self.images(documents) == [f"{self.REGISTRY}{chart}:{self.TAG}"]
