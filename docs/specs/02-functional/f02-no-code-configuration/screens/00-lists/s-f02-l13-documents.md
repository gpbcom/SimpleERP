🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔧 [F2 No-code configuration](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: No-code configuration menu](README.md) › 🗂️ S-F2-L13 Documents

# 🗂️ S-F2-L13 Documents

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U16 Office worker](../../../../01-users/personas/u16-office-worker.md) | as the permissions row "Document and email templates (UC-F2-05, 06)": yes | actions as [permissions](../../permissions.md) gives them |
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | as the permissions row "Document and email templates (UC-F2-05, 06)": yes | actions as [permissions](../../permissions.md) gives them |
| [U53 Coach](../../../../01-users/personas/u53-coach.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F2-13 Document](../../data/e-f02-13-document.md) the user may see: to find, filter,
total and act on many documents at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** No-code configuration › Documents, in the capability's menu (D495).
- **Workspaces:** 4 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "documents" offers this view.
- **AI assistant:** "show the documents that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Documents    No-code configuration › Documents   [+ New]                                                     |
| [count]   [chart: count by state]                                                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| folder            | [ ] FOLDER   STATE   LINKED RECORD   TAGS                                                |
| tags              | [ ] ...                                                  Open >                          |
| linked record     | [ ] ...                                                  Open >                          |
| state             | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Folder | folder | text | yes |
| State | state | badge: ToSort, ToValidate, Done | yes |
| Linked record | linked record | link to the record | yes |
| Tags | tags | text | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| Folder | each value | the visible rows (D488) |
| Tags | each value | the visible rows (D488) |
| Linked record | each linked linked record | the visible rows (D488) |
| State | ToSort, ToValidate, Done | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Documents of a chosen folder, or of the folders that match a filter.
- From the other side: the folders that have documents, or none.
- Documents of a chosen linked record, or of the linked records that match a filter.
- From the other side: the linked records that have documents, or none.

## KPI strip

- Count of the visible rows.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Open: ToSort, ToValidate.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New document | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- tags: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F2-13 Documents workspace](../07-benchmark-additions/s-f02-13-documents-workspace.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 documents of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no document the user may see yet, with the create action when allowed.
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
| Listed, U16, view Open: ToSort, ToValidate | desktop | ![Listed, U16, view Open: ToSort, ToValidate, light](../../images/lists/s-f02-l13-documents-u16-office-worker-desktop-light.png) | ![Listed, U16, view Open: ToSort, ToValidate, dark](../../images/lists/s-f02-l13-documents-u16-office-worker-desktop-dark.png) |
| Listed, U16, view Open: ToSort, ToValidate | phone | ![Listed, U16, view Open: ToSort, ToValidate, light](../../images/lists/s-f02-l13-documents-u16-office-worker-phone-light.png) | ![Listed, U16, view Open: ToSort, ToValidate, dark](../../images/lists/s-f02-l13-documents-u16-office-worker-phone-dark.png) |
| Listed, U05, view Open: ToSort, ToValidate | desktop | ![Listed, U05, view Open: ToSort, ToValidate, light](../../images/lists/s-f02-l13-documents-u05-accounting-desktop-light.png) | ![Listed, U05, view Open: ToSort, ToValidate, dark](../../images/lists/s-f02-l13-documents-u05-accounting-desktop-dark.png) |
| Listed, U05, view Open: ToSort, ToValidate | phone | ![Listed, U05, view Open: ToSort, ToValidate, light](../../images/lists/s-f02-l13-documents-u05-accounting-phone-light.png) | ![Listed, U05, view Open: ToSort, ToValidate, dark](../../images/lists/s-f02-l13-documents-u05-accounting-phone-dark.png) |
| Listed, U07, view Open: ToSort, ToValidate | desktop | ![Listed, U07, view Open: ToSort, ToValidate, light](../../images/lists/s-f02-l13-documents-u07-administrator-desktop-light.png) | ![Listed, U07, view Open: ToSort, ToValidate, dark](../../images/lists/s-f02-l13-documents-u07-administrator-desktop-dark.png) |
| Listed, U07, view Open: ToSort, ToValidate | phone | ![Listed, U07, view Open: ToSort, ToValidate, light](../../images/lists/s-f02-l13-documents-u07-administrator-phone-light.png) | ![Listed, U07, view Open: ToSort, ToValidate, dark](../../images/lists/s-f02-l13-documents-u07-administrator-phone-dark.png) |
| Listed, U53, view Open | desktop | ![Listed, U53, view Open, light](../../images/lists/s-f02-l13-documents-u53-coach-desktop-light.png) | ![Listed, U53, view Open, dark](../../images/lists/s-f02-l13-documents-u53-coach-desktop-dark.png) |
| Listed, U53, view Open | phone | ![Listed, U53, view Open, light](../../images/lists/s-f02-l13-documents-u53-coach-phone-light.png) | ![Listed, U53, view Open, dark](../../images/lists/s-f02-l13-documents-u53-coach-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [No-code configuration › Documents](README.md) |
| Workspaces | [U16](../../../../04-ux/views/u16-office-worker/workspace.md), [U05](../../../../04-ux/views/u05-accounting/workspace.md), [U07](../../../../04-ux/views/u07-administrator/workspace.md), [U53](../../../../04-ux/views/u53-coach/workspace.md) |
| Flows | [FL-F1-14](../../../f01-administration/flows/fl-f01-14-close-a-company.md), [FL-F11-03](../../../f11-online-shop/flows/fl-f11-03-after-the-order.md), [FL-F15-03](../../../f15-legal-assistant/flows/fl-f15-03-check-a-document-against-the-law.md), [FL-F15-05](../../../f15-legal-assistant/flows/fl-f15-05-duties-and-records.md), [FL-F2-07](../../flows/fl-f02-07-benchmark-additions.md), [FL-F3-08](../../../f03-assistant/flows/fl-f03-08-manage-and-share-conversations.md), [FL-F3-11](../../../f03-assistant/flows/fl-f03-11-trust-the-answers.md), [FL-F6-06](../../../f06-customers-and-sales/flows/fl-f06-06-accounts-and-credit.md), [FL-F8-10](../../../f08-accounting/flows/fl-f08-10-accountant-collaboration.md), [FL-SC01-01](../../../../08-sectors/sc01-construction/flows/fl-sc01-01-win-the-work.md), [FL-SC03-03](../../../../08-sectors/sc03-services/flows/fl-sc03-03-deliver-and-record.md), [FL-SC07-01](../../../../08-sectors/sc07-transport/flows/fl-sc07-01-orders-and-planning.md), [FL-SC07-06](../../../../08-sectors/sc07-transport/flows/fl-sc07-06-logistics-for-clients.md) |

## Open questions

None.

---

⬅️ [S-F2-L12 Spreadsheets](s-f02-l12-spreadsheets.md) · ⬆️ [Up](README.md) ·
➡️ [S-F2-L14 Signature requests](s-f02-l14-signature-requests.md)
