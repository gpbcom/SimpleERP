from __future__ import annotations

from pathlib import Path
from typing import Dict, FrozenSet, Tuple

ROOT = Path(__file__).resolve().parents[2]
# The source folder of every Python package of the repository (D438): the shared models, the shared libraries, the
# services, the plugins and the plugin SDK. Each holds one package, ``src/<package>/``.
SOURCE_GLOBS: Tuple[str, ...] = (
    "backend/models/src",
    "backend/shared/*/src",
    "backend/services/*/src",
    "plugins/*/src",
    "sdk/src",
)
# The shared models package: every file of it is in the ``models`` layer.
SHARED_MODELS_SOURCE = "backend/models/src"
# The source folders of the services: one service never imports another.
SERVICE_SOURCE_GLOB = "backend/services/*/src"
# The source folders of the shared libraries: they import the shared models and each other, never a service.
SHARED_LIBRARY_SOURCE_GLOB = "backend/shared/*/src"
# The source folders of the plugins and of the plugin SDK: they reach SimpleERP through the shared models only.
PLUGIN_AND_SDK_SOURCE_GLOBS: Tuple[str, ...] = ("plugins/*/src", "sdk/src")
# The name of the shared models package, which every package may import.
SHARED_MODELS_PACKAGE = "erp_models"
# The repository-level tests, and the ``tests/`` folder of every package.
TEST_GLOBS: Tuple[str, ...] = (
    "tests",
    "backend/models/tests",
    "backend/shared/*/tests",
    "backend/services/*/tests",
    "plugins/*/tests",
    "sdk/tests",
)
# Each layer, and the layers it may import. A layer may always import itself.
ALLOWED_IMPORTS: Dict[str, FrozenSet[str]] = {
    "api": frozenset({"api", "service", "models"}),
    "service": frozenset({"service", "storage", "models"}),
    "storage": frozenset({"storage", "models"}),
    "models": frozenset({"models"}),
}
# Names a third-party protocol owns, which may start with an underscore.
THIRD_PARTY_ATTRIBUTES: FrozenSet[str] = frozenset()
RUNNABLE_BASES = {"Runnable", "AsyncRunnable", "Command"}
# The two method banners of a class (AGENT.md, "File shape"); async methods follow the sync ones within each.
METHOD_BANNERS: Tuple[str, ...] = ("Internal Helpers Methods", "Publicly Exposed Methods")
# Every npm package of the front ends is named in this scope (AGENT.md, "Front ends").
FRONTEND_FOLDER = "frontend"
NPM_SCOPE = "@simpleerp"
FOLDER_LIMIT = 5
FOLDER_LIMIT_IGNORES = {"__init__.py", "conftest.py"}
