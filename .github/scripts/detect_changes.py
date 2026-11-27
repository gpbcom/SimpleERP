"""Select what CI checks from the paths a push or a pull request changes (layout D438).

Usage:
    git diff --name-only <base> <head> | python3 .github/scripts/detect_changes.py [--root <repo root>]
    python3 .github/scripts/detect_changes.py --all [--root <repo root>]

It prints five ``key=value`` lines for ``$GITHUB_OUTPUT``, in this order:

- ``services``: a compact JSON list of the ``backend/services/<service>`` folders to check;
- ``packages``: a compact JSON list of the shared Python packages to check (``backend/models``,
  ``backend/shared/<lib>``, ``plugins/<plugin>``, ``sdk``);
- ``typescript``: a compact JSON list of the front-end projects to check (``frontend/<app>``,
  ``frontend/portals/<portal>``, ``frontend/packages/<package>``), each with a ``package.json``;
- ``repository``: ``true`` when the repository tests must run (``tests/``, ``.claude/``, ``.githooks/``, ``.github/``);
- ``images``: a compact JSON list of ``{"folder": ..., "name": ...}`` objects, one per folder with a ``Dockerfile`` that
  the change touches. The image is ``ghcr.io/<owner>/<repo>-<name>``.

A shared path (the root lock files and manifests, ``backend/models/``, ``backend/shared/``, ``compose.e2e.yaml``,
``.dockerignore``, ``.github/scripts/`` and the reusable workflows) selects everything that exists. ``--all`` does the
same without reading stdin. A folder that does not exist yet is never listed, so every list is empty on a repository
with no service and no front end.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import List, Optional, Set

SERVICES = "backend/services"
FRONTEND = "frontend"
PORTALS = "frontend/portals"
FRONTEND_PACKAGES = "frontend/packages"
PACKAGE_GROUPS = ("backend/shared", "plugins")
PACKAGE_FOLDERS = ("backend/models", "sdk")
FRONTEND_GROUPS = frozenset({"portals", "packages"})
SHARED_PREFIXES = ("backend/models/", "backend/shared/", ".github/scripts/")
SHARED_FILES = frozenset(
    {
        "uv.lock",
        "pyproject.toml",
        ".python-version",
        "pnpm-lock.yaml",
        "package.json",
        "pnpm-workspace.yaml",
        "compose.e2e.yaml",
        ".dockerignore",
        ".github/workflows/ci.yml",
        ".github/workflows/python.yml",
        ".github/workflows/typescript.yml",
        ".github/workflows/images.yml",
    }
)
REPOSITORY_PREFIXES = ("tests/", ".claude/", ".githooks/", ".github/")
PORTAL_IMAGE_PREFIX = "portal-"
USAGE = "usage: detect_changes.py [--root <repo root>] [--all]"


def children(root: Path, parent: str, marker: str) -> List[str]:
    """List the folders directly under ``parent`` that hold ``marker``, skipping hidden and ``_`` folders."""
    folder = root / parent
    if not folder.is_dir():
        return []
    return sorted(
        f"{parent}/{child.name}"
        for child in folder.iterdir()
        if child.is_dir() and not child.name.startswith((".", "_")) and (child / marker).is_file()
    )


def discover_services(root: Path) -> List[str]:
    """List the ``backend/services/<service>`` folders holding a ``pyproject.toml``."""
    return children(root, SERVICES, "pyproject.toml")


def discover_packages(root: Path) -> List[str]:
    """List the shared Python package folders holding a ``pyproject.toml``."""
    found = [folder for folder in PACKAGE_FOLDERS if (root / folder / "pyproject.toml").is_file()]
    for group in PACKAGE_GROUPS:
        found += children(root, group, "pyproject.toml")
    return sorted(found)


def discover_frontends(root: Path, marker: str) -> List[str]:
    """List the front-end project folders (apps, portals and packages) holding ``marker``."""
    apps = [folder for folder in children(root, FRONTEND, marker) if folder.split("/", 1)[1] not in FRONTEND_GROUPS]
    return sorted(apps + children(root, PORTALS, marker) + children(root, FRONTEND_PACKAGES, marker))


def image_name(folder: str) -> str:
    """Return the image name of a folder: its own name, ``portal-<name>`` for a portal."""
    name = folder.rsplit("/", 1)[-1]
    return f"{PORTAL_IMAGE_PREFIX}{name}" if folder.startswith(f"{PORTALS}/") else name


def discover_images(root: Path) -> List[str]:
    """List the service and front-end folders holding a ``Dockerfile`` (shared packages build no image)."""
    frontends = [
        folder for folder in discover_frontends(root, "Dockerfile") if not folder.startswith(FRONTEND_PACKAGES)
    ]
    return sorted(children(root, SERVICES, "Dockerfile") + frontends)


def owner(path: str, folders: List[str]) -> Optional[str]:
    """Return the folder of ``folders`` that holds ``path``, if any."""
    return next((folder for folder in folders if path.startswith(f"{folder}/")), None)


def is_shared(path: str) -> bool:
    """Tell whether a changed path selects everything that exists."""
    return path in SHARED_FILES or path.startswith(SHARED_PREFIXES)


def read_paths(text: str) -> List[str]:
    """Split stdin into paths, ignoring blank lines and surrounding spaces."""
    return [line.strip() for line in text.splitlines() if line.strip()]


def parse_args(argv: List[str]) -> Optional[argparse.Namespace]:
    """Read the arguments: the root and the ``--all`` flag, or None when they are bad."""
    parser = argparse.ArgumentParser(add_help=False, allow_abbrev=False, exit_on_error=False)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--all", action="store_true", dest="everything")
    try:
        args, unknown = parser.parse_known_args(argv)
    except argparse.ArgumentError:
        return None
    return None if unknown else args


def compact(value: object) -> str:
    """Write ``value`` as compact JSON, on one line."""
    return json.dumps(value, separators=(",", ":"))


def main(argv: Optional[List[str]] = None) -> int:
    """Print the five output lines for the changed paths on stdin."""
    parsed = parse_args(sys.argv[1:] if argv is None else argv)
    if parsed is None:
        print(USAGE, file=sys.stderr)
        return 2
    root, everything = parsed.root, parsed.everything
    all_services = discover_services(root)
    all_packages = discover_packages(root)
    all_typescript = discover_frontends(root, "package.json")
    all_images = discover_images(root)
    frontend_images = [folder for folder in all_images if folder.startswith(f"{FRONTEND}/")]

    services: Set[str] = set()
    packages: Set[str] = set()
    typescript: Set[str] = set()
    images: Set[str] = set()
    repository = False
    for path in [] if everything else read_paths(sys.stdin.read()):
        if is_shared(path):
            everything = True
            continue
        if path.startswith(f"{FRONTEND_PACKAGES}/"):
            typescript |= set(all_typescript)
            images |= set(frontend_images)
        for selected, folders in (
            (services, all_services),
            (packages, all_packages),
            (typescript, all_typescript),
            (images, all_images),
        ):
            folder = owner(path, folders)
            if folder:
                selected.add(folder)
        repository = repository or path.startswith(REPOSITORY_PREFIXES)
    if everything:
        services, packages = set(all_services), set(all_packages)
        typescript, images = set(all_typescript), set(all_images)
        repository = True

    print(f"services={compact(sorted(services))}")
    print(f"packages={compact(sorted(packages))}")
    print(f"typescript={compact(sorted(typescript))}")
    print(f"repository={str(repository).lower()}")
    print(f"images={compact([{'folder': folder, 'name': image_name(folder)} for folder in sorted(images)])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
