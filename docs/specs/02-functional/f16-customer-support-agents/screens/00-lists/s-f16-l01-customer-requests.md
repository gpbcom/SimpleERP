🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🎧 [F16 Customer support agents](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Customer support agents menu](README.md) › 🗂️ S-F16-L01 Customer requests

# 🗂️ S-F16-L01 Customer requests

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |
| [U16 Office worker](../../../../01-users/personas/u16-office-worker.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U29 Dispatcher](../../../../01-users/personas/u29-dispatcher.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U25 Care coordinator](../../../../01-users/personas/u25-care-coordinator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U41: their use cases only read these records, inside a screen of the use case, so they open them
from there (D493).

## Purpose

The aggregated list of every [E-F16-01 Customer request](../../data/e-f16-01-customer-request.md) the user may see: to
find, filter, total and act on many customer requests at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Customer support agents › Customer requests, in the capability's menu (D495).
- **Workspaces:** 5 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "customer requests" offers this view.
- **AI assistant:** "show the customer requests that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Customer requests    Customer support agents › Customer requests   [+ New]                                   |
| [count] [Waiting]   [chart: count by state]                                                                  |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| channel           | [ ] CHANNEL   STATE   CUSTOMER   INTENT   JUDGE SCORE                                    |
| customer          | [ ] ...                                                  Open >                          |
| intent            | [ ] ...                                                  Open >                          |
| state             | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Channel | channel | label | yes |
| State | state | badge: New, InProgress, Resolved, Waiting, Escalated | yes |
| Customer | customer | text | yes |
| Intent | intent | text | yes |
| Judge score | judge score | number, right-aligned | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| Channel | email, portal, form, chat, social, phone | the visible rows (D488) |
| Customer | each value | the visible rows (D488) |
| Intent | each value | the visible rows (D488) |
| State | New, InProgress, Resolved, Waiting, Escalated | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Customer requests of a chosen customer, or of the customers that match a filter.
- From the other side: the customers that have customer requests, or none.
- Customer requests of a chosen intent, or of the intents that match a filter.
- From the other side: the intents that have customer requests, or none.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Waiting.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Open: New, InProgress, Waiting.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New customer request | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- judge score: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F16-01 Request inbox](../01-resolve-a-request/s-f16-01-request-inbox.md).

The records also show on: [S-F16-04 Review queue](../03-review-and-monitor/s-f16-04-review-queue.md),
[S-F16-07 Service levels](../04-human-agent-workspace/s-f16-07-service-levels.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 customer requests of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no customer request the user may see yet, with the create action when allowed.
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
| Listed, U09, view Open: New, InProgress, Waiting | desktop | ![Listed, U09, view Open: New, InProgress, Waiting, light](../../images/lists/s-f16-l01-customer-requests-u09-customer-desktop-light.png) | ![Listed, U09, view Open: New, InProgress, Waiting, dark](../../images/lists/s-f16-l01-customer-requests-u09-customer-desktop-dark.png) |
| Listed, U09, view Open: New, InProgress, Waiting | phone | ![Listed, U09, view Open: New, InProgress, Waiting, light](../../images/lists/s-f16-l01-customer-requests-u09-customer-phone-light.png) | ![Listed, U09, view Open: New, InProgress, Waiting, dark](../../images/lists/s-f16-l01-customer-requests-u09-customer-phone-dark.png) |
| Listed, U16, view Open: New, InProgress, Waiting | desktop | ![Listed, U16, view Open: New, InProgress, Waiting, light](../../images/lists/s-f16-l01-customer-requests-u16-office-worker-desktop-light.png) | ![Listed, U16, view Open: New, InProgress, Waiting, dark](../../images/lists/s-f16-l01-customer-requests-u16-office-worker-desktop-dark.png) |
| Listed, U16, view Open: New, InProgress, Waiting | phone | ![Listed, U16, view Open: New, InProgress, Waiting, light](../../images/lists/s-f16-l01-customer-requests-u16-office-worker-phone-light.png) | ![Listed, U16, view Open: New, InProgress, Waiting, dark](../../images/lists/s-f16-l01-customer-requests-u16-office-worker-phone-dark.png) |
| Listed, U02, view Needs attention | desktop | ![Listed, U02, view Needs attention, light](../../images/lists/s-f16-l01-customer-requests-u02-manager-desktop-light.png) | ![Listed, U02, view Needs attention, dark](../../images/lists/s-f16-l01-customer-requests-u02-manager-desktop-dark.png) |
| Listed, U02, view Needs attention | phone | ![Listed, U02, view Needs attention, light](../../images/lists/s-f16-l01-customer-requests-u02-manager-phone-light.png) | ![Listed, U02, view Needs attention, dark](../../images/lists/s-f16-l01-customer-requests-u02-manager-phone-dark.png) |
| Listed, U29, view Needs attention | desktop | ![Listed, U29, view Needs attention, light](../../images/lists/s-f16-l01-customer-requests-u29-dispatcher-desktop-light.png) | ![Listed, U29, view Needs attention, dark](../../images/lists/s-f16-l01-customer-requests-u29-dispatcher-desktop-dark.png) |
| Listed, U29, view Needs attention | phone | ![Listed, U29, view Needs attention, light](../../images/lists/s-f16-l01-customer-requests-u29-dispatcher-phone-light.png) | ![Listed, U29, view Needs attention, dark](../../images/lists/s-f16-l01-customer-requests-u29-dispatcher-phone-dark.png) |
| Listed, U25, view Needs attention | desktop | ![Listed, U25, view Needs attention, light](../../images/lists/s-f16-l01-customer-requests-u25-care-coordinator-desktop-light.png) | ![Listed, U25, view Needs attention, dark](../../images/lists/s-f16-l01-customer-requests-u25-care-coordinator-desktop-dark.png) |
| Listed, U25, view Needs attention | phone | ![Listed, U25, view Needs attention, light](../../images/lists/s-f16-l01-customer-requests-u25-care-coordinator-phone-light.png) | ![Listed, U25, view Needs attention, dark](../../images/lists/s-f16-l01-customer-requests-u25-care-coordinator-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Customer support agents › Customer requests](README.md) |
| Workspaces | [U09](../../../../04-ux/views/u09-customer/workspace.md), [U16](../../../../04-ux/views/u16-office-worker/workspace.md), [U02](../../../../04-ux/views/u02-manager/workspace.md), [U29](../../../../04-ux/views/u29-dispatcher/workspace.md), [U25](../../../../04-ux/views/u25-care-coordinator/workspace.md) |
| Flows | [FL-F16-01](../../flows/fl-f16-01-resolve-a-request.md), [FL-F16-02](../../flows/fl-f16-02-automate-an-intent.md), [FL-F16-03](../../flows/fl-f16-03-review-and-monitor.md), [FL-F16-04](../../flows/fl-f16-04-human-agent-workspace.md), [FL-F16-05](../../flows/fl-f16-05-customer-side.md), [FL-F16-06](../../flows/fl-f16-06-take-in-every-request.md), [FL-F5-03](../../../f05-social-media/flows/fl-f05-03-inbox-and-statistics.md), [FL-SC01-01](../../../../08-sectors/sc01-construction/flows/fl-sc01-01-win-the-work.md), [FL-SC04-01](../../../../08-sectors/sc04-home-care/flows/fl-sc04-01-take-on-a-recipient.md), [FL-SC07-01](../../../../08-sectors/sc07-transport/flows/fl-sc07-01-orders-and-planning.md), [FL-SC14-03](../../../../08-sectors/sc14-it-and-software/flows/fl-sc14-03-support-and-services.md), [FL-SC14-05](../../../../08-sectors/sc14-it-and-software/flows/fl-sc14-05-security-and-data-compliance.md) |

## Open questions

None.

---

⬅️ [S-F16-21 Canned replies](../07-live-chat-voice-and-contracts/s-f16-21-canned-replies.md) · ⬆️ [Up](README.md) ·
➡️ [S-F16-L02 Intents](s-f16-l02-intents.md)
