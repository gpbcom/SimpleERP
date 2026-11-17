🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F19 Feature factory (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Feature factory (hosted edition) menu](README.md) › 🗂️ S-F19-L09 Hosted invoices

# 🗂️ S-F19-L09 Hosted invoices

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F19-09 Hosted invoice](../../data/e-f19-09-hosted-invoice.md) the user may see: to find,
filter, total and act on many hosted invoices at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Feature factory (hosted edition) › Hosted invoices, in the capability's menu (D495).
- **Workspaces:** 3 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "hosted invoices" offers this view.
- **AI assistant:** "show the hosted invoices that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Hosted invoices    Feature factory (hosted edition) › Hosted invoices   [+ New]                              |
| [count]   [chart: count by state]                                                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] COMPANY   STATE   KIND                                                               |
| company           | [ ] ...                                                  Open >                          |
| kind              | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Company | company | link to the record | yes |
| State | state | badge: Active | yes |
| Kind | kind | link to the record | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Active | the visible rows (D488) |
| Company | each linked company | the visible rows (D488) |
| Kind | each linked kind | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Hosted invoices of a chosen company, or of the companies that match a filter.
- From the other side: the companies that have hosted invoices, or none.

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
| New hosted invoice | header | the personas whose roles may create it | the record's own page (Row opens) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- kind: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F19-16 Invoices](../05-bill-and-credit/s-f19-16-invoices.md).

The records also show on: [S-F19-15 Credits](../05-bill-and-credit/s-f19-15-credits.md),
[S-F19-22 Refunds](../06-delivery-and-refunds/s-f19-22-refunds.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 hosted invoices of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no hosted invoice the user may see yet, with the create action when allowed.
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
| Listed, U05, view All | desktop | ![Listed, U05, view All, light](../../images/lists/s-f19-l09-hosted-invoices-u05-accounting-desktop-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-f19-l09-hosted-invoices-u05-accounting-desktop-dark.png) |
| Listed, U05, view All | phone | ![Listed, U05, view All, light](../../images/lists/s-f19-l09-hosted-invoices-u05-accounting-phone-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-f19-l09-hosted-invoices-u05-accounting-phone-dark.png) |
| Listed, U13, view All | desktop | ![Listed, U13, view All, light](../../images/lists/s-f19-l09-hosted-invoices-u13-owner-desktop-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f19-l09-hosted-invoices-u13-owner-desktop-dark.png) |
| Listed, U13, view All | phone | ![Listed, U13, view All, light](../../images/lists/s-f19-l09-hosted-invoices-u13-owner-phone-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f19-l09-hosted-invoices-u13-owner-phone-dark.png) |
| Listed, U07, view All | desktop | ![Listed, U07, view All, light](../../images/lists/s-f19-l09-hosted-invoices-u07-administrator-desktop-light.png) | ![Listed, U07, view All, dark](../../images/lists/s-f19-l09-hosted-invoices-u07-administrator-desktop-dark.png) |
| Listed, U07, view All | phone | ![Listed, U07, view All, light](../../images/lists/s-f19-l09-hosted-invoices-u07-administrator-phone-light.png) | ![Listed, U07, view All, dark](../../images/lists/s-f19-l09-hosted-invoices-u07-administrator-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Feature factory (hosted edition) › Hosted invoices](README.md) |
| Workspaces | [U05](../../../../04-ux/views/u05-accounting/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md), [U07](../../../../04-ux/views/u07-administrator/workspace.md) |
| Flows | [FL-F19-05](../../flows/fl-f19-05-bill-and-credit.md), [FL-F19-06](../../flows/fl-f19-06-delivery-and-refunds.md), [FL-F20-06](../../../f20-hosted-support-assistant/flows/fl-f20-06-after-an-incident.md) |

## Open questions

None.

---

⬅️ [S-F19-L08 Promotion credits](s-f19-l08-promotion-credits.md) · ⬆️ [Up](README.md) ·
➡️ [S-F19-L10 Feature withdrawals](s-f19-l10-feature-withdrawals.md)
