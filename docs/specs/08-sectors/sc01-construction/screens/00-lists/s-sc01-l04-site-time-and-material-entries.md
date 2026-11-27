🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏗️ [SC01 Construction](../../README.md) ›
🖥️ [Screens](../README.md) › 🗂️ [Views: Construction menu](README.md) › 🗂️ S-SC01-L04 Site time and material entries

# 🗂️ S-SC01-L04 Site time and material entries

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U14 Field worker](../../../../01-users/personas/u14-field-worker.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U22 Site manager](../../../../01-users/personas/u22-site-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every
[E-SC01-04 Site time and material entry](../../data/e-sc01-04-site-time-and-material-entry.md) the user may see: to
find, filter, total and act on many site time and material entries at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Construction › Site time and material entries, in the capability's menu (D495).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "site time and material entries" offers this view.
- **AI assistant:** "show the site time and material entries that need attention" opens it with the filter as editable
  chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Site time and material entries    Construction › Site time and material entries   [+ New]                    |
| [count]   [chart: count by state]                                                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] SITE   STATE   LOT   PERSON OR ITEM   ENTERED OFFLINE                                |
| site              | [ ] ...                                                  Open >                          |
| lot               | [ ] ...                                                  Open >                          |
| person or item    | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Site | site | link to the record | yes |
| State | state | badge: Recorded | yes |
| Lot | lot | link to the record | yes |
| Person or item | person or item | link to the record | yes |
| Entered offline | entered offline | yes or no | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Recorded | the visible rows (D488) |
| Site | each linked site | the visible rows (D488) |
| Lot | each linked lot | the visible rows (D488) |
| Person or item | each linked person or item | the visible rows (D488) |
| Entered offline | yes, no | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Site time and material entries of a chosen lot, or of the lots that match a filter.
- From the other side: the lots that have site time and material entries, or none.
- Site time and material entries of a chosen person or item, or of the person or items that match a filter.
- From the other side: the person or items that have site time and material entries, or none.

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

- **Place:** site.
- **Layout:** a map, [C-17](../../../../04-ux/design-system/components/c-17-map.md).
- **Marker:** the site and the state.
- **Layers:** by state.
- **Who sees the switch:** the roles with the map right, the planner roles and U02 and U13 (BR-F1-32, D502); the others
  see the table with the place as a column.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New site time and material entry | header | the personas whose roles may create it | the record's own page (Row opens) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- entered offline: editable in its cell unless the record's state locks it.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| person or item | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-SC01-04 Site time](../03-run-the-site/s-sc01-04-site-time.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 site time and material entries of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no site time and material entry the user may see yet, with the create action when allowed.
- **Selected:** the bulk bar with the actions allowed on every selected row.
- **Error:** the query failed, with Retry.

On the map layout, Listed also shows the count of rows without a place.

## Responsive behaviour

On a phone the table keeps its columns and scrolls sideways, the facet panel becomes a drawer and the KPI strip stays
(VR-14, D491); the map takes the full width.

## Accessibility

The KPI strip, the facet panel, the toolbar and the table are named landmarks; the result count is announced when the
filters change; each chip has its remove button; the facet drawer returns the focus to its button. The table holds the
same rows as the map.

## Example images

Drawn in step S8 (36k) from this page: one row per persona and device for each state of the view, light and dark
([D490](../../../../06-decisions/ux/d490-example-images-for-every-persona-that-can-open-a-view.md),
[D500](../../../../06-decisions/ux/d500-images-live-in-the-specs-folders.md)).

| Shows | Device | Light | Dark |
|---|---|---|---|
| Listed, U14, view All | desktop | ![Listed, U14, view All, light](../../images/lists/s-sc01-l04-site-time-and-material-entries-u14-field-worker-desktop-light.png) | ![Listed, U14, view All, dark](../../images/lists/s-sc01-l04-site-time-and-material-entries-u14-field-worker-desktop-dark.png) |
| Listed, U14, view All | phone | ![Listed, U14, view All, light](../../images/lists/s-sc01-l04-site-time-and-material-entries-u14-field-worker-phone-light.png) | ![Listed, U14, view All, dark](../../images/lists/s-sc01-l04-site-time-and-material-entries-u14-field-worker-phone-dark.png) |
| Listed, U22, view All | desktop | ![Listed, U22, view All, light](../../images/lists/s-sc01-l04-site-time-and-material-entries-u22-site-manager-desktop-light.png) | ![Listed, U22, view All, dark](../../images/lists/s-sc01-l04-site-time-and-material-entries-u22-site-manager-desktop-dark.png) |
| Listed, U22, view All | phone | ![Listed, U22, view All, light](../../images/lists/s-sc01-l04-site-time-and-material-entries-u22-site-manager-phone-light.png) | ![Listed, U22, view All, dark](../../images/lists/s-sc01-l04-site-time-and-material-entries-u22-site-manager-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md),
[C-17 Map](../../../../04-ux/design-system/components/c-17-map.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Construction › Site time and material entries](README.md) |
| Workspaces | [U14](../../../../04-ux/views/u14-field-worker/workspace.md), [U22](../../../../04-ux/views/u22-site-manager/workspace.md) |
| Flows | [FL-SC01-03](../../flows/fl-sc01-03-run-the-site.md), [FL-SC03-04](../../../sc03-services/flows/fl-sc03-04-bill-and-recognise.md) |

## Open questions

None.

---

⬅️ [S-SC01-L03 Site phases](s-sc01-l03-site-phases.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC01-L05 Site diary entries](s-sc01-l05-site-diary-entries.md)
