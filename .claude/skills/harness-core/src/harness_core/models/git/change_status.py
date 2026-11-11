from __future__ import annotations

# Standard library imports
from enum import StrEnum, unique


@unique
class ChangeStatus(StrEnum):
    """How git says a file changed, by the letter of ``git diff --name-status``.

    Attributes:
        ADDED: The file is new.
        COPIED: The file is a copy of another one.
        DELETED: The file was removed.
        MODIFIED: The file's content changed.
        RENAMED: The file was moved.
        TYPE_CHANGED: The file changed kind, such as a file becoming a link.
        UNTRACKED: The file is new and git does not track it yet (``??`` in ``git status --porcelain``).
    """

    ADDED = "A"
    COPIED = "C"
    DELETED = "D"
    MODIFIED = "M"
    RENAMED = "R"
    TYPE_CHANGED = "T"
    UNTRACKED = "?"
