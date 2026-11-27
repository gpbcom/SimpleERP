🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🔧 [SC19 Trades and home services](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Trades and home services menu](README.md) › 🗂️ S-SC19-L07 Installations

# 🗂️ S-SC19-L07 Installations

**Status:** ✅ specified

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U22 Site manager](../../../../01-users/personas/u22-site-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U14 Field worker](../../../../01-users/personas/u14-field-worker.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-SC19-07 Installation](../../data/e-sc19-07-installation.md) the user may see: to find,
filter, total and act on many installations at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Trades and home services › Installations, in the capability's menu (D495).
- **Workspaces:** the persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "installations" offers this view.
- **AI assistant:** "show the installations that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Installations    Trades and home services > Installations   [+ New]                                          |
| [count] [Planned] [new this month]   [chart: count by state]                                                 |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                              n of N results                      |
| kind              | [ ] CUSTOMER   KIND   TECHNICIAN   GRANT   COMMISSIONED   STATE                          |
| technician        | [ ] ...                                              Open >                              |
| Related records   | [ ] ...                                              Open >                              |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Customer | customer | text | yes |
| Kind | kind | text | yes |
| Technician | technician | text | yes |
| Grant | grant | text | yes |
| Commissioned on | commissioned on | date | yes |
| State | state | badge: Planned, InProgress, Completed, Commissioned, Cancelled | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| Kind | each value | the visible rows (D488) |
| Technician | each value | the visible rows (D488) |
| State | Planned, InProgress, Completed, Commissioned, Cancelled | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Accepted quotes.
- From the other side: installations Planned with works due within a week and no grant request.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Planned.
- New this month, by commissioned on.

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
| New installation | header | the personas whose roles may create it | the record's own page (Row opens) |
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
| owner | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-SC19-13](../04-installations-and-labels/s-sc19-13-installation-project.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 installations of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no installation the user may see yet, with the create action when allowed.
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
| Listed, U22, view All | desktop | ![Listed, U22, view All, light](../../images/lists/s-sc19-l07-installations-u22-site-manager-desktop-light.png) | ![Listed, U22, view All, dark](../../images/lists/s-sc19-l07-installations-u22-site-manager-desktop-dark.png) |
| Listed, U14, view All | phone | ![Listed, U14, view All, light](../../images/lists/s-sc19-l07-installations-u14-field-worker-phone-light.png) | ![Listed, U14, view All, dark](../../images/lists/s-sc19-l07-installations-u14-field-worker-phone-dark.png) |
| Listed, U14, view All | desktop | ![Listed, U14, view All, light](../../images/lists/s-sc19-l07-installations-u14-field-worker-desktop-light.png) | ![Listed, U14, view All, dark](../../images/lists/s-sc19-l07-installations-u14-field-worker-desktop-dark.png) |
| Listed, U22, view All | phone | ![Listed, U22, view All, light](../../images/lists/s-sc19-l07-installations-u22-site-manager-phone-light.png) | ![Listed, U22, view All, dark](../../images/lists/s-sc19-l07-installations-u22-site-manager-phone-dark.png) |

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md)
- [C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md)
- [C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md)

## Shown in

| Where | Pages |
|---|---|
| Menu | [Trades and home services › Installations](README.md) |
| Workspaces | [U22](../../../../04-ux/views/u22-site-manager/workspace.md), [U14](../../../../04-ux/views/u14-field-worker/workspace.md) |
| Flows | [FL-SC19-04](../../flows/fl-sc19-04-installations-and-labels.md) |

## Open questions

This list waits for the owner's confirmation: its entity was created in the benchmark-gap interview of
2026-11-14.

---

⬅️ [S-SC19-L06 Household contracts](s-sc19-l06-household-contracts.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC19-L08 Grant files](s-sc19-l08-grant-files.md)
