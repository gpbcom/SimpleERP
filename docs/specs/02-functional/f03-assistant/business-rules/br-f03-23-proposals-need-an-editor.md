🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🤖 [F3 Assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F3-23 Proposals need an editor

# 📏 BR-F3-23 Proposals need an editor

**Status:** ✅ specified

## Statement

Any internal user can propose a new item or a fix to an item they can see; the proposal goes to the folder's editors,
who approve, change or decline it; the proposer is told; only approved content is used by the AI assistant.

## Why

Knowledge improves from use, but stays checked. See
[D176](../../../06-decisions/f03-assistant/d176-knowledge-editors.md).

## Examples

| Case | Result |
|---|---|
| An employee finds a wrong phone number in a procedure | "Propose a fix"; the editor approves; the item is updated |
| A proposal declined | The proposer gets the editor's reason |

## Applies to

- [UC-F3-07](../use-cases/07-manage-knowledge/uc-f03-07-manage-the-company-knowledge-base.md); every AI assistant answer
  using knowledge (UC-F3-01, UC-F3-05).
- [UC-F3-19 Turn unanswered topics into knowledge proposals](../use-cases/12-personal-cost-aware-and-learning/uc-f03-19-turn-unanswered-topics-into-knowledge-proposals.md)

## Exceptions

None.

## Configurable

Proposals can be turned off per folder.

## Open questions

None.

---

⬅️ [BR-F3-22 Out-of-date knowledge is flagged](br-f03-22-out-of-date-knowledge-is-flagged.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F3-24 Synced sources follow their origin](br-f03-24-synced-sources-follow-their-origin.md)
