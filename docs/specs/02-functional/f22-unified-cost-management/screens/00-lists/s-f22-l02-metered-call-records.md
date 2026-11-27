🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💸 [F22 Unified platform cost management](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Unified platform cost management menu](README.md) › 🗂️ S-F22-L02 Metered call records

# 🗂️ S-F22-L02 Metered call records

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U48 Hosting engineer](../../../../01-users/personas/u48-hosting-engineer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F22-02 Metered call record](../../data/e-f22-02-metered-call-record.md) the user may
see: to find, filter, total and act on many metered call records at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Unified platform cost management › Metered call records, in the capability's menu (D495).
- **Workspaces:** 5 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "metered call records" offers this view.
- **AI assistant:** "show the metered call records that need attention" opens it with the filter as editable chips
  (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Metered call records    Unified platform cost management › Metered call records   [+ New]                    |
| [count] [total cost] [new this month]   [chart: count by state, cost stacked]                                |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] COMPANY   STATE   USER   MODULE   COST   AT                                          |
| company           | [ ] ...                                                  Open >                          |
| user              | [ ] ...                                                  Open >                          |
| module            | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Company | company | link to the record | yes |
| State | state | badge: Recorded | yes |
| User | user | link to the record | yes |
| Module | module | link to the record | yes |
| Cost | cost | amount, right-aligned | yes |
| At | at | link to the record | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Recorded | the visible rows (D488) |
| Company | each linked company | the visible rows (D488) |
| User | each linked user | the visible rows (D488) |
| Module | each linked module | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Metered call records of a chosen company, or of the companies that match a filter.
- From the other side: the companies that have metered call records, or none.
- Metered call records of a chosen module, or of the modules that match a filter.
- From the other side: the modules that have metered call records, or none.

## KPI strip

- Count of the visible rows.
- Total of cost.
- New this month, by at.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state, cost stacked (VR-8); the Chart button turns the filtered list into a chart the user can pin to their
home screen (C-09).

## Saved views

- All.
- Mine: user.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New metered call record | header | the personas whose roles may create it | the record's own page (Row opens) |
| Assign | bulk bar | the personas whose roles may assign | sets the user; audited |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- user: editable in its cell unless the record's state locks it.
- at: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F22-01 Costs overview](../01-see-and-set-up/s-f22-01-costs-overview.md).

The records also show on: [S-F22-02 Cost breakdown](../01-see-and-set-up/s-f22-02-cost-breakdown.md),
[S-F22-03 Cost allocation](../04-accounting/s-f22-03-cost-allocation.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 metered call records of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no metered call record the user may see yet, with the create action when allowed.
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
| Listed, U05, view Mine: user | desktop | ![Listed, U05, view Mine: user, light](../../images/lists/s-f22-l02-metered-call-records-u05-accounting-desktop-light.png) | ![Listed, U05, view Mine: user, dark](../../images/lists/s-f22-l02-metered-call-records-u05-accounting-desktop-dark.png) |
| Listed, U05, view Mine: user | phone | ![Listed, U05, view Mine: user, light](../../images/lists/s-f22-l02-metered-call-records-u05-accounting-phone-light.png) | ![Listed, U05, view Mine: user, dark](../../images/lists/s-f22-l02-metered-call-records-u05-accounting-phone-dark.png) |
| Listed, U13, view All | desktop | ![Listed, U13, view All, light](../../images/lists/s-f22-l02-metered-call-records-u13-owner-desktop-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f22-l02-metered-call-records-u13-owner-desktop-dark.png) |
| Listed, U13, view All | phone | ![Listed, U13, view All, light](../../images/lists/s-f22-l02-metered-call-records-u13-owner-phone-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f22-l02-metered-call-records-u13-owner-phone-dark.png) |
| Listed, U07, view All | desktop | ![Listed, U07, view All, light](../../images/lists/s-f22-l02-metered-call-records-u07-administrator-desktop-light.png) | ![Listed, U07, view All, dark](../../images/lists/s-f22-l02-metered-call-records-u07-administrator-desktop-dark.png) |
| Listed, U07, view All | phone | ![Listed, U07, view All, light](../../images/lists/s-f22-l02-metered-call-records-u07-administrator-phone-light.png) | ![Listed, U07, view All, dark](../../images/lists/s-f22-l02-metered-call-records-u07-administrator-phone-dark.png) |
| Listed, U48, view All | desktop | ![Listed, U48, view All, light](../../images/lists/s-f22-l02-metered-call-records-u48-hosting-engineer-desktop-light.png) | ![Listed, U48, view All, dark](../../images/lists/s-f22-l02-metered-call-records-u48-hosting-engineer-desktop-dark.png) |
| Listed, U48, view All | phone | ![Listed, U48, view All, light](../../images/lists/s-f22-l02-metered-call-records-u48-hosting-engineer-phone-light.png) | ![Listed, U48, view All, dark](../../images/lists/s-f22-l02-metered-call-records-u48-hosting-engineer-phone-dark.png) |
| Listed, U02, view All | desktop | ![Listed, U02, view All, light](../../images/lists/s-f22-l02-metered-call-records-u02-manager-desktop-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-f22-l02-metered-call-records-u02-manager-desktop-dark.png) |
| Listed, U02, view All | phone | ![Listed, U02, view All, light](../../images/lists/s-f22-l02-metered-call-records-u02-manager-phone-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-f22-l02-metered-call-records-u02-manager-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Unified platform cost management › Metered call records](README.md) |
| Workspaces | [U05](../../../../04-ux/views/u05-accounting/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md), [U07](../../../../04-ux/views/u07-administrator/workspace.md), [U48](../../../../04-ux/views/u48-hosting-engineer/workspace.md), [U02](../../../../04-ux/views/u02-manager/workspace.md) |
| Flows | [FL-F22-01](../../flows/fl-f22-01-see-and-set-up.md), [FL-F22-03](../../flows/fl-f22-03-runs.md), [FL-F22-04](../../flows/fl-f22-04-accounting.md), [FL-F22-05](../../flows/fl-f22-05-billing.md), [FL-F22-06](../../flows/fl-f22-06-savings-and-kpis.md), [FL-F22-07](../../flows/fl-f22-07-it-provider-re-billing.md), [FL-F24-04](../../../f24-integrations-hub/flows/fl-f24-04-run-and-control.md) |

## Open questions

None.

---

⬅️ [S-F22-L01 Cost periods](s-f22-l01-cost-periods.md) · ⬆️ [Up](README.md) ·
➡️ [S-F22-L03 Provider price lists](s-f22-l03-provider-price-lists.md)
