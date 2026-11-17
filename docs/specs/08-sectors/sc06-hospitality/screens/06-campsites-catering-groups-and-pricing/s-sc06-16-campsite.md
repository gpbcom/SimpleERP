🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🍽️ [SC06 Restaurant and hospitality](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC06-06 Campsites, catering, groups, pricing and licences](README.md) › 🖥️ S-SC06-16 Campsite

# 🖥️ S-SC06-16 Campsite

**Status:** 🔄 waiting for the owner

## Personas

- [U28 Hotel receptionist](../../../../01-users/personas/u28-hotel-receptionist.md): the plan of pitches, free dates and
  arrivals.
- [U09 Customer](../../../../01-users/personas/u09-customer.md): their own booking and the arrival instructions.

## Purpose

Find a free pitch for the dates and type, see its price by season and book it with its options.

## Entry points

Restaurant and hospitality › Pitches; the booking calendar; the guest's booking link.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Campsite Les Pins   Aug 2026   Caravan  7 nights  2 adults                [Book pitch]           |
| Pitch  Type     m2   Power  Season   Per night   Free for the stay                               |
| 44     Caravan  110  10 A   High     38.00       yes                                             |
| 45     Caravan  95   6 A    High     34.00       yes                                             |
| 52     Tent     70   none   High     24.00       no (booked 14-16 Aug)                           |
| Options: electricity 4.50  dog 2.00  extra vehicle 3.00     Tourist tax: 0.66 per adult and nigh |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC06-06 step 1, U28 | desktop | ![FL-SC06-06 step 1, U28, light](../../images/06-campsites-catering-groups-and-pricing/u28-hotel-receptionist/1-campsite-desktop-light.png) | ![FL-SC06-06 step 1, U28, dark](../../images/06-campsites-catering-groups-and-pricing/u28-hotel-receptionist/1-campsite-desktop-dark.png) |
| FL-SC06-06 step 1, U28 | tablet | ![FL-SC06-06 step 1, U28, light](../../images/06-campsites-catering-groups-and-pricing/u28-hotel-receptionist/1-campsite-tablet-light.png) | ![FL-SC06-06 step 1, U28, dark](../../images/06-campsites-catering-groups-and-pricing/u28-hotel-receptionist/1-campsite-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc06-16-campsite-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc06-16-campsite-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc06-16-campsite-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc06-16-campsite-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc06-16-campsite-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc06-16-campsite-read-only-desktop-dark.png) |
| Offline | tablet | ![Offline, light](../../images/states/s-sc06-16-campsite-offline-tablet-light.png) | ![Offline, dark](../../images/states/s-sc06-16-campsite-offline-tablet-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Pitch | E-SC06-13 number | text | no | yes |
| Type | E-SC06-13 type | tent, caravan, motorhome, mobile home | yes while Draft | yes |
| Area | E-SC06-13 area | number in m2 | yes while Draft | yes |
| Power | E-SC06-13 power | amperes | yes while Draft | no |
| Season grid | E-SC06-13 grid | link to rate plan | yes while Draft | yes |
| Night price | E-SC06-13 night price | amount in EUR | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Book pitch | row | receptionist | a booking, a deposit and the confirmation |
| Block pitch | row | receptionist | the pitch is Blocked for the dates, with a reason |
| Change grid | header | owner | a new price for a season, applied to later bookings |
| Check in | booking | receptionist | the guest and the vehicle are recorded on the pitch |

## States

- Normal: the free pitches for the stay with their night price.
- Empty: No pitch yet, with New pitch.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a date with no
  price in the grid, with the rate plan to complete.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC06-13 Pitch](../../data/e-sc06-13-pitch.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC06-13 Pitch | Draft | Badge "Draft"; a new record starts here; next: Open (BR-SC06-16); fields editable within the role | U28, U09 | `u28-hotel-receptionist/s-sc06-16-campsite-e-sc06-13-pitch-draft-{desktop,tablet}-{light,dark}.png`, `u09-customer/s-sc06-16-campsite-e-sc06-13-pitch-draft-phone-{light,dark}.png` |
| E-SC06-13 Pitch | Open | Badge "Open"; next: Blocked or Retired (UC-SC06-16); fields editable within the role | U28, U09 | `u28-hotel-receptionist/s-sc06-16-campsite-e-sc06-13-pitch-open-{desktop,tablet}-{light,dark}.png`, `u09-customer/s-sc06-16-campsite-e-sc06-13-pitch-open-phone-{light,dark}.png` |
| E-SC06-13 Pitch | Blocked | Badge "Blocked"; next: Open (UC-SC06-16); fields editable within the role | U28, U09 | `u28-hotel-receptionist/s-sc06-16-campsite-e-sc06-13-pitch-blocked-{desktop,tablet}-{light,dark}.png`, `u09-customer/s-sc06-16-campsite-e-sc06-13-pitch-blocked-phone-{light,dark}.png` |
| E-SC06-13 Pitch | Retired | Badge "Retired"; final: read-only, no next state; the history shows how it got here | U28, U09 | `u28-hotel-receptionist/s-sc06-16-campsite-e-sc06-13-pitch-retired-{desktop,tablet}-{light,dark}.png`, `u09-customer/s-sc06-16-campsite-e-sc06-13-pitch-retired-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop for the receptionist. The guest's page works on a phone with the pitch number and the gate code.

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

⬅️ [S-SC06-15 Hospitality assistant](../03-rooms-and-bookings/s-sc06-15-hospitality-assistant.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC06-17 Catering](s-sc06-17-catering.md)
