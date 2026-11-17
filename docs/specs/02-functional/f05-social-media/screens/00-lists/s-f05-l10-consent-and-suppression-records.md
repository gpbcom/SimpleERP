🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📣 [F5 Social media and marketing](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Social media and marketing menu](README.md) › 🗂️ S-F5-L10 Consent and suppression records

# 🗂️ S-F5-L10 Consent and suppression records

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U03, U16, U52, U53: their use cases only read these records, inside a screen of the use case, so
they open them from there (D493).

## Purpose

The aggregated list of every
[E-F5-10 Consent and suppression record](../../data/e-f05-10-consent-and-suppression-record.md) the user may see: to
find, filter, total and act on many consent and suppression records at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Social media and marketing › Consent and suppression records, in the capability's menu (D495).
- **Workspaces:** 4 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "consent and suppression records" offers this view.
- **AI assistant:** "show the consent and suppression records that need attention" opens it with the filter as editable
  chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Consent and suppression records    Social media and marketing › Consent and suppression records   [+ New]    |
| [count] [new this month]   [chart: count by state]                                                           |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] CONTACT   STATUS   PROOF   CHANNEL                                                   |
| contact           | [ ] ...                                                  Open >                          |
| channel           | [ ] ...                                                  Open >                          |
| status            | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Contact | contact | person's name | yes |
| Status | status | badge | yes |
| Proof | proof | date | yes |
| Channel | channel | label | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Given, Withdrawn, Suppressed | the visible rows (D488) |
| Contact | each person, the user first | the visible rows (D488) |
| Channel | email, SMS, WhatsApp | the visible rows (D488) |
| Status | Given, Withdrawn, Suppressed | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: consent and suppression records link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- New this month, by proof.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Mine: contact.
- Open: Given, Suppressed.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New consent and suppression record | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change status | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Assign | bulk bar | the personas whose roles may assign | sets the contact; audited |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- channel: editable in its cell unless the record's state locks it.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| contact | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| proof | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F5-15 Consent register](../06-audiences-consent-and-journeys/s-f05-15-consent-register.md).

The records also show on: [S-F5-14 Segments](../06-audiences-consent-and-journeys/s-f05-14-segments.md),
[S-F5-16 Deliverability](../06-audiences-consent-and-journeys/s-f05-16-deliverability.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 consent and suppression records of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no consent and suppression record the user may see yet, with the create action when allowed.
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
| Listed, U12, view Mine: contact | desktop | ![Listed, U12, view Mine: contact, light](../../images/lists/s-f05-l10-consent-and-suppression-records-u12-marketing-desktop-light.png) | ![Listed, U12, view Mine: contact, dark](../../images/lists/s-f05-l10-consent-and-suppression-records-u12-marketing-desktop-dark.png) |
| Listed, U12, view Mine: contact | phone | ![Listed, U12, view Mine: contact, light](../../images/lists/s-f05-l10-consent-and-suppression-records-u12-marketing-phone-light.png) | ![Listed, U12, view Mine: contact, dark](../../images/lists/s-f05-l10-consent-and-suppression-records-u12-marketing-phone-dark.png) |
| Listed, U09, view Mine: contact | desktop | ![Listed, U09, view Mine: contact, light](../../images/lists/s-f05-l10-consent-and-suppression-records-u09-customer-desktop-light.png) | ![Listed, U09, view Mine: contact, dark](../../images/lists/s-f05-l10-consent-and-suppression-records-u09-customer-desktop-dark.png) |
| Listed, U09, view Mine: contact | phone | ![Listed, U09, view Mine: contact, light](../../images/lists/s-f05-l10-consent-and-suppression-records-u09-customer-phone-light.png) | ![Listed, U09, view Mine: contact, dark](../../images/lists/s-f05-l10-consent-and-suppression-records-u09-customer-phone-dark.png) |
| Listed, U13, view Open: Given, Suppressed | desktop | ![Listed, U13, view Open: Given, Suppressed, light](../../images/lists/s-f05-l10-consent-and-suppression-records-u13-owner-desktop-light.png) | ![Listed, U13, view Open: Given, Suppressed, dark](../../images/lists/s-f05-l10-consent-and-suppression-records-u13-owner-desktop-dark.png) |
| Listed, U13, view Open: Given, Suppressed | phone | ![Listed, U13, view Open: Given, Suppressed, light](../../images/lists/s-f05-l10-consent-and-suppression-records-u13-owner-phone-light.png) | ![Listed, U13, view Open: Given, Suppressed, dark](../../images/lists/s-f05-l10-consent-and-suppression-records-u13-owner-phone-dark.png) |
| Listed, U07, view Open: Given, Suppressed | desktop | ![Listed, U07, view Open: Given, Suppressed, light](../../images/lists/s-f05-l10-consent-and-suppression-records-u07-administrator-desktop-light.png) | ![Listed, U07, view Open: Given, Suppressed, dark](../../images/lists/s-f05-l10-consent-and-suppression-records-u07-administrator-desktop-dark.png) |
| Listed, U07, view Open: Given, Suppressed | phone | ![Listed, U07, view Open: Given, Suppressed, light](../../images/lists/s-f05-l10-consent-and-suppression-records-u07-administrator-phone-light.png) | ![Listed, U07, view Open: Given, Suppressed, dark](../../images/lists/s-f05-l10-consent-and-suppression-records-u07-administrator-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Social media and marketing › Consent and suppression records](README.md) |
| Workspaces | [U12](../../../../04-ux/views/u12-marketing/workspace.md), [U09](../../../../04-ux/views/u09-customer/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md), [U07](../../../../04-ux/views/u07-administrator/workspace.md) |
| Flows | [FL-F5-05](../../flows/fl-f05-05-benchmark-additions.md), [FL-F5-06](../../flows/fl-f05-06-audiences-consent-and-journeys.md), [FL-F5-08](../../flows/fl-f05-08-pages-forms-surveys-and-whatsapp.md), [FL-SC02-04](../../../../08-sectors/sc02-retail/flows/fl-sc02-04-customers-and-staff.md), [FL-SC04-05](../../../../08-sectors/sc04-home-care/flows/fl-sc04-05-people-and-quality.md), [FL-SC08-06](../../../../08-sectors/sc08-non-profit/flows/fl-sc08-06-accounts-and-data.md), [FL-SC09-01](../../../../08-sectors/sc09-health-practices/flows/fl-sc09-01-appointments.md), [FL-SC15-05](../../../../08-sectors/sc15-wholesale-and-distribution/flows/fl-sc15-05-sales-force-and-performance.md), [FL-SC16-04](../../../../08-sectors/sc16-events-and-culture/flows/fl-sc16-04-on-site.md) |

## Open questions

None.

---

⬅️ [S-F5-L09 Contact segments](s-f05-l09-contact-segments.md) · ⬆️ [Up](README.md) ·
➡️ [S-F5-L11 Ticket type and seat maps](s-f05-l11-ticket-type-and-seat-maps.md)
