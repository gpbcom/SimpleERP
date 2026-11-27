🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🎙️ [F4 Meetings](../../README.md) ›
🖥️ [Screens](../README.md) › 🗂️ [Views: Meetings menu](README.md) › 🗂️ S-F4-L08 Key moments

# 🗂️ S-F4-L08 Key moments

**Status:** ✅ specified

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U03 Sales](../../../../01-users/personas/u03-sales.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U14 Field worker](../../../../01-users/personas/u14-field-worker.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U01 Employee](../../../../01-users/personas/u01-employee.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |
| [U04 Purchasing and stock](../../../../01-users/personas/u04-purchasing.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U06 Human resources](../../../../01-users/personas/u06-hr.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U36 Professional](../../../../01-users/personas/u36-professional.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U33 Medical secretary](../../../../01-users/personas/u33-medical-secretary.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

- The owner's review (VC-10, D519): "Create persona(s) related to this enitity."
- The meeting's participants are the personas of the meeting use cases (the E-F4-01 Meeting list) and their
  managers U02; UC-F4-11 names no persona.

## Purpose

The aggregated list of every [E-F4-08 Key moment](../../data/e-f04-08-key-moment.md) the user may see: to find, filter,
total and act on many key moments at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Meetings › Key moments, in the capability's menu (D495).
- **Workspaces:** 10 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "key moments" offers this view.
- **AI assistant:** "show the key moments that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Key moments    Meetings › Key moments   [+ New]                                                              |
| [count]   [chart: count by state]                                                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] MEETING   STATE                                                                      |
| meeting           | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Meeting | meeting | text | yes |
| State | state | badge: Recorded | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Recorded | the visible rows (D488) |
| Meeting | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Key moments of a chosen meeting, or of the meetings that match a filter.
- From the other side: the meetings that have key moments, or none.

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
| New key moment | header | the personas whose roles may create it | the record's own page (Row opens) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

None: no field is editable in a cell.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| clip | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F4-10 Share and export](../08-share-and-reuse-outside/s-f04-10-share-and-export.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 key moments of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no key moment the user may see yet, with the create action when allowed.
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
| Listed, U03, view All | desktop | ![Listed, U03, view All, light](../../images/lists/s-f04-l08-key-moments-u03-sales-desktop-light.png) | ![Listed, U03, view All, dark](../../images/lists/s-f04-l08-key-moments-u03-sales-desktop-dark.png) |
| Listed, U03, view All | phone | ![Listed, U03, view All, light](../../images/lists/s-f04-l08-key-moments-u03-sales-phone-light.png) | ![Listed, U03, view All, dark](../../images/lists/s-f04-l08-key-moments-u03-sales-phone-dark.png) |
| Listed, U02, view All | desktop | ![Listed, U02, view All, light](../../images/lists/s-f04-l08-key-moments-u02-manager-desktop-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-f04-l08-key-moments-u02-manager-desktop-dark.png) |
| Listed, U02, view All | phone | ![Listed, U02, view All, light](../../images/lists/s-f04-l08-key-moments-u02-manager-phone-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-f04-l08-key-moments-u02-manager-phone-dark.png) |
| Listed, U13, view All | desktop | ![Listed, U13, view All, light](../../images/lists/s-f04-l08-key-moments-u13-owner-desktop-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f04-l08-key-moments-u13-owner-desktop-dark.png) |
| Listed, U13, view All | phone | ![Listed, U13, view All, light](../../images/lists/s-f04-l08-key-moments-u13-owner-phone-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f04-l08-key-moments-u13-owner-phone-dark.png) |
| Listed, U14, view All | desktop | ![Listed, U14, view All, light](../../images/lists/s-f04-l08-key-moments-u14-field-worker-desktop-light.png) | ![Listed, U14, view All, dark](../../images/lists/s-f04-l08-key-moments-u14-field-worker-desktop-dark.png) |
| Listed, U14, view All | phone | ![Listed, U14, view All, light](../../images/lists/s-f04-l08-key-moments-u14-field-worker-phone-light.png) | ![Listed, U14, view All, dark](../../images/lists/s-f04-l08-key-moments-u14-field-worker-phone-dark.png) |
| Listed, U01, view All | desktop | ![Listed, U01, view All, light](../../images/lists/s-f04-l08-key-moments-u01-employee-desktop-light.png) | ![Listed, U01, view All, dark](../../images/lists/s-f04-l08-key-moments-u01-employee-desktop-dark.png) |
| Listed, U01, view All | phone | ![Listed, U01, view All, light](../../images/lists/s-f04-l08-key-moments-u01-employee-phone-light.png) | ![Listed, U01, view All, dark](../../images/lists/s-f04-l08-key-moments-u01-employee-phone-dark.png) |
| Listed, U09, view All | desktop | ![Listed, U09, view All, light](../../images/lists/s-f04-l08-key-moments-u09-customer-desktop-light.png) | ![Listed, U09, view All, dark](../../images/lists/s-f04-l08-key-moments-u09-customer-desktop-dark.png) |
| Listed, U09, view All | phone | ![Listed, U09, view All, light](../../images/lists/s-f04-l08-key-moments-u09-customer-phone-light.png) | ![Listed, U09, view All, dark](../../images/lists/s-f04-l08-key-moments-u09-customer-phone-dark.png) |
| Listed, U04, view All | desktop | ![Listed, U04, view All, light](../../images/lists/s-f04-l08-key-moments-u04-purchasing-desktop-light.png) | ![Listed, U04, view All, dark](../../images/lists/s-f04-l08-key-moments-u04-purchasing-desktop-dark.png) |
| Listed, U04, view All | phone | ![Listed, U04, view All, light](../../images/lists/s-f04-l08-key-moments-u04-purchasing-phone-light.png) | ![Listed, U04, view All, dark](../../images/lists/s-f04-l08-key-moments-u04-purchasing-phone-dark.png) |
| Listed, U06, view All | desktop | ![Listed, U06, view All, light](../../images/lists/s-f04-l08-key-moments-u06-hr-desktop-light.png) | ![Listed, U06, view All, dark](../../images/lists/s-f04-l08-key-moments-u06-hr-desktop-dark.png) |
| Listed, U06, view All | phone | ![Listed, U06, view All, light](../../images/lists/s-f04-l08-key-moments-u06-hr-phone-light.png) | ![Listed, U06, view All, dark](../../images/lists/s-f04-l08-key-moments-u06-hr-phone-dark.png) |
| Listed, U36, view All | desktop | ![Listed, U36, view All, light](../../images/lists/s-f04-l08-key-moments-u36-professional-desktop-light.png) | ![Listed, U36, view All, dark](../../images/lists/s-f04-l08-key-moments-u36-professional-desktop-dark.png) |
| Listed, U36, view All | phone | ![Listed, U36, view All, light](../../images/lists/s-f04-l08-key-moments-u36-professional-phone-light.png) | ![Listed, U36, view All, dark](../../images/lists/s-f04-l08-key-moments-u36-professional-phone-dark.png) |
| Listed, U33, view All | desktop | ![Listed, U33, view All, light](../../images/lists/s-f04-l08-key-moments-u33-medical-secretary-desktop-light.png) | ![Listed, U33, view All, dark](../../images/lists/s-f04-l08-key-moments-u33-medical-secretary-desktop-dark.png) |
| Listed, U33, view All | phone | ![Listed, U33, view All, light](../../images/lists/s-f04-l08-key-moments-u33-medical-secretary-phone-light.png) | ![Listed, U33, view All, dark](../../images/lists/s-f04-l08-key-moments-u33-medical-secretary-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Meetings › Key moments](README.md) |
| Workspaces | [U03](../../../../04-ux/views/u03-sales/workspace.md), [U02](../../../../04-ux/views/u02-manager/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md), [U14](../../../../04-ux/views/u14-field-worker/workspace.md), [U01](../../../../04-ux/views/u01-employee/workspace.md), [U09](../../../../04-ux/views/u09-customer/workspace.md), [U04](../../../../04-ux/views/u04-purchasing/workspace.md), [U06](../../../../04-ux/views/u06-hr/workspace.md), [U36](../../../../04-ux/views/u36-professional/workspace.md), [U33](../../../../04-ux/views/u33-medical-secretary/workspace.md) |
| Flows | [FL-F4-08](../../flows/fl-f04-08-share-and-reuse-outside.md) |

## Open questions

None.

---

⬅️ [S-F4-L07 Evaluation grids](s-f04-l07-evaluation-grids.md) · ⬆️ [Up](README.md) ·
➡️ [S-F4-L09 Scheduled digests](s-f04-l09-scheduled-digests.md)
