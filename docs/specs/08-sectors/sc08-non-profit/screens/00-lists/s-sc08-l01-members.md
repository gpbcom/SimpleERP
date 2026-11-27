🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🤲 [SC08 Non-profit association](../../README.md) ›
🖥️ [Screens](../README.md) › 🗂️ [Views: Non-profit association menu](README.md) › 🗂️ S-SC08-L01 Members

# 🗂️ S-SC08-L01 Members

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U31 Treasurer](../../../../01-users/personas/u31-treasurer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-SC08-01 Member](../../data/e-sc08-01-member.md) the user may see: to find, filter, total
and act on many members at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Non-profit association › Members, in the capability's menu (D495).
- **Workspaces:** 4 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "members" offers this view.
- **AI assistant:** "show the members that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Members    Non-profit association › Members   [+ New]                                                        |
| [count]   [chart: count by state]                                                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] CONTACT   STATE   KIND   CONSENTS                                                    |
| contact           | [ ] ...                                                  Open >                          |
| kind              | [ ] ...                                                  Open >                          |
| consents          | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Contact | contact | person's name | yes |
| State | state | badge: Active | yes |
| Kind | kind | date | yes |
| Consents | consents | text | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Active | the visible rows (D488) |
| Contact | each person, the user first | the visible rows (D488) |
| Kind | dates, kind | the visible rows (D488) |
| Consents | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: members link to no other record type in their fields.

## KPI strip

- Count of the visible rows.

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
| New member | header | the personas whose roles may create it | the record's own page (Row opens) |
| Assign | bulk bar | the personas whose roles may assign | sets the contact; audited |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- kind: editable in its cell unless the record's state locks it.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| contact | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| consents | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-SC08-01 Members](../01-members-and-governance/s-sc08-01-members.md).

The records also show on: [S-SC08-17 News](../06-accounts-and-data/s-sc08-17-news.md),
[S-SC08-18 Data rights](../06-accounts-and-data/s-sc08-18-data-rights.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 members of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no member the user may see yet, with the create action when allowed.
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
| Listed, U31, view Mine: contact | desktop | ![Listed, U31, view Mine: contact, light](../../images/lists/s-sc08-l01-members-u31-treasurer-desktop-light.png) | ![Listed, U31, view Mine: contact, dark](../../images/lists/s-sc08-l01-members-u31-treasurer-desktop-dark.png) |
| Listed, U31, view Mine: contact | phone | ![Listed, U31, view Mine: contact, light](../../images/lists/s-sc08-l01-members-u31-treasurer-phone-light.png) | ![Listed, U31, view Mine: contact, dark](../../images/lists/s-sc08-l01-members-u31-treasurer-phone-dark.png) |
| Listed, U09, view Mine: contact | desktop | ![Listed, U09, view Mine: contact, light](../../images/lists/s-sc08-l01-members-u09-customer-desktop-light.png) | ![Listed, U09, view Mine: contact, dark](../../images/lists/s-sc08-l01-members-u09-customer-desktop-dark.png) |
| Listed, U09, view Mine: contact | phone | ![Listed, U09, view Mine: contact, light](../../images/lists/s-sc08-l01-members-u09-customer-phone-light.png) | ![Listed, U09, view Mine: contact, dark](../../images/lists/s-sc08-l01-members-u09-customer-phone-dark.png) |
| Listed, U13, view All | desktop | ![Listed, U13, view All, light](../../images/lists/s-sc08-l01-members-u13-owner-desktop-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-sc08-l01-members-u13-owner-desktop-dark.png) |
| Listed, U13, view All | phone | ![Listed, U13, view All, light](../../images/lists/s-sc08-l01-members-u13-owner-phone-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-sc08-l01-members-u13-owner-phone-dark.png) |
| Listed, U12, view Mine: contact | desktop | ![Listed, U12, view Mine: contact, light](../../images/lists/s-sc08-l01-members-u12-marketing-desktop-light.png) | ![Listed, U12, view Mine: contact, dark](../../images/lists/s-sc08-l01-members-u12-marketing-desktop-dark.png) |
| Listed, U12, view Mine: contact | phone | ![Listed, U12, view Mine: contact, light](../../images/lists/s-sc08-l01-members-u12-marketing-phone-light.png) | ![Listed, U12, view Mine: contact, dark](../../images/lists/s-sc08-l01-members-u12-marketing-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Non-profit association › Members](README.md) |
| Workspaces | [U31](../../../../04-ux/views/u31-treasurer/workspace.md), [U09](../../../../04-ux/views/u09-customer/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md), [U12](../../../../04-ux/views/u12-marketing/workspace.md) |
| Flows | [FL-SC08-01](../../flows/fl-sc08-01-members-and-governance.md), [FL-SC08-06](../../flows/fl-sc08-06-accounts-and-data.md) |

## Open questions

None.

---

⬅️ [S-SC08-24 Peer-to-peer fundraising](../07-foundations-integration-and-federations/s-sc08-24-peer-fundraising.md) ·
⬆️ [Up](README.md) · ➡️ [S-SC08-L02 Dues payments](s-sc08-l02-dues-payments.md)
