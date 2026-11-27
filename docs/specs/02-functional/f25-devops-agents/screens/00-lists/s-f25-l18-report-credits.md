🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: DevOps agents (hosted edition) menu](README.md) › 🗂️ S-F25-L18 Report credits

# 🗂️ S-F25-L18 Report credits

**Status:** ✅ specified

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U47 SimpleERP maintainer](../../../../01-users/personas/u47-simpleerp-maintainer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F25-18 Report credit](../../data/e-f25-18-report-credit.md) the user may see: to find,
filter, total and act on many report credits at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** DevOps agents › Report credits, in the capability's menu (D495).
- **Workspaces:** the persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "report credits" offers this view.
- **AI assistant:** "show the report credits that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Report credits    DevOps agents > Report credits   [+ New]                                                   |
| [count] [Pending] [new this month]   [chart: count by state]                                                 |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                              n of N results                      |
| company           | [ ] REPORT   COMPANY   SEVERITY   AMOUNT   BILL   STATE                                  |
| severity          | [ ] ...                                              Open >                              |
| Related records   | [ ] ...                                              Open >                              |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Report | report | text | yes |
| Company | company | text | yes |
| Severity | severity | text | yes |
| Amount | amount | amount with currency | yes |
| Bill | bill | text | yes |
| State | state | badge: Pending, Granted, Refused, Applied, Withdrawn | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| Company | each value | the visible rows (D488) |
| Severity | each value | the visible rows (D488) |
| State | Pending, Granted, Refused, Applied, Withdrawn | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- The user ticket behind a credit.
- The vulnerability case behind a credit, when any.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Pending.
- New this month, by bill.

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
| New report credit | header | the personas whose roles may create it | the record's own page (Row opens) |
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

Open › goes to [S-F25-27 Report credits](../07-roadmap-beta-and-credits/s-f25-27-report-credits.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 report credits of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no report credit the user may see yet, with the create action when allowed.
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
| Listed, U07, view All | desktop | ![Listed, U07, view All, light](../../images/lists/s-f25-l18-report-credits-u07-administrator-desktop-light.png) | ![Listed, U07, view All, dark](../../images/lists/s-f25-l18-report-credits-u07-administrator-desktop-dark.png) |
| Listed, U47, view All | desktop | ![Listed, U47, view All, light](../../images/lists/s-f25-l18-report-credits-u47-simpleerp-maintainer-desktop-light.png) | ![Listed, U47, view All, dark](../../images/lists/s-f25-l18-report-credits-u47-simpleerp-maintainer-desktop-dark.png) |
| Listed, U07, view All | phone | ![Listed, U07, view All, light](../../images/lists/s-f25-l18-report-credits-u07-administrator-phone-light.png) | ![Listed, U07, view All, dark](../../images/lists/s-f25-l18-report-credits-u07-administrator-phone-dark.png) |
| Listed, U47, view All | phone | ![Listed, U47, view All, light](../../images/lists/s-f25-l18-report-credits-u47-simpleerp-maintainer-phone-light.png) | ![Listed, U47, view All, dark](../../images/lists/s-f25-l18-report-credits-u47-simpleerp-maintainer-phone-dark.png) |

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md)
- [C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md)
- [C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md)

## Shown in

| Where | Pages |
|---|---|
| Menu | [DevOps agents › Report credits](README.md) |
| Workspaces | [U07](../../../../04-ux/views/u07-administrator/workspace.md), [U47](../../../../04-ux/views/u47-simpleerp-maintainer/workspace.md) |
| Flows | [FL-F25-07](../../flows/fl-f25-07-roadmap-beta-and-credits.md) |

## Open questions

This list waits for the owner's confirmation: its entity was created in the benchmark-gap interview of
2026-11-14.

---

⬅️ [S-F25-L17 Beta enrolments](s-f25-l17-beta-enrolments.md) · ⬆️ [Up](README.md) ·
➡️ [S-F25-L19 Work contracts](s-f25-l19-work-contracts.md)
