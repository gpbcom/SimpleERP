🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏋️ [SC18 Sports and fitness](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC18-05 Facilities, events, camps and rentals](README.md) ›
🖥️ S-SC18-20 Equipment rental

# 🖥️ S-SC18-20 Equipment rental

**Status:** ✅ specified

## Personas

- [U53 Coach](../../../../01-users/personas/u53-coach.md): the items they rent out and take back.
- [U09 Customer](../../../../01-users/personas/u09-customer.md): their own rentals.

## Purpose

Rent out an item with its deposit, check it at the return and refund or keep the deposit.

## Entry points

Sports and fitness › Rental items; the item's code; the AI assistant.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Rental: Racket R-114                                                      Rented out             |
| Renter Noor A.   Out 2026-11-21 16:00   Due 18:00   Price 6.00 EUR   Deposit 30.00 EUR           |
| Condition at departure: good   Photos 2                                                          |
| Return: [ ] good  [ ] damaged  [ ] lost    Photos [Add]                                          |
| Deposit: refund 30.00 EUR     Damage: 0.00 EUR                                                   |
| [Rent out]  [Take back]  [Send to repair]  [Retire]                                              |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC18-05 step 4, U53 | phone | ![FL-SC18-05 step 4, U53, light](../../images/05-facilities-events-camps-and-rentals/u53-coach/4-equipment-rental-phone-light.png) | ![FL-SC18-05 step 4, U53, dark](../../images/05-facilities-events-camps-and-rentals/u53-coach/4-equipment-rental-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-sc18-20-equipment-rental-empty-phone-light.png) | ![Empty, dark](../../images/states/s-sc18-20-equipment-rental-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-sc18-20-equipment-rental-loading-phone-light.png) | ![Loading, dark](../../images/states/s-sc18-20-equipment-rental-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-sc18-20-equipment-rental-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-sc18-20-equipment-rental-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc18-20-equipment-rental-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc18-20-equipment-rental-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Item | E-SC18-16 item | stock item | no | yes |
| Renter | E-SC18-16 renter | customer or guest | yes while Available | yes |
| Out and due | E-SC18-16 out at, due at | date and time | yes while Available | yes |
| Deposit | E-SC18-16 deposit | amount | yes while Available | yes |
| Condition | E-SC18-16 condition | good, damaged, lost | yes at return | yes |
| Photos | E-SC18-16 photos | images | yes | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Rent out | item | coach | the item becomes Rented out and the deposit is taken |
| Take back | item | coach | the item is checked and the deposit refunded or kept |
| Send to repair | item | coach, owner | the item becomes In repair |
| Retire | item | owner | the item leaves the rental stock |

## States

- Normal: the item with its state, renter, due time, deposit and condition.
- Empty: No item rented out.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a missing
  deposit or an item not available, with what to do.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC18-16 Rental item](../../data/e-sc18-16-rental-item.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC18-16 Rental item | Available | Badge "Available"; a new record starts here; next: Rented out or Retired (UC-SC18-20); fields editable within the role | U53, U09 | `u53-coach/s-sc18-20-equipment-rental-e-sc18-16-rental-item-available-phone-{light,dark}.png`, `u09-customer/s-sc18-20-equipment-rental-e-sc18-16-rental-item-available-phone-{light,dark}.png` |
| E-SC18-16 Rental item | Rented out | Badge "Rented out"; next: Available, In repair or Retired (BR-SC18-20, UC-SC18-20); fields editable within the role | U53, U09 | `u53-coach/s-sc18-20-equipment-rental-e-sc18-16-rental-item-rented-out-phone-{light,dark}.png`, `u09-customer/s-sc18-20-equipment-rental-e-sc18-16-rental-item-rented-out-phone-{light,dark}.png` |
| E-SC18-16 Rental item | In repair | Badge "In repair"; next: Available or Retired (UC-SC18-20); fields editable within the role | U53, U09 | `u53-coach/s-sc18-20-equipment-rental-e-sc18-16-rental-item-in-repair-phone-{light,dark}.png`, `u09-customer/s-sc18-20-equipment-rental-e-sc18-16-rental-item-in-repair-phone-{light,dark}.png` |
| E-SC18-16 Rental item | Retired | Badge "Retired"; final: read-only, no next state; the history shows how it got here | U53, U09 | `u53-coach/s-sc18-20-equipment-rental-e-sc18-16-rental-item-retired-phone-{light,dark}.png`, `u09-customer/s-sc18-20-equipment-rental-e-sc18-16-rental-item-retired-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

The coach and the member use the phone, the owner and the treasurer a desktop, with the same actions in one column.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC18-05](../../flows/fl-sc18-05-facilities-events-camps-and-rentals.md)

## Open questions

None.

---

⬅️ [S-SC18-19 Holiday camps](s-sc18-19-holiday-camps.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC18-L01 Club memberships](../00-lists/s-sc18-l01-club-memberships.md)
