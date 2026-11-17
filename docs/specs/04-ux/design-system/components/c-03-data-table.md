🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 📐 [Design system](../README.md) › 🧩 [Components](README.md) ›
🧩 C-03 Data table

# 🧩 C-03 Data table

**Status:** 🔄 waiting for the owner

## Purpose

Shows many records in rows and columns, to scan, sort, filter, select and open them: the list of the
[List and detail pattern](../patterns/list-detail.md).

## Anatomy

```text
+------------------------------------------------------------------+
| View: [My open quotes v]  [Search...]  [Status v] [+ Filter]  [Export]|
|------------------------------------------------------------------|
| [ ] | NUMBER ^     | CUSTOMER     | AMOUNT    | STATUS           |
| [ ] | QU-2026-0042 | Durand SA    | 12,400.00 | (Sent)           |
| [ ] | QU-2026-0041 | Martin & Co  |  3,150.00 | (Draft)          |
|------------------------------------------------------------------|
| 1-50 of 1,284                                     [<] [1] [2] [>]  |
+------------------------------------------------------------------+
```

1. **Toolbar:** the saved view ([D109](../../../06-decisions/f02-no-code-configuration/d109-list-views.md)), search and
   filters ([Search and filter pattern](../patterns/search-and-filter.md)), actions such as Export.
2. **Header:** column names; a sortable column shows its order.
3. **Rows:** a selection box when bulk actions exist ([Bulk actions pattern](../patterns/bulk-actions.md)); codes in
   `font-code`; amounts right-aligned (Proposed) with tabular figures; states as badges with a word.
4. **Pager:** the range shown and the total; lists are paged on the server
   ([Performance](../../../05-non-functional/performance.md)).

**Example images** (its variants and states, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| Variants and states | desktop | ![Variants and states, light](../images/c-03-data-table-desktop-light.png) | ![Variants and states, dark](../images/c-03-data-table-desktop-dark.png) |

## Variants

- **Comfortable and compact:** the density of the role or the user
  ([D42](../../../06-decisions/ux/d42-density-per-role.md)).
- **Read-only table:** such as the changes of a confirmation card, as on
  [S-F3-02 Change confirmation card](../../../02-functional/f03-assistant/screens/03-act-through-the-assistant/s-f03-02-change-confirmation-card.md).
- **Editable grid:** (Proposed) cells are form fields ([C-02 Form field](c-02-form-field.md)), for timesheets and
  journal lines.
- **Phone:** rows become cards; the view chooses the fields shown on each card, as on
  [S-F2-04 List view settings](../../../02-functional/f02-no-code-configuration/screens/01-configure-a-record-type/s-f02-04-list-view-settings.md).

## States

| State | Look |
|---|---|
| Loading | (Proposed) Skeleton rows; the first page within 1 second ([Performance](../../../05-non-functional/performance.md)) |
| Empty | The [C-10 Empty state](c-10-empty-state.md) of the list |
| No result | (Proposed) The empty state with "Clear filters" |
| Row hover and focus | (Proposed) `color-surface-alt` background |
| Selected | (Proposed) The box ticked and the row tinted with `color-primary` at 8 % |
| Highlighted | A row that needs attention, with a word or icon, never colour alone (such as "TO REVIEW", [S-F3-07 Knowledge base](../../../02-functional/f03-assistant/screens/07-manage-knowledge/s-f03-07-knowledge-base.md)) |
| Error | A banner with the [error message pattern](../patterns/error-messages.md) |

## Tokens

`row-height` (48 or 32 px), `cell-padding` (12 or 6 px), `body-size` (16 or 14 px) ([Tokens](../tokens.md)); `font-body`
or `font-body-compact`, `font-code` for IDs, tabular figures for numbers
([Typography](../../visual-identity/typography.md)); `color-border` dividers, `color-surface-alt` stripes
([Colours](../../visual-identity/colours.md)); icons at 16 px in dense tables
([Iconography](../../visual-identity/iconography.md)); header in `font-caption`, upper case, `color-text-muted`
(Proposed: as drawn).

## Accessibility

- A real table with column headers; a sortable header is a button and states its order (`aria-sort`).
- Each selection box is named after its record ("Select QU-2026-0042").
- The pager and the result count are announced when they change.
- A chart's data is also given as a table, as on
  [S-F3-13 Assistant usage dashboard](../../../02-functional/f03-assistant/screens/01-ask-the-assistant/s-f03-13-assistant-usage-dashboard.md).

## Do and don't

- Do let users save the columns, filters and sort they need
  ([D109](../../../06-decisions/f02-no-code-configuration/d109-list-views.md)).
- Do show money with its currency and line up figures.
- Don't load a whole list in the browser: page, sort and filter on the server
  ([Performance](../../../05-non-functional/performance.md)).
- Don't show a state by colour alone.

## Used in

About 690 screens list it among their components, for example
[S-F2-04 List view settings](../../../02-functional/f02-no-code-configuration/screens/01-configure-a-record-type/s-f02-04-list-view-settings.md),
[S-F9-09 Time off](../../../02-functional/f09-hr-and-projects/screens/03-time/s-f09-09-time-off.md) and
[S-F13-14 Sick leave](../../../02-functional/f13-payroll/screens/04-events/s-f13-14-sick-leave.md).

## Open questions

None.

---

⬅️ [Form field](c-02-form-field.md) · ⬆️ [Up](README.md) · ➡️ [Card](c-04-card.md)
