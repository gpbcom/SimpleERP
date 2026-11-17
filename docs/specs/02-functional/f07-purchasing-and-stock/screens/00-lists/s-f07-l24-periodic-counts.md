🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📦 [F7 Purchasing and stock](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Purchasing and stock menu](README.md) › 🗂️ S-F7-L24 Periodic counts

# 🗂️ S-F7-L24 Periodic counts

**Status:** ✅ specified

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U04 Purchasing and stock](../../../../01-users/personas/u04-purchasing.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F7-24 Periodic count](../../data/e-f07-24-periodic-count.md) the user may see: to find,
filter, total and act on many periodic counts at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Purchasing and stock › Periodic counts, in the capability's menu (D495).
- **Workspaces:** the persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "periodic counts" offers this view.
- **AI assistant:** "show the periodic counts that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Periodic counts    Purchasing and stock > Periodic counts   [+ New]                                          |
| [count] [Approved] [new this month]   [chart: count by state]                                                |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                              n of N results                      |
| period            | [ ] PERIOD   OPENING VALU   PURCHASES   CLOSING VALU   STOCK VARIAT   STATE              |
| approved by       | [ ] ...                                              Open >                              |
| Related records   | [ ] ...                                              Open >                              |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Period | period | text | yes |
| Opening value | opening value | amount with currency | yes |
| Purchases | purchases | amount with currency | yes |
| Closing value | closing value | amount with currency | yes |
| Stock variation | stock variation | amount with currency | yes |
| State | state | badge: Counted, Valued, Approved, Posted, Reversed | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| Period | each value | the visible rows (D488) |
| Approved by | each value | the visible rows (D488) |
| State | Counted, Valued, Approved, Posted, Reversed | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Valuations of a chosen period, or of the periods that match a filter.
- From the other side: the periods with no valuation.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Approved.
- New this month, by period.

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
| New periodic count | header | the personas whose roles may create it | the record's own page (Row opens) |
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
| approved by | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| owner | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F7-27 Periodic valuation](../10-consignment-scanning-and-edi/s-f07-27-periodic-valuation.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 periodic counts of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no periodic count the user may see yet, with the create action when allowed.
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
| Listed, U05, view All | desktop | ![Listed, U05, view All, light](../../images/lists/s-f07-l24-periodic-counts-u05-accounting-desktop-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-f07-l24-periodic-counts-u05-accounting-desktop-dark.png) |
| Listed, U04, view All | desktop | ![Listed, U04, view All, light](../../images/lists/s-f07-l24-periodic-counts-u04-purchasing-desktop-light.png) | ![Listed, U04, view All, dark](../../images/lists/s-f07-l24-periodic-counts-u04-purchasing-desktop-dark.png) |
| Listed, U04, view All | phone | ![Listed, U04, view All, light](../../images/lists/s-f07-l24-periodic-counts-u04-purchasing-phone-light.png) | ![Listed, U04, view All, dark](../../images/lists/s-f07-l24-periodic-counts-u04-purchasing-phone-dark.png) |
| Listed, U05, view All | phone | ![Listed, U05, view All, light](../../images/lists/s-f07-l24-periodic-counts-u05-accounting-phone-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-f07-l24-periodic-counts-u05-accounting-phone-dark.png) |

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md)
- [C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md)
- [C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md)

## Shown in

| Where | Pages |
|---|---|
| Menu | [Purchasing and stock › Periodic counts](README.md) |
| Workspaces | [U05](../../../../04-ux/views/u05-accounting/workspace.md), [U04](../../../../04-ux/views/u04-purchasing/workspace.md) |
| Flows | [FL-F7-10](../../flows/fl-f07-10-consignment-scanning-and-edi.md) |

## Open questions

This list waits for the owner's confirmation: its entity was created in the benchmark-gap interview of
2026-11-14.

---

⬅️ [S-F7-L23 Stock owners](s-f07-l23-stock-owners.md) · ⬆️ [Up](README.md) ·
➡️ [S-F7-L25 Packaging deposits](s-f07-l25-packaging-deposits.md)
