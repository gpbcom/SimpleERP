🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📒 [F8 Accounting](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: Accounting menu](README.md) ›
🗂️ S-F8-L26 Accountant requests

# 🗂️ S-F8-L26 Accountant requests

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U08 External accountant](../../../../01-users/personas/u08-external-accountant.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U01 Employee](../../../../01-users/personas/u01-employee.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U49: their use cases only read these records, inside a screen of the use case, so they open them
from there (D493).

## Purpose

The aggregated list of every [E-F8-26 Accountant request](../../data/e-f08-26-accountant-request.md) the user may see:
to find, filter, total and act on many accountant requests at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Accounting › Accountant requests, in the capability's menu (D495).
- **Workspaces:** 3 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "accountant requests" offers this view.
- **AI assistant:** "show the accountant requests that need attention" opens it with the filter as editable chips
  (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Accountant requests    Accounting › Accountant requests   [+ New]                                            |
| [count] [Open]   [chart: count by state]                                                                     |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] ENTRIES   STATUS   ASSIGNEE   KIND                                                   |
| entries           | [ ] ...                                                  Open >                          |
| kind              | [ ] ...                                                  Open >                          |
| assignee          | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Entries | entries | text | yes |
| Status | status | badge | yes |
| Assignee | assignee | person's name | yes |
| Kind | kind | label | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Open, Answered, Closed | the visible rows (D488) |
| Entries | each value | the visible rows (D488) |
| Kind | question, receipt | the visible rows (D488) |
| Assignee | each person, the user first | the visible rows (D488) |
| Status | Open, Answered, Closed | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: accountant requests link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Open.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Mine: assignee.
- Open: Open, Answered.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New accountant request | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change status | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Assign | bulk bar | the personas whose roles may assign | sets the assignee; audited |
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
| assignee | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F8-14 Accountant workspace](../01-set-up-and-post/s-f08-14-accountant-workspace.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 accountant requests of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no accountant request the user may see yet, with the create action when allowed.
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
| Listed, U08, view Needs attention | desktop | ![Listed, U08, view Needs attention, light](../../images/lists/s-f08-l26-accountant-requests-u08-external-accountant-desktop-light.png) | ![Listed, U08, view Needs attention, dark](../../images/lists/s-f08-l26-accountant-requests-u08-external-accountant-desktop-dark.png) |
| Listed, U08, view Needs attention | phone | ![Listed, U08, view Needs attention, light](../../images/lists/s-f08-l26-accountant-requests-u08-external-accountant-phone-light.png) | ![Listed, U08, view Needs attention, dark](../../images/lists/s-f08-l26-accountant-requests-u08-external-accountant-phone-dark.png) |
| Listed, U05, view Mine: assignee | desktop | ![Listed, U05, view Mine: assignee, light](../../images/lists/s-f08-l26-accountant-requests-u05-accounting-desktop-light.png) | ![Listed, U05, view Mine: assignee, dark](../../images/lists/s-f08-l26-accountant-requests-u05-accounting-desktop-dark.png) |
| Listed, U05, view Mine: assignee | phone | ![Listed, U05, view Mine: assignee, light](../../images/lists/s-f08-l26-accountant-requests-u05-accounting-phone-light.png) | ![Listed, U05, view Mine: assignee, dark](../../images/lists/s-f08-l26-accountant-requests-u05-accounting-phone-dark.png) |
| Listed, U01, view Mine: assignee | desktop | ![Listed, U01, view Mine: assignee, light](../../images/lists/s-f08-l26-accountant-requests-u01-employee-desktop-light.png) | ![Listed, U01, view Mine: assignee, dark](../../images/lists/s-f08-l26-accountant-requests-u01-employee-desktop-dark.png) |
| Listed, U01, view Mine: assignee | phone | ![Listed, U01, view Mine: assignee, light](../../images/lists/s-f08-l26-accountant-requests-u01-employee-phone-light.png) | ![Listed, U01, view Mine: assignee, dark](../../images/lists/s-f08-l26-accountant-requests-u01-employee-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Accounting › Accountant requests](README.md) |
| Workspaces | [U08](../../../../04-ux/views/u08-external-accountant/workspace.md), [U05](../../../../04-ux/views/u05-accounting/workspace.md), [U01](../../../../04-ux/views/u01-employee/workspace.md) |
| Flows | [FL-F8-01](../../flows/fl-f08-01-set-up-and-post.md), [FL-F8-10](../../flows/fl-f08-10-accountant-collaboration.md) |

## Open questions

None.

---

⬅️ [S-F8-L25 Sustainability reports](s-f08-l25-sustainability-reports.md) · ⬆️ [Up](README.md) ·
➡️ [S-F8-L27 FEC files](s-f08-l27-fec-files.md)
