🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🎧 [F16 Customer support agents](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Customer support agents menu](README.md) › 🗂️ S-F16-L08 Satisfaction ratings

# 🗂️ S-F16-L08 Satisfaction ratings

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |
| [U16 Office worker](../../../../01-users/personas/u16-office-worker.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F16-08 Satisfaction rating](../../data/e-f16-08-satisfaction-rating.md) the user may
see: to find, filter, total and act on many satisfaction ratings at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Customer support agents › Satisfaction ratings, in the capability's menu (D495).
- **Workspaces:** 4 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "satisfaction ratings" offers this view.
- **AI assistant:** "show the satisfaction ratings that need attention" opens it with the filter as editable chips
  (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Satisfaction ratings    Customer support agents › Satisfaction ratings   [+ New]                             |
| [count] [Expired]   [chart: count by state]                                                                  |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] REQUEST   STATE   HANDLED BY   SCORE                                                 |
| request           | [ ] ...                                                  Open >                          |
| handled by        | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Request | request | link to the record | yes |
| State | state | badge: Asked, Answered, Expired | yes |
| Handled by | handled by | text | yes |
| Score | score | number, right-aligned | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Asked, Answered, Expired | the visible rows (D488) |
| Request | each linked request | the visible rows (D488) |
| Handled by | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Satisfaction ratings of a chosen request, or of the requests that match a filter.
- From the other side: the requests that have satisfaction ratings, or none.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Expired.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Open: Asked, Answered.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New satisfaction rating | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- score: editable in its cell unless the record's state locks it.
- handled by: editable in its cell unless the record's state locks it.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| comment | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F16-01 Request inbox](../01-resolve-a-request/s-f16-01-request-inbox.md).

The records also show on: [S-F16-04 Review queue](../03-review-and-monitor/s-f16-04-review-queue.md),
[S-F16-05 Support dashboard](../03-review-and-monitor/s-f16-05-support-dashboard.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 satisfaction ratings of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no satisfaction rating the user may see yet, with the create action when allowed.
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
| Listed, U02, view Needs attention | desktop | ![Listed, U02, view Needs attention, light](../../images/lists/s-f16-l08-satisfaction-ratings-u02-manager-desktop-light.png) | ![Listed, U02, view Needs attention, dark](../../images/lists/s-f16-l08-satisfaction-ratings-u02-manager-desktop-dark.png) |
| Listed, U02, view Needs attention | phone | ![Listed, U02, view Needs attention, light](../../images/lists/s-f16-l08-satisfaction-ratings-u02-manager-phone-light.png) | ![Listed, U02, view Needs attention, dark](../../images/lists/s-f16-l08-satisfaction-ratings-u02-manager-phone-dark.png) |
| Listed, U09, view Open: Asked, Answered | desktop | ![Listed, U09, view Open: Asked, Answered, light](../../images/lists/s-f16-l08-satisfaction-ratings-u09-customer-desktop-light.png) | ![Listed, U09, view Open: Asked, Answered, dark](../../images/lists/s-f16-l08-satisfaction-ratings-u09-customer-desktop-dark.png) |
| Listed, U09, view Open: Asked, Answered | phone | ![Listed, U09, view Open: Asked, Answered, light](../../images/lists/s-f16-l08-satisfaction-ratings-u09-customer-phone-light.png) | ![Listed, U09, view Open: Asked, Answered, dark](../../images/lists/s-f16-l08-satisfaction-ratings-u09-customer-phone-dark.png) |
| Listed, U16, view Open: Asked, Answered | desktop | ![Listed, U16, view Open: Asked, Answered, light](../../images/lists/s-f16-l08-satisfaction-ratings-u16-office-worker-desktop-light.png) | ![Listed, U16, view Open: Asked, Answered, dark](../../images/lists/s-f16-l08-satisfaction-ratings-u16-office-worker-desktop-dark.png) |
| Listed, U16, view Open: Asked, Answered | phone | ![Listed, U16, view Open: Asked, Answered, light](../../images/lists/s-f16-l08-satisfaction-ratings-u16-office-worker-phone-light.png) | ![Listed, U16, view Open: Asked, Answered, dark](../../images/lists/s-f16-l08-satisfaction-ratings-u16-office-worker-phone-dark.png) |
| Listed, U13, view Needs attention | desktop | ![Listed, U13, view Needs attention, light](../../images/lists/s-f16-l08-satisfaction-ratings-u13-owner-desktop-light.png) | ![Listed, U13, view Needs attention, dark](../../images/lists/s-f16-l08-satisfaction-ratings-u13-owner-desktop-dark.png) |
| Listed, U13, view Needs attention | phone | ![Listed, U13, view Needs attention, light](../../images/lists/s-f16-l08-satisfaction-ratings-u13-owner-phone-light.png) | ![Listed, U13, view Needs attention, dark](../../images/lists/s-f16-l08-satisfaction-ratings-u13-owner-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Customer support agents › Satisfaction ratings](README.md) |
| Workspaces | [U02](../../../../04-ux/views/u02-manager/workspace.md), [U09](../../../../04-ux/views/u09-customer/workspace.md), [U16](../../../../04-ux/views/u16-office-worker/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md) |
| Flows | [FL-F16-01](../../flows/fl-f16-01-resolve-a-request.md), [FL-F16-03](../../flows/fl-f16-03-review-and-monitor.md), [FL-F16-04](../../flows/fl-f16-04-human-agent-workspace.md), [FL-F16-05](../../flows/fl-f16-05-customer-side.md) |

## Open questions

None.

---

⬅️ [S-F16-L07 Macros](s-f16-l07-macros.md) · ⬆️ [Up](README.md) ·
➡️ [S-F16-L09 Help-centre articles](s-f16-l09-help-centre-articles.md)
