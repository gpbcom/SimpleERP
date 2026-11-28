from __future__ import annotations

# Standard library imports
import re
from pathlib import Path
from typing import Dict, List, Set, cast

# Third-party imports
import yaml
from pydantic import JsonValue

ROOT = Path(__file__).resolve().parents[4]
COMPOSE = ROOT / "compose.e2e.yaml"
SERVICES = ["platform", "backoffice", "postgres"]
BUILT_SERVICES = {
    "platform": "backend/services/platform/Dockerfile",
    "backoffice": "frontend/backoffice/Dockerfile",
}
PROVIDED_VARIABLES = {"ERP_IMAGE_PREFIX", "ERP_IMAGE_TAG"}
Service = Dict[str, JsonValue]


def compose_text() -> str:
    return COMPOSE.read_text(encoding="utf-8")


def compose() -> Dict[str, JsonValue]:
    data = yaml.safe_load(compose_text())
    assert isinstance(data, dict), "compose.e2e.yaml must be a mapping"
    return cast(Dict[str, JsonValue], data)


def services() -> Dict[str, Service]:
    return cast(Dict[str, Service], compose()["services"])


def service(name: str) -> Service:
    return services()[name]


def depends_on(name: str) -> Dict[str, Dict[str, JsonValue]]:
    """Return ``depends_on`` of a service in its long form, whichever form the file uses."""
    value = service(name).get("depends_on", {})
    if isinstance(value, list):
        return {str(item): {} for item in value}
    return cast(Dict[str, Dict[str, JsonValue]], value)


def environment(name: str) -> Dict[str, str]:
    """Return the environment of a service as a dictionary, whichever form the file uses."""
    value = service(name).get("environment", {})
    result: Dict[str, str] = {}
    if isinstance(value, list):
        for entry in value:
            key, _, text = str(entry).partition("=")
            result[key] = text
    elif isinstance(value, dict):
        for key, item in value.items():
            result[key] = "" if item is None else str(item)
    return result


def healthcheck_command(name: str) -> str:
    test = cast(Dict[str, JsonValue], service(name)["healthcheck"])["test"]
    if isinstance(test, list):
        return " ".join(str(part) for part in test)
    return str(test)


def variables_without_default() -> Set[str]:
    """Return the variables referenced as ``${VAR}`` or ``${VAR:?message}``, which have no default."""
    found: List[str] = re.findall(r"(?<!\$)\$\{([A-Za-z_][A-Za-z0-9_]*)(?::?\?[^}]*)?\}", compose_text())
    return set(found)
