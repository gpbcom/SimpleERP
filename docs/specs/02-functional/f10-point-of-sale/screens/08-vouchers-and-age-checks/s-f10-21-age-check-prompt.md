🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏪 [F10 Point of sale (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F10-08 Vouchers and age checks](README.md) › 🖥️ S-F10-21 Age check prompt

# 🖥️ S-F10-21 Age check prompt

**Status:** ✅ specified

## Personas

- [U17 Cashier](../../../../01-users/personas/u17-cashier.md)
- [U18 Waiter](../../../../01-users/personas/u18-waiter.md)
- [U44 Box-office agent](../../../../01-users/personas/u44-box-office-agent.md)

## Purpose

Ask the cashier to check the customer's age before a restricted item.

## Entry points

Shown on the till when a restricted item is added.

## Wireframe

```text
+------------------------------------------+
| Age check: Wine 75 cl (18+)              |
| Born before 2008-11-12?                  |
| [Checked: of age]   [Refused: remove]    |
+------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F10-08 step 1, U17 | desktop | ![FL-F10-08 step 1, U17, light](../../images/08-vouchers-and-age-checks/u17-cashier/1-age-check-prompt-desktop-light.png) | ![FL-F10-08 step 1, U17, dark](../../images/08-vouchers-and-age-checks/u17-cashier/1-age-check-prompt-desktop-dark.png) |
| FL-F10-08 step 1, U17 | phone | ![FL-F10-08 step 1, U17, light](../../images/08-vouchers-and-age-checks/u17-cashier/1-age-check-prompt-phone-light.png) | ![FL-F10-08 step 1, U17, dark](../../images/08-vouchers-and-age-checks/u17-cashier/1-age-check-prompt-phone-dark.png) |
| FL-F10-08 step 1, U17 | tablet | ![FL-F10-08 step 1, U17, light](../../images/08-vouchers-and-age-checks/u17-cashier/1-age-check-prompt-tablet-light.png) | ![FL-F10-08 step 1, U17, dark](../../images/08-vouchers-and-age-checks/u17-cashier/1-age-check-prompt-tablet-dark.png) |
| Error E1, U17 | desktop | ![Error E1, U17, light](../../images/08-vouchers-and-age-checks/u17-cashier/e1-age-check-prompt-refused-desktop-light.png) | ![Error E1, U17, dark](../../images/08-vouchers-and-age-checks/u17-cashier/e1-age-check-prompt-refused-desktop-dark.png) |
| Error E1, U17 | phone | ![Error E1, U17, light](../../images/08-vouchers-and-age-checks/u17-cashier/e1-age-check-prompt-refused-phone-light.png) | ![Error E1, U17, dark](../../images/08-vouchers-and-age-checks/u17-cashier/e1-age-check-prompt-refused-phone-dark.png) |
| Error E1, U17 | tablet | ![Error E1, U17, light](../../images/08-vouchers-and-age-checks/u17-cashier/e1-age-check-prompt-refused-tablet-light.png) | ![Error E1, U17, dark](../../images/08-vouchers-and-age-checks/u17-cashier/e1-age-check-prompt-refused-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f10-21-age-check-prompt-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f10-21-age-check-prompt-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f10-21-age-check-prompt-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f10-21-age-check-prompt-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f10-21-age-check-prompt-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f10-21-age-check-prompt-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f10-21-age-check-prompt-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f10-21-age-check-prompt-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Item, required birth date | E-F10-16 | decision |

## Actions

| Action | Who | Result |
|---|---|---|
| Checked | cashier | Sale goes on, logged |
| Refused | cashier | Item removed, logged |

## States

- Normal: ask the cashier to check the customer's age before a restricted item.
- Empty: never: shown only for a restricted item.
- Loading: never: the prompt is local.
- Error: the error message pattern (D122).
- Read-only: always for the date; the cashier decides.
- Offline: Works offline as [BR-F10-06](../../business-rules/br-f10-06-offline-keeps-selling.md); the check is logged
  and synced with the sale.

Shown entities (VD-15): [E-F10-16 Age check](../../data/e-f10-16-age-check.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F10-16 Age check | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U17 | `u17-cashier/s-f10-21-age-check-prompt-e-f10-16-age-check-recorded-{desktop,phone,tablet}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Till, tablet and phone.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-05 Modal](../../../../04-ux/design-system/components/c-05-modal.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F10-08 Vouchers and age checks](../../flows/fl-f10-08-vouchers-and-age-checks.md)

## Open questions

None.

---

⬅️ [S-F10-20 Till assistant](../07-set-up-and-report/s-f10-20-till-assistant.md) · ⬆️ [Up](README.md) ·
➡️ [S-F10-22 Safe and deposits](../09-cash-and-settlements/s-f10-22-safe-and-deposits.md)
