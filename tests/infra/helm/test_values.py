from __future__ import annotations

import re
from pathlib import Path
from typing import ClassVar, Dict, List, Tuple

import pytest
import yaml


class TestValues:
    ROOT: ClassVar[Path] = Path(__file__).resolve().parents[3]
    HELM: ClassVar[Path] = ROOT / "infra" / "helm"
    GLOBAL_IMAGE: ClassVar[Dict[str, str]] = {
        "prefix": "ghcr.io/gpbcom/simpleerp",
        "tag": "",
        "pullPolicy": "IfNotPresent",
    }
    CHART_DEFAULTS: ClassVar[Dict[str, object]] = {
        "enabled": True,
        "replicaCount": 1,
        "env": {},
        "resources": {},
        "podSecurityContext": {},
        "securityContext": {},
        "nodeSelector": {},
        "tolerations": [],
        "affinity": {},
    }
    VALUES_REFERENCE: ClassVar[re.Pattern[str]] = re.compile(
        r"\.Values\.([A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z_][A-Za-z0-9_]*)*)"
    )
    BARE_VALUES: ClassVar[re.Pattern[str]] = re.compile(r"\.Values\b(?!\.)")
    SECRET_KEY: ClassVar[re.Pattern[str]] = re.compile(
        r"password|passwd|secret|token|credential|private_?key|api_?key", re.IGNORECASE
    )
    KIND_SECRET: ClassVar[re.Pattern[str]] = re.compile(r"^\s*kind:\s*[\"']?Secret[\"']?\s*$", re.MULTILINE)
    ENTRY_NAME: ClassVar[re.Pattern[str]] = re.compile(r"^[A-Za-z0-9_.\-/]*$")

    def values_path(self, name: str) -> Path:
        if name == "umbrella":
            return self.HELM / "values.yaml"
        return self.HELM / "charts" / name / "values.yaml"

    def load(self, name: str) -> Dict[str, object]:
        data = yaml.safe_load(self.values_path(name).read_text(encoding="utf-8"))
        assert isinstance(data, dict)
        return data

    def is_port(self, value: object) -> bool:
        return isinstance(value, int) and not isinstance(value, bool) and 0 < value < 65536

    def lookup(self, data: object, dotted: str) -> Tuple[bool, object]:
        current = data
        for part in dotted.split("."):
            if not isinstance(current, dict) or part not in current:
                return False, None
            current = current[part]
        return True, current

    def walk(self, data: object, prefix: str = "") -> List[Tuple[str, object]]:
        found: List[Tuple[str, object]] = []
        if isinstance(data, dict):
            for key, value in data.items():
                path = f"{prefix}.{key}" if prefix else str(key)
                found.append((path, value))
                found.extend(self.walk(value, path))
        return found

    def template_files(self, chart: str) -> List[Path]:
        folder = self.HELM / "charts" / chart / "templates"
        return sorted(path for path in folder.glob("*") if path.is_file())

    @pytest.mark.parametrize("name", ["umbrella", "platform", "backoffice"])
    def test_each_values_file_parses_to_a_mapping(self, name: str) -> None:
        assert isinstance(self.load(name), dict)

    @pytest.mark.parametrize("name", ["umbrella", "platform", "backoffice"])
    @pytest.mark.parametrize("key", ["prefix", "tag", "pullPolicy"])
    def test_the_global_image_is_written_out_in_every_values_file(self, name: str, key: str) -> None:
        found, value = self.lookup(self.load(name), f"global.image.{key}")
        assert found
        assert value == self.GLOBAL_IMAGE[key]

    @pytest.mark.parametrize("chart", ["platform", "backoffice"])
    @pytest.mark.parametrize("key", sorted(CHART_DEFAULTS))
    def test_a_chart_writes_out_its_defaults(self, chart: str, key: str) -> None:
        found, value = self.lookup(self.load(chart), key)
        assert found
        assert value == self.CHART_DEFAULTS[key]
        assert type(value) is type(self.CHART_DEFAULTS[key])

    @pytest.mark.parametrize("chart", ["platform", "backoffice"])
    def test_a_chart_writes_out_its_port_service_and_probe(self, chart: str) -> None:
        values = self.load(chart)
        found_port, port = self.lookup(values, "containerPort")
        found_service_port, service_port = self.lookup(values, "service.port")
        found_type, service_type = self.lookup(values, "service.type")
        found_path, probe_path = self.lookup(values, "probe.path")
        assert [found_port, found_service_port, found_type, found_path] == [True] * 4
        assert self.is_port(port)
        assert self.is_port(service_port)
        assert service_type == "ClusterIP"
        assert str(probe_path).startswith("/")

    @pytest.mark.parametrize("chart", ["platform", "backoffice"])
    def test_a_chart_image_name_is_its_folder_name(self, chart: str) -> None:
        found, value = self.lookup(self.load(chart), "image.name")
        assert found
        assert value == chart

    @pytest.mark.parametrize("chart", ["platform", "backoffice"])
    def test_every_value_a_template_reads_is_written_out_in_the_chart_values(self, chart: str) -> None:
        templates = self.template_files(chart)
        assert templates, f"The chart {chart} has no template."
        values = self.load(chart)
        missing: List[str] = []
        for path in templates:
            for match in self.VALUES_REFERENCE.finditer(path.read_text(encoding="utf-8")):
                if not self.lookup(values, match.group(1))[0]:
                    missing.append(f"{path.name}: {match.group(1)}")
        assert missing == []

    @pytest.mark.parametrize("chart", ["platform", "backoffice"])
    def test_a_template_reads_values_only_through_full_paths(self, chart: str) -> None:
        templates = self.template_files(chart)
        assert templates, f"The chart {chart} has no template."
        offenders = [path.name for path in templates if self.BARE_VALUES.search(path.read_text(encoding="utf-8"))]
        assert offenders == []

    @pytest.mark.parametrize("chart", ["platform", "backoffice"])
    def test_the_umbrella_enables_each_chart(self, chart: str) -> None:
        found, value = self.lookup(self.load("umbrella"), f"{chart}.enabled")
        assert found
        assert value is True

    @pytest.mark.parametrize("chart", ["platform", "backoffice"])
    def test_the_umbrella_section_uses_no_key_the_chart_lacks(self, chart: str) -> None:
        found, section = self.lookup(self.load("umbrella"), chart)
        assert found
        own = self.load(chart)
        unknown = [path for path, _ in self.walk(section) if not self.lookup(own, path)[0]]
        assert unknown == []

    @pytest.mark.parametrize("name", ["umbrella", "platform", "backoffice"])
    def test_no_key_names_a_secret(self, name: str) -> None:
        offenders: List[str] = []
        for path, _ in self.walk(self.load(name)):
            if self.SECRET_KEY.search(path.split(".")[-1]):
                offenders.append(path)
        assert offenders == []

    @pytest.mark.parametrize("name", ["umbrella", "platform", "backoffice"])
    def test_a_key_ending_in_key_holds_only_an_empty_value_or_an_entry_name(self, name: str) -> None:
        offenders: List[str] = []
        for path, value in self.walk(self.load(name)):
            if not path.split(".")[-1].endswith("_key"):
                continue
            if not (value is None or (isinstance(value, str) and self.ENTRY_NAME.match(value))):
                offenders.append(path)
        assert offenders == []

    def test_no_template_declares_a_secret(self) -> None:
        templates = [path for path in self.HELM.rglob("templates/*") if path.is_file()]
        assert templates
        offenders = [str(path) for path in templates if self.KIND_SECRET.search(path.read_text(encoding="utf-8"))]
        assert offenders == []
