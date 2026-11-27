🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🛡️ [F1 Administration](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F1-12 Record rule kinds

# 📏 BR-F1-12 Record rule kinds

**Status:** ✅ specified

## Statement

A role's row can limit its records to the user's own, the user's site, the user's team, and set amount limits on Approve
(and Create).

## Why

The four kinds cover the needs of the eight example companies. See
[D77](../../../06-decisions/f01-administration/d77-record-rule-kinds.md).

## Examples

| Rule on a row | A user sees or may act on |
|---|---|
| Own records only | What they created or are assigned to |
| Own site only | The records of their site |
| Own team | What the people they manage own, and their own |
| Amount limit 2,000 EUR on Approve | Approve purchases up to 2,000 EUR; above goes to the next approver |

## Applies to

- [UC-F1-06](../use-cases/04-edit-a-role/uc-f01-06-edit-a-role-and-its-record-rules.md); every permission check (T2) on
  every channel (D12).

## Exceptions

A record a user is explicitly shared on is visible whatever the rule.

## Configurable

Yes: per role and per row.

## Open questions

None.

---

⬅️ [BR-F1-11 Ready-made roles are copied](br-f01-11-ready-made-roles-are-copied.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F1-13 External data warning](br-f01-13-external-data-warning.md)
