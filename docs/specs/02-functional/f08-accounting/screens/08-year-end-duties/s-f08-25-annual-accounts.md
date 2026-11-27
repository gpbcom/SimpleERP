🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📒 [F8 Accounting](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F8-08 Year-end duties](README.md) ›
🖥️ S-F8-25 Annual accounts

# 🖥️ S-F8-25 Annual accounts

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U08 External accountant](../../../../01-users/personas/u08-external-accountant.md)

## Purpose

Draft, approve and file the annual accounts.

## Entry points

Accounting › Annual accounts.

## Wireframe

```text
+------------------------------------------------------------------+
| Annual accounts 2026        deadline 2027-06-30                   |
| 1 Draft      balance sheet, income statement, notes   done        |
| 2 Approve    meeting 2027-05-20, minutes [upload]     done        |
| 3 Allocate   reserves 20,000, dividends 60,000        posted      |
| 4 File       registry                                 [File]      |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F8-08 step 4, U13 | desktop | ![FL-F8-08 step 4, U13, light](../../images/08-year-end-duties/u13-owner/4-annual-accounts-desktop-light.png) | ![FL-F8-08 step 4, U13, dark](../../images/08-year-end-duties/u13-owner/4-annual-accounts-desktop-dark.png) |
| FL-F8-08 step 4, U13 | phone | ![FL-F8-08 step 4, U13, light](../../images/08-year-end-duties/u13-owner/4-annual-accounts-phone-light.png) | ![FL-F8-08 step 4, U13, dark](../../images/08-year-end-duties/u13-owner/4-annual-accounts-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f08-25-annual-accounts-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f08-25-annual-accounts-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f08-25-annual-accounts-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f08-25-annual-accounts-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f08-25-annual-accounts-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f08-25-annual-accounts-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f08-25-annual-accounts-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f08-25-annual-accounts-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Documents, approval, allocation, filing | E-F8-22 | through the steps |

## Actions

| Action | Who | Result |
|---|---|---|
| File | accounting | Filed with the registry |

## States

- Normal: draft, approve and file the annual accounts.
- Empty: the year is not closed: "Close the year first".
- Loading: placeholders in the steps.
- Error: the error message pattern (D122).
- Read-only: a filed year.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F8-22 Annual accounts file](../../data/e-f08-22-annual-accounts-file.md),
[E-F8-10 Fiscal period](../../data/e-f08-10-fiscal-period.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F8-22 Annual accounts file | Draft | Badge "Draft"; a new record starts here; next: Approved (UC-F8-25); fields editable within the role | U08, U13 | `u08-external-accountant/s-f08-25-annual-accounts-e-f08-22-annual-accounts-file-draft-desktop-{light,dark}.png`, `u13-owner/s-f08-25-annual-accounts-e-f08-22-annual-accounts-file-draft-{desktop,phone}-{light,dark}.png` |
| E-F8-22 Annual accounts file | Approved | Badge "Approved"; next: Filed (UC-F8-25); fields editable within the role | U08, U13 | `u08-external-accountant/s-f08-25-annual-accounts-e-f08-22-annual-accounts-file-approved-desktop-{light,dark}.png`, `u13-owner/s-f08-25-annual-accounts-e-f08-22-annual-accounts-file-approved-{desktop,phone}-{light,dark}.png` |
| E-F8-22 Annual accounts file | Filed | Badge "Filed"; final: read-only, no next state; the history shows how it got here | U08, U13 | `u08-external-accountant/s-f08-25-annual-accounts-e-f08-22-annual-accounts-file-filed-desktop-{light,dark}.png`, `u13-owner/s-f08-25-annual-accounts-e-f08-22-annual-accounts-file-filed-{desktop,phone}-{light,dark}.png` |
| E-F8-10 Fiscal period | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U08, U13 | `u08-external-accountant/s-f08-25-annual-accounts-e-f08-10-fiscal-period-active-desktop-{light,dark}.png`, `u13-owner/s-f08-25-annual-accounts-e-f08-10-fiscal-period-active-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-13 Stepper](../../../../04-ux/design-system/components/c-13-stepper.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F8-08 Year-end duties](../../flows/fl-f08-08-year-end-duties.md)

## Open questions

None.

---

⬅️ [S-F8-24 Corporate tax](s-f08-24-corporate-tax.md) · ⬆️ [Up](README.md) ·
➡️ [S-F8-26 Doubtful debts](s-f08-26-doubtful-debts.md)
