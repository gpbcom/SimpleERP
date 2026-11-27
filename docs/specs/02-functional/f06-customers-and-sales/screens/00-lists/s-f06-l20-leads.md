🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛒 [F6 Customers and sales](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Customers and sales menu](README.md) › 🗂️ S-F6-L20 Leads

# 🗂️ S-F6-L20 Leads

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U03 Sales](../../../../01-users/personas/u03-sales.md) | as the permissions row "Leads, pipeline": ✅ own | actions as [permissions](../../permissions.md) gives them |
| [U16 Office worker](../../../../01-users/personas/u16-office-worker.md) | as the permissions row "Leads, pipeline": read the leads made from inbox messages (UC-F5-05) | actions as [permissions](../../permissions.md) gives them |
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | as the permissions row "Leads, pipeline": the leads of their own form answers (UC-F5-19) | actions as [permissions](../../permissions.md) gives them |
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | as the permissions row "Leads, pipeline": ✅ team | actions as [permissions](../../permissions.md) gives them |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U51 Reseller partner](../../../../01-users/personas/u51-reseller-partner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F6-20 Lead](../../data/e-f06-20-lead.md) the user may see: to find, filter, total and
act on many leads at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Customers and sales › Leads, in the capability's menu (D495).
- **Workspaces:** 7 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "leads" offers this view.
- **AI assistant:** "show the leads that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Leads    Customers and sales › Leads   [+ New]                                                               |
| [count]   [chart: count by state]                                                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] LEAD   STATE                                                                         |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Lead | the record's title | text | yes |
| State | state | badge: Active | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Active | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: leads link to no other record type in their fields.

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
| New lead | header | the personas whose roles may create it | the record's own page (Row opens) |
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

None: no personal data and no secret among its fields.

## Row opens

Open › goes to
[S-F5-13 Social leads](../../../f05-social-media/screens/05-benchmark-additions/s-f05-13-social-leads.md).

The records also show on:
[S-F5-05 Social inbox](../../../f05-social-media/screens/03-inbox-and-statistics/s-f05-05-social-inbox.md),
[S-F5-19 Landing page editor](../../../f05-social-media/screens/08-pages-forms-surveys-and-whatsapp/s-f05-19-landing-page-editor.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 leads of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no lead the user may see yet, with the create action when allowed.
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
| Listed, U12, view All | desktop | ![Listed, U12, view All, light](../../images/lists/s-f06-l20-leads-u12-marketing-desktop-light.png) | ![Listed, U12, view All, dark](../../images/lists/s-f06-l20-leads-u12-marketing-desktop-dark.png) |
| Listed, U12, view All | phone | ![Listed, U12, view All, light](../../images/lists/s-f06-l20-leads-u12-marketing-phone-light.png) | ![Listed, U12, view All, dark](../../images/lists/s-f06-l20-leads-u12-marketing-phone-dark.png) |
| Listed, U03, view All | desktop | ![Listed, U03, view All, light](../../images/lists/s-f06-l20-leads-u03-sales-desktop-light.png) | ![Listed, U03, view All, dark](../../images/lists/s-f06-l20-leads-u03-sales-desktop-dark.png) |
| Listed, U03, view All | phone | ![Listed, U03, view All, light](../../images/lists/s-f06-l20-leads-u03-sales-phone-light.png) | ![Listed, U03, view All, dark](../../images/lists/s-f06-l20-leads-u03-sales-phone-dark.png) |
| Listed, U16, view All | desktop | ![Listed, U16, view All, light](../../images/lists/s-f06-l20-leads-u16-office-worker-desktop-light.png) | ![Listed, U16, view All, dark](../../images/lists/s-f06-l20-leads-u16-office-worker-desktop-dark.png) |
| Listed, U16, view All | phone | ![Listed, U16, view All, light](../../images/lists/s-f06-l20-leads-u16-office-worker-phone-light.png) | ![Listed, U16, view All, dark](../../images/lists/s-f06-l20-leads-u16-office-worker-phone-dark.png) |
| Listed, U09, view All | desktop | ![Listed, U09, view All, light](../../images/lists/s-f06-l20-leads-u09-customer-desktop-light.png) | ![Listed, U09, view All, dark](../../images/lists/s-f06-l20-leads-u09-customer-desktop-dark.png) |
| Listed, U09, view All | phone | ![Listed, U09, view All, light](../../images/lists/s-f06-l20-leads-u09-customer-phone-light.png) | ![Listed, U09, view All, dark](../../images/lists/s-f06-l20-leads-u09-customer-phone-dark.png) |
| Listed, U02, view All | desktop | ![Listed, U02, view All, light](../../images/lists/s-f06-l20-leads-u02-manager-desktop-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-f06-l20-leads-u02-manager-desktop-dark.png) |
| Listed, U02, view All | phone | ![Listed, U02, view All, light](../../images/lists/s-f06-l20-leads-u02-manager-phone-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-f06-l20-leads-u02-manager-phone-dark.png) |
| Listed, U13, view All | desktop | ![Listed, U13, view All, light](../../images/lists/s-f06-l20-leads-u13-owner-desktop-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f06-l20-leads-u13-owner-desktop-dark.png) |
| Listed, U13, view All | phone | ![Listed, U13, view All, light](../../images/lists/s-f06-l20-leads-u13-owner-phone-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f06-l20-leads-u13-owner-phone-dark.png) |
| Listed, U51, view All | desktop | ![Listed, U51, view All, light](../../images/lists/s-f06-l20-leads-u51-reseller-partner-desktop-light.png) | ![Listed, U51, view All, dark](../../images/lists/s-f06-l20-leads-u51-reseller-partner-desktop-dark.png) |
| Listed, U51, view All | phone | ![Listed, U51, view All, light](../../images/lists/s-f06-l20-leads-u51-reseller-partner-phone-light.png) | ![Listed, U51, view All, dark](../../images/lists/s-f06-l20-leads-u51-reseller-partner-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Customers and sales › Leads](README.md) |
| Workspaces | [U12](../../../../04-ux/views/u12-marketing/workspace.md), [U03](../../../../04-ux/views/u03-sales/workspace.md), [U16](../../../../04-ux/views/u16-office-worker/workspace.md), [U09](../../../../04-ux/views/u09-customer/workspace.md), [U02](../../../../04-ux/views/u02-manager/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md), [U51](../../../../04-ux/views/u51-reseller-partner/workspace.md) |
| Flows | [FL-F5-03](../../../f05-social-media/flows/fl-f05-03-inbox-and-statistics.md), [FL-F5-05](../../../f05-social-media/flows/fl-f05-05-benchmark-additions.md), [FL-F5-08](../../../f05-social-media/flows/fl-f05-08-pages-forms-surveys-and-whatsapp.md), [FL-F6-01](../../flows/fl-f06-01-lead-to-quote.md), [FL-F6-05](../../flows/fl-f06-05-benchmark-additions.md) |

## Open questions

None.

---

⬅️ [S-F6-L19 Commission lines](s-f06-l19-commission-lines.md) · ⬆️ [Up](README.md) ·
➡️ [S-F6-L21 Payment reminders](s-f06-l21-payment-reminders.md)
