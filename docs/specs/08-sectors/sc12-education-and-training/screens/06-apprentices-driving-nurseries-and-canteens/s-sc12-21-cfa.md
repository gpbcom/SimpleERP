🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🎓 [SC12 Education and training](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC12-06 Apprentices, driving schools, nurseries, canteens](README.md) ›
🖥️ S-SC12-21 Apprentice training centre

# 🖥️ S-SC12-21 Apprentice training centre

**Status:** ✅ specified

## Personas

- [U38 Training coordinator](../../../../01-users/personas/u38-training-coordinator.md): the contracts, claims and
  schedules of the centre.
- [U01 Employee](../../../../01-users/personas/u01-employee.md): their schedule and absences.

## Purpose

Record the apprenticeship contracts, read the support level and claim the funding from the OPCO in instalments,
pro rata of the days done (Code du travail R6332-25).

## Entry points

Education and training › Apprenticeship contracts; the course session; the apprentice's phone.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Contract AC-2026-0217: Lea Martin, sales diploma          Registered   [Claim an instalment]     |
| Employer Atelier Faure   OPCO Commerce   2026-09-01 to 2028-08-31   Level 7,500.00 a year        |
| Instalment   Due          Amount     State                                                       |
| 1st, 40 %    2026-10-01   3,000.00   Paid                                                        |
| 2nd, 30 %    2027-03      2,250.00   Planned                                                     |
| 3rd, 20 %    2027-06      1,500.00   Planned                                                     |
| Balance      2027-08        750.00   Planned                                                     |
| Year 1: pro rata of the days done           Total claimed 3,000.00                               |
| Break date -      Documents 5 of 6     [Send to the OPCO]                                        |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC12-06 step 1, U38 | desktop | ![FL-SC12-06 step 1, U38, light](../../images/06-apprentices-driving-nurseries-and-canteens/u38-training-coordinator/1-cfa-desktop-light.png) | ![FL-SC12-06 step 1, U38, dark](../../images/06-apprentices-driving-nurseries-and-canteens/u38-training-coordinator/1-cfa-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc12-21-cfa-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc12-21-cfa-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc12-21-cfa-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc12-21-cfa-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc12-21-cfa-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc12-21-cfa-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc12-21-cfa-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc12-21-cfa-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Apprentice and employer | E-SC12-20 apprentice, employer | links | yes while Draft | yes |
| Diploma | E-SC12-20 diploma | choice | yes while Draft | yes |
| Dates | E-SC12-20 start, end | dates | yes while Draft | yes |
| OPCO | E-SC12-20 OPCO | choice | yes while Draft | yes |
| Support level | E-SC12-20 support level | amount a year | yes while Draft | yes |
| Instalments claimed | E-SC12-20 months claimed, E-SC12-05 funding lines | 40 % within 30 days of the first invoice, 30 % in the seventh month, 20 % in the tenth month, then the balance, each pro rata of the days done | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Send to the OPCO | contract | training coordinator | the contract waits for the OPCO's answer |
| Claim an instalment | contract | training coordinator | a funding line for the instalment due, pro rata of the days done |
| Record a break | contract | training coordinator | the contract becomes Broken with its date; the funding goes on pro rata of the days for up to six months while the apprentice stays in the centre, or until a new contract |
| End | contract | training coordinator | the contract becomes Ended |

## States

- Normal: the contract, its level, its dates and its instalments with their due dates, amounts and state.
- Empty: No contract yet, with New contract.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a missing level
  or a claim for days after the funding's end (six months after the break, or the new contract), with the field to correct.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC12-20 Apprenticeship contract](../../data/e-sc12-20-apprenticeship-contract.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC12-20 Apprenticeship contract | Draft | Badge "Draft"; a new record starts here; next: Registered (UC-SC12-21); fields editable within the role | U38, U01 | `u38-training-coordinator/s-sc12-21-cfa-e-sc12-20-apprenticeship-contract-draft-desktop-{light,dark}.png`, `u01-employee/s-sc12-21-cfa-e-sc12-20-apprenticeship-contract-draft-{desktop,phone}-{light,dark}.png` |
| E-SC12-20 Apprenticeship contract | Registered | Badge "Registered"; next: Broken or Ended (UC-SC12-21); fields editable within the role | U38, U01 | `u38-training-coordinator/s-sc12-21-cfa-e-sc12-20-apprenticeship-contract-registered-desktop-{light,dark}.png`, `u01-employee/s-sc12-21-cfa-e-sc12-20-apprenticeship-contract-registered-{desktop,phone}-{light,dark}.png` |
| E-SC12-20 Apprenticeship contract | Broken | Badge "Broken"; final: read-only, no next state; the history shows how it got here | U38, U01 | `u38-training-coordinator/s-sc12-21-cfa-e-sc12-20-apprenticeship-contract-broken-desktop-{light,dark}.png`, `u01-employee/s-sc12-21-cfa-e-sc12-20-apprenticeship-contract-broken-{desktop,phone}-{light,dark}.png` |
| E-SC12-20 Apprenticeship contract | Ended | Badge "Ended"; final: read-only, no next state; the history shows how it got here | U38, U01 | `u38-training-coordinator/s-sc12-21-cfa-e-sc12-20-apprenticeship-contract-ended-desktop-{light,dark}.png`, `u01-employee/s-sc12-21-cfa-e-sc12-20-apprenticeship-contract-ended-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

The coordinator works on a desktop; the apprentice, the instructor and the parents use the phone, with the same actions
in one column.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC12-06](../../flows/fl-sc12-06-apprentices-driving-nurseries-and-canteens.md)

## Open questions

None.

---

⬅️ [S-SC12-20 Training assistant](../03-deliver-and-assess/s-sc12-20-training-assistant.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC12-22 Driving school](s-sc12-22-driving-school.md)
