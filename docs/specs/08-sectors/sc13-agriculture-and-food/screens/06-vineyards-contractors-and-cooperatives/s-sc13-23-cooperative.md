🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🌾 [SC13 Agriculture and food](../../README.md) ›
🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC13-06 Vineyards, contractors, cooperatives, baskets, forests](README.md) › 🖥️ S-SC13-23 Cooperative

# 🖥️ S-SC13-23 Cooperative

**Status:** ✅ specified

## Personas

- [U31 Treasurer](../../../../01-users/personas/u31-treasurer.md): the settlements, the advances and the rebate.
- [U40 Farmer](../../../../01-users/personas/u40-farmer.md): the member's own deliveries and payments on the phone.

## Purpose

Record the members' deliveries, pay advances and balances by grade and allocate the rebate of the year in proportion to
the deliveries.

## Entry points

Agriculture › Cooperative; the weighbridge screen; the member's phone.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Deliveries: wheat, harvest 2026                       [Record delivery] [Pay advance] [Rebate]   |
| Delivery  Member        Net t   Grade  Value EUR   Advance    Balance    State                   |
| L-0912    0412 Aubin    12.4    1      2,852.00    1,426.00   -          Advance paid            |
| L-0913    0377 Moulin   8.1     2      1,741.50    -          -          Graded                  |
| L-0914    0412 Aubin    9.7     1      2,231.00    1,115.50   1,115.50   Settled                 |
| Surplus to allocate: 10,000.00 EUR in proportion to the value delivered                          |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC13-06 step 3, U31 | desktop | ![FL-SC13-06 step 3, U31, light](../../images/06-vineyards-contractors-and-cooperatives/u31-treasurer/3-cooperative-desktop-light.png) | ![FL-SC13-06 step 3, U31, dark](../../images/06-vineyards-contractors-and-cooperatives/u31-treasurer/3-cooperative-desktop-dark.png) |
| FL-SC13-06 step 3, U31 | phone | ![FL-SC13-06 step 3, U31, light](../../images/06-vineyards-contractors-and-cooperatives/u31-treasurer/3-cooperative-phone-light.png) | ![FL-SC13-06 step 3, U31, dark](../../images/06-vineyards-contractors-and-cooperatives/u31-treasurer/3-cooperative-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc13-23-cooperative-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc13-23-cooperative-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc13-23-cooperative-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc13-23-cooperative-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc13-23-cooperative-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc13-23-cooperative-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc13-23-cooperative-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc13-23-cooperative-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Member | E-SC13-19 member | link | no | yes |
| Product | E-SC13-19 product | link | yes while Received | yes |
| Net weight | E-SC13-19 net weight | number in tonnes | yes while Received | yes |
| Grade | E-SC13-19 grade | text from the grid | yes while Received | yes |
| Value | E-SC13-19 value | amount in EUR | no | no |
| Advance and balance | E-SC13-19 advance, balance | amounts in EUR | no | no |
| Rebate | E-SC13-19 rebate | amount in EUR | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Record delivery | header | collection agent | a delivery in state Received |
| Grade | delivery | collection agent | the grade and the value are set, state Graded |
| Pay advance | header | treasurer | the deliveries of the week are Advance paid |
| Settle | lot | treasurer | the balances are paid and the deliveries are Settled |
| Allocate rebate | header | treasurer | each member's rebate from the surplus decided |

## States

- Normal: the deliveries with member, weight, grade, value, advance, balance and state.
- Empty: No delivery yet, with Record delivery.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a missing tare
  or grade, a rebate above the surplus, with the field to correct.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC13-19 Member delivery](../../data/e-sc13-19-member-delivery.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC13-19 Member delivery | Received | Badge "Received"; a new record starts here; next: Graded (UC-SC13-23); fields editable within the role | U31, U40 | `u31-treasurer/s-sc13-23-cooperative-e-sc13-19-member-delivery-received-{desktop,phone}-{light,dark}.png`, `u40-farmer/s-sc13-23-cooperative-e-sc13-19-member-delivery-received-{desktop,phone}-{light,dark}.png` |
| E-SC13-19 Member delivery | Graded | Badge "Graded"; next: Advance paid or Settled (UC-SC13-23); fields editable within the role | U31, U40 | `u31-treasurer/s-sc13-23-cooperative-e-sc13-19-member-delivery-graded-{desktop,phone}-{light,dark}.png`, `u40-farmer/s-sc13-23-cooperative-e-sc13-19-member-delivery-graded-{desktop,phone}-{light,dark}.png` |
| E-SC13-19 Member delivery | Advance paid | Badge "Advance paid"; next: Settled (BR-SC13-18); fields editable within the role | U31, U40 | `u31-treasurer/s-sc13-23-cooperative-e-sc13-19-member-delivery-advance-paid-{desktop,phone}-{light,dark}.png`, `u40-farmer/s-sc13-23-cooperative-e-sc13-19-member-delivery-advance-paid-{desktop,phone}-{light,dark}.png` |
| E-SC13-19 Member delivery | Settled | Badge "Settled"; final: read-only, no next state; the history shows how it got here | U31, U40 | `u31-treasurer/s-sc13-23-cooperative-e-sc13-19-member-delivery-settled-{desktop,phone}-{light,dark}.png`, `u40-farmer/s-sc13-23-cooperative-e-sc13-19-member-delivery-settled-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC13-06](../../flows/fl-sc13-06-vineyards-contractors-and-cooperatives.md)

## Open questions

None.

---

⬅️ [S-SC13-22 Farm contractor](s-sc13-22-farm-contractor.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC13-24 Basket subscriptions](s-sc13-24-baskets.md)
