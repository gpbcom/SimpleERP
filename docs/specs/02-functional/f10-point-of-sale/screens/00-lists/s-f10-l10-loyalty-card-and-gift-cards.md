🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏪 [F10 Point of sale (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Point of sale (plugin) menu](README.md) › 🗂️ S-F10-L10 Loyalty card and gift cards

# 🗂️ S-F10-L10 Loyalty card and gift cards

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U17 Cashier](../../../../01-users/personas/u17-cashier.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |
| [U23 Store manager](../../../../01-users/personas/u23-store-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U52 Beautician](../../../../01-users/personas/u52-beautician.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U43, U44: their use cases only read these records, inside a screen of the use case, so they open
them from there (D493).

## Purpose

The aggregated list of every [E-F10-10 Loyalty card and gift card](../../data/e-f10-10-loyalty-card-and-gift-card.md)
the user may see: to find, filter, total and act on many loyalty card and gift cards at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Point of sale (plugin) › Loyalty card and gift cards, in the capability's menu (D495).
- **Workspaces:** 4 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "loyalty card and gift cards" offers this view.
- **AI assistant:** "show the loyalty card and gift cards that need attention" opens it with the filter as editable
  chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Loyalty card and gift cards    Point of sale (plugin) › Loyalty card and gift cards   [+ New]                |
| [count] [total balance] [new this month]   [chart: count by state, balance stacked]                          |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] KIND   STATE   CUSTOMER   BALANCE   VALID UNTIL                                      |
| kind              | [ ] ...                                                  Open >                          |
| customer          | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Kind | kind | label | yes |
| State | state | badge: Active | yes |
| Customer | customer | person's name | yes |
| Balance | balance | amount, right-aligned | yes |
| Valid until | valid until | date | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Active | the visible rows (D488) |
| Kind | loyalty, gift card, e-wallet | the visible rows (D488) |
| Customer | each person, the user first | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: loyalty card and gift cards link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- Total of balance.
- New this month, by valid until.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state, balance stacked (VR-8); the Chart button turns the filtered list into a chart the user can pin to their
home screen (C-09).

## Saved views

- All.
- Mine: customer.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New loyalty card and gift card | header | the personas whose roles may create it | the record's own page (Row opens) |
| Assign | bulk bar | the personas whose roles may assign | sets the customer; audited |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- valid until: editable in its cell unless the record's state locks it.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| customer | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F10-07 Loyalty](../03-after-sales/s-f10-07-loyalty.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 loyalty card and gift cards of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no loyalty card and gift card the user may see yet, with the create action when allowed.
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
| Listed, U17, view Mine: customer | desktop | ![Listed, U17, view Mine: customer, light](../../images/lists/s-f10-l10-loyalty-card-and-gift-cards-u17-cashier-desktop-light.png) | ![Listed, U17, view Mine: customer, dark](../../images/lists/s-f10-l10-loyalty-card-and-gift-cards-u17-cashier-desktop-dark.png) |
| Listed, U17, view Mine: customer | phone | ![Listed, U17, view Mine: customer, light](../../images/lists/s-f10-l10-loyalty-card-and-gift-cards-u17-cashier-phone-light.png) | ![Listed, U17, view Mine: customer, dark](../../images/lists/s-f10-l10-loyalty-card-and-gift-cards-u17-cashier-phone-dark.png) |
| Listed, U09, view Mine: customer | desktop | ![Listed, U09, view Mine: customer, light](../../images/lists/s-f10-l10-loyalty-card-and-gift-cards-u09-customer-desktop-light.png) | ![Listed, U09, view Mine: customer, dark](../../images/lists/s-f10-l10-loyalty-card-and-gift-cards-u09-customer-desktop-dark.png) |
| Listed, U09, view Mine: customer | phone | ![Listed, U09, view Mine: customer, light](../../images/lists/s-f10-l10-loyalty-card-and-gift-cards-u09-customer-phone-light.png) | ![Listed, U09, view Mine: customer, dark](../../images/lists/s-f10-l10-loyalty-card-and-gift-cards-u09-customer-phone-dark.png) |
| Listed, U23, view Mine | desktop | ![Listed, U23, view Mine, light](../../images/lists/s-f10-l10-loyalty-card-and-gift-cards-u23-store-manager-desktop-light.png) | ![Listed, U23, view Mine, dark](../../images/lists/s-f10-l10-loyalty-card-and-gift-cards-u23-store-manager-desktop-dark.png) |
| Listed, U23, view Mine | phone | ![Listed, U23, view Mine, light](../../images/lists/s-f10-l10-loyalty-card-and-gift-cards-u23-store-manager-phone-light.png) | ![Listed, U23, view Mine, dark](../../images/lists/s-f10-l10-loyalty-card-and-gift-cards-u23-store-manager-phone-dark.png) |
| Listed, U52, view Mine | desktop | ![Listed, U52, view Mine, light](../../images/lists/s-f10-l10-loyalty-card-and-gift-cards-u52-beautician-desktop-light.png) | ![Listed, U52, view Mine, dark](../../images/lists/s-f10-l10-loyalty-card-and-gift-cards-u52-beautician-desktop-dark.png) |
| Listed, U52, view Mine | phone | ![Listed, U52, view Mine, light](../../images/lists/s-f10-l10-loyalty-card-and-gift-cards-u52-beautician-phone-light.png) | ![Listed, U52, view Mine, dark](../../images/lists/s-f10-l10-loyalty-card-and-gift-cards-u52-beautician-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Point of sale (plugin) › Loyalty card and gift cards](README.md) |
| Workspaces | [U17](../../../../04-ux/views/u17-cashier/workspace.md), [U09](../../../../04-ux/views/u09-customer/workspace.md), [U23](../../../../04-ux/views/u23-store-manager/workspace.md), [U52](../../../../04-ux/views/u52-beautician/workspace.md) |
| Flows | [FL-F10-03](../../flows/fl-f10-03-after-sales.md) |

## Open questions

None.

---

⬅️ [S-F10-L09 Combos](s-f10-l09-combos.md) · ⬆️ [Up](README.md) ·
➡️ [S-F10-L11 Floor and tables](s-f10-l11-floor-and-tables.md)
