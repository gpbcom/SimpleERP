🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛒 [F6 Customers and sales](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F6-08 Collect and settle](README.md) › 🖥️ S-F6-20 Instalments and disputes

# 🖥️ S-F6-20 Instalments and disputes

**Status:** ✅ specified

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)
- [U03 Sales](../../../../01-users/personas/u03-sales.md)

## Purpose

Agree instalment plans and settle disputes.

## Entry points

Accounting › Instalments and disputes.

## Wireframe

```text
+------------------------------------------------------------------+
| [Instalments] [Disputes (2)]                                      |
| Dispute INV-2026-1184  line 3  86 EUR  "2 crates missing"        |
|   Reminders paused on 86 EUR      [Credit note] [Reject] [Mixed]  |
| Plan Brasserie du Parc  3 x 1,400  next 2026-12-15  kept          |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F6-08 step 1, U05 | desktop | ![FL-F6-08 step 1, U05, light](../../images/08-collect-and-settle/u05-accounting/1-instalments-and-disputes-desktop-light.png) | ![FL-F6-08 step 1, U05, dark](../../images/08-collect-and-settle/u05-accounting/1-instalments-and-disputes-desktop-dark.png) |
| Error E1, U05 | desktop | ![Error E1, U05, light](../../images/08-collect-and-settle/u05-accounting/e1-instalments-and-disputes-refused-desktop-light.png) | ![Error E1, U05, dark](../../images/08-collect-and-settle/u05-accounting/e1-instalments-and-disputes-refused-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f06-20-instalments-and-disputes-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f06-20-instalments-and-disputes-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f06-20-instalments-and-disputes-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f06-20-instalments-and-disputes-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f06-20-instalments-and-disputes-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f06-20-instalments-and-disputes-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f06-20-instalments-and-disputes-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f06-20-instalments-and-disputes-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Plans | E-F6-16 | while proposed |
| Disputes | E-F6-17 | outcome |

## Actions

| Action | Who | Result |
|---|---|---|
| Create plan | accounting | Plan to accept |
| Settle | accounting | Credit note or rejection |

## States

- Normal: agree instalment plans and settle disputes.
- Empty: nothing open: "No instalment plan or dispute".
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: for sales: read and comment.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F6-05 Invoice](../../data/e-f06-05-invoice.md),
[E-F6-16 Instalment plan](../../data/e-f06-16-instalment-plan.md),
[E-F6-21 Payment reminder](../../data/e-f06-21-payment-reminder.md),
[E-F6-17 Invoice dispute](../../data/e-f06-17-invoice-dispute.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F6-05 Invoice | Sent | Badge "Sent"; a new record starts here; next: Received or Refused (UC-F6-06); fields editable within the role | U05 | `u05-accounting/s-f06-20-instalments-and-disputes-e-f06-05-invoice-sent-desktop-{light,dark}.png` |
| E-F6-05 Invoice | Received | Badge "Received"; next: Paid or Refused (UC-F6-06); fields editable within the role | U05 | `u05-accounting/s-f06-20-instalments-and-disputes-e-f06-05-invoice-received-desktop-{light,dark}.png` |
| E-F6-05 Invoice | Paid | Badge "Paid"; next: Draft or Refused (BR-F6-07, UC-F6-06); fields editable within the role | U05 | `u05-accounting/s-f06-20-instalments-and-disputes-e-f06-05-invoice-paid-desktop-{light,dark}.png` |
| E-F6-16 Instalment plan | Proposed | Badge "Proposed"; a new record starts here; next: Accepted (UC-F6-23); fields editable within the role | U05 | `u05-accounting/s-f06-20-instalments-and-disputes-e-f06-16-instalment-plan-proposed-desktop-{light,dark}.png` |
| E-F6-16 Instalment plan | Accepted | Badge "Accepted"; next: Done, Broken or Kept (UC-F6-23); fields editable within the role | U05 | `u05-accounting/s-f06-20-instalments-and-disputes-e-f06-16-instalment-plan-accepted-desktop-{light,dark}.png` |
| E-F6-16 Instalment plan | Done | Badge "Done"; final: read-only, no next state; the history shows how it got here | U05 | `u05-accounting/s-f06-20-instalments-and-disputes-e-f06-16-instalment-plan-done-desktop-{light,dark}.png` |
| E-F6-16 Instalment plan | Broken | Badge "Broken"; final: read-only, no next state; the history shows how it got here | U05 | `u05-accounting/s-f06-20-instalments-and-disputes-e-f06-16-instalment-plan-broken-desktop-{light,dark}.png` |
| E-F6-16 Instalment plan | Kept | Badge "Kept"; final: read-only, no next state; the history shows how it got here | U05 | `u05-accounting/s-f06-20-instalments-and-disputes-e-f06-16-instalment-plan-kept-desktop-{light,dark}.png` |
| E-F6-21 Payment reminder | Active | Badge "Active"; a new record starts here; next: Paused or Stopped (UC-F6-24, UC-F6-23, BR-F6-05); fields editable within the role | U05 | `u05-accounting/s-f06-20-instalments-and-disputes-e-f06-21-payment-reminder-active-desktop-{light,dark}.png` |
| E-F6-21 Payment reminder | Paused | Badge "Paused"; next: Active or Stopped (UC-F6-24); fields editable within the role | U05 | `u05-accounting/s-f06-20-instalments-and-disputes-e-f06-21-payment-reminder-paused-desktop-{light,dark}.png` |
| E-F6-21 Payment reminder | Stopped | Badge "Stopped"; final: read-only, no next state; the history shows how it got here | U05 | `u05-accounting/s-f06-20-instalments-and-disputes-e-f06-21-payment-reminder-stopped-desktop-{light,dark}.png` |
| E-F6-17 Invoice dispute | Open | Badge "Open"; a new record starts here; next: Settled (UC-F6-24); fields editable within the role | U05 | `u05-accounting/s-f06-20-instalments-and-disputes-e-f06-17-invoice-dispute-open-desktop-{light,dark}.png` |
| E-F6-17 Invoice dispute | Settled | Badge "Settled"; final: read-only, no next state; the history shows how it got here | U05 | `u05-accounting/s-f06-20-instalments-and-disputes-e-f06-17-invoice-dispute-settled-desktop-{light,dark}.png` |

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

- [FL-F6-08 Collect and settle](../../flows/fl-f06-08-collect-and-settle.md)

## Open questions

None.

---

⬅️ [S-F6-19 Statement of account](../07-special-invoicing/s-f06-19-statement-of-account.md) · ⬆️ [Up](README.md) ·
➡️ [S-F6-21 Targets and commissions](../09-sell-on-the-road-and-steer-sales/s-f06-21-targets-and-commissions.md)
