🏠 [Specs](../../../../README.md) › ⚙️ [Technical capabilities](../../../README.md) ›
🗺️ [T13 Maps and geodata](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: Maps and geodata menu](README.md) ›
🗂️ S-T13-L01 Geocoded places

# 🗂️ S-T13-L01 Geocoded places

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U29 Dispatcher](../../../../01-users/personas/u29-dispatcher.md) | the records their roles' record rules allow (T2) | an admin list (D494): settings and technical records |
| [U25 Care coordinator](../../../../01-users/personas/u25-care-coordinator.md) | the records their roles' record rules allow (T2) | an admin list (D494): settings and technical records |
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | the records their roles' record rules allow (T2) | an admin list (D494): settings and technical records |
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | only their own records, through the portal or the AI assistant | an admin list (D494): settings and technical records |
| [U16 Office worker](../../../../01-users/personas/u16-office-worker.md) | the records their roles' record rules allow (T2) | an admin list (D494): settings and technical records |

## Purpose

The aggregated list of every [E-T13-01 Geocoded place](../../data/e-t13-01-geocoded-place.md) the user may see: to find,
filter, total and act on many geocoded places at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Administration › Geocoded places, in the Administration menu (D494).
- **Workspaces:** 5 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "geocoded places" offers this view.
- **AI assistant:** "show the geocoded places that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Geocoded places    Administration › Geocoded places   [+ New]                                                |
| [count] [new this month]   [chart: count by state]                                                           |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] RECORD   STATE   GEOCODED AT   CONFIDENCE                                            |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Record | record | text | yes |
| State | state | badge: ToGeocode, Geocoded, NotFound | yes |
| Geocoded at | geocoded at | date and time | yes |
| Confidence | confidence | number, right-aligned | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | ToGeocode, Geocoded, NotFound | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: geocoded places link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- New this month, by geocoded at.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New geocoded place | header | U07 and the administration roles | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- confidence: editable in its cell unless the record's state locks it.
- geocoded at: editable in its cell unless the record's state locks it.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| address | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| normalised address | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| shape | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| position | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to
[S-F16-11 My requests](../../../../02-functional/f16-customer-support-agents/screens/05-customer-side/s-f16-11-my-requests.md).

The records also show on:
[S-F16-14 Work requests](../../../../02-functional/f16-customer-support-agents/screens/06-take-in-every-request/s-f16-14-work-requests.md),
[S-F9-33 Planning map](../../../../02-functional/f09-hr-and-projects/screens/12-schedule-customer-requests/s-f09-33-planning-map.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 geocoded places of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no geocoded place the user may see yet, with the create action when allowed.
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
| Listed, U29, view All | desktop | ![Listed, U29, view All, light](../../images/lists/s-t13-l01-geocoded-places-u29-dispatcher-desktop-light.png) | ![Listed, U29, view All, dark](../../images/lists/s-t13-l01-geocoded-places-u29-dispatcher-desktop-dark.png) |
| Listed, U29, view All | phone | ![Listed, U29, view All, light](../../images/lists/s-t13-l01-geocoded-places-u29-dispatcher-phone-light.png) | ![Listed, U29, view All, dark](../../images/lists/s-t13-l01-geocoded-places-u29-dispatcher-phone-dark.png) |
| Listed, U25, view All | desktop | ![Listed, U25, view All, light](../../images/lists/s-t13-l01-geocoded-places-u25-care-coordinator-desktop-light.png) | ![Listed, U25, view All, dark](../../images/lists/s-t13-l01-geocoded-places-u25-care-coordinator-desktop-dark.png) |
| Listed, U25, view All | phone | ![Listed, U25, view All, light](../../images/lists/s-t13-l01-geocoded-places-u25-care-coordinator-phone-light.png) | ![Listed, U25, view All, dark](../../images/lists/s-t13-l01-geocoded-places-u25-care-coordinator-phone-dark.png) |
| Listed, U02, view All | desktop | ![Listed, U02, view All, light](../../images/lists/s-t13-l01-geocoded-places-u02-manager-desktop-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-t13-l01-geocoded-places-u02-manager-desktop-dark.png) |
| Listed, U02, view All | phone | ![Listed, U02, view All, light](../../images/lists/s-t13-l01-geocoded-places-u02-manager-phone-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-t13-l01-geocoded-places-u02-manager-phone-dark.png) |
| Listed, U09, view All | desktop | ![Listed, U09, view All, light](../../images/lists/s-t13-l01-geocoded-places-u09-customer-desktop-light.png) | ![Listed, U09, view All, dark](../../images/lists/s-t13-l01-geocoded-places-u09-customer-desktop-dark.png) |
| Listed, U09, view All | phone | ![Listed, U09, view All, light](../../images/lists/s-t13-l01-geocoded-places-u09-customer-phone-light.png) | ![Listed, U09, view All, dark](../../images/lists/s-t13-l01-geocoded-places-u09-customer-phone-dark.png) |
| Listed, U16, view All | desktop | ![Listed, U16, view All, light](../../images/lists/s-t13-l01-geocoded-places-u16-office-worker-desktop-light.png) | ![Listed, U16, view All, dark](../../images/lists/s-t13-l01-geocoded-places-u16-office-worker-desktop-dark.png) |
| Listed, U16, view All | phone | ![Listed, U16, view All, light](../../images/lists/s-t13-l01-geocoded-places-u16-office-worker-phone-light.png) | ![Listed, U16, view All, dark](../../images/lists/s-t13-l01-geocoded-places-u16-office-worker-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Administration › Geocoded places](README.md) |
| Workspaces | [U29](../../../../04-ux/views/u29-dispatcher/workspace.md), [U25](../../../../04-ux/views/u25-care-coordinator/workspace.md), [U02](../../../../04-ux/views/u02-manager/workspace.md), [U09](../../../../04-ux/views/u09-customer/workspace.md), [U16](../../../../04-ux/views/u16-office-worker/workspace.md) |
| Flows | [FL-F16-06](../../../../02-functional/f16-customer-support-agents/flows/fl-f16-06-take-in-every-request.md), [FL-F9-12](../../../../02-functional/f09-hr-and-projects/flows/fl-f09-12-schedule-customer-requests.md) |

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [S-T13-L02 Routes](s-t13-l02-routes.md)
