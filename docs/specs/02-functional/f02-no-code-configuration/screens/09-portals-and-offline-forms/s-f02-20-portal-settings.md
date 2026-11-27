🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔧 [F2 No-code configuration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F2-09 Portals and offline forms](README.md) › 🖥️ S-F2-20 Portal settings

# 🖥️ S-F2-20 Portal settings

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

Choose how a record type shows on a portal, and preview it as a contact.

## Entry points

A record type › Portal.

## Wireframe

```text
+------------------------------------------------------------------+
| Care log › Portal       Audience [Family contact v]              |
| Fields   [x] Date [x] Carer [x] Tasks done [x] Comment           |
|          [ ] Health notes (not allowed: other person's data)     |
| Lists    [x] Next visits  [ ] Invoices                           |
| Actions  [x] Comment  [ ] Upload                                 |
| Preview as [ Martine Roche v ]          [Preview] [Publish]      |
+------------------------------------------------------------------+
Portal (phone)   Visits of Jeanne Roche
  12 Nov 09:00  Lea R.  wash, meal  "Good mood"   [Comment]
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F2-09 step 1, U07 | desktop | ![FL-F2-09 step 1, U07, light](../../images/09-portals-and-offline-forms/u07-administrator/1-portal-settings-desktop-light.png) | ![FL-F2-09 step 1, U07, dark](../../images/09-portals-and-offline-forms/u07-administrator/1-portal-settings-desktop-dark.png) |
| Error E1, U07 | desktop | ![Error E1, U07, light](../../images/09-portals-and-offline-forms/u07-administrator/e1-portal-settings-refused-desktop-light.png) | ![Error E1, U07, dark](../../images/09-portals-and-offline-forms/u07-administrator/e1-portal-settings-refused-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f02-20-portal-settings-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f02-20-portal-settings-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f02-20-portal-settings-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f02-20-portal-settings-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f02-20-portal-settings-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f02-20-portal-settings-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f02-20-portal-settings-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f02-20-portal-settings-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Audience, fields, lists, actions | E-F2-19 | yes |

## Actions

| Action | Who | Result |
|---|---|---|
| Preview as | configurator | The portal as that contact sees it |
| Publish | configurator | Record type on the portal |

## States

- Normal: choose how a record type shows on a portal, and preview it as a contact.
- Empty: not on a portal: Put on a portal.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: for users who are not configurators; on the portal, records the person may only read.
- Offline: Not available offline: the portal is served live to outside people
  ([D407](../../../../06-decisions/technical/d407-front-end.md)).

Shown entities (VD-15): [E-F2-05 Record type](../../data/e-f02-05-record-type.md),
[E-F2-19 Portal exposure](../../data/e-f02-19-portal-exposure.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F2-05 Record type | Draft | Badge "Draft"; a new record starts here; next: Live (UC-F2-04); fields editable within the role | U07, U09 | `u07-administrator/s-f02-20-portal-settings-e-f02-05-record-type-draft-desktop-{light,dark}.png`, `u09-customer/s-f02-20-portal-settings-e-f02-05-record-type-draft-phone-{light,dark}.png` |
| E-F2-05 Record type | Live | Badge "Live"; next: Archived (UC-F2-04); fields editable within the role | U07, U09 | `u07-administrator/s-f02-20-portal-settings-e-f02-05-record-type-live-desktop-{light,dark}.png`, `u09-customer/s-f02-20-portal-settings-e-f02-05-record-type-live-phone-{light,dark}.png` |
| E-F2-05 Record type | Archived | Badge "Archived"; next: Live (UC-F2-04); fields editable within the role | U07, U09 | `u07-administrator/s-f02-20-portal-settings-e-f02-05-record-type-archived-desktop-{light,dark}.png`, `u09-customer/s-f02-20-portal-settings-e-f02-05-record-type-archived-phone-{light,dark}.png` |
| E-F2-19 Portal exposure | Draft | Badge "Draft"; a new record starts here; next: Published (UC-F2-20); fields editable within the role | U07, U09 | `u07-administrator/s-f02-20-portal-settings-e-f02-19-portal-exposure-draft-desktop-{light,dark}.png`, `u09-customer/s-f02-20-portal-settings-e-f02-19-portal-exposure-draft-phone-{light,dark}.png` |
| E-F2-19 Portal exposure | Published | Badge "Published"; next: Archived (BR-F2-20); fields editable within the role | U07, U09 | `u07-administrator/s-f02-20-portal-settings-e-f02-19-portal-exposure-published-desktop-{light,dark}.png`, `u09-customer/s-f02-20-portal-settings-e-f02-19-portal-exposure-published-phone-{light,dark}.png` |
| E-F2-19 Portal exposure | Archived | Badge "Archived"; final: read-only, no next state; the history shows how it got here | U07, U09 | `u07-administrator/s-f02-20-portal-settings-e-f02-19-portal-exposure-archived-desktop-{light,dark}.png`, `u09-customer/s-f02-20-portal-settings-e-f02-19-portal-exposure-archived-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Settings on desktop; the portal on a phone.

## Accessibility

Every status is a word, not only a colour; drag and drop has a keyboard equivalent; fields have labels.

## Components

- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-04 Card](../../../../04-ux/design-system/components/c-04-card.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F2-09 Portals and offline forms](../../flows/fl-f02-09-portals-and-offline-forms.md)

## Open questions

None.

---

⬅️ [S-F2-19 Booking calendar](../08-views-and-bookings/s-f02-19-booking-calendar.md) · ⬆️ [Up](README.md) ·
➡️ [S-F2-21 Offline form](s-f02-21-offline-form.md)
