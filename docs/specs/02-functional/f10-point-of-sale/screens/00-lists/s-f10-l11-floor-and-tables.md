🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏪 [F10 Point of sale (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Point of sale (plugin) menu](README.md) › 🗂️ S-F10-L11 Floor and tables

# 🗂️ S-F10-L11 Floor and tables

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U18 Waiter](../../../../01-users/personas/u18-waiter.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F10-11 Floor and table](../../data/e-f10-11-floor-and-table.md) the user may see: to
find, filter, total and act on many floor and tables at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Point of sale (plugin) › Floor and tables, in the capability's menu (D495).
- **Workspaces:** 4 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "floor and tables" offers this view.
- **AI assistant:** "show the floor and tables that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Floor and tables    Point of sale (plugin) › Floor and tables   [+ New]                                      |
| [count]   [chart: count by state]                                                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] FLOOR   STATE                                                                        |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Floor | floor | text | yes |
| State | state | badge: Free, Occupied, Booked | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Free, Occupied, Booked | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: floor and tables link to no other record type in their fields.

## KPI strip

- Count of the visible rows.

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
| New floor and table | header | the personas whose roles may create it | the record's own page (Row opens) |
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

Open › goes to [S-F10-09 Floor](../04-restaurant-service/s-f10-09-floor.md).

The records also show on: [S-F10-12 QR menu](../05-self-order-and-kiosk/s-f10-12-qr-menu.md),
[S-F10-15 Point of sale settings](../07-set-up-and-report/s-f10-15-point-of-sale-settings.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 floor and tables of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no floor and table the user may see yet, with the create action when allowed.
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
| Listed, U02, view All | desktop | ![Listed, U02, view All, light](../../images/lists/s-f10-l11-floor-and-tables-u02-manager-desktop-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-f10-l11-floor-and-tables-u02-manager-desktop-dark.png) |
| Listed, U02, view All | phone | ![Listed, U02, view All, light](../../images/lists/s-f10-l11-floor-and-tables-u02-manager-phone-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-f10-l11-floor-and-tables-u02-manager-phone-dark.png) |
| Listed, U18, view All | desktop | ![Listed, U18, view All, light](../../images/lists/s-f10-l11-floor-and-tables-u18-waiter-desktop-light.png) | ![Listed, U18, view All, dark](../../images/lists/s-f10-l11-floor-and-tables-u18-waiter-desktop-dark.png) |
| Listed, U18, view All | phone | ![Listed, U18, view All, light](../../images/lists/s-f10-l11-floor-and-tables-u18-waiter-phone-light.png) | ![Listed, U18, view All, dark](../../images/lists/s-f10-l11-floor-and-tables-u18-waiter-phone-dark.png) |
| Listed, U09, view All | desktop | ![Listed, U09, view All, light](../../images/lists/s-f10-l11-floor-and-tables-u09-customer-desktop-light.png) | ![Listed, U09, view All, dark](../../images/lists/s-f10-l11-floor-and-tables-u09-customer-desktop-dark.png) |
| Listed, U09, view All | phone | ![Listed, U09, view All, light](../../images/lists/s-f10-l11-floor-and-tables-u09-customer-phone-light.png) | ![Listed, U09, view All, dark](../../images/lists/s-f10-l11-floor-and-tables-u09-customer-phone-dark.png) |
| Listed, U07, view All | desktop | ![Listed, U07, view All, light](../../images/lists/s-f10-l11-floor-and-tables-u07-administrator-desktop-light.png) | ![Listed, U07, view All, dark](../../images/lists/s-f10-l11-floor-and-tables-u07-administrator-desktop-dark.png) |
| Listed, U07, view All | phone | ![Listed, U07, view All, light](../../images/lists/s-f10-l11-floor-and-tables-u07-administrator-phone-light.png) | ![Listed, U07, view All, dark](../../images/lists/s-f10-l11-floor-and-tables-u07-administrator-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Point of sale (plugin) › Floor and tables](README.md) |
| Workspaces | [U02](../../../../04-ux/views/u02-manager/workspace.md), [U18](../../../../04-ux/views/u18-waiter/workspace.md), [U09](../../../../04-ux/views/u09-customer/workspace.md), [U07](../../../../04-ux/views/u07-administrator/workspace.md) |
| Flows | [FL-F10-04](../../flows/fl-f10-04-restaurant-service.md), [FL-F10-05](../../flows/fl-f10-05-self-order-and-kiosk.md), [FL-F10-07](../../flows/fl-f10-07-set-up-and-report.md) |

## Open questions

None.

---

⬅️ [S-F10-L10 Loyalty card and gift cards](s-f10-l10-loyalty-card-and-gift-cards.md) · ⬆️ [Up](README.md) ·
➡️ [S-F10-L12 Table bookings](s-f10-l12-table-bookings.md)
