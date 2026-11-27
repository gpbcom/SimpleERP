🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏪 [F10 Point of sale (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Point of sale (plugin) menu](README.md) › 🗂️ S-F10-L02 Till sessions

# 🗂️ S-F10-L02 Till sessions

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U17 Cashier](../../../../01-users/personas/u17-cashier.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U23 Store manager](../../../../01-users/personas/u23-store-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U14 Field worker](../../../../01-users/personas/u14-field-worker.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U18 Waiter](../../../../01-users/personas/u18-waiter.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F10-02 Till session](../../data/e-f10-02-till-session.md) the user may see: to find,
filter, total and act on many till sessions at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Point of sale (plugin) › Till sessions, in the capability's menu (D495).
- **Workspaces:** 7 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "till sessions" offers this view.
- **AI assistant:** "show the till sessions that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Till sessions    Point of sale (plugin) › Till sessions   [+ New]                                            |
| [count] [Open]   [chart: count by state]                                                                     |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| point of sale     | [ ] POINT OF SALE   STATE                                                                |
| state             | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Point of sale | point of sale | link to the record | yes |
| State | state | badge: Open, Closing, Closed, Posted | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| Point of sale | each linked point of sale | the visible rows (D488) |
| State | Open, Closing, Closed, Posted | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Till sessions of a chosen point of sale, or of the point of sales that match a filter.
- From the other side: the point of sales that have till sessions, or none.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Open.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Open: Open, Closing, Posted.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New till session | header | the personas whose roles may create it | the record's own page (Row opens) |
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

Open › goes to [S-F10-01 Till session](../01-till-session/s-f10-01-till-session.md).

The records also show on: [S-F10-14 Mobile till](../06-mobile-and-delivery/s-f10-14-mobile-till.md),
[S-F10-20 Till assistant](../07-set-up-and-report/s-f10-20-till-assistant.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 till sessions of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no till session the user may see yet, with the create action when allowed.
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
| Listed, U17, view Open: Open, Closing, Posted | desktop | ![Listed, U17, view Open: Open, Closing, Posted, light](../../images/lists/s-f10-l02-till-sessions-u17-cashier-desktop-light.png) | ![Listed, U17, view Open: Open, Closing, Posted, dark](../../images/lists/s-f10-l02-till-sessions-u17-cashier-desktop-dark.png) |
| Listed, U17, view Open: Open, Closing, Posted | phone | ![Listed, U17, view Open: Open, Closing, Posted, light](../../images/lists/s-f10-l02-till-sessions-u17-cashier-phone-light.png) | ![Listed, U17, view Open: Open, Closing, Posted, dark](../../images/lists/s-f10-l02-till-sessions-u17-cashier-phone-dark.png) |
| Listed, U02, view Needs attention | desktop | ![Listed, U02, view Needs attention, light](../../images/lists/s-f10-l02-till-sessions-u02-manager-desktop-light.png) | ![Listed, U02, view Needs attention, dark](../../images/lists/s-f10-l02-till-sessions-u02-manager-desktop-dark.png) |
| Listed, U02, view Needs attention | phone | ![Listed, U02, view Needs attention, light](../../images/lists/s-f10-l02-till-sessions-u02-manager-phone-light.png) | ![Listed, U02, view Needs attention, dark](../../images/lists/s-f10-l02-till-sessions-u02-manager-phone-dark.png) |
| Listed, U23, view Needs attention | desktop | ![Listed, U23, view Needs attention, light](../../images/lists/s-f10-l02-till-sessions-u23-store-manager-desktop-light.png) | ![Listed, U23, view Needs attention, dark](../../images/lists/s-f10-l02-till-sessions-u23-store-manager-desktop-dark.png) |
| Listed, U23, view Needs attention | phone | ![Listed, U23, view Needs attention, light](../../images/lists/s-f10-l02-till-sessions-u23-store-manager-phone-light.png) | ![Listed, U23, view Needs attention, dark](../../images/lists/s-f10-l02-till-sessions-u23-store-manager-phone-dark.png) |
| Listed, U14, view Open: Open, Closing, Posted | desktop | ![Listed, U14, view Open: Open, Closing, Posted, light](../../images/lists/s-f10-l02-till-sessions-u14-field-worker-desktop-light.png) | ![Listed, U14, view Open: Open, Closing, Posted, dark](../../images/lists/s-f10-l02-till-sessions-u14-field-worker-desktop-dark.png) |
| Listed, U14, view Open: Open, Closing, Posted | phone | ![Listed, U14, view Open: Open, Closing, Posted, light](../../images/lists/s-f10-l02-till-sessions-u14-field-worker-phone-light.png) | ![Listed, U14, view Open: Open, Closing, Posted, dark](../../images/lists/s-f10-l02-till-sessions-u14-field-worker-phone-dark.png) |
| Listed, U18, view Open: Open, Closing, Posted | desktop | ![Listed, U18, view Open: Open, Closing, Posted, light](../../images/lists/s-f10-l02-till-sessions-u18-waiter-desktop-light.png) | ![Listed, U18, view Open: Open, Closing, Posted, dark](../../images/lists/s-f10-l02-till-sessions-u18-waiter-desktop-dark.png) |
| Listed, U18, view Open: Open, Closing, Posted | phone | ![Listed, U18, view Open: Open, Closing, Posted, light](../../images/lists/s-f10-l02-till-sessions-u18-waiter-phone-light.png) | ![Listed, U18, view Open: Open, Closing, Posted, dark](../../images/lists/s-f10-l02-till-sessions-u18-waiter-phone-dark.png) |
| Listed, U05, view Open: Open, Closing, Posted | desktop | ![Listed, U05, view Open: Open, Closing, Posted, light](../../images/lists/s-f10-l02-till-sessions-u05-accounting-desktop-light.png) | ![Listed, U05, view Open: Open, Closing, Posted, dark](../../images/lists/s-f10-l02-till-sessions-u05-accounting-desktop-dark.png) |
| Listed, U05, view Open: Open, Closing, Posted | phone | ![Listed, U05, view Open: Open, Closing, Posted, light](../../images/lists/s-f10-l02-till-sessions-u05-accounting-phone-light.png) | ![Listed, U05, view Open: Open, Closing, Posted, dark](../../images/lists/s-f10-l02-till-sessions-u05-accounting-phone-dark.png) |
| Listed, U13, view Needs attention | desktop | ![Listed, U13, view Needs attention, light](../../images/lists/s-f10-l02-till-sessions-u13-owner-desktop-light.png) | ![Listed, U13, view Needs attention, dark](../../images/lists/s-f10-l02-till-sessions-u13-owner-desktop-dark.png) |
| Listed, U13, view Needs attention | phone | ![Listed, U13, view Needs attention, light](../../images/lists/s-f10-l02-till-sessions-u13-owner-phone-light.png) | ![Listed, U13, view Needs attention, dark](../../images/lists/s-f10-l02-till-sessions-u13-owner-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Point of sale (plugin) › Till sessions](README.md) |
| Workspaces | [U17](../../../../04-ux/views/u17-cashier/workspace.md), [U02](../../../../04-ux/views/u02-manager/workspace.md), [U23](../../../../04-ux/views/u23-store-manager/workspace.md), [U14](../../../../04-ux/views/u14-field-worker/workspace.md), [U18](../../../../04-ux/views/u18-waiter/workspace.md), [U05](../../../../04-ux/views/u05-accounting/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md) |
| Flows | [FL-F10-01](../../flows/fl-f10-01-till-session.md), [FL-F10-06](../../flows/fl-f10-06-mobile-and-delivery.md), [FL-F10-07](../../flows/fl-f10-07-set-up-and-report.md), [FL-F10-09](../../flows/fl-f10-09-cash-and-settlements.md), [FL-F10-11](../../flows/fl-f10-11-store-reports.md), [FL-SC16-04](../../../../08-sectors/sc16-events-and-culture/flows/fl-sc16-04-on-site.md) |

## Open questions

None.

---

⬅️ [S-F10-L01 Point of sales](s-f10-l01-point-of-sales.md) · ⬆️ [Up](README.md) ·
➡️ [S-F10-L03 Point of sale orders](s-f10-l03-point-of-sale-orders.md)
