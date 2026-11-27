🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: HR and projects menu](README.md) ›
🗂️ S-F9-L52 Online courses

# 🗂️ S-F9-L52 Online courses

**Status:** ✅ specified

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U38 Training coordinator](../../../../01-users/personas/u38-training-coordinator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U01 Employee](../../../../01-users/personas/u01-employee.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F9-52 Online course](../../data/e-f09-52-online-course.md) the user may see: to find,
filter, total and act on many online courses at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** HR and projects › Online courses, in the capability's menu (D495).
- **Workspaces:** 3 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "online courses" offers this view.
- **AI assistant:** "show the online courses that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Online courses    HR and projects › Online courses   [+ New]                                                 |
| [count] [Draft] [new this month]   [chart: count by state]                                                                   |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] COURSE   AUDIENCE   PRICE   PASS MARK   STATE                                        |
| [ ] ...                                                                       Open >                         |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Course | title | text | yes |
| Audience | audience | text | yes |
| Price | price | money | yes |
| Pass mark | pass mark | percent | yes |
| State | state | badge: Draft, Published, Unpublished, Archived | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Draft, Published, Unpublished, Archived | the visible rows (D488) |
| Audience | staff, customers, public | the visible rows (D488) |
| Price | free, priced | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Courses of a chosen learner, or of the learners that match a filter.
- From the other side: the learners who took a course, or none.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Draft.
- New this month, by creation date.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Mine: learner.
- Open: Published.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New online course | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only, audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows, audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted, audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns, audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

None: a course is edited on its own screen.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| learners and results | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F9-44 Online courses](../15-work-location-headcount-and-learning/s-f09-44-online-courses.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 online courses of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no online course the user may see yet, with the create action when allowed.
- **Selected:** the bulk bar with the actions allowed on every selected row.
- **Error:** the query failed, with Retry.

## Responsive behaviour

On a phone the table keeps its columns and scrolls sideways, the facet panel becomes a drawer and the KPI strip stays
(VR-14, D491).

## Accessibility

The KPI strip, the facet panel, the toolbar and the table are named landmarks; the result count is announced when the
filters change; each chip has its remove button; the facet drawer returns the focus to its button.

## Example images

Drawn in the image round from this page: one row per persona and device, light and dark
([D490](../../../../06-decisions/ux/d490-example-images-for-every-persona-that-can-open-a-view.md),
[D500](../../../../06-decisions/ux/d500-images-live-in-the-specs-folders.md)). The files are named by the plan.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Listed, U01, view Needs attention | phone | ![Listed, U01, view Needs attention, light](../../images/lists/s-f09-l52-online-courses-u01-employee-phone-light.png) | ![Listed, U01, view Needs attention, dark](../../images/lists/s-f09-l52-online-courses-u01-employee-phone-dark.png) |
| Listed, U09, view Needs attention | phone | ![Listed, U09, view Needs attention, light](../../images/lists/s-f09-l52-online-courses-u09-customer-phone-light.png) | ![Listed, U09, view Needs attention, dark](../../images/lists/s-f09-l52-online-courses-u09-customer-phone-dark.png) |
| Listed, U38, view Needs attention | desktop | ![Listed, U38, view Needs attention, light](../../images/lists/s-f09-l52-online-courses-u38-training-coordinator-desktop-light.png) | ![Listed, U38, view Needs attention, dark](../../images/lists/s-f09-l52-online-courses-u38-training-coordinator-desktop-dark.png) |
| Listed, U38, view Mine: learner | phone | ![Listed, U38, view Mine: learner, light](../../images/lists/s-f09-l52-online-courses-u38-training-coordinator-phone-light.png) | ![Listed, U38, view Mine: learner, dark](../../images/lists/s-f09-l52-online-courses-u38-training-coordinator-phone-dark.png) |
| Listed, U01, view Mine: learner | desktop | ![Listed, U01, view Mine: learner, light](../../images/lists/s-f09-l52-online-courses-u01-employee-desktop-light.png) | ![Listed, U01, view Mine: learner, dark](../../images/lists/s-f09-l52-online-courses-u01-employee-desktop-dark.png) |
| Listed, U09, view Mine: learner | desktop | ![Listed, U09, view Mine: learner, light](../../images/lists/s-f09-l52-online-courses-u09-customer-desktop-light.png) | ![Listed, U09, view Mine: learner, dark](../../images/lists/s-f09-l52-online-courses-u09-customer-desktop-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [HR and projects › Online courses](README.md) |
| Workspaces | [U38](../../../../04-ux/views/u38-training-coordinator/workspace.md), [U01](../../../../04-ux/views/u01-employee/workspace.md), [U09](../../../../04-ux/views/u09-customer/workspace.md) |
| Flows | [FL-F9-15](../../flows/fl-f09-15-work-location-headcount-and-learning.md) |

## Open questions

None.

---

⬅️ [S-F9-L51 Change requests](s-f09-l51-change-requests.md) · ⬆️ [Up](README.md)
