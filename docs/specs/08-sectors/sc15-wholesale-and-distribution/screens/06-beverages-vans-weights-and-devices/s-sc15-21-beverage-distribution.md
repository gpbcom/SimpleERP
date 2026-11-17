🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
📦 [SC15 Wholesale and distribution](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC15-06 Beverages, van sales, catch weight and medical devices](README.md) ›
🖥️ S-SC15-21 Beverage distribution

# 🖥️ S-SC15-21 Beverage distribution

**Status:** 🔄 waiting for the owner

## Personas

- [U42 Sales representative](../../../../01-users/personas/u42-sales-representative.md): the bars' orders, the empties
  and the loans on the phone.
- [U04 Purchasing and stock](../../../../01-users/personas/u04-purchasing.md): the commitments, the loans due back and
  the supplies.

## Purpose

Sell beverages with their excise duty and deposits on the invoice and follow the equipment lent to bars against their
yearly volume.

## Entry points

Wholesale › Beverages; a bar's page; the representative's day on the phone.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Bar Le Phare                               Licence IV    Commitment 120 hl    [New order] [Lend] |
| Line            Qty   Goods EUR   Duty EUR   Deposit EUR   Empties back   Credit EUR             |
| Lager 24x33cl   20    640.00      46.40      60.00         14             -42.00                 |
| Pale ale keg    4     320.00      21.20      120.00        3              -90.00                 |
| Total                 960.00      67.60      180.00                       -132.00                |
| Loans: draught system 1,800.00 EUR since 2025-03-01, 74 hl of 120 hl     State: Lent             |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC15-06 step 1, U42 | phone | ![FL-SC15-06 step 1, U42, light](../../images/06-beverages-vans-weights-and-devices/u42-sales-representative/1-beverage-distribution-phone-light.png) | ![FL-SC15-06 step 1, U42, dark](../../images/06-beverages-vans-weights-and-devices/u42-sales-representative/1-beverage-distribution-phone-dark.png) |
| FL-SC15-06 step 1, U42 | desktop | ![FL-SC15-06 step 1, U42, light](../../images/06-beverages-vans-weights-and-devices/u42-sales-representative/1-beverage-distribution-desktop-light.png) | ![FL-SC15-06 step 1, U42, dark](../../images/06-beverages-vans-weights-and-devices/u42-sales-representative/1-beverage-distribution-desktop-dark.png) |
| FL-SC15-06 step 1, U42 | tablet | ![FL-SC15-06 step 1, U42, light](../../images/06-beverages-vans-weights-and-devices/u42-sales-representative/1-beverage-distribution-tablet-light.png) | ![FL-SC15-06 step 1, U42, dark](../../images/06-beverages-vans-weights-and-devices/u42-sales-representative/1-beverage-distribution-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc15-21-beverage-distribution-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc15-21-beverage-distribution-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc15-21-beverage-distribution-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc15-21-beverage-distribution-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc15-21-beverage-distribution-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc15-21-beverage-distribution-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc15-21-beverage-distribution-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc15-21-beverage-distribution-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Customer | E-SC15-15 customer | link | no | yes |
| Equipment | E-SC15-15 equipment | text | yes while Lent | yes |
| Serial number | E-SC15-15 serial | text | yes while Lent | yes |
| Value | E-SC15-15 value | amount in EUR | yes while Lent | yes |
| Yearly commitment | E-SC15-15 volume commitment | number in hectolitres | yes while Lent | yes |
| Volume bought | E-SC15-15 volume bought | number in hectolitres | no | no |
| Lent on | E-SC15-15 lent on | date | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| New order | header | sales representative | an order with duty and deposits per line |
| Count empties | delivery | driver | the empties by container and the credit of the deposits |
| Lend | customer | sales representative | a loan in state Lent with its commitment |
| Mark lost | loan | sales representative | the loan is Lost and its value is billed |

## States

- Normal: the order lines with goods, duty, deposits and credits, and the customer's loans.
- Empty: No order yet, with New order.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); an alcoholic
  item without an excise category, empties above the deposits charged, with the field to correct.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC15-15 Bar loan](../../data/e-sc15-15-bar-loan.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC15-15 Bar loan | Lent | Badge "Lent"; a new record starts here; next: Returned or Lost (UC-SC15-21, BR-SC15-16); fields editable within the role | U42, U04 | `u42-sales-representative/s-sc15-21-beverage-distribution-e-sc15-15-bar-loan-lent-{desktop,phone,tablet}-{light,dark}.png`, `u04-purchasing/s-sc15-21-beverage-distribution-e-sc15-15-bar-loan-lent-desktop-{light,dark}.png` |
| E-SC15-15 Bar loan | Returned | Badge "Returned"; final: read-only, no next state; the history shows how it got here | U42, U04 | `u42-sales-representative/s-sc15-21-beverage-distribution-e-sc15-15-bar-loan-returned-{desktop,phone,tablet}-{light,dark}.png`, `u04-purchasing/s-sc15-21-beverage-distribution-e-sc15-15-bar-loan-returned-desktop-{light,dark}.png` |
| E-SC15-15 Bar loan | Lost | Badge "Lost"; final: read-only, no next state; the history shows how it got here | U42, U04 | `u42-sales-representative/s-sc15-21-beverage-distribution-e-sc15-15-bar-loan-lost-{desktop,phone,tablet}-{light,dark}.png`, `u04-purchasing/s-sc15-21-beverage-distribution-e-sc15-15-bar-loan-lost-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

The representative's phone shows the order lines with duty and deposits and the loans of the customer.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC15-06](../../flows/fl-sc15-06-beverages-vans-weights-and-devices.md)

## Open questions

None.

---

⬅️ [S-SC15-20 Sales assistant](../05-sales-force-and-performance/s-sc15-20-sales-assistant.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC15-22 Van sales](s-sc15-22-van-sales.md)
