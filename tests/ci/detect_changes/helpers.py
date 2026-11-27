from __future__ import annotations

# Standard library imports
import json
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Union

SERVICES_KEY = "services"
PACKAGES_KEY = "packages"
TYPESCRIPT_KEY = "typescript"
REPOSITORY_KEY = "repository"
IMAGES_KEY = "images"
KEYS = [SERVICES_KEY, PACKAGES_KEY, TYPESCRIPT_KEY, REPOSITORY_KEY, IMAGES_KEY]
SALES = "backend/services/sales"
STOCK = "backend/services/stock"
BACKOFFICE = "frontend/backoffice"
CUSTOMER_PORTAL = "frontend/portals/customer"
UI = "frontend/packages/ui"
ALL_SERVICES = [SALES, STOCK]
ALL_PACKAGES = ["backend/models", "backend/shared/logging", "plugins/hello", "sdk"]
ALL_TYPESCRIPT = [BACKOFFICE, UI, CUSTOMER_PORTAL]
ALL_IMAGES: List[Dict[str, str]] = [
    {"folder": SALES, "name": "sales"},
    {"folder": BACKOFFICE, "name": "backoffice"},
    {"folder": CUSTOMER_PORTAL, "name": "portal-customer"},
]
REPO_FILES: Dict[str, str] = {
    f"{SALES}/pyproject.toml": "[project]\nname = 'sales'\n",
    f"{SALES}/Dockerfile": "FROM scratch\n",
    f"{STOCK}/pyproject.toml": "[project]\nname = 'stock'\n",
    "backend/services/_template/pyproject.toml": "[project]\nname = 'template'\n",
    "backend/services/.hidden/pyproject.toml": "[project]\nname = 'hidden'\n",
    "backend/services/README.md": "Services.\n",
    "backend/models/pyproject.toml": "[project]\nname = 'erp-models'\n",
    "backend/shared/logging/pyproject.toml": "[project]\nname = 'erp-logging'\n",
    "plugins/hello/pyproject.toml": "[project]\nname = 'hello'\n",
    "sdk/pyproject.toml": "[project]\nname = 'erp-sdk'\n",
    f"{BACKOFFICE}/package.json": "{}\n",
    f"{BACKOFFICE}/Dockerfile": "FROM scratch\n",
    f"{CUSTOMER_PORTAL}/package.json": "{}\n",
    f"{CUSTOMER_PORTAL}/Dockerfile": "FROM scratch\n",
    f"{UI}/package.json": "{}\n",
    f"{UI}/Dockerfile": "FROM scratch\n",
    "frontend/mobile/README.md": "Not started.\n",
}


def script_path() -> Path:
    return Path(__file__).resolve().parents[3] / ".github" / "scripts" / "detect_changes.py"


def write_repo(root: Path) -> None:
    for relative, content in REPO_FILES.items():
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")


def run_detector(root: Path, changed: List[str], *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(script_path()), "--root", str(root), *args],
        input="\n".join(changed) + "\n",
        capture_output=True,
        text=True,
        check=False,
    )


def outputs(result: subprocess.CompletedProcess[str]) -> Dict[str, str]:
    return dict(line.split("=", 1) for line in result.stdout.splitlines())


def compact(value: Union[List[str], List[Dict[str, str]]]) -> str:
    return json.dumps(value, separators=(",", ":"))


def nothing() -> Dict[str, str]:
    return {SERVICES_KEY: "[]", PACKAGES_KEY: "[]", TYPESCRIPT_KEY: "[]", REPOSITORY_KEY: "false", IMAGES_KEY: "[]"}


def everything() -> Dict[str, str]:
    return {
        SERVICES_KEY: compact(ALL_SERVICES),
        PACKAGES_KEY: compact(ALL_PACKAGES),
        TYPESCRIPT_KEY: compact(sorted(ALL_TYPESCRIPT)),
        REPOSITORY_KEY: "true",
        IMAGES_KEY: compact(sorted(ALL_IMAGES, key=lambda image: image["folder"])),
    }


def detect(root: Path, changed: List[str], *args: str) -> Dict[str, str]:
    write_repo(root)
    result = run_detector(root, changed, *args)
    assert result.returncode == 0, result.stderr
    return outputs(result)
