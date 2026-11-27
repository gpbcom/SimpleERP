🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🤖 [F3 Assistant](../../README.md) ›
🖥️ [Screens](../README.md) › 🗂️ [Views: Assistant menu](README.md) › 🗂️ S-F3-L14 Answer feedbacks

# 🗂️ S-F3-L14 Answer feedbacks

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U01 Employee](../../../../01-users/personas/u01-employee.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U03 Sales](../../../../01-users/personas/u03-sales.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U04 Purchasing and stock](../../../../01-users/personas/u04-purchasing.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U06 Human resources](../../../../01-users/personas/u06-hr.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U14 Field worker](../../../../01-users/personas/u14-field-worker.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U15 Warehouse operator](../../../../01-users/personas/u15-warehouse-operator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U16 Office worker](../../../../01-users/personas/u16-office-worker.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

- The owner's review (VC-6, D519): "Create persona(s) related to this enitity."
- Every AI assistant user sees their own records.
- U07 Administrator and U13 Owner also curate the feedback, as they set up the AI assistant (F3 permissions); they never
  read the conversations behind it (BR-F3-33).

## Purpose

The aggregated list of every [E-F3-14 Answer feedback](../../data/e-f03-14-answer-feedback.md) the user may see: to
find, filter, total and act on many answer feedbacks at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Assistant › Answer feedbacks, in the capability's menu (D495).
- **Workspaces:** 12 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "answer feedbacks" offers this view.
- **AI assistant:** "show the answer feedbacks that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Answer feedbacks    Assistant › Answer feedbacks   [+ New]                                                   |
| [count] [new this month]   [chart: count by state]                                                           |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] ANSWER   STATE   RATING   REASON                                                     |
| answer            | [ ] ...                                                  Open >                          |
| rating            | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Answer | answer | text | yes |
| State | state | badge: Recorded | yes |
| Rating | rating | label | yes |
| Reason | reason | date | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Recorded | the visible rows (D488) |
| Answer | each value | the visible rows (D488) |
| Rating | up, down | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Answer feedbacks of a chosen answer, or of the answers that match a filter.
- From the other side: the answers that have answer feedbacks, or none.
- Answer feedbacks of a chosen rating, or of the ratings that match a filter.
- From the other side: the ratings that have answer feedbacks, or none.

## KPI strip

- Count of the visible rows.
- New this month, by reason.

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
| New answer feedback | header | the personas whose roles may create it | the record's own page (Row opens) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- reason: editable in its cell unless the record's state locks it.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| comment | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F3-01 Assistant panel](../01-ask-the-assistant/s-f03-01-assistant-panel.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 answer feedbacks of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no answer feedback the user may see yet, with the create action when allowed.
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
| Listed, U01, view All | desktop | ![Listed, U01, view All, light](../../images/lists/s-f03-l14-answer-feedbacks-u01-employee-desktop-light.png) | ![Listed, U01, view All, dark](../../images/lists/s-f03-l14-answer-feedbacks-u01-employee-desktop-dark.png) |
| Listed, U01, view All | phone | ![Listed, U01, view All, light](../../images/lists/s-f03-l14-answer-feedbacks-u01-employee-phone-light.png) | ![Listed, U01, view All, dark](../../images/lists/s-f03-l14-answer-feedbacks-u01-employee-phone-dark.png) |
| Listed, U02, view All | desktop | ![Listed, U02, view All, light](../../images/lists/s-f03-l14-answer-feedbacks-u02-manager-desktop-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-f03-l14-answer-feedbacks-u02-manager-desktop-dark.png) |
| Listed, U02, view All | phone | ![Listed, U02, view All, light](../../images/lists/s-f03-l14-answer-feedbacks-u02-manager-phone-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-f03-l14-answer-feedbacks-u02-manager-phone-dark.png) |
| Listed, U03, view All | desktop | ![Listed, U03, view All, light](../../images/lists/s-f03-l14-answer-feedbacks-u03-sales-desktop-light.png) | ![Listed, U03, view All, dark](../../images/lists/s-f03-l14-answer-feedbacks-u03-sales-desktop-dark.png) |
| Listed, U03, view All | phone | ![Listed, U03, view All, light](../../images/lists/s-f03-l14-answer-feedbacks-u03-sales-phone-light.png) | ![Listed, U03, view All, dark](../../images/lists/s-f03-l14-answer-feedbacks-u03-sales-phone-dark.png) |
| Listed, U04, view All | desktop | ![Listed, U04, view All, light](../../images/lists/s-f03-l14-answer-feedbacks-u04-purchasing-desktop-light.png) | ![Listed, U04, view All, dark](../../images/lists/s-f03-l14-answer-feedbacks-u04-purchasing-desktop-dark.png) |
| Listed, U04, view All | phone | ![Listed, U04, view All, light](../../images/lists/s-f03-l14-answer-feedbacks-u04-purchasing-phone-light.png) | ![Listed, U04, view All, dark](../../images/lists/s-f03-l14-answer-feedbacks-u04-purchasing-phone-dark.png) |
| Listed, U05, view All | desktop | ![Listed, U05, view All, light](../../images/lists/s-f03-l14-answer-feedbacks-u05-accounting-desktop-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-f03-l14-answer-feedbacks-u05-accounting-desktop-dark.png) |
| Listed, U05, view All | phone | ![Listed, U05, view All, light](../../images/lists/s-f03-l14-answer-feedbacks-u05-accounting-phone-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-f03-l14-answer-feedbacks-u05-accounting-phone-dark.png) |
| Listed, U06, view All | desktop | ![Listed, U06, view All, light](../../images/lists/s-f03-l14-answer-feedbacks-u06-hr-desktop-light.png) | ![Listed, U06, view All, dark](../../images/lists/s-f03-l14-answer-feedbacks-u06-hr-desktop-dark.png) |
| Listed, U06, view All | phone | ![Listed, U06, view All, light](../../images/lists/s-f03-l14-answer-feedbacks-u06-hr-phone-light.png) | ![Listed, U06, view All, dark](../../images/lists/s-f03-l14-answer-feedbacks-u06-hr-phone-dark.png) |
| Listed, U07, view All | desktop | ![Listed, U07, view All, light](../../images/lists/s-f03-l14-answer-feedbacks-u07-administrator-desktop-light.png) | ![Listed, U07, view All, dark](../../images/lists/s-f03-l14-answer-feedbacks-u07-administrator-desktop-dark.png) |
| Listed, U07, view All | phone | ![Listed, U07, view All, light](../../images/lists/s-f03-l14-answer-feedbacks-u07-administrator-phone-light.png) | ![Listed, U07, view All, dark](../../images/lists/s-f03-l14-answer-feedbacks-u07-administrator-phone-dark.png) |
| Listed, U12, view All | desktop | ![Listed, U12, view All, light](../../images/lists/s-f03-l14-answer-feedbacks-u12-marketing-desktop-light.png) | ![Listed, U12, view All, dark](../../images/lists/s-f03-l14-answer-feedbacks-u12-marketing-desktop-dark.png) |
| Listed, U12, view All | phone | ![Listed, U12, view All, light](../../images/lists/s-f03-l14-answer-feedbacks-u12-marketing-phone-light.png) | ![Listed, U12, view All, dark](../../images/lists/s-f03-l14-answer-feedbacks-u12-marketing-phone-dark.png) |
| Listed, U13, view All | desktop | ![Listed, U13, view All, light](../../images/lists/s-f03-l14-answer-feedbacks-u13-owner-desktop-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f03-l14-answer-feedbacks-u13-owner-desktop-dark.png) |
| Listed, U13, view All | phone | ![Listed, U13, view All, light](../../images/lists/s-f03-l14-answer-feedbacks-u13-owner-phone-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f03-l14-answer-feedbacks-u13-owner-phone-dark.png) |
| Listed, U14, view All | desktop | ![Listed, U14, view All, light](../../images/lists/s-f03-l14-answer-feedbacks-u14-field-worker-desktop-light.png) | ![Listed, U14, view All, dark](../../images/lists/s-f03-l14-answer-feedbacks-u14-field-worker-desktop-dark.png) |
| Listed, U14, view All | phone | ![Listed, U14, view All, light](../../images/lists/s-f03-l14-answer-feedbacks-u14-field-worker-phone-light.png) | ![Listed, U14, view All, dark](../../images/lists/s-f03-l14-answer-feedbacks-u14-field-worker-phone-dark.png) |
| Listed, U15, view All | desktop | ![Listed, U15, view All, light](../../images/lists/s-f03-l14-answer-feedbacks-u15-warehouse-operator-desktop-light.png) | ![Listed, U15, view All, dark](../../images/lists/s-f03-l14-answer-feedbacks-u15-warehouse-operator-desktop-dark.png) |
| Listed, U15, view All | phone | ![Listed, U15, view All, light](../../images/lists/s-f03-l14-answer-feedbacks-u15-warehouse-operator-phone-light.png) | ![Listed, U15, view All, dark](../../images/lists/s-f03-l14-answer-feedbacks-u15-warehouse-operator-phone-dark.png) |
| Listed, U16, view All | desktop | ![Listed, U16, view All, light](../../images/lists/s-f03-l14-answer-feedbacks-u16-office-worker-desktop-light.png) | ![Listed, U16, view All, dark](../../images/lists/s-f03-l14-answer-feedbacks-u16-office-worker-desktop-dark.png) |
| Listed, U16, view All | phone | ![Listed, U16, view All, light](../../images/lists/s-f03-l14-answer-feedbacks-u16-office-worker-phone-light.png) | ![Listed, U16, view All, dark](../../images/lists/s-f03-l14-answer-feedbacks-u16-office-worker-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Assistant › Answer feedbacks](README.md) |
| Workspaces | [U01](../../../../04-ux/views/u01-employee/workspace.md), [U02](../../../../04-ux/views/u02-manager/workspace.md), [U03](../../../../04-ux/views/u03-sales/workspace.md), [U04](../../../../04-ux/views/u04-purchasing/workspace.md), [U05](../../../../04-ux/views/u05-accounting/workspace.md), [U06](../../../../04-ux/views/u06-hr/workspace.md), [U07](../../../../04-ux/views/u07-administrator/workspace.md), [U12](../../../../04-ux/views/u12-marketing/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md), [U14](../../../../04-ux/views/u14-field-worker/workspace.md), [U15](../../../../04-ux/views/u15-warehouse-operator/workspace.md), [U16](../../../../04-ux/views/u16-office-worker/workspace.md) |
| Flows | [FL-F3-01](../../flows/fl-f03-01-ask-the-assistant.md) |

## Open questions

None.

---

⬅️ [S-F3-L13 Queued questions](s-f03-l13-queued-questions.md) · ⬆️ [Up](README.md) ·
➡️ [S-F3-L15 Agents](s-f03-l15-agents.md)
