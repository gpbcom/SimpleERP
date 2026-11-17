🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Manufacturing (plugin) menu](README.md) › 🗂️ S-F12-L05 Work orders

# 🗂️ S-F12-L05 Work orders

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U21 Production planner](../../../../01-users/personas/u21-production-planner.md) | as the permissions row "Work orders, quantities, scrap, checks": ✅ | actions as [permissions](../../permissions.md) gives them |
| [U20 Production operator](../../../../01-users/personas/u20-production-operator.md) | as the permissions row "Work orders, quantities, scrap, checks": ✅ own | actions as [permissions](../../permissions.md) gives them |
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | as the permissions row "Work orders, quantities, scrap, checks": read | actions as [permissions](../../permissions.md) gives them |

**Not embedded for:** U27: their use cases only read these records, inside a screen of the use case, so they open them
from there (D493).

## Purpose

The aggregated list of every [E-F12-05 Work order](../../data/e-f12-05-work-order.md) the user may see: to find, filter,
total and act on many work orders at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Manufacturing (plugin) › Work orders, in the capability's menu (D495).
- **Workspaces:** 3 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "work orders" offers this view.
- **AI assistant:** "show the work orders that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Work orders    Manufacturing (plugin) › Work orders   [+ New]                                                |
| [count] [Late]   [chart: count by state]                                                                     |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] ORDER   STATE                                                                        |
| order             | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Order | order | link to the record | yes |
| State | state | badge: New, Done, Late | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | New, Done, Late | the visible rows (D488) |
| Order | each linked order | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Work orders of a chosen order, or of the orders that match a filter.
- From the other side: the orders that have work orders, or none.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Late.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Open: New, Late.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New work order | header | the personas whose roles may create it | the record's own page (Row opens) |
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

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| operator | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F12-04 Manufacturing order](../03-make-the-products/s-f12-04-manufacturing-order.md).

The records also show on: [S-F12-05 Shop-floor tablet](../03-make-the-products/s-f12-05-shop-floor-tablet.md),
[S-F12-20 Production assistant](../08-report-and-assist/s-f12-20-production-assistant.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 work orders of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no work order the user may see yet, with the create action when allowed.
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
| Listed, U21, view Needs attention | desktop | ![Listed, U21, view Needs attention, light](../../images/lists/s-f12-l05-work-orders-u21-production-planner-desktop-light.png) | ![Listed, U21, view Needs attention, dark](../../images/lists/s-f12-l05-work-orders-u21-production-planner-desktop-dark.png) |
| Listed, U21, view Needs attention | phone | ![Listed, U21, view Needs attention, light](../../images/lists/s-f12-l05-work-orders-u21-production-planner-phone-light.png) | ![Listed, U21, view Needs attention, dark](../../images/lists/s-f12-l05-work-orders-u21-production-planner-phone-dark.png) |
| Listed, U20, view Open: New, Late | desktop | ![Listed, U20, view Open: New, Late, light](../../images/lists/s-f12-l05-work-orders-u20-production-operator-desktop-light.png) | ![Listed, U20, view Open: New, Late, dark](../../images/lists/s-f12-l05-work-orders-u20-production-operator-desktop-dark.png) |
| Listed, U20, view Open: New, Late | phone | ![Listed, U20, view Open: New, Late, light](../../images/lists/s-f12-l05-work-orders-u20-production-operator-phone-light.png) | ![Listed, U20, view Open: New, Late, dark](../../images/lists/s-f12-l05-work-orders-u20-production-operator-phone-dark.png) |
| Listed, U02, view Needs attention | desktop | ![Listed, U02, view Needs attention, light](../../images/lists/s-f12-l05-work-orders-u02-manager-desktop-light.png) | ![Listed, U02, view Needs attention, dark](../../images/lists/s-f12-l05-work-orders-u02-manager-desktop-dark.png) |
| Listed, U02, view Needs attention | phone | ![Listed, U02, view Needs attention, light](../../images/lists/s-f12-l05-work-orders-u02-manager-phone-light.png) | ![Listed, U02, view Needs attention, dark](../../images/lists/s-f12-l05-work-orders-u02-manager-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Manufacturing (plugin) › Work orders](README.md) |
| Workspaces | [U21](../../../../04-ux/views/u21-production-planner/workspace.md), [U20](../../../../04-ux/views/u20-production-operator/workspace.md), [U02](../../../../04-ux/views/u02-manager/workspace.md) |
| Flows | [FL-F12-03](../../flows/fl-f12-03-make-the-products.md), [FL-F12-08](../../flows/fl-f12-08-report-and-assist.md), [FL-F12-10](../../flows/fl-f12-10-people-and-tools.md), [FL-F12-11](../../flows/fl-f12-11-finite-schedule-and-the-tablet.md) |

## Open questions

None.

---

⬅️ [S-F12-L04 Manufacturing orders](s-f12-l04-manufacturing-orders.md) · ⬆️ [Up](README.md) ·
➡️ [S-F12-L06 Component consumptions](s-f12-l06-component-consumptions.md)
