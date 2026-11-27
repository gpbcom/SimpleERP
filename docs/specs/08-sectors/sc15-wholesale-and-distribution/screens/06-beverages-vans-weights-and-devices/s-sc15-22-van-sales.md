🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
📦 [SC15 Wholesale and distribution](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC15-06 Beverages, van sales, catch weight and medical devices](README.md) › 🖥️ S-SC15-22 Van sales

# 🖥️ S-SC15-22 Van sales

**Status:** 🔄 waiting for the owner

## Personas

- [U42 Sales representative](../../../../01-users/personas/u42-sales-representative.md): their van's load, the stops and
  the count on the phone.
- [U04 Purchasing and stock](../../../../01-users/personas/u04-purchasing.md): the vans' counts, the differences and the
  reloads.

## Purpose

Load a van, sell and invoice at each stop on the phone, count the van on its return and settle the differences before
the next load.

## Entry points

Wholesale › Van sales; the driver's round on the phone; the warehouse's loading list.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Van 4  Lucas M.  2026-11-12                                   [Confirm load] [Count] [Reconcile] |
| Item            Loaded   Sold   Returned   Expected   Counted   Difference   State               |
| Baguette tray   40       32     1          9          9         0            Counted             |
| Cheese 1 kg     30       18     0          12         9         -3           Counted             |
| Oil 5 l         50       41     2          11         10        -1           Counted             |
| Differences: 2 items, 4 units                              [Post as loss] [Explain]              |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC15-06 step 2, U42 | phone | ![FL-SC15-06 step 2, U42, light](../../images/06-beverages-vans-weights-and-devices/u42-sales-representative/2-van-sales-phone-light.png) | ![FL-SC15-06 step 2, U42, dark](../../images/06-beverages-vans-weights-and-devices/u42-sales-representative/2-van-sales-phone-dark.png) |
| FL-SC15-06 step 2, U42 | desktop | ![FL-SC15-06 step 2, U42, light](../../images/06-beverages-vans-weights-and-devices/u42-sales-representative/2-van-sales-desktop-light.png) | ![FL-SC15-06 step 2, U42, dark](../../images/06-beverages-vans-weights-and-devices/u42-sales-representative/2-van-sales-desktop-dark.png) |
| FL-SC15-06 step 2, U42 | tablet | ![FL-SC15-06 step 2, U42, light](../../images/06-beverages-vans-weights-and-devices/u42-sales-representative/2-van-sales-tablet-light.png) | ![FL-SC15-06 step 2, U42, dark](../../images/06-beverages-vans-weights-and-devices/u42-sales-representative/2-van-sales-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc15-22-van-sales-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc15-22-van-sales-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc15-22-van-sales-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc15-22-van-sales-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc15-22-van-sales-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc15-22-van-sales-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc15-22-van-sales-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc15-22-van-sales-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Van | E-SC15-16 van | link to a location | no | yes |
| Date | E-SC15-16 date | date | no | yes |
| Item | E-SC15-16 item | link | no | yes |
| Loaded | E-SC15-16 loaded | number | yes while Loaded | yes |
| Sold | E-SC15-16 sold | number | no | no |
| Counted | E-SC15-16 counted | number | yes while Loaded | yes to reconcile |
| Difference | E-SC15-16 difference | number | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Confirm load | phone | driver | the van stock is created and the van is Loaded |
| Count | van | driver | the counted quantities are saved and the van is Counted |
| Post as loss | difference | manager | the stock is corrected and the loss is recorded |
| Explain | difference | manager | a reason is saved and the van is Reconciled |

## States

- Normal: the van's items with loaded, sold, returned, expected, counted and difference.
- Empty: No van loaded today, with Confirm load.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a count
  missing, a sale above the stock, with the line to correct.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC15-16 Van stock](../../data/e-sc15-16-van-stock.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC15-16 Van stock | Loaded | Badge "Loaded"; a new record starts here; next: Counted (BR-SC15-17); fields editable within the role | U42, U04 | `u42-sales-representative/s-sc15-22-van-sales-e-sc15-16-van-stock-loaded-{desktop,phone,tablet}-{light,dark}.png`, `u04-purchasing/s-sc15-22-van-sales-e-sc15-16-van-stock-loaded-desktop-{light,dark}.png` |
| E-SC15-16 Van stock | Counted | Badge "Counted"; next: Reconciled (BR-SC15-17); fields editable within the role | U42, U04 | `u42-sales-representative/s-sc15-22-van-sales-e-sc15-16-van-stock-counted-{desktop,phone,tablet}-{light,dark}.png`, `u04-purchasing/s-sc15-22-van-sales-e-sc15-16-van-stock-counted-desktop-{light,dark}.png` |
| E-SC15-16 Van stock | Reconciled | Badge "Reconciled"; final: read-only, no next state; the history shows how it got here | U42, U04 | `u42-sales-representative/s-sc15-22-van-sales-e-sc15-16-van-stock-reconciled-{desktop,phone,tablet}-{light,dark}.png`, `u04-purchasing/s-sc15-22-van-sales-e-sc15-16-van-stock-reconciled-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

The driver's phone shows the load, the stops and a count screen with large number buttons.

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

⬅️ [S-SC15-21 Beverage distribution](s-sc15-21-beverage-distribution.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC15-23 Catch weight](s-sc15-23-catch-weight.md)
