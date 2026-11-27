🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🔧 [F2 No-code configuration](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F2-02 Custom data follows permissions

# 📏 BR-F2-02 Custom data follows permissions

**Status:** ✅ specified

## Statement

Custom fields and new record types appear in the API, webhooks, the AI assistant, the RAG index, MCP and A2A, under the
same permissions as the screens.

## Why

Every channel obeys the same permissions (D12). See
[D100](../../../06-decisions/f02-no-code-configuration/d100-custom-data-exposure.md).

## Examples

| Case | Result |
|---|---|
| A "Vehicles" record type | Listed in the API and to the AI assistant for the roles that may see it |
| A custom field on employees, HR only | Never in a webhook or an answer to a non-HR user |
| A spreadsheet export of quotes | Standard fields only (D100) |

## Applies to

Every F2 use case; T5, T6, T8.

- [UC-F2-17 Add a kanban, calendar, map, Gantt or timeline view](../use-cases/08-views-and-bookings/uc-f02-17-add-a-kanban-calendar-map-gantt-or-timeline-view.md)

- [UC-F2-20 Expose a record type on a portal](../use-cases/09-portals-and-offline-forms/uc-f02-20-expose-a-record-type-on-a-portal.md)

- [UC-F2-21 Make a phone form work offline](../use-cases/09-portals-and-offline-forms/uc-f02-21-make-a-phone-form-work-offline.md)

## Exceptions

None.

## Configurable

Through roles (F1), like any record.

## Open questions

None.

---

⬅️ [BR-F2-01 Archive, never delete](br-f02-01-archive-never-delete.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F2-03 Field visibility per role](br-f02-03-field-visibility-per-role.md)
