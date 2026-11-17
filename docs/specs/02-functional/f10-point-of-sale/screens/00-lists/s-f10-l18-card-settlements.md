🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏪 [F10 Point of sale (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Point of sale (plugin) menu](README.md) › 🗂️ S-F10-L18 Card settlements

# 🗂️ S-F10-L18 Card settlements

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U17, U18: their use cases only read these records, inside a screen of the use case, so they open
them from there (D493).

## Purpose

The aggregated list of every [E-F10-18 Card settlement](../../data/e-f10-18-card-settlement.md) the user may see: to
find, filter, total and act on many card settlements at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Point of sale (plugin) › Card settlements, in the capability's menu (D495).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "card settlements" offers this view.
- **AI assistant:** "show the card settlements that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Card settlements    Point of sale (plugin) › Card settlements   [+ New]                                      |
| [count] [total fees] [new this month]   [chart: count by state, fees stacked]                                |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] ACQUIRER AND DATE   STATUS   FEES   SESSIONS                                         |
| sessions          | [ ] ...                                                  Open >                          |
| status            | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Acquirer and date | acquirer and date | date | yes |
| Status | status | badge | yes |
| Fees | fees | amount, right-aligned | yes |
| Sessions | sessions | text | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Matched, Gap | the visible rows (D488) |
| Sessions | each value | the visible rows (D488) |
| Status | Matched, Gap | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: card settlements link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- Total of fees.
- New this month, by acquirer and date.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state, fees stacked (VR-8); the Chart button turns the filtered list into a chart the user can pin to their
home screen (C-09).

## Saved views

- All.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New card settlement | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change status | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- sessions: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F10-23 Card settlements](../09-cash-and-settlements/s-f10-23-card-settlements.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 card settlements of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no card settlement the user may see yet, with the create action when allowed.
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
| Listed, U05, view All | desktop | ![Listed, U05, view All, light](../../images/lists/s-f10-l18-card-settlements-u05-accounting-desktop-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-f10-l18-card-settlements-u05-accounting-desktop-dark.png) |
| Listed, U05, view All | phone | ![Listed, U05, view All, light](../../images/lists/s-f10-l18-card-settlements-u05-accounting-phone-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-f10-l18-card-settlements-u05-accounting-phone-dark.png) |
| Listed, U13, view All | desktop | ![Listed, U13, view All, light](../../images/lists/s-f10-l18-card-settlements-u13-owner-desktop-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f10-l18-card-settlements-u13-owner-desktop-dark.png) |
| Listed, U13, view All | phone | ![Listed, U13, view All, light](../../images/lists/s-f10-l18-card-settlements-u13-owner-phone-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f10-l18-card-settlements-u13-owner-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Point of sale (plugin) › Card settlements](README.md) |
| Workspaces | [U05](../../../../04-ux/views/u05-accounting/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md) |
| Flows | [FL-F10-09](../../flows/fl-f10-09-cash-and-settlements.md) |

## Open questions

None.

---

⬅️ [S-F10-L17 Cash movements](s-f10-l17-cash-movements.md) · ⬆️ [Up](README.md) ·
➡️ [S-F10-L19 Clienteling profiles](s-f10-l19-clienteling-profiles.md)
