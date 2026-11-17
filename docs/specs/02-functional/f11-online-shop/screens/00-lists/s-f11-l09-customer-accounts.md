🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛍️ [F11 Online shop (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Online shop (plugin) menu](README.md) › 🗂️ S-F11-L09 Customer accounts

# 🗂️ S-F11-L09 Customer accounts

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |
| [U03 Sales](../../../../01-users/personas/u03-sales.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U12, U16, U23, U56: their use cases only read these records, inside a screen of the use case, so
they open them from there (D493).

## Purpose

The aggregated list of every [E-F11-09 Customer account](../../data/e-f11-09-customer-account.md) the user may see: to
find, filter, total and act on many customer accounts at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Online shop (plugin) › Customer accounts, in the capability's menu (D495).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "customer accounts" offers this view.
- **AI assistant:** "show the customer accounts that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Customer accounts    Online shop (plugin) › Customer accounts   [+ New]                                      |
| [count] [new this month]   [chart: count by state]                                                           |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] CONTACT   STATE   CONSENTS   ADDRESSES                                               |
| contact           | [ ] ...                                                  Open >                          |
| addresses         | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Contact | contact | person's name | yes |
| State | state | badge: Active | yes |
| Consents | consents | date | yes |
| Addresses | addresses | text | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Active | the visible rows (D488) |
| Contact | each person, the user first | the visible rows (D488) |
| Addresses | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: customer accounts link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- New this month, by consents.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Mine: contact.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New customer account | header | the personas whose roles may create it | the record's own page (Row opens) |
| Assign | bulk bar | the personas whose roles may assign | sets the contact; audited |
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
| contact | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| addresses | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| consents | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F11-10 Customer account](../03-after-the-order/s-f11-10-customer-account.md).

The records also show on: [S-F11-11 B2B access](../04-special-sales/s-f11-11-b2b-access.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 customer accounts of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no customer account the user may see yet, with the create action when allowed.
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
| Listed, U09, view Mine: contact | desktop | ![Listed, U09, view Mine: contact, light](../../images/lists/s-f11-l09-customer-accounts-u09-customer-desktop-light.png) | ![Listed, U09, view Mine: contact, dark](../../images/lists/s-f11-l09-customer-accounts-u09-customer-desktop-dark.png) |
| Listed, U09, view Mine: contact | phone | ![Listed, U09, view Mine: contact, light](../../images/lists/s-f11-l09-customer-accounts-u09-customer-phone-light.png) | ![Listed, U09, view Mine: contact, dark](../../images/lists/s-f11-l09-customer-accounts-u09-customer-phone-dark.png) |
| Listed, U03, view Mine: contact | desktop | ![Listed, U03, view Mine: contact, light](../../images/lists/s-f11-l09-customer-accounts-u03-sales-desktop-light.png) | ![Listed, U03, view Mine: contact, dark](../../images/lists/s-f11-l09-customer-accounts-u03-sales-desktop-dark.png) |
| Listed, U03, view Mine: contact | phone | ![Listed, U03, view Mine: contact, light](../../images/lists/s-f11-l09-customer-accounts-u03-sales-phone-light.png) | ![Listed, U03, view Mine: contact, dark](../../images/lists/s-f11-l09-customer-accounts-u03-sales-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Online shop (plugin) › Customer accounts](README.md) |
| Workspaces | [U09](../../../../04-ux/views/u09-customer/workspace.md), [U03](../../../../04-ux/views/u03-sales/workspace.md) |
| Flows | [FL-F11-03](../../flows/fl-f11-03-after-the-order.md), [FL-F11-04](../../flows/fl-f11-04-special-sales.md) |

## Open questions

None.

---

⬅️ [S-F11-L08 Withdrawal requests](s-f11-l08-withdrawal-requests.md) · ⬆️ [Up](README.md) ·
➡️ [S-F11-L10 Product reviews](s-f11-l10-product-reviews.md)
