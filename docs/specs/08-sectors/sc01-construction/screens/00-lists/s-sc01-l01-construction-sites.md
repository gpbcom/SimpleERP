🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏗️ [SC01 Construction](../../README.md) ›
🖥️ [Screens](../README.md) › 🗂️ [Views: Construction menu](README.md) › 🗂️ S-SC01-L01 Construction sites

# 🗂️ S-SC01-L01 Construction sites

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U22 Site manager](../../../../01-users/personas/u22-site-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U03 Sales](../../../../01-users/personas/u03-sales.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U14 Field worker](../../../../01-users/personas/u14-field-worker.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U05, U09: their use cases only read these records, inside a screen of the use case, so they open
them from there (D493).

## Purpose

The aggregated list of every [E-SC01-01 Construction site](../../data/e-sc01-01-construction-site.md) the user may see:
to find, filter, total and act on many construction sites at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Construction › Construction sites, in the capability's menu (D495).
- **Workspaces:** 4 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "construction sites" offers this view.
- **AI assistant:** "show the construction sites that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Construction sites    Construction › Construction sites   [+ New]                                            |
| [count] [total budget]   [chart: count by state, budget stacked]                                             |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] REFERENCE   STATE   BUDGET                                                           |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Reference | reference | text | yes |
| State | state | badge: Planned, Running, Accepted, Closed | yes |
| Budget | budget | amount, right-aligned | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Planned, Running, Accepted, Closed | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: construction sites link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- Total of budget.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state, budget stacked (VR-8); the Chart button turns the filtered list into a chart the user can pin to their
home screen (C-09).

## Saved views

- All.
- Open: Planned, Running, Accepted.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

- **Place:** address.
- **Layout:** a map, [C-17](../../../../04-ux/design-system/components/c-17-map.md).
- **Marker:** the reference and the state.
- **Layers:** by state.
- **Who sees the switch:** the roles with the map right, the planner roles and U02 and U13 (BR-F1-32, D502); the others
  see the table with the place as a column.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New construction site | header | the personas whose roles may create it | the record's own page (Row opens) |
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

Open › goes to [S-SC01-01 Site](../01-win-the-work/s-sc01-01-site.md).

The records also show on: [S-SC01-14 Site margin](../04-bill-and-subcontract/s-sc01-14-site-margin.md),
[S-SC01-02 Quote by lots](../01-win-the-work/s-sc01-02-quote-by-lots.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 construction sites of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no construction site the user may see yet, with the create action when allowed.
- **Selected:** the bulk bar with the actions allowed on every selected row.
- **Error:** the query failed, with Retry.

On the map layout, Listed also shows the count of rows without a place.

## Responsive behaviour

On a phone the table keeps its columns and scrolls sideways, the facet panel becomes a drawer and the KPI strip stays
(VR-14, D491); the map takes the full width.

## Accessibility

The KPI strip, the facet panel, the toolbar and the table are named landmarks; the result count is announced when the
filters change; each chip has its remove button; the facet drawer returns the focus to its button. The table holds the
same rows as the map.

## Example images

Drawn in step S8 (36k) from this page: one row per persona and device for each state of the view, light and dark
([D490](../../../../06-decisions/ux/d490-example-images-for-every-persona-that-can-open-a-view.md),
[D500](../../../../06-decisions/ux/d500-images-live-in-the-specs-folders.md)).

| Shows | Device | Light | Dark |
|---|---|---|---|
| Listed, U22, view Open: Planned, Running, Accepted | desktop | ![Listed, U22, view Open: Planned, Running, Accepted, light](../../images/lists/s-sc01-l01-construction-sites-u22-site-manager-desktop-light.png) | ![Listed, U22, view Open: Planned, Running, Accepted, dark](../../images/lists/s-sc01-l01-construction-sites-u22-site-manager-desktop-dark.png) |
| Listed, U22, view Open: Planned, Running, Accepted | phone | ![Listed, U22, view Open: Planned, Running, Accepted, light](../../images/lists/s-sc01-l01-construction-sites-u22-site-manager-phone-light.png) | ![Listed, U22, view Open: Planned, Running, Accepted, dark](../../images/lists/s-sc01-l01-construction-sites-u22-site-manager-phone-dark.png) |
| Listed, U03, view Open: Planned, Running, Accepted | desktop | ![Listed, U03, view Open: Planned, Running, Accepted, light](../../images/lists/s-sc01-l01-construction-sites-u03-sales-desktop-light.png) | ![Listed, U03, view Open: Planned, Running, Accepted, dark](../../images/lists/s-sc01-l01-construction-sites-u03-sales-desktop-dark.png) |
| Listed, U03, view Open: Planned, Running, Accepted | phone | ![Listed, U03, view Open: Planned, Running, Accepted, light](../../images/lists/s-sc01-l01-construction-sites-u03-sales-phone-light.png) | ![Listed, U03, view Open: Planned, Running, Accepted, dark](../../images/lists/s-sc01-l01-construction-sites-u03-sales-phone-dark.png) |
| Listed, U13, view Open: Planned, Running, Accepted | desktop | ![Listed, U13, view Open: Planned, Running, Accepted, light](../../images/lists/s-sc01-l01-construction-sites-u13-owner-desktop-light.png) | ![Listed, U13, view Open: Planned, Running, Accepted, dark](../../images/lists/s-sc01-l01-construction-sites-u13-owner-desktop-dark.png) |
| Listed, U13, view Open: Planned, Running, Accepted | phone | ![Listed, U13, view Open: Planned, Running, Accepted, light](../../images/lists/s-sc01-l01-construction-sites-u13-owner-phone-light.png) | ![Listed, U13, view Open: Planned, Running, Accepted, dark](../../images/lists/s-sc01-l01-construction-sites-u13-owner-phone-dark.png) |
| Listed, U14, view Open: Planned, Running, Accepted | desktop | ![Listed, U14, view Open: Planned, Running, Accepted, light](../../images/lists/s-sc01-l01-construction-sites-u14-field-worker-desktop-light.png) | ![Listed, U14, view Open: Planned, Running, Accepted, dark](../../images/lists/s-sc01-l01-construction-sites-u14-field-worker-desktop-dark.png) |
| Listed, U14, view Open: Planned, Running, Accepted | phone | ![Listed, U14, view Open: Planned, Running, Accepted, light](../../images/lists/s-sc01-l01-construction-sites-u14-field-worker-phone-light.png) | ![Listed, U14, view Open: Planned, Running, Accepted, dark](../../images/lists/s-sc01-l01-construction-sites-u14-field-worker-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md),
[C-17 Map](../../../../04-ux/design-system/components/c-17-map.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Construction › Construction sites](README.md) |
| Workspaces | [U22](../../../../04-ux/views/u22-site-manager/workspace.md), [U03](../../../../04-ux/views/u03-sales/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md), [U14](../../../../04-ux/views/u14-field-worker/workspace.md) |
| Flows | [FL-SC01-01](../../flows/fl-sc01-01-win-the-work.md), [FL-SC01-02](../../flows/fl-sc01-02-prepare-the-site.md), [FL-SC01-03](../../flows/fl-sc01-03-run-the-site.md), [FL-SC01-04](../../flows/fl-sc01-04-bill-and-subcontract.md), [FL-SC01-05](../../flows/fl-sc01-05-hand-over-and-follow-up.md) |

## Open questions

None.

---

⬅️ [S-SC01-19 Renovation grants](../06-revision-developers-bim-and-grants/s-sc01-19-renovation-grants.md) ·
⬆️ [Up](README.md) · ➡️ [S-SC01-L02 Quote lots](s-sc01-l02-quote-lots.md)
