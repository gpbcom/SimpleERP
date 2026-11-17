🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: HR and projects menu](README.md) ›
🗂️ S-F9-L20 Equality indexes

# 🗂️ S-F9-L20 Equality indexes

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U06 Human resources](../../../../01-users/personas/u06-hr.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U45 Payroll officer](../../../../01-users/personas/u45-payroll-officer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U01 Employee](../../../../01-users/personas/u01-employee.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F9-20 Equality index](../../data/e-f09-20-equality-index.md) the user may see: to find,
filter, total and act on many equality indexes at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** HR and projects › Equality indexes, in the capability's menu (D495).
- **Workspaces:** 4 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "equality indexes" offers this view.
- **AI assistant:** "show the equality indexes that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Equality indexes    HR and projects › Equality indexes   [+ New]                                             |
| [count] [Draft] [new this month]   [chart: count by state]                                                   |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] YEAR   STATE   MEASURES   PUBLISHED   GAPS PER CATEGORY                              |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Year | year | text | yes |
| State | state | badge: Draft, Published | yes |
| Measures | measures | date | yes |
| Published | published | date | yes |
| Gaps per category | gaps per category | number, right-aligned | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Draft, Published | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: equality indexes link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Draft.
- New this month, by year.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New equality index | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- gaps per category: editable in its cell unless the record's state locks it.
- measures: editable in its cell unless the record's state locks it.
- published: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to
[S-F9-20 Equality and pay transparency](../07-fair-pay-and-speaking-up/s-f09-20-equality-and-pay-transparency.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 equality indexes of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no equality index the user may see yet, with the create action when allowed.
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
| Listed, U06, view Needs attention | desktop | ![Listed, U06, view Needs attention, light](../../images/lists/s-f09-l20-equality-indexes-u06-hr-desktop-light.png) | ![Listed, U06, view Needs attention, dark](../../images/lists/s-f09-l20-equality-indexes-u06-hr-desktop-dark.png) |
| Listed, U06, view Needs attention | phone | ![Listed, U06, view Needs attention, light](../../images/lists/s-f09-l20-equality-indexes-u06-hr-phone-light.png) | ![Listed, U06, view Needs attention, dark](../../images/lists/s-f09-l20-equality-indexes-u06-hr-phone-dark.png) |
| Listed, U13, view Needs attention | desktop | ![Listed, U13, view Needs attention, light](../../images/lists/s-f09-l20-equality-indexes-u13-owner-desktop-light.png) | ![Listed, U13, view Needs attention, dark](../../images/lists/s-f09-l20-equality-indexes-u13-owner-desktop-dark.png) |
| Listed, U13, view Needs attention | phone | ![Listed, U13, view Needs attention, light](../../images/lists/s-f09-l20-equality-indexes-u13-owner-phone-light.png) | ![Listed, U13, view Needs attention, dark](../../images/lists/s-f09-l20-equality-indexes-u13-owner-phone-dark.png) |
| Listed, U45, view All | desktop | ![Listed, U45, view All, light](../../images/lists/s-f09-l20-equality-indexes-u45-payroll-officer-desktop-light.png) | ![Listed, U45, view All, dark](../../images/lists/s-f09-l20-equality-indexes-u45-payroll-officer-desktop-dark.png) |
| Listed, U45, view All | phone | ![Listed, U45, view All, light](../../images/lists/s-f09-l20-equality-indexes-u45-payroll-officer-phone-light.png) | ![Listed, U45, view All, dark](../../images/lists/s-f09-l20-equality-indexes-u45-payroll-officer-phone-dark.png) |
| Listed, U01, view All | desktop | ![Listed, U01, view All, light](../../images/lists/s-f09-l20-equality-indexes-u01-employee-desktop-light.png) | ![Listed, U01, view All, dark](../../images/lists/s-f09-l20-equality-indexes-u01-employee-desktop-dark.png) |
| Listed, U01, view All | phone | ![Listed, U01, view All, light](../../images/lists/s-f09-l20-equality-indexes-u01-employee-phone-light.png) | ![Listed, U01, view All, dark](../../images/lists/s-f09-l20-equality-indexes-u01-employee-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [HR and projects › Equality indexes](README.md) |
| Workspaces | [U06](../../../../04-ux/views/u06-hr/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md), [U45](../../../../04-ux/views/u45-payroll-officer/workspace.md), [U01](../../../../04-ux/views/u01-employee/workspace.md) |
| Flows | [FL-F9-07](../../flows/fl-f09-07-fair-pay-and-speaking-up.md) |

## Open questions

None.

---

⬅️ [S-F9-L19 Contract templates](s-f09-l19-contract-templates.md) · ⬆️ [Up](README.md) ·
➡️ [S-F9-L21 Whistleblowing reports](s-f09-l21-whistleblowing-reports.md)
