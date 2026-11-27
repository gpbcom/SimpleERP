🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💼 [SC03 Services](../../README.md) ›
🖥️ [Screens](../README.md) › 🗂️ [Views: Services menu](README.md) › 🗂️ S-SC03-L13 Satisfaction surveys

# 🗂️ S-SC03-L13 Satisfaction surveys

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U24 Engagement manager](../../../../01-users/personas/u24-engagement-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-SC03-13 Satisfaction survey](../../data/e-sc03-13-satisfaction-survey.md) the user may
see: to find, filter, total and act on many satisfaction surveys at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Services › Satisfaction surveys, in the capability's menu (D495).
- **Workspaces:** 3 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "satisfaction surveys" offers this view.
- **AI assistant:** "show the satisfaction surveys that need attention" opens it with the filter as editable chips
  (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Satisfaction surveys    Services › Satisfaction surveys   [+ New]                                            |
| [count]   [chart: count by state]                                                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] ENGAGEMENT   STATE                                                                   |
| engagement        | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Engagement | engagement | link to the record | yes |
| State | state | badge: Sent, Closed | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Sent, Closed | the visible rows (D488) |
| Engagement | each linked engagement | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Satisfaction surveys of a chosen engagement, or of the engagements that match a filter.
- From the other side: the engagements that have satisfaction surveys, or none.

## KPI strip

- Count of the visible rows.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Open: Sent.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New satisfaction survey | header | the personas whose roles may create it | the record's own page (Row opens) |
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

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-SC03-12 Satisfaction](../05-client-and-people/s-sc03-12-satisfaction.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 satisfaction surveys of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no satisfaction survey the user may see yet, with the create action when allowed.
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
| Listed, U24, view Open: Sent | desktop | ![Listed, U24, view Open: Sent, light](../../images/lists/s-sc03-l13-satisfaction-surveys-u24-engagement-manager-desktop-light.png) | ![Listed, U24, view Open: Sent, dark](../../images/lists/s-sc03-l13-satisfaction-surveys-u24-engagement-manager-desktop-dark.png) |
| Listed, U24, view Open: Sent | phone | ![Listed, U24, view Open: Sent, light](../../images/lists/s-sc03-l13-satisfaction-surveys-u24-engagement-manager-phone-light.png) | ![Listed, U24, view Open: Sent, dark](../../images/lists/s-sc03-l13-satisfaction-surveys-u24-engagement-manager-phone-dark.png) |
| Listed, U13, view Open: Sent | desktop | ![Listed, U13, view Open: Sent, light](../../images/lists/s-sc03-l13-satisfaction-surveys-u13-owner-desktop-light.png) | ![Listed, U13, view Open: Sent, dark](../../images/lists/s-sc03-l13-satisfaction-surveys-u13-owner-desktop-dark.png) |
| Listed, U13, view Open: Sent | phone | ![Listed, U13, view Open: Sent, light](../../images/lists/s-sc03-l13-satisfaction-surveys-u13-owner-phone-light.png) | ![Listed, U13, view Open: Sent, dark](../../images/lists/s-sc03-l13-satisfaction-surveys-u13-owner-phone-dark.png) |
| Listed, U09, view Open: Sent | desktop | ![Listed, U09, view Open: Sent, light](../../images/lists/s-sc03-l13-satisfaction-surveys-u09-customer-desktop-light.png) | ![Listed, U09, view Open: Sent, dark](../../images/lists/s-sc03-l13-satisfaction-surveys-u09-customer-desktop-dark.png) |
| Listed, U09, view Open: Sent | phone | ![Listed, U09, view Open: Sent, light](../../images/lists/s-sc03-l13-satisfaction-surveys-u09-customer-phone-light.png) | ![Listed, U09, view Open: Sent, dark](../../images/lists/s-sc03-l13-satisfaction-surveys-u09-customer-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Services › Satisfaction surveys](README.md) |
| Workspaces | [U24](../../../../04-ux/views/u24-engagement-manager/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md), [U09](../../../../04-ux/views/u09-customer/workspace.md) |
| Flows | [FL-F16-05](../../../../02-functional/f16-customer-support-agents/flows/fl-f16-05-customer-side.md), [FL-SC03-05](../../flows/fl-sc03-05-client-and-people.md), [FL-SC04-05](../../../sc04-home-care/flows/fl-sc04-05-people-and-quality.md) |

## Open questions

None.

---

⬅️ [S-SC03-L12 Shared items](s-sc03-l12-shared-items.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC03-L14 Pricing models](s-sc03-l14-pricing-models.md)
