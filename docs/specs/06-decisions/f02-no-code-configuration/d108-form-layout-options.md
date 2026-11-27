🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🔧 [Decisions: F2 No-code configuration](README.md) ›
📜 D108 Form layout options

# 📜 D108 Form layout options

**Status:** ✅ decided

## Context

What a configurator can change in a form.

## Options

- Sections and order.
- Show or hide per condition.
- Read-only per status.
- One layout per role.

## Choice

All four: sections, tabs and order; showing a field or section only when another field has a value; locking fields once
the record reaches a status; a different layout of the same form per role.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

Layouts are presentation; data stays protected by permissions (BR-F2-07).

## Related

- [UC-F2-03](../../02-functional/f02-no-code-configuration/use-cases/01-configure-a-record-type/uc-f02-03-arrange-a-form.md)

---

⬅️ [D107 Move records before removing a status](d107-move-records-before-removing.md) · ⬆️ [Up](README.md) ·
➡️ [D109 Shared and personal list views](d109-list-views.md)
