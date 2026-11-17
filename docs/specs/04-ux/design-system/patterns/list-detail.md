🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 📐 [Design system](../README.md) › 🧵 [Patterns](README.md) ›
🧵 List detail

# 🧵 List detail

**Status:** 🔄 waiting for the owner

## Purpose

How users find a record in a list and work on it: the most common shape of simple-ERP's screens.

## When to use

Every kind of record users browse: customers, quotes, invoices, employees, items, meetings. Not for a task done in steps
(use the [Wizard pattern](wizard.md)) or for a single settings page.

## Anatomy

```text
Desktop                                         Phone
+----------------------+-------------------+     +-------------------+
| Quotes   [+ New]     | QU-2026-0042      |     | Quotes      [+]   |
| [view v] [search]    | Durand SA  (Sent) |     | [search]          |
| QU-0042  Durand  ... | [Edit] [Send]     |     | QU-0042  Durand > |
| QU-0041  Martin  ... | Lines | History   |     | QU-0041  Martin > |
+----------------------+-------------------+     +-------------------+
```

1. **List:** a [C-03 Data table](../components/c-03-data-table.md) with its saved views, search and filters
   ([Search and filter pattern](search-and-filter.md)).
2. **Detail:** the record's page: its title and state, its actions, its fields
   ([C-02 Form field](../components/c-02-form-field.md)) and its parts in [C-07 Tabs](../components/c-07-tabs.md); the
   AI assistant knows which record is open ([D49](../../../06-decisions/ux/d49-assistant-side-panel.md)).

**Example images** (its variants and states, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| Variants and states | desktop | ![Variants and states, light](../images/list-detail-desktop-light.png) | ![Variants and states, dark](../images/list-detail-desktop-dark.png) |

## Behaviour

- Opening a row opens the record's page; (Proposed) on wide screens, from 1,600 px ([Layout grid](../layout-grid.md)),
  the detail can open next to the list.
- Back returns to the list with its view, filters, sort and scroll kept (Proposed).
- On a phone, the list shows cards and the detail is its own screen, as on
  [S-F2-04 List view settings](../../../02-functional/f02-no-code-configuration/screens/01-configure-a-record-type/s-f02-04-list-view-settings.md).
- Lists are paged on the server; the first page shows within 1 second
  ([Performance](../../../05-non-functional/performance.md)).
- The detail shows only what the user's permissions allow, as on every channel
  ([D12](../../../06-decisions/foundations/d12-permissions-model.md)).

## Accessibility

- The list is a table with headers, the detail has one level-1 heading and landmarks.
- Moving from list to detail moves the focus to the detail's heading; going back returns it to the row.

## Used in

Most screens of the capabilities and sectors, for example
[S-F9-09 Time off](../../../02-functional/f09-hr-and-projects/screens/03-time/s-f09-09-time-off.md),
[S-F4-06 Meetings](../../../02-functional/f04-meetings/screens/04-find-and-reuse-meetings/s-f04-06-meetings.md) and
[S-F3-07 Knowledge base](../../../02-functional/f03-assistant/screens/07-manage-knowledge/s-f03-07-knowledge-base.md).

---

⬆️ [Up](README.md) · ➡️ [Wizard](wizard.md)
