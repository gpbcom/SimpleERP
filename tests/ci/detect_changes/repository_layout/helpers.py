from __future__ import annotations

# Standard library imports
from pathlib import Path
from typing import Dict, List

# First-party imports
from tests.ci.detect_changes.helpers import (
    HELM_KEY,
    IMAGES_KEY,
    PACKAGES_KEY,
    REPOSITORY_KEY,
    SERVICES_KEY,
    TYPESCRIPT_KEY,
    compact,
    nothing,
)

# The repository the layout tests read: the one this file is in, or the fixture repository it was copied into.
LAYOUT_ROOT = Path(__file__).resolve().parents[4]
# The marker files ``.github/scripts/detect_changes.py`` selects a folder on, and the output each one fills, by kind
# of folder of the layout (D438). A README in a folder selects exactly what the markers present in that folder fill.
# Compose files are no marker: the detector never selects ``infra/compose/`` (``compose.e2e.yaml`` at the root is a
# shared file), so that folder stays a folder without a project.
SERVICE_MARKERS: Dict[str, str] = {"pyproject.toml": SERVICES_KEY, "Dockerfile": IMAGES_KEY}
PACKAGE_MARKERS: Dict[str, str] = {"pyproject.toml": PACKAGES_KEY}
FRONT_END_MARKERS: Dict[str, str] = {"package.json": TYPESCRIPT_KEY, "Dockerfile": IMAGES_KEY}
HELM_MARKERS: Dict[str, str] = {"Chart.yaml": HELM_KEY}
NO_MARKERS: Dict[str, str] = {}
# The folders of the layout whose README the detector judges, as globs; an exact folder beats a glob that matches it.
# ``backend/models`` and ``backend/shared`` are shared (everything), ``frontend/packages`` selects every front end and
# ``infra/terraform`` every module: each has its own test, so they are skipped here.
LAYOUT: Dict[str, Dict[str, str]] = {
    "backend/services": NO_MARKERS,
    "backend/services/*": SERVICE_MARKERS,
    "plugins": NO_MARKERS,
    "plugins/*": PACKAGE_MARKERS,
    "sdk": PACKAGE_MARKERS,
    "frontend/*": FRONT_END_MARKERS,
    "frontend/portals": NO_MARKERS,
    "frontend/portals/*": FRONT_END_MARKERS,
    "infra/*": NO_MARKERS,
    "infra/helm": HELM_MARKERS,
    "packs/*": NO_MARKERS,
}
SKIPPED = frozenset({"frontend/packages", "infra/terraform"})
# A changed path under ``bruno/`` always sets ``repository``, and ``bruno/<name>/`` selects the service of that name.
BRUNO = "bruno"
SERVICES = "backend/services"
PORTALS = "frontend/portals"
PORTAL_IMAGE_PREFIX = "portal-"


def layout_folders(root: Path) -> Dict[str, Dict[str, str]]:
    """Return every folder of the layout present under ``root``, with the markers that would make it a project."""
    found: Dict[str, Dict[str, str]] = {}
    for pattern, markers in sorted(LAYOUT.items(), key=lambda item: "*" not in item[0]):
        for folder in root.glob(pattern):
            name = folder.relative_to(root).as_posix()
            if folder.is_dir() and not folder.name.startswith((".", "_")) and name not in SKIPPED:
                found[name] = markers
    bruno = root / BRUNO
    if bruno.is_dir():
        found[BRUNO] = NO_MARKERS
        for collection in bruno.iterdir():
            if collection.is_dir() and not collection.name.startswith((".", "_")):
                found[f"{BRUNO}/{collection.name}"] = NO_MARKERS
    return dict(sorted(found.items()))


def image_name(folder: str) -> str:
    name = folder.rsplit("/", 1)[-1]
    return f"{PORTAL_IMAGE_PREFIX}{name}" if folder.startswith(f"{PORTALS}/") else name


def readme_selection(root: Path, folder: str) -> Dict[str, str]:
    """Return what a change to ``<folder>/README.md`` selects, from the marker files present in ``folder``."""
    expected = nothing()
    for marker, key in layout_folders(root).get(folder, NO_MARKERS).items():
        if not (root / folder / marker).is_file():
            continue
        if key == IMAGES_KEY:
            expected[key] = compact([{"folder": folder, "name": image_name(folder)}])
        elif key == HELM_KEY:
            expected[HELM_KEY] = "true"
            expected[REPOSITORY_KEY] = "true"
        else:
            expected[key] = compact([folder])
    parts = folder.split("/")
    if parts[0] == BRUNO:
        expected[REPOSITORY_KEY] = "true"
        service = f"{SERVICES}/{parts[1]}" if len(parts) == 2 else None
        if service and (root / service / "pyproject.toml").is_file():
            expected[SERVICES_KEY] = compact([service])
    return expected


def folders_without_a_project(root: Path) -> List[str]:
    """Return the layout folders whose README selects nothing, because they hold no marker of the detector."""
    return [folder for folder in layout_folders(root) if readme_selection(root, folder) == nothing()]


def folders_with_a_project(root: Path) -> List[str]:
    """Return the layout folders whose README selects something, because they hold a marker of the detector."""
    return [folder for folder in layout_folders(root) if readme_selection(root, folder) != nothing()]
