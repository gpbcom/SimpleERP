🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📒 [F8 Accounting](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: Accounting menu](README.md) ›
🗂️ S-F8-L13 Books

# 🗂️ S-F8-L13 Books

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U08 External accountant](../../../../01-users/personas/u08-external-accountant.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U36: their use cases only read these records, inside a screen of the use case, so they open them
from there (D493).

## Purpose

The aggregated list of every [E-F8-13 Book](../../data/e-f08-13-book.md) the user may see: to find, filter, total and
act on many books at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Accounting › Books, in the capability's menu (D495).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "books" offers this view.
- **AI assistant:** "show the books that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Books    Accounting › Books   [+ New]                                                                        |
| [count]   [chart: count by state]                                                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] FRAMEWORK   STATE                                                                    |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Framework | framework | label | yes |
| State | state | badge: Closed, Refused | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Closed, Refused | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: books link to no other record type in their fields.

## KPI strip

- Count of the visible rows.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Open: Refused.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New book | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

None: no field is editable in a cell.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F8-15 Books](../06-benchmark-additions/s-f08-15-books.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 books of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no book the user may see yet, with the create action when allowed.
- **Selected:** the bulk bar with the actions allowed on every selected row.
- **Error:** the query failed, with Retry.

## Responsive behaviour

On a phone the table keeps its columns and scrolls sideways, the facet panel becomes a drawer and the KPI strip stays
(VR-14, D491).

## Accessibility

The KPI strip, the facet panel, the toolbar and the table are named landmarks; the result count is announced when the
filters change; each chip has its remove button; the facet drawer returns the focus to its button.

## Example images

Drawn in step S8 (36k) from this page: one row per persona and device for each state of the view, light and dark
([D490](../../../../06-decisions/ux/d490-example-images-for-every-persona-that-can-open-a-view.md),
[D500](../../../../06-decisions/ux/d500-images-live-in-the-specs-folders.md)).

| Shows | Device | Light | Dark |
|---|---|---|---|
| Listed, U05, view Open: Refused | desktop | ![Listed, U05, view Open: Refused, light](../../images/lists/s-f08-l13-books-u05-accounting-desktop-light.png) | ![Listed, U05, view Open: Refused, dark](../../images/lists/s-f08-l13-books-u05-accounting-desktop-dark.png) |
| Listed, U05, view Open: Refused | phone | ![Listed, U05, view Open: Refused, light](../../images/lists/s-f08-l13-books-u05-accounting-phone-light.png) | ![Listed, U05, view Open: Refused, dark](../../images/lists/s-f08-l13-books-u05-accounting-phone-dark.png) |
| Listed, U08, view Open: Refused | desktop | ![Listed, U08, view Open: Refused, light](../../images/lists/s-f08-l13-books-u08-external-accountant-desktop-light.png) | ![Listed, U08, view Open: Refused, dark](../../images/lists/s-f08-l13-books-u08-external-accountant-desktop-dark.png) |
| Listed, U08, view Open: Refused | phone | ![Listed, U08, view Open: Refused, light](../../images/lists/s-f08-l13-books-u08-external-accountant-phone-light.png) | ![Listed, U08, view Open: Refused, dark](../../images/lists/s-f08-l13-books-u08-external-accountant-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Accounting › Books](README.md) |
| Workspaces | [U05](../../../../04-ux/views/u05-accounting/workspace.md), [U08](../../../../04-ux/views/u08-external-accountant/workspace.md) |
| Flows | [FL-F8-06](../../flows/fl-f08-06-benchmark-additions.md), [FL-SC08-06](../../../../08-sectors/sc08-non-profit/flows/fl-sc08-06-accounts-and-data.md), [FL-SC09-05](../../../../08-sectors/sc09-health-practices/flows/fl-sc09-05-practice-organisation.md), [FL-SC10-05](../../../../08-sectors/sc10-real-estate/flows/fl-sc10-05-co-ownership.md) |

## Open questions

None.

---

⬅️ [S-F8-L12 Filing partners](s-f08-l12-filing-partners.md) · ⬆️ [Up](README.md) ·
➡️ [S-F8-L14 Revenue schedules](s-f08-l14-revenue-schedules.md)
