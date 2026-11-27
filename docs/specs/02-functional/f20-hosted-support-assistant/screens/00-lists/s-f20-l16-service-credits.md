🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛟 [F20 Hosted support assistant (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Hosted support assistant (hosted edition) menu](README.md) › 🗂️ S-F20-L16 Service credits

# 🗂️ S-F20-L16 Service credits

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U07: their use cases only read these records, inside a screen of the use case, so they open them
from there (D493).

## Purpose

The aggregated list of every [E-F20-16 Service credit](../../data/e-f20-16-service-credit.md) the user may see: to find,
filter, total and act on many service credits at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Hosted support assistant (hosted edition) › Service credits, in the capability's menu (D495).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "service credits" offers this view.
- **AI assistant:** "show the service credits that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Service credits    Hosted support assistant (hosted edition) › Service credits   [+ New]                     |
| [count] [total amount] [Disputed] [new this month]   [chart: count by state, amount stacked]                 |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] COMPANY   STATE   CREDIT NOTE   AMOUNT   MONTH   TARGETS MISSED                      |
| company           | [ ] ...                                                  Open >                          |
| targets missed    | [ ] ...                                                  Open >                          |
| credit note       | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Company | company | link to the record | yes |
| State | state | badge: Computed, Issued, Disputed | yes |
| Credit note | credit note | link to the record | yes |
| Amount | amount | amount, right-aligned | yes |
| Month | month | text | yes |
| Targets missed | targets missed | text | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Computed, Issued, Disputed | the visible rows (D488) |
| Company | each linked company | the visible rows (D488) |
| Targets missed | each value | the visible rows (D488) |
| Credit note | each linked credit note | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Service credits of a chosen company, or of the companies that match a filter.
- From the other side: the companies that have service credits, or none.
- Service credits of a chosen credit note, or of the credit notes that match a filter.
- From the other side: the credit notes that have service credits, or none.

## KPI strip

- Count of the visible rows.
- Total of amount.
- Needs attention: count in the state Disputed.
- New this month, by month.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state, amount stacked (VR-8); the Chart button turns the filtered list into a chart the user can pin to their
home screen (C-09).

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
| New service credit | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- month: editable in its cell unless the record's state locks it.
- targets missed: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F20-24 Service credits](../06-after-an-incident/s-f20-24-service-credits.md).

The records also show on: [S-F20-19 Support plans](../04-govern-the-assistant/s-f20-19-support-plans.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 service credits of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no service credit the user may see yet, with the create action when allowed.
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
| Listed, U13, view Needs attention | desktop | ![Listed, U13, view Needs attention, light](../../images/lists/s-f20-l16-service-credits-u13-owner-desktop-light.png) | ![Listed, U13, view Needs attention, dark](../../images/lists/s-f20-l16-service-credits-u13-owner-desktop-dark.png) |
| Listed, U13, view Needs attention | phone | ![Listed, U13, view Needs attention, light](../../images/lists/s-f20-l16-service-credits-u13-owner-phone-light.png) | ![Listed, U13, view Needs attention, dark](../../images/lists/s-f20-l16-service-credits-u13-owner-phone-dark.png) |
| Listed, U05, view All | desktop | ![Listed, U05, view All, light](../../images/lists/s-f20-l16-service-credits-u05-accounting-desktop-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-f20-l16-service-credits-u05-accounting-desktop-dark.png) |
| Listed, U05, view All | phone | ![Listed, U05, view All, light](../../images/lists/s-f20-l16-service-credits-u05-accounting-phone-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-f20-l16-service-credits-u05-accounting-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Hosted support assistant (hosted edition) › Service credits](README.md) |
| Workspaces | [U13](../../../../04-ux/views/u13-owner/workspace.md), [U05](../../../../04-ux/views/u05-accounting/workspace.md) |
| Flows | [FL-F20-04](../../flows/fl-f20-04-govern-the-assistant.md), [FL-F20-06](../../flows/fl-f20-06-after-an-incident.md) |

## Open questions

None.

---

⬅️ [S-F20-L15 Incident reports](s-f20-l15-incident-reports.md) · ⬆️ [Up](README.md) ·
➡️ [S-F20-L17 NIS2 fact sheets](s-f20-l17-nis2-fact-sheets.md)
