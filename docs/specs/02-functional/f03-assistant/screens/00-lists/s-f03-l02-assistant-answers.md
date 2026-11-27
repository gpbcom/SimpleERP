🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🤖 [F3 Assistant](../../README.md) ›
🖥️ [Screens](../README.md) › 🗂️ [Views: Assistant menu](README.md) › 🗂️ S-F3-L02 Assistant answers

# 🗂️ S-F3-L02 Assistant answers

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U01 Employee](../../../../01-users/personas/u01-employee.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U08 External accountant](../../../../01-users/personas/u08-external-accountant.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U03 Sales](../../../../01-users/personas/u03-sales.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U04 Purchasing and stock](../../../../01-users/personas/u04-purchasing.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U06 Human resources](../../../../01-users/personas/u06-hr.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U14 Field worker](../../../../01-users/personas/u14-field-worker.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U15 Warehouse operator](../../../../01-users/personas/u15-warehouse-operator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U16 Office worker](../../../../01-users/personas/u16-office-worker.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

- Every AI assistant user sees their own records, as the F3 use cases list them (D519).

## Purpose

The aggregated list of every [E-F3-02 Assistant answer](../../data/e-f03-02-assistant-answer.md) the user may see: to
find, filter, total and act on many assistant answers at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Assistant › Assistant answers, in the capability's menu (D495).
- **Workspaces:** 13 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "assistant answers" offers this view.
- **AI assistant:** "show the assistant answers that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Assistant answers    Assistant › Assistant answers   [+ New]                                                 |
| [count]   [chart: count by state]                                                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] QUESTION   STATE   KIND                                                              |
| kind              | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Question | question | text | yes |
| State | state | badge: Recorded | yes |
| Kind | kind | text | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Recorded | the visible rows (D488) |
| Kind | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: assistant answers link to no other record type in their fields.

## KPI strip

- Count of the visible rows.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New assistant answer | header | the personas whose roles may create it | the record's own page (Row opens) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- kind: editable in its cell unless the record's state locks it.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| question | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| text | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F3-01 Assistant panel](../01-ask-the-assistant/s-f03-01-assistant-panel.md).

The records also show on: [S-F3-03 Writing style settings](../04-summarise-or-draft/s-f03-03-writing-style-settings.md),
[S-F3-19 Injection alerts](../11-trust-the-answers/s-f03-19-injection-alerts.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 assistant answers of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no assistant answer the user may see yet, with the create action when allowed.
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
| Listed, U13, view All | desktop | ![Listed, U13, view All, light](../../images/lists/s-f03-l02-assistant-answers-u13-owner-desktop-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f03-l02-assistant-answers-u13-owner-desktop-dark.png) |
| Listed, U13, view All | phone | ![Listed, U13, view All, light](../../images/lists/s-f03-l02-assistant-answers-u13-owner-phone-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f03-l02-assistant-answers-u13-owner-phone-dark.png) |
| Listed, U07, view All | desktop | ![Listed, U07, view All, light](../../images/lists/s-f03-l02-assistant-answers-u07-administrator-desktop-light.png) | ![Listed, U07, view All, dark](../../images/lists/s-f03-l02-assistant-answers-u07-administrator-desktop-dark.png) |
| Listed, U07, view All | phone | ![Listed, U07, view All, light](../../images/lists/s-f03-l02-assistant-answers-u07-administrator-phone-light.png) | ![Listed, U07, view All, dark](../../images/lists/s-f03-l02-assistant-answers-u07-administrator-phone-dark.png) |
| Listed, U01, view All | desktop | ![Listed, U01, view All, light](../../images/lists/s-f03-l02-assistant-answers-u01-employee-desktop-light.png) | ![Listed, U01, view All, dark](../../images/lists/s-f03-l02-assistant-answers-u01-employee-desktop-dark.png) |
| Listed, U01, view All | phone | ![Listed, U01, view All, light](../../images/lists/s-f03-l02-assistant-answers-u01-employee-phone-light.png) | ![Listed, U01, view All, dark](../../images/lists/s-f03-l02-assistant-answers-u01-employee-phone-dark.png) |
| Listed, U05, view All | desktop | ![Listed, U05, view All, light](../../images/lists/s-f03-l02-assistant-answers-u05-accounting-desktop-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-f03-l02-assistant-answers-u05-accounting-desktop-dark.png) |
| Listed, U05, view All | phone | ![Listed, U05, view All, light](../../images/lists/s-f03-l02-assistant-answers-u05-accounting-phone-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-f03-l02-assistant-answers-u05-accounting-phone-dark.png) |
| Listed, U08, view All | desktop | ![Listed, U08, view All, light](../../images/lists/s-f03-l02-assistant-answers-u08-external-accountant-desktop-light.png) | ![Listed, U08, view All, dark](../../images/lists/s-f03-l02-assistant-answers-u08-external-accountant-desktop-dark.png) |
| Listed, U08, view All | phone | ![Listed, U08, view All, light](../../images/lists/s-f03-l02-assistant-answers-u08-external-accountant-phone-light.png) | ![Listed, U08, view All, dark](../../images/lists/s-f03-l02-assistant-answers-u08-external-accountant-phone-dark.png) |
| Listed, U02, view All | desktop | ![Listed, U02, view All, light](../../images/lists/s-f03-l02-assistant-answers-u02-manager-desktop-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-f03-l02-assistant-answers-u02-manager-desktop-dark.png) |
| Listed, U02, view All | phone | ![Listed, U02, view All, light](../../images/lists/s-f03-l02-assistant-answers-u02-manager-phone-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-f03-l02-assistant-answers-u02-manager-phone-dark.png) |
| Listed, U03, view All | desktop | ![Listed, U03, view All, light](../../images/lists/s-f03-l02-assistant-answers-u03-sales-desktop-light.png) | ![Listed, U03, view All, dark](../../images/lists/s-f03-l02-assistant-answers-u03-sales-desktop-dark.png) |
| Listed, U03, view All | phone | ![Listed, U03, view All, light](../../images/lists/s-f03-l02-assistant-answers-u03-sales-phone-light.png) | ![Listed, U03, view All, dark](../../images/lists/s-f03-l02-assistant-answers-u03-sales-phone-dark.png) |
| Listed, U04, view All | desktop | ![Listed, U04, view All, light](../../images/lists/s-f03-l02-assistant-answers-u04-purchasing-desktop-light.png) | ![Listed, U04, view All, dark](../../images/lists/s-f03-l02-assistant-answers-u04-purchasing-desktop-dark.png) |
| Listed, U04, view All | phone | ![Listed, U04, view All, light](../../images/lists/s-f03-l02-assistant-answers-u04-purchasing-phone-light.png) | ![Listed, U04, view All, dark](../../images/lists/s-f03-l02-assistant-answers-u04-purchasing-phone-dark.png) |
| Listed, U06, view All | desktop | ![Listed, U06, view All, light](../../images/lists/s-f03-l02-assistant-answers-u06-hr-desktop-light.png) | ![Listed, U06, view All, dark](../../images/lists/s-f03-l02-assistant-answers-u06-hr-desktop-dark.png) |
| Listed, U06, view All | phone | ![Listed, U06, view All, light](../../images/lists/s-f03-l02-assistant-answers-u06-hr-phone-light.png) | ![Listed, U06, view All, dark](../../images/lists/s-f03-l02-assistant-answers-u06-hr-phone-dark.png) |
| Listed, U12, view All | desktop | ![Listed, U12, view All, light](../../images/lists/s-f03-l02-assistant-answers-u12-marketing-desktop-light.png) | ![Listed, U12, view All, dark](../../images/lists/s-f03-l02-assistant-answers-u12-marketing-desktop-dark.png) |
| Listed, U12, view All | phone | ![Listed, U12, view All, light](../../images/lists/s-f03-l02-assistant-answers-u12-marketing-phone-light.png) | ![Listed, U12, view All, dark](../../images/lists/s-f03-l02-assistant-answers-u12-marketing-phone-dark.png) |
| Listed, U14, view All | desktop | ![Listed, U14, view All, light](../../images/lists/s-f03-l02-assistant-answers-u14-field-worker-desktop-light.png) | ![Listed, U14, view All, dark](../../images/lists/s-f03-l02-assistant-answers-u14-field-worker-desktop-dark.png) |
| Listed, U14, view All | phone | ![Listed, U14, view All, light](../../images/lists/s-f03-l02-assistant-answers-u14-field-worker-phone-light.png) | ![Listed, U14, view All, dark](../../images/lists/s-f03-l02-assistant-answers-u14-field-worker-phone-dark.png) |
| Listed, U15, view All | desktop | ![Listed, U15, view All, light](../../images/lists/s-f03-l02-assistant-answers-u15-warehouse-operator-desktop-light.png) | ![Listed, U15, view All, dark](../../images/lists/s-f03-l02-assistant-answers-u15-warehouse-operator-desktop-dark.png) |
| Listed, U15, view All | phone | ![Listed, U15, view All, light](../../images/lists/s-f03-l02-assistant-answers-u15-warehouse-operator-phone-light.png) | ![Listed, U15, view All, dark](../../images/lists/s-f03-l02-assistant-answers-u15-warehouse-operator-phone-dark.png) |
| Listed, U16, view All | desktop | ![Listed, U16, view All, light](../../images/lists/s-f03-l02-assistant-answers-u16-office-worker-desktop-light.png) | ![Listed, U16, view All, dark](../../images/lists/s-f03-l02-assistant-answers-u16-office-worker-desktop-dark.png) |
| Listed, U16, view All | phone | ![Listed, U16, view All, light](../../images/lists/s-f03-l02-assistant-answers-u16-office-worker-phone-light.png) | ![Listed, U16, view All, dark](../../images/lists/s-f03-l02-assistant-answers-u16-office-worker-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Assistant › Assistant answers](README.md) |
| Workspaces | [U13](../../../../04-ux/views/u13-owner/workspace.md), [U07](../../../../04-ux/views/u07-administrator/workspace.md), [U01](../../../../04-ux/views/u01-employee/workspace.md), [U05](../../../../04-ux/views/u05-accounting/workspace.md), [U08](../../../../04-ux/views/u08-external-accountant/workspace.md), [U02](../../../../04-ux/views/u02-manager/workspace.md), [U03](../../../../04-ux/views/u03-sales/workspace.md), [U04](../../../../04-ux/views/u04-purchasing/workspace.md), [U06](../../../../04-ux/views/u06-hr/workspace.md), [U12](../../../../04-ux/views/u12-marketing/workspace.md), [U14](../../../../04-ux/views/u14-field-worker/workspace.md), [U15](../../../../04-ux/views/u15-warehouse-operator/workspace.md), [U16](../../../../04-ux/views/u16-office-worker/workspace.md) |
| Flows | [FL-F12-08](../../../f12-manufacturing/flows/fl-f12-08-report-and-assist.md), [FL-F13-06](../../../f13-payroll/flows/fl-f13-06-assistant.md), [FL-F15-01](../../../f15-legal-assistant/flows/fl-f15-01-ask-a-legal-question.md), [FL-F16-01](../../../f16-customer-support-agents/flows/fl-f16-01-resolve-a-request.md), [FL-F24-07](../../../f24-integrations-hub/flows/fl-f24-07-employees-and-their-tools.md), [FL-F3-01](../../flows/fl-f03-01-ask-the-assistant.md), [FL-F3-02](../../flows/fl-f03-02-ask-about-the-screen.md), [FL-F3-04](../../flows/fl-f03-04-summarise-or-draft.md), [FL-F3-07](../../flows/fl-f03-07-manage-knowledge.md), [FL-F3-09](../../flows/fl-f03-09-assistant-on-a-phone.md), [FL-F3-11](../../flows/fl-f03-11-trust-the-answers.md), [FL-F3-12](../../flows/fl-f03-12-personal-cost-aware-and-learning.md), [FL-F4-01](../../../f04-meetings/flows/fl-f04-01-record-an-online-meeting.md) |

## Open questions

None.

---

⬅️ [S-F3-L01 Conversations](s-f03-l01-conversations.md) · ⬆️ [Up](README.md) ·
➡️ [S-F3-L03 Suggested questions](s-f03-l03-suggested-questions.md)
