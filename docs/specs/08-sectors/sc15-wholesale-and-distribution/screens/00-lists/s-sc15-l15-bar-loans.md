🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
📦 [SC15 Wholesale and distribution](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Wholesale and distribution menu](README.md) › 🗂️ S-SC15-L15 Bar loans

# 🗂️ S-SC15-L15 Bar loans

**Status:** ✅ specified

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U42 Sales representative](../../../../01-users/personas/u42-sales-representative.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U04 Purchasing and stock](../../../../01-users/personas/u04-purchasing.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U09: their use cases only read these records, inside a screen of the use case, so they open them
from there (D493).

## Purpose

The aggregated list of every [E-SC15-15 Bar loan](../../data/e-sc15-15-bar-loan.md) the user may see: to find, filter,
total and act on many bar loans at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Wholesale and distribution › Bar loans, in the capability's menu (D495).
- **Workspaces:** the persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "bar loans" offers this view.
- **AI assistant:** "show the bar loans that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Bar loans    Wholesale and distribution > Bar loans   [+ New]                                                |
| [count] [Lent] [new this month]   [chart: count by state]                                                    |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                              n of N results                      |
| equipment         | [ ] CUSTOMER   EQUIPMENT   SERIAL   VALUE   VOLUME COMMI   VOLUME BOUGH                  |
| customer          | [ ] ...                                              Open >                              |
| Related records   | [ ] ...                                              Open >                              |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Customer | customer | text | yes |
| Equipment | equipment | text | yes |
| Serial | serial | text | yes |
| Value | value | amount with currency | yes |
| Volume commitment | volume commitment | number | yes |
| Volume bought | volume bought | number | yes |
| State | state | badge: Lent, Returned, Lost | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| Equipment | each value | the visible rows (D488) |
| Customer | each value | the visible rows (D488) |
| State | Lent, Returned, Lost | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Deposits on returnable packaging.
- From the other side: loans of bars that fell below their commitment.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Lent.
- New this month, by lent on.

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
| New bar loan | header | the personas whose roles may create it | the record's own page (Row opens) |
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

Open › goes to [S-SC15-21](../06-beverages-vans-weights-and-devices/s-sc15-21-beverage-distribution.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 bar loans of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no bar loan the user may see yet, with the create action when allowed.
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
| Listed, U42, view All | phone | ![Listed, U42, view All, light](../../images/lists/s-sc15-l15-bar-loans-u42-sales-representative-phone-light.png) | ![Listed, U42, view All, dark](../../images/lists/s-sc15-l15-bar-loans-u42-sales-representative-phone-dark.png) |
| Listed, U04, view All | desktop | ![Listed, U04, view All, light](../../images/lists/s-sc15-l15-bar-loans-u04-purchasing-desktop-light.png) | ![Listed, U04, view All, dark](../../images/lists/s-sc15-l15-bar-loans-u04-purchasing-desktop-dark.png) |
| Listed, U04, view All | phone | ![Listed, U04, view All, light](../../images/lists/s-sc15-l15-bar-loans-u04-purchasing-phone-light.png) | ![Listed, U04, view All, dark](../../images/lists/s-sc15-l15-bar-loans-u04-purchasing-phone-dark.png) |
| Listed, U42, view All | desktop | ![Listed, U42, view All, light](../../images/lists/s-sc15-l15-bar-loans-u42-sales-representative-desktop-light.png) | ![Listed, U42, view All, dark](../../images/lists/s-sc15-l15-bar-loans-u42-sales-representative-desktop-dark.png) |

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md)
- [C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md)
- [C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md)

## Shown in

| Where | Pages |
|---|---|
| Menu | [Wholesale and distribution › Bar loans](README.md) |
| Workspaces | [U42](../../../../04-ux/views/u42-sales-representative/workspace.md), [U04](../../../../04-ux/views/u04-purchasing/workspace.md) |
| Flows | [FL-SC15-06](../../flows/fl-sc15-06-beverages-vans-weights-and-devices.md) |

## Open questions

This list waits for the owner's confirmation: its entity was created in the benchmark-gap interview of
2026-11-14.

---

⬅️ [S-SC15-L14 Pallets](s-sc15-l14-pallets.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC15-L16 Van stocks](s-sc15-l16-van-stocks.md)
