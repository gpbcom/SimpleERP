🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏪 [F10 Point of sale (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F10-10 Clienteling, transfers and tax-free](README.md) › 🖥️ S-F10-26 Tax-free

# 🖥️ S-F10-26 Tax-free

**Status:** ✅ specified

## Personas

- [U17 Cashier](../../../../01-users/personas/u17-cashier.md)
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Issue a tax-free form for an eligible visitor.

## Entry points

The till › Tax-free on a paid sale.

## Wireframe

```text
+------------------------------------------+
| Tax-free   basket 240.00 EUR (VAT 40.00) |
| Passport [         ] Country [US v]      |
| Eligible: yes (above the minimum)        |
| [Issue the form]                          |
+------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F10-10 step 4, U17 | desktop | ![FL-F10-10 step 4, U17, light](../../images/10-clienteling-transfers-and-tax-free/u17-cashier/4-tax-free-desktop-light.png) | ![FL-F10-10 step 4, U17, dark](../../images/10-clienteling-transfers-and-tax-free/u17-cashier/4-tax-free-desktop-dark.png) |
| FL-F10-10 step 4, U17 | phone | ![FL-F10-10 step 4, U17, light](../../images/10-clienteling-transfers-and-tax-free/u17-cashier/4-tax-free-phone-light.png) | ![FL-F10-10 step 4, U17, dark](../../images/10-clienteling-transfers-and-tax-free/u17-cashier/4-tax-free-phone-dark.png) |
| FL-F10-10 step 4, U17 | tablet | ![FL-F10-10 step 4, U17, light](../../images/10-clienteling-transfers-and-tax-free/u17-cashier/4-tax-free-tablet-light.png) | ![FL-F10-10 step 4, U17, dark](../../images/10-clienteling-transfers-and-tax-free/u17-cashier/4-tax-free-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f10-26-tax-free-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f10-26-tax-free-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f10-26-tax-free-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f10-26-tax-free-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f10-26-tax-free-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f10-26-tax-free-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f10-26-tax-free-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f10-26-tax-free-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Visitor, basket, VAT, status | E-F10-20 | visitor |

## Actions

| Action | Who | Result |
|---|---|---|
| Issue | cashier | Electronic form |

## States

- Normal: issue a tax-free form for an eligible visitor.
- Empty: never: opened on a sale.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: issued forms.
- Offline: Not available offline: the electronic form is issued through the customs system.

Shown entities (VD-15): [E-F10-20 Tax-free form](../../data/e-f10-20-tax-free-form.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F10-20 Tax-free form | Issued | Badge "Issued"; a new record starts here; next: Validated (UC-F10-27); fields editable within the role | U17 | `u17-cashier/s-f10-26-tax-free-e-f10-20-tax-free-form-issued-{desktop,phone,tablet}-{light,dark}.png` |
| E-F10-20 Tax-free form | Validated | Badge "Validated"; next: Refunded or Expired (UC-F10-27); fields editable within the role | U17 | `u17-cashier/s-f10-26-tax-free-e-f10-20-tax-free-form-validated-{desktop,phone,tablet}-{light,dark}.png` |
| E-F10-20 Tax-free form | Refunded | Badge "Refunded"; next: Expired (UC-F10-27); fields editable within the role | U17 | `u17-cashier/s-f10-26-tax-free-e-f10-20-tax-free-form-refunded-{desktop,phone,tablet}-{light,dark}.png` |
| E-F10-20 Tax-free form | Expired | Badge "Expired"; final: read-only, no next state; the history shows how it got here | U17 | `u17-cashier/s-f10-26-tax-free-e-f10-20-tax-free-form-expired-{desktop,phone,tablet}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Till and tablet.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F10-10 Clienteling, transfers and tax-free](../../flows/fl-f10-10-clienteling-transfers-and-tax-free.md)

## Open questions

None.

---

⬅️ [S-F10-25 Store stock and transfers](s-f10-25-store-stock-and-transfers.md) · ⬆️ [Up](README.md) ·
➡️ [S-F10-27 Store reports](../11-store-reports/s-f10-27-store-reports.md)
