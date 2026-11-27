🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F19 Feature factory (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Feature factory (hosted edition) menu](README.md) › 🗂️ S-F19-L11 Delivery commitments

# 🗂️ S-F19-L11 Delivery commitments

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U48 Hosting engineer](../../../../01-users/personas/u48-hosting-engineer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F19-11 Delivery commitment](../../data/e-f19-11-delivery-commitment.md) the user may
see: to find, filter, total and act on many delivery commitments at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Feature factory (hosted edition) › Delivery commitments, in the capability's menu (D495).
- **Workspaces:** 4 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "delivery commitments" offers this view.
- **AI assistant:** "show the delivery commitments that need attention" opens it with the filter as editable chips
  (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Delivery commitments    Feature factory (hosted edition) › Delivery commitments   [+ New]                    |
| [count] [Late] [new this month]   [chart: count by state]                                                    |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| feature request   | [ ] FEATURE REQUEST   STATE   COMMITTED   DELIVERED   DELAYS                             |
| delays            | [ ] ...                                                  Open >                          |
| state             | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Feature request | feature request | link to the record | yes |
| State | state | badge: OnTime, Delayed, Late, Delivered, Cancelled | yes |
| Committed | committed | date | yes |
| Delivered | delivered | date | yes |
| Delays | delays | text | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| Feature request | each linked feature request | the visible rows (D488) |
| Delays | each value | the visible rows (D488) |
| State | OnTime, Delayed, Late, Delivered, Cancelled | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Delivery commitments of a chosen feature request, or of the feature requests that match a filter.
- From the other side: the feature requests that have delivery commitments, or none.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Late.
- New this month, by committed.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Open: OnTime, Delayed, Late.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New delivery commitment | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- committed: editable in its cell unless the record's state locks it.
- delays: editable in its cell unless the record's state locks it.
- delivered: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F19-21 Delivery plan](../01-describe-and-order/s-f19-21-delivery-plan.md).

The records also show on: [S-F19-03 Quote](../01-describe-and-order/s-f19-03-quote.md),
[S-F19-19 Feature board](../05-bill-and-credit/s-f19-19-feature-board.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 delivery commitments of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no delivery commitment the user may see yet, with the create action when allowed.
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
| Listed, U13, view Needs attention | desktop | ![Listed, U13, view Needs attention, light](../../images/lists/s-f19-l11-delivery-commitments-u13-owner-desktop-light.png) | ![Listed, U13, view Needs attention, dark](../../images/lists/s-f19-l11-delivery-commitments-u13-owner-desktop-dark.png) |
| Listed, U13, view Needs attention | phone | ![Listed, U13, view Needs attention, light](../../images/lists/s-f19-l11-delivery-commitments-u13-owner-phone-light.png) | ![Listed, U13, view Needs attention, dark](../../images/lists/s-f19-l11-delivery-commitments-u13-owner-phone-dark.png) |
| Listed, U05, view Open: OnTime, Delayed, Late | desktop | ![Listed, U05, view Open: OnTime, Delayed, Late, light](../../images/lists/s-f19-l11-delivery-commitments-u05-accounting-desktop-light.png) | ![Listed, U05, view Open: OnTime, Delayed, Late, dark](../../images/lists/s-f19-l11-delivery-commitments-u05-accounting-desktop-dark.png) |
| Listed, U05, view Open: OnTime, Delayed, Late | phone | ![Listed, U05, view Open: OnTime, Delayed, Late, light](../../images/lists/s-f19-l11-delivery-commitments-u05-accounting-phone-light.png) | ![Listed, U05, view Open: OnTime, Delayed, Late, dark](../../images/lists/s-f19-l11-delivery-commitments-u05-accounting-phone-dark.png) |
| Listed, U48, view Needs attention | desktop | ![Listed, U48, view Needs attention, light](../../images/lists/s-f19-l11-delivery-commitments-u48-hosting-engineer-desktop-light.png) | ![Listed, U48, view Needs attention, dark](../../images/lists/s-f19-l11-delivery-commitments-u48-hosting-engineer-desktop-dark.png) |
| Listed, U48, view Needs attention | phone | ![Listed, U48, view Needs attention, light](../../images/lists/s-f19-l11-delivery-commitments-u48-hosting-engineer-phone-light.png) | ![Listed, U48, view Needs attention, dark](../../images/lists/s-f19-l11-delivery-commitments-u48-hosting-engineer-phone-dark.png) |
| Listed, U07, view Needs attention | desktop | ![Listed, U07, view Needs attention, light](../../images/lists/s-f19-l11-delivery-commitments-u07-administrator-desktop-light.png) | ![Listed, U07, view Needs attention, dark](../../images/lists/s-f19-l11-delivery-commitments-u07-administrator-desktop-dark.png) |
| Listed, U07, view Needs attention | phone | ![Listed, U07, view Needs attention, light](../../images/lists/s-f19-l11-delivery-commitments-u07-administrator-phone-light.png) | ![Listed, U07, view Needs attention, dark](../../images/lists/s-f19-l11-delivery-commitments-u07-administrator-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Feature factory (hosted edition) › Delivery commitments](README.md) |
| Workspaces | [U13](../../../../04-ux/views/u13-owner/workspace.md), [U05](../../../../04-ux/views/u05-accounting/workspace.md), [U48](../../../../04-ux/views/u48-hosting-engineer/workspace.md), [U07](../../../../04-ux/views/u07-administrator/workspace.md) |
| Flows | [FL-F19-01](../../flows/fl-f19-01-describe-and-order.md), [FL-F19-05](../../flows/fl-f19-05-bill-and-credit.md), [FL-F19-06](../../flows/fl-f19-06-delivery-and-refunds.md) |

## Open questions

None.

---

⬅️ [S-F19-L10 Feature withdrawals](s-f19-l10-feature-withdrawals.md) · ⬆️ [Up](README.md) ·
➡️ [S-F19-L12 Feature refunds](s-f19-l12-feature-refunds.md)
