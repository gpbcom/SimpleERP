🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛒 [F6 Customers and sales](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F6-07 Special invoicing](README.md) › 🖥️ S-F6-23 Pro-forma invoice

# 🖥️ S-F6-23 Pro-forma invoice

**Status:** 🔄 waiting for the owner

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Issue pro-forma invoices: from a quote or an order, numbered in their own range and marked "pro-forma, not an invoice"
(UC-F6-22).

## Entry points

Accounting › Pro-forma invoices.

## Wireframe

(Proposed) As drawn here, to confirm with the owner.

```text
+------------------------------------------------------------------+
| Pro-forma invoice                                                |
|------------------------------------------------------------------|
| From quote or order   [Q-2026-118 Brasserie du Parc  v]          |
| Number                PF-2026-014 (own range)                    |
| Marked                Pro-forma, not an invoice                  |
|                               [Preview]  [Issue]                 |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F6-07 step 3, U05 | desktop | ![FL-F6-07 step 3, U05, light](../../images/07-special-invoicing/u05-accounting/3-pro-forma-and-statements-desktop-light.png) | ![FL-F6-07 step 3, U05, dark](../../images/07-special-invoicing/u05-accounting/3-pro-forma-and-statements-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f06-23-pro-forma-invoice-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f06-23-pro-forma-invoice-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f06-23-pro-forma-invoice-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f06-23-pro-forma-invoice-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f06-23-pro-forma-invoice-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f06-23-pro-forma-invoice-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f06-23-pro-forma-invoice-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f06-23-pro-forma-invoice-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Pro-forma | E-F6-15 | at issue |

## Actions

| Action | Who | Result |
|---|---|---|
| Issue pro-forma | accounting | PF number |

## States

- Normal: issue pro-forma invoices.
- Empty: no quote or order to invoice: "No pro-forma to issue".
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: issued pro-formas.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F6-05 Invoice](../../data/e-f06-05-invoice.md),
[E-F6-15 Pro-forma invoice](../../data/e-f06-15-pro-forma-invoice.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F6-05 Invoice | Sent | Badge "Sent"; a new record starts here; next: Received or Refused (UC-F6-06); fields editable within the role | U05 | `u05-accounting/s-f06-23-pro-forma-invoice-e-f06-05-invoice-sent-desktop-{light,dark}.png` |
| E-F6-05 Invoice | Received | Badge "Received"; next: Paid or Refused (UC-F6-06); fields editable within the role | U05 | `u05-accounting/s-f06-23-pro-forma-invoice-e-f06-05-invoice-received-desktop-{light,dark}.png` |
| E-F6-05 Invoice | Paid | Badge "Paid"; next: Draft or Refused (BR-F6-07, UC-F6-06); fields editable within the role | U05 | `u05-accounting/s-f06-23-pro-forma-invoice-e-f06-05-invoice-paid-desktop-{light,dark}.png` |
| E-F6-15 Pro-forma invoice | Issued | Badge "Issued"; a new record starts here; next: Superseded (UC-F6-22); fields editable within the role | U05 | `u05-accounting/s-f06-23-pro-forma-invoice-e-f06-15-pro-forma-invoice-issued-desktop-{light,dark}.png` |
| E-F6-15 Pro-forma invoice | Superseded | Badge "Superseded"; next: Expired (UC-F6-22); fields editable within the role | U05 | `u05-accounting/s-f06-23-pro-forma-invoice-e-f06-15-pro-forma-invoice-superseded-desktop-{light,dark}.png` |
| E-F6-15 Pro-forma invoice | Expired | Badge "Expired"; final: read-only, no next state; the history shows how it got here | U05 | `u05-accounting/s-f06-23-pro-forma-invoice-e-f06-15-pro-forma-invoice-expired-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F6-07 Special invoicing](../../flows/fl-f06-07-special-invoicing.md)

## Open questions

None.

---

⬅️ [S-F6-22 Sales reports](../09-sell-on-the-road-and-steer-sales/s-f06-22-sales-reports.md) · ⬆️ [Up](README.md) ·
➡️ [S-F6-24 Partner programme](../10-partners-contracts-and-warranties/s-f06-24-partner-programme.md)
