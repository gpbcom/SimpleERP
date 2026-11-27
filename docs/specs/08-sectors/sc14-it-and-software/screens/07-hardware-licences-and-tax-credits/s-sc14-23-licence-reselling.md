🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💻 [SC14 IT and software](../../README.md) ›
🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC14-07 Hardware, licences, research tax credit and sponsorship](README.md) ›
🖥️ S-SC14-23 Licence reselling

# 🖥️ S-SC14-23 Licence reselling

**Status:** 🔄 waiting for the owner

## Personas

- [U41 Customer success manager](../../../../01-users/personas/u41-customer-success-manager.md): the customers' seats,
  the renewals and the differences.
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md): the statement, the comparison and the release of
  the invoices.

## Purpose

Order and change the seats of resold licences by customer and compare them each month with the distributor's statement
before invoicing.

## Entry points

IT and software › Licence reselling; a customer's page; the statement import.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Licences: October 2026                    Statement imported: 212 seats  [Order seats] [Compare] |
| Customer        Product     Seats  Own price  Cost     Renewal     Statement  State              |
| Atelier Roche   Mail suite  40     12.00      8.40     2027-01-15  40         Active             |
| Cabinet Perrin  Docs suite  120    9.50       6.10     2027-03-01  125        Active             |
| Studio Lenoir   Mail suite  12     12.00      8.40     2026-12-01  12         Renewal due        |
| Differences: 1 customer, 5 seats                      [Explain] [Dispute] [Release invoices]     |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC14-07 step 2, U41 | desktop | ![FL-SC14-07 step 2, U41, light](../../images/07-hardware-licences-and-tax-credits/u41-customer-success-manager/2-licence-reselling-desktop-light.png) | ![FL-SC14-07 step 2, U41, dark](../../images/07-hardware-licences-and-tax-credits/u41-customer-success-manager/2-licence-reselling-desktop-dark.png) |
| FL-SC14-07 step 2, U41 | phone | ![FL-SC14-07 step 2, U41, light](../../images/07-hardware-licences-and-tax-credits/u41-customer-success-manager/2-licence-reselling-phone-light.png) | ![FL-SC14-07 step 2, U41, dark](../../images/07-hardware-licences-and-tax-credits/u41-customer-success-manager/2-licence-reselling-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc14-23-licence-reselling-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc14-23-licence-reselling-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc14-23-licence-reselling-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc14-23-licence-reselling-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc14-23-licence-reselling-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc14-23-licence-reselling-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc14-23-licence-reselling-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc14-23-licence-reselling-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Customer | E-SC14-18 customer | link | no | yes |
| Product | E-SC14-18 product | text | yes while Ordered | yes |
| Seats | E-SC14-18 seats | number | yes while Active | yes |
| Customer price | E-SC14-18 price | amount in EUR per seat and month | yes while Ordered | yes |
| Distributor cost | E-SC14-18 cost | amount in EUR per seat and month | yes while Ordered | yes |
| Renewal date | E-SC14-18 renewal date | date | yes while Active | yes |
| Statement seats | E-SC14-18 statement seats | number | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Order seats | header | customer success manager | a subscription in state Ordered |
| Change seats | subscription | customer success manager | the seats and the date of the change are saved |
| Compare | header | accounting | own seats against the statement per customer |
| Release invoices | header | accounting | the invoices of the month for the customers without an open difference |

## States

- Normal: the subscriptions with customer, product, seats, prices, renewal date and the statement's seats.
- Empty: No licence subscription yet, with Order seats.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a statement
  that cannot be read, an open difference, a missing cost price, with the field to correct.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC14-18 Licence subscription](../../data/e-sc14-18-licence-subscription.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC14-18 Licence subscription | Ordered | Badge "Ordered"; a new record starts here; next: Active (UC-SC14-23); fields editable within the role | U41, U05 | `u41-customer-success-manager/s-sc14-23-licence-reselling-e-sc14-18-licence-subscription-ordered-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-sc14-23-licence-reselling-e-sc14-18-licence-subscription-ordered-desktop-{light,dark}.png` |
| E-SC14-18 Licence subscription | Active | Badge "Active"; next: Renewal due or Cancelled (UC-SC14-23); fields editable within the role | U41, U05 | `u41-customer-success-manager/s-sc14-23-licence-reselling-e-sc14-18-licence-subscription-active-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-sc14-23-licence-reselling-e-sc14-18-licence-subscription-active-desktop-{light,dark}.png` |
| E-SC14-18 Licence subscription | Renewal due | Badge "Renewal due"; next: Active or Cancelled (UC-SC14-23); fields editable within the role | U41, U05 | `u41-customer-success-manager/s-sc14-23-licence-reselling-e-sc14-18-licence-subscription-renewal-due-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-sc14-23-licence-reselling-e-sc14-18-licence-subscription-renewal-due-desktop-{light,dark}.png` |
| E-SC14-18 Licence subscription | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U41, U05 | `u41-customer-success-manager/s-sc14-23-licence-reselling-e-sc14-18-licence-subscription-cancelled-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-sc14-23-licence-reselling-e-sc14-18-licence-subscription-cancelled-desktop-{light,dark}.png` |

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

- [FL-SC14-07](../../flows/fl-sc14-07-hardware-licences-and-tax-credits.md)

## Open questions

None.

---

⬅️ [S-SC14-22 Hardware leasing](s-sc14-22-hardware-leasing.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC14-24 Research tax credit](s-sc14-24-research-tax-credit.md)
