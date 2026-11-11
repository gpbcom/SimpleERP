from __future__ import annotations

# Standard library imports
from enum import StrEnum, unique


@unique
class ReleaseNotesCommand(StrEnum):
    """The commands of ``release-notes``.

    Attributes:
        CHECK: Print every problem of the changelog, the fragments and the release note, nothing when DOC-3 holds.
        NEXT_VERSION: Suggest the next version from the last tag and the fragments.
        BUILD: Add the version's section to CHANGELOG.md and delete the fragments it used.
        RELEASE_BODY: Print the GitHub Release body of a version.
    """

    CHECK = "check"
    NEXT_VERSION = "next-version"
    BUILD = "build"
    RELEASE_BODY = "release-body"
