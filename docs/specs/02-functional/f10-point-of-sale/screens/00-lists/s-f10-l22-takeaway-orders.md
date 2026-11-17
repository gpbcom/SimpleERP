🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏪 [F10 Point of sale (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Point of sale (plugin) menu](README.md) › 🗂️ S-F10-L22 Takeaway orders

# 🗂️ S-F10-L22 Takeaway orders

**Status:** ✅ specified

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U19 Kitchen staff](../../../../01-users/personas/u19-kitchen-staff.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F10-22 Takeaway order](../../data/e-f10-22-takeaway-order.md) the user may see: to find,
filter, total and act on many takeaway orders at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Point of sale › Takeaway orders, in the capability's menu (D495).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "takeaway orders" offers this view.
- **AI assistant:** "show the takeaway orders that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Takeaway orders    Point of sale › Takeaway orders   [+ New]                                                 |
| [count] [Placed] [new this month]   [chart: count by state]                                                                   |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] NUMBER   SLOT   LINES   TOTAL   STATE                                                |
| [ ] ...                                                                       Open >                         |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Number | number | text | yes |
| Slot | pickup slot | date and time | yes |
| Lines | lines | text | yes |
| Total | total | money | yes |
| State | state | badge: Placed, Accepted, In preparation, Ready, Collected, Cancelled, Refused, Not collected | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Placed, Accepted, In preparation, Ready, Collected, Cancelled, Refused, Not collected | the visible rows (D488) |
| Slot | each value | the visible rows (D488) |
| Payment | paid online, pay at collection | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Orders of a chosen customer, or of the customers that match a filter.
- From the other side: the customers with a takeaway order today, or none.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Placed.
- New this month, by pickup slot.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Mine: customer.
- Open: Accepted.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New takeaway order | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only, audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows, audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted, audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns, audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

None: orders move by action, never by editing.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| customer | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F10-28 Online takeaway](../12-takeaway-softpos-and-labels/s-f10-28-online-takeaway.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 takeaway orders of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no takeaway order the user may see yet, with the create action when allowed.
- **Selected:** the bulk bar with the actions allowed on every selected row.
- **Error:** the query failed, with Retry.

## Responsive behaviour

On a phone the table keeps its columns and scrolls sideways, the facet panel becomes a drawer and the KPI strip stays
(VR-14, D491).

## Accessibility

The KPI strip, the facet panel, the toolbar and the table are named landmarks; the result count is announced when the
filters change; each chip has its remove button; the facet drawer returns the focus to its button.

## Example images

Drawn in the image round from this page: one row per persona and device, light and dark
([D490](../../../../06-decisions/ux/d490-example-images-for-every-persona-that-can-open-a-view.md),
[D500](../../../../06-decisions/ux/d500-images-live-in-the-specs-folders.md)). The files are named by the plan.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Listed, U09, view Needs attention | phone | ![Listed, U09, view Needs attention, light](../../images/lists/s-f10-l22-takeaway-orders-u09-customer-phone-light.png) | ![Listed, U09, view Needs attention, dark](../../images/lists/s-f10-l22-takeaway-orders-u09-customer-phone-dark.png) |
| Listed, U19, view Needs attention | desktop | ![Listed, U19, view Needs attention, light](../../images/lists/s-f10-l22-takeaway-orders-u19-kitchen-staff-desktop-light.png) | ![Listed, U19, view Needs attention, dark](../../images/lists/s-f10-l22-takeaway-orders-u19-kitchen-staff-desktop-dark.png) |
| Listed, U09, view Mine: customer | desktop | ![Listed, U09, view Mine: customer, light](../../images/lists/s-f10-l22-takeaway-orders-u09-customer-desktop-light.png) | ![Listed, U09, view Mine: customer, dark](../../images/lists/s-f10-l22-takeaway-orders-u09-customer-desktop-dark.png) |
| Listed, U19, view Mine: customer | phone | ![Listed, U19, view Mine: customer, light](../../images/lists/s-f10-l22-takeaway-orders-u19-kitchen-staff-phone-light.png) | ![Listed, U19, view Mine: customer, dark](../../images/lists/s-f10-l22-takeaway-orders-u19-kitchen-staff-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Point of sale › Takeaway orders](README.md) |
| Workspaces | [U09](../../../../04-ux/views/u09-customer/workspace.md), [U19](../../../../04-ux/views/u19-kitchen-staff/workspace.md) |
| Flows | [FL-F10-12](../../flows/fl-f10-12-takeaway-softpos-and-labels.md) |

## Open questions

None.

---

⬅️ [S-F10-L21 Table QR codes](s-f10-l21-table-qr-codes.md) · ⬆️ [Up](README.md) ·
➡️ [S-F10-L23 Shelf labels](s-f10-l23-shelf-labels.md)
