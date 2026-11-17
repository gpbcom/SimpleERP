🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: HR and projects menu](README.md) ›
🗂️ S-F9-L27 Subcontractor assignments

# 🗂️ S-F9-L27 Subcontractor assignments

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U10 Supplier](../../../../01-users/personas/u10-supplier.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |
| [U24 Engagement manager](../../../../01-users/personas/u24-engagement-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F9-27 Subcontractor assignment](../../data/e-f09-27-subcontractor-assignment.md) the
user may see: to find, filter, total and act on many subcontractor assignments at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** HR and projects › Subcontractor assignments, in the capability's menu (D495).
- **Workspaces:** 3 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "subcontractor assignments" offers this view.
- **AI assistant:** "show the subcontractor assignments that need attention" opens it with the filter as editable chips
  (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Subcontractor assignments    HR and projects › Subcontractor assignments   [+ New]                           |
| [count] [total price] [new this month]   [chart: count by state, price stacked]                              |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] SUPPLIER   STATE   PRICE   DOCUMENTS                                                 |
| supplier          | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Supplier | supplier | text | yes |
| State | state | badge: Proposed, Active, Done | yes |
| Price | price | amount, right-aligned | yes |
| Documents | documents | date | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Proposed, Active, Done | the visible rows (D488) |
| Supplier | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Subcontractor assignments of a chosen supplier, or of the suppliers that match a filter.
- From the other side: the suppliers that have subcontractor assignments, or none.

## KPI strip

- Count of the visible rows.
- Total of price.
- New this month, by documents.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state, price stacked (VR-8); the Chart button turns the filtered list into a chart the user can pin to their
home screen (C-09).

## Saved views

- All.
- Open: Proposed, Active.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New subcontractor assignment | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- documents: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F9-29 Subcontractors](../11-capacity-rounds-and-partners/s-f09-29-subcontractors.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 subcontractor assignments of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no subcontractor assignment the user may see yet, with the create action when allowed.
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
| Listed, U02, view Open: Proposed, Active | desktop | ![Listed, U02, view Open: Proposed, Active, light](../../images/lists/s-f09-l27-subcontractor-assignments-u02-manager-desktop-light.png) | ![Listed, U02, view Open: Proposed, Active, dark](../../images/lists/s-f09-l27-subcontractor-assignments-u02-manager-desktop-dark.png) |
| Listed, U02, view Open: Proposed, Active | phone | ![Listed, U02, view Open: Proposed, Active, light](../../images/lists/s-f09-l27-subcontractor-assignments-u02-manager-phone-light.png) | ![Listed, U02, view Open: Proposed, Active, dark](../../images/lists/s-f09-l27-subcontractor-assignments-u02-manager-phone-dark.png) |
| Listed, U10, view Open: Proposed, Active | desktop | ![Listed, U10, view Open: Proposed, Active, light](../../images/lists/s-f09-l27-subcontractor-assignments-u10-supplier-desktop-light.png) | ![Listed, U10, view Open: Proposed, Active, dark](../../images/lists/s-f09-l27-subcontractor-assignments-u10-supplier-desktop-dark.png) |
| Listed, U10, view Open: Proposed, Active | phone | ![Listed, U10, view Open: Proposed, Active, light](../../images/lists/s-f09-l27-subcontractor-assignments-u10-supplier-phone-light.png) | ![Listed, U10, view Open: Proposed, Active, dark](../../images/lists/s-f09-l27-subcontractor-assignments-u10-supplier-phone-dark.png) |
| Listed, U24, view Open: Proposed, Active | desktop | ![Listed, U24, view Open: Proposed, Active, light](../../images/lists/s-f09-l27-subcontractor-assignments-u24-engagement-manager-desktop-light.png) | ![Listed, U24, view Open: Proposed, Active, dark](../../images/lists/s-f09-l27-subcontractor-assignments-u24-engagement-manager-desktop-dark.png) |
| Listed, U24, view Open: Proposed, Active | phone | ![Listed, U24, view Open: Proposed, Active, light](../../images/lists/s-f09-l27-subcontractor-assignments-u24-engagement-manager-phone-light.png) | ![Listed, U24, view Open: Proposed, Active, dark](../../images/lists/s-f09-l27-subcontractor-assignments-u24-engagement-manager-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [HR and projects › Subcontractor assignments](README.md) |
| Workspaces | [U02](../../../../04-ux/views/u02-manager/workspace.md), [U10](../../../../04-ux/views/u10-supplier/workspace.md), [U24](../../../../04-ux/views/u24-engagement-manager/workspace.md) |
| Flows | [FL-F9-11](../../flows/fl-f09-11-capacity-rounds-and-partners.md) |

## Open questions

None.

---

⬅️ [S-F9-L26 Rounds](s-f09-l26-rounds.md) · ⬆️ [Up](README.md) ·
➡️ [S-F9-L28 Assignment proposals](s-f09-l28-assignment-proposals.md)
