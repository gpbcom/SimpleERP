🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🤖 [F3 Assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F3-24 Synced sources follow their origin

# 📏 BR-F3-24 Synced sources follow their origin

**Status:** ✅ specified

## Statement

A synced folder (shared drive, website section) is re-read when its origin changes, checked at least every hour: new and
changed files are indexed, and files removed at the origin are removed from the knowledge base and the index.

## Why

The knowledge base must not keep what the origin removed. See
[D173](../../../06-decisions/f03-assistant/d173-knowledge-content.md).

## Examples

| Case | Result |
|---|---|
| A file is updated on the shared drive | The new version is used within the hour |
| A file is deleted at the origin | It is no longer found or used |
| The origin is unreachable | The last copy is kept and the editors are told |

## Applies to

- [UC-F3-07](../use-cases/07-manage-knowledge/uc-f03-07-manage-the-company-knowledge-base.md); every AI assistant answer
  using knowledge (UC-F3-01, UC-F3-05).

## Exceptions

None.

## Configurable

The check period, by the folder's editors.

## Open questions

None.

---

⬅️ [BR-F3-23 Proposals need an editor](br-f03-23-proposals-need-an-editor.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F3-25 Shared conversations continue as a copy](br-f03-25-shared-conversations-continue-as-a-copy.md)
