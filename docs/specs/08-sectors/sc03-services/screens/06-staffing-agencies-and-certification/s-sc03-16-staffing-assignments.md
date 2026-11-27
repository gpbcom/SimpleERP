🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💼 [SC03 Services](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC03-06 Staffing, agencies, certification and tender library](README.md) ›
🖥️ S-SC03-16 Staffing assignments

# 🖥️ S-SC03-16 Staffing assignments

**Status:** 🔄 waiting for the owner

## Personas

- [U24 Engagement manager](../../../../01-users/personas/u24-engagement-manager.md): every assignment of the agency.
- [U14 Field worker](../../../../01-users/personas/u14-field-worker.md): their own contract and hours.

## Purpose

Create assignments, send the contracts, follow the signatures against the deadline and see the hours approved.

## Entry points

Services › Assignment contracts; the AI assistant; the worker's app for the worker.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Assignment AC-2026-317: Karim D. at Maison Lorrain                Sent   [Save] [Resend]         |
| Reason  Replacement of an absent employee    Job  Warehouse operator   2026-11-16 to 2026-12-18  |
| Pay 13.40 EUR/h   Client's pay for the job 13.40 EUR/h   Coefficient 1.85   Billing 24.79 EUR/h  |
| Worker contract  sent 2026-11-16   sign before 2026-11-18   not signed                           |
| Placement contract  signed by the client 2026-11-16                                              |
| Hours  week 47: 35.00 declared, approved   Total length 32 days of 548 allowed                   |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC03-06 step 1, U24 | desktop | ![FL-SC03-06 step 1, U24, light](../../images/06-staffing-agencies-and-certification/u24-engagement-manager/1-staffing-assignments-desktop-light.png) | ![FL-SC03-06 step 1, U24, dark](../../images/06-staffing-agencies-and-certification/u24-engagement-manager/1-staffing-assignments-desktop-dark.png) |
| FL-SC03-06 step 1, U24 | phone | ![FL-SC03-06 step 1, U24, light](../../images/06-staffing-agencies-and-certification/u24-engagement-manager/1-staffing-assignments-phone-light.png) | ![FL-SC03-06 step 1, U24, dark](../../images/06-staffing-agencies-and-certification/u24-engagement-manager/1-staffing-assignments-phone-dark.png) |
| Error E1, U24 | desktop | ![Error E1, U24, light](../../images/06-staffing-agencies-and-certification/u24-engagement-manager/e1-the-contract-is-late-desktop-light.png) | ![Error E1, U24, dark](../../images/06-staffing-agencies-and-certification/u24-engagement-manager/e1-the-contract-is-late-desktop-dark.png) |
| Error E1, U24 | phone | ![Error E1, U24, light](../../images/06-staffing-agencies-and-certification/u24-engagement-manager/e1-the-contract-is-late-phone-light.png) | ![Error E1, U24, dark](../../images/06-staffing-agencies-and-certification/u24-engagement-manager/e1-the-contract-is-late-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc03-16-staffing-assignments-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc03-16-staffing-assignments-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc03-16-staffing-assignments-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc03-16-staffing-assignments-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc03-16-staffing-assignments-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc03-16-staffing-assignments-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc03-16-staffing-assignments-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc03-16-staffing-assignments-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Worker | E-SC03-17 worker | link | no | yes |
| Client | E-SC03-17 client | link | no | yes |
| Reason for use | E-SC03-17 reason | choice | yes while Draft | yes |
| Job and dates | E-SC03-17 job, dates | text and two dates | yes while Draft | yes |
| Pay and billing | E-SC03-17 pay, coefficient | amounts | yes while Draft | yes |
| Worker deadline and signature | E-SC03-17 sign-by, signed on | dates | no | no |
| Client signature | E-SC03-17 client signed on | date | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Send contracts | header | engagement manager | both contracts go out and the deadline is set |
| Resend | contract | engagement manager | a new link to the worker |
| Extend | assignment | engagement manager | an amendment, checked against the maximum length |
| End | assignment | engagement manager | the contract is Ended and the papers prepared |

## States

- Normal: the assignment with its reason, pay, billing rate, both signatures and the deadline.
- Empty: No assignment yet, with New assignment.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a late
  contract, a pay below the client's or a renewal beyond the limit, with the date or amount.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC03-17 Assignment contract](../../data/e-sc03-17-assignment-contract.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC03-17 Assignment contract | Draft | Badge "Draft"; a new record starts here; next: Sent or Cancelled (UC-SC03-16); fields editable within the role | U24, U14 | `u24-engagement-manager/s-sc03-16-staffing-assignments-e-sc03-17-assignment-contract-draft-{desktop,phone}-{light,dark}.png`, `u14-field-worker/s-sc03-16-staffing-assignments-e-sc03-17-assignment-contract-draft-phone-{light,dark}.png` |
| E-SC03-17 Assignment contract | Sent | Badge "Sent"; next: Signed or Overdue (BR-SC03-16); fields editable within the role | U24, U14 | `u24-engagement-manager/s-sc03-16-staffing-assignments-e-sc03-17-assignment-contract-sent-{desktop,phone}-{light,dark}.png`, `u14-field-worker/s-sc03-16-staffing-assignments-e-sc03-17-assignment-contract-sent-phone-{light,dark}.png` |
| E-SC03-17 Assignment contract | Signed | Badge "Signed"; next: Ended (UC-SC03-16); fields editable within the role | U24, U14 | `u24-engagement-manager/s-sc03-16-staffing-assignments-e-sc03-17-assignment-contract-signed-{desktop,phone}-{light,dark}.png`, `u14-field-worker/s-sc03-16-staffing-assignments-e-sc03-17-assignment-contract-signed-phone-{light,dark}.png` |
| E-SC03-17 Assignment contract | Overdue | Badge "Overdue"; next: Signed (UC-SC03-16); fields editable within the role | U24, U14 | `u24-engagement-manager/s-sc03-16-staffing-assignments-e-sc03-17-assignment-contract-overdue-{desktop,phone}-{light,dark}.png`, `u14-field-worker/s-sc03-16-staffing-assignments-e-sc03-17-assignment-contract-overdue-phone-{light,dark}.png` |
| E-SC03-17 Assignment contract | Ended | Badge "Ended"; final: read-only, no next state; the history shows how it got here | U24, U14 | `u24-engagement-manager/s-sc03-16-staffing-assignments-e-sc03-17-assignment-contract-ended-{desktop,phone}-{light,dark}.png`, `u14-field-worker/s-sc03-16-staffing-assignments-e-sc03-17-assignment-contract-ended-phone-{light,dark}.png` |
| E-SC03-17 Assignment contract | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U24, U14 | `u24-engagement-manager/s-sc03-16-staffing-assignments-e-sc03-17-assignment-contract-cancelled-{desktop,phone}-{light,dark}.png`, `u14-field-worker/s-sc03-16-staffing-assignments-e-sc03-17-assignment-contract-cancelled-phone-{light,dark}.png` |

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

- [FL-SC03-06](../../flows/fl-sc03-06-staffing-agencies-and-certification.md)

## Open questions

None.

---

⬅️ [S-SC03-15 Engagement assistant](../03-deliver-and-record/s-sc03-15-engagement-assistant.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC03-17 Agency approvals](s-sc03-17-agency-approvals.md)
