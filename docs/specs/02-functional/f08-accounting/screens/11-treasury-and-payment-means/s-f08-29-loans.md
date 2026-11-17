🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📒 [F8 Accounting](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ S-F8-29 Loans

# 🖥️ S-F8-29 Loans

**Status:** 🔄 waiting for the owner

## Personas

- [U31 Treasurer](../../../../01-users/personas/u31-treasurer.md): the loans they manage.
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md): the entries and the period-end accruals.

## Purpose

Record a loan, see its schedule and its balance, and follow its instalments and its interest.

## Entry points

Accounting › Loans; a bank line's Match to a loan action; the AI assistant.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Loan: Banque du Nord 2026                 Active     Balance 187,400 EUR   Due in 1 year 17,000|
|---------------------------------------------------------------------------------------------|
| Amount 200,000 EUR   Rate 3.20 percent fixed   Term 120 months   First due 2026-12-05        |
| DUE         PRINCIPAL   INTEREST   INSTALMENT   BALANCE     BANK LINE                       |
| 2026-12-05  1,417.00    533.00     1,950.00      198,583.00  matched                        |
| 2027-01-05  1,420.77    529.23     1,950.00      197,162.23  planned                        |
| Accrued interest at 2026-12-31: 468.50 EUR       [Add early repayment] [Rebuild the schedule]|
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F8-11 step 1, U31 | desktop | ![FL-F8-11 step 1, U31, light](../../images/11-treasury-and-payment-means/u31-treasurer/1-loans-desktop-light.png) | ![FL-F8-11 step 1, U31, dark](../../images/11-treasury-and-payment-means/u31-treasurer/1-loans-desktop-dark.png) |
| FL-F8-11 step 1, U31 | phone | ![FL-F8-11 step 1, U31, light](../../images/11-treasury-and-payment-means/u31-treasurer/1-loans-phone-light.png) | ![FL-F8-11 step 1, U31, dark](../../images/11-treasury-and-payment-means/u31-treasurer/1-loans-phone-dark.png) |
| Error E1, U31 | desktop | ![Error E1, U31, light](../../images/11-treasury-and-payment-means/u31-treasurer/e1-the-repayment-schedule-does-not-add-up-desktop-light.png) | ![Error E1, U31, dark](../../images/11-treasury-and-payment-means/u31-treasurer/e1-the-repayment-schedule-does-not-add-up-desktop-dark.png) |
| Error E1, U31 | phone | ![Error E1, U31, light](../../images/11-treasury-and-payment-means/u31-treasurer/e1-the-repayment-schedule-does-not-add-up-phone-light.png) | ![Error E1, U31, dark](../../images/11-treasury-and-payment-means/u31-treasurer/e1-the-repayment-schedule-does-not-add-up-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f08-29-loans-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f08-29-loans-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f08-29-loans-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f08-29-loans-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f08-29-loans-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f08-29-loans-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f08-29-loans-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f08-29-loans-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Lender and contract | E-F8-34 | text and file | yes while Draft | yes |
| Amount, rate, term | E-F8-34 | amount, percent, months | yes while Draft | yes |
| Repayment type | E-F8-34 | list | yes while Draft | yes |
| Schedule | E-F8-34 schedule | table | no | yes |
| Balance and due within one year | E-F8-34 | two amounts | no | yes |
| Accrued interest | E-F8-03 | amount with currency | no | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Approve | header | treasurer | the loan becomes Active and the schedule is fixed |
| Add early repayment | header | treasurer | the schedule is rebuilt |
| Match an instalment | row | treasurer, accounting | a bank line is posted as principal and interest |
| Rebuild the schedule | header | treasurer | a new schedule from a date, for a new rate |

## States

- Normal: the loan's terms, the schedule with the instalments matched and planned, and the balance.
- Empty: No loan yet, with Add a loan.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a schedule that
  does not add up shows the difference on the last line.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F8-34 Loan](../../data/e-f08-34-loan.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F8-34 Loan | Draft | Badge "Draft"; a new record starts here; next: Active or Cancelled (UC-F8-30); fields editable within the role | U31, U05 | `u31-treasurer/s-f08-29-loans-e-f08-34-loan-draft-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-f08-29-loans-e-f08-34-loan-draft-desktop-{light,dark}.png` |
| E-F8-34 Loan | Active | Badge "Active"; next: Repaid (UC-F8-30); fields editable within the role | U31, U05 | `u31-treasurer/s-f08-29-loans-e-f08-34-loan-active-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-f08-29-loans-e-f08-34-loan-active-desktop-{light,dark}.png` |
| E-F8-34 Loan | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U31, U05 | `u31-treasurer/s-f08-29-loans-e-f08-34-loan-cancelled-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-f08-29-loans-e-f08-34-loan-cancelled-desktop-{light,dark}.png` |
| E-F8-34 Loan | Repaid | Badge "Repaid"; final: read-only, no next state; the history shows how it got here | U31, U05 | `u31-treasurer/s-f08-29-loans-e-f08-34-loan-repaid-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-f08-29-loans-e-f08-34-loan-repaid-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop only; on a phone, the app asks to continue on a larger screen.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F8-11 Treasury and payment means](../../flows/fl-f08-11-treasury-and-payment-means.md)

## Open questions

None.

---

⬅️ [S-F8-28 Sustainability report](../09-pay-analyse-and-report/s-f08-28-sustainability-report.md) ·
⬆️ [Up](README.md) · ➡️ [S-F8-30 Payment means](s-f08-30-payment-means.md)
