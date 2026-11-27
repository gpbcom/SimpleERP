🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🍽️ [SC06 Restaurant and hospitality](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC06-06 Campsites, catering, groups, pricing and licences](README.md) › 🖥️ S-SC06-20 Alcohol licences

# 🖥️ S-SC06-20 Alcohol licences

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md): the licences and permits of each venue and their dates.

## Purpose

Keep the licence, the operating permit and the hours of each venue, and warn before they end.

## Entry points

Restaurant and hospitality › Licences; a venue's settings; the reminder of a renewal.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Licences                                                                    [New licence]        |
| Venue         Category     Declared    Permit holder   Permit ends   Hours       State           |
| Bar Le Quai   III          2019-03-12  M. Roux         2027-02-10    11:00-02:00 Expiring        |
| Restaurant    Small rest.  2021-05-03  Ms Benali       2031-05-03    11:00-23:30 Active          |
| Terrace       III          2022-04-01  M. Roux         2027-02-10    11:00-23:00 Active          |
| Alcohol can be sold now at: Restaurant, Terrace            Attempts refused this month: 3        |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC06-06 step 5, U13 | desktop | ![FL-SC06-06 step 5, U13, light](../../images/06-campsites-catering-groups-and-pricing/u13-owner/5-alcohol-licences-desktop-light.png) | ![FL-SC06-06 step 5, U13, dark](../../images/06-campsites-catering-groups-and-pricing/u13-owner/5-alcohol-licences-desktop-dark.png) |
| FL-SC06-06 step 5, U13 | phone | ![FL-SC06-06 step 5, U13, light](../../images/06-campsites-catering-groups-and-pricing/u13-owner/5-alcohol-licences-phone-light.png) | ![FL-SC06-06 step 5, U13, dark](../../images/06-campsites-catering-groups-and-pricing/u13-owner/5-alcohol-licences-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc06-20-alcohol-licences-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc06-20-alcohol-licences-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc06-20-alcohol-licences-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc06-20-alcohol-licences-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc06-20-alcohol-licences-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc06-20-alcohol-licences-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc06-20-alcohol-licences-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc06-20-alcohol-licences-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Venue | E-SC06-17 venue | link | no | yes |
| Category | E-SC06-17 category | III, IV, small restaurant, full restaurant | yes while Draft | yes |
| Declared on | E-SC06-17 declared on | date | yes while Draft | yes |
| Permit holder | E-SC06-17 permit holder | person | yes | yes |
| Permit ends | E-SC06-17 permit ends | date | yes | yes |
| Hours | E-SC06-17 hours | times per weekday | yes | yes |
| Refused attempts | E-SC06-17 refused attempts | number | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| New licence | header | owner | a licence in Draft for a venue |
| Activate | licence | owner | the till of the venue applies the category and the hours |
| Renew permit | licence | owner | new dates and holder, with the training proof |
| Close | licence | owner | the venue sells no alcohol until a new licence is active |

## States

- Normal: the licences with their category, permit dates, hours and state.
- Empty: No licence yet, with New licence.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a missing
  category or permit date, with the field to correct.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC06-17 Licence](../../data/e-sc06-17-licence.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC06-17 Licence | Draft | Badge "Draft"; a new record starts here; next: Active (BR-SC06-20); fields editable within the role | U13 | `u13-owner/s-sc06-20-alcohol-licences-e-sc06-17-licence-draft-{desktop,phone}-{light,dark}.png` |
| E-SC06-17 Licence | Active | Badge "Active"; next: Expiring (UC-SC06-20); fields editable within the role | U13 | `u13-owner/s-sc06-20-alcohol-licences-e-sc06-17-licence-active-{desktop,phone}-{light,dark}.png` |
| E-SC06-17 Licence | Expiring | Badge "Expiring"; next: Active or Expired (UC-SC06-20, BR-SC06-20); fields editable within the role | U13 | `u13-owner/s-sc06-20-alcohol-licences-e-sc06-17-licence-expiring-{desktop,phone}-{light,dark}.png` |
| E-SC06-17 Licence | Expired | Badge "Expired"; final: read-only, no next state; the history shows how it got here | U13 | `u13-owner/s-sc06-20-alcohol-licences-e-sc06-17-licence-expired-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop only; on a phone, the app asks to continue on a larger screen.

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

⬅️ [S-SC06-19 Dynamic pricing](s-sc06-19-dynamic-pricing.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC06-21 Guest profiles](s-sc06-21-guest-profiles.md)
