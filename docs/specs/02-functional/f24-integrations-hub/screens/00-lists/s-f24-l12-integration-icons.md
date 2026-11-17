🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔌 [F24 Integrations hub](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: Integrations hub menu](README.md) ›
🗂️ S-F24-L12 Integration icons

# 🗂️ S-F24-L12 Integration icons

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U47 simple-ERP maintainer](../../../../01-users/personas/u47-simple-erp-maintainer.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F24-12 Integration icon](../../data/e-f24-12-integration-icon.md) the user may see: to
find, filter, total and act on many integration icons at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Integrations hub › Integration icons, in the capability's menu (D495).
- **Workspaces:** 3 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "integration icons" offers this view.
- **AI assistant:** "show the integration icons that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Integration icons    Integrations hub › Integration icons   [+ New]                                          |
| [count] [new this month]   [chart: count by state]                                                           |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] CONNECTOR   STATE   BRAND TERMS   CHECKED                                            |
| connector         | [ ] ...                                                  Open >                          |
| brand terms       | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Connector | connector | link to the record | yes |
| State | state | badge: Proposed, Approved, Replaced, Withdrawn | yes |
| Brand terms | brand terms | link to the record | yes |
| Checked | checked | date | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Proposed, Approved, Replaced, Withdrawn | the visible rows (D488) |
| Connector | each linked connector | the visible rows (D488) |
| Brand terms | each linked brand terms | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Integration icons of a chosen brand terms, or of the brand terms that match a filter.
- From the other side: the brand terms that have integration icons, or none.
- Integration icons of a chosen connector, or of the connectors that match a filter.
- From the other side: the connectors that have integration icons, or none.

## KPI strip

- Count of the visible rows.
- New this month, by checked.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Open: Proposed, Approved, Replaced.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New integration icon | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- checked: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F24-01 Catalogue](../01-find-and-connect/s-f24-01-catalogue.md).

The records also show on: [S-F24-02 Connect](../01-find-and-connect/s-f24-02-connect.md),
[S-F24-10 CRM sync](../03-crm-and-ats/s-f24-10-crm-sync.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 integration icons of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no integration icon the user may see yet, with the create action when allowed.
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
| Listed, U07, view Open: Proposed, Approved, Replaced | desktop | ![Listed, U07, view Open: Proposed, Approved, Replaced, light](../../images/lists/s-f24-l12-integration-icons-u07-administrator-desktop-light.png) | ![Listed, U07, view Open: Proposed, Approved, Replaced, dark](../../images/lists/s-f24-l12-integration-icons-u07-administrator-desktop-dark.png) |
| Listed, U07, view Open: Proposed, Approved, Replaced | phone | ![Listed, U07, view Open: Proposed, Approved, Replaced, light](../../images/lists/s-f24-l12-integration-icons-u07-administrator-phone-light.png) | ![Listed, U07, view Open: Proposed, Approved, Replaced, dark](../../images/lists/s-f24-l12-integration-icons-u07-administrator-phone-dark.png) |
| Listed, U13, view Open: Proposed, Approved, Replaced | desktop | ![Listed, U13, view Open: Proposed, Approved, Replaced, light](../../images/lists/s-f24-l12-integration-icons-u13-owner-desktop-light.png) | ![Listed, U13, view Open: Proposed, Approved, Replaced, dark](../../images/lists/s-f24-l12-integration-icons-u13-owner-desktop-dark.png) |
| Listed, U13, view Open: Proposed, Approved, Replaced | phone | ![Listed, U13, view Open: Proposed, Approved, Replaced, light](../../images/lists/s-f24-l12-integration-icons-u13-owner-phone-light.png) | ![Listed, U13, view Open: Proposed, Approved, Replaced, dark](../../images/lists/s-f24-l12-integration-icons-u13-owner-phone-dark.png) |
| Listed, U47, view Open: Proposed, Approved, Replaced | desktop | ![Listed, U47, view Open: Proposed, Approved, Replaced, light](../../images/lists/s-f24-l12-integration-icons-u47-simple-erp-maintainer-desktop-light.png) | ![Listed, U47, view Open: Proposed, Approved, Replaced, dark](../../images/lists/s-f24-l12-integration-icons-u47-simple-erp-maintainer-desktop-dark.png) |
| Listed, U47, view Open: Proposed, Approved, Replaced | phone | ![Listed, U47, view Open: Proposed, Approved, Replaced, light](../../images/lists/s-f24-l12-integration-icons-u47-simple-erp-maintainer-phone-light.png) | ![Listed, U47, view Open: Proposed, Approved, Replaced, dark](../../images/lists/s-f24-l12-integration-icons-u47-simple-erp-maintainer-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Integrations hub › Integration icons](README.md) |
| Workspaces | [U07](../../../../04-ux/views/u07-administrator/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md), [U47](../../../../04-ux/views/u47-simple-erp-maintainer/workspace.md) |
| Flows | [FL-F24-01](../../flows/fl-f24-01-find-and-connect.md), [FL-F24-05](../../flows/fl-f24-05-keep-the-catalogue.md), [FL-F24-06](../../flows/fl-f24-06-business-tools.md), [FL-F9-14](../../../f09-hr-and-projects/flows/fl-f09-14-source-candidates-on-linkedin.md) |

## Open questions

None.

---

⬅️ [S-F24-L11 Connector categories](s-f24-l11-connector-categories.md) · ⬆️ [Up](README.md) ·
➡️ [S-F24-L13 Webhook subscriptions](s-f24-l13-webhook-subscriptions.md)
