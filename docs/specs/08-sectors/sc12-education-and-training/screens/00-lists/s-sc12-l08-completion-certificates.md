🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🎓 [SC12 Education and training](../../README.md) ›
🖥️ [Screens](../README.md) › 🗂️ [Views: Education and training menu](README.md) ›
🗂️ S-SC12-L08 Completion certificates

# 🗂️ S-SC12-L08 Completion certificates

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U39 Trainer](../../../../01-users/personas/u39-trainer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U38 Training coordinator](../../../../01-users/personas/u38-training-coordinator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-SC12-08 Completion certificate](../../data/e-sc12-08-completion-certificate.md) the user
may see: to find, filter, total and act on many completion certificates at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Education and training › Completion certificates, in the capability's menu (D495).
- **Workspaces:** 3 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "completion certificates" offers this view.
- **AI assistant:** "show the completion certificates that need attention" opens it with the filter as editable chips
  (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Completion certificates    Education and training › Completion certificates   [+ New]                        |
| [count] [new this month]   [chart: count by state]                                                           |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] ENROLMENT   STATE   DATE                                                             |
| enrolment         | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Enrolment | enrolment | link to the record | yes |
| State | state | badge: Active | yes |
| Date | date | link to the record | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Active | the visible rows (D488) |
| Enrolment | each linked enrolment | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Completion certificates of a chosen enrolment, or of the enrolments that match a filter.
- From the other side: the enrolments that have completion certificates, or none.

## KPI strip

- Count of the visible rows.
- New this month, by date.

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
| New completion certificate | header | the personas whose roles may create it | the record's own page (Row opens) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- date: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-SC12-08 Certificates](../03-deliver-and-assess/s-sc12-08-certificates.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 completion certificates of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no completion certificate the user may see yet, with the create action when allowed.
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
| Listed, U39, view All | desktop | ![Listed, U39, view All, light](../../images/lists/s-sc12-l08-completion-certificates-u39-trainer-desktop-light.png) | ![Listed, U39, view All, dark](../../images/lists/s-sc12-l08-completion-certificates-u39-trainer-desktop-dark.png) |
| Listed, U39, view All | phone | ![Listed, U39, view All, light](../../images/lists/s-sc12-l08-completion-certificates-u39-trainer-phone-light.png) | ![Listed, U39, view All, dark](../../images/lists/s-sc12-l08-completion-certificates-u39-trainer-phone-dark.png) |
| Listed, U38, view All | desktop | ![Listed, U38, view All, light](../../images/lists/s-sc12-l08-completion-certificates-u38-training-coordinator-desktop-light.png) | ![Listed, U38, view All, dark](../../images/lists/s-sc12-l08-completion-certificates-u38-training-coordinator-desktop-dark.png) |
| Listed, U38, view All | phone | ![Listed, U38, view All, light](../../images/lists/s-sc12-l08-completion-certificates-u38-training-coordinator-phone-light.png) | ![Listed, U38, view All, dark](../../images/lists/s-sc12-l08-completion-certificates-u38-training-coordinator-phone-dark.png) |
| Listed, U09, view All | desktop | ![Listed, U09, view All, light](../../images/lists/s-sc12-l08-completion-certificates-u09-customer-desktop-light.png) | ![Listed, U09, view All, dark](../../images/lists/s-sc12-l08-completion-certificates-u09-customer-desktop-dark.png) |
| Listed, U09, view All | phone | ![Listed, U09, view All, light](../../images/lists/s-sc12-l08-completion-certificates-u09-customer-phone-light.png) | ![Listed, U09, view All, dark](../../images/lists/s-sc12-l08-completion-certificates-u09-customer-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Education and training › Completion certificates](README.md) |
| Workspaces | [U39](../../../../04-ux/views/u39-trainer/workspace.md), [U38](../../../../04-ux/views/u38-training-coordinator/workspace.md), [U09](../../../../04-ux/views/u09-customer/workspace.md) |
| Flows | [FL-SC12-03](../../flows/fl-sc12-03-deliver-and-assess.md) |

## Open questions

None.

---

⬅️ [S-SC12-L07 E-learning records](s-sc12-l07-e-learning-records.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC12-L09 Survey answers](s-sc12-l09-survey-answers.md)
