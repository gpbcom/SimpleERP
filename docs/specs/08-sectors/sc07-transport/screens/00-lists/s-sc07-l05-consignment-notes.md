🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🚛 [SC07 Transport and logistics](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Transport and logistics menu](README.md) › 🗂️ S-SC07-L05 Consignment notes

# 🗂️ S-SC07-L05 Consignment notes

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U29 Dispatcher](../../../../01-users/personas/u29-dispatcher.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U30 Driver](../../../../01-users/personas/u30-driver.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-SC07-05 Consignment note](../../data/e-sc07-05-consignment-note.md) the user may see: to
find, filter, total and act on many consignment notes at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Transport and logistics › Consignment notes, in the capability's menu (D495).
- **Workspaces:** 4 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "consignment notes" offers this view.
- **AI assistant:** "show the consignment notes that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Consignment notes    Transport and logistics › Consignment notes   [+ New]                                   |
| [count]   [chart: count by state]                                                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] ORDER   STATE                                                                        |
| order             | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Order | order | link to the record | yes |
| State | state | badge: Recorded | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Recorded | the visible rows (D488) |
| Order | each linked order | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Consignment notes of a chosen order, or of the orders that match a filter.
- From the other side: the orders that have consignment notes, or none.

## KPI strip

- Count of the visible rows.

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
| New consignment note | header | the personas whose roles may create it | the record's own page (Row opens) |
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

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| signatures | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-SC07-05 Consignment notes](../03-on-the-road/s-sc07-05-consignment-notes.md).

The records also show on: [S-SC07-16 Client portal](../06-logistics-for-clients/s-sc07-16-client-portal.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 consignment notes of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no consignment note the user may see yet, with the create action when allowed.
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
| Listed, U29, view All | desktop | ![Listed, U29, view All, light](../../images/lists/s-sc07-l05-consignment-notes-u29-dispatcher-desktop-light.png) | ![Listed, U29, view All, dark](../../images/lists/s-sc07-l05-consignment-notes-u29-dispatcher-desktop-dark.png) |
| Listed, U29, view All | phone | ![Listed, U29, view All, light](../../images/lists/s-sc07-l05-consignment-notes-u29-dispatcher-phone-light.png) | ![Listed, U29, view All, dark](../../images/lists/s-sc07-l05-consignment-notes-u29-dispatcher-phone-dark.png) |
| Listed, U30, view All | desktop | ![Listed, U30, view All, light](../../images/lists/s-sc07-l05-consignment-notes-u30-driver-desktop-light.png) | ![Listed, U30, view All, dark](../../images/lists/s-sc07-l05-consignment-notes-u30-driver-desktop-dark.png) |
| Listed, U30, view All | phone | ![Listed, U30, view All, light](../../images/lists/s-sc07-l05-consignment-notes-u30-driver-phone-light.png) | ![Listed, U30, view All, dark](../../images/lists/s-sc07-l05-consignment-notes-u30-driver-phone-dark.png) |
| Listed, U09, view All | desktop | ![Listed, U09, view All, light](../../images/lists/s-sc07-l05-consignment-notes-u09-customer-desktop-light.png) | ![Listed, U09, view All, dark](../../images/lists/s-sc07-l05-consignment-notes-u09-customer-desktop-dark.png) |
| Listed, U09, view All | phone | ![Listed, U09, view All, light](../../images/lists/s-sc07-l05-consignment-notes-u09-customer-phone-light.png) | ![Listed, U09, view All, dark](../../images/lists/s-sc07-l05-consignment-notes-u09-customer-phone-dark.png) |
| Listed, U05, view All | desktop | ![Listed, U05, view All, light](../../images/lists/s-sc07-l05-consignment-notes-u05-accounting-desktop-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-sc07-l05-consignment-notes-u05-accounting-desktop-dark.png) |
| Listed, U05, view All | phone | ![Listed, U05, view All, light](../../images/lists/s-sc07-l05-consignment-notes-u05-accounting-phone-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-sc07-l05-consignment-notes-u05-accounting-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Transport and logistics › Consignment notes](README.md) |
| Workspaces | [U29](../../../../04-ux/views/u29-dispatcher/workspace.md), [U30](../../../../04-ux/views/u30-driver/workspace.md), [U09](../../../../04-ux/views/u09-customer/workspace.md), [U05](../../../../04-ux/views/u05-accounting/workspace.md) |
| Flows | [FL-SC07-03](../../flows/fl-sc07-03-on-the-road.md), [FL-SC07-05](../../flows/fl-sc07-05-billing-and-performance.md), [FL-SC07-06](../../flows/fl-sc07-06-logistics-for-clients.md) |

## Open questions

None.

---

⬅️ [S-SC07-L04 Driver documents](s-sc07-l04-driver-documents.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC07-L06 Stops](s-sc07-l06-stops.md)
