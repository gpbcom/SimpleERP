🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏘️ [SC10 Real estate](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC10-07 Short stays, commercial leases, LMNP and coworking](README.md) ›
🖥️ S-SC10-21 Short-term rentals

# 🖥️ S-SC10-21 Short-term rentals

**Status:** 🔄 waiting for the owner

## Personas

- [U34 Property manager](../../../../01-users/personas/u34-property-manager.md): the properties, stays and the tax
  declaration.
- [U09 Customer](../../../../01-users/personas/u09-customer.md): their booking, check-in details and invoice.

## Purpose

Book stays on the properties, count the tourist tax per night and guest and prepare the declaration.

## Entry points

Real estate › Stays; the calendar of a property; the guest's booking link.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Property: Studio Le Port, 2 guests max                       Registration number 13055 0123      |
| Stay S-2026-0412   2026-12-20 to 2026-12-24   4 nights   Booked   [Check in]                     |
| Guests 2 adults + 1 child    Rent 480.00   Cleaning 60.00                                        |
| Tourist tax 1.05 x 4 nights x 2 guests = 8.40   (child exempt)                                   |
| Deposit 120.00 paid     Balance 428.40 due 2026-12-20                                            |
| Declaration of the period: 214 nights, tax 449.40     [Prepare the declaration]                  |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC10-07 step 1, U34 | desktop | ![FL-SC10-07 step 1, U34, light](../../images/07-short-stays-commercial-and-coworking/u34-property-manager/1-short-term-rentals-desktop-light.png) | ![FL-SC10-07 step 1, U34, dark](../../images/07-short-stays-commercial-and-coworking/u34-property-manager/1-short-term-rentals-desktop-dark.png) |
| FL-SC10-07 step 1, U34 | tablet | ![FL-SC10-07 step 1, U34, light](../../images/07-short-stays-commercial-and-coworking/u34-property-manager/1-short-term-rentals-tablet-light.png) | ![FL-SC10-07 step 1, U34, dark](../../images/07-short-stays-commercial-and-coworking/u34-property-manager/1-short-term-rentals-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc10-21-short-term-rentals-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc10-21-short-term-rentals-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc10-21-short-term-rentals-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc10-21-short-term-rentals-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc10-21-short-term-rentals-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc10-21-short-term-rentals-read-only-desktop-dark.png) |
| Offline | tablet | ![Offline, light](../../images/states/s-sc10-21-short-term-rentals-offline-tablet-light.png) | ![Offline, dark](../../images/states/s-sc10-21-short-term-rentals-offline-tablet-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Property | E-SC10-17 property | link | yes while Booked | yes |
| Dates and nights | E-SC10-17 arrival, departure | dates | yes while Booked | yes |
| Guests | E-SC10-17 guests | adults, minors, exempt | yes while Booked | yes |
| Rent and cleaning | E-SC10-17 rent, cleaning | amounts | yes while Booked | yes |
| Tourist tax | E-SC10-17 tourist tax | amount | no | no |
| Collected by | E-SC10-17 tax collector | manager or platform | yes while Booked | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Book | calendar | property manager, guest | a stay Booked with its price and tax |
| Check in | stay | property manager | the stay becomes Staying |
| Complete | stay | property manager | the stay becomes Completed and invoiced |
| Prepare the declaration | header | property manager | the tax of the period as a statement |

## States

- Normal: the calendar, the stay with its guests, the tax apart and the invoice.
- Empty: No stay yet, with New stay.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); overlapping
  dates or a missing registration number, with the field to correct.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC10-17 Stay](../../data/e-sc10-17-stay.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC10-17 Stay | Booked | Badge "Booked"; a new record starts here; next: Staying or Cancelled (UC-SC10-21); fields editable within the role | U34, U09 | `u34-property-manager/s-sc10-21-short-term-rentals-e-sc10-17-stay-booked-{desktop,tablet}-{light,dark}.png`, `u09-customer/s-sc10-21-short-term-rentals-e-sc10-17-stay-booked-phone-{light,dark}.png` |
| E-SC10-17 Stay | Staying | Badge "Staying"; next: Completed (UC-SC10-21); fields editable within the role | U34, U09 | `u34-property-manager/s-sc10-21-short-term-rentals-e-sc10-17-stay-staying-{desktop,tablet}-{light,dark}.png`, `u09-customer/s-sc10-21-short-term-rentals-e-sc10-17-stay-staying-phone-{light,dark}.png` |
| E-SC10-17 Stay | Completed | Badge "Completed"; final: read-only, no next state; the history shows how it got here | U34, U09 | `u34-property-manager/s-sc10-21-short-term-rentals-e-sc10-17-stay-completed-{desktop,tablet}-{light,dark}.png`, `u09-customer/s-sc10-21-short-term-rentals-e-sc10-17-stay-completed-phone-{light,dark}.png` |
| E-SC10-17 Stay | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U34, U09 | `u34-property-manager/s-sc10-21-short-term-rentals-e-sc10-17-stay-cancelled-{desktop,tablet}-{light,dark}.png`, `u09-customer/s-sc10-21-short-term-rentals-e-sc10-17-stay-cancelled-phone-{light,dark}.png` |

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

⬅️ [S-SC10-20 Portfolio assistant](../06-portal-and-assistant/s-sc10-20-portfolio-assistant.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC10-22 Commercial leases](s-sc10-22-commercial-leases.md)
