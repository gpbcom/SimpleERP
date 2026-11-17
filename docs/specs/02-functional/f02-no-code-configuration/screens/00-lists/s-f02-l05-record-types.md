🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔧 [F2 No-code configuration](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: No-code configuration menu](README.md) › 🗂️ S-F2-L05 Record types

# 🗂️ S-F2-L05 Record types

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | as the permissions row "Custom fields, statuses, forms, record types (UC-F2-01 to 04)": yes | actions as [permissions](../../permissions.md) gives them |
| [U28 Hotel receptionist](../../../../01-users/personas/u28-hotel-receptionist.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U33 Medical secretary](../../../../01-users/personas/u33-medical-secretary.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U38 Training coordinator](../../../../01-users/personas/u38-training-coordinator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U43 Event producer](../../../../01-users/personas/u43-event-producer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U13, U16: their use cases only read these records, inside a screen of the use case, so they open
them from there (D493).

## Purpose

The aggregated list of every [E-F2-05 Record type](../../data/e-f02-05-record-type.md) the user may see: to find,
filter, total and act on many record types at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** No-code configuration › Record types, in the capability's menu (D495).
- **Workspaces:** 6 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "record types" offers this view.
- **AI assistant:** "show the record types that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Record types    No-code configuration › Record types   [+ New]                                               |
| [count] [Draft]   [chart: count by state]                                                                    |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] NAME   STATUS   MODEL   SOURCE   OPEN TO CUSTOM FIELDS                               |
| source            | [ ] ...                                                  Open >                          |
| open to custom fi | [ ] ...                                                  Open >                          |
| model             | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Name | name | text | yes |
| Status | status | badge | yes |
| Model | model | text | yes |
| Source | source | text | yes |
| Open to custom fields | open to custom fields | yes or no | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Draft, Live, Archived | the visible rows (D488) |
| Source | each value | the visible rows (D488) |
| Open to custom fields | each value | the visible rows (D488) |
| Model | each value | the visible rows (D488) |
| Status | Draft, Live, Archived | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Record types of a chosen model, or of the models that match a filter.
- From the other side: the models that have record types, or none.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Draft.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Open: Draft, Live.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New record type | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change status | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- source: editable in its cell unless the record's state locks it.
- open to custom fields: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F2-01 Record type editor](../01-configure-a-record-type/s-f02-01-record-type-editor.md).

The records also show on: [S-F2-05 Record type gallery](../01-configure-a-record-type/s-f02-05-record-type-gallery.md),
[S-F1-19 Portal accounts](../../../f01-administration/screens/12-portal-accounts-and-integrations/s-f01-19-portal-accounts.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 record types of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no record type the user may see yet, with the create action when allowed.
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
| Listed, U07, view Needs attention | desktop | ![Listed, U07, view Needs attention, light](../../images/lists/s-f02-l05-record-types-u07-administrator-desktop-light.png) | ![Listed, U07, view Needs attention, dark](../../images/lists/s-f02-l05-record-types-u07-administrator-desktop-dark.png) |
| Listed, U07, view Needs attention | phone | ![Listed, U07, view Needs attention, light](../../images/lists/s-f02-l05-record-types-u07-administrator-phone-light.png) | ![Listed, U07, view Needs attention, dark](../../images/lists/s-f02-l05-record-types-u07-administrator-phone-dark.png) |
| Listed, U28, view Needs attention | desktop | ![Listed, U28, view Needs attention, light](../../images/lists/s-f02-l05-record-types-u28-hotel-receptionist-desktop-light.png) | ![Listed, U28, view Needs attention, dark](../../images/lists/s-f02-l05-record-types-u28-hotel-receptionist-desktop-dark.png) |
| Listed, U28, view Needs attention | phone | ![Listed, U28, view Needs attention, light](../../images/lists/s-f02-l05-record-types-u28-hotel-receptionist-phone-light.png) | ![Listed, U28, view Needs attention, dark](../../images/lists/s-f02-l05-record-types-u28-hotel-receptionist-phone-dark.png) |
| Listed, U33, view Open: Draft, Live | desktop | ![Listed, U33, view Open: Draft, Live, light](../../images/lists/s-f02-l05-record-types-u33-medical-secretary-desktop-light.png) | ![Listed, U33, view Open: Draft, Live, dark](../../images/lists/s-f02-l05-record-types-u33-medical-secretary-desktop-dark.png) |
| Listed, U33, view Open: Draft, Live | phone | ![Listed, U33, view Open: Draft, Live, light](../../images/lists/s-f02-l05-record-types-u33-medical-secretary-phone-light.png) | ![Listed, U33, view Open: Draft, Live, dark](../../images/lists/s-f02-l05-record-types-u33-medical-secretary-phone-dark.png) |
| Listed, U38, view Needs attention | desktop | ![Listed, U38, view Needs attention, light](../../images/lists/s-f02-l05-record-types-u38-training-coordinator-desktop-light.png) | ![Listed, U38, view Needs attention, dark](../../images/lists/s-f02-l05-record-types-u38-training-coordinator-desktop-dark.png) |
| Listed, U38, view Needs attention | phone | ![Listed, U38, view Needs attention, light](../../images/lists/s-f02-l05-record-types-u38-training-coordinator-phone-light.png) | ![Listed, U38, view Needs attention, dark](../../images/lists/s-f02-l05-record-types-u38-training-coordinator-phone-dark.png) |
| Listed, U43, view Needs attention | desktop | ![Listed, U43, view Needs attention, light](../../images/lists/s-f02-l05-record-types-u43-event-producer-desktop-light.png) | ![Listed, U43, view Needs attention, dark](../../images/lists/s-f02-l05-record-types-u43-event-producer-desktop-dark.png) |
| Listed, U43, view Needs attention | phone | ![Listed, U43, view Needs attention, light](../../images/lists/s-f02-l05-record-types-u43-event-producer-phone-light.png) | ![Listed, U43, view Needs attention, dark](../../images/lists/s-f02-l05-record-types-u43-event-producer-phone-dark.png) |
| Listed, U09, view Open: Draft, Live | desktop | ![Listed, U09, view Open: Draft, Live, light](../../images/lists/s-f02-l05-record-types-u09-customer-desktop-light.png) | ![Listed, U09, view Open: Draft, Live, dark](../../images/lists/s-f02-l05-record-types-u09-customer-desktop-dark.png) |
| Listed, U09, view Open: Draft, Live | phone | ![Listed, U09, view Open: Draft, Live, light](../../images/lists/s-f02-l05-record-types-u09-customer-phone-light.png) | ![Listed, U09, view Open: Draft, Live, dark](../../images/lists/s-f02-l05-record-types-u09-customer-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [No-code configuration › Record types](README.md) |
| Workspaces | [U07](../../../../04-ux/views/u07-administrator/workspace.md), [U28](../../../../04-ux/views/u28-hotel-receptionist/workspace.md), [U33](../../../../04-ux/views/u33-medical-secretary/workspace.md), [U38](../../../../04-ux/views/u38-training-coordinator/workspace.md), [U43](../../../../04-ux/views/u43-event-producer/workspace.md), [U09](../../../../04-ux/views/u09-customer/workspace.md) |
| Flows | [FL-F2-01](../../flows/fl-f02-01-configure-a-record-type.md), [FL-F2-08](../../flows/fl-f02-08-views-and-bookings.md), [FL-F2-09](../../flows/fl-f02-09-portals-and-offline-forms.md), [FL-F2-11](../../flows/fl-f02-11-rights-translations-and-approvals.md) |

## Open questions

None.

---

⬅️ [S-F2-L04 List views](s-f02-l04-list-views.md) · ⬆️ [Up](README.md) ·
➡️ [S-F2-L06 Document templates](s-f02-l06-document-templates.md)
