from __future__ import annotations

# Standard library imports
import re
from pathlib import Path
from typing import Dict, List, Optional, cast

# Third-party imports
import yaml
from pydantic import JsonValue

ROOT = Path(__file__).resolve().parents[4]
E2E = ROOT / "compose.e2e.yaml"
ONE_SERVER = ROOT / "infra" / "compose" / "compose.yaml"
LAPTOP = ROOT / "infra" / "compose" / "compose.laptop.yaml"
PREFIX = "ghcr.io/gpbcom/simpleerp"
TAG = "0123456789abcdef0123456789abcdef01234567"
SERVICES = ["platform", "backoffice", "postgres"]
PATTERN = re.compile(r"\$\{(?P<name>[A-Za-z_][A-Za-z0-9_]*)(?:(?P<op>:-|:\?)(?P<arg>[^}]*))?\}")


class ComposeLoader(yaml.SafeLoader):
    """A safe YAML loader that reads the Compose ``!override`` and ``!reset`` tags as plain values."""


def construct_tagged(loader: yaml.SafeLoader, node: yaml.Node) -> object:
    """Return the value under a Compose merge tag, as if the tag were absent."""
    if isinstance(node, yaml.MappingNode):
        return loader.construct_mapping(node, deep=True)
    if isinstance(node, yaml.SequenceNode):
        return loader.construct_sequence(node, deep=True)
    assert isinstance(node, yaml.ScalarNode)
    return loader.construct_scalar(node)


ComposeLoader.add_constructor("!override", construct_tagged)
ComposeLoader.add_constructor("!reset", construct_tagged)


def environment() -> Dict[str, str]:
    return {"ERP_IMAGE_PREFIX": PREFIX, "ERP_IMAGE_TAG": TAG}


def resolve_one(match: re.Match[str], env: Dict[str, str]) -> str:
    name = match.group("name")
    op: Optional[str] = match.group("op")
    value = env.get(name, "")
    if value:
        return value
    if op == ":-":
        return resolve(match.group("arg"), env)
    if op == ":?":
        raise KeyError(f"{name}: {match.group('arg')}")
    return ""


def resolve(text: str, env: Dict[str, str]) -> str:
    """Resolve ``${VAR}``, ``${VAR:-default}`` and ``${VAR:?message}`` against ``env``."""
    out = ""
    last = 0
    for match in PATTERN.finditer(text):
        out += text[last : match.start()] + resolve_one(match, env)
        last = match.end()
    return out + text[last:]


def services(path: Path) -> Dict[str, Dict[str, JsonValue]]:
    data = yaml.load(path.read_text(encoding="utf-8"), Loader=ComposeLoader)  # noqa: S506
    assert isinstance(data, dict), path
    return cast(Dict[str, Dict[str, JsonValue]], data.get("services", {}))


def merged_services(paths: List[Path]) -> Dict[str, Dict[str, JsonValue]]:
    """Merge the services of several Compose files, a later file overriding an earlier one key by key."""
    merged: Dict[str, Dict[str, JsonValue]] = {}
    for path in paths:
        for name, service in services(path).items():
            merged.setdefault(name, {}).update(service)
    return merged


def image_of(paths: List[Path], service: str, env: Dict[str, str]) -> str:
    found = merged_services(paths)[service]["image"]
    assert isinstance(found, str), service
    return resolve(found, env)
