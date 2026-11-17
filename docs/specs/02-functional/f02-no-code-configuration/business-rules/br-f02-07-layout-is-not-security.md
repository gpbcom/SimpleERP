🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🔧 [F2 No-code configuration](../README.md) › 📏 [Business rules](README.md) › 📏 BR-F2-07 Layout is not security

# 📏 BR-F2-07 Layout is not security

**Status:** ✅ specified

## Statement

Hiding a field through a role's layout or a condition only changes what the form shows; who may read or
change the field is set by permissions (D76, BR-F2-03), on every channel.

## Why

A field hidden by layout would still be readable through the API, the AI assistant or an export if layout were mistaken
for security. See [D108](../../../06-decisions/f02-no-code-configuration/d108-form-layout-options.md).

## Examples

| Setting | Effect |
|---|---|
| "Salary" left out of the field worker's layout | Not shown on their form; still readable through the API if their role may read it |
| "Salary" limited to HR (BR-F2-03) | Readable by HR only, on every channel |

## Applies to

- [UC-F2-03](../use-cases/01-configure-a-record-type/uc-f02-03-arrange-a-form.md)
- [UC-F2-17 Add a kanban, calendar, map, Gantt or timeline view](../use-cases/08-views-and-bookings/uc-f02-17-add-a-kanban-calendar-map-gantt-or-timeline-view.md)
- [UC-F2-27 Set field-level rights and validation rules](../use-cases/11-rights-translations-and-approvals/uc-f02-27-set-field-level-rights-and-validation-rules.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F2-06 Move records before removing a status](br-f02-06-move-records-before-removing-a-status.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F2-08 Read-only per status on every channel](br-f02-08-read-only-per-status-on-every-channel.md)
