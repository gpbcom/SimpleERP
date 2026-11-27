🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🎭 [SC16 Events and culture](../../README.md) ›
🖥️ [Screens](../README.md) › 🗂️ [Views: Events and culture menu](README.md) › 🗂️ S-SC16-L01 Shows

# 🗂️ S-SC16-L01 Shows

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U43 Event producer](../../../../01-users/personas/u43-event-producer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U44 Box-office agent](../../../../01-users/personas/u44-box-office-agent.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-SC16-01 Show](../../data/e-sc16-01-show.md) the user may see: to find, filter, total and
act on many shows at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Events and culture › Shows, in the capability's menu (D495).
- **Workspaces:** 3 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "shows" offers this view.
- **AI assistant:** "show the shows that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Shows    Events and culture › Shows   [+ New]                                                                |
| [count]   [chart: count by state]                                                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] NAME   STATE                                                                         |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Name | name | link to the record | yes |
| State | state | badge: OnSale, Approved, Paid, Held | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | OnSale, Approved, Paid, Held | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: shows link to no other record type in their fields.

## KPI strip

- Count of the visible rows.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Open: OnSale, Approved, Held.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

- **Place:** venue.
- **Layout:** a map, [C-17](../../../../04-ux/design-system/components/c-17-map.md).
- **Marker:** the name and the state.
- **Layers:** by state.
- **Who sees the switch:** the roles with the map right, the planner roles and U02 and U13 (BR-F1-32, D502); the others
  see the table with the place as a column.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New show | header | the personas whose roles may create it | the record's own page (Row opens) |
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

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-SC16-01 Event plan](../01-plan-and-book/s-sc16-01-event-plan.md).

The records also show on: [S-SC16-18 Event report](../05-declarations-and-reports/s-sc16-18-event-report.md),
[S-SC16-20 Events assistant](../05-declarations-and-reports/s-sc16-20-events-assistant.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 shows of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no show the user may see yet, with the create action when allowed.
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
| Listed, U43, view Open: OnSale, Approved, Held | desktop | ![Listed, U43, view Open: OnSale, Approved, Held, light](../../images/lists/s-sc16-l01-shows-u43-event-producer-desktop-light.png) | ![Listed, U43, view Open: OnSale, Approved, Held, dark](../../images/lists/s-sc16-l01-shows-u43-event-producer-desktop-dark.png) |
| Listed, U43, view Open: OnSale, Approved, Held | phone | ![Listed, U43, view Open: OnSale, Approved, Held, light](../../images/lists/s-sc16-l01-shows-u43-event-producer-phone-light.png) | ![Listed, U43, view Open: OnSale, Approved, Held, dark](../../images/lists/s-sc16-l01-shows-u43-event-producer-phone-dark.png) |
| Listed, U13, view Open: OnSale, Approved, Held | desktop | ![Listed, U13, view Open: OnSale, Approved, Held, light](../../images/lists/s-sc16-l01-shows-u13-owner-desktop-light.png) | ![Listed, U13, view Open: OnSale, Approved, Held, dark](../../images/lists/s-sc16-l01-shows-u13-owner-desktop-dark.png) |
| Listed, U13, view Open: OnSale, Approved, Held | phone | ![Listed, U13, view Open: OnSale, Approved, Held, light](../../images/lists/s-sc16-l01-shows-u13-owner-phone-light.png) | ![Listed, U13, view Open: OnSale, Approved, Held, dark](../../images/lists/s-sc16-l01-shows-u13-owner-phone-dark.png) |
| Listed, U44, view Open: OnSale, Approved, Held | desktop | ![Listed, U44, view Open: OnSale, Approved, Held, light](../../images/lists/s-sc16-l01-shows-u44-box-office-agent-desktop-light.png) | ![Listed, U44, view Open: OnSale, Approved, Held, dark](../../images/lists/s-sc16-l01-shows-u44-box-office-agent-desktop-dark.png) |
| Listed, U44, view Open: OnSale, Approved, Held | phone | ![Listed, U44, view Open: OnSale, Approved, Held, light](../../images/lists/s-sc16-l01-shows-u44-box-office-agent-phone-light.png) | ![Listed, U44, view Open: OnSale, Approved, Held, dark](../../images/lists/s-sc16-l01-shows-u44-box-office-agent-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md),
[C-17 Map](../../../../04-ux/design-system/components/c-17-map.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Events and culture › Shows](README.md) |
| Workspaces | [U43](../../../../04-ux/views/u43-event-producer/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md), [U44](../../../../04-ux/views/u44-box-office-agent/workspace.md) |
| Flows | [FL-SC16-01](../../flows/fl-sc16-01-plan-and-book.md), [FL-SC16-05](../../flows/fl-sc16-05-declarations-and-reports.md) |

## Open questions

None.

---

⬅️ [S-SC16-24 Photography](../06-cashless-cinemas-tours-and-photos/s-sc16-24-photography.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC16-L02 Event budgets](s-sc16-l02-event-budgets.md)
