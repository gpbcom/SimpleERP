🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💸 [F22 Unified platform cost management](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Unified platform cost management menu](README.md) › 🗂️ S-F22-L15 Compute machines

# 🗂️ S-F22-L15 Compute machines

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U48 Hosting engineer](../../../../01-users/personas/u48-hosting-engineer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F22-15 Compute machine](../../data/e-f22-15-compute-machine.md) the user may see: to
find, filter, total and act on many compute machines at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Unified platform cost management › Compute machines, in the capability's menu (D495).
- **Workspaces:** 4 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "compute machines" offers this view.
- **AI assistant:** "show the compute machines that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Compute machines    Unified platform cost management › Compute machines   [+ New]                            |
| [count] [total purchase price]   [chart: count by state, purchase price stacked]                             |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] NAME   STATE   PURCHASE PRICE   ELECTRICITY PRICE   COST PER HOUR                    |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Name | name | text | yes |
| State | state | badge: InService, Retired | yes |
| Purchase price | purchase price | amount, right-aligned | yes |
| Electricity price | electricity price | amount, right-aligned | yes |
| Cost per hour | cost per hour | amount, right-aligned | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | InService, Retired | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: compute machines link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- Total of purchase price.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state, purchase price stacked (VR-8); the Chart button turns the filtered list into a chart the user can pin to
their home screen (C-09).

## Saved views

- All.
- Open: InService.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New compute machine | header | the personas whose roles may create it | the record's own page (Row opens) |
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

Open › goes to [S-F22-01 Costs overview](../01-see-and-set-up/s-f22-01-costs-overview.md).

The records also show on: [S-F22-14 Allocation rules](../04-accounting/s-f22-14-allocation-rules.md),
[S-F22-17 Platform costs](../05-billing/s-f22-17-platform-costs.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 compute machines of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no compute machine the user may see yet, with the create action when allowed.
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
| Listed, U05, view Open: InService | desktop | ![Listed, U05, view Open: InService, light](../../images/lists/s-f22-l15-compute-machines-u05-accounting-desktop-light.png) | ![Listed, U05, view Open: InService, dark](../../images/lists/s-f22-l15-compute-machines-u05-accounting-desktop-dark.png) |
| Listed, U05, view Open: InService | phone | ![Listed, U05, view Open: InService, light](../../images/lists/s-f22-l15-compute-machines-u05-accounting-phone-light.png) | ![Listed, U05, view Open: InService, dark](../../images/lists/s-f22-l15-compute-machines-u05-accounting-phone-dark.png) |
| Listed, U48, view Open: InService | desktop | ![Listed, U48, view Open: InService, light](../../images/lists/s-f22-l15-compute-machines-u48-hosting-engineer-desktop-light.png) | ![Listed, U48, view Open: InService, dark](../../images/lists/s-f22-l15-compute-machines-u48-hosting-engineer-desktop-dark.png) |
| Listed, U48, view Open: InService | phone | ![Listed, U48, view Open: InService, light](../../images/lists/s-f22-l15-compute-machines-u48-hosting-engineer-phone-light.png) | ![Listed, U48, view Open: InService, dark](../../images/lists/s-f22-l15-compute-machines-u48-hosting-engineer-phone-dark.png) |
| Listed, U13, view Open: InService | desktop | ![Listed, U13, view Open: InService, light](../../images/lists/s-f22-l15-compute-machines-u13-owner-desktop-light.png) | ![Listed, U13, view Open: InService, dark](../../images/lists/s-f22-l15-compute-machines-u13-owner-desktop-dark.png) |
| Listed, U13, view Open: InService | phone | ![Listed, U13, view Open: InService, light](../../images/lists/s-f22-l15-compute-machines-u13-owner-phone-light.png) | ![Listed, U13, view Open: InService, dark](../../images/lists/s-f22-l15-compute-machines-u13-owner-phone-dark.png) |
| Listed, U07, view Open: InService | desktop | ![Listed, U07, view Open: InService, light](../../images/lists/s-f22-l15-compute-machines-u07-administrator-desktop-light.png) | ![Listed, U07, view Open: InService, dark](../../images/lists/s-f22-l15-compute-machines-u07-administrator-desktop-dark.png) |
| Listed, U07, view Open: InService | phone | ![Listed, U07, view Open: InService, light](../../images/lists/s-f22-l15-compute-machines-u07-administrator-phone-light.png) | ![Listed, U07, view Open: InService, dark](../../images/lists/s-f22-l15-compute-machines-u07-administrator-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Unified platform cost management › Compute machines](README.md) |
| Workspaces | [U05](../../../../04-ux/views/u05-accounting/workspace.md), [U48](../../../../04-ux/views/u48-hosting-engineer/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md), [U07](../../../../04-ux/views/u07-administrator/workspace.md) |
| Flows | [FL-F22-01](../../flows/fl-f22-01-see-and-set-up.md), [FL-F22-04](../../flows/fl-f22-04-accounting.md), [FL-F22-05](../../flows/fl-f22-05-billing.md) |

## Open questions

None.

---

⬅️ [S-F22-L14 Exchange rates](s-f22-l14-exchange-rates.md) · ⬆️ [Up](README.md) ·
➡️ [S-F22-L16 Savings recommendations](s-f22-l16-savings-recommendations.md)
