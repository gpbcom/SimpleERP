🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🍽️ [SC06 Restaurant and hospitality](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC06-06 Campsites, catering, groups, pricing and licences](README.md) › 🖥️ S-SC06-21 Guest profiles

# 🖥️ S-SC06-21 Guest profiles

**Status:** ✅ specified

## Personas

- [U28 Hotel receptionist](../../../../01-users/personas/u28-hotel-receptionist.md): the profile with its preferences,
  past stays and consent.
- [U18 Waiter](../../../../01-users/personas/u18-waiter.md): the allergies and diet shown at the top of each order.

## Purpose

Know the guest: allergies, diet, preferences and past stays, shown where the staff need them.

## Entry points

Restaurant and hospitality › Guest profiles; a booking's guest; the waiter's order screen.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Guest: Ms Nakamura   Stays 4   Last 2026-08-12            Consent: preferences kept (2025-06-03) |
| ALLERGIES: peanuts, shellfish          Diet: pescatarian                                         |
| Preferences: quiet room, firm pillow, tea at arrival, table by the window                        |
| Special dates: birthday 4 March                                                                  |
| Past stays: 2025-06 room 12, 2026-02 room 14, 2026-08 room 12                                    |
| Open order: table 7        Warning: dish 'Pad thai' contains peanuts      [Edit] [Anonymise]     |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC06-06 step 6, U28 | desktop | ![FL-SC06-06 step 6, U28, light](../../images/06-campsites-catering-groups-and-pricing/u28-hotel-receptionist/6-guest-profiles-desktop-light.png) | ![FL-SC06-06 step 6, U28, dark](../../images/06-campsites-catering-groups-and-pricing/u28-hotel-receptionist/6-guest-profiles-desktop-dark.png) |
| FL-SC06-06 step 6, U28 | tablet | ![FL-SC06-06 step 6, U28, light](../../images/06-campsites-catering-groups-and-pricing/u28-hotel-receptionist/6-guest-profiles-tablet-light.png) | ![FL-SC06-06 step 6, U28, dark](../../images/06-campsites-catering-groups-and-pricing/u28-hotel-receptionist/6-guest-profiles-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc06-21-guest-profiles-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc06-21-guest-profiles-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc06-21-guest-profiles-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc06-21-guest-profiles-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc06-21-guest-profiles-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc06-21-guest-profiles-read-only-desktop-dark.png) |
| Offline | tablet | ![Offline, light](../../images/states/s-sc06-21-guest-profiles-offline-tablet-light.png) | ![Offline, dark](../../images/states/s-sc06-21-guest-profiles-offline-tablet-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Guest | E-SC06-18 guest | link | no | yes |
| Allergies | E-SC06-18 allergies | list of allergens | yes | no |
| Diet | E-SC06-18 diet | list | yes | no |
| Preferences | E-SC06-18 preferences | text | yes with consent | no |
| Special dates | E-SC06-18 special dates | dates | yes with consent | no |
| Consent | E-SC06-18 consent | date and wording | yes | yes for preferences |
| Stays | E-SC06-18 stays | number | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Add allergy | profile, waiter's phone | receptionist, waiter | shown at once on every open order of the guest |
| Record consent | profile | receptionist | the preferences may be kept |
| Anonymise | profile | receptionist, owner | the personal data are removed and the stays counts remain |
| Show on an order | order screen | waiter | the allergies at the top of the order |

## States

- Normal: the allergies, diet, preferences and past stays with the consent.
- Empty: No profile yet, with New profile.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a preference
  without consent, with the way to record it.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC06-18 Guest profile](../../data/e-sc06-18-guest-profile.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC06-18 Guest profile | Active | Badge "Active"; a new record starts here; next: Dormant (UC-SC06-21); fields editable within the role | U28, U18 | `u28-hotel-receptionist/s-sc06-21-guest-profiles-e-sc06-18-guest-profile-active-{desktop,tablet}-{light,dark}.png`, `u18-waiter/s-sc06-21-guest-profiles-e-sc06-18-guest-profile-active-{phone,tablet}-{light,dark}.png` |
| E-SC06-18 Guest profile | Dormant | Badge "Dormant"; next: Active or Anonymised (UC-SC06-21, BR-SC06-21); fields editable within the role | U28, U18 | `u28-hotel-receptionist/s-sc06-21-guest-profiles-e-sc06-18-guest-profile-dormant-{desktop,tablet}-{light,dark}.png`, `u18-waiter/s-sc06-21-guest-profiles-e-sc06-18-guest-profile-dormant-{phone,tablet}-{light,dark}.png` |
| E-SC06-18 Guest profile | Anonymised | Badge "Anonymised"; final: read-only, no next state; the history shows how it got here | U28, U18 | `u28-hotel-receptionist/s-sc06-21-guest-profiles-e-sc06-18-guest-profile-anonymised-{desktop,tablet}-{light,dark}.png`, `u18-waiter/s-sc06-21-guest-profiles-e-sc06-18-guest-profile-anonymised-{phone,tablet}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop for the receptionist. The waiter's phone shows the allergies in red at the top of the order, in large type.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC06-06](../../flows/fl-sc06-06-campsites-catering-groups-and-pricing.md)

## Open questions

None.

---

⬅️ [S-SC06-20 Alcohol licences](s-sc06-20-alcohol-licences.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC06-L02 Menu dishes](../00-lists/s-sc06-l02-menu-dishes.md)
