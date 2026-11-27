🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🎭 [SC16 Events and culture](../../README.md) ›
🖥️ [Screens](../README.md) › 🗂️ [Views: Events and culture menu](README.md) › 🗂️ S-SC16-L07 Ticket orders

# 🗂️ S-SC16-L07 Ticket orders

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U44 Box-office agent](../../../../01-users/personas/u44-box-office-agent.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |
| [U43 Event producer](../../../../01-users/personas/u43-event-producer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-SC16-07 Ticket order](../../data/e-sc16-07-ticket-order.md) the user may see: to find,
filter, total and act on many ticket orders at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Events and culture › Ticket orders, in the capability's menu (D495).
- **Workspaces:** 4 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "ticket orders" offers this view.
- **AI assistant:** "show the ticket orders that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Ticket orders    Events and culture › Ticket orders   [+ New]                                                |
| [count] [total price]   [chart: count by state, price stacked]                                               |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| category          | [ ] BUYER   STATE   PRICE   CATEGORY                                                     |
| state             | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Buyer | buyer | link to the record | yes |
| State | state | badge: Paid, Refunded, Exchanged | yes |
| Price | price | amount, right-aligned | yes |
| Category | category | link to the record | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| Category | each linked category | the visible rows (D488) |
| State | Paid, Refunded, Exchanged | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: ticket orders link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- Total of price.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state, price stacked (VR-8); the Chart button turns the filtered list into a chart the user can pin to their
home screen (C-09).

## Saved views

- All.
- Open: Refunded, Exchanged.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New ticket order | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- category: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-SC16-05 Ticketing](../02-ticketing/s-sc16-05-ticketing.md).

The records also show on: [S-SC16-17 Refunds](../02-ticketing/s-sc16-17-refunds.md),
[S-SC16-19 Attendee messages](../04-on-site/s-sc16-19-attendee-messages.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 ticket orders of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no ticket order the user may see yet, with the create action when allowed.
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
| Listed, U44, view Open: Refunded, Exchanged | desktop | ![Listed, U44, view Open: Refunded, Exchanged, light](../../images/lists/s-sc16-l07-ticket-orders-u44-box-office-agent-desktop-light.png) | ![Listed, U44, view Open: Refunded, Exchanged, dark](../../images/lists/s-sc16-l07-ticket-orders-u44-box-office-agent-desktop-dark.png) |
| Listed, U44, view Open: Refunded, Exchanged | phone | ![Listed, U44, view Open: Refunded, Exchanged, light](../../images/lists/s-sc16-l07-ticket-orders-u44-box-office-agent-phone-light.png) | ![Listed, U44, view Open: Refunded, Exchanged, dark](../../images/lists/s-sc16-l07-ticket-orders-u44-box-office-agent-phone-dark.png) |
| Listed, U09, view Open: Refunded, Exchanged | desktop | ![Listed, U09, view Open: Refunded, Exchanged, light](../../images/lists/s-sc16-l07-ticket-orders-u09-customer-desktop-light.png) | ![Listed, U09, view Open: Refunded, Exchanged, dark](../../images/lists/s-sc16-l07-ticket-orders-u09-customer-desktop-dark.png) |
| Listed, U09, view Open: Refunded, Exchanged | phone | ![Listed, U09, view Open: Refunded, Exchanged, light](../../images/lists/s-sc16-l07-ticket-orders-u09-customer-phone-light.png) | ![Listed, U09, view Open: Refunded, Exchanged, dark](../../images/lists/s-sc16-l07-ticket-orders-u09-customer-phone-dark.png) |
| Listed, U43, view Open: Refunded, Exchanged | desktop | ![Listed, U43, view Open: Refunded, Exchanged, light](../../images/lists/s-sc16-l07-ticket-orders-u43-event-producer-desktop-light.png) | ![Listed, U43, view Open: Refunded, Exchanged, dark](../../images/lists/s-sc16-l07-ticket-orders-u43-event-producer-desktop-dark.png) |
| Listed, U43, view Open: Refunded, Exchanged | phone | ![Listed, U43, view Open: Refunded, Exchanged, light](../../images/lists/s-sc16-l07-ticket-orders-u43-event-producer-phone-light.png) | ![Listed, U43, view Open: Refunded, Exchanged, dark](../../images/lists/s-sc16-l07-ticket-orders-u43-event-producer-phone-dark.png) |
| Listed, U05, view Open: Refunded, Exchanged | desktop | ![Listed, U05, view Open: Refunded, Exchanged, light](../../images/lists/s-sc16-l07-ticket-orders-u05-accounting-desktop-light.png) | ![Listed, U05, view Open: Refunded, Exchanged, dark](../../images/lists/s-sc16-l07-ticket-orders-u05-accounting-desktop-dark.png) |
| Listed, U05, view Open: Refunded, Exchanged | phone | ![Listed, U05, view Open: Refunded, Exchanged, light](../../images/lists/s-sc16-l07-ticket-orders-u05-accounting-phone-light.png) | ![Listed, U05, view Open: Refunded, Exchanged, dark](../../images/lists/s-sc16-l07-ticket-orders-u05-accounting-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Events and culture › Ticket orders](README.md) |
| Workspaces | [U44](../../../../04-ux/views/u44-box-office-agent/workspace.md), [U09](../../../../04-ux/views/u09-customer/workspace.md), [U43](../../../../04-ux/views/u43-event-producer/workspace.md), [U05](../../../../04-ux/views/u05-accounting/workspace.md) |
| Flows | [FL-SC16-02](../../flows/fl-sc16-02-ticketing.md), [FL-SC16-04](../../flows/fl-sc16-04-on-site.md) |

## Open questions

None.

---

⬅️ [S-SC16-L06 Performer declarations](s-sc16-l06-performer-declarations.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC16-L08 Admission tickets](s-sc16-l08-admission-tickets.md)
