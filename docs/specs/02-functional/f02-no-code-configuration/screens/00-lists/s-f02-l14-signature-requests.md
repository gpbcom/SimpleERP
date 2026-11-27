🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔧 [F2 No-code configuration](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: No-code configuration menu](README.md) › 🗂️ S-F2-L14 Signature requests

# 🗂️ S-F2-L14 Signature requests

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U16 Office worker](../../../../01-users/personas/u16-office-worker.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U03 Sales](../../../../01-users/personas/u03-sales.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U06 Human resources](../../../../01-users/personas/u06-hr.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U14 Field worker](../../../../01-users/personas/u14-field-worker.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U56: their use cases only read these records, inside a screen of the use case, so they open them
from there (D493).

## Purpose

The aggregated list of every [E-F2-14 Signature request](../../data/e-f02-14-signature-request.md) the user may see: to
find, filter, total and act on many signature requests at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** No-code configuration › Signature requests, in the capability's menu (D495).
- **Workspaces:** 5 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "signature requests" offers this view.
- **AI assistant:** "show the signature requests that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Signature requests    No-code configuration › Signature requests   [+ New]                                   |
| [count] [Expired]   [chart: count by state]                                                                  |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| document          | [ ] DOCUMENT   STATE                                                                     |
| state             | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Document | document | file name | no |
| State | state | badge: Sent, Signed, Refused, Expired | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| Document | each value | the visible rows (D488) |
| State | Sent, Signed, Refused, Expired | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Signature requests of a chosen document, or of the documents that match a filter.
- From the other side: the documents that have signature requests, or none.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Expired.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Open: Sent, Signed, Refused.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New signature request | header | the personas whose roles may create it | the record's own page (Row opens) |
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

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| signers | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F2-14 Signature requests](../07-benchmark-additions/s-f02-14-signature-requests.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 signature requests of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no signature request the user may see yet, with the create action when allowed.
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
| Listed, U16, view Open: Sent, Signed, Refused | desktop | ![Listed, U16, view Open: Sent, Signed, Refused, light](../../images/lists/s-f02-l14-signature-requests-u16-office-worker-desktop-light.png) | ![Listed, U16, view Open: Sent, Signed, Refused, dark](../../images/lists/s-f02-l14-signature-requests-u16-office-worker-desktop-dark.png) |
| Listed, U16, view Open: Sent, Signed, Refused | phone | ![Listed, U16, view Open: Sent, Signed, Refused, light](../../images/lists/s-f02-l14-signature-requests-u16-office-worker-phone-light.png) | ![Listed, U16, view Open: Sent, Signed, Refused, dark](../../images/lists/s-f02-l14-signature-requests-u16-office-worker-phone-dark.png) |
| Listed, U03, view Open: Sent, Signed, Refused | desktop | ![Listed, U03, view Open: Sent, Signed, Refused, light](../../images/lists/s-f02-l14-signature-requests-u03-sales-desktop-light.png) | ![Listed, U03, view Open: Sent, Signed, Refused, dark](../../images/lists/s-f02-l14-signature-requests-u03-sales-desktop-dark.png) |
| Listed, U03, view Open: Sent, Signed, Refused | phone | ![Listed, U03, view Open: Sent, Signed, Refused, light](../../images/lists/s-f02-l14-signature-requests-u03-sales-phone-light.png) | ![Listed, U03, view Open: Sent, Signed, Refused, dark](../../images/lists/s-f02-l14-signature-requests-u03-sales-phone-dark.png) |
| Listed, U06, view Needs attention | desktop | ![Listed, U06, view Needs attention, light](../../images/lists/s-f02-l14-signature-requests-u06-hr-desktop-light.png) | ![Listed, U06, view Needs attention, dark](../../images/lists/s-f02-l14-signature-requests-u06-hr-desktop-dark.png) |
| Listed, U06, view Needs attention | phone | ![Listed, U06, view Needs attention, light](../../images/lists/s-f02-l14-signature-requests-u06-hr-phone-light.png) | ![Listed, U06, view Needs attention, dark](../../images/lists/s-f02-l14-signature-requests-u06-hr-phone-dark.png) |
| Listed, U09, view Open | desktop | ![Listed, U09, view Open, light](../../images/lists/s-f02-l14-signature-requests-u09-customer-desktop-light.png) | ![Listed, U09, view Open, dark](../../images/lists/s-f02-l14-signature-requests-u09-customer-desktop-dark.png) |
| Listed, U09, view Open | phone | ![Listed, U09, view Open, light](../../images/lists/s-f02-l14-signature-requests-u09-customer-phone-light.png) | ![Listed, U09, view Open, dark](../../images/lists/s-f02-l14-signature-requests-u09-customer-phone-dark.png) |
| Listed, U14, view Open | desktop | ![Listed, U14, view Open, light](../../images/lists/s-f02-l14-signature-requests-u14-field-worker-desktop-light.png) | ![Listed, U14, view Open, dark](../../images/lists/s-f02-l14-signature-requests-u14-field-worker-desktop-dark.png) |
| Listed, U14, view Open | phone | ![Listed, U14, view Open, light](../../images/lists/s-f02-l14-signature-requests-u14-field-worker-phone-light.png) | ![Listed, U14, view Open, dark](../../images/lists/s-f02-l14-signature-requests-u14-field-worker-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [No-code configuration › Signature requests](README.md) |
| Workspaces | [U16](../../../../04-ux/views/u16-office-worker/workspace.md), [U03](../../../../04-ux/views/u03-sales/workspace.md), [U06](../../../../04-ux/views/u06-hr/workspace.md), [U09](../../../../04-ux/views/u09-customer/workspace.md), [U14](../../../../04-ux/views/u14-field-worker/workspace.md) |
| Flows | [FL-F2-07](../../flows/fl-f02-07-benchmark-additions.md), [FL-F6-02](../../../f06-customers-and-sales/flows/fl-f06-02-quote-to-order.md), [FL-F9-06](../../../f09-hr-and-projects/flows/fl-f09-06-plan-and-deliver-work.md), [FL-SC11-02](../../../../08-sectors/sc11-professional-firms/flows/fl-sc11-02-matters-and-documents.md) |

## Open questions

None.

---

⬅️ [S-F2-L13 Documents](s-f02-l13-documents.md) · ⬆️ [Up](README.md) · ➡️ [S-F2-L15 Sandboxes](s-f02-l15-sandboxes.md)
