🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛍️ [F11 Online shop (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F11-07 Payment risk](README.md) › 🖥️ S-F11-21 Order risk

# 🖥️ S-F11-21 Order risk

**Status:** ✅ specified

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)
- [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md)

## Purpose

Review orders held for fraud risk with their signals.

## Entry points

Shop › Orders at risk.

## Wireframe

```text
+------------------------------------------------------------------+
| Orders held (3)                                                   |
| Order        Amount  Score  Signals                    Age        |
| W-2026-1184  640     82     card abroad, 3 orders/10m  2 h        |
|                                   [Accept] [Cancel and refund]    |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F11-07 step 2, U05 | desktop | ![FL-F11-07 step 2, U05, light](../../images/07-payment-risk/u05-accounting/2-order-risk-desktop-light.png) | ![FL-F11-07 step 2, U05, dark](../../images/07-payment-risk/u05-accounting/2-order-risk-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f11-21-order-risk-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f11-21-order-risk-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f11-21-order-risk-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f11-21-order-risk-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f11-21-order-risk-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f11-21-order-risk-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f11-21-order-risk-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f11-21-order-risk-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Order, amount, score, signals | E-F11-16 | decision |

## Actions

| Action | Who | Result |
|---|---|---|
| Accept | accounting | Ships |
| Cancel | accounting | Refunded, shopper told |

## States

- Normal: review orders held for fraud risk with their signals.
- Empty: "No order held".
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: decided orders.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F11-16 Fraud check](../../data/e-f11-16-fraud-check.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F11-16 Fraud check | Accepted | Badge "Accepted"; a new record starts here; next: Held (UC-F11-21); fields editable within the role | U05 | `u05-accounting/s-f11-21-order-risk-e-f11-16-fraud-check-accepted-desktop-{light,dark}.png` |
| E-F11-16 Fraud check | Held | Badge "Held"; next: Accepted (UC-F11-21); fields editable within the role | U05 | `u05-accounting/s-f11-21-order-risk-e-f11-16-fraud-check-held-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop and phone.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F11-07 Payment risk](../../flows/fl-f11-07-payment-risk.md)

## Open questions

None.

---

⬅️ [S-F11-20 Shop assistant](../05-grow-the-shop/s-f11-20-shop-assistant.md) · ⬆️ [Up](README.md) ·
➡️ [S-F11-22 Chargebacks](s-f11-22-chargebacks.md)
