🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💼 [SC03 Services](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC03-03 Deliver and record](README.md) › 🖥️ S-SC03-05 Timesheets

# 🖥️ S-SC03-05 Timesheets

**Status:** ✅ specified

## Personas

- [U16 Office worker](../../../../01-users/personas/u16-office-worker.md)
- [U24 Engagement manager](../../../../01-users/personas/u24-engagement-manager.md)

## Purpose

Used to record and approve time and expenses
([UC-SC03-05](../../use-cases/03-deliver-and-record/uc-sc03-05-record-and-approve-time-and-expenses.md)).

## Entry points

Services in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC03-03 step 1, U16 | phone | ![FL-SC03-03 step 1, U16, light](../../images/03-deliver-and-record/u16-office-worker/1-timesheet-phone-light.png) | ![FL-SC03-03 step 1, U16, dark](../../images/03-deliver-and-record/u16-office-worker/1-timesheet-phone-dark.png) |
| FL-SC03-03 step 1, U16 | desktop | ![FL-SC03-03 step 1, U16, light](../../images/03-deliver-and-record/u16-office-worker/1-timesheet-desktop-light.png) | ![FL-SC03-03 step 1, U16, dark](../../images/03-deliver-and-record/u16-office-worker/1-timesheet-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc03-05-timesheets-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc03-05-timesheets-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc03-05-timesheets-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc03-05-timesheets-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc03-05-timesheets-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc03-05-timesheets-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc03-05-timesheets-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc03-05-timesheets-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC03-05 Timesheet](../../data/e-sc03-05-timesheet.md),
[E-SC03-06 Rebillable cost](../../data/e-sc03-06-rebillable-cost.md), shown as the entity pages list them, with their
examples.

## Actions

- Enter time and expenses:
  [UC-SC03-05](../../use-cases/03-deliver-and-record/uc-sc03-05-record-and-approve-time-and-expenses.md), step 1.
- Submit: [UC-SC03-05](../../use-cases/03-deliver-and-record/uc-sc03-05-record-and-approve-time-and-expenses.md), step
  2.
- Approve or reject:
  [UC-SC03-05](../../use-cases/03-deliver-and-record/uc-sc03-05-record-and-approve-time-and-expenses.md), step 3.
- Release to billing and pay:
  [UC-SC03-05](../../use-cases/03-deliver-and-record/uc-sc03-05-record-and-approve-time-and-expenses.md), step 4.

## States

- Normal: the week per engagement and day, expenses with receipts, and each line's state.
- Empty: "No time this week", with Copy last week.
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a missing week: the consultant is reminded.
- Read-only: an approved week is read-only.
- Offline: the week typed on the phone is kept and submitted when the network is back,
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).

Shown entities (VD-15): [E-SC03-05 Timesheet](../../data/e-sc03-05-timesheet.md),
[E-SC03-06 Rebillable cost](../../data/e-sc03-06-rebillable-cost.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC03-05 Timesheet | Submitted | Badge "Submitted"; next: Approved or Rejected (UC-SC03-05); fields editable within the role | U16, U24 | `u16-office-worker/s-sc03-05-timesheets-e-sc03-05-timesheet-submitted-{desktop,phone}-{light,dark}.png`, `u24-engagement-manager/s-sc03-05-timesheets-e-sc03-05-timesheet-submitted-{desktop,phone}-{light,dark}.png` |
| E-SC03-05 Timesheet | Approved | Badge "Approved"; final: read-only, no next state; the history shows how it got here | U16, U24 | `u16-office-worker/s-sc03-05-timesheets-e-sc03-05-timesheet-approved-{desktop,phone}-{light,dark}.png`, `u24-engagement-manager/s-sc03-05-timesheets-e-sc03-05-timesheet-approved-{desktop,phone}-{light,dark}.png` |
| E-SC03-06 Rebillable cost | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U16, U24 | `u16-office-worker/s-sc03-05-timesheets-e-sc03-06-rebillable-cost-active-{desktop,phone}-{light,dark}.png`, `u24-engagement-manager/s-sc03-05-timesheets-e-sc03-06-rebillable-cost-active-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-SC03-03 Deliver and record](../../flows/fl-sc03-03-deliver-and-record.md)

## Open questions

None.

---

⬅️ [S-SC03-04 Resource plan](../02-staff-and-plan/s-sc03-04-resource-plan.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC03-06 T&M billing](../04-bill-and-recognise/s-sc03-06-t-m-billing.md)
