🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔌 [F24 Integrations hub](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: Integrations hub menu](README.md) ›
🗂️ S-F24-L13 Webhook subscriptions

# 🗂️ S-F24-L13 Webhook subscriptions

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F24-13 Webhook subscription](../../data/e-f24-13-webhook-subscription.md) the user may
see: to find, filter, total and act on many webhook subscriptions at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Integrations hub › Webhook subscriptions, in the capability's menu (D495).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "webhook subscriptions" offers this view.
- **AI assistant:** "show the webhook subscriptions that need attention" opens it with the filter as editable chips
  (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Webhook subscriptions    Integrations hub › Webhook subscriptions   [+ New]                                  |
| [count]   [chart: count by state]                                                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| connection        | [ ] CONNECTION   STATE   EVENTS   FAILURES                                               |
| events            | [ ] ...                                                  Open >                          |
| state             | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Connection | connection | link to the record | yes |
| State | state | badge: Active, Paused, Deleted | yes |
| Events | events | text | yes |
| Failures | failures | number, right-aligned | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| Connection | each linked connection | the visible rows (D488) |
| Events | each value | the visible rows (D488) |
| State | Active, Paused, Deleted | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Webhook subscriptions of a chosen connection, or of the connections that match a filter.
- From the other side: the connections that have webhook subscriptions, or none.

## KPI strip

- Count of the visible rows.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Open: Active, Paused.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New webhook subscription | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- events: editable in its cell unless the record's state locks it.
- failures: editable in its cell unless the record's state locks it.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| secret | secret | nobody | everyone (VR-4) |

## Row opens

Open › goes to [S-F24-20 Rights and costs](../04-run-and-control/s-f24-20-rights-and-costs.md).

The records also show on: [S-F24-21 Automation](../06-business-tools/s-f24-21-automation.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 webhook subscriptions of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no webhook subscription the user may see yet, with the create action when allowed.
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
| Listed, U07, view Open: Active, Paused | desktop | ![Listed, U07, view Open: Active, Paused, light](../../images/lists/s-f24-l13-webhook-subscriptions-u07-administrator-desktop-light.png) | ![Listed, U07, view Open: Active, Paused, dark](../../images/lists/s-f24-l13-webhook-subscriptions-u07-administrator-desktop-dark.png) |
| Listed, U07, view Open: Active, Paused | phone | ![Listed, U07, view Open: Active, Paused, light](../../images/lists/s-f24-l13-webhook-subscriptions-u07-administrator-phone-light.png) | ![Listed, U07, view Open: Active, Paused, dark](../../images/lists/s-f24-l13-webhook-subscriptions-u07-administrator-phone-dark.png) |
| Listed, U13, view Open: Active, Paused | desktop | ![Listed, U13, view Open: Active, Paused, light](../../images/lists/s-f24-l13-webhook-subscriptions-u13-owner-desktop-light.png) | ![Listed, U13, view Open: Active, Paused, dark](../../images/lists/s-f24-l13-webhook-subscriptions-u13-owner-desktop-dark.png) |
| Listed, U13, view Open: Active, Paused | phone | ![Listed, U13, view Open: Active, Paused, light](../../images/lists/s-f24-l13-webhook-subscriptions-u13-owner-phone-light.png) | ![Listed, U13, view Open: Active, Paused, dark](../../images/lists/s-f24-l13-webhook-subscriptions-u13-owner-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Integrations hub › Webhook subscriptions](README.md) |
| Workspaces | [U07](../../../../04-ux/views/u07-administrator/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md) |
| Flows | [FL-F24-04](../../flows/fl-f24-04-run-and-control.md), [FL-F24-06](../../flows/fl-f24-06-business-tools.md) |

## Open questions

None.

---

⬅️ [S-F24-L12 Integration icons](s-f24-l12-integration-icons.md) · ⬆️ [Up](README.md) ·
➡️ [S-F24-L14 E-invoicing registrations](s-f24-l14-e-invoicing-registrations.md)
