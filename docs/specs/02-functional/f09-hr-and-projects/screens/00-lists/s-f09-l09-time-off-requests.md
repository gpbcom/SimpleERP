🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: HR and projects menu](README.md) ›
🗂️ S-F9-L09 Time-off requests

# 🗂️ S-F9-L09 Time-off requests

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U01 Employee](../../../../01-users/personas/u01-employee.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U06 Human resources](../../../../01-users/personas/u06-hr.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U25 Care coordinator](../../../../01-users/personas/u25-care-coordinator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U29 Dispatcher](../../../../01-users/personas/u29-dispatcher.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U26 Carer](../../../../01-users/personas/u26-carer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U30 Driver](../../../../01-users/personas/u30-driver.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U45: their use cases only read these records, inside a screen of the use case, so they open them
from there (D493).

## Purpose

The aggregated list of every [E-F9-09 Time-off request](../../data/e-f09-09-time-off-request.md) the user may see: to
find, filter, total and act on many time-off requests at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** HR and projects › Time-off requests, in the capability's menu (D495).
- **Workspaces:** 8 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "time-off requests" offers this view.
- **AI assistant:** "show the time-off requests that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Time-off requests    HR and projects › Time-off requests   [+ New]                                           |
| [count] [new this month]   [chart: count by state]                                                           |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] TYPE   STATE                                                                         |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Type | type | date and time | yes |
| State | state | badge: ToApprove, Approved, Refused, Cancelled | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | ToApprove, Approved, Refused, Cancelled | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: time-off requests link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- New this month, by type.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Open: ToApprove, Approved, Refused.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New time-off request | header | the personas whose roles may create it | the record's own page (Row opens) |
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

Open › goes to [S-F9-09 Time off](../03-time/s-f09-09-time-off.md).

The records also show on: [S-F9-27 Rounds](../11-capacity-rounds-and-partners/s-f09-27-rounds.md),
[S-F9-30 Scheduling board](../12-schedule-customer-requests/s-f09-30-scheduling-board.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 time-off requests of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no time-off request the user may see yet, with the create action when allowed.
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
| Listed, U01, view Open: ToApprove, Approved, Refused | desktop | ![Listed, U01, view Open: ToApprove, Approved, Refused, light](../../images/lists/s-f09-l09-time-off-requests-u01-employee-desktop-light.png) | ![Listed, U01, view Open: ToApprove, Approved, Refused, dark](../../images/lists/s-f09-l09-time-off-requests-u01-employee-desktop-dark.png) |
| Listed, U01, view Open: ToApprove, Approved, Refused | phone | ![Listed, U01, view Open: ToApprove, Approved, Refused, light](../../images/lists/s-f09-l09-time-off-requests-u01-employee-phone-light.png) | ![Listed, U01, view Open: ToApprove, Approved, Refused, dark](../../images/lists/s-f09-l09-time-off-requests-u01-employee-phone-dark.png) |
| Listed, U02, view Open: ToApprove, Approved, Refused | desktop | ![Listed, U02, view Open: ToApprove, Approved, Refused, light](../../images/lists/s-f09-l09-time-off-requests-u02-manager-desktop-light.png) | ![Listed, U02, view Open: ToApprove, Approved, Refused, dark](../../images/lists/s-f09-l09-time-off-requests-u02-manager-desktop-dark.png) |
| Listed, U02, view Open: ToApprove, Approved, Refused | phone | ![Listed, U02, view Open: ToApprove, Approved, Refused, light](../../images/lists/s-f09-l09-time-off-requests-u02-manager-phone-light.png) | ![Listed, U02, view Open: ToApprove, Approved, Refused, dark](../../images/lists/s-f09-l09-time-off-requests-u02-manager-phone-dark.png) |
| Listed, U06, view Open: ToApprove, Approved, Refused | desktop | ![Listed, U06, view Open: ToApprove, Approved, Refused, light](../../images/lists/s-f09-l09-time-off-requests-u06-hr-desktop-light.png) | ![Listed, U06, view Open: ToApprove, Approved, Refused, dark](../../images/lists/s-f09-l09-time-off-requests-u06-hr-desktop-dark.png) |
| Listed, U06, view Open: ToApprove, Approved, Refused | phone | ![Listed, U06, view Open: ToApprove, Approved, Refused, light](../../images/lists/s-f09-l09-time-off-requests-u06-hr-phone-light.png) | ![Listed, U06, view Open: ToApprove, Approved, Refused, dark](../../images/lists/s-f09-l09-time-off-requests-u06-hr-phone-dark.png) |
| Listed, U25, view Open: ToApprove, Approved, Refused | desktop | ![Listed, U25, view Open: ToApprove, Approved, Refused, light](../../images/lists/s-f09-l09-time-off-requests-u25-care-coordinator-desktop-light.png) | ![Listed, U25, view Open: ToApprove, Approved, Refused, dark](../../images/lists/s-f09-l09-time-off-requests-u25-care-coordinator-desktop-dark.png) |
| Listed, U25, view Open: ToApprove, Approved, Refused | phone | ![Listed, U25, view Open: ToApprove, Approved, Refused, light](../../images/lists/s-f09-l09-time-off-requests-u25-care-coordinator-phone-light.png) | ![Listed, U25, view Open: ToApprove, Approved, Refused, dark](../../images/lists/s-f09-l09-time-off-requests-u25-care-coordinator-phone-dark.png) |
| Listed, U29, view Open: ToApprove, Approved, Refused | desktop | ![Listed, U29, view Open: ToApprove, Approved, Refused, light](../../images/lists/s-f09-l09-time-off-requests-u29-dispatcher-desktop-light.png) | ![Listed, U29, view Open: ToApprove, Approved, Refused, dark](../../images/lists/s-f09-l09-time-off-requests-u29-dispatcher-desktop-dark.png) |
| Listed, U29, view Open: ToApprove, Approved, Refused | phone | ![Listed, U29, view Open: ToApprove, Approved, Refused, light](../../images/lists/s-f09-l09-time-off-requests-u29-dispatcher-phone-light.png) | ![Listed, U29, view Open: ToApprove, Approved, Refused, dark](../../images/lists/s-f09-l09-time-off-requests-u29-dispatcher-phone-dark.png) |
| Listed, U26, view Open: ToApprove, Approved, Refused | desktop | ![Listed, U26, view Open: ToApprove, Approved, Refused, light](../../images/lists/s-f09-l09-time-off-requests-u26-carer-desktop-light.png) | ![Listed, U26, view Open: ToApprove, Approved, Refused, dark](../../images/lists/s-f09-l09-time-off-requests-u26-carer-desktop-dark.png) |
| Listed, U26, view Open: ToApprove, Approved, Refused | phone | ![Listed, U26, view Open: ToApprove, Approved, Refused, light](../../images/lists/s-f09-l09-time-off-requests-u26-carer-phone-light.png) | ![Listed, U26, view Open: ToApprove, Approved, Refused, dark](../../images/lists/s-f09-l09-time-off-requests-u26-carer-phone-dark.png) |
| Listed, U30, view Open: ToApprove, Approved, Refused | desktop | ![Listed, U30, view Open: ToApprove, Approved, Refused, light](../../images/lists/s-f09-l09-time-off-requests-u30-driver-desktop-light.png) | ![Listed, U30, view Open: ToApprove, Approved, Refused, dark](../../images/lists/s-f09-l09-time-off-requests-u30-driver-desktop-dark.png) |
| Listed, U30, view Open: ToApprove, Approved, Refused | phone | ![Listed, U30, view Open: ToApprove, Approved, Refused, light](../../images/lists/s-f09-l09-time-off-requests-u30-driver-phone-light.png) | ![Listed, U30, view Open: ToApprove, Approved, Refused, dark](../../images/lists/s-f09-l09-time-off-requests-u30-driver-phone-dark.png) |
| Listed, U09, view Open: ToApprove, Approved, Refused | desktop | ![Listed, U09, view Open: ToApprove, Approved, Refused, light](../../images/lists/s-f09-l09-time-off-requests-u09-customer-desktop-light.png) | ![Listed, U09, view Open: ToApprove, Approved, Refused, dark](../../images/lists/s-f09-l09-time-off-requests-u09-customer-desktop-dark.png) |
| Listed, U09, view Open: ToApprove, Approved, Refused | phone | ![Listed, U09, view Open: ToApprove, Approved, Refused, light](../../images/lists/s-f09-l09-time-off-requests-u09-customer-phone-light.png) | ![Listed, U09, view Open: ToApprove, Approved, Refused, dark](../../images/lists/s-f09-l09-time-off-requests-u09-customer-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [HR and projects › Time-off requests](README.md) |
| Workspaces | [U01](../../../../04-ux/views/u01-employee/workspace.md), [U02](../../../../04-ux/views/u02-manager/workspace.md), [U06](../../../../04-ux/views/u06-hr/workspace.md), [U25](../../../../04-ux/views/u25-care-coordinator/workspace.md), [U29](../../../../04-ux/views/u29-dispatcher/workspace.md), [U26](../../../../04-ux/views/u26-carer/workspace.md), [U30](../../../../04-ux/views/u30-driver/workspace.md), [U09](../../../../04-ux/views/u09-customer/workspace.md) |
| Flows | [FL-F13-08](../../../f13-payroll/flows/fl-f13-08-deductions-savings-and-leave-pay.md), [FL-F15-02](../../../f15-legal-assistant/flows/fl-f15-02-receive-a-legal-warning.md), [FL-F2-11](../../../f02-no-code-configuration/flows/fl-f02-11-rights-translations-and-approvals.md), [FL-F9-03](../../flows/fl-f09-03-time.md), [FL-F9-12](../../flows/fl-f09-12-schedule-customer-requests.md), [FL-F9-13](../../flows/fl-f09-13-keep-qualifications.md) |

## Open questions

None.

---

⬅️ [S-F9-L08 Time-off allocations](s-f09-l08-time-off-allocations.md) · ⬆️ [Up](README.md) ·
➡️ [S-F9-L10 Attendances](s-f09-l10-attendances.md)
