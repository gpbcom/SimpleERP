from __future__ import annotations

from ticket_docs.service.checks.markdown_tables import MarkdownTables


class TestMarkdownTables:
    TEXT = (
        "# Title\n\n## Status\n\n| Step | Status | Note |\n|---|---|---|\n| 1 — a | ✅ Done | x \\| y |\n"
        "| 2 — b | ⬜ To do | — |\n\n### Detail\n\n| A | B |\n|---|---|\n| sub | row |\n\n## Other\n\ntext\n"
    )

    def test_a_section_stops_at_the_next_heading_unless_nested(self, tables: MarkdownTables) -> None:
        flat = tables.section(self.TEXT, "## Status")
        nested = tables.section(self.TEXT, "## Status", nested=True)
        assert flat is not None
        assert nested is not None
        assert "### Detail" not in flat
        assert "| sub | row |" in nested
        assert "## Other" not in nested
        assert tables.section(self.TEXT, "## Missing") is None

    def test_rows_and_header_of_a_section_table(self, tables: MarkdownTables) -> None:
        assert tables.header(self.TEXT, "## Status") == ["Step", "Status", "Note"]
        assert tables.rows(self.TEXT, "## Status") == [["1 — a", "✅ Done", "x \\| y"], ["2 — b", "⬜ To do", "—"]]
        assert tables.rows(self.TEXT, "## Missing") == []

    def test_prose_drops_code_and_comments_but_keeps_the_lines(self, tables: MarkdownTables) -> None:
        text = "a `<code>` b\n```text\n<fenced>\n```\n<!-- <comment>\nstill -->\nc <!-- x --> d\n"
        prose = tables.prose(text)
        assert prose.count("\n") == text.count("\n")
        assert "<code>" not in prose
        assert "<fenced>" not in prose
        assert "<comment>" not in prose
        assert "still" not in prose
        assert "c  d" in prose

    def test_cells_split_on_pipes_that_are_not_escaped(self, tables: MarkdownTables) -> None:
        assert tables.cells("| a | b \\| c | d |") == ["a", "b \\| c", "d"]
