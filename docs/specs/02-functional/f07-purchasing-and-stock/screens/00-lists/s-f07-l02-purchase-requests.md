🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📦 [F7 Purchasing and stock](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Purchasing and stock menu](README.md) › 🗂️ S-F7-L02 Purchase requests

# 🗂️ S-F7-L02 Purchase requests

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U01 Employee](../../../../01-users/personas/u01-employee.md) | as the permissions row "Purchase request": ✅ | actions as [permissions](../../permissions.md) gives them |
| [U04 Purchasing and stock](../../../../01-users/personas/u04-purchasing.md) | as the permissions row "Purchase request": ✅ | actions as [permissions](../../permissions.md) gives them |
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | as the permissions row "Purchase request": ✅ approve | actions as [permissions](../../permissions.md) gives them |
| [U20 Production operator](../../../../01-users/personas/u20-production-operator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U21 Production planner](../../../../01-users/personas/u21-production-planner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U54: their use cases only read these records, inside a screen of the use case, so they open them
from there (D493).

## Purpose

The aggregated list of every [E-F7-02 Purchase request](../../data/e-f07-02-purchase-request.md) the user may see: to
find, filter, total and act on many purchase requests at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Purchasing and stock › Purchase requests, in the capability's menu (D495).
- **Workspaces:** 5 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "purchase requests" offers this view.
- **AI assistant:** "show the purchase requests that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Purchase requests    Purchasing and stock › Purchase requests   [+ New]                                      |
| [count] [total amount] [Draft]   [chart: count by state, amount stacked]                                     |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| items             | [ ] ITEMS   STATE   PROJECT OR DEPARTMENT   AMOUNT                                       |
| project or depart | [ ] ...                                                  Open >                          |
| state             | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Items | items | text | yes |
| State | state | badge: Draft, ToApprove, Approved, Ordered, Refused | yes |
| Project or department | project or department | link to the record | yes |
| Amount | amount | amount, right-aligned | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| Items | each value | the visible rows (D488) |
| Project or department | each linked project or department | the visible rows (D488) |
| State | Draft, ToApprove, Approved, Ordered, Refused | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Purchase requests of a chosen project or department, or of the project or departments that match a filter.
- From the other side: the project or departments that have purchase requests, or none.

## KPI strip

- Count of the visible rows.
- Total of amount.
- Needs attention: count in the state Draft.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state, amount stacked (VR-8); the Chart button turns the filtered list into a chart the user can pin to their
home screen (C-09).

## Saved views

- All.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New purchase request | header | the personas whose roles may create it | the record's own page (Row opens) |
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

Open › goes to [S-F7-01 Purchase request](../01-procure/s-f07-01-purchase-request.md).

The records also show on: [S-F7-20 Buy](../08-catalogues-and-stock-levels/s-f07-20-buy.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 purchase requests of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no purchase request the user may see yet, with the create action when allowed.
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
| Listed, U01, view All | desktop | ![Listed, U01, view All, light](../../images/lists/s-f07-l02-purchase-requests-u01-employee-desktop-light.png) | ![Listed, U01, view All, dark](../../images/lists/s-f07-l02-purchase-requests-u01-employee-desktop-dark.png) |
| Listed, U01, view All | phone | ![Listed, U01, view All, light](../../images/lists/s-f07-l02-purchase-requests-u01-employee-phone-light.png) | ![Listed, U01, view All, dark](../../images/lists/s-f07-l02-purchase-requests-u01-employee-phone-dark.png) |
| Listed, U04, view All | desktop | ![Listed, U04, view All, light](../../images/lists/s-f07-l02-purchase-requests-u04-purchasing-desktop-light.png) | ![Listed, U04, view All, dark](../../images/lists/s-f07-l02-purchase-requests-u04-purchasing-desktop-dark.png) |
| Listed, U04, view All | phone | ![Listed, U04, view All, light](../../images/lists/s-f07-l02-purchase-requests-u04-purchasing-phone-light.png) | ![Listed, U04, view All, dark](../../images/lists/s-f07-l02-purchase-requests-u04-purchasing-phone-dark.png) |
| Listed, U02, view Needs attention | desktop | ![Listed, U02, view Needs attention, light](../../images/lists/s-f07-l02-purchase-requests-u02-manager-desktop-light.png) | ![Listed, U02, view Needs attention, dark](../../images/lists/s-f07-l02-purchase-requests-u02-manager-desktop-dark.png) |
| Listed, U02, view Needs attention | phone | ![Listed, U02, view Needs attention, light](../../images/lists/s-f07-l02-purchase-requests-u02-manager-phone-light.png) | ![Listed, U02, view Needs attention, dark](../../images/lists/s-f07-l02-purchase-requests-u02-manager-phone-dark.png) |
| Listed, U20, view All | desktop | ![Listed, U20, view All, light](../../images/lists/s-f07-l02-purchase-requests-u20-production-operator-desktop-light.png) | ![Listed, U20, view All, dark](../../images/lists/s-f07-l02-purchase-requests-u20-production-operator-desktop-dark.png) |
| Listed, U20, view All | phone | ![Listed, U20, view All, light](../../images/lists/s-f07-l02-purchase-requests-u20-production-operator-phone-light.png) | ![Listed, U20, view All, dark](../../images/lists/s-f07-l02-purchase-requests-u20-production-operator-phone-dark.png) |
| Listed, U21, view All | desktop | ![Listed, U21, view All, light](../../images/lists/s-f07-l02-purchase-requests-u21-production-planner-desktop-light.png) | ![Listed, U21, view All, dark](../../images/lists/s-f07-l02-purchase-requests-u21-production-planner-desktop-dark.png) |
| Listed, U21, view All | phone | ![Listed, U21, view All, light](../../images/lists/s-f07-l02-purchase-requests-u21-production-planner-phone-light.png) | ![Listed, U21, view All, dark](../../images/lists/s-f07-l02-purchase-requests-u21-production-planner-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Purchasing and stock › Purchase requests](README.md) |
| Workspaces | [U01](../../../../04-ux/views/u01-employee/workspace.md), [U04](../../../../04-ux/views/u04-purchasing/workspace.md), [U02](../../../../04-ux/views/u02-manager/workspace.md), [U20](../../../../04-ux/views/u20-production-operator/workspace.md), [U21](../../../../04-ux/views/u21-production-planner/workspace.md) |
| Flows | [FL-F2-11](../../../f02-no-code-configuration/flows/fl-f02-11-rights-translations-and-approvals.md), [FL-F7-01](../../flows/fl-f07-01-procure.md), [FL-F7-08](../../flows/fl-f07-08-catalogues-and-stock-levels.md) |

## Open questions

None.

---

⬅️ [S-F7-L01 Supplier records](s-f07-l01-supplier-records.md) · ⬆️ [Up](README.md) ·
➡️ [S-F7-L03 Purchase orders](s-f07-l03-purchase-orders.md)
