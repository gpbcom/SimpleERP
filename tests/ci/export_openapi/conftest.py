from __future__ import annotations

from pathlib import Path
from typing import ClassVar

import pytest


class ServiceWriter:
    FACTORY: ClassVar[str] = """\
from __future__ import annotations

from pathlib import Path
from typing import Dict


class Sample:
    def __init__(self, title: str) -> None:
        self.title = title

    def openapi(self) -> Dict[str, object]:
        return {"openapi": "3.1.0", "info": {"title": self.title, "version": "1"}, "paths": {}, "zeta": "caf\\u00e9"}


class AppFactory:
    @classmethod
    def create(cls) -> Sample:
        text = Path("conf/app.yaml").read_text(encoding="utf-8")
        return Sample(text.strip())
"""
    FAILING_FACTORY: ClassVar[str] = (
        "class AppFactory:\n    @classmethod\n    def create(cls) -> object:\n        raise RuntimeError('boom')\n"
    )

    def write(self, folder: Path, factory: str) -> Path:
        api = folder / "src" / "erp_sample" / "api"
        api.mkdir(parents=True)
        (folder / "src" / "erp_sample" / "__init__.py").write_text("", encoding="utf-8")
        (api / "__init__.py").write_text("", encoding="utf-8")
        (api / "app_factory.py").write_text(factory, encoding="utf-8")
        (folder / "conf").mkdir()
        (folder / "conf" / "app.yaml").write_text("Sample éè service\n", encoding="utf-8")
        return folder


@pytest.fixture
def writer() -> ServiceWriter:
    return ServiceWriter()


@pytest.fixture
def service(tmp_path: Path, writer: ServiceWriter) -> Path:
    return writer.write(tmp_path / "service", writer.FACTORY)


@pytest.fixture
def broken_import_service(tmp_path: Path, writer: ServiceWriter) -> Path:
    return writer.write(tmp_path / "broken_import", "raise RuntimeError('boom')\n")


@pytest.fixture
def failing_factory_service(tmp_path: Path, writer: ServiceWriter) -> Path:
    return writer.write(tmp_path / "failing_factory", writer.FAILING_FACTORY)


@pytest.fixture
def two_packages_service(tmp_path: Path, writer: ServiceWriter) -> Path:
    folder = writer.write(tmp_path / "two_packages", writer.FACTORY)
    (folder / "src" / "erp_other").mkdir()
    (folder / "src" / "erp_other" / "__init__.py").write_text("", encoding="utf-8")
    return folder


@pytest.fixture
def no_package_service(tmp_path: Path) -> Path:
    folder = tmp_path / "empty"
    (folder / "src").mkdir(parents=True)
    return folder


@pytest.fixture
def work_dir(tmp_path: Path) -> Path:
    folder = tmp_path / "work"
    folder.mkdir()
    return folder
