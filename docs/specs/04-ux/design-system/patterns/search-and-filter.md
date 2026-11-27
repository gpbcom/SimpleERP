🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 📐 [Design system](../README.md) › 🧵 [Patterns](README.md) ›
🧵 Search and filter

# 🧵 Search and filter

**Status:** 🔄 waiting for the owner

## Purpose

How users find records: the global search of the top bar ([D47](../../../06-decisions/ux/d47-app-shell.md)) and the
search, filters and saved views of each list
([D109](../../../06-decisions/f02-no-code-configuration/d109-list-views.md)).

## When to use

Every list ([C-03 Data table](../components/c-03-data-table.md)) and the top bar of every screen. The AI assistant is
the other way to find, in plain words ([D49](../../../06-decisions/ux/d49-assistant-side-panel.md)).

## Anatomy

```text
[ View: My open quotes v ]  [ Search quotes...      ]  [Status: Sent, Draft x] [+ Filter]
3 filters  [Clear all]                                    48 results
```

1. **View:** the saved columns, filters, sort and grouping; shared views per role, personal views on top
   ([D109](../../../06-decisions/f02-no-code-configuration/d109-list-views.md)).
2. **Search:** words matched on the list's main fields.
3. **Filters:** chips with a field, a condition and values; [+ Filter] adds one.
4. **Result count** and **Clear all**.

**Example images** (its variants and states, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| Variants and states | desktop | ![Variants and states, light](../images/search-and-filter-desktop-light.png) | ![Variants and states, dark](../images/search-and-filter-desktop-dark.png) |

## Behaviour

- The search runs as the user types (Proposed: after 300 ms or on Enter) and on the server
  ([Performance](../../../05-non-functional/performance.md)).
- Results never include what the user may not see ([D12](../../../06-decisions/foundations/d12-permissions-model.md)).
- (Proposed) Filters show as chips that can be removed one by one; the result count updates.
- A user saves the current set as a personal view; a configurator shares it with roles, as on
  [S-F2-04 List view settings](../../../02-functional/f02-no-code-configuration/screens/01-configure-a-record-type/s-f02-04-list-view-settings.md).
- No result shows the [C-10 Empty state](../components/c-10-empty-state.md) with "Clear filters".
- The global search groups results by kind of record (Proposed).

## Accessibility

- The search field has a label; the result count is announced when it changes.
- Each filter chip's remove button is named ("Remove filter Status").
- The global search can be reached by a keyboard shortcut (Proposed: "/").

## Used in

[S-F2-04 List view settings](../../../02-functional/f02-no-code-configuration/screens/01-configure-a-record-type/s-f02-04-list-view-settings.md),
the top bar of every screen ([C-08 Navigation](../components/c-08-navigation.md)), and every list, for example
[S-F4-06 Meetings](../../../02-functional/f04-meetings/screens/04-find-and-reuse-meetings/s-f04-06-meetings.md) and
[S-F3-07 Knowledge base](../../../02-functional/f03-assistant/screens/07-manage-knowledge/s-f03-07-knowledge-base.md).

---

⬅️ [Approval](approval.md) · ⬆️ [Up](README.md) · ➡️ [Bulk actions](bulk-actions.md)
