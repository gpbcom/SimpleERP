from __future__ import annotations

import logging
from typing import List

import pytest

from project_docs.models.catalogs.doc_map import DocMap
from project_docs.models.catalogs.doc_map_rule import DocMapRule
from project_docs.service.mapping.chapter_mapper import ChapterMapper


class TestChapterMapper:
    @pytest.mark.parametrize(
        ("path", "chapters"),
        [
            (
                "services/billing/src/billing/api/routes.py",
                ["docs/technical/services/billing.md", "docs/technical/api.md"],
            ),
            (
                "services/billing/src/billing/storage/invoices.py",
                ["docs/technical/services/billing.md", "docs/technical/data-model.md"],
            ),
            ("services/billing/Dockerfile", ["docs/technical/services/billing.md"]),
            ("frontends/web/src/App.vue", ["docs/technical/frontends/web.md", "docs/functional/README.md"]),
            ("packages/logs/src/x.py", ["docs/technical/architecture.md"]),
            ("src/api/cli/main.py", ["docs/technical/api.md", "README.md"]),
            ("src/service/customers/customer_service.py", ["docs/technical/architecture.md"]),
            ("conf/logger.yaml", ["docs/technical/configuration.md"]),
            (".github/workflows/ci.yml", ["docs/technical/ci-cd-and-stages.md"]),
            ("compose.e2e.yaml", ["docs/technical/ci-cd-and-stages.md"]),
            ("frontends/web/e2e/login.spec.ts", ["docs/technical/frontends/web.md", "docs/functional/README.md"]),
            ("tests/conventions/test_layers.py", ["docs/technical/tests-and-traceability.md"]),
            ("uv.lock", ["README.md", "docs/technical/architecture.md"]),
            ("docs/specs/flowcharts/customer.mmd", ["docs/functional/README.md"]),
            (".claude/skills/project-docs/conf/doc-map.yaml", ["docs/technical/development-process.md"]),
            ("AGENT.md", ["docs/technical/development-process.md"]),
            ("CHANGELOG.md", []),
            ("changelog.d/GH-7.added.md", []),
            ("docs/technical/api.md", []),
            ("LICENSE", ["README.md"]),
        ],
    )
    def test_each_path_takes_the_chapters_of_its_first_rule(
        self, doc_map: DocMap, logger: logging.Logger, path: str, chapters: List[str]
    ) -> None:
        assert ChapterMapper(doc_map, logger).chapters(path) == chapters

    def test_the_paths_are_gathered_under_each_chapter(self, doc_map: DocMap, logger: logging.Logger) -> None:
        mapping = ChapterMapper(doc_map, logger).map(
            ["src/api/cli/main.py", "LICENSE", "CHANGELOG.md", "src/api/routes.py", "conf/app.yaml"]
        )
        assert mapping == {
            "README.md": ["LICENSE", "src/api/cli/main.py", "src/api/routes.py"],
            "docs/technical/api.md": ["src/api/cli/main.py", "src/api/routes.py"],
            "docs/technical/configuration.md": ["conf/app.yaml"],
        }
        assert list(mapping) == sorted(mapping)

    def test_no_path_maps_to_no_chapter(self, doc_map: DocMap, logger: logging.Logger) -> None:
        assert ChapterMapper(doc_map, logger).map([]) == {}

    def test_a_pattern_is_a_whole_path_glob_with_its_special_characters_escaped(self, logger: logging.Logger) -> None:
        doc_map = DocMap(
            rules=[
                DocMapRule(paths=["a+b/[x].md"], chapters=["docs/one.md"]),
                DocMapRule(paths=["src/?.py"], chapters=["docs/two.md"]),
            ],
            always=[],
            per_service="docs/technical/services/{service}.md",
            per_frontend="docs/technical/frontends/{frontend}.md",
        )
        mapper = ChapterMapper(doc_map, logger)
        assert mapper.chapters("a+b/[x].md") == ["docs/one.md"]
        assert mapper.chapters("src/a.py") == ["docs/two.md"]
        assert mapper.chapters("src/ab.py") == []
        assert mapper.chapters("x/a+b/[x].md") == []
