"""The paths, changelogs and release notes the tests share."""

from __future__ import annotations

from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parents[1]
REPOSITORY_ROOT = SKILL_DIR.parents[2]
TYPES_FILE = SKILL_DIR / "conf" / "changelog-types.yaml"
GITHUB_API_FILE = SKILL_DIR / "conf" / "github-api.yaml"
GITHUB_FILE = SKILL_DIR.parent / "ticket-docs" / "conf" / "github.yaml"
TEMPLATES = SKILL_DIR / "templates"
FEATURE_BRANCH = "feature/GH-7-add-customers"
ISSUES = "https://github.com/gpbcom/simple-erp/issues"
MARKER = "<!-- release-note -->"


def changelog(*sections: str) -> str:
    """The CHANGELOG.md template, followed by released sections."""
    text = (TEMPLATES / "CHANGELOG.md").read_text(encoding="utf-8")
    return text + "".join(f"\n{section.strip()}\n" for section in sections)


def release_note(key: str = "GH-7", upgrade: str = "Nothing to do.") -> str:
    """A release note filled from the template, nothing left to replace."""
    return (
        f"{MARKER}\n# {key}: Customers\n\n**For:** sales staff · **Type:** added · **Version:** next release\n\n"
        "## What is new\n\nCustomers can be archived from their page.\n\n"
        "## How to use it\n\nOpen a customer and choose `Archive <name>`.\n\n"
        f"## Upgrade notes\n\n{upgrade}\n\n## Known limits\n\nNone.\n\n"
        f"## Links\n\n- Issue: <{ISSUES}/7>\n- Pull request: <https://github.com/gpbcom/simple-erp/pull/9>\n"
        "- Evidence: <https://github.com/gpbcom/simple-erp/releases/tag/evidence-GH-7>\n"
    )
