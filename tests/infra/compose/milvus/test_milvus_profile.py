from __future__ import annotations

from typing import Dict, List, Optional

import yaml
from yaml.nodes import MappingNode, Node, ScalarNode, SequenceNode

from tests.infra.compose.helpers import COMPOSE_DIR, profile_settings


class TestMilvusProfile:
    def plain(self, node: Node) -> object:
        """Turn a YAML node into plain data, ignoring Compose tags such as ``!override``."""
        if isinstance(node, MappingNode):
            return {str(self.plain(key)): self.plain(value) for key, value in node.value}
        if isinstance(node, SequenceNode):
            return [self.plain(item) for item in node.value]
        assert isinstance(node, ScalarNode)
        return node.value

    def compose_services(self) -> Dict[str, Dict[str, Dict[str, object]]]:
        found: Dict[str, Dict[str, Dict[str, object]]] = {}
        for path in sorted(list(COMPOSE_DIR.rglob("*.yaml")) + list(COMPOSE_DIR.rglob("*.yml"))):
            with path.open(encoding="utf-8") as handle:
                node: Optional[Node] = yaml.compose(handle, Loader=yaml.SafeLoader)
            document = self.plain(node) if node is not None else None
            if isinstance(document, dict) and isinstance(document.get("services"), dict):
                found[str(path.relative_to(COMPOSE_DIR))] = document["services"]
        return found

    def test_the_folder_holds_compose_files_including_the_laptop_profile(self) -> None:
        found = self.compose_services()
        laptop = str((COMPOSE_DIR / profile_settings()["LAPTOP_COMPOSE_FILE"]).relative_to(COMPOSE_DIR))
        assert found, f"No Compose file with services under {COMPOSE_DIR}."
        assert laptop in found, f"The laptop profile file {laptop} is not a Compose file with services."

    def test_every_milvus_service_is_only_started_by_the_ai_profile(self) -> None:
        offenders: List[str] = []
        for file_name, services in self.compose_services().items():
            for name, service in services.items():
                service = service or {}
                text = f"{name} {service.get('image', '')}".lower()
                profiles = service.get("profiles") or []
                if "milvus" in text and "ai" not in profiles:
                    offenders.append(f"{file_name}: service {name}")
        assert not offenders, f"Milvus must list the profile ai in its profiles: {offenders}."
