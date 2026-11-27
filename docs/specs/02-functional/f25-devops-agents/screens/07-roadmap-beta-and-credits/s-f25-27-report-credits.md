🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F25-07 Roadmap, beta, credits and changelog](README.md) › 🖥️ S-F25-27 Report credits

# 🖥️ S-F25-27 Report credits

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md): the credits of the company, by report.
- [U47 SimpleERP maintainer](../../../../01-users/personas/u47-simpleerp-maintainer.md): the reports to confirm and
  grant, and the totals.

## Purpose

Show the credits earned by confirmed reports, grant them and see them on the bill.

## Entry points

DevOps agents › Report credits; a confirmed report; the hosted bill.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Report credits                      Pending 2   Granted 1   Applied this year 3   Total 110 EUR |
|---------------------------------------------------------------------------------------------|
| REPORT   COMPANY  SEVERITY  AMOUNT  REASON                        BILL        STATE         |
| #313     Acme     Medium    25 EUR  first confirmed report        2026-12     Granted       |
| #318     Acme     -         0 EUR   duplicate of #290             -           Refused       |
| #321     Norte    High      50 EUR  waits for the fix             -           Pending       |
| [Grant] [Refuse with reason] [Open report] [Open bill]                                      |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F25-07 step 3, U07 | desktop | ![FL-F25-07 step 3, U07, light](../../images/07-roadmap-beta-and-credits/u07-administrator/3-report-credits-desktop-light.png) | ![FL-F25-07 step 3, U07, dark](../../images/07-roadmap-beta-and-credits/u07-administrator/3-report-credits-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f25-27-report-credits-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f25-27-report-credits-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f25-27-report-credits-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f25-27-report-credits-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f25-27-report-credits-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f25-27-report-credits-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f25-27-report-credits-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f25-27-report-credits-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Report | E-F25-18 report | link | no | yes |
| Severity | E-F25-18 severity | badge | no | yes |
| Amount | E-F25-18 amount | amount with currency | maintainer | yes |
| Reason | E-F25-18 reason | text | maintainer | yes |
| Bill | E-F25-18 bill | month | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Grant | row | maintainer | grants a Pending credit once the fix is merged |
| Refuse with reason | row | maintainer | refuses the credit and tells the reporter why |
| Open report | row | maintainer, administrator | opens the ticket the credit is for |
| Open bill | row | administrator, accounting | opens the bill that carries the credit |

## States

- Normal: the credits with report, severity, amount, reason, bill and state.
- Empty: No credit yet, with how to report a bug.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a refused
  credit shows the earlier report for a duplicate, or what is missing to reproduce.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F25-18 Report credit](../../data/e-f25-18-report-credit.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F25-18 Report credit | Pending | Badge "Pending"; a new record starts here; next: Granted or Refused (BR-F25-20); fields editable within the role | U07, U47 | `u07-administrator/s-f25-27-report-credits-e-f25-18-report-credit-pending-desktop-{light,dark}.png`, `u47-simpleerp-maintainer/s-f25-27-report-credits-e-f25-18-report-credit-pending-{desktop,phone}-{light,dark}.png` |
| E-F25-18 Report credit | Granted | Badge "Granted"; next: Applied or Withdrawn (UC-F25-27); fields editable within the role | U07, U47 | `u07-administrator/s-f25-27-report-credits-e-f25-18-report-credit-granted-desktop-{light,dark}.png`, `u47-simpleerp-maintainer/s-f25-27-report-credits-e-f25-18-report-credit-granted-{desktop,phone}-{light,dark}.png` |
| E-F25-18 Report credit | Refused | Badge "Refused"; final: read-only, no next state; the history shows how it got here | U07, U47 | `u07-administrator/s-f25-27-report-credits-e-f25-18-report-credit-refused-desktop-{light,dark}.png`, `u47-simpleerp-maintainer/s-f25-27-report-credits-e-f25-18-report-credit-refused-{desktop,phone}-{light,dark}.png` |
| E-F25-18 Report credit | Applied | Badge "Applied"; final: read-only, no next state; the history shows how it got here | U07, U47 | `u07-administrator/s-f25-27-report-credits-e-f25-18-report-credit-applied-desktop-{light,dark}.png`, `u47-simpleerp-maintainer/s-f25-27-report-credits-e-f25-18-report-credit-applied-{desktop,phone}-{light,dark}.png` |
| E-F25-18 Report credit | Withdrawn | Badge "Withdrawn"; final: read-only, no next state; the history shows how it got here | U07, U47 | `u07-administrator/s-f25-27-report-credits-e-f25-18-report-credit-withdrawn-desktop-{light,dark}.png`, `u47-simpleerp-maintainer/s-f25-27-report-credits-e-f25-18-report-credit-withdrawn-{desktop,phone}-{light,dark}.png` |

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

- [FL-F25-07](../../flows/fl-f25-07-roadmap-beta-and-credits.md)

## Open questions

None.

---

⬅️ [S-F25-26 Beta programme](s-f25-26-beta-programme.md) · ⬆️ [Up](README.md) ·
➡️ [S-F25-28 Module changelog](s-f25-28-module-changelog.md)
