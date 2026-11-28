from __future__ import annotations

# Standard library imports
from pathlib import Path

# Third-party imports
import pytest

# First-party imports
from tests.ci.detect_changes.helpers import (
    BACKOFFICE,
    IMAGES_KEY,
    PACKAGES_KEY,
    REPOSITORY_KEY,
    SALES,
    SERVICES_KEY,
    TYPESCRIPT_KEY,
    compact,
    detect,
)


class TestBrunoChanges:
    @pytest.mark.parametrize("path", ["bruno/sales/tests/health.bru", "bruno/sales/requests/default/x.bru"])
    def test_a_change_in_a_services_bruno_folder_selects_that_service_and_the_repository_tests(
        self, tmp_path: Path, path: str
    ) -> None:
        selected = detect(tmp_path, [path])
        assert selected[SERVICES_KEY] == compact([SALES])
        assert selected[REPOSITORY_KEY] == "true"
        assert selected[IMAGES_KEY] == "[]"
        assert selected[PACKAGES_KEY] == "[]"
        assert selected[TYPESCRIPT_KEY] == "[]"

    @pytest.mark.parametrize("path", ["bruno/unknown/x.bru", "bruno/README.md"])
    def test_a_bruno_change_without_a_matching_service_selects_only_the_repository_tests(
        self, tmp_path: Path, path: str
    ) -> None:
        selected = detect(tmp_path, [path])
        assert selected[SERVICES_KEY] == "[]"
        assert selected[REPOSITORY_KEY] == "true"

    def test_a_bruno_change_beside_a_front_end_change_keeps_both_selections(self, tmp_path: Path) -> None:
        selected = detect(tmp_path, ["bruno/sales/tests/health.bru", f"{BACKOFFICE}/src/main.ts"])
        assert selected[SERVICES_KEY] == compact([SALES])
        assert selected[TYPESCRIPT_KEY] == compact([BACKOFFICE])
        assert selected[REPOSITORY_KEY] == "true"
