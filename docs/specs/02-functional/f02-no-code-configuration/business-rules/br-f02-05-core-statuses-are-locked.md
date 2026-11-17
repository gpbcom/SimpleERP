🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🔧 [F2 No-code configuration](../README.md) › 📏 [Business rules](README.md) › 📏 BR-F2-05 Core statuses are locked

# 📏 BR-F2-05 Core statuses are locked

**Status:** ✅ specified

## Statement

A status the core logic relies on cannot be removed, nor its meaning changed; its label and colour can
change; configurators add their own statuses around it.

## Why

Invoicing, stock and accounting depend on them. See
[D106](../../../06-decisions/f02-no-code-configuration/d106-core-statuses-locked.md).

## Examples

| Case | Result |
|---|---|
| Remove "Issued" from invoices | Refused |
| Add "Checked" before "Issued" | Allowed |
| Relabel "Issued" as "Sent to customer" | Allowed; its meaning stays |

## Applies to

- [UC-F2-02](../use-cases/01-configure-a-record-type/uc-f02-02-change-the-statuses-of-a-record-type.md)
- [UC-F2-17 Add a kanban, calendar, map, Gantt or timeline view](../use-cases/08-views-and-bookings/uc-f02-17-add-a-kanban-calendar-map-gantt-or-timeline-view.md)

## Exceptions

Statuses of F2's own new record types are never core.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F2-04 Computed fields are read-only](br-f02-04-computed-fields-are-read-only.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F2-06 Move records before removing a status](br-f02-06-move-records-before-removing-a-status.md)
