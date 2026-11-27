🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: HR and projects menu](README.md) ›
🗂️ S-F9-L18 Project and tasks

# 🗂️ S-F9-L18 Project and tasks

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U24 Engagement manager](../../../../01-users/personas/u24-engagement-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |
| [U03 Sales](../../../../01-users/personas/u03-sales.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U14 Field worker](../../../../01-users/personas/u14-field-worker.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U10 Supplier](../../../../01-users/personas/u10-supplier.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |
| [U06 Human resources](../../../../01-users/personas/u06-hr.md) | only the tasks assigned to them, such as the prepared LinkedIn messages of their outreach sequences (D570) | the saved view "Messages to send" and Send on each such task |

**Not embedded for:** U05, U22: their use cases only read these records, inside a screen of the use case, so they open
them from there (D493).

## Purpose

The aggregated list of every [E-F9-18 Project and task](../../data/e-f09-18-project-and-task.md) the user may see: to
find, filter, total and act on many project and tasks at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** HR and projects › Project and tasks, in the capability's menu (D495).
- **Workspaces:** 7 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "project and tasks" offers this view.
- **AI assistant:** "show the project and tasks that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Project and tasks    HR and projects › Project and tasks   [+ New]                                           |
| [count] [total budget]   [chart: count by state, budget stacked]                                             |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] PROJECT   STATE   BUDGET   MILESTONES                                                |
| milestones        | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Project | project | text | yes |
| State | state | badge: New, Planned, Active, Delivered, Done | yes |
| Budget | budget | amount, right-aligned | yes |
| Milestones | milestones | text | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | New, Planned, Active, Delivered, Done | the visible rows (D488) |
| Milestones | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Prepared outreach message: the tasks that carry one, for the HR user they are assigned to
  ([E-F9-47 Outreach message](../../data/e-f09-47-outreach-message.md)).

## KPI strip

- Count of the visible rows.
- Total of budget.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state, budget stacked (VR-8); the Chart button turns the filtered list into a chart the user can pin to their
home screen (C-09).

## Saved views

- All.
- Open: New, Planned, Active.
- Recently changed.
- Messages to send: the open tasks that carry a prepared outreach message, soonest to expire first (U06, D570).

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New project and task | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |
| Send | row, on a task carrying a prepared outreach message | the HR user the task is assigned to | the message goes out through Unipile within the account's limits (BR-F9-41); the task closes as Done, outcome sent (D570) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- milestones: editable in its cell unless the record's state locks it.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| worksheet | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| prepared outreach message | a prospect's personal data (BR-F9-39) | the HR user the task is assigned to, and HR as the [record rules](../../permissions.md#record-rules) allow | every other persona of this list: the task itself is not listed for them |

## Row opens

Open › goes to [S-F9-17 Projects](../06-plan-and-deliver-work/s-f09-17-projects.md).

The records also show on: [S-F9-18 Field service](../06-plan-and-deliver-work/s-f09-18-field-service.md),
[S-F9-26 Capacity planning](../11-capacity-rounds-and-partners/s-f09-26-capacity-planning.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 project and tasks of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no project and task the user may see yet, with the create action when allowed.
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
| Listed, U02, view Open: New, Planned, Active | desktop | ![Listed, U02, view Open: New, Planned, Active, light](../../images/lists/s-f09-l18-project-and-tasks-u02-manager-desktop-light.png) | ![Listed, U02, view Open: New, Planned, Active, dark](../../images/lists/s-f09-l18-project-and-tasks-u02-manager-desktop-dark.png) |
| Listed, U02, view Open: New, Planned, Active | phone | ![Listed, U02, view Open: New, Planned, Active, light](../../images/lists/s-f09-l18-project-and-tasks-u02-manager-phone-light.png) | ![Listed, U02, view Open: New, Planned, Active, dark](../../images/lists/s-f09-l18-project-and-tasks-u02-manager-phone-dark.png) |
| Listed, U24, view Open: New, Planned, Active | desktop | ![Listed, U24, view Open: New, Planned, Active, light](../../images/lists/s-f09-l18-project-and-tasks-u24-engagement-manager-desktop-light.png) | ![Listed, U24, view Open: New, Planned, Active, dark](../../images/lists/s-f09-l18-project-and-tasks-u24-engagement-manager-desktop-dark.png) |
| Listed, U24, view Open: New, Planned, Active | phone | ![Listed, U24, view Open: New, Planned, Active, light](../../images/lists/s-f09-l18-project-and-tasks-u24-engagement-manager-phone-light.png) | ![Listed, U24, view Open: New, Planned, Active, dark](../../images/lists/s-f09-l18-project-and-tasks-u24-engagement-manager-phone-dark.png) |
| Listed, U09, view Open: New, Planned, Active | desktop | ![Listed, U09, view Open: New, Planned, Active, light](../../images/lists/s-f09-l18-project-and-tasks-u09-customer-desktop-light.png) | ![Listed, U09, view Open: New, Planned, Active, dark](../../images/lists/s-f09-l18-project-and-tasks-u09-customer-desktop-dark.png) |
| Listed, U09, view Open: New, Planned, Active | phone | ![Listed, U09, view Open: New, Planned, Active, light](../../images/lists/s-f09-l18-project-and-tasks-u09-customer-phone-light.png) | ![Listed, U09, view Open: New, Planned, Active, dark](../../images/lists/s-f09-l18-project-and-tasks-u09-customer-phone-dark.png) |
| Listed, U03, view Open: New, Planned, Active | desktop | ![Listed, U03, view Open: New, Planned, Active, light](../../images/lists/s-f09-l18-project-and-tasks-u03-sales-desktop-light.png) | ![Listed, U03, view Open: New, Planned, Active, dark](../../images/lists/s-f09-l18-project-and-tasks-u03-sales-desktop-dark.png) |
| Listed, U03, view Open: New, Planned, Active | phone | ![Listed, U03, view Open: New, Planned, Active, light](../../images/lists/s-f09-l18-project-and-tasks-u03-sales-phone-light.png) | ![Listed, U03, view Open: New, Planned, Active, dark](../../images/lists/s-f09-l18-project-and-tasks-u03-sales-phone-dark.png) |
| Listed, U14, view Open: New, Planned, Active | desktop | ![Listed, U14, view Open: New, Planned, Active, light](../../images/lists/s-f09-l18-project-and-tasks-u14-field-worker-desktop-light.png) | ![Listed, U14, view Open: New, Planned, Active, dark](../../images/lists/s-f09-l18-project-and-tasks-u14-field-worker-desktop-dark.png) |
| Listed, U14, view Open: New, Planned, Active | phone | ![Listed, U14, view Open: New, Planned, Active, light](../../images/lists/s-f09-l18-project-and-tasks-u14-field-worker-phone-light.png) | ![Listed, U14, view Open: New, Planned, Active, dark](../../images/lists/s-f09-l18-project-and-tasks-u14-field-worker-phone-dark.png) |
| Listed, U13, view Open: New, Planned, Active | desktop | ![Listed, U13, view Open: New, Planned, Active, light](../../images/lists/s-f09-l18-project-and-tasks-u13-owner-desktop-light.png) | ![Listed, U13, view Open: New, Planned, Active, dark](../../images/lists/s-f09-l18-project-and-tasks-u13-owner-desktop-dark.png) |
| Listed, U13, view Open: New, Planned, Active | phone | ![Listed, U13, view Open: New, Planned, Active, light](../../images/lists/s-f09-l18-project-and-tasks-u13-owner-phone-light.png) | ![Listed, U13, view Open: New, Planned, Active, dark](../../images/lists/s-f09-l18-project-and-tasks-u13-owner-phone-dark.png) |
| Listed, U10, view Open: New, Planned, Active | desktop | ![Listed, U10, view Open: New, Planned, Active, light](../../images/lists/s-f09-l18-project-and-tasks-u10-supplier-desktop-light.png) | ![Listed, U10, view Open: New, Planned, Active, dark](../../images/lists/s-f09-l18-project-and-tasks-u10-supplier-desktop-dark.png) |
| Listed, U10, view Open: New, Planned, Active | phone | ![Listed, U10, view Open: New, Planned, Active, light](../../images/lists/s-f09-l18-project-and-tasks-u10-supplier-phone-light.png) | ![Listed, U10, view Open: New, Planned, Active, dark](../../images/lists/s-f09-l18-project-and-tasks-u10-supplier-phone-dark.png) |
| Listed, U06, view Messages to send | desktop | ![Listed, U06, view Messages to send, light](../../images/lists/s-f09-l18-project-and-tasks-u06-hr-desktop-light.png) | ![Listed, U06, view Messages to send, dark](../../images/lists/s-f09-l18-project-and-tasks-u06-hr-desktop-dark.png) |
| Listed, U06, view Messages to send | phone | ![Listed, U06, view Messages to send, light](../../images/lists/s-f09-l18-project-and-tasks-u06-hr-phone-light.png) | ![Listed, U06, view Messages to send, dark](../../images/lists/s-f09-l18-project-and-tasks-u06-hr-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [HR and projects › Project and tasks](README.md) |
| Workspaces | [U02](../../../../04-ux/views/u02-manager/workspace.md), [U24](../../../../04-ux/views/u24-engagement-manager/workspace.md), [U09](../../../../04-ux/views/u09-customer/workspace.md), [U03](../../../../04-ux/views/u03-sales/workspace.md), [U14](../../../../04-ux/views/u14-field-worker/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md), [U10](../../../../04-ux/views/u10-supplier/workspace.md), [U06](../../../../04-ux/views/u06-hr/workspace.md) |
| Flows | [FL-F13-05](../../../f13-payroll/flows/fl-f13-05-reports-and-rules.md), [FL-F24-02](../../../f24-integrations-hub/flows/fl-f24-02-office-suites.md), [FL-F3-09](../../../f03-assistant/flows/fl-f03-09-assistant-on-a-phone.md), [FL-F4-03](../../../f04-meetings/flows/fl-f04-03-review-a-meeting.md), [FL-F4-13](../../../f04-meetings/flows/fl-f04-13-outside-people-and-follow-up.md), [FL-F6-02](../../../f06-customers-and-sales/flows/fl-f06-02-quote-to-order.md), [FL-F9-06](../../flows/fl-f09-06-plan-and-deliver-work.md), [FL-F9-11](../../flows/fl-f09-11-capacity-rounds-and-partners.md), [FL-F9-12](../../flows/fl-f09-12-schedule-customer-requests.md), [FL-SC11-02](../../../../08-sectors/sc11-professional-firms/flows/fl-sc11-02-matters-and-documents.md), [FL-SC14-04](../../../../08-sectors/sc14-it-and-software/flows/fl-sc14-04-product-delivery.md) |

## Open questions

None.

---

⬅️ [S-F9-L17 Timesheet lines](s-f09-l17-timesheet-lines.md) · ⬆️ [Up](README.md) ·
➡️ [S-F9-L19 Contract templates](s-f09-l19-contract-templates.md)
