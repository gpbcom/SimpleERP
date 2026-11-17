🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏭 [SC05 Manufacturing](../../README.md) ›
🖥️ [Screens](../README.md) › 🗂️ [Views: Manufacturing menu](README.md) › 🗂️ S-SC05-L15 Bonded stocks

# 🗂️ S-SC05-L15 Bonded stocks

**Status:** ✅ specified

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U21 Production planner](../../../../01-users/personas/u21-production-planner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U19, U20, U40: their use cases only read these records, inside a screen of the use case, so they
open them from there (D493).

## Purpose

The aggregated list of every [E-SC05-15 Bonded stock](../../data/e-sc05-15-bonded-stock.md) the user may see: to find,
filter, total and act on many bonded stocks at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Manufacturing › Bonded stocks, in the capability's menu (D495).
- **Workspaces:** the persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "bonded stocks" offers this view.
- **AI assistant:** "show the bonded stocks that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Bonded stocks    Manufacturing > Bonded stocks   [+ New]                                                     |
| [count] [Bonded] [new this month]   [chart: count by state]                                                  |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                              n of N results                      |
| category          | [ ] LOT   ITEM   VOLUME   STRENGTH   CATEGORY   DUTY                                     |
| movement          | [ ] ...                                              Open >                              |
| Related records   | [ ] ...                                              Open >                              |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Lot | lot | text | yes |
| Item | item | text | yes |
| Volume | volume | number | yes |
| Strength | strength | number | yes |
| Category | category | text | yes |
| Duty | duty | amount with currency | yes |
| State | state | badge: Bonded, Released, Shipped, Declared | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| Category | each value | the visible rows (D488) |
| Movement | each value | the visible rows (D488) |
| State | Bonded, Released, Shipped, Declared | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Lots of the items in bonded stock.
- From the other side: the alcohol lots not yet entered as bonded stock.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Bonded.
- New this month, by released on.

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
| New bonded stock | header | the personas whose roles may create it | the record's own page (Row opens) |
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

Open › goes to [S-SC05-16 Alcohol excise](../06-excise-refurbishment-and-cutting/s-sc05-16-alcohol-excise.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 bonded stocks of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no bonded stock the user may see yet, with the create action when allowed.
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
| Listed, U21, view All | desktop | ![Listed, U21, view All, light](../../images/lists/s-sc05-l15-bonded-stocks-u21-production-planner-desktop-light.png) | ![Listed, U21, view All, dark](../../images/lists/s-sc05-l15-bonded-stocks-u21-production-planner-desktop-dark.png) |
| Listed, U05, view All | desktop | ![Listed, U05, view All, light](../../images/lists/s-sc05-l15-bonded-stocks-u05-accounting-desktop-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-sc05-l15-bonded-stocks-u05-accounting-desktop-dark.png) |
| Listed, U05, view All | phone | ![Listed, U05, view All, light](../../images/lists/s-sc05-l15-bonded-stocks-u05-accounting-phone-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-sc05-l15-bonded-stocks-u05-accounting-phone-dark.png) |
| Listed, U21, view All | phone | ![Listed, U21, view All, light](../../images/lists/s-sc05-l15-bonded-stocks-u21-production-planner-phone-light.png) | ![Listed, U21, view All, dark](../../images/lists/s-sc05-l15-bonded-stocks-u21-production-planner-phone-dark.png) |

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md)
- [C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md)
- [C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md)

## Shown in

| Where | Pages |
|---|---|
| Menu | [Manufacturing › Bonded stocks](README.md) |
| Workspaces | [U21](../../../../04-ux/views/u21-production-planner/workspace.md), [U05](../../../../04-ux/views/u05-accounting/workspace.md) |
| Flows | [FL-SC05-06](../../flows/fl-sc05-06-excise-refurbishment-and-cutting.md) |

## Open questions

This list waits for the owner's confirmation: its entity was created in the benchmark-gap interview of
2026-11-14.

---

⬅️ [S-SC05-L14 Management reviews](s-sc05-l14-management-reviews.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC05-L16 Graded units](s-sc05-l16-graded-units.md)
