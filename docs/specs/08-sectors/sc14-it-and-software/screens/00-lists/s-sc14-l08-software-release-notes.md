🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💻 [SC14 IT and software](../../README.md) ›
🖥️ [Screens](../README.md) › 🗂️ [Views: IT and software menu](README.md) › 🗂️ S-SC14-L08 Software release notes

# 🗂️ S-SC14-L08 Software release notes

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U16 Office worker](../../../../01-users/personas/u16-office-worker.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U41 Customer success manager](../../../../01-users/personas/u41-customer-success-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-SC14-08 Software release note](../../data/e-sc14-08-software-release-note.md) the user
may see: to find, filter, total and act on many software release notes at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** IT and software › Software release notes, in the capability's menu (D495).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "software release notes" offers this view.
- **AI assistant:** "show the software release notes that need attention" opens it with the filter as editable chips
  (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Software release notes    IT and software › Software release notes   [+ New]                                 |
| [count] [new this month]   [chart: count by state]                                                           |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] PRODUCT   STATE   FEATURES   DATE                                                    |
| features          | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Product | product | link to the record | yes |
| State | state | badge: Recorded | yes |
| Features | features | link to the record | yes |
| Date | date | link to the record | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Recorded | the visible rows (D488) |
| Features | each linked features | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Software release notes of a chosen features, or of the features that match a filter.
- From the other side: the features that have software release notes, or none.

## KPI strip

- Count of the visible rows.
- New this month, by date.

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
| New software release note | header | the personas whose roles may create it | the record's own page (Row opens) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- date: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-SC14-08 Release notes](../04-product-delivery/s-sc14-08-release-notes.md).

The records also show on: [S-SC14-21 Features](../04-product-delivery/s-sc14-21-features.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 software release notes of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no software release note the user may see yet, with the create action when allowed.
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
| Listed, U16, view All | desktop | ![Listed, U16, view All, light](../../images/lists/s-sc14-l08-software-release-notes-u16-office-worker-desktop-light.png) | ![Listed, U16, view All, dark](../../images/lists/s-sc14-l08-software-release-notes-u16-office-worker-desktop-dark.png) |
| Listed, U16, view All | phone | ![Listed, U16, view All, light](../../images/lists/s-sc14-l08-software-release-notes-u16-office-worker-phone-light.png) | ![Listed, U16, view All, dark](../../images/lists/s-sc14-l08-software-release-notes-u16-office-worker-phone-dark.png) |
| Listed, U41, view All | desktop | ![Listed, U41, view All, light](../../images/lists/s-sc14-l08-software-release-notes-u41-customer-success-manager-desktop-light.png) | ![Listed, U41, view All, dark](../../images/lists/s-sc14-l08-software-release-notes-u41-customer-success-manager-desktop-dark.png) |
| Listed, U41, view All | phone | ![Listed, U41, view All, light](../../images/lists/s-sc14-l08-software-release-notes-u41-customer-success-manager-phone-light.png) | ![Listed, U41, view All, dark](../../images/lists/s-sc14-l08-software-release-notes-u41-customer-success-manager-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [IT and software › Software release notes](README.md) |
| Workspaces | [U16](../../../../04-ux/views/u16-office-worker/workspace.md), [U41](../../../../04-ux/views/u41-customer-success-manager/workspace.md) |
| Flows | [FL-SC14-04](../../flows/fl-sc14-04-product-delivery.md) |

## Open questions

None.

---

⬅️ [S-SC14-L07 Sprints](s-sc14-l07-sprints.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC14-L09 Health scores](s-sc14-l09-health-scores.md)
