🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏪 [F10 Point of sale (plugin)](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F10-12](README.md) ›
🖥️ S-F10-31 Layaway

# 🖥️ S-F10-31 Layaway

**Status:** ✅ specified

## Personas

- [U17 Cashier](../../../../01-users/personas/u17-cashier.md): parks sales and takes deposits, on a tablet.
- [U23 Store manager](../../../../01-users/personas/u23-store-manager.md): sets the terms and follows the held items, on
  a desktop.

## Purpose

Park a sale or hold items against a deposit, and complete or refund them.

## Entry points

Till › Park or Layaway; Point of sale › Layaways.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Layaway                         Terms: deposit 30 percent, refund 14 days   [New layaway] [Parked sales] |
| ------------------------------------------------------------------------------------------- |
| KIND      CUSTOMER    ITEMS          TOTAL    DEPOSIT   COLLECT BY   STATE                  |
| Layaway   Sonia M.    Winter coat    150.00   45.00     2026-12-05   Held        [Take the balance] |
| Layaway   Julien R.   Boots          89.00    27.00     2026-11-20   Expired     [Refund]   |
| Parked    -           3 lines        64.20    -         today        Parked      [Resume]   |
| Held: 4   Expiring this week: 1   Parked: 2                                                 |
+---------------------------------------------------------------------------------------------+
```

Example images of the empty, loading, read-only and offline states, drawn in the image round
([D120](../../../../06-decisions/ux/d120-png-mockups.md)): `s-f10-31-layaway-empty-desktop-{light,dark}.png`,
`s-f10-31-layaway-empty-tablet-{light,dark}.png`, `s-f10-31-layaway-loading-desktop-{light,dark}.png`,
`s-f10-31-layaway-loading-tablet-{light,dark}.png`, `s-f10-31-layaway-offline-desktop-{light,dark}.png`,
`s-f10-31-layaway-offline-tablet-{light,dark}.png`, `s-f10-31-layaway-read-only-desktop-{light,dark}.png`,
`s-f10-31-layaway-read-only-tablet-{light,dark}.png`.

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F10-12 step 4, U17 | tablet | ![FL-F10-12 step 4, U17, light](../../images/12-takeaway-softpos-and-labels/u17-cashier/4-layaway-tablet-light.png) | ![FL-F10-12 step 4, U17, dark](../../images/12-takeaway-softpos-and-labels/u17-cashier/4-layaway-tablet-dark.png) |
| FL-F10-12 step 4, U17 | desktop | ![FL-F10-12 step 4, U17, light](../../images/12-takeaway-softpos-and-labels/u17-cashier/4-layaway-desktop-light.png) | ![FL-F10-12 step 4, U17, dark](../../images/12-takeaway-softpos-and-labels/u17-cashier/4-layaway-desktop-dark.png) |
| FL-F10-12 step 4, U17 | phone | ![FL-F10-12 step 4, U17, light](../../images/12-takeaway-softpos-and-labels/u17-cashier/4-layaway-phone-light.png) | ![FL-F10-12 step 4, U17, dark](../../images/12-takeaway-softpos-and-labels/u17-cashier/4-layaway-phone-dark.png) |
| FL-F10-12 step 4, U17 | tablet | ![FL-F10-12 step 4, U17, light](../../images/12-takeaway-softpos-and-labels/u17-cashier/4-layaway-tablet-light.png) | ![FL-F10-12 step 4, U17, dark](../../images/12-takeaway-softpos-and-labels/u17-cashier/4-layaway-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f10-31-layaway-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f10-31-layaway-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f10-31-layaway-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f10-31-layaway-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f10-31-layaway-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f10-31-layaway-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f10-31-layaway-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f10-31-layaway-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Kind and customer | E-F10-24 kind and customer | text | layaway only | yes |
| Items and total | E-F10-24 lines and total | list and money | before the deposit | yes |
| Deposit | E-F10-24 deposit paid | money | at least the minimum | for a layaway |
| Collection date | E-F10-24 collection date | date | within the holding time | for a layaway |
| State | E-F10-24 state | badge | by action | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Park | till | the seller | the sale is put aside (UC-F10-32) |
| Resume | parked row | the seller | the sale opens with its lines |
| New layaway | header | the seller | items are held against a deposit |
| Take the balance | row | the seller | the sale completes and the items leave stock |
| Cancel, Refund | row | the seller, the store manager | the deposit is refunded per the terms |

## States

- Normal: the layaways and parked sales with their customer, items, deposit, date and state.
- Empty: Nothing parked or held: a hint on how to park a sale or take a deposit.
- Loading: The list as placeholders, then the terms.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a deposit below
  the minimum says so under the field.
- Read-only: a closed session or a layaway already refunded: shown, with no action.
- Offline: A parked sale stays on the till when the network is down
  ([BR-F10-06](../../business-rules/br-f10-06-offline-keeps-selling.md)); a deposit is taken and chained locally and
  synchronised later, and a layaway of another till is read when the network is back.

Shown entities (VD-15): [E-F10-24 Layaway](../../data/e-f10-24-layaway.md),
[E-F10-03 Point of sale order](../../data/e-f10-03-point-of-sale-order.md),
[E-F10-04 Till payment](../../data/e-f10-04-till-payment.md),
[E-F7-06 Item](../../../f07-purchasing-and-stock/data/e-f07-06-item.md),
[E-F6-01 Customer record](../../../f06-customers-and-sales/data/e-f06-01-customer-record.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F10-24 Layaway | Parked | Badge "Parked"; a new record starts here; next: Resumed or Expired (UC-F10-32); fields editable within the role | U17, U23 | `u17-cashier/s-f10-31-layaway-e-f10-24-layaway-parked-{desktop,phone,tablet}-{light,dark}.png`; `u23-store-manager/s-f10-31-layaway-e-f10-24-layaway-parked-{desktop,phone,tablet}-{light,dark}.png` |
| E-F10-24 Layaway | Held | Badge "Held"; a new record starts here; next: Collected or Cancelled or Expired (UC-F10-32, BR-F10-26); fields editable within the role | U17, U23 | `u17-cashier/s-f10-31-layaway-e-f10-24-layaway-held-{desktop,phone,tablet}-{light,dark}.png`; `u23-store-manager/s-f10-31-layaway-e-f10-24-layaway-held-{desktop,phone,tablet}-{light,dark}.png` |
| E-F10-24 Layaway | Resumed | Badge "Resumed"; final state, read-only | U17, U23 | `u17-cashier/s-f10-31-layaway-e-f10-24-layaway-resumed-{desktop,phone,tablet}-{light,dark}.png`; `u23-store-manager/s-f10-31-layaway-e-f10-24-layaway-resumed-{desktop,phone,tablet}-{light,dark}.png` |
| E-F10-24 Layaway | Expired | Badge "Expired"; next: Refunded (BR-F10-26); fields editable within the role | U17, U23 | `u17-cashier/s-f10-31-layaway-e-f10-24-layaway-expired-{desktop,phone,tablet}-{light,dark}.png`; `u23-store-manager/s-f10-31-layaway-e-f10-24-layaway-expired-{desktop,phone,tablet}-{light,dark}.png` |
| E-F10-24 Layaway | Collected | Badge "Collected"; final state, read-only | U17, U23 | `u17-cashier/s-f10-31-layaway-e-f10-24-layaway-collected-{desktop,phone,tablet}-{light,dark}.png`; `u23-store-manager/s-f10-31-layaway-e-f10-24-layaway-collected-{desktop,phone,tablet}-{light,dark}.png` |
| E-F10-24 Layaway | Cancelled | Badge "Cancelled"; next: Refunded (BR-F10-26); fields editable within the role | U17, U23 | `u17-cashier/s-f10-31-layaway-e-f10-24-layaway-cancelled-{desktop,phone,tablet}-{light,dark}.png`; `u23-store-manager/s-f10-31-layaway-e-f10-24-layaway-cancelled-{desktop,phone,tablet}-{light,dark}.png` |
| E-F10-24 Layaway | Refunded | Badge "Refunded"; final state, read-only | U17, U23 | `u17-cashier/s-f10-31-layaway-e-f10-24-layaway-refunded-{desktop,phone,tablet}-{light,dark}.png`; `u23-store-manager/s-f10-31-layaway-e-f10-24-layaway-refunded-{desktop,phone,tablet}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per persona, device and theme; the
image round draws them. Rows are derived from each entity's Lifecycle: the badge is the state's name, the next states
are its transitions, and a final state is read-only.

## Responsive behaviour

On a tablet at the till; the store manager's list is a desktop table.

## Accessibility

Terms and refund are written out in words; keyboard: next row, resume, take the balance.

## Components

- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-14 Timeline](../../../../04-ux/design-system/components/c-14-timeline.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F10-12 Takeaway, tap to pay, labels and layaway](../../flows/fl-f10-12-takeaway-softpos-and-labels.md)

## Open questions

None.

---

⬅️ [S-F10-30 Shelf labels](s-f10-30-shelf-labels.md) · ⬆️ [Up](README.md) ·
➡️ [S-F10-L01 Point of sales](../00-lists/s-f10-l01-point-of-sales.md)
