🏠 [Specs](../../../../README.md) › ⚙️ [Technical capabilities](../../../README.md) ›
🗺️ [T13 Maps and geodata](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: Maps and geodata menu](README.md) ›
🗂️ S-T13-L02 Routes

# 🗂️ S-T13-L02 Routes

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U25 Care coordinator](../../../../01-users/personas/u25-care-coordinator.md) | the records their roles' record rules allow (T2) | an admin list (D494): settings and technical records |
| [U29 Dispatcher](../../../../01-users/personas/u29-dispatcher.md) | the records their roles' record rules allow (T2) | an admin list (D494): settings and technical records |
| [U26 Carer](../../../../01-users/personas/u26-carer.md) | the records their roles' record rules allow (T2) | an admin list (D494): settings and technical records |
| [U30 Driver](../../../../01-users/personas/u30-driver.md) | the records their roles' record rules allow (T2) | an admin list (D494): settings and technical records |
| [U42 Sales representative](../../../../01-users/personas/u42-sales-representative.md) | the records their roles' record rules allow (T2) | an admin list (D494): settings and technical records |
| [U14 Field worker](../../../../01-users/personas/u14-field-worker.md) | the records their roles' record rules allow (T2) | an admin list (D494): settings and technical records |
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | the records their roles' record rules allow (T2) | an admin list (D494): settings and technical records |

## Purpose

The aggregated list of every [E-T13-02 Route](../../data/e-t13-02-route.md) the user may see: to find, filter, total and
act on many routes at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Administration › Routes, in the Administration menu (D494).
- **Workspaces:** 7 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "routes" offers this view.
- **AI assistant:** "show the routes that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Routes    Administration › Routes   [+ New]                                                                  |
| [count] [new this month]   [chart: count by state]                                                           |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] FOR   STATE   LEGS   COMPUTED AT                                                     |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| For | for | label | yes |
| State | state | badge: Computed, Outdated | yes |
| Legs | legs | date and time | yes |
| Computed at | computed at | date and time | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Computed, Outdated | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: routes link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- New this month, by legs.

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
| New route | header | U07 and the administration roles | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- legs: editable in its cell unless the record's state locks it.
- computed at: editable in its cell unless the record's state locks it.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| stops | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| line | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to
[S-F16-14 Work requests](../../../../02-functional/f16-customer-support-agents/screens/06-take-in-every-request/s-f16-14-work-requests.md).

The records also show on:
[S-F9-18 Field service](../../../../02-functional/f09-hr-and-projects/screens/06-plan-and-deliver-work/s-f09-18-field-service.md),
[S-F9-27 Rounds](../../../../02-functional/f09-hr-and-projects/screens/11-capacity-rounds-and-partners/s-f09-27-rounds.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 routes of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no route the user may see yet, with the create action when allowed.
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
| Listed, U25, view All | desktop | ![Listed, U25, view All, light](../../images/lists/s-t13-l02-routes-u25-care-coordinator-desktop-light.png) | ![Listed, U25, view All, dark](../../images/lists/s-t13-l02-routes-u25-care-coordinator-desktop-dark.png) |
| Listed, U25, view All | phone | ![Listed, U25, view All, light](../../images/lists/s-t13-l02-routes-u25-care-coordinator-phone-light.png) | ![Listed, U25, view All, dark](../../images/lists/s-t13-l02-routes-u25-care-coordinator-phone-dark.png) |
| Listed, U29, view All | desktop | ![Listed, U29, view All, light](../../images/lists/s-t13-l02-routes-u29-dispatcher-desktop-light.png) | ![Listed, U29, view All, dark](../../images/lists/s-t13-l02-routes-u29-dispatcher-desktop-dark.png) |
| Listed, U29, view All | phone | ![Listed, U29, view All, light](../../images/lists/s-t13-l02-routes-u29-dispatcher-phone-light.png) | ![Listed, U29, view All, dark](../../images/lists/s-t13-l02-routes-u29-dispatcher-phone-dark.png) |
| Listed, U26, view All | desktop | ![Listed, U26, view All, light](../../images/lists/s-t13-l02-routes-u26-carer-desktop-light.png) | ![Listed, U26, view All, dark](../../images/lists/s-t13-l02-routes-u26-carer-desktop-dark.png) |
| Listed, U26, view All | phone | ![Listed, U26, view All, light](../../images/lists/s-t13-l02-routes-u26-carer-phone-light.png) | ![Listed, U26, view All, dark](../../images/lists/s-t13-l02-routes-u26-carer-phone-dark.png) |
| Listed, U30, view All | desktop | ![Listed, U30, view All, light](../../images/lists/s-t13-l02-routes-u30-driver-desktop-light.png) | ![Listed, U30, view All, dark](../../images/lists/s-t13-l02-routes-u30-driver-desktop-dark.png) |
| Listed, U30, view All | phone | ![Listed, U30, view All, light](../../images/lists/s-t13-l02-routes-u30-driver-phone-light.png) | ![Listed, U30, view All, dark](../../images/lists/s-t13-l02-routes-u30-driver-phone-dark.png) |
| Listed, U42, view All | desktop | ![Listed, U42, view All, light](../../images/lists/s-t13-l02-routes-u42-sales-representative-desktop-light.png) | ![Listed, U42, view All, dark](../../images/lists/s-t13-l02-routes-u42-sales-representative-desktop-dark.png) |
| Listed, U42, view All | phone | ![Listed, U42, view All, light](../../images/lists/s-t13-l02-routes-u42-sales-representative-phone-light.png) | ![Listed, U42, view All, dark](../../images/lists/s-t13-l02-routes-u42-sales-representative-phone-dark.png) |
| Listed, U14, view All | desktop | ![Listed, U14, view All, light](../../images/lists/s-t13-l02-routes-u14-field-worker-desktop-light.png) | ![Listed, U14, view All, dark](../../images/lists/s-t13-l02-routes-u14-field-worker-desktop-dark.png) |
| Listed, U14, view All | phone | ![Listed, U14, view All, light](../../images/lists/s-t13-l02-routes-u14-field-worker-phone-light.png) | ![Listed, U14, view All, dark](../../images/lists/s-t13-l02-routes-u14-field-worker-phone-dark.png) |
| Listed, U02, view All | desktop | ![Listed, U02, view All, light](../../images/lists/s-t13-l02-routes-u02-manager-desktop-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-t13-l02-routes-u02-manager-desktop-dark.png) |
| Listed, U02, view All | phone | ![Listed, U02, view All, light](../../images/lists/s-t13-l02-routes-u02-manager-phone-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-t13-l02-routes-u02-manager-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Administration › Routes](README.md) |
| Workspaces | [U25](../../../../04-ux/views/u25-care-coordinator/workspace.md), [U29](../../../../04-ux/views/u29-dispatcher/workspace.md), [U26](../../../../04-ux/views/u26-carer/workspace.md), [U30](../../../../04-ux/views/u30-driver/workspace.md), [U42](../../../../04-ux/views/u42-sales-representative/workspace.md), [U14](../../../../04-ux/views/u14-field-worker/workspace.md), [U02](../../../../04-ux/views/u02-manager/workspace.md) |
| Flows | [FL-F2-12](../../../../02-functional/f02-no-code-configuration/flows/fl-f02-12-set-up-request-types.md), [FL-F9-11](../../../../02-functional/f09-hr-and-projects/flows/fl-f09-11-capacity-rounds-and-partners.md), [FL-F9-12](../../../../02-functional/f09-hr-and-projects/flows/fl-f09-12-schedule-customer-requests.md) |

## Open questions

None.

---

⬅️ [S-T13-L01 Geocoded places](s-t13-l01-geocoded-places.md) · ⬆️ [Up](README.md) ·
➡️ [S-T13-L03 Map layers](s-t13-l03-map-layers.md)
