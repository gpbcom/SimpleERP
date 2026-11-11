from __future__ import annotations

import logging

import pytest

from harness_core.testing.git_sandbox import GitSandbox
from release_notes.models.catalogs.changelog_type_catalog import ChangelogTypeCatalog
from release_notes.service.fragments.fragment_reader import FragmentReader
from release_notes.storage.files.text_files import TextFiles


class TestFragmentReader:
    def reader(self, sandbox: GitSandbox, catalog: ChangelogTypeCatalog, logger: logging.Logger) -> FragmentReader:
        return FragmentReader(TextFiles(sandbox.root, logger), catalog, logger)

    def test_the_names_leave_out_the_readme(
        self, sandbox: GitSandbox, catalog: ChangelogTypeCatalog, logger: logging.Logger
    ) -> None:
        sandbox.write("changelog.d/GH-7.added.md", "Customers.\n")
        sandbox.write("changelog.d/notes.txt", "x\n")
        assert self.reader(sandbox, catalog, logger).names() == ["GH-7.added.md", "notes.txt"]

    def test_a_valid_fragment_is_read_with_its_non_empty_lines(
        self, sandbox: GitSandbox, catalog: ChangelogTypeCatalog, logger: logging.Logger
    ) -> None:
        sandbox.write("changelog.d/GH-7.added.md", "\nCustomers can be archived.\n\n- Their invoices stay.\n")
        fragment, problems = self.reader(sandbox, catalog, logger).read("GH-7.added.md")
        assert problems == []
        assert fragment is not None
        assert (fragment.ticket, fragment.type_name) == ("GH-7", "added")
        assert fragment.lines == ["Customers can be archived.", "- Their invoices stay."]

    @pytest.mark.parametrize(
        ("name", "text", "problem"),
        [
            ("notes.md", "x\n", "changelog.d/notes.md: not a fragment name, expected GH-<n>.<type>.md."),
            ("GH-7.added.txt", "x\n", "changelog.d/GH-7.added.txt: not a fragment name, expected GH-<n>.<type>.md."),
            (
                "GH-7.feature.md",
                "x\n",
                "changelog.d/GH-7.feature.md: unknown type feature, expected one of added, changed, deprecated,"
                " removed, fixed, security.",
            ),
            ("GH-7.added.md", "\n \n", "changelog.d/GH-7.added.md: 0 non-empty lines, expected 1 to 3."),
            ("GH-7.added.md", "a\nb\nc\nd\n", "changelog.d/GH-7.added.md: 4 non-empty lines, expected 1 to 3."),
        ],
    )
    def test_an_invalid_fragment_gives_its_problem(
        self,
        sandbox: GitSandbox,
        catalog: ChangelogTypeCatalog,
        logger: logging.Logger,
        name: str,
        text: str,
        problem: str,
    ) -> None:
        sandbox.write(f"changelog.d/{name}", text)
        assert self.reader(sandbox, catalog, logger).read(name) == (None, [problem])

    def test_read_all_gives_the_valid_fragments_and_the_problems(
        self, sandbox: GitSandbox, catalog: ChangelogTypeCatalog, logger: logging.Logger
    ) -> None:
        sandbox.write("changelog.d/GH-7.added.md", "Customers.\n")
        sandbox.write("changelog.d/GH-12.fixed.md", "Login.\n")
        sandbox.write("changelog.d/GH-8.oops.md", "x\n")
        fragments, problems = self.reader(sandbox, catalog, logger).read_all()
        assert [fragment.file_name for fragment in fragments] == ["GH-12.fixed.md", "GH-7.added.md"]
        assert len(problems) == 1
        assert problems[0].startswith("changelog.d/GH-8.oops.md: unknown type oops")
