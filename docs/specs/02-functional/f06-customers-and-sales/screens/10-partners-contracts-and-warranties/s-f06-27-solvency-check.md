🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛒 [F6 Customers and sales](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ S-F6-27 Solvency check

# 🖥️ S-F6-27 Solvency check

**Status:** 🔄 waiting for the owner

## Personas

- [U03 Sales](../../../../01-users/personas/u03-sales.md): the customers they sell to.
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md): the customers with open credit.

## Purpose

Ask for a solvency report, read it and set the limit and the terms from it.

## Entry points

Customers and sales › a customer › Solvency; an order held for its limit.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Solvency: Bois et Fils            Report of 2026-11-14, valid to 2027-02-12   [Ask a new one]|
|---------------------------------------------------------------------------------------------|
| Provider  CreditInfo     Score 7 of 10     Recommended limit 15,000 EUR                     |
| Reasons   Paid on time 11 of 12 invoices; 3 years old; no collective procedure              |
| Current limit 10,000 EUR      New limit [12,000]   Terms [45 days]   Reason [..........]    |
| Orders held: 1 (SO-2318, 4,200 EUR)                                      [Save and release] |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F6-10 step 4, U03 | desktop | ![FL-F6-10 step 4, U03, light](../../images/10-partners-contracts-and-warranties/u03-sales/4-solvency-check-desktop-light.png) | ![FL-F6-10 step 4, U03, dark](../../images/10-partners-contracts-and-warranties/u03-sales/4-solvency-check-desktop-dark.png) |
| FL-F6-10 step 4, U03 | phone | ![FL-F6-10 step 4, U03, light](../../images/10-partners-contracts-and-warranties/u03-sales/4-solvency-check-phone-light.png) | ![FL-F6-10 step 4, U03, dark](../../images/10-partners-contracts-and-warranties/u03-sales/4-solvency-check-phone-dark.png) |
| FL-F6-10 step 4, U03 | tablet | ![FL-F6-10 step 4, U03, light](../../images/10-partners-contracts-and-warranties/u03-sales/4-solvency-check-tablet-light.png) | ![FL-F6-10 step 4, U03, dark](../../images/10-partners-contracts-and-warranties/u03-sales/4-solvency-check-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f06-27-solvency-check-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f06-27-solvency-check-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f06-27-solvency-check-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f06-27-solvency-check-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f06-27-solvency-check-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f06-27-solvency-check-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f06-27-solvency-check-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f06-27-solvency-check-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Provider and date | E-F6-26 | name and date | no | yes |
| Score and recommended limit | E-F6-26 | number and amount | no | yes |
| Reasons | E-F6-26 | text | no | no |
| Current limit | E-F6-12 | amount with currency | no | yes |
| New limit and terms | E-F6-12 | amount and days | yes | yes |
| Reason | E-F6-12 | text | yes | when above the recommendation |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Ask a new report | header | sales, accounting | a request to the provider |
| Save and release | header | sales, accounting | limit and terms saved; held orders released |
| Open the provider's report | row | sales, accounting | the full report, read-only |

## States

- Normal: the latest report, the current limit and the form for the new limit and terms.
- Empty: No report yet, with Ask a report.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a provider that
  does not answer shows the retry and the date of the last good report.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F6-26 Solvency report](../../data/e-f06-26-solvency-report.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F6-26 Solvency report | Requested | Badge "Requested"; a new record starts here; next: Received or Failed (UC-F6-30); fields editable within the role | U03, U05 | `u03-sales/s-f06-27-solvency-check-e-f06-26-solvency-report-requested-{desktop,phone,tablet}-{light,dark}.png`, `u05-accounting/s-f06-27-solvency-check-e-f06-26-solvency-report-requested-desktop-{light,dark}.png` |
| E-F6-26 Solvency report | Received | Badge "Received"; next: Expired (BR-F6-22); fields editable within the role | U03, U05 | `u03-sales/s-f06-27-solvency-check-e-f06-26-solvency-report-received-{desktop,phone,tablet}-{light,dark}.png`, `u05-accounting/s-f06-27-solvency-check-e-f06-26-solvency-report-received-desktop-{light,dark}.png` |
| E-F6-26 Solvency report | Failed | Badge "Failed"; next: Requested (UC-F6-30); fields editable within the role | U03, U05 | `u03-sales/s-f06-27-solvency-check-e-f06-26-solvency-report-failed-{desktop,phone,tablet}-{light,dark}.png`, `u05-accounting/s-f06-27-solvency-check-e-f06-26-solvency-report-failed-desktop-{light,dark}.png` |
| E-F6-26 Solvency report | Expired | Badge "Expired"; final: read-only, no next state; the history shows how it got here | U03, U05 | `u03-sales/s-f06-27-solvency-check-e-f06-26-solvency-report-expired-{desktop,phone,tablet}-{light,dark}.png`, `u05-accounting/s-f06-27-solvency-check-e-f06-26-solvency-report-expired-desktop-{light,dark}.png` |

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

- [FL-F6-10](../../flows/fl-f06-10-partners-contracts-and-warranties.md)

## Open questions

None.

---

⬅️ [S-F6-26 Frame contracts](s-f06-26-frame-contracts.md) · ⬆️ [Up](README.md) ·
➡️ [S-F6-28 Warranty claims](s-f06-28-warranty-claims.md)
