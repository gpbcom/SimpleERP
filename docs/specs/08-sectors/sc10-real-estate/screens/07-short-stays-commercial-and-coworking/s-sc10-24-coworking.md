🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏘️ [SC10 Real estate](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC10-07 Short stays, commercial leases, LMNP and coworking](README.md) ›
🖥️ S-SC10-24 Coworking

# 🖥️ S-SC10-24 Coworking

**Status:** ✅ specified

## Personas

- [U34 Property manager](../../../../01-users/personas/u34-property-manager.md): the memberships, rooms and invoices.
- [U09 Customer](../../../../01-users/personas/u09-customer.md): their credits and their bookings.

## Purpose

Run the memberships of a coworking space, book rooms within the credits and see the occupancy.

## Entry points

Real estate › Memberships; the room calendar; the member's phone app.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Member: Studio Nova (Nina R.)   Plan Flexible 120.00 a month   Active   [Pause]                  |
| Credits  6 hours a month   Used 2   Left 4   Expire 2026-11-30                                   |
| Booking     Room     Date         Time          Hours   From credits                             |
| B-0412      Aster    2026-11-18   10:00-12:00   2       2                                        |
| B-0420      Aster    2026-11-20   14:00-19:00   5       4 + 1 extra at 12.00                     |
| Occupancy this week: rooms 62 %, desks 81 %        [Book a room]                                 |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC10-07 step 4, U34 | desktop | ![FL-SC10-07 step 4, U34, light](../../images/07-short-stays-commercial-and-coworking/u34-property-manager/4-coworking-desktop-light.png) | ![FL-SC10-07 step 4, U34, dark](../../images/07-short-stays-commercial-and-coworking/u34-property-manager/4-coworking-desktop-dark.png) |
| FL-SC10-07 step 4, U34 | tablet | ![FL-SC10-07 step 4, U34, light](../../images/07-short-stays-commercial-and-coworking/u34-property-manager/4-coworking-tablet-light.png) | ![FL-SC10-07 step 4, U34, dark](../../images/07-short-stays-commercial-and-coworking/u34-property-manager/4-coworking-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc10-24-coworking-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc10-24-coworking-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc10-24-coworking-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc10-24-coworking-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc10-24-coworking-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc10-24-coworking-read-only-desktop-dark.png) |
| Offline | tablet | ![Offline, light](../../images/states/s-sc10-24-coworking-offline-tablet-light.png) | ![Offline, dark](../../images/states/s-sc10-24-coworking-offline-tablet-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Member | E-SC10-20 member | customer link | yes while Pending | yes |
| Plan and fee | E-SC10-20 plan, monthly fee | choice and amount | yes while Pending | yes |
| Credits | E-SC10-20 credit hours | number | yes while Pending | yes |
| Credits used | E-SC10-20 used hours | number | no | no |
| Extra hours | E-SC10-20 extra hours | number | no | no |
| Bookings | E-SC10-20 bookings | list | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Book a room | calendar | member, property manager | a booking taken from the credits |
| Cancel a booking | booking | member, property manager | the credits are returned if in time |
| Pause | membership | property manager | the membership becomes Paused |
| End | membership | property manager | the membership becomes Ended |

## States

- Normal: the membership, its credits, the bookings and the extra hours.
- Empty: No membership yet, with New membership.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a double
  booking or extra hours not accepted, with the free slots.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC10-20 Membership](../../data/e-sc10-20-membership.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC10-20 Membership | Pending | Badge "Pending"; a new record starts here; next: Active (UC-SC10-24); fields editable within the role | U34, U09 | `u34-property-manager/s-sc10-24-coworking-e-sc10-20-membership-pending-{desktop,tablet}-{light,dark}.png`, `u09-customer/s-sc10-24-coworking-e-sc10-20-membership-pending-phone-{light,dark}.png` |
| E-SC10-20 Membership | Active | Badge "Active"; next: Paused or Ended (UC-SC10-24); fields editable within the role | U34, U09 | `u34-property-manager/s-sc10-24-coworking-e-sc10-20-membership-active-{desktop,tablet}-{light,dark}.png`, `u09-customer/s-sc10-24-coworking-e-sc10-20-membership-active-phone-{light,dark}.png` |
| E-SC10-20 Membership | Paused | Badge "Paused"; next: Active (UC-SC10-24); fields editable within the role | U34, U09 | `u34-property-manager/s-sc10-24-coworking-e-sc10-20-membership-paused-{desktop,tablet}-{light,dark}.png`, `u09-customer/s-sc10-24-coworking-e-sc10-20-membership-paused-phone-{light,dark}.png` |
| E-SC10-20 Membership | Ended | Badge "Ended"; final: read-only, no next state; the history shows how it got here | U34, U09 | `u34-property-manager/s-sc10-24-coworking-e-sc10-20-membership-ended-{desktop,tablet}-{light,dark}.png`, `u09-customer/s-sc10-24-coworking-e-sc10-20-membership-ended-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

The property manager works on a desktop; the guest, the tenant or the member uses the phone, with the same actions in
one column.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC10-07](../../flows/fl-sc10-07-short-stays-commercial-and-coworking.md)

## Open questions

None.

---

⬅️ [S-SC10-23 Furnished rentals](s-sc10-23-furnished-rentals.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC10-L01 Mandates](../00-lists/s-sc10-l01-mandates.md)
