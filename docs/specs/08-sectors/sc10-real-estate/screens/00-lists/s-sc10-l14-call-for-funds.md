🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏘️ [SC10 Real estate](../../README.md) ›
🖥️ [Screens](../README.md) › 🗂️ [Views: Real estate menu](README.md) › 🗂️ S-SC10-L14 Call for funds

# 🗂️ S-SC10-L14 Call for funds

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U34 Property manager](../../../../01-users/personas/u34-property-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-SC10-14 Call for funds](../../data/e-sc10-14-call-for-funds.md) the user may see: to
find, filter, total and act on many call for funds at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Real estate › Call for funds, in the capability's menu (D495).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "call for funds" offers this view.
- **AI assistant:** "show the call for funds that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Call for funds    Real estate › Call for funds   [+ New]                                                     |
| [count] [total amount] [new this month]   [chart: count by state, amount stacked]                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] CO-OWNERSHIP   STATE   LOT   AMOUNT   PERIOD   KIND                                  |
| co-ownership      | [ ] ...                                                  Open >                          |
| kind              | [ ] ...                                                  Open >                          |
| lot               | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Co-ownership | co-ownership | link to the record | yes |
| State | state | badge: Recorded | yes |
| Lot | lot | link to the record | yes |
| Amount | amount | amount, right-aligned | yes |
| Period | period | link to the record | yes |
| Kind | kind | link to the record | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Recorded | the visible rows (D488) |
| Co-ownership | each linked co-ownership | the visible rows (D488) |
| Kind | each linked kind | the visible rows (D488) |
| Lot | each linked lot | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Call for funds of a chosen lot, or of the lots that match a filter.
- From the other side: the lots that have call for funds, or none.

## KPI strip

- Count of the visible rows.
- Total of amount.
- New this month, by period.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state, amount stacked (VR-8); the Chart button turns the filtered list into a chart the user can pin to their
home screen (C-09).

## Saved views

- All.
- Mine: co-ownership.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New call for funds | header | the personas whose roles may create it | the record's own page (Row opens) |
| Assign | bulk bar | the personas whose roles may assign | sets the co-ownership; audited |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- period: editable in its cell unless the record's state locks it.
- kind: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-SC10-16 Budget and calls](../05-co-ownership/s-sc10-16-budget-and-calls.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 call for funds of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no call for funds the user may see yet, with the create action when allowed.
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
| Listed, U34, view All | desktop | ![Listed, U34, view All, light](../../images/lists/s-sc10-l14-call-for-funds-u34-property-manager-desktop-light.png) | ![Listed, U34, view All, dark](../../images/lists/s-sc10-l14-call-for-funds-u34-property-manager-desktop-dark.png) |
| Listed, U34, view All | phone | ![Listed, U34, view All, light](../../images/lists/s-sc10-l14-call-for-funds-u34-property-manager-phone-light.png) | ![Listed, U34, view All, dark](../../images/lists/s-sc10-l14-call-for-funds-u34-property-manager-phone-dark.png) |
| Listed, U09, view Mine: co-ownership | desktop | ![Listed, U09, view Mine: co-ownership, light](../../images/lists/s-sc10-l14-call-for-funds-u09-customer-desktop-light.png) | ![Listed, U09, view Mine: co-ownership, dark](../../images/lists/s-sc10-l14-call-for-funds-u09-customer-desktop-dark.png) |
| Listed, U09, view Mine: co-ownership | phone | ![Listed, U09, view Mine: co-ownership, light](../../images/lists/s-sc10-l14-call-for-funds-u09-customer-phone-light.png) | ![Listed, U09, view Mine: co-ownership, dark](../../images/lists/s-sc10-l14-call-for-funds-u09-customer-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Real estate › Call for funds](README.md) |
| Workspaces | [U34](../../../../04-ux/views/u34-property-manager/workspace.md), [U09](../../../../04-ux/views/u09-customer/workspace.md) |
| Flows | [FL-SC10-05](../../flows/fl-sc10-05-co-ownership.md) |

## Open questions

None.

---

⬅️ [S-SC10-L13 Co-owners' assemblies](s-sc10-l13-co-owners-assemblies.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC10-L15 Works funds](s-sc10-l15-works-funds.md)
