🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🌐 [F18 Hosted websites and domains (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Hosted websites and domains (hosted edition) menu](README.md) › 🗂️ S-F18-L16 Spam holds

# 🗂️ S-F18-L16 Spam holds

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F18-16 Spam hold](../../data/e-f18-16-spam-hold.md) the user may see: to find, filter,
total and act on many spam holds at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Hosted websites and domains (hosted edition) › Spam holds, in the capability's menu (D495).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "spam holds" offers this view.
- **AI assistant:** "show the spam holds that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Spam holds    Hosted websites and domains (hosted edition) › Spam holds   [+ New]                            |
| [count] [new this month]   [chart: count by state]                                                           |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] FORM   STATE   RECEIVED   REASON   DECISION                                          |
| form              | [ ] ...                                                  Open >                          |
| reason            | [ ] ...                                                  Open >                          |
| decision          | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Form | form | link to the record | yes |
| State | state | badge: Held, Released, Deleted | yes |
| Received | received | date and time | yes |
| Reason | reason | text | yes |
| Decision | decision | text | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Held, Released, Deleted | the visible rows (D488) |
| Form | each linked form | the visible rows (D488) |
| Reason | each value | the visible rows (D488) |
| Decision | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Spam holds of a chosen form, or of the forms that match a filter.
- From the other side: the forms that have spam holds, or none.

## KPI strip

- Count of the visible rows.
- New this month, by received.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Open: Held, Released.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New spam hold | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- received: editable in its cell unless the record's state locks it.
- reason: editable in its cell unless the record's state locks it.
- decision: editable in its cell unless the record's state locks it.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| content | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F18-04 Contact page](../01-build-the-site/s-f18-04-contact-page.md).

The records also show on: [S-F18-24 Form protection](../01-build-the-site/s-f18-24-form-protection.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 spam holds of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no spam hold the user may see yet, with the create action when allowed.
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
| Listed, U12, view Open: Held, Released | desktop | ![Listed, U12, view Open: Held, Released, light](../../images/lists/s-f18-l16-spam-holds-u12-marketing-desktop-light.png) | ![Listed, U12, view Open: Held, Released, dark](../../images/lists/s-f18-l16-spam-holds-u12-marketing-desktop-dark.png) |
| Listed, U12, view Open: Held, Released | phone | ![Listed, U12, view Open: Held, Released, light](../../images/lists/s-f18-l16-spam-holds-u12-marketing-phone-light.png) | ![Listed, U12, view Open: Held, Released, dark](../../images/lists/s-f18-l16-spam-holds-u12-marketing-phone-dark.png) |
| Listed, U09, view Open: Held, Released | desktop | ![Listed, U09, view Open: Held, Released, light](../../images/lists/s-f18-l16-spam-holds-u09-customer-desktop-light.png) | ![Listed, U09, view Open: Held, Released, dark](../../images/lists/s-f18-l16-spam-holds-u09-customer-desktop-dark.png) |
| Listed, U09, view Open: Held, Released | phone | ![Listed, U09, view Open: Held, Released, light](../../images/lists/s-f18-l16-spam-holds-u09-customer-phone-light.png) | ![Listed, U09, view Open: Held, Released, dark](../../images/lists/s-f18-l16-spam-holds-u09-customer-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Hosted websites and domains (hosted edition) › Spam holds](README.md) |
| Workspaces | [U12](../../../../04-ux/views/u12-marketing/workspace.md), [U09](../../../../04-ux/views/u09-customer/workspace.md) |
| Flows | [FL-F18-01](../../flows/fl-f18-01-build-the-site.md) |

## Open questions

None.

---

⬅️ [S-F18-L15 Mailboxes](s-f18-l15-mailboxes.md) · ⬆️ [Up](README.md) ·
➡️ [S-F18-L17 Sector templates](s-f18-l17-sector-templates.md)
