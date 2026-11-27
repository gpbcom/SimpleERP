🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🩺 [SC09 Health practices](../../README.md) ›
🖥️ [Screens](../README.md) › 🗂️ [Views: Health practices menu](README.md) › 🗂️ S-SC09-L03 Clinical record entries

# 🗂️ S-SC09-L03 Clinical record entries

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U33 Medical secretary](../../../../01-users/personas/u33-medical-secretary.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |
| [U36 Professional](../../../../01-users/personas/u36-professional.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-SC09-03 Clinical record entry](../../data/e-sc09-03-clinical-record-entry.md) the user
may see: to find, filter, total and act on many clinical record entries at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Health practices › Clinical record entries, in the capability's menu (D495).
- **Workspaces:** 4 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "clinical record entries" offers this view.
- **AI assistant:** "show the clinical record entries that need attention" opens it with the filter as editable chips
  (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Clinical record entries    Health practices › Clinical record entries   [+ New]                              |
| [count] [new this month]   [chart: count by state]                                                           |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] PATIENT   STATE   AUTHOR   DATE                                                      |
| patient           | [ ] ...                                                  Open >                          |
| author            | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Patient | patient | link to the record | yes |
| State | state | badge: Recorded | yes |
| Author | author | link to the record | yes |
| Date | date | link to the record | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Recorded | the visible rows (D488) |
| Patient | each linked patient | the visible rows (D488) |
| Author | each linked author | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Clinical record entries of a chosen patient, or of the patients that match a filter.
- From the other side: the patients that have clinical record entries, or none.

## KPI strip

- Count of the visible rows.
- New this month, by date.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Mine: author.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New clinical record entry | header | the personas whose roles may create it | the record's own page (Row opens) |
| Assign | bulk bar | the personas whose roles may assign | sets the author; audited |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- date: editable in its cell unless the record's state locks it.
- author: editable in its cell unless the record's state locks it.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| content | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-SC09-04 Clinical record](../02-patient-file-and-care/s-sc09-04-clinical-record.md).

The records also show on: [S-SC09-01 Agenda](../01-appointments/s-sc09-01-agenda.md),
[S-SC09-09 Health exchanges](../04-health-exchanges/s-sc09-09-health-exchanges.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 clinical record entries of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no clinical record entry the user may see yet, with the create action when allowed.
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
| Listed, U13, view All | desktop | ![Listed, U13, view All, light](../../images/lists/s-sc09-l03-clinical-record-entries-u13-owner-desktop-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-sc09-l03-clinical-record-entries-u13-owner-desktop-dark.png) |
| Listed, U13, view All | phone | ![Listed, U13, view All, light](../../images/lists/s-sc09-l03-clinical-record-entries-u13-owner-phone-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-sc09-l03-clinical-record-entries-u13-owner-phone-dark.png) |
| Listed, U33, view Mine: author | desktop | ![Listed, U33, view Mine: author, light](../../images/lists/s-sc09-l03-clinical-record-entries-u33-medical-secretary-desktop-light.png) | ![Listed, U33, view Mine: author, dark](../../images/lists/s-sc09-l03-clinical-record-entries-u33-medical-secretary-desktop-dark.png) |
| Listed, U33, view Mine: author | phone | ![Listed, U33, view Mine: author, light](../../images/lists/s-sc09-l03-clinical-record-entries-u33-medical-secretary-phone-light.png) | ![Listed, U33, view Mine: author, dark](../../images/lists/s-sc09-l03-clinical-record-entries-u33-medical-secretary-phone-dark.png) |
| Listed, U09, view Mine: author | desktop | ![Listed, U09, view Mine: author, light](../../images/lists/s-sc09-l03-clinical-record-entries-u09-customer-desktop-light.png) | ![Listed, U09, view Mine: author, dark](../../images/lists/s-sc09-l03-clinical-record-entries-u09-customer-desktop-dark.png) |
| Listed, U09, view Mine: author | phone | ![Listed, U09, view Mine: author, light](../../images/lists/s-sc09-l03-clinical-record-entries-u09-customer-phone-light.png) | ![Listed, U09, view Mine: author, dark](../../images/lists/s-sc09-l03-clinical-record-entries-u09-customer-phone-dark.png) |
| Listed, U36, view Mine | desktop | ![Listed, U36, view Mine, light](../../images/lists/s-sc09-l03-clinical-record-entries-u36-professional-desktop-light.png) | ![Listed, U36, view Mine, dark](../../images/lists/s-sc09-l03-clinical-record-entries-u36-professional-desktop-dark.png) |
| Listed, U36, view Mine | phone | ![Listed, U36, view Mine, light](../../images/lists/s-sc09-l03-clinical-record-entries-u36-professional-phone-light.png) | ![Listed, U36, view Mine, dark](../../images/lists/s-sc09-l03-clinical-record-entries-u36-professional-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Health practices › Clinical record entries](README.md) |
| Workspaces | [U13](../../../../04-ux/views/u13-owner/workspace.md), [U33](../../../../04-ux/views/u33-medical-secretary/workspace.md), [U09](../../../../04-ux/views/u09-customer/workspace.md), [U36](../../../../04-ux/views/u36-professional/workspace.md) |
| Flows | [FL-SC09-01](../../flows/fl-sc09-01-appointments.md), [FL-SC09-02](../../flows/fl-sc09-02-patient-file-and-care.md), [FL-SC09-04](../../flows/fl-sc09-04-health-exchanges.md), [FL-SC09-06](../../flows/fl-sc09-06-compliance-and-certification.md) |

## Open questions

None.

---

⬅️ [S-SC09-L02 Patients](s-sc09-l02-patients.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC09-L04 Prescriptions](s-sc09-l04-prescriptions.md)
