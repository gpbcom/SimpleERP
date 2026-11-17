🏠 [Specs](../../../../README.md) › ⚙️ [Technical capabilities](../../../README.md) ›
🗺️ [T13 Maps and geodata](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: Maps and geodata menu](README.md) ›
🗂️ S-T13-L03 Map layers

# 🗂️ S-T13-L03 Map layers

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | only their own records, through the portal or the AI assistant | an admin list (D494): settings and technical records |
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | the records their roles' record rules allow (T2) | an admin list (D494): settings and technical records |
| [U25 Care coordinator](../../../../01-users/personas/u25-care-coordinator.md) | the records their roles' record rules allow (T2) | an admin list (D494): settings and technical records |
| [U29 Dispatcher](../../../../01-users/personas/u29-dispatcher.md) | the records their roles' record rules allow (T2) | an admin list (D494): settings and technical records |

## Purpose

The aggregated list of every [E-T13-03 Map layer](../../data/e-t13-03-map-layer.md) the user may see: to find, filter,
total and act on many map layers at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Administration › Map layers, in the Administration menu (D494).
- **Workspaces:** 4 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "map layers" offers this view.
- **AI assistant:** "show the map layers that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Map layers    Administration › Map layers   [+ New]                                                          |
| [count] [Draft]   [chart: count by state]                                                                    |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] NAME   STATUS   RECORD TYPE   DOMAIN   KIND   SHOWN BY DEFAULT                       |
| kind              | [ ] ...                                                  Open >                          |
| record type       | [ ] ...                                                  Open >                          |
| shown by default  | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Name | name | label | yes |
| Status | status | badge | yes |
| Record type | record type | text | yes |
| Domain | domain | text | yes |
| Kind | kind | text | yes |
| Shown by default | shown by default | yes or no | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Draft, Published, Retired | the visible rows (D488) |
| Kind | each value | the visible rows (D488) |
| Record type | each value | the visible rows (D488) |
| Shown by default | each value | the visible rows (D488) |
| Domain | each value | the visible rows (D488) |
| Status | Draft, Published, Retired | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Map layers of a chosen domain, or of the domains that match a filter.
- From the other side: the domains that have map layers, or none.
- Map layers of a chosen record type, or of the record types that match a filter.
- From the other side: the record types that have map layers, or none.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Draft.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Open: Draft, Published.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New map layer | header | U07 and the administration roles | the record's own page (Row opens) |
| Change status | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- kind: editable in its cell unless the record's state locks it.
- shown by default: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to
[S-F16-11 My requests](../../../../02-functional/f16-customer-support-agents/screens/05-customer-side/s-f16-11-my-requests.md).

The records also show on:
[S-F16-14 Work requests](../../../../02-functional/f16-customer-support-agents/screens/06-take-in-every-request/s-f16-14-work-requests.md),
[S-F16-15 Arrival of your visit](../../../../02-functional/f16-customer-support-agents/screens/06-take-in-every-request/s-f16-15-arrival-of-your-visit.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 map layers of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no map layer the user may see yet, with the create action when allowed.
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
| Listed, U09, view Open: Draft, Published | desktop | ![Listed, U09, view Open: Draft, Published, light](../../images/lists/s-t13-l03-map-layers-u09-customer-desktop-light.png) | ![Listed, U09, view Open: Draft, Published, dark](../../images/lists/s-t13-l03-map-layers-u09-customer-desktop-dark.png) |
| Listed, U09, view Open: Draft, Published | phone | ![Listed, U09, view Open: Draft, Published, light](../../images/lists/s-t13-l03-map-layers-u09-customer-phone-light.png) | ![Listed, U09, view Open: Draft, Published, dark](../../images/lists/s-t13-l03-map-layers-u09-customer-phone-dark.png) |
| Listed, U02, view Needs attention | desktop | ![Listed, U02, view Needs attention, light](../../images/lists/s-t13-l03-map-layers-u02-manager-desktop-light.png) | ![Listed, U02, view Needs attention, dark](../../images/lists/s-t13-l03-map-layers-u02-manager-desktop-dark.png) |
| Listed, U02, view Needs attention | phone | ![Listed, U02, view Needs attention, light](../../images/lists/s-t13-l03-map-layers-u02-manager-phone-light.png) | ![Listed, U02, view Needs attention, dark](../../images/lists/s-t13-l03-map-layers-u02-manager-phone-dark.png) |
| Listed, U25, view Needs attention | desktop | ![Listed, U25, view Needs attention, light](../../images/lists/s-t13-l03-map-layers-u25-care-coordinator-desktop-light.png) | ![Listed, U25, view Needs attention, dark](../../images/lists/s-t13-l03-map-layers-u25-care-coordinator-desktop-dark.png) |
| Listed, U25, view Needs attention | phone | ![Listed, U25, view Needs attention, light](../../images/lists/s-t13-l03-map-layers-u25-care-coordinator-phone-light.png) | ![Listed, U25, view Needs attention, dark](../../images/lists/s-t13-l03-map-layers-u25-care-coordinator-phone-dark.png) |
| Listed, U29, view Needs attention | desktop | ![Listed, U29, view Needs attention, light](../../images/lists/s-t13-l03-map-layers-u29-dispatcher-desktop-light.png) | ![Listed, U29, view Needs attention, dark](../../images/lists/s-t13-l03-map-layers-u29-dispatcher-desktop-dark.png) |
| Listed, U29, view Needs attention | phone | ![Listed, U29, view Needs attention, light](../../images/lists/s-t13-l03-map-layers-u29-dispatcher-phone-light.png) | ![Listed, U29, view Needs attention, dark](../../images/lists/s-t13-l03-map-layers-u29-dispatcher-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Administration › Map layers](README.md) |
| Workspaces | [U09](../../../../04-ux/views/u09-customer/workspace.md), [U02](../../../../04-ux/views/u02-manager/workspace.md), [U25](../../../../04-ux/views/u25-care-coordinator/workspace.md), [U29](../../../../04-ux/views/u29-dispatcher/workspace.md) |
| Flows | [FL-F16-06](../../../../02-functional/f16-customer-support-agents/flows/fl-f16-06-take-in-every-request.md), [FL-F9-12](../../../../02-functional/f09-hr-and-projects/flows/fl-f09-12-schedule-customer-requests.md) |

## Open questions

None.

---

⬅️ [S-T13-L02 Routes](s-t13-l02-routes.md) · ⬆️ [Up](README.md) ·
➡️ [S-T13-L04 Geodata sources](s-t13-l04-geodata-sources.md)
