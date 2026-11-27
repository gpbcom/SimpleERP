from __future__ import annotations

# Standard library imports
import json
from pathlib import Path

# Third-party imports
import pytest

# First-party imports
from tests.ci.detect_changes.helpers import ALL_IMAGES, BACKOFFICE, IMAGES_KEY, SALES, UI, compact, detect


class TestImages:
    @pytest.mark.parametrize("path", [f"{SALES}/Dockerfile", f"{SALES}/.dockerignore", f"{SALES}/conf/app.yaml"])
    def test_any_change_in_a_service_folder_lists_its_image(self, tmp_path: Path, path: str) -> None:
        assert detect(tmp_path, [path])[IMAGES_KEY] == compact([{"folder": SALES, "name": "sales"}])

    def test_a_shared_front_end_package_builds_no_image_of_its_own(self, tmp_path: Path) -> None:
        images = json.loads(detect(tmp_path, [f"{UI}/Dockerfile"])[IMAGES_KEY])
        assert UI not in [image["folder"] for image in images]

    def test_two_folders_are_listed_sorted_and_once_each(self, tmp_path: Path) -> None:
        changed = [f"{BACKOFFICE}/a.ts", f"{SALES}/a.py", f"{BACKOFFICE}/b.ts"]
        assert detect(tmp_path, changed)[IMAGES_KEY] == compact(
            [{"folder": SALES, "name": "sales"}, {"folder": BACKOFFICE, "name": "backoffice"}]
        )

    def test_all_lists_every_image_folder_with_its_name(self, tmp_path: Path) -> None:
        images = json.loads(detect(tmp_path, [], "--all")[IMAGES_KEY])
        assert images == sorted(ALL_IMAGES, key=lambda image: image["folder"])
        assert all(set(image) == {"folder", "name"} for image in images)
