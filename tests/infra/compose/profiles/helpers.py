from __future__ import annotations

import os
import re
import shutil
import subprocess
from pathlib import Path
from typing import Dict, List

import yaml

ROOT = Path(__file__).resolve().parents[4]
COMPOSE_DIR = ROOT / "infra" / "compose"
ONE_SERVER = COMPOSE_DIR / "compose.yaml"
LAPTOP = COMPOSE_DIR / "compose.laptop.yaml"
GITIGNORE = COMPOSE_DIR / ".gitignore"
SERVICES = ["backoffice", "platform", "postgres"]


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


def load(path: Path) -> Dict[str, object]:
    """Load one Compose file as a mapping."""
    loaded = yaml.load(path.read_text(encoding="utf-8"), Loader=ComposeLoader)  # noqa: S506
    assert isinstance(loaded, dict)
    return loaded


def services_of(path: Path) -> Dict[str, Dict[str, object]]:
    """Return the ``services`` mapping of one Compose file."""
    services = load(path).get("services") or {}
    assert isinstance(services, dict)
    return services


def variable_names(image: str) -> List[str]:
    """Return the names of the ``${NAME...}`` variables of an image reference, in order."""
    return re.findall(r"\$\{([A-Za-z_][A-Za-z0-9_]*)", image)


def docker_available() -> bool:
    """Tell whether the ``docker compose`` command can be run."""
    if shutil.which("docker") is None:
        return False
    result = subprocess.run(["docker", "compose", "version"], capture_output=True, check=False)
    return result.returncode == 0


def sandbox(tmp_path: Path) -> Path:
    """Copy the Compose files to ``tmp_path`` with a throwaway file for every ``file:`` secret."""
    target = tmp_path / "compose"
    target.mkdir()
    for source in (ONE_SERVER, LAPTOP):
        if source.is_file():
            shutil.copy(source, target / source.name)
    secrets = load(ONE_SERVER).get("secrets") or {}
    assert isinstance(secrets, dict)
    for secret in secrets.values():
        if isinstance(secret, dict) and isinstance(secret.get("file"), str):
            secret_file = (target / str(secret["file"])).resolve()
            secret_file.parent.mkdir(parents=True, exist_ok=True)
            secret_file.write_text("throwaway\n", encoding="utf-8")
    return target


def compose(directory: Path, files: List[str], *args: str) -> subprocess.CompletedProcess[str]:
    """Run ``docker compose`` on the given files of ``directory``, with ``ERP_IMAGE_TAG`` as the only ERP variable."""
    env = {key: value for key, value in os.environ.items() if not key.startswith("ERP_")}
    env["ERP_IMAGE_TAG"] = "test"
    command = ["docker", "compose"]
    for name in files:
        command += ["-f", str(directory / name)]
    return subprocess.run(
        command + list(args),
        capture_output=True,
        text=True,
        check=False,
        encoding="utf-8",
        env=env,
        cwd=str(directory),
    )
