🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🛡️ [Decisions: F1 Administration](README.md) ›
📜 D76 Role permissions as a matrix

# 📜 D76 Role permissions as a matrix

**Status:** ✅ decided

## Context

How permissions are edited in a role.

## Options

- A matrix per capability.
- Per screen.
- Advanced rules.

## Choice

A table with one row per capability and the columns See, Create, Change, Delete, Approve, Export, plus record rules per
row.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

Every capability declares its rows; plugins add theirs (T4).

## Related

- [UC-F1-06](../../02-functional/f01-administration/use-cases/04-edit-a-role/uc-f01-06-edit-a-role-and-its-record-rules.md)

---

⬅️ [D75 A leaver's personal data](d75-leavers-personal-data.md) · ⬆️ [Up](README.md) ·
➡️ [D77 Record rule kinds](d77-record-rule-kinds.md)
