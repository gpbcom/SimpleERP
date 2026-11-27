🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏪 [F10 Point of sale (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Point of sale (plugin) menu](README.md) › 🗂️ S-F10-L15 Till event logs

# 🗂️ S-F10-L15 Till event logs

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U17 Cashier](../../../../01-users/personas/u17-cashier.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U18: their use cases only read these records, inside a screen of the use case, so they open them
from there (D493).

## Purpose

The aggregated list of every [E-F10-15 Till event log](../../data/e-f10-15-till-event-log.md) the user may see: to find,
filter, total and act on many till event logs at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Point of sale (plugin) › Till event logs, in the capability's menu (D495).
- **Workspaces:** 4 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "till event logs" offers this view.
- **AI assistant:** "show the till event logs that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Till event logs    Point of sale (plugin) › Till event logs   [+ New]                                        |
| [count]   [chart: count by state]                                                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] EVENT   STATE   USER                                                                 |
| user              | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Event | event | label | yes |
| State | state | badge: Recorded | yes |
| User | user | date and time | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Recorded | the visible rows (D488) |
| User | user, time | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: till event logs link to no other record type in their fields.

## KPI strip

- Count of the visible rows.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Mine: user.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New till event log | header | the personas whose roles may create it | the record's own page (Row opens) |
| Assign | bulk bar | the personas whose roles may assign | sets the user; audited |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- user: editable in its cell unless the record's state locks it.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| signature | secret | nobody | everyone (VR-4) |

## Row opens

Open › goes to [S-F10-01 Till session](../01-till-session/s-f10-01-till-session.md).

The records also show on: [S-F10-18 Point of sale reports](../07-set-up-and-report/s-f10-18-point-of-sale-reports.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 till event logs of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no till event log the user may see yet, with the create action when allowed.
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
| Listed, U02, view All | desktop | ![Listed, U02, view All, light](../../images/lists/s-f10-l15-till-event-logs-u02-manager-desktop-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-f10-l15-till-event-logs-u02-manager-desktop-dark.png) |
| Listed, U02, view All | phone | ![Listed, U02, view All, light](../../images/lists/s-f10-l15-till-event-logs-u02-manager-phone-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-f10-l15-till-event-logs-u02-manager-phone-dark.png) |
| Listed, U17, view Mine: user | desktop | ![Listed, U17, view Mine: user, light](../../images/lists/s-f10-l15-till-event-logs-u17-cashier-desktop-light.png) | ![Listed, U17, view Mine: user, dark](../../images/lists/s-f10-l15-till-event-logs-u17-cashier-desktop-dark.png) |
| Listed, U17, view Mine: user | phone | ![Listed, U17, view Mine: user, light](../../images/lists/s-f10-l15-till-event-logs-u17-cashier-phone-light.png) | ![Listed, U17, view Mine: user, dark](../../images/lists/s-f10-l15-till-event-logs-u17-cashier-phone-dark.png) |
| Listed, U05, view Mine: user | desktop | ![Listed, U05, view Mine: user, light](../../images/lists/s-f10-l15-till-event-logs-u05-accounting-desktop-light.png) | ![Listed, U05, view Mine: user, dark](../../images/lists/s-f10-l15-till-event-logs-u05-accounting-desktop-dark.png) |
| Listed, U05, view Mine: user | phone | ![Listed, U05, view Mine: user, light](../../images/lists/s-f10-l15-till-event-logs-u05-accounting-phone-light.png) | ![Listed, U05, view Mine: user, dark](../../images/lists/s-f10-l15-till-event-logs-u05-accounting-phone-dark.png) |
| Listed, U13, view All | desktop | ![Listed, U13, view All, light](../../images/lists/s-f10-l15-till-event-logs-u13-owner-desktop-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f10-l15-till-event-logs-u13-owner-desktop-dark.png) |
| Listed, U13, view All | phone | ![Listed, U13, view All, light](../../images/lists/s-f10-l15-till-event-logs-u13-owner-phone-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f10-l15-till-event-logs-u13-owner-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Point of sale (plugin) › Till event logs](README.md) |
| Workspaces | [U02](../../../../04-ux/views/u02-manager/workspace.md), [U17](../../../../04-ux/views/u17-cashier/workspace.md), [U05](../../../../04-ux/views/u05-accounting/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md) |
| Flows | [FL-F10-01](../../flows/fl-f10-01-till-session.md), [FL-F10-07](../../flows/fl-f10-07-set-up-and-report.md) |

## Open questions

None.

---

⬅️ [S-F10-L14 Point of sale devices](s-f10-l14-point-of-sale-devices.md) · ⬆️ [Up](README.md) ·
➡️ [S-F10-L16 Age checks](s-f10-l16-age-checks.md)
