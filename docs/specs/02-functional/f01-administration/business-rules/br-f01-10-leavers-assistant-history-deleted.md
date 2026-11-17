🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🛡️ [F1 Administration](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F1-10 A leaver's AI assistant history is deleted

# 📏 BR-F1-10 A leaver's AI assistant history is deleted

**Status:** ✅ specified

## Statement

When a user is deactivated, their private AI assistant history is deleted; their business records stay, with their name
in the history.

## Why

The AI assistant history is personal; business records are the company's. See
[D75](../../../06-decisions/f01-administration/d75-leavers-personal-data.md).

Legal values from the France country pack:
[CR-FR-052 Personal data kept no longer than needed](../../../10-country-packs/france/data-protection/cr-fr-052-storage-limitation.md).

## Examples

| Data | At deactivation |
|---|---|
| Quotes Marie wrote | Kept; history says "by Marie Dupont" |
| Marie's questions to the AI assistant | Deleted |
| A meeting recording where Marie speaks | Follows the meetings' retention rule (F4) |

## Applies to

- [UC-F1-05](../use-cases/03-user-lifecycle/uc-f01-05-deactivate-and-offboard-a-user.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F1-09 Dated changes](br-f01-09-dated-changes.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F1-11 Ready-made roles are copied](br-f01-11-ready-made-roles-are-copied.md)
