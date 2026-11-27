🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: HR and projects menu](README.md) ›
🗂️ S-F9-L16 Shifts

# 🗂️ S-F9-L16 Shifts

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U26 Carer](../../../../01-users/personas/u26-carer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U30 Driver](../../../../01-users/personas/u30-driver.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | as the permissions row "Shifts": ✅ plan | actions as [permissions](../../permissions.md) gives them |
| [U14 Field worker](../../../../01-users/personas/u14-field-worker.md) | as the permissions row "Shifts": see, swap | actions as [permissions](../../permissions.md) gives them |
| [U25 Care coordinator](../../../../01-users/personas/u25-care-coordinator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U29 Dispatcher](../../../../01-users/personas/u29-dispatcher.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U42 Sales representative](../../../../01-users/personas/u42-sales-representative.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U53 Coach](../../../../01-users/personas/u53-coach.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U09, U23, U52: their use cases only read these records, inside a screen of the use case, so they
open them from there (D493).

## Purpose

The aggregated list of every [E-F9-16 Shift](../../data/e-f09-16-shift.md) the user may see: to find, filter, total and
act on many shifts at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** HR and projects › Shifts, in the capability's menu (D495).
- **Workspaces:** 9 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "shifts" offers this view.
- **AI assistant:** "show the shifts that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Shifts    HR and projects › Shifts   [+ New]                                                                 |
| [count] [Draft]   [chart: count by state]                                                                    |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| role              | [ ] RESOURCE   STATE   ROLE                                                              |
| state             | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Resource | resource | text | yes |
| State | state | badge: Draft, Published | yes |
| Role | role | text | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| Role | each value | the visible rows (D488) |
| State | Draft, Published | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: shifts link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Draft.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Mine: role.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New shift | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Assign | bulk bar | the personas whose roles may assign | sets the role; audited |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- role: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F9-04 My HR](../01-people/s-f09-04-my-hr.md).

The records also show on: [S-F9-15 Planning](../06-plan-and-deliver-work/s-f09-15-planning.md),
[S-F9-18 Field service](../06-plan-and-deliver-work/s-f09-18-field-service.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 shifts of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no shift the user may see yet, with the create action when allowed.
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
| Listed, U26, view Mine: role | desktop | ![Listed, U26, view Mine: role, light](../../images/lists/s-f09-l16-shifts-u26-carer-desktop-light.png) | ![Listed, U26, view Mine: role, dark](../../images/lists/s-f09-l16-shifts-u26-carer-desktop-dark.png) |
| Listed, U26, view Mine: role | phone | ![Listed, U26, view Mine: role, light](../../images/lists/s-f09-l16-shifts-u26-carer-phone-light.png) | ![Listed, U26, view Mine: role, dark](../../images/lists/s-f09-l16-shifts-u26-carer-phone-dark.png) |
| Listed, U30, view Mine: role | desktop | ![Listed, U30, view Mine: role, light](../../images/lists/s-f09-l16-shifts-u30-driver-desktop-light.png) | ![Listed, U30, view Mine: role, dark](../../images/lists/s-f09-l16-shifts-u30-driver-desktop-dark.png) |
| Listed, U30, view Mine: role | phone | ![Listed, U30, view Mine: role, light](../../images/lists/s-f09-l16-shifts-u30-driver-phone-light.png) | ![Listed, U30, view Mine: role, dark](../../images/lists/s-f09-l16-shifts-u30-driver-phone-dark.png) |
| Listed, U02, view Needs attention | desktop | ![Listed, U02, view Needs attention, light](../../images/lists/s-f09-l16-shifts-u02-manager-desktop-light.png) | ![Listed, U02, view Needs attention, dark](../../images/lists/s-f09-l16-shifts-u02-manager-desktop-dark.png) |
| Listed, U02, view Needs attention | phone | ![Listed, U02, view Needs attention, light](../../images/lists/s-f09-l16-shifts-u02-manager-phone-light.png) | ![Listed, U02, view Needs attention, dark](../../images/lists/s-f09-l16-shifts-u02-manager-phone-dark.png) |
| Listed, U14, view Mine: role | desktop | ![Listed, U14, view Mine: role, light](../../images/lists/s-f09-l16-shifts-u14-field-worker-desktop-light.png) | ![Listed, U14, view Mine: role, dark](../../images/lists/s-f09-l16-shifts-u14-field-worker-desktop-dark.png) |
| Listed, U14, view Mine: role | phone | ![Listed, U14, view Mine: role, light](../../images/lists/s-f09-l16-shifts-u14-field-worker-phone-light.png) | ![Listed, U14, view Mine: role, dark](../../images/lists/s-f09-l16-shifts-u14-field-worker-phone-dark.png) |
| Listed, U25, view Needs attention | desktop | ![Listed, U25, view Needs attention, light](../../images/lists/s-f09-l16-shifts-u25-care-coordinator-desktop-light.png) | ![Listed, U25, view Needs attention, dark](../../images/lists/s-f09-l16-shifts-u25-care-coordinator-desktop-dark.png) |
| Listed, U25, view Needs attention | phone | ![Listed, U25, view Needs attention, light](../../images/lists/s-f09-l16-shifts-u25-care-coordinator-phone-light.png) | ![Listed, U25, view Needs attention, dark](../../images/lists/s-f09-l16-shifts-u25-care-coordinator-phone-dark.png) |
| Listed, U29, view Needs attention | desktop | ![Listed, U29, view Needs attention, light](../../images/lists/s-f09-l16-shifts-u29-dispatcher-desktop-light.png) | ![Listed, U29, view Needs attention, dark](../../images/lists/s-f09-l16-shifts-u29-dispatcher-desktop-dark.png) |
| Listed, U29, view Needs attention | phone | ![Listed, U29, view Needs attention, light](../../images/lists/s-f09-l16-shifts-u29-dispatcher-phone-light.png) | ![Listed, U29, view Needs attention, dark](../../images/lists/s-f09-l16-shifts-u29-dispatcher-phone-dark.png) |
| Listed, U42, view Mine: role | desktop | ![Listed, U42, view Mine: role, light](../../images/lists/s-f09-l16-shifts-u42-sales-representative-desktop-light.png) | ![Listed, U42, view Mine: role, dark](../../images/lists/s-f09-l16-shifts-u42-sales-representative-desktop-dark.png) |
| Listed, U42, view Mine: role | phone | ![Listed, U42, view Mine: role, light](../../images/lists/s-f09-l16-shifts-u42-sales-representative-phone-light.png) | ![Listed, U42, view Mine: role, dark](../../images/lists/s-f09-l16-shifts-u42-sales-representative-phone-dark.png) |
| Listed, U13, view Needs attention | desktop | ![Listed, U13, view Needs attention, light](../../images/lists/s-f09-l16-shifts-u13-owner-desktop-light.png) | ![Listed, U13, view Needs attention, dark](../../images/lists/s-f09-l16-shifts-u13-owner-desktop-dark.png) |
| Listed, U13, view Needs attention | phone | ![Listed, U13, view Needs attention, light](../../images/lists/s-f09-l16-shifts-u13-owner-phone-light.png) | ![Listed, U13, view Needs attention, dark](../../images/lists/s-f09-l16-shifts-u13-owner-phone-dark.png) |
| Listed, U53, view Mine | desktop | ![Listed, U53, view Mine, light](../../images/lists/s-f09-l16-shifts-u53-coach-desktop-light.png) | ![Listed, U53, view Mine, dark](../../images/lists/s-f09-l16-shifts-u53-coach-desktop-dark.png) |
| Listed, U53, view Mine | phone | ![Listed, U53, view Mine, light](../../images/lists/s-f09-l16-shifts-u53-coach-phone-light.png) | ![Listed, U53, view Mine, dark](../../images/lists/s-f09-l16-shifts-u53-coach-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [HR and projects › Shifts](README.md) |
| Workspaces | [U26](../../../../04-ux/views/u26-carer/workspace.md), [U30](../../../../04-ux/views/u30-driver/workspace.md), [U02](../../../../04-ux/views/u02-manager/workspace.md), [U14](../../../../04-ux/views/u14-field-worker/workspace.md), [U25](../../../../04-ux/views/u25-care-coordinator/workspace.md), [U29](../../../../04-ux/views/u29-dispatcher/workspace.md), [U42](../../../../04-ux/views/u42-sales-representative/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md), [U53](../../../../04-ux/views/u53-coach/workspace.md) |
| Flows | [FL-F15-02](../../../f15-legal-assistant/flows/fl-f15-02-receive-a-legal-warning.md), [FL-F23-03](../../../f23-what-if-simulation/flows/fl-f23-03-see-the-impact.md), [FL-F9-06](../../flows/fl-f09-06-plan-and-deliver-work.md), [FL-F9-11](../../flows/fl-f09-11-capacity-rounds-and-partners.md), [FL-F9-12](../../flows/fl-f09-12-schedule-customer-requests.md), [FL-SC02-04](../../../../08-sectors/sc02-retail/flows/fl-sc02-04-customers-and-staff.md), [FL-SC04-04](../../../../08-sectors/sc04-home-care/flows/fl-sc04-04-bill-and-fund.md) |

## Open questions

None.

---

⬅️ [S-F9-L15 Visitors](s-f09-l15-visitors.md) · ⬆️ [Up](README.md) ·
➡️ [S-F9-L17 Timesheet lines](s-f09-l17-timesheet-lines.md)
