🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📒 [F8 Accounting](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F8-08 Year-end duties](README.md) ›
🖥️ S-F8-24 Corporate tax

# 🖥️ S-F8-24 Corporate tax

**Status:** ✅ specified

## Personas

- [U08 External accountant](../../../../01-users/personas/u08-external-accountant.md)
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Compute corporate tax and follow instalments and local business taxes.

## Entry points

Accounting › Taxes › Corporate tax.

## Wireframe

```text
+------------------------------------------------------------------+
| Corporate tax 2026                                                |
| Result 182,000  + adjustments 6,000  = taxable 188,000            |
| Tax 41,250   Instalments paid 36,000   Balance 5,250 on 05-15     |
| CFE 1,840 on 12-15   CVAE -                       [File] [Pay]   |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F8-08 step 2, U08 | desktop | ![FL-F8-08 step 2, U08, light](../../images/08-year-end-duties/u08-external-accountant/2-corporate-tax-desktop-light.png) | ![FL-F8-08 step 2, U08, dark](../../images/08-year-end-duties/u08-external-accountant/2-corporate-tax-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f08-24-corporate-tax-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f08-24-corporate-tax-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f08-24-corporate-tax-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f08-24-corporate-tax-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f08-24-corporate-tax-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f08-24-corporate-tax-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f08-24-corporate-tax-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f08-24-corporate-tax-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Result, adjustments, tax, instalments | E-F8-21 | adjustments |

## Actions

| Action | Who | Result |
|---|---|---|
| File | accountant | Through the EDI partner |
| Pay | accounting | Into the payment run |

## States

- Normal: compute corporate tax and follow instalments and local business taxes.
- Empty: no closed year yet: "Close the year first".
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: a filed year.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F8-21 Corporate tax computation](../../data/e-f08-21-corporate-tax-computation.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F8-21 Corporate tax computation | Draft | Badge "Draft"; a new record starts here; next: Filed (UC-F8-24); fields editable within the role | U08 | `u08-external-accountant/s-f08-24-corporate-tax-e-f08-21-corporate-tax-computation-draft-desktop-{light,dark}.png` |
| E-F8-21 Corporate tax computation | Filed | Badge "Filed"; next: Paid (UC-F8-24); fields editable within the role | U08 | `u08-external-accountant/s-f08-24-corporate-tax-e-f08-21-corporate-tax-computation-filed-desktop-{light,dark}.png` |
| E-F8-21 Corporate tax computation | Paid | Badge "Paid"; final: read-only, no next state; the history shows how it got here | U08 | `u08-external-accountant/s-f08-24-corporate-tax-e-f08-21-corporate-tax-computation-paid-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-04 Card](../../../../04-ux/design-system/components/c-04-card.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F8-08 Year-end duties](../../flows/fl-f08-08-year-end-duties.md)

## Open questions

None.

---

⬅️ [S-F8-23 Non-profit accounts](../07-client-money-grants-and-non-profits/s-f08-23-non-profit-accounts.md) ·
⬆️ [Up](README.md) · ➡️ [S-F8-25 Annual accounts](s-f08-25-annual-accounts.md)
