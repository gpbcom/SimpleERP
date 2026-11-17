🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
📦 [SC15 Wholesale and distribution](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Wholesale and distribution menu](README.md) › 🗂️ S-SC15-L11 Visit reports

# 🗂️ S-SC15-L11 Visit reports

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U42 Sales representative](../../../../01-users/personas/u42-sales-representative.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U03 Sales](../../../../01-users/personas/u03-sales.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-SC15-11 Visit report](../../data/e-sc15-11-visit-report.md) the user may see: to find,
filter, total and act on many visit reports at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Wholesale and distribution › Visit reports, in the capability's menu (D495).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "visit reports" offers this view.
- **AI assistant:** "show the visit reports that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Visit reports    Wholesale and distribution › Visit reports   [+ New]                                        |
| [count] [new this month]   [chart: count by state]                                                           |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] REP   STATE   ORDER   DATE                                                           |
| order             | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Rep | rep | link to the record | yes |
| State | state | badge: Active | yes |
| Order | order | label | yes |
| Date | date | link to the record | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Active | the visible rows (D488) |
| Order | text, order | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Visit reports of a chosen order, or of the orders that match a filter.
- From the other side: the orders that have visit reports, or none.

## KPI strip

- Count of the visible rows.
- New this month, by date.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New visit report | header | the personas whose roles may create it | the record's own page (Row opens) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- date: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-SC15-14 Visits](../05-sales-force-and-performance/s-sc15-14-visits.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 visit reports of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no visit report the user may see yet, with the create action when allowed.
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
| Listed, U42, view All | desktop | ![Listed, U42, view All, light](../../images/lists/s-sc15-l11-visit-reports-u42-sales-representative-desktop-light.png) | ![Listed, U42, view All, dark](../../images/lists/s-sc15-l11-visit-reports-u42-sales-representative-desktop-dark.png) |
| Listed, U42, view All | phone | ![Listed, U42, view All, light](../../images/lists/s-sc15-l11-visit-reports-u42-sales-representative-phone-light.png) | ![Listed, U42, view All, dark](../../images/lists/s-sc15-l11-visit-reports-u42-sales-representative-phone-dark.png) |
| Listed, U03, view All | desktop | ![Listed, U03, view All, light](../../images/lists/s-sc15-l11-visit-reports-u03-sales-desktop-light.png) | ![Listed, U03, view All, dark](../../images/lists/s-sc15-l11-visit-reports-u03-sales-desktop-dark.png) |
| Listed, U03, view All | phone | ![Listed, U03, view All, light](../../images/lists/s-sc15-l11-visit-reports-u03-sales-phone-light.png) | ![Listed, U03, view All, dark](../../images/lists/s-sc15-l11-visit-reports-u03-sales-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Wholesale and distribution › Visit reports](README.md) |
| Workspaces | [U42](../../../../04-ux/views/u42-sales-representative/workspace.md), [U03](../../../../04-ux/views/u03-sales/workspace.md) |
| Flows | [FL-SC15-05](../../flows/fl-sc15-05-sales-force-and-performance.md) |

## Open questions

None.

---

⬅️ [S-SC15-L10 Statistics returns](s-sc15-l10-statistics-returns.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC15-L13 Supplier scorecards](s-sc15-l13-supplier-scorecards.md)
