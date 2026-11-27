from __future__ import annotations

# First-party imports
from tests.harness.checks.helpers import call

CHANGED = ["frontend/backoffice/src/app.test.ts", "frontend/backoffice/src/app.ts"]


class TestChecksFailingFiles:
    def test_a_path_printed_from_the_package_root_names_the_changed_file(self) -> None:
        out = "FAIL src/app.test.ts > the app > shows its title"
        found = call(f"checks.failing_files({out!r}, {CHANGED!r})")
        assert [name for name, _ in found] == [CHANGED[0]]

    def test_a_full_path_still_names_the_changed_file(self) -> None:
        out = f"{CHANGED[1]}:3:1: E501 line too long"
        found = call(f"checks.failing_files({out!r}, {CHANGED!r})")
        assert [name for name, _ in found] == [CHANGED[1]]

    def test_a_bare_file_name_names_nothing(self) -> None:
        out = "FAIL app.test.ts > the app"
        assert call(f"checks.failing_files({out!r}, {CHANGED!r})") == []
