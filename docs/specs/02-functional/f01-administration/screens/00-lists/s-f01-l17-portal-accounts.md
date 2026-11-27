🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛡️ [F1 Administration](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: Administration menu](README.md) ›
🗂️ S-F1-L17 Portal accounts

# 🗂️ S-F1-L17 Portal accounts

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |
| [U10 Supplier](../../../../01-users/personas/u10-supplier.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U12: their use cases only read these records, inside a screen of the use case, so they open them
from there (D493).

## Purpose

The aggregated list of every [E-F1-17 Portal account](../../data/e-f01-17-portal-account.md) the user may see: to find,
filter, total and act on many portal accounts at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Administration › Portal accounts, in the capability's menu (D495).
- **Workspaces:** 3 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "portal accounts" offers this view.
- **AI assistant:** "show the portal accounts that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Portal accounts    Administration › Portal accounts   [+ New]                                                |
| [count] [Blocked] [new this month]   [chart: count by state]                                                 |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] EMAIL   STATUS   LAST SIGN-IN   TWO-FACTOR                                           |
| status            | [ ] ...                                                  Open >                          |
| two-factor        | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Email | email | text | yes |
| Status | status | badge | yes |
| Last sign-in | last sign-in | date and time | yes |
| Two-factor | two-factor | yes or no | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Invited, Active, Blocked, Deactivated | the visible rows (D488) |
| Status | Invited, Active, Blocked, Deactivated | the visible rows (D488) |
| Two-factor | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: portal accounts link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Blocked.
- New this month, by last sign-in.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New portal account | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change status | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- two-factor: editable in its cell unless the record's state locks it.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| email | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| last sign-in | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F1-19 Portal accounts](../12-portal-accounts-and-integrations/s-f01-19-portal-accounts.md).

The records also show on:
[S-F2-20 Portal settings](../../../f02-no-code-configuration/screens/09-portals-and-offline-forms/s-f02-20-portal-settings.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 portal accounts of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no portal account the user may see yet, with the create action when allowed.
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
| Listed, U07, view Needs attention | desktop | ![Listed, U07, view Needs attention, light](../../images/lists/s-f01-l17-portal-accounts-u07-administrator-desktop-light.png) | ![Listed, U07, view Needs attention, dark](../../images/lists/s-f01-l17-portal-accounts-u07-administrator-desktop-dark.png) |
| Listed, U07, view Needs attention | phone | ![Listed, U07, view Needs attention, light](../../images/lists/s-f01-l17-portal-accounts-u07-administrator-phone-light.png) | ![Listed, U07, view Needs attention, dark](../../images/lists/s-f01-l17-portal-accounts-u07-administrator-phone-dark.png) |
| Listed, U09, view All | desktop | ![Listed, U09, view All, light](../../images/lists/s-f01-l17-portal-accounts-u09-customer-desktop-light.png) | ![Listed, U09, view All, dark](../../images/lists/s-f01-l17-portal-accounts-u09-customer-desktop-dark.png) |
| Listed, U09, view All | phone | ![Listed, U09, view All, light](../../images/lists/s-f01-l17-portal-accounts-u09-customer-phone-light.png) | ![Listed, U09, view All, dark](../../images/lists/s-f01-l17-portal-accounts-u09-customer-phone-dark.png) |
| Listed, U10, view All | desktop | ![Listed, U10, view All, light](../../images/lists/s-f01-l17-portal-accounts-u10-supplier-desktop-light.png) | ![Listed, U10, view All, dark](../../images/lists/s-f01-l17-portal-accounts-u10-supplier-desktop-dark.png) |
| Listed, U10, view All | phone | ![Listed, U10, view All, light](../../images/lists/s-f01-l17-portal-accounts-u10-supplier-phone-light.png) | ![Listed, U10, view All, dark](../../images/lists/s-f01-l17-portal-accounts-u10-supplier-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Administration › Portal accounts](README.md) |
| Workspaces | [U07](../../../../04-ux/views/u07-administrator/workspace.md), [U09](../../../../04-ux/views/u09-customer/workspace.md), [U10](../../../../04-ux/views/u10-supplier/workspace.md) |
| Flows | [FL-F1-12](../../flows/fl-f01-12-portal-accounts-and-integrations.md), [FL-F16-05](../../../f16-customer-support-agents/flows/fl-f16-05-customer-side.md), [FL-F2-09](../../../f02-no-code-configuration/flows/fl-f02-09-portals-and-offline-forms.md), [FL-F4-12](../../../f04-meetings/flows/fl-f04-12-rooms-and-client-video.md), [FL-F6-02](../../../f06-customers-and-sales/flows/fl-f06-02-quote-to-order.md), [FL-F7-01](../../../f07-purchasing-and-stock/flows/fl-f07-01-procure.md), [FL-F9-11](../../../f09-hr-and-projects/flows/fl-f09-11-capacity-rounds-and-partners.md), [FL-SC03-05](../../../../08-sectors/sc03-services/flows/fl-sc03-05-client-and-people.md), [FL-SC07-06](../../../../08-sectors/sc07-transport/flows/fl-sc07-06-logistics-for-clients.md), [FL-SC10-06](../../../../08-sectors/sc10-real-estate/flows/fl-sc10-06-portal-and-assistant.md), [FL-SC11-02](../../../../08-sectors/sc11-professional-firms/flows/fl-sc11-02-matters-and-documents.md), [FL-SC14-06](../../../../08-sectors/sc14-it-and-software/flows/fl-sc14-06-portal-and-metrics.md), [FL-SC15-02](../../../../08-sectors/sc15-wholesale-and-distribution/flows/fl-sc15-02-orders.md) |

## Open questions

None.

---

⬅️ [S-F1-L16 Access review campaigns](s-f01-l16-access-review-campaigns.md) · ⬆️ [Up](README.md) ·
➡️ [S-F1-L18 API tokens](s-f01-l18-api-tokens.md)
