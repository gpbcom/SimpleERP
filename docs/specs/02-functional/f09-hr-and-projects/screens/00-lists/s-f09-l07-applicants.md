🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: HR and projects menu](README.md) ›
🗂️ S-F9-L07 Applicants

# 🗂️ S-F9-L07 Applicants

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U06 Human resources](../../../../01-users/personas/u06-hr.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U01 Employee](../../../../01-users/personas/u01-employee.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F9-07 Applicant](../../data/e-f09-07-applicant.md) the user may see: to find, filter,
total and act on many applicants at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** HR and projects › Applicants, in the capability's menu (D495).
- **Workspaces:** 3 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "applicants" offers this view.
- **AI assistant:** "show the applicants that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Applicants    HR and projects › Applicants   [+ New]                                                         |
| [count] [new this month]   [chart: count by state]                                                           |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] NAME   STAGE   CONTACT   JOB   KEPT UNTIL                                            |
| contact           | [ ] ...                                                  Open >                          |
| job               | [ ] ...                                                  Open >                          |
| stage             | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Name | name | text | yes |
| Stage | stage | badge | yes |
| Contact | contact | text | yes |
| Job | job | text | yes |
| Kept until | kept until | date | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Active | the visible rows (D488) |
| Contact | each value | the visible rows (D488) |
| Job | each value | the visible rows (D488) |
| Stage | Active | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Applicants of a chosen contact, or of the contacts that match a filter.
- From the other side: the contacts that have applicants, or none.
- Applicants of a chosen job, or of the jobs that match a filter.
- From the other side: the jobs that have applicants, or none.

## KPI strip

- Count of the visible rows.
- New this month, by kept until.

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
| New applicant | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change stage | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- kept until: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F9-06 Applicant pipeline](../02-recruit/s-f09-06-applicant-pipeline.md).

The records also show on: [S-F9-05 Job position](../02-recruit/s-f09-05-job-position.md),
[S-F9-07 Offer](../02-recruit/s-f09-07-offer.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 applicants of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no applicant the user may see yet, with the create action when allowed.
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
| Listed, U06, view All | desktop | ![Listed, U06, view All, light](../../images/lists/s-f09-l07-applicants-u06-hr-desktop-light.png) | ![Listed, U06, view All, dark](../../images/lists/s-f09-l07-applicants-u06-hr-desktop-dark.png) |
| Listed, U06, view All | phone | ![Listed, U06, view All, light](../../images/lists/s-f09-l07-applicants-u06-hr-phone-light.png) | ![Listed, U06, view All, dark](../../images/lists/s-f09-l07-applicants-u06-hr-phone-dark.png) |
| Listed, U02, view All | desktop | ![Listed, U02, view All, light](../../images/lists/s-f09-l07-applicants-u02-manager-desktop-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-f09-l07-applicants-u02-manager-desktop-dark.png) |
| Listed, U02, view All | phone | ![Listed, U02, view All, light](../../images/lists/s-f09-l07-applicants-u02-manager-phone-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-f09-l07-applicants-u02-manager-phone-dark.png) |
| Listed, U01, view All | desktop | ![Listed, U01, view All, light](../../images/lists/s-f09-l07-applicants-u01-employee-desktop-light.png) | ![Listed, U01, view All, dark](../../images/lists/s-f09-l07-applicants-u01-employee-desktop-dark.png) |
| Listed, U01, view All | phone | ![Listed, U01, view All, light](../../images/lists/s-f09-l07-applicants-u01-employee-phone-light.png) | ![Listed, U01, view All, dark](../../images/lists/s-f09-l07-applicants-u01-employee-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [HR and projects › Applicants](README.md) |
| Workspaces | [U06](../../../../04-ux/views/u06-hr/workspace.md), [U02](../../../../04-ux/views/u02-manager/workspace.md), [U01](../../../../04-ux/views/u01-employee/workspace.md) |
| Flows | [FL-F4-09](../../../f04-meetings/flows/fl-f04-09-score-calls-and-interviews.md), [FL-F9-02](../../flows/fl-f09-02-recruit.md), [FL-F9-14](../../flows/fl-f09-14-source-candidates-on-linkedin.md) |

## Open questions

None.

---

⬅️ [S-F9-L06 Job positions](s-f09-l06-job-positions.md) · ⬆️ [Up](README.md) ·
➡️ [S-F9-L08 Time-off allocations](s-f09-l08-time-off-allocations.md)
