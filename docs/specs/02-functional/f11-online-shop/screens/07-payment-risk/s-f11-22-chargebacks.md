🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛍️ [F11 Online shop (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F11-07 Payment risk](README.md) › 🖥️ S-F11-22 Chargebacks

# 🖥️ S-F11-22 Chargebacks

**Status:** ✅ specified

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Answer chargebacks with evidence before their deadline.

## Entry points

Accounting › Chargebacks.

## Wireframe

```text
+------------------------------------------------------------------+
| Chargebacks                                                       |
| Order        Amount  Reason        Deadline  Evidence     Status  |
| W-2026-1022  640     not received  11-26     tracking ok  to send |
|                                       [Send evidence]             |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F11-07 step 3, U05 | desktop | ![FL-F11-07 step 3, U05, light](../../images/07-payment-risk/u05-accounting/3-chargebacks-desktop-light.png) | ![FL-F11-07 step 3, U05, dark](../../images/07-payment-risk/u05-accounting/3-chargebacks-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f11-22-chargebacks-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f11-22-chargebacks-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f11-22-chargebacks-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f11-22-chargebacks-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f11-22-chargebacks-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f11-22-chargebacks-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f11-22-chargebacks-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f11-22-chargebacks-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Payment, reason, deadline, evidence | E-F11-17 | evidence |

## Actions

| Action | Who | Result |
|---|---|---|
| Send evidence | accounting | Through the provider |

## States

- Normal: answer chargebacks with evidence before their deadline.
- Empty: "No chargeback".
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: closed chargebacks.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F11-17 Chargeback](../../data/e-f11-17-chargeback.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F11-17 Chargeback | Received | Badge "Received"; a new record starts here; next: Won or Lost (UC-F11-22); fields editable within the role | U05 | `u05-accounting/s-f11-22-chargebacks-e-f11-17-chargeback-received-desktop-{light,dark}.png` |
| E-F11-17 Chargeback | Won | Badge "Won"; final: read-only, no next state; the history shows how it got here | U05 | `u05-accounting/s-f11-22-chargebacks-e-f11-17-chargeback-won-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-12 File upload](../../../../04-ux/design-system/components/c-12-file-upload.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F11-07 Payment risk](../../flows/fl-f11-07-payment-risk.md)

## Open questions

None.

---

⬅️ [S-F11-21 Order risk](s-f11-21-order-risk.md) · ⬆️ [Up](README.md) ·
➡️ [S-F11-23 Product content](../08-product-content-and-listings/s-f11-23-product-content.md)
