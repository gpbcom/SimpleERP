🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏠 [SC04 Home care](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC04-06 Care homes, CESU, agent mode, childcare and nursing](README.md) ›
🖥️ S-SC04-20 Home nursing

# 🖥️ S-SC04-20 Home nursing

**Status:** 🔄 waiting for the owner

## Personas

- [U25 Care coordinator](../../../../01-users/personas/u25-care-coordinator.md): every prescription and act of the
  service.
- [U26 Carer](../../../../01-users/personas/u26-carer.md): the acts they perform today.

## Purpose

Record prescriptions, plan and perform acts against them, and prepare the bill for the health insurance.

## Entry points

Home care › Care acts; the carer's day list on the phone; the AI assistant.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Prescription P-2026-118: Dr Henri B., Jeanne R.                       Valid   [Add act]          |
| Acts  Dressing, daily     From 2026-11-01 to 2026-11-28     Acts 28   Done 12   Left 16          |
| Act of 2026-11-12  09:10  Aisha T. (nursing assistant), nurse Lea F.   Signed by the patient     |
| Act of 2026-11-13  09:05  Aisha T.   Done     Act of 2026-11-14  planned                         |
| Bill  12 acts ready for the health insurance                       [Prepare the bill]            |
| Renewal needed in 14 days   [Ask the doctor]                                                     |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC04-06 step 5, U25 | desktop | ![FL-SC04-06 step 5, U25, light](../../images/06-care-homes-cesu-and-nursing/u25-care-coordinator/5-home-nursing-desktop-light.png) | ![FL-SC04-06 step 5, U25, dark](../../images/06-care-homes-cesu-and-nursing/u25-care-coordinator/5-home-nursing-desktop-dark.png) |
| FL-SC04-06 step 5, U25 | phone | ![FL-SC04-06 step 5, U25, light](../../images/06-care-homes-cesu-and-nursing/u25-care-coordinator/5-home-nursing-phone-light.png) | ![FL-SC04-06 step 5, U25, dark](../../images/06-care-homes-cesu-and-nursing/u25-care-coordinator/5-home-nursing-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc04-20-home-nursing-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc04-20-home-nursing-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc04-20-home-nursing-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc04-20-home-nursing-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc04-20-home-nursing-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc04-20-home-nursing-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc04-20-home-nursing-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc04-20-home-nursing-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Patient | E-SC04-18 patient | link | no | yes |
| Prescription | E-SC04-18 prescription | prescriber, date, acts, period | yes while Planned | yes |
| Act | E-SC04-18 act | choice | yes while Planned | yes |
| Performed by | E-SC04-18 performer | carer and coordinating nurse | yes while Planned | yes |
| Time and note | E-SC04-18 time, note | date, time and text | yes while Planned | no |
| Patient signature | E-SC04-18 signed on | date and time | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Add prescription | header | coordinator | a prescription with its acts and period |
| Plan act | prescription | coordinator | an act as a visit, if the prescription allows |
| Record act | act | carer | the act becomes Done |
| Prepare the bill | header | coordinator | the acts done go to the health insurance bill |

## States

- Normal: the prescription with its acts allowed, done and left, and each act with its performer and signature.
- Empty: No prescription yet, with Add a prescription.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); an ended
  prescription or an act outside the performer's qualification, with what to do.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC04-18 Care act](../../data/e-sc04-18-care-act.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC04-18 Care act | Planned | Badge "Planned"; a new record starts here; next: Done or Cancelled (UC-SC04-20); fields editable within the role | U25, U26 | `u25-care-coordinator/s-sc04-20-home-nursing-e-sc04-18-care-act-planned-{desktop,phone}-{light,dark}.png`, `u26-carer/s-sc04-20-home-nursing-e-sc04-18-care-act-planned-phone-{light,dark}.png` |
| E-SC04-18 Care act | Done | Badge "Done"; next: Billed (UC-SC04-20); fields editable within the role | U25, U26 | `u25-care-coordinator/s-sc04-20-home-nursing-e-sc04-18-care-act-done-{desktop,phone}-{light,dark}.png`, `u26-carer/s-sc04-20-home-nursing-e-sc04-18-care-act-done-phone-{light,dark}.png` |
| E-SC04-18 Care act | Billed | Badge "Billed"; final: read-only, no next state; the history shows how it got here | U25, U26 | `u25-care-coordinator/s-sc04-20-home-nursing-e-sc04-18-care-act-billed-{desktop,phone}-{light,dark}.png`, `u26-carer/s-sc04-20-home-nursing-e-sc04-18-care-act-billed-phone-{light,dark}.png` |
| E-SC04-18 Care act | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U25, U26 | `u25-care-coordinator/s-sc04-20-home-nursing-e-sc04-18-care-act-cancelled-{desktop,phone}-{light,dark}.png`, `u26-carer/s-sc04-20-home-nursing-e-sc04-18-care-act-cancelled-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

The coordinator works on a desktop; the carer and the family use the phone, with the same actions in one column.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC04-06](../../flows/fl-sc04-06-care-homes-cesu-and-nursing.md)

## Open questions

None.

---

⬅️ [S-SC04-19 Childcare](s-sc04-19-childcare.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC04-L01 Care recipients](../00-lists/s-sc04-l01-care-recipients.md)
