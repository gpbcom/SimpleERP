🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🤖 [F3 Assistant](../../README.md) ›
🖥️ [Screens](../README.md) › 🗂️ [Views: Assistant menu](README.md) › 🗂️ S-F3-L04 Assistant change batches

# 🗂️ S-F3-L04 Assistant change batches

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U01 Employee](../../../../01-users/personas/u01-employee.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U03 Sales](../../../../01-users/personas/u03-sales.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U04 Purchasing and stock](../../../../01-users/personas/u04-purchasing.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U06 Human resources](../../../../01-users/personas/u06-hr.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U14 Field worker](../../../../01-users/personas/u14-field-worker.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U15 Warehouse operator](../../../../01-users/personas/u15-warehouse-operator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U16 Office worker](../../../../01-users/personas/u16-office-worker.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

- The owner's review (VC-2, D519): "Create persona(s) related to this enitity."
- Each user sees the batches they asked for; U07 Administrator sees every batch.

## Purpose

The aggregated list of every [E-F3-04 Assistant change batch](../../data/e-f03-04-assistant-change-batch.md) the user
may see: to find, filter, total and act on many assistant change batches at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Assistant › Assistant change batches, in the capability's menu (D495).
- **Workspaces:** 12 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "assistant change batches" offers this view.
- **AI assistant:** "show the assistant change batches that need attention" opens it with the filter as editable chips
  (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Assistant change batches    Assistant › Assistant change batches   [+ New]                                   |
| [count] [new this month]   [chart: count by state]                                                           |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] CONVERSATION   STATUS   USER   CONFIRMED AT                                          |
| conversation      | [ ] ...                                                  Open >                          |
| user              | [ ] ...                                                  Open >                          |
| status            | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Conversation | conversation | text | yes |
| Status | status | badge | yes |
| User | user | person's name | yes |
| Confirmed at | confirmed at | date and time | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Proposed, Cancelled, Done, PartlyDone, Undone | the visible rows (D488) |
| Conversation | each value | the visible rows (D488) |
| User | each person, the user first | the visible rows (D488) |
| Status | Proposed, Cancelled, Done, PartlyDone, Undone | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Assistant change batches of a chosen conversation, or of the conversations that match a filter.
- From the other side: the conversations that have assistant change batches, or none.

## KPI strip

- Count of the visible rows.
- New this month, by confirmed at.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Mine: user.
- Open: Proposed.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New assistant change batch | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change status | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Assign | bulk bar | the personas whose roles may assign | sets the user; audited |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- confirmed at: editable in its cell unless the record's state locks it.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| user | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| changes | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F3-01 Assistant panel](../01-ask-the-assistant/s-f03-01-assistant-panel.md).

The records also show on:
[S-F3-02 Change confirmation card](../03-act-through-the-assistant/s-f03-02-change-confirmation-card.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 assistant change batches of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no assistant change batch the user may see yet, with the create action when allowed.
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
| Listed, U01, view Mine: user | desktop | ![Listed, U01, view Mine: user, light](../../images/lists/s-f03-l04-assistant-change-batches-u01-employee-desktop-light.png) | ![Listed, U01, view Mine: user, dark](../../images/lists/s-f03-l04-assistant-change-batches-u01-employee-desktop-dark.png) |
| Listed, U01, view Mine: user | phone | ![Listed, U01, view Mine: user, light](../../images/lists/s-f03-l04-assistant-change-batches-u01-employee-phone-light.png) | ![Listed, U01, view Mine: user, dark](../../images/lists/s-f03-l04-assistant-change-batches-u01-employee-phone-dark.png) |
| Listed, U02, view Open: Proposed | desktop | ![Listed, U02, view Open: Proposed, light](../../images/lists/s-f03-l04-assistant-change-batches-u02-manager-desktop-light.png) | ![Listed, U02, view Open: Proposed, dark](../../images/lists/s-f03-l04-assistant-change-batches-u02-manager-desktop-dark.png) |
| Listed, U02, view Open: Proposed | phone | ![Listed, U02, view Open: Proposed, light](../../images/lists/s-f03-l04-assistant-change-batches-u02-manager-phone-light.png) | ![Listed, U02, view Open: Proposed, dark](../../images/lists/s-f03-l04-assistant-change-batches-u02-manager-phone-dark.png) |
| Listed, U03, view Mine: user | desktop | ![Listed, U03, view Mine: user, light](../../images/lists/s-f03-l04-assistant-change-batches-u03-sales-desktop-light.png) | ![Listed, U03, view Mine: user, dark](../../images/lists/s-f03-l04-assistant-change-batches-u03-sales-desktop-dark.png) |
| Listed, U03, view Mine: user | phone | ![Listed, U03, view Mine: user, light](../../images/lists/s-f03-l04-assistant-change-batches-u03-sales-phone-light.png) | ![Listed, U03, view Mine: user, dark](../../images/lists/s-f03-l04-assistant-change-batches-u03-sales-phone-dark.png) |
| Listed, U04, view Mine: user | desktop | ![Listed, U04, view Mine: user, light](../../images/lists/s-f03-l04-assistant-change-batches-u04-purchasing-desktop-light.png) | ![Listed, U04, view Mine: user, dark](../../images/lists/s-f03-l04-assistant-change-batches-u04-purchasing-desktop-dark.png) |
| Listed, U04, view Mine: user | phone | ![Listed, U04, view Mine: user, light](../../images/lists/s-f03-l04-assistant-change-batches-u04-purchasing-phone-light.png) | ![Listed, U04, view Mine: user, dark](../../images/lists/s-f03-l04-assistant-change-batches-u04-purchasing-phone-dark.png) |
| Listed, U05, view Mine: user | desktop | ![Listed, U05, view Mine: user, light](../../images/lists/s-f03-l04-assistant-change-batches-u05-accounting-desktop-light.png) | ![Listed, U05, view Mine: user, dark](../../images/lists/s-f03-l04-assistant-change-batches-u05-accounting-desktop-dark.png) |
| Listed, U05, view Mine: user | phone | ![Listed, U05, view Mine: user, light](../../images/lists/s-f03-l04-assistant-change-batches-u05-accounting-phone-light.png) | ![Listed, U05, view Mine: user, dark](../../images/lists/s-f03-l04-assistant-change-batches-u05-accounting-phone-dark.png) |
| Listed, U06, view Open: Proposed | desktop | ![Listed, U06, view Open: Proposed, light](../../images/lists/s-f03-l04-assistant-change-batches-u06-hr-desktop-light.png) | ![Listed, U06, view Open: Proposed, dark](../../images/lists/s-f03-l04-assistant-change-batches-u06-hr-desktop-dark.png) |
| Listed, U06, view Open: Proposed | phone | ![Listed, U06, view Open: Proposed, light](../../images/lists/s-f03-l04-assistant-change-batches-u06-hr-phone-light.png) | ![Listed, U06, view Open: Proposed, dark](../../images/lists/s-f03-l04-assistant-change-batches-u06-hr-phone-dark.png) |
| Listed, U07, view Open: Proposed | desktop | ![Listed, U07, view Open: Proposed, light](../../images/lists/s-f03-l04-assistant-change-batches-u07-administrator-desktop-light.png) | ![Listed, U07, view Open: Proposed, dark](../../images/lists/s-f03-l04-assistant-change-batches-u07-administrator-desktop-dark.png) |
| Listed, U07, view Open: Proposed | phone | ![Listed, U07, view Open: Proposed, light](../../images/lists/s-f03-l04-assistant-change-batches-u07-administrator-phone-light.png) | ![Listed, U07, view Open: Proposed, dark](../../images/lists/s-f03-l04-assistant-change-batches-u07-administrator-phone-dark.png) |
| Listed, U12, view Mine: user | desktop | ![Listed, U12, view Mine: user, light](../../images/lists/s-f03-l04-assistant-change-batches-u12-marketing-desktop-light.png) | ![Listed, U12, view Mine: user, dark](../../images/lists/s-f03-l04-assistant-change-batches-u12-marketing-desktop-dark.png) |
| Listed, U12, view Mine: user | phone | ![Listed, U12, view Mine: user, light](../../images/lists/s-f03-l04-assistant-change-batches-u12-marketing-phone-light.png) | ![Listed, U12, view Mine: user, dark](../../images/lists/s-f03-l04-assistant-change-batches-u12-marketing-phone-dark.png) |
| Listed, U13, view Open: Proposed | desktop | ![Listed, U13, view Open: Proposed, light](../../images/lists/s-f03-l04-assistant-change-batches-u13-owner-desktop-light.png) | ![Listed, U13, view Open: Proposed, dark](../../images/lists/s-f03-l04-assistant-change-batches-u13-owner-desktop-dark.png) |
| Listed, U13, view Open: Proposed | phone | ![Listed, U13, view Open: Proposed, light](../../images/lists/s-f03-l04-assistant-change-batches-u13-owner-phone-light.png) | ![Listed, U13, view Open: Proposed, dark](../../images/lists/s-f03-l04-assistant-change-batches-u13-owner-phone-dark.png) |
| Listed, U14, view Mine: user | desktop | ![Listed, U14, view Mine: user, light](../../images/lists/s-f03-l04-assistant-change-batches-u14-field-worker-desktop-light.png) | ![Listed, U14, view Mine: user, dark](../../images/lists/s-f03-l04-assistant-change-batches-u14-field-worker-desktop-dark.png) |
| Listed, U14, view Mine: user | phone | ![Listed, U14, view Mine: user, light](../../images/lists/s-f03-l04-assistant-change-batches-u14-field-worker-phone-light.png) | ![Listed, U14, view Mine: user, dark](../../images/lists/s-f03-l04-assistant-change-batches-u14-field-worker-phone-dark.png) |
| Listed, U15, view Mine: user | desktop | ![Listed, U15, view Mine: user, light](../../images/lists/s-f03-l04-assistant-change-batches-u15-warehouse-operator-desktop-light.png) | ![Listed, U15, view Mine: user, dark](../../images/lists/s-f03-l04-assistant-change-batches-u15-warehouse-operator-desktop-dark.png) |
| Listed, U15, view Mine: user | phone | ![Listed, U15, view Mine: user, light](../../images/lists/s-f03-l04-assistant-change-batches-u15-warehouse-operator-phone-light.png) | ![Listed, U15, view Mine: user, dark](../../images/lists/s-f03-l04-assistant-change-batches-u15-warehouse-operator-phone-dark.png) |
| Listed, U16, view Mine: user | desktop | ![Listed, U16, view Mine: user, light](../../images/lists/s-f03-l04-assistant-change-batches-u16-office-worker-desktop-light.png) | ![Listed, U16, view Mine: user, dark](../../images/lists/s-f03-l04-assistant-change-batches-u16-office-worker-desktop-dark.png) |
| Listed, U16, view Mine: user | phone | ![Listed, U16, view Mine: user, light](../../images/lists/s-f03-l04-assistant-change-batches-u16-office-worker-phone-light.png) | ![Listed, U16, view Mine: user, dark](../../images/lists/s-f03-l04-assistant-change-batches-u16-office-worker-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Assistant › Assistant change batches](README.md) |
| Workspaces | [U01](../../../../04-ux/views/u01-employee/workspace.md), [U02](../../../../04-ux/views/u02-manager/workspace.md), [U03](../../../../04-ux/views/u03-sales/workspace.md), [U04](../../../../04-ux/views/u04-purchasing/workspace.md), [U05](../../../../04-ux/views/u05-accounting/workspace.md), [U06](../../../../04-ux/views/u06-hr/workspace.md), [U07](../../../../04-ux/views/u07-administrator/workspace.md), [U12](../../../../04-ux/views/u12-marketing/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md), [U14](../../../../04-ux/views/u14-field-worker/workspace.md), [U15](../../../../04-ux/views/u15-warehouse-operator/workspace.md), [U16](../../../../04-ux/views/u16-office-worker/workspace.md) |
| Flows | [FL-F12-08](../../../f12-manufacturing/flows/fl-f12-08-report-and-assist.md), [FL-F15-03](../../../f15-legal-assistant/flows/fl-f15-03-check-a-document-against-the-law.md), [FL-F3-03](../../flows/fl-f03-03-act-through-the-assistant.md), [FL-SC01-03](../../../../08-sectors/sc01-construction/flows/fl-sc01-03-run-the-site.md), [FL-SC02-05](../../../../08-sectors/sc02-retail/flows/fl-sc02-05-unsold-goods-and-performance.md), [FL-SC03-03](../../../../08-sectors/sc03-services/flows/fl-sc03-03-deliver-and-record.md), [FL-SC05-04](../../../../08-sectors/sc05-manufacturing/flows/fl-sc05-04-quality-system.md), [FL-SC06-03](../../../../08-sectors/sc06-hospitality/flows/fl-sc06-03-rooms-and-bookings.md), [FL-SC07-01](../../../../08-sectors/sc07-transport/flows/fl-sc07-01-orders-and-planning.md), [FL-SC08-02](../../../../08-sectors/sc08-non-profit/flows/fl-sc08-02-donations-and-receipts.md), [FL-SC10-06](../../../../08-sectors/sc10-real-estate/flows/fl-sc10-06-portal-and-assistant.md), [FL-SC12-03](../../../../08-sectors/sc12-education-and-training/flows/fl-sc12-03-deliver-and-assess.md), [FL-SC13-03](../../../../08-sectors/sc13-agriculture-and-food/flows/fl-sc13-03-farm-business.md), [FL-SC14-06](../../../../08-sectors/sc14-it-and-software/flows/fl-sc14-06-portal-and-metrics.md), [FL-SC15-05](../../../../08-sectors/sc15-wholesale-and-distribution/flows/fl-sc15-05-sales-force-and-performance.md), [FL-SC16-05](../../../../08-sectors/sc16-events-and-culture/flows/fl-sc16-05-declarations-and-reports.md) |

## Open questions

None.

---

⬅️ [S-F3-L03 Suggested questions](s-f03-l03-suggested-questions.md) · ⬆️ [Up](README.md) ·
➡️ [S-F3-L05 Company writing styles](s-f03-l05-company-writing-styles.md)
