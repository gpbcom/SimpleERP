🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💇 [SC17 Beauty and wellness](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC17-02 Packages and memberships](README.md) ›
🖥️ S-SC17-08 Customer balances

# 🖥️ S-SC17-08 Customer balances

**Status:** ✅ specified

## Personas

- [U23 Store manager](../../../../01-users/personas/u23-store-manager.md): the balances of every customer of the salon.

## Purpose

Show a customer's sessions, vouchers, points and dues before a sale, and what the salon owes.

## Entry points

Beauty and wellness › Customer balances; the till; the AI assistant.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Balances: Camille R.                                              Open invoices 0.00 EUR         |
| Packages     5 facials: 4 left, valid to 2027-05-21                                              |
| Membership   Glow: 1 facial included this month, used 0                                          |
| Vouchers     G-4471: 18.00 EUR, valid to 2027-11-21                                              |
| Points       120   (Next reward at 200)                                                          |
| [Apply a session]  [Apply the voucher]  [Show the sales history]                                 |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC17-02 step 4, U23 | desktop | ![FL-SC17-02 step 4, U23, light](../../images/02-packages-and-memberships/u23-store-manager/4-customer-balances-desktop-light.png) | ![FL-SC17-02 step 4, U23, dark](../../images/02-packages-and-memberships/u23-store-manager/4-customer-balances-desktop-dark.png) |
| FL-SC17-02 step 4, U23 | phone | ![FL-SC17-02 step 4, U23, light](../../images/02-packages-and-memberships/u23-store-manager/4-customer-balances-phone-light.png) | ![FL-SC17-02 step 4, U23, dark](../../images/02-packages-and-memberships/u23-store-manager/4-customer-balances-phone-dark.png) |
| FL-SC17-02 step 4, U23 | tablet | ![FL-SC17-02 step 4, U23, light](../../images/02-packages-and-memberships/u23-store-manager/4-customer-balances-tablet-light.png) | ![FL-SC17-02 step 4, U23, dark](../../images/02-packages-and-memberships/u23-store-manager/4-customer-balances-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc17-08-customer-balances-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc17-08-customer-balances-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc17-08-customer-balances-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc17-08-customer-balances-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc17-08-customer-balances-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc17-08-customer-balances-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc17-08-customer-balances-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc17-08-customer-balances-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Customer | E-F6-01 customer record | link | no | yes |
| Sessions left | E-SC17-04 sessions left | number per package | no | no |
| Included services | E-SC17-05 included used this month | number | no | no |
| Voucher balance | E-SC17-06 balance | amount | no | no |
| Points | E-F10-10 points | number | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Apply a session | package row | beautician | one session is taken from the oldest package |
| Apply the voucher | voucher row | beautician | the voucher balance is reduced |
| Correct a balance | any row | manager | the balance changes with a reason |

## States

- Normal: the customer's balances with their end dates.
- Empty: The customer holds no package, voucher or points.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a balance that
  does not match its sales, with the figures.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

Desktop first; on a tablet at the till the balances come first.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC17-02 Packages and memberships](../../flows/fl-sc17-02-packages-and-memberships.md)

## Open questions

None.

---

⬅️ [S-SC17-07 Gift vouchers](s-sc17-07-gift-vouchers.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC17-09 Salon retail](../03-salon-retail-and-stock/s-sc17-09-salon-retail.md)
