🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 📐 [Design system](../README.md) › 🧵 [Patterns](README.md) ›
🧵 Bulk actions

# 🧵 Bulk actions

**Status:** 🔄 waiting for the owner

## Purpose

How users act on many records at once, safely: select, check what will change, confirm, and undo.

## When to use

When the same action applies to several records of a list: approve, assign, change a state, export, delete. Also when
the AI assistant prepares a change on many records
([D140](../../../06-decisions/f03-assistant/d140-assistant-confirms-changes.md)).

## Anatomy

```text
+------------------------------------------------------------------+
| 12 selected  [Select all 1,284]   [Assign...] [Change state...]  |
|------------------------------------------------------------------|
| [x] T-81 Visit   ...                                             |
| [x] T-82 Call    ...                                             |
+------------------------------------------------------------------+
           I will change 12 tasks: ... [Cancel] [Confirm 12 changes]
                         Done: 12 tasks moved.   [Undo]
```

1. **Selection:** a box per row of the [C-03 Data table](../components/c-03-data-table.md) and a select-all box.
2. **Bar:** the count and the actions allowed on all the selected records.
3. **Confirmation:** the full list of what will change
   ([D140](../../../06-decisions/f03-assistant/d140-assistant-confirms-changes.md)), as on
   [S-F3-02 Change confirmation card](../../../02-functional/f03-assistant/screens/03-act-through-the-assistant/s-f03-02-change-confirmation-card.md).
4. **Result:** done, partly done (each skipped record and why), with Undo
   ([D158](../../../06-decisions/f03-assistant/d158-assistant-undo.md)).

**Example images** (its variants and states, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| Variants and states | desktop | ![Variants and states, light](../images/bulk-actions-desktop-light.png) | ![Variants and states, dark](../images/bulk-actions-desktop-dark.png) |

## Behaviour

- (Proposed) The bar appears as soon as one record is selected; it lists only the actions the user may take on all of
  them.
- Every change shows the full list before it is made, and the button states the number
  ([D140](../../../06-decisions/f03-assistant/d140-assistant-confirms-changes.md)).
- Large requests run in batches of 100 by default, a setting with "No limit" as one choice
  ([D159](../../../06-decisions/f03-assistant/d159-assistant-batch-size.md)).
- Undo reverts the whole batch while no one has changed those records since; otherwise each record's history shows what
  to restore ([D158](../../../06-decisions/f03-assistant/d158-assistant-undo.md)).
- Records the rules refuse are skipped and listed with the reason ([error message pattern](error-messages.md)).

## Accessibility

- Each selection box is named after its record; the count is announced when it changes.
- The bar is reachable by keyboard right after the table (Proposed).
- The confirmation is a table with headers, as on
  [S-F3-02 Change confirmation card](../../../02-functional/f03-assistant/screens/03-act-through-the-assistant/s-f03-02-change-confirmation-card.md).

## Used in

[S-F3-02 Change confirmation card](../../../02-functional/f03-assistant/screens/03-act-through-the-assistant/s-f03-02-change-confirmation-card.md);
lists with a selection box ([C-03 Data table](../components/c-03-data-table.md)); the AI assistant's changes on many
records (UC-F3-03).

---

⬅️ [Search and filter](search-and-filter.md) · ⬆️ [Up](README.md) · ➡️ [Import export](import-export.md)
