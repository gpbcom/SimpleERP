🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
⚖️ [F15 Legal assistant](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: Legal assistant menu](README.md) ›
🗂️ S-F15-L05 Compliance duties

# 🗂️ S-F15-L05 Compliance duties

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U06 Human resources](../../../../01-users/personas/u06-hr.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U04 Purchasing and stock](../../../../01-users/personas/u04-purchasing.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U08 External accountant](../../../../01-users/personas/u08-external-accountant.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |
| [U36 Professional](../../../../01-users/personas/u36-professional.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F15-05 Compliance duty](../../data/e-f15-05-compliance-duty.md) the user may see: to
find, filter, total and act on many compliance duties at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Legal assistant › Compliance duties, in the capability's menu (D495).
- **Workspaces:** 6 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "compliance duties" offers this view.
- **AI assistant:** "show the compliance duties that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Compliance duties    Legal assistant › Compliance duties   [+ New]                                           |
| [count] [Overdue] [due in 7 days]   [chart: count by state]                                                  |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] TITLE   STATUS   OWNER   SOURCE   DUE DATE   RECURRENCE                              |
| source            | [ ] ...                                                  Open >                          |
| recurrence        | [ ] ...                                                  Open >                          |
| owner             | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Title | title | text | yes |
| Status | status | badge | yes |
| Owner | owner | link to the record | yes |
| Source | source | link to the record | yes |
| Due date | due date | date | yes |
| Recurrence | recurrence | text | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Planned, Done, Overdue | the visible rows (D488) |
| Source | each linked source | the visible rows (D488) |
| Recurrence | each value | the visible rows (D488) |
| Owner | each linked owner | the visible rows (D488) |
| Status | Planned, Done, Overdue | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Compliance duties of a chosen source, or of the sources that match a filter.
- From the other side: the sources that have compliance duties, or none.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Overdue.
- Due in 7 days, by due date.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Mine: owner.
- Open: Planned, Overdue.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New compliance duty | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change status | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Assign | bulk bar | the personas whose roles may assign | sets the owner; audited |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- due date: editable in its cell unless the record's state locks it.
- recurrence: editable in its cell unless the record's state locks it.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| owner | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F15-07 Compliance calendar](../05-duties-and-records/s-f15-07-compliance-calendar.md).

The records also show on: [S-F15-08 Contracts](../05-duties-and-records/s-f15-08-contracts.md),
[S-F15-09 Company records](../05-duties-and-records/s-f15-09-company-records.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 compliance duties of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no compliance duty the user may see yet, with the create action when allowed.
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
| Listed, U13, view Needs attention | desktop | ![Listed, U13, view Needs attention, light](../../images/lists/s-f15-l05-compliance-duties-u13-owner-desktop-light.png) | ![Listed, U13, view Needs attention, dark](../../images/lists/s-f15-l05-compliance-duties-u13-owner-desktop-dark.png) |
| Listed, U13, view Needs attention | phone | ![Listed, U13, view Needs attention, light](../../images/lists/s-f15-l05-compliance-duties-u13-owner-phone-light.png) | ![Listed, U13, view Needs attention, dark](../../images/lists/s-f15-l05-compliance-duties-u13-owner-phone-dark.png) |
| Listed, U06, view Needs attention | desktop | ![Listed, U06, view Needs attention, light](../../images/lists/s-f15-l05-compliance-duties-u06-hr-desktop-light.png) | ![Listed, U06, view Needs attention, dark](../../images/lists/s-f15-l05-compliance-duties-u06-hr-desktop-dark.png) |
| Listed, U06, view Needs attention | phone | ![Listed, U06, view Needs attention, light](../../images/lists/s-f15-l05-compliance-duties-u06-hr-phone-light.png) | ![Listed, U06, view Needs attention, dark](../../images/lists/s-f15-l05-compliance-duties-u06-hr-phone-dark.png) |
| Listed, U05, view Mine: owner | desktop | ![Listed, U05, view Mine: owner, light](../../images/lists/s-f15-l05-compliance-duties-u05-accounting-desktop-light.png) | ![Listed, U05, view Mine: owner, dark](../../images/lists/s-f15-l05-compliance-duties-u05-accounting-desktop-dark.png) |
| Listed, U05, view Mine: owner | phone | ![Listed, U05, view Mine: owner, light](../../images/lists/s-f15-l05-compliance-duties-u05-accounting-phone-light.png) | ![Listed, U05, view Mine: owner, dark](../../images/lists/s-f15-l05-compliance-duties-u05-accounting-phone-dark.png) |
| Listed, U04, view Mine: owner | desktop | ![Listed, U04, view Mine: owner, light](../../images/lists/s-f15-l05-compliance-duties-u04-purchasing-desktop-light.png) | ![Listed, U04, view Mine: owner, dark](../../images/lists/s-f15-l05-compliance-duties-u04-purchasing-desktop-dark.png) |
| Listed, U04, view Mine: owner | phone | ![Listed, U04, view Mine: owner, light](../../images/lists/s-f15-l05-compliance-duties-u04-purchasing-phone-light.png) | ![Listed, U04, view Mine: owner, dark](../../images/lists/s-f15-l05-compliance-duties-u04-purchasing-phone-dark.png) |
| Listed, U08, view Needs attention | desktop | ![Listed, U08, view Needs attention, light](../../images/lists/s-f15-l05-compliance-duties-u08-external-accountant-desktop-light.png) | ![Listed, U08, view Needs attention, dark](../../images/lists/s-f15-l05-compliance-duties-u08-external-accountant-desktop-dark.png) |
| Listed, U08, view Needs attention | phone | ![Listed, U08, view Needs attention, light](../../images/lists/s-f15-l05-compliance-duties-u08-external-accountant-phone-light.png) | ![Listed, U08, view Needs attention, dark](../../images/lists/s-f15-l05-compliance-duties-u08-external-accountant-phone-dark.png) |
| Listed, U36, view Mine | desktop | ![Listed, U36, view Mine, light](../../images/lists/s-f15-l05-compliance-duties-u36-professional-desktop-light.png) | ![Listed, U36, view Mine, dark](../../images/lists/s-f15-l05-compliance-duties-u36-professional-desktop-dark.png) |
| Listed, U36, view Mine | phone | ![Listed, U36, view Mine, light](../../images/lists/s-f15-l05-compliance-duties-u36-professional-phone-light.png) | ![Listed, U36, view Mine, dark](../../images/lists/s-f15-l05-compliance-duties-u36-professional-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Legal assistant › Compliance duties](README.md) |
| Workspaces | [U13](../../../../04-ux/views/u13-owner/workspace.md), [U06](../../../../04-ux/views/u06-hr/workspace.md), [U05](../../../../04-ux/views/u05-accounting/workspace.md), [U04](../../../../04-ux/views/u04-purchasing/workspace.md), [U08](../../../../04-ux/views/u08-external-accountant/workspace.md), [U36](../../../../04-ux/views/u36-professional/workspace.md) |
| Flows | [FL-F15-05](../../flows/fl-f15-05-duties-and-records.md), [FL-F22-02](../../../f22-unified-cost-management/flows/fl-f22-02-budgets-and-stops.md) |

## Open questions

None.

---

⬅️ [S-F15-L04 Standard register entries](s-f15-l04-standard-register-entries.md) · ⬆️ [Up](README.md) ·
➡️ [S-F15-L06 Contract records](s-f15-l06-contract-records.md)
