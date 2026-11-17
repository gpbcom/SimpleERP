🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
⚖️ [F15 Legal assistant](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: Legal assistant menu](README.md) ›
🗂️ S-F15-L06 Contract records

# 🗂️ S-F15-L06 Contract records

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U04 Purchasing and stock](../../../../01-users/personas/u04-purchasing.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U36 Professional](../../../../01-users/personas/u36-professional.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U50: their use cases only read these records, inside a screen of the use case, so they open them
from there (D493).

## Purpose

The aggregated list of every [E-F15-06 Contract record](../../data/e-f15-06-contract-record.md) the user may see: to
find, filter, total and act on many contract records at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Legal assistant › Contract records, in the capability's menu (D495).
- **Workspaces:** 3 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "contract records" offers this view.
- **AI assistant:** "show the contract records that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Contract records    Legal assistant › Contract records   [+ New]                                             |
| [count] [new this month]   [chart: count by state]                                                           |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] TITLE   STATE   DOCUMENT   START   LAST NOTICE DAY   KIND   RENEWAL   NOTICE PERIOD  |
| kind              | [ ] ...                                                  Open >                          |
| renewal           | [ ] ...                                                  Open >                          |
| document          | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Title | title | label | yes |
| State | state | badge: Active, NoticeGiven, Renewed, Ended | yes |
| Document | document | file name | no |
| Start | start | date | yes |
| Last notice day | last notice day | date | yes |
| Kind | kind | text | yes |
| Renewal | renewal | text | yes |
| Notice period | notice period | number, right-aligned | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Active, NoticeGiven, Renewed, Ended | the visible rows (D488) |
| Kind | each value | the visible rows (D488) |
| Renewal | each value | the visible rows (D488) |
| Document | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Contract records of a chosen document, or of the documents that match a filter.
- From the other side: the documents that have contract records, or none.

## KPI strip

- Count of the visible rows.
- New this month, by start.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Open: Active, NoticeGiven, Renewed.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New contract record | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- kind: editable in its cell unless the record's state locks it.
- start: editable in its cell unless the record's state locks it.
- renewal: editable in its cell unless the record's state locks it.
- notice period: editable in its cell unless the record's state locks it.
- last notice day: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F15-08 Contracts](../05-duties-and-records/s-f15-08-contracts.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 contract records of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no contract record the user may see yet, with the create action when allowed.
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
| Listed, U13, view Open: Active, NoticeGiven, Renewed | desktop | ![Listed, U13, view Open: Active, NoticeGiven, Renewed, light](../../images/lists/s-f15-l06-contract-records-u13-owner-desktop-light.png) | ![Listed, U13, view Open: Active, NoticeGiven, Renewed, dark](../../images/lists/s-f15-l06-contract-records-u13-owner-desktop-dark.png) |
| Listed, U13, view Open: Active, NoticeGiven, Renewed | phone | ![Listed, U13, view Open: Active, NoticeGiven, Renewed, light](../../images/lists/s-f15-l06-contract-records-u13-owner-phone-light.png) | ![Listed, U13, view Open: Active, NoticeGiven, Renewed, dark](../../images/lists/s-f15-l06-contract-records-u13-owner-phone-dark.png) |
| Listed, U04, view Open: Active, NoticeGiven, Renewed | desktop | ![Listed, U04, view Open: Active, NoticeGiven, Renewed, light](../../images/lists/s-f15-l06-contract-records-u04-purchasing-desktop-light.png) | ![Listed, U04, view Open: Active, NoticeGiven, Renewed, dark](../../images/lists/s-f15-l06-contract-records-u04-purchasing-desktop-dark.png) |
| Listed, U04, view Open: Active, NoticeGiven, Renewed | phone | ![Listed, U04, view Open: Active, NoticeGiven, Renewed, light](../../images/lists/s-f15-l06-contract-records-u04-purchasing-phone-light.png) | ![Listed, U04, view Open: Active, NoticeGiven, Renewed, dark](../../images/lists/s-f15-l06-contract-records-u04-purchasing-phone-dark.png) |
| Listed, U36, view Open | desktop | ![Listed, U36, view Open, light](../../images/lists/s-f15-l06-contract-records-u36-professional-desktop-light.png) | ![Listed, U36, view Open, dark](../../images/lists/s-f15-l06-contract-records-u36-professional-desktop-dark.png) |
| Listed, U36, view Open | phone | ![Listed, U36, view Open, light](../../images/lists/s-f15-l06-contract-records-u36-professional-phone-light.png) | ![Listed, U36, view Open, dark](../../images/lists/s-f15-l06-contract-records-u36-professional-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Legal assistant › Contract records](README.md) |
| Workspaces | [U13](../../../../04-ux/views/u13-owner/workspace.md), [U04](../../../../04-ux/views/u04-purchasing/workspace.md), [U36](../../../../04-ux/views/u36-professional/workspace.md) |
| Flows | [FL-F15-03](../../flows/fl-f15-03-check-a-document-against-the-law.md), [FL-F15-05](../../flows/fl-f15-05-duties-and-records.md) |

## Open questions

None.

---

⬅️ [S-F15-L05 Compliance duties](s-f15-l05-compliance-duties.md) · ⬆️ [Up](README.md) ·
➡️ [S-F15-L07 Corporate decisions](s-f15-l07-corporate-decisions.md)
