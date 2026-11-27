🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏗️ [SC01 Construction](../../README.md) ›
🖥️ [Screens](../README.md) › 🗂️ [Views: Construction menu](README.md) › 🗂️ S-SC01-L06 Progress bills

# 🗂️ S-SC01-L06 Progress bills

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U22 Site manager](../../../../01-users/personas/u22-site-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U03 Sales](../../../../01-users/personas/u03-sales.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-SC01-06 Progress bill](../../data/e-sc01-06-progress-bill.md) the user may see: to find,
filter, total and act on many progress bills at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Construction › Progress bills, in the capability's menu (D495).
- **Workspaces:** 4 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "progress bills" offers this view.
- **AI assistant:** "show the progress bills that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Progress bills    Construction › Progress bills   [+ New]                                                    |
| [count] [Draft]   [chart: count by state]                                                                    |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| site              | [ ] SITE   STATE   PROGRESS PER LOT                                                      |
| state             | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Site | site | label | yes |
| State | state | badge: Draft, Sent, Paid | yes |
| Progress per lot | progress per lot | number, right-aligned | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| Site | site, number | the visible rows (D488) |
| State | Draft, Sent, Paid | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: progress bills link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Draft.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Open: Draft, Sent.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

- **Place:** site.
- **Layout:** a map, [C-17](../../../../04-ux/design-system/components/c-17-map.md).
- **Marker:** the site and the state.
- **Layers:** by state.
- **Who sees the switch:** the roles with the map right, the planner roles and U02 and U13 (BR-F1-32, D502); the others
  see the table with the place as a column.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New progress bill | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- progress per lot: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-SC01-06 Progress bill](../04-bill-and-subcontract/s-sc01-06-progress-bill.md).

The records also show on: [S-SC01-13 Public tenders](../01-win-the-work/s-sc01-13-public-tenders.md),
[S-SC01-14 Site margin](../04-bill-and-subcontract/s-sc01-14-site-margin.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 progress bills of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no progress bill the user may see yet, with the create action when allowed.
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
| Listed, U22, view Needs attention | desktop | ![Listed, U22, view Needs attention, light](../../images/lists/s-sc01-l06-progress-bills-u22-site-manager-desktop-light.png) | ![Listed, U22, view Needs attention, dark](../../images/lists/s-sc01-l06-progress-bills-u22-site-manager-desktop-dark.png) |
| Listed, U22, view Needs attention | phone | ![Listed, U22, view Needs attention, light](../../images/lists/s-sc01-l06-progress-bills-u22-site-manager-phone-light.png) | ![Listed, U22, view Needs attention, dark](../../images/lists/s-sc01-l06-progress-bills-u22-site-manager-phone-dark.png) |
| Listed, U05, view Open: Draft, Sent | desktop | ![Listed, U05, view Open: Draft, Sent, light](../../images/lists/s-sc01-l06-progress-bills-u05-accounting-desktop-light.png) | ![Listed, U05, view Open: Draft, Sent, dark](../../images/lists/s-sc01-l06-progress-bills-u05-accounting-desktop-dark.png) |
| Listed, U05, view Open: Draft, Sent | phone | ![Listed, U05, view Open: Draft, Sent, light](../../images/lists/s-sc01-l06-progress-bills-u05-accounting-phone-light.png) | ![Listed, U05, view Open: Draft, Sent, dark](../../images/lists/s-sc01-l06-progress-bills-u05-accounting-phone-dark.png) |
| Listed, U03, view Open: Draft, Sent | desktop | ![Listed, U03, view Open: Draft, Sent, light](../../images/lists/s-sc01-l06-progress-bills-u03-sales-desktop-light.png) | ![Listed, U03, view Open: Draft, Sent, dark](../../images/lists/s-sc01-l06-progress-bills-u03-sales-desktop-dark.png) |
| Listed, U03, view Open: Draft, Sent | phone | ![Listed, U03, view Open: Draft, Sent, light](../../images/lists/s-sc01-l06-progress-bills-u03-sales-phone-light.png) | ![Listed, U03, view Open: Draft, Sent, dark](../../images/lists/s-sc01-l06-progress-bills-u03-sales-phone-dark.png) |
| Listed, U13, view Needs attention | desktop | ![Listed, U13, view Needs attention, light](../../images/lists/s-sc01-l06-progress-bills-u13-owner-desktop-light.png) | ![Listed, U13, view Needs attention, dark](../../images/lists/s-sc01-l06-progress-bills-u13-owner-desktop-dark.png) |
| Listed, U13, view Needs attention | phone | ![Listed, U13, view Needs attention, light](../../images/lists/s-sc01-l06-progress-bills-u13-owner-phone-light.png) | ![Listed, U13, view Needs attention, dark](../../images/lists/s-sc01-l06-progress-bills-u13-owner-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md),
[C-17 Map](../../../../04-ux/design-system/components/c-17-map.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Construction › Progress bills](README.md) |
| Workspaces | [U22](../../../../04-ux/views/u22-site-manager/workspace.md), [U05](../../../../04-ux/views/u05-accounting/workspace.md), [U03](../../../../04-ux/views/u03-sales/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md) |
| Flows | [FL-SC01-01](../../flows/fl-sc01-01-win-the-work.md), [FL-SC01-04](../../flows/fl-sc01-04-bill-and-subcontract.md) |

## Open questions

None.

---

⬅️ [S-SC01-L05 Site diary entries](s-sc01-l05-site-diary-entries.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC01-L07 Subcontracts](s-sc01-l07-subcontracts.md)
