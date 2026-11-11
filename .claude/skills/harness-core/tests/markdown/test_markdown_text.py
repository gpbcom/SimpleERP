from __future__ import annotations

from typing import List

import pytest

from harness_core.markdown.markdown_text import MarkdownText

DOCUMENT = """# Title

See [the API](api.md#routes) and ![a picture](img/a.png "A title").
Also [a site](https://example.com) and [spaced](<my file.md>).

`[not a link](inline.md)` stays code.

```bash
echo "[not a link](fenced.md)"
```

## Upgrade notes

Run the migration.

### Details

Keep this.

## Known limits

None.

```mermaid
flowchart LR
    A --> B
```
"""


class TestMarkdownText:
    def test_prose_blanks_code_and_keeps_the_line_numbers(self) -> None:
        prose = MarkdownText.prose(DOCUMENT)
        assert len(prose.splitlines()) == len(DOCUMENT.splitlines())
        assert "inline.md" not in prose
        assert "fenced.md" not in prose
        assert "stays code." in prose

    def test_links_give_their_line_and_target_outside_code(self) -> None:
        assert MarkdownText.links(DOCUMENT) == [
            (3, "api.md#routes"),
            (3, "img/a.png"),
            (4, "https://example.com"),
            (4, "my file.md"),
        ]

    def test_fenced_blocks_of_one_language(self) -> None:
        assert MarkdownText.fenced_blocks(DOCUMENT, "mermaid") == [(24, "flowchart LR\n    A --> B\n")]
        assert MarkdownText.fenced_blocks(DOCUMENT, "bash") == [(8, 'echo "[not a link](fenced.md)"\n')]

    def test_a_section_runs_to_the_next_heading_of_its_level(self) -> None:
        section = MarkdownText.section(DOCUMENT, "Upgrade notes")
        assert section is not None
        assert section.strip().splitlines() == ["Run the migration.", "", "### Details", "", "Keep this."]
        assert (MarkdownText.section(DOCUMENT, "known LIMITS") or "").strip().splitlines()[0] == "None."
        assert MarkdownText.section(DOCUMENT, "Missing") is None

    @pytest.mark.parametrize(
        ("level", "expected"),
        [(1, ["Title"]), (2, ["Upgrade notes", "Known limits"]), (3, ["Details"])],
    )
    def test_headings_of_one_level(self, level: int, expected: List[str]) -> None:
        assert MarkdownText.headings(DOCUMENT, level) == expected

    def test_a_heading_inside_code_is_not_a_heading(self) -> None:
        assert MarkdownText.headings("```\n## Not one\n```\n## Real\n", 2) == ["Real"]
