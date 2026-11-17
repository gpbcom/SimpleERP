🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛍️ [F11 Online shop (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F11-10 Fulfil from stores and report](README.md) › 🖥️ S-F11-28 Shop reports

# 🖥️ S-F11-28 Shop reports

**Status:** ✅ specified

## Personas

- [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Show the checkout funnel, customer value and return reasons.

## Entry points

Shop › Reports.

## Wireframe

```text
+------------------------------------------------------------------+
| Shop reports  November                                            |
| Funnel: cart 4,100 > address 2,900 > delivery 1,800 (-38 %) > paid|
| Customer value: top 10 % = 41 % of revenue                       |
| Returns: navy coat 38 too small 41 %                             |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F11-10 step 2, U13 | desktop | ![FL-F11-10 step 2, U13, light](../../images/10-fulfil-from-stores-and-report/u13-owner/2-shop-reports-desktop-light.png) | ![FL-F11-10 step 2, U13, dark](../../images/10-fulfil-from-stores-and-report/u13-owner/2-shop-reports-desktop-dark.png) |
| FL-F11-10 step 2, U13 | phone | ![FL-F11-10 step 2, U13, light](../../images/10-fulfil-from-stores-and-report/u13-owner/2-shop-reports-phone-light.png) | ![FL-F11-10 step 2, U13, dark](../../images/10-fulfil-from-stores-and-report/u13-owner/2-shop-reports-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f11-28-shop-reports-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f11-28-shop-reports-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f11-28-shop-reports-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f11-28-shop-reports-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f11-28-shop-reports-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f11-28-shop-reports-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f11-28-shop-reports-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f11-28-shop-reports-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Funnel, value, returns | computed | no |

## Actions

| Action | Who | Result |
|---|---|---|
| Export | marketing, owner | File |

## States

- Normal: show the checkout funnel, customer value and return reasons.
- Empty: no order in the period: "No checkout yet".
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: always: computed.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F11-05 Checkout](../../data/e-f11-05-checkout.md),
[E-F11-08 Withdrawal request](../../data/e-f11-08-withdrawal-request.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F11-05 Checkout | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U13 | `u13-owner/s-f11-28-shop-reports-e-f11-05-checkout-recorded-{desktop,phone}-{light,dark}.png` |
| E-F11-08 Withdrawal request | Received | Badge "Received"; a new record starts here; next: Acknowledged (UC-F11-09); fields editable within the role | U13 | `u13-owner/s-f11-28-shop-reports-e-f11-08-withdrawal-request-received-{desktop,phone}-{light,dark}.png` |
| E-F11-08 Withdrawal request | Acknowledged | Badge "Acknowledged"; next: Returned (UC-F11-09); fields editable within the role | U13 | `u13-owner/s-f11-28-shop-reports-e-f11-08-withdrawal-request-acknowledged-{desktop,phone}-{light,dark}.png` |
| E-F11-08 Withdrawal request | Returned | Badge "Returned"; next: Refunded (UC-F11-09); fields editable within the role | U13 | `u13-owner/s-f11-28-shop-reports-e-f11-08-withdrawal-request-returned-{desktop,phone}-{light,dark}.png` |
| E-F11-08 Withdrawal request | Refunded | Badge "Refunded"; final: read-only, no next state; the history shows how it got here | U13 | `u13-owner/s-f11-28-shop-reports-e-f11-08-withdrawal-request-refunded-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md)
- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)

## Shown in

- [FL-F11-10 Fulfil from stores and report](../../flows/fl-f11-10-fulfil-from-stores-and-report.md)

## Open questions

None.

---

⬅️ [S-F11-27 Store fulfilment](s-f11-27-store-fulfilment.md) · ⬆️ [Up](README.md) ·
➡️ [S-F11-29 Checkout donations](../11-donations-gift-cards-and-cross-border/s-f11-29-checkout-donations.md)
