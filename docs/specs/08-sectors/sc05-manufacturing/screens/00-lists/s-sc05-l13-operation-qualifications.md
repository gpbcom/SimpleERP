🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏭 [SC05 Manufacturing](../../README.md) ›
🖥️ [Screens](../README.md) › 🗂️ [Views: Manufacturing menu](README.md) › 🗂️ S-SC05-L13 Operation qualifications

# 🗂️ S-SC05-L13 Operation qualifications

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U27 Quality manager](../../../../01-users/personas/u27-quality-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U06 Human resources](../../../../01-users/personas/u06-hr.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U20 Production operator](../../../../01-users/personas/u20-production-operator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-SC05-13 Operation qualification](../../data/e-sc05-13-operation-qualification.md) the
user may see: to find, filter, total and act on many operation qualifications at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Manufacturing › Operation qualifications, in the capability's menu (D495).
- **Workspaces:** 3 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "operation qualifications" offers this view.
- **AI assistant:** "show the operation qualifications that need attention" opens it with the filter as editable chips
  (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Operation qualifications    Manufacturing › Operation qualifications   [+ New]                               |
| [count] [new this month]   [chart: count by state]                                                           |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] PERSON   STATE   VALID TO                                                            |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Person | person | link to the record | yes |
| State | state | badge: Active | yes |
| Valid to | valid to | date | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Active | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: operation qualifications link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- New this month, by valid to.

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
| New operation qualification | header | the personas whose roles may create it | the record's own page (Row opens) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- valid to: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-SC05-13 Qualifications](../05-suppliers-and-customers/s-sc05-13-qualifications.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 operation qualifications of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no operation qualification the user may see yet, with the create action when allowed.
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
| Listed, U27, view All | desktop | ![Listed, U27, view All, light](../../images/lists/s-sc05-l13-operation-qualifications-u27-quality-manager-desktop-light.png) | ![Listed, U27, view All, dark](../../images/lists/s-sc05-l13-operation-qualifications-u27-quality-manager-desktop-dark.png) |
| Listed, U27, view All | phone | ![Listed, U27, view All, light](../../images/lists/s-sc05-l13-operation-qualifications-u27-quality-manager-phone-light.png) | ![Listed, U27, view All, dark](../../images/lists/s-sc05-l13-operation-qualifications-u27-quality-manager-phone-dark.png) |
| Listed, U06, view All | desktop | ![Listed, U06, view All, light](../../images/lists/s-sc05-l13-operation-qualifications-u06-hr-desktop-light.png) | ![Listed, U06, view All, dark](../../images/lists/s-sc05-l13-operation-qualifications-u06-hr-desktop-dark.png) |
| Listed, U06, view All | phone | ![Listed, U06, view All, light](../../images/lists/s-sc05-l13-operation-qualifications-u06-hr-phone-light.png) | ![Listed, U06, view All, dark](../../images/lists/s-sc05-l13-operation-qualifications-u06-hr-phone-dark.png) |
| Listed, U20, view All | desktop | ![Listed, U20, view All, light](../../images/lists/s-sc05-l13-operation-qualifications-u20-production-operator-desktop-light.png) | ![Listed, U20, view All, dark](../../images/lists/s-sc05-l13-operation-qualifications-u20-production-operator-desktop-dark.png) |
| Listed, U20, view All | phone | ![Listed, U20, view All, light](../../images/lists/s-sc05-l13-operation-qualifications-u20-production-operator-phone-light.png) | ![Listed, U20, view All, dark](../../images/lists/s-sc05-l13-operation-qualifications-u20-production-operator-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Manufacturing › Operation qualifications](README.md) |
| Workspaces | [U27](../../../../04-ux/views/u27-quality-manager/workspace.md), [U06](../../../../04-ux/views/u06-hr/workspace.md), [U20](../../../../04-ux/views/u20-production-operator/workspace.md) |
| Flows | [FL-SC05-05](../../flows/fl-sc05-05-suppliers-and-customers.md) |

## Open questions

None.

---

⬅️ [S-SC05-L12 Instruments](s-sc05-l12-instruments.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC05-L14 Management reviews](s-sc05-l14-management-reviews.md)
