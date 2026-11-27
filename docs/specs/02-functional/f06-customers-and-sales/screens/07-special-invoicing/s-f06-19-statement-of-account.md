🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛒 [F6 Customers and sales](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F6-07 Special invoicing](README.md) › 🖥️ S-F6-19 Statement of account

# 🖥️ S-F6-19 Statement of account

**Status:** ✅ specified

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)
- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

Send statements of account. Pro-forma invoices are issued on [S-F6-23 Pro-forma invoice](s-f06-23-pro-forma-invoice.md).

## Entry points

Accounting › Statements of account.

## Wireframe

```text
+------------------------------------------------------------------+
| Statements of account                                             |
| Statements at [2026-11-30]   80 customers with a balance          |
| Customer            0-30    31-60   61-90   >90    Balance         |
| Brasserie du Parc   2,970   1,240   0       0      4,210          |
|                                  [Preview] [Send all]             |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F6-07 step 3, U05 | desktop | ![FL-F6-07 step 3, U05, light](../../images/07-special-invoicing/u05-accounting/3-pro-forma-and-statements-desktop-light.png) | ![FL-F6-07 step 3, U05, dark](../../images/07-special-invoicing/u05-accounting/3-pro-forma-and-statements-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f06-19-pro-forma-and-statements-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f06-19-pro-forma-and-statements-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f06-19-pro-forma-and-statements-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f06-19-pro-forma-and-statements-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f06-19-pro-forma-and-statements-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f06-19-pro-forma-and-statements-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f06-19-pro-forma-and-statements-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f06-19-pro-forma-and-statements-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Pro-forma | E-F6-15 | at issue |
| Statement | invoices and payments | no |

## Actions

| Action | Who | Result |
|---|---|---|
| Issue pro-forma | accounting | PF number |
| Send statements | accounting | Email or portal |

## States

- Normal: send statements of account.
- Empty: no balance at the date: "No statement to send".
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: sent statements.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F6-05 Invoice](../../data/e-f06-05-invoice.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F6-05 Invoice | Sent | Badge "Sent"; a new record starts here; next: Received or Refused (UC-F6-06); fields editable within the role | U05 | `u05-accounting/s-f06-19-statement-of-account-e-f06-05-invoice-sent-desktop-{light,dark}.png` |
| E-F6-05 Invoice | Received | Badge "Received"; next: Paid or Refused (UC-F6-06); fields editable within the role | U05 | `u05-accounting/s-f06-19-statement-of-account-e-f06-05-invoice-received-desktop-{light,dark}.png` |
| E-F6-05 Invoice | Paid | Badge "Paid"; next: Draft or Refused (BR-F6-07, UC-F6-06); fields editable within the role | U05 | `u05-accounting/s-f06-19-statement-of-account-e-f06-05-invoice-paid-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-07 Tabs](../../../../04-ux/design-system/components/c-07-tabs.md)
- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F6-07 Special invoicing](../../flows/fl-f06-07-special-invoicing.md)
- [FL-F6-08 Collect and settle](../../flows/fl-f06-08-collect-and-settle.md)

## Open questions

None.

---

⬅️ [S-F6-18 Phone order](../09-sell-on-the-road-and-steer-sales/s-f06-18-phone-order.md) · ⬆️ [Up](README.md) ·
➡️ [S-F6-20 Instalments and disputes](../08-collect-and-settle/s-f06-20-instalments-and-disputes.md)
