🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏘️ [SC10 Real estate](../../README.md) ›
🖥️ [Screens](../README.md) › 🗂️ [Views: Real estate menu](README.md) › 🗂️ S-SC10-L01 Mandates

# 🗂️ S-SC10-L01 Mandates

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U35 Real-estate agent](../../../../01-users/personas/u35-real-estate-agent.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-SC10-01 Mandate](../../data/e-sc10-01-mandate.md) the user may see: to find, filter,
total and act on many mandates at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Real estate › Mandates, in the capability's menu (D495).
- **Workspaces:** 1 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "mandates" offers this view.
- **AI assistant:** "show the mandates that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Mandates    Real estate › Mandates   [+ New]                                                                 |
| [count] [total price] [Blocked] [due in 7 days]   [chart: count by state, price stacked]                     |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] NUMBER   STATE   OWNER   PRICE   END   KIND                                          |
| kind              | [ ] ...                                                  Open >                          |
| owner             | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Number | number | label | yes |
| State | state | badge: Signed, Active, Blocked, Cancelled | yes |
| Owner | owner | link to the record | yes |
| Price | price | amount, right-aligned | yes |
| End | end | date | yes |
| Kind | kind | label | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Signed, Active, Blocked, Cancelled | the visible rows (D488) |
| Kind | register number, sale or letting | the visible rows (D488) |
| Owner | each linked owner | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: mandates link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- Total of price.
- Needs attention: count in the state Blocked.
- Due in 7 days, by end.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state, price stacked (VR-8); the Chart button turns the filtered list into a chart the user can pin to their
home screen (C-09).

## Saved views

- All.
- Mine: owner.
- Open: Signed, Active, Blocked.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

- **Place:** property.
- **Layout:** a map, [C-17](../../../../04-ux/design-system/components/c-17-map.md).
- **Marker:** the number and the state.
- **Layers:** by state.
- **Who sees the switch:** the roles with the map right, the planner roles and U02 and U13 (BR-F1-32, D502); the others
  see the table with the place as a column.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New mandate | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Assign | bulk bar | the personas whose roles may assign | sets the owner; audited |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- kind: editable in its cell unless the record's state locks it.
- owner: editable in its cell unless the record's state locks it.
- end: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-SC10-01 Mandates](../01-mandates-and-listings/s-sc10-01-mandates.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 mandates of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no mandate the user may see yet, with the create action when allowed.
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
| Listed, U35, view Mine: owner | desktop | ![Listed, U35, view Mine: owner, light](../../images/lists/s-sc10-l01-mandates-u35-real-estate-agent-desktop-light.png) | ![Listed, U35, view Mine: owner, dark](../../images/lists/s-sc10-l01-mandates-u35-real-estate-agent-desktop-dark.png) |
| Listed, U35, view Mine: owner | phone | ![Listed, U35, view Mine: owner, light](../../images/lists/s-sc10-l01-mandates-u35-real-estate-agent-phone-light.png) | ![Listed, U35, view Mine: owner, dark](../../images/lists/s-sc10-l01-mandates-u35-real-estate-agent-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md),
[C-17 Map](../../../../04-ux/design-system/components/c-17-map.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Real estate › Mandates](README.md) |
| Workspaces | [U35](../../../../04-ux/views/u35-real-estate-agent/workspace.md) |
| Flows | [FL-SC10-01](../../flows/fl-sc10-01-mandates-and-listings.md) |

## Open questions

None.

---

⬅️ [S-SC10-24 Coworking](../07-short-stays-commercial-and-coworking/s-sc10-24-coworking.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC10-L02 Property listings](s-sc10-l02-property-listings.md)
