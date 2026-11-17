🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💶 [F13 Payroll (plugin)](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: Payroll (plugin) menu](README.md) ›
🗂️ S-F13-L03 Pay inputs

# 🗂️ S-F13-L03 Pay inputs

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U45 Payroll officer](../../../../01-users/personas/u45-payroll-officer.md) | as the permissions row "Pay inputs": ✅ | actions as [permissions](../../permissions.md) gives them |
| [U06 Human resources](../../../../01-users/personas/u06-hr.md) | as the permissions row "Pay inputs": ✅ | actions as [permissions](../../permissions.md) gives them |
| [U14 Field worker](../../../../01-users/personas/u14-field-worker.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U29 Dispatcher](../../../../01-users/personas/u29-dispatcher.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U08: their use cases only read these records, inside a screen of the use case, so they open them
from there (D493).

## Purpose

The aggregated list of every [E-F13-03 Pay input](../../data/e-f13-03-pay-input.md) the user may see: to find, filter,
total and act on many pay inputs at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Payroll (plugin) › Pay inputs, in the capability's menu (D495).
- **Workspaces:** 4 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "pay inputs" offers this view.
- **AI assistant:** "show the pay inputs that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Pay inputs    Payroll (plugin) › Pay inputs   [+ New]                                                        |
| [count] [Open] [new this month]   [chart: count by state]                                                    |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] EMPLOYEE   STATE   PERIOD   KIND                                                     |
| employee          | [ ] ...                                                  Open >                          |
| kind              | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Employee | employee | link to the record | yes |
| State | state | badge: Open, Complete, Closed, Late | yes |
| Period | period | link to the record | yes |
| Kind | kind | link to the record | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Open, Complete, Closed, Late | the visible rows (D488) |
| Employee | each linked employee | the visible rows (D488) |
| Kind | each linked kind | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: pay inputs link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Open.
- New this month, by period.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Mine: employee.
- Open: Open, Complete, Late.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New pay input | header | the personas whose roles may create it | the record's own page (Row opens) |
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

- period: editable in its cell unless the record's state locks it.
- kind: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F13-03 Pay inputs](../02-monthly-pay-run/s-f13-03-pay-inputs.md).

The records also show on: [S-F13-05 Agreement rules](../02-monthly-pay-run/s-f13-05-agreement-rules.md),
[S-F13-14 Sick leave](../04-events/s-f13-14-sick-leave.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 pay inputs of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no pay input the user may see yet, with the create action when allowed.
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
| Listed, U45, view Mine: employee | desktop | ![Listed, U45, view Mine: employee, light](../../images/lists/s-f13-l03-pay-inputs-u45-payroll-officer-desktop-light.png) | ![Listed, U45, view Mine: employee, dark](../../images/lists/s-f13-l03-pay-inputs-u45-payroll-officer-desktop-dark.png) |
| Listed, U45, view Mine: employee | phone | ![Listed, U45, view Mine: employee, light](../../images/lists/s-f13-l03-pay-inputs-u45-payroll-officer-phone-light.png) | ![Listed, U45, view Mine: employee, dark](../../images/lists/s-f13-l03-pay-inputs-u45-payroll-officer-phone-dark.png) |
| Listed, U06, view Needs attention | desktop | ![Listed, U06, view Needs attention, light](../../images/lists/s-f13-l03-pay-inputs-u06-hr-desktop-light.png) | ![Listed, U06, view Needs attention, dark](../../images/lists/s-f13-l03-pay-inputs-u06-hr-desktop-dark.png) |
| Listed, U06, view Needs attention | phone | ![Listed, U06, view Needs attention, light](../../images/lists/s-f13-l03-pay-inputs-u06-hr-phone-light.png) | ![Listed, U06, view Needs attention, dark](../../images/lists/s-f13-l03-pay-inputs-u06-hr-phone-dark.png) |
| Listed, U14, view Mine | desktop | ![Listed, U14, view Mine, light](../../images/lists/s-f13-l03-pay-inputs-u14-field-worker-desktop-light.png) | ![Listed, U14, view Mine, dark](../../images/lists/s-f13-l03-pay-inputs-u14-field-worker-desktop-dark.png) |
| Listed, U14, view Mine | phone | ![Listed, U14, view Mine, light](../../images/lists/s-f13-l03-pay-inputs-u14-field-worker-phone-light.png) | ![Listed, U14, view Mine, dark](../../images/lists/s-f13-l03-pay-inputs-u14-field-worker-phone-dark.png) |
| Listed, U29, view Mine | desktop | ![Listed, U29, view Mine, light](../../images/lists/s-f13-l03-pay-inputs-u29-dispatcher-desktop-light.png) | ![Listed, U29, view Mine, dark](../../images/lists/s-f13-l03-pay-inputs-u29-dispatcher-desktop-dark.png) |
| Listed, U29, view Mine | phone | ![Listed, U29, view Mine, light](../../images/lists/s-f13-l03-pay-inputs-u29-dispatcher-phone-light.png) | ![Listed, U29, view Mine, dark](../../images/lists/s-f13-l03-pay-inputs-u29-dispatcher-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Payroll (plugin) › Pay inputs](README.md) |
| Workspaces | [U45](../../../../04-ux/views/u45-payroll-officer/workspace.md), [U06](../../../../04-ux/views/u06-hr/workspace.md), [U14](../../../../04-ux/views/u14-field-worker/workspace.md), [U29](../../../../04-ux/views/u29-dispatcher/workspace.md) |
| Flows | [FL-F13-02](../../flows/fl-f13-02-monthly-pay-run.md), [FL-F13-04](../../flows/fl-f13-04-events.md), [FL-F13-09](../../flows/fl-f13-09-collective-agreements-by-family.md), [FL-F6-09](../../../f06-customers-and-sales/flows/fl-f06-09-sell-on-the-road-and-steer-sales.md), [FL-F9-03](../../../f09-hr-and-projects/flows/fl-f09-03-time.md), [FL-F9-11](../../../f09-hr-and-projects/flows/fl-f09-11-capacity-rounds-and-partners.md), [FL-SC04-04](../../../../08-sectors/sc04-home-care/flows/fl-sc04-04-bill-and-fund.md), [FL-SC13-03](../../../../08-sectors/sc13-agriculture-and-food/flows/fl-sc13-03-farm-business.md), [FL-SC16-01](../../../../08-sectors/sc16-events-and-culture/flows/fl-sc16-01-plan-and-book.md) |

## Open questions

None.

---

⬅️ [S-F13-L02 Employee pay profiles](s-f13-l02-employee-pay-profiles.md) · ⬆️ [Up](README.md) ·
➡️ [S-F13-L04 Payslip lines](s-f13-l04-payslip-lines.md)
