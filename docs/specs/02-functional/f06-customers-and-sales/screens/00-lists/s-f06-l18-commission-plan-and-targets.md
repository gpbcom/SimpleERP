🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛒 [F6 Customers and sales](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Customers and sales menu](README.md) › 🗂️ S-F6-L18 Commission plan and targets

# 🗂️ S-F6-L18 Commission plan and targets

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U42 Sales representative](../../../../01-users/personas/u42-sales-representative.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U23 Store manager](../../../../01-users/personas/u23-store-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U03 Sales](../../../../01-users/personas/u03-sales.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U51, U52: their use cases only read these records, inside a screen of the use case, so they open
them from there (D493).

## Purpose

The aggregated list of every [E-F6-18 Commission plan and target](../../data/e-f06-18-commission-plan-and-target.md) the
user may see: to find, filter, total and act on many commission plan and targets at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Customers and sales › Commission plan and targets, in the capability's menu (D495).
- **Workspaces:** 6 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "commission plan and targets" offers this view.
- **AI assistant:** "show the commission plan and targets that need attention" opens it with the filter as editable
  chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Commission plan and targets    Customers and sales › Commission plan and targets   [+ New]                   |
| [count] [Draft] [new this month]   [chart: count by state]                                                   |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] PERIOD   STATE   RATES AND TIERS                                                     |
| rates and tiers   | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Period | period | date | yes |
| State | state | badge: Draft, Active, Closed | yes |
| Rates and tiers | rates and tiers | text | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Draft, Active, Closed | the visible rows (D488) |
| Rates and tiers | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: commission plan and targets link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Draft.
- New this month, by period.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Open: Draft, Active.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New commission plan and target | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- rates and tiers: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to
[S-F6-21 Targets and commissions](../09-sell-on-the-road-and-steer-sales/s-f06-21-targets-and-commissions.md).

The records also show on: [S-F6-22 Sales reports](../09-sell-on-the-road-and-steer-sales/s-f06-22-sales-reports.md),
[S-SC11-17 Partners](../../../../08-sectors/sc11-professional-firms/screens/06-firm-management/s-sc11-17-partners.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 commission plan and targets of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no commission plan and target the user may see yet, with the create action when allowed.
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
| Listed, U13, view Needs attention | desktop | ![Listed, U13, view Needs attention, light](../../images/lists/s-f06-l18-commission-plan-and-targets-u13-owner-desktop-light.png) | ![Listed, U13, view Needs attention, dark](../../images/lists/s-f06-l18-commission-plan-and-targets-u13-owner-desktop-dark.png) |
| Listed, U13, view Needs attention | phone | ![Listed, U13, view Needs attention, light](../../images/lists/s-f06-l18-commission-plan-and-targets-u13-owner-phone-light.png) | ![Listed, U13, view Needs attention, dark](../../images/lists/s-f06-l18-commission-plan-and-targets-u13-owner-phone-dark.png) |
| Listed, U02, view Needs attention | desktop | ![Listed, U02, view Needs attention, light](../../images/lists/s-f06-l18-commission-plan-and-targets-u02-manager-desktop-light.png) | ![Listed, U02, view Needs attention, dark](../../images/lists/s-f06-l18-commission-plan-and-targets-u02-manager-desktop-dark.png) |
| Listed, U02, view Needs attention | phone | ![Listed, U02, view Needs attention, light](../../images/lists/s-f06-l18-commission-plan-and-targets-u02-manager-phone-light.png) | ![Listed, U02, view Needs attention, dark](../../images/lists/s-f06-l18-commission-plan-and-targets-u02-manager-phone-dark.png) |
| Listed, U42, view Open: Draft, Active | desktop | ![Listed, U42, view Open: Draft, Active, light](../../images/lists/s-f06-l18-commission-plan-and-targets-u42-sales-representative-desktop-light.png) | ![Listed, U42, view Open: Draft, Active, dark](../../images/lists/s-f06-l18-commission-plan-and-targets-u42-sales-representative-desktop-dark.png) |
| Listed, U42, view Open: Draft, Active | phone | ![Listed, U42, view Open: Draft, Active, light](../../images/lists/s-f06-l18-commission-plan-and-targets-u42-sales-representative-phone-light.png) | ![Listed, U42, view Open: Draft, Active, dark](../../images/lists/s-f06-l18-commission-plan-and-targets-u42-sales-representative-phone-dark.png) |
| Listed, U23, view Needs attention | desktop | ![Listed, U23, view Needs attention, light](../../images/lists/s-f06-l18-commission-plan-and-targets-u23-store-manager-desktop-light.png) | ![Listed, U23, view Needs attention, dark](../../images/lists/s-f06-l18-commission-plan-and-targets-u23-store-manager-desktop-dark.png) |
| Listed, U23, view Needs attention | phone | ![Listed, U23, view Needs attention, light](../../images/lists/s-f06-l18-commission-plan-and-targets-u23-store-manager-phone-light.png) | ![Listed, U23, view Needs attention, dark](../../images/lists/s-f06-l18-commission-plan-and-targets-u23-store-manager-phone-dark.png) |
| Listed, U05, view Open: Draft, Active | desktop | ![Listed, U05, view Open: Draft, Active, light](../../images/lists/s-f06-l18-commission-plan-and-targets-u05-accounting-desktop-light.png) | ![Listed, U05, view Open: Draft, Active, dark](../../images/lists/s-f06-l18-commission-plan-and-targets-u05-accounting-desktop-dark.png) |
| Listed, U05, view Open: Draft, Active | phone | ![Listed, U05, view Open: Draft, Active, light](../../images/lists/s-f06-l18-commission-plan-and-targets-u05-accounting-phone-light.png) | ![Listed, U05, view Open: Draft, Active, dark](../../images/lists/s-f06-l18-commission-plan-and-targets-u05-accounting-phone-dark.png) |
| Listed, U03, view Open: Draft, Active | desktop | ![Listed, U03, view Open: Draft, Active, light](../../images/lists/s-f06-l18-commission-plan-and-targets-u03-sales-desktop-light.png) | ![Listed, U03, view Open: Draft, Active, dark](../../images/lists/s-f06-l18-commission-plan-and-targets-u03-sales-desktop-dark.png) |
| Listed, U03, view Open: Draft, Active | phone | ![Listed, U03, view Open: Draft, Active, light](../../images/lists/s-f06-l18-commission-plan-and-targets-u03-sales-phone-light.png) | ![Listed, U03, view Open: Draft, Active, dark](../../images/lists/s-f06-l18-commission-plan-and-targets-u03-sales-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Customers and sales › Commission plan and targets](README.md) |
| Workspaces | [U13](../../../../04-ux/views/u13-owner/workspace.md), [U02](../../../../04-ux/views/u02-manager/workspace.md), [U42](../../../../04-ux/views/u42-sales-representative/workspace.md), [U23](../../../../04-ux/views/u23-store-manager/workspace.md), [U05](../../../../04-ux/views/u05-accounting/workspace.md), [U03](../../../../04-ux/views/u03-sales/workspace.md) |
| Flows | [FL-F6-09](../../flows/fl-f06-09-sell-on-the-road-and-steer-sales.md), [FL-SC11-06](../../../../08-sectors/sc11-professional-firms/flows/fl-sc11-06-firm-management.md), [FL-SC15-05](../../../../08-sectors/sc15-wholesale-and-distribution/flows/fl-sc15-05-sales-force-and-performance.md) |

## Open questions

None.

---

⬅️ [S-F6-L17 Invoice disputes](s-f06-l17-invoice-disputes.md) · ⬆️ [Up](README.md) ·
➡️ [S-F6-L19 Commission lines](s-f06-l19-commission-lines.md)
