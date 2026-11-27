🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🤲 [SC08 Non-profit association](../../README.md) ›
🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC08-07 Foundations, integration, federations, peer fundraising](README.md) ›
🖥️ S-SC08-21 Grant-making

# 🖥️ S-SC08-21 Grant-making

**Status:** ✅ specified

## Personas

- [U31 Treasurer](../../../../01-users/personas/u31-treasurer.md): the budget of the call, the awards and the tranches
  to pay.
- [U13 Owner](../../../../01-users/personas/u13-owner.md): the committee's vote and the decisions to sign.

## Purpose

Run a call for applications, let the committee decide without conflicts and follow each grant from its agreement to its
report.

## Entry points

Non-profit association › Grant applications; the call's page; the committee's meeting.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Call 2026 Youth projects  Budget 200,000  Awarded 150,000  Applications 118   State: Open        |
| App   Applicant            Asked    Score   Conflicts       Decision                             |
| 17    Association Arc-en-C  30,000   8.4     none            Awarded 30,000                      |
| 41    Club Sports Vallée    25,000   7.9     2 members       Vote pending                        |
| 58    Collectif Réseau      40,000   6.1     none            Declined                            |
| Committee: 9 members, 7 present   Quorum 5   [Open vote] [Record decision] [Prepare agreement]   |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC08-07 step 1, U31 | desktop | ![FL-SC08-07 step 1, U31, light](../../images/07-foundations-integration-and-federations/u31-treasurer/1-grant-making-desktop-light.png) | ![FL-SC08-07 step 1, U31, dark](../../images/07-foundations-integration-and-federations/u31-treasurer/1-grant-making-desktop-dark.png) |
| FL-SC08-07 step 1, U31 | phone | ![FL-SC08-07 step 1, U31, light](../../images/07-foundations-integration-and-federations/u31-treasurer/1-grant-making-phone-light.png) | ![FL-SC08-07 step 1, U31, dark](../../images/07-foundations-integration-and-federations/u31-treasurer/1-grant-making-phone-dark.png) |
| Error E1, U31 | desktop | ![Error E1, U31, light](../../images/07-foundations-integration-and-federations/u31-treasurer/e1-a-member-has-a-conflict-of-interest-desktop-light.png) | ![Error E1, U31, dark](../../images/07-foundations-integration-and-federations/u31-treasurer/e1-a-member-has-a-conflict-of-interest-desktop-dark.png) |
| Error E1, U31 | phone | ![Error E1, U31, light](../../images/07-foundations-integration-and-federations/u31-treasurer/e1-a-member-has-a-conflict-of-interest-phone-light.png) | ![Error E1, U31, dark](../../images/07-foundations-integration-and-federations/u31-treasurer/e1-a-member-has-a-conflict-of-interest-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc08-21-grant-making-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc08-21-grant-making-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc08-21-grant-making-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc08-21-grant-making-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc08-21-grant-making-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc08-21-grant-making-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc08-21-grant-making-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc08-21-grant-making-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Applicant | E-SC08-16 applicant | link | no | yes |
| Amount asked | E-SC08-16 amount asked | amount in EUR | yes while Received | yes |
| Project and purpose | E-SC08-16 project | text | yes while Received | yes |
| Score | E-SC08-16 score | number | committee | no |
| Conflicts | E-SC08-16 conflicts | list of members | no | no |
| Decision | E-SC08-16 decision | awarded, declined | committee | no |
| Amount awarded | E-SC08-16 amount awarded | amount in EUR | yes when Awarded | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Declare interest | committee member's page | committee member | the member is marked for that application |
| Vote | meeting | committee member | the vote counts unless the member has a conflict |
| Record decision | application | foundation manager | the application is Awarded or Declined and the answer is sent |
| Pay tranche | grant | treasurer | the payment is prepared and posted |

## States

- Normal: the applications with their score, conflicts, vote and decision.
- Empty: No application yet, with New call.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a vote of a
  member with a conflict or awards above the budget, with the member or amount.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC08-16 Grant application](../../data/e-sc08-16-grant-application.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC08-16 Grant application | Received | Badge "Received"; a new record starts here; next: Eligible (UC-SC08-21); fields editable within the role | U31, U13 | `u31-treasurer/s-sc08-21-grant-making-e-sc08-16-grant-application-received-{desktop,phone}-{light,dark}.png`, `u13-owner/s-sc08-21-grant-making-e-sc08-16-grant-application-received-{desktop,phone}-{light,dark}.png` |
| E-SC08-16 Grant application | Eligible | Badge "Eligible"; next: Awarded or Declined (BR-SC08-16); fields editable within the role | U31, U13 | `u31-treasurer/s-sc08-21-grant-making-e-sc08-16-grant-application-eligible-{desktop,phone}-{light,dark}.png`, `u13-owner/s-sc08-21-grant-making-e-sc08-16-grant-application-eligible-{desktop,phone}-{light,dark}.png` |
| E-SC08-16 Grant application | Awarded | Badge "Awarded"; next: Paid (UC-SC08-21); fields editable within the role | U31, U13 | `u31-treasurer/s-sc08-21-grant-making-e-sc08-16-grant-application-awarded-{desktop,phone}-{light,dark}.png`, `u13-owner/s-sc08-21-grant-making-e-sc08-16-grant-application-awarded-{desktop,phone}-{light,dark}.png` |
| E-SC08-16 Grant application | Declined | Badge "Declined"; final: read-only, no next state; the history shows how it got here | U31, U13 | `u31-treasurer/s-sc08-21-grant-making-e-sc08-16-grant-application-declined-{desktop,phone}-{light,dark}.png`, `u13-owner/s-sc08-21-grant-making-e-sc08-16-grant-application-declined-{desktop,phone}-{light,dark}.png` |
| E-SC08-16 Grant application | Paid | Badge "Paid"; final: read-only, no next state; the history shows how it got here | U31, U13 | `u31-treasurer/s-sc08-21-grant-making-e-sc08-16-grant-application-paid-{desktop,phone}-{light,dark}.png`, `u13-owner/s-sc08-21-grant-making-e-sc08-16-grant-application-paid-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC08-07](../../flows/fl-sc08-07-foundations-integration-and-federations.md)

## Open questions

None.

---

⬅️ [S-SC08-20 Association assistant](../02-donations-and-receipts/s-sc08-20-association-assistant.md) ·
⬆️ [Up](README.md) · ➡️ [S-SC08-22 Work integration](s-sc08-22-work-integration.md)
