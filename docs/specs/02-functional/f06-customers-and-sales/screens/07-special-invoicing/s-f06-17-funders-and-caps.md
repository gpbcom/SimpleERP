🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛒 [F6 Customers and sales](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F6-07 Special invoicing](README.md) › 🖥️ S-F6-17 Funders and caps

# 🖥️ S-F6-17 Funders and caps

**Status:** ✅ specified

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)
- [U25 Care coordinator](../../../../01-users/personas/u25-care-coordinator.md)
- [U38 Training coordinator](../../../../01-users/personas/u38-training-coordinator.md)

## Purpose

Set funder agreements and see each payer's share per invoice.

## Entry points

Accounting › Funders; a beneficiary's record.

## Wireframe

```text
+------------------------------------------------------------------+
| Mme Roche   November 2026: 46 h at 25 EUR                         |
| Payer                  Share   Cap         Used    Invoiced       |
| Département du Rhône   70 %    40 h/month  40 h    700 EUR        |
| Mme Roche              rest    -           -       450 EUR        |
| Agreement ends 2026-12-31                    [Issue invoices]     |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F6-07 step 2, U05 | desktop | ![FL-F6-07 step 2, U05, light](../../images/07-special-invoicing/u05-accounting/2-funders-and-caps-desktop-light.png) | ![FL-F6-07 step 2, U05, dark](../../images/07-special-invoicing/u05-accounting/2-funders-and-caps-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f06-17-funders-and-caps-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f06-17-funders-and-caps-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f06-17-funders-and-caps-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f06-17-funders-and-caps-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f06-17-funders-and-caps-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f06-17-funders-and-caps-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f06-17-funders-and-caps-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f06-17-funders-and-caps-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Payers, share, cap, used, invoiced | E-F6-14 | agreements |

## Actions

| Action | Who | Result |
|---|---|---|
| Issue invoices | accounting | One invoice per payer |

## States

- Normal: set funder agreements and see each payer's share per invoice.
- Empty: no funder: "The beneficiary pays everything" with Add a funder.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: for coordinators, who read.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F6-05 Invoice](../../data/e-f06-05-invoice.md),
[E-F6-14 Funder agreement](../../data/e-f06-14-funder-agreement.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F6-05 Invoice | Sent | Badge "Sent"; a new record starts here; next: Received or Refused (UC-F6-06); fields editable within the role | U05 | `u05-accounting/s-f06-17-funders-and-caps-e-f06-05-invoice-sent-desktop-{light,dark}.png` |
| E-F6-05 Invoice | Received | Badge "Received"; next: Paid or Refused (UC-F6-06); fields editable within the role | U05 | `u05-accounting/s-f06-17-funders-and-caps-e-f06-05-invoice-received-desktop-{light,dark}.png` |
| E-F6-05 Invoice | Paid | Badge "Paid"; next: Draft or Refused (BR-F6-07, UC-F6-06); fields editable within the role | U05 | `u05-accounting/s-f06-17-funders-and-caps-e-f06-05-invoice-paid-desktop-{light,dark}.png` |
| E-F6-14 Funder agreement | Active | Badge "Active"; a new record starts here; next: Expired (UC-F6-20); fields editable within the role | U05 | `u05-accounting/s-f06-17-funders-and-caps-e-f06-14-funder-agreement-active-desktop-{light,dark}.png` |
| E-F6-14 Funder agreement | Expired | Badge "Expired"; final: read-only, no next state; the history shows how it got here | U05 | `u05-accounting/s-f06-17-funders-and-caps-e-f06-14-funder-agreement-expired-desktop-{light,dark}.png` |

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
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F6-07 Special invoicing](../../flows/fl-f06-07-special-invoicing.md)

## Open questions

None.

---

⬅️ [S-F6-16 Credit control](../06-accounts-and-credit/s-f06-16-credit-control.md) · ⬆️ [Up](README.md) ·
➡️ [S-F6-18 Phone order](../09-sell-on-the-road-and-steer-sales/s-f06-18-phone-order.md)
