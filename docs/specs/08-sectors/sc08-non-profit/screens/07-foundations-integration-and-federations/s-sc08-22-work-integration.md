🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🤲 [SC08 Non-profit association](../../README.md) ›
🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC08-07 Foundations, integration, federations, peer fundraising](README.md) ›
🖥️ S-SC08-22 Work integration

# 🖥️ S-SC08-22 Work integration

**Status:** 🔄 waiting for the owner

## Personas

- [U06 Human resources](../../../../01-users/personas/u06-hr.md): the pathways, approvals, steps and the monthly aid
  claim.
- [U01 Employee](../../../../01-users/personas/u01-employee.md): their own steps and appointments.

## Purpose

Follow each person's approval and pathway and compute the aid the approved positions allow.

## Entry points

Non-profit association › Integration pathways; an employee's file; the monthly claim.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Work integration   Structure type: EI   Approved positions 20   In post 21     [Month claim]     |
| Person        Approval to  Hours/month  Step                 State      Aid                      |
| Ms Diallo     2027-05      104          Training Jan         Active     0.69 pos.                |
| M. Laurent    2026-12      151          Work experience      Active     1.00 pos.                |
| Ms Kone       2026-11-05   0            Exit: job            Completed  0.00 pos.                |
| Month: 20.00 positions claimed of 20 approved. 1 person beyond the approval, listed.             |
| Steps for Ms Diallo: [x] Support interview  [ ] Driving theory 14 Jan  [ ] CV workshop           |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC08-07 step 2, U06 | desktop | ![FL-SC08-07 step 2, U06, light](../../images/07-foundations-integration-and-federations/u06-hr/2-work-integration-desktop-light.png) | ![FL-SC08-07 step 2, U06, dark](../../images/07-foundations-integration-and-federations/u06-hr/2-work-integration-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc08-22-work-integration-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc08-22-work-integration-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc08-22-work-integration-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc08-22-work-integration-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc08-22-work-integration-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc08-22-work-integration-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc08-22-work-integration-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc08-22-work-integration-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Person | E-SC08-17 person | link | no | yes |
| Approval | E-SC08-17 approval from, to | dates | yes while Draft | yes |
| Steps | E-SC08-17 steps | list with dates | yes | no |
| Hours | E-SC08-17 hours | number per month | no | no |
| Aid | E-SC08-17 aid | share of a position | no | no |
| Exit result | E-SC08-17 exit | job, training, other | yes when Completed | yes to close |
| Social notes | E-SC08-17 notes | text | yes | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| New pathway | header | HR | a pathway in Draft with the person's approval |
| Confirm step | person's phone | employee | the step is marked done |
| Claim the month | header | HR | the aid per position with the cap shown |
| Record exit | pathway | HR | the pathway is Completed with its result |

## States

- Normal: the pathways with their approval, steps, hours, aid and exit.
- Empty: No pathway yet, with New pathway.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a missing
  approval or an exit with no result, with the field to complete.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC08-17 Integration pathway](../../data/e-sc08-17-integration-pathway.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC08-17 Integration pathway | Draft | Badge "Draft"; a new record starts here; next: Active (BR-SC08-17); fields editable within the role | U06, U01 | `u06-hr/s-sc08-22-work-integration-e-sc08-17-integration-pathway-draft-desktop-{light,dark}.png`, `u01-employee/s-sc08-22-work-integration-e-sc08-17-integration-pathway-draft-{desktop,phone}-{light,dark}.png` |
| E-SC08-17 Integration pathway | Active | Badge "Active"; next: Completed or Ended (UC-SC08-22); fields editable within the role | U06, U01 | `u06-hr/s-sc08-22-work-integration-e-sc08-17-integration-pathway-active-desktop-{light,dark}.png`, `u01-employee/s-sc08-22-work-integration-e-sc08-17-integration-pathway-active-{desktop,phone}-{light,dark}.png` |
| E-SC08-17 Integration pathway | Completed | Badge "Completed"; final: read-only, no next state; the history shows how it got here | U06, U01 | `u06-hr/s-sc08-22-work-integration-e-sc08-17-integration-pathway-completed-desktop-{light,dark}.png`, `u01-employee/s-sc08-22-work-integration-e-sc08-17-integration-pathway-completed-{desktop,phone}-{light,dark}.png` |
| E-SC08-17 Integration pathway | Ended | Badge "Ended"; final: read-only, no next state; the history shows how it got here | U06, U01 | `u06-hr/s-sc08-22-work-integration-e-sc08-17-integration-pathway-ended-desktop-{light,dark}.png`, `u01-employee/s-sc08-22-work-integration-e-sc08-17-integration-pathway-ended-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop for HR. The employee's page on a phone lists their next steps with dates and a Confirm button, without the
social notes.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC08-07](../../flows/fl-sc08-07-foundations-integration-and-federations.md)

## Open questions

None.

---

⬅️ [S-SC08-21 Grant-making](s-sc08-21-grant-making.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC08-23 Federation](s-sc08-23-federation.md)
