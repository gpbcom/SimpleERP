🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💶 [F13 Payroll (plugin)](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: Payroll (plugin) menu](README.md) ›
🗂️ S-F13-L02 Employee pay profiles

# 🗂️ S-F13-L02 Employee pay profiles

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U45 Payroll officer](../../../../01-users/personas/u45-payroll-officer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U06 Human resources](../../../../01-users/personas/u06-hr.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U25 Care coordinator](../../../../01-users/personas/u25-care-coordinator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U01, U14, U23, U24, U52: their use cases only read these records, inside a screen of the use case,
so they open them from there (D493).

## Purpose

The aggregated list of every [E-F13-02 Employee pay profile](../../data/e-f13-02-employee-pay-profile.md) the user may
see: to find, filter, total and act on many employee pay profiles at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Payroll (plugin) › Employee pay profiles, in the capability's menu (D495).
- **Workspaces:** 4 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "employee pay profiles" offers this view.
- **AI assistant:** "show the employee pay profiles that need attention" opens it with the filter as editable chips
  (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Employee pay profiles    Payroll (plugin) › Employee pay profiles   [+ New]                                  |
| [count]   [chart: count by state]                                                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] EMPLOYEE   STATE   BENEFITS                                                          |
| employee          | [ ] ...                                                  Open >                          |
| benefits          | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Employee | employee | link to the record | yes |
| State | state | badge: Checked, Complete | yes |
| Benefits | benefits | text | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Checked, Complete | the visible rows (D488) |
| Employee | each linked employee | the visible rows (D488) |
| Benefits | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: employee pay profiles link to no other record type in their fields.

## KPI strip

- Count of the visible rows.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Mine: employee.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New employee pay profile | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Assign | bulk bar | the personas whose roles may assign | sets the employee; audited |
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
| benefits | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F13-02 Employee pay](../01-set-up/s-f13-02-employee-pay.md).

The records also show on: [S-F13-17 Benefits](../04-events/s-f13-17-benefits.md),
[S-F13-21 Schemes](../07-schemes-and-special-contracts/s-f13-21-schemes.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 employee pay profiles of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no employee pay profile the user may see yet, with the create action when allowed.
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
| Listed, U45, view Mine: employee | desktop | ![Listed, U45, view Mine: employee, light](../../images/lists/s-f13-l02-employee-pay-profiles-u45-payroll-officer-desktop-light.png) | ![Listed, U45, view Mine: employee, dark](../../images/lists/s-f13-l02-employee-pay-profiles-u45-payroll-officer-desktop-dark.png) |
| Listed, U45, view Mine: employee | phone | ![Listed, U45, view Mine: employee, light](../../images/lists/s-f13-l02-employee-pay-profiles-u45-payroll-officer-phone-light.png) | ![Listed, U45, view Mine: employee, dark](../../images/lists/s-f13-l02-employee-pay-profiles-u45-payroll-officer-phone-dark.png) |
| Listed, U06, view All | desktop | ![Listed, U06, view All, light](../../images/lists/s-f13-l02-employee-pay-profiles-u06-hr-desktop-light.png) | ![Listed, U06, view All, dark](../../images/lists/s-f13-l02-employee-pay-profiles-u06-hr-desktop-dark.png) |
| Listed, U06, view All | phone | ![Listed, U06, view All, light](../../images/lists/s-f13-l02-employee-pay-profiles-u06-hr-phone-light.png) | ![Listed, U06, view All, dark](../../images/lists/s-f13-l02-employee-pay-profiles-u06-hr-phone-dark.png) |
| Listed, U09, view Mine | desktop | ![Listed, U09, view Mine, light](../../images/lists/s-f13-l02-employee-pay-profiles-u09-customer-desktop-light.png) | ![Listed, U09, view Mine, dark](../../images/lists/s-f13-l02-employee-pay-profiles-u09-customer-desktop-dark.png) |
| Listed, U09, view Mine | phone | ![Listed, U09, view Mine, light](../../images/lists/s-f13-l02-employee-pay-profiles-u09-customer-phone-light.png) | ![Listed, U09, view Mine, dark](../../images/lists/s-f13-l02-employee-pay-profiles-u09-customer-phone-dark.png) |
| Listed, U25, view Mine | desktop | ![Listed, U25, view Mine, light](../../images/lists/s-f13-l02-employee-pay-profiles-u25-care-coordinator-desktop-light.png) | ![Listed, U25, view Mine, dark](../../images/lists/s-f13-l02-employee-pay-profiles-u25-care-coordinator-desktop-dark.png) |
| Listed, U25, view Mine | phone | ![Listed, U25, view Mine, light](../../images/lists/s-f13-l02-employee-pay-profiles-u25-care-coordinator-phone-light.png) | ![Listed, U25, view Mine, dark](../../images/lists/s-f13-l02-employee-pay-profiles-u25-care-coordinator-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Payroll (plugin) › Employee pay profiles](README.md) |
| Workspaces | [U45](../../../../04-ux/views/u45-payroll-officer/workspace.md), [U06](../../../../04-ux/views/u06-hr/workspace.md), [U09](../../../../04-ux/views/u09-customer/workspace.md), [U25](../../../../04-ux/views/u25-care-coordinator/workspace.md) |
| Flows | [FL-F13-01](../../flows/fl-f13-01-set-up.md), [FL-F13-04](../../flows/fl-f13-04-events.md), [FL-F13-07](../../flows/fl-f13-07-schemes-and-special-contracts.md) |

## Open questions

None.

---

⬅️ [S-F13-L01 Payroll establishments](s-f13-l01-payroll-establishments.md) · ⬆️ [Up](README.md) ·
➡️ [S-F13-L03 Pay inputs](s-f13-l03-pay-inputs.md)
