🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏛️ [SC20 Public bodies](../../README.md) ›
🖥️ [Screens](../README.md) › 🗂️ [Views: Public bodies menu](README.md) › 🗂️ S-SC20-L13 Civil records

# 🗂️ S-SC20-L13 Civil records

**Status:** ✅ specified

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U16 Office worker](../../../../01-users/personas/u16-office-worker.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U56 Citizen](../../../../01-users/personas/u56-citizen.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U54: their use cases only read these records, inside a screen of the use case, so they open them
from there (D493).

## Purpose

The aggregated list of every [E-SC20-13 Civil record](../../data/e-sc20-13-civil-record.md) the user may see: to find,
filter, total and act on many civil records at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Public bodies › Civil records, in the capability's menu (D495).
- **Workspaces:** the persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "civil records" offers this view.
- **AI assistant:** "show the civil records that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Civil records    Public bodies > Civil records   [+ New]                                                     |
| [count] [Drafted] [new this month]   [chart: count by state]                                                 |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                              n of N results                      |
| kind              | [ ] NUMBER   KIND   DATE OF THE    NOTES   SIGNED BY   STATE                             |
| year              | [ ] ...                                              Open >                              |
| Related records   | [ ] ...                                              Open >                              |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Number | number | text | yes |
| Kind | kind | text | yes |
| Date of the event | date of the event | date | yes |
| Notes | notes | text | yes |
| Signed by | signed by | text | yes |
| State | state | badge: Drafted, Registered, Annotated, Archived | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| Kind | each value | the visible rows (D488) |
| Year | each value | the visible rows (D488) |
| State | Drafted, Registered, Annotated, Archived | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Citizen requests.
- From the other side: acts Drafted and not signed for more than a day.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Drafted.
- New this month, by date of the event.

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
| New civil record | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
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
| persons | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| date of the event | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| declared by | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| owner | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-SC20-18](../05-council-registry-permits-and-assets/s-sc20-18-civil-registry.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 civil records of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no civil record the user may see yet, with the create action when allowed.
- **Selected:** the bulk bar with the actions allowed on every selected row.
- **Error:** the query failed, with Retry.

## Responsive behaviour

On a phone the table keeps its columns and scrolls sideways, the facet panel becomes a drawer and the KPI strip stays
(VR-14, D491).

## Accessibility

The KPI strip, the facet panel, the toolbar and the table are named landmarks; the result count is announced when the
filters change; each chip has its remove button; the facet drawer returns the focus to its button.

## Example images

Not drawn yet: step S8 draws them from this page, one row per persona and device, light and dark
([D490](../../../../06-decisions/ux/d490-example-images-for-every-persona-that-can-open-a-view.md),
[D500](../../../../06-decisions/ux/d500-images-live-in-the-specs-folders.md)).

| Shows | Device | Light | Dark |
|---|---|---|---|
| Listed, U16, view All | desktop | ![Listed, U16, view All, light](../../images/lists/s-sc20-l13-civil-records-u16-office-worker-desktop-light.png) | ![Listed, U16, view All, dark](../../images/lists/s-sc20-l13-civil-records-u16-office-worker-desktop-dark.png) |
| Listed, U56, view All | phone | ![Listed, U56, view All, light](../../images/lists/s-sc20-l13-civil-records-u56-citizen-phone-light.png) | ![Listed, U56, view All, dark](../../images/lists/s-sc20-l13-civil-records-u56-citizen-phone-dark.png) |
| Listed, U16, view All | phone | ![Listed, U16, view All, light](../../images/lists/s-sc20-l13-civil-records-u16-office-worker-phone-light.png) | ![Listed, U16, view All, dark](../../images/lists/s-sc20-l13-civil-records-u16-office-worker-phone-dark.png) |
| Listed, U56, view All | desktop | ![Listed, U56, view All, light](../../images/lists/s-sc20-l13-civil-records-u56-citizen-desktop-light.png) | ![Listed, U56, view All, dark](../../images/lists/s-sc20-l13-civil-records-u56-citizen-desktop-dark.png) |

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md)
- [C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md)
- [C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md)

## Shown in

| Where | Pages |
|---|---|
| Menu | [Public bodies › Civil records](README.md) |
| Workspaces | [U16](../../../../04-ux/views/u16-office-worker/workspace.md) |
| Flows | [FL-SC20-05](../../flows/fl-sc20-05-council-registry-permits-and-assets.md) |

## Open questions

This list waits for the owner's confirmation: its entity was created in the benchmark-gap interview of
2026-11-14.

---

⬅️ [S-SC20-L12 Deliberations](s-sc20-l12-deliberations.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC20-L14 Permit requests](s-sc20-l14-permit-requests.md)
