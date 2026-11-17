🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏗️ [SC01 Construction](../../README.md) ›
🖥️ [Screens](../README.md) › 🗂️ [Views: Construction menu](README.md) › 🗂️ S-SC01-L05 Site diary entries

# 🗂️ S-SC01-L05 Site diary entries

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U14 Field worker](../../../../01-users/personas/u14-field-worker.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U22 Site manager](../../../../01-users/personas/u22-site-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-SC01-05 Site diary entry](../../data/e-sc01-05-site-diary-entry.md) the user may see: to
find, filter, total and act on many site diary entries at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Construction › Site diary entries, in the capability's menu (D495).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "site diary entries" offers this view.
- **AI assistant:** "show the site diary entries that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Site diary entries    Construction › Site diary entries   [+ New]                                            |
| [count] [new this month]   [chart: count by state]                                                           |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] SITE   STATE   DATE                                                                  |
| site              | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Site | site | date | yes |
| State | state | badge: Recorded | yes |
| Date | date | date | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Recorded | the visible rows (D488) |
| Site | site, date | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: site diary entries link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- New this month, by date.

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
| New site diary entry | header | the personas whose roles may create it | the record's own page (Row opens) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- date: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-SC01-05 Site diary](../03-run-the-site/s-sc01-05-site-diary.md).

The records also show on: [S-SC01-15 Site assistant](../03-run-the-site/s-sc01-15-site-assistant.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 site diary entries of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no site diary entry the user may see yet, with the create action when allowed.
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
| Listed, U14, view All | desktop | ![Listed, U14, view All, light](../../images/lists/s-sc01-l05-site-diary-entries-u14-field-worker-desktop-light.png) | ![Listed, U14, view All, dark](../../images/lists/s-sc01-l05-site-diary-entries-u14-field-worker-desktop-dark.png) |
| Listed, U14, view All | phone | ![Listed, U14, view All, light](../../images/lists/s-sc01-l05-site-diary-entries-u14-field-worker-phone-light.png) | ![Listed, U14, view All, dark](../../images/lists/s-sc01-l05-site-diary-entries-u14-field-worker-phone-dark.png) |
| Listed, U22, view All | desktop | ![Listed, U22, view All, light](../../images/lists/s-sc01-l05-site-diary-entries-u22-site-manager-desktop-light.png) | ![Listed, U22, view All, dark](../../images/lists/s-sc01-l05-site-diary-entries-u22-site-manager-desktop-dark.png) |
| Listed, U22, view All | phone | ![Listed, U22, view All, light](../../images/lists/s-sc01-l05-site-diary-entries-u22-site-manager-phone-light.png) | ![Listed, U22, view All, dark](../../images/lists/s-sc01-l05-site-diary-entries-u22-site-manager-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md),
[C-17 Map](../../../../04-ux/design-system/components/c-17-map.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Construction › Site diary entries](README.md) |
| Workspaces | [U14](../../../../04-ux/views/u14-field-worker/workspace.md), [U22](../../../../04-ux/views/u22-site-manager/workspace.md) |
| Flows | [FL-SC01-03](../../flows/fl-sc01-03-run-the-site.md) |

## Open questions

None.

---

⬅️ [S-SC01-L04 Site time and material entries](s-sc01-l04-site-time-and-material-entries.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC01-L06 Progress bills](s-sc01-l06-progress-bills.md)
