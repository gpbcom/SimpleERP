🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🩺 [SC09 Health practices](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC09-07 Pharmacy, eyewear, vets, dental and health centres](README.md) ›
🖥️ S-SC09-25 Health centre

# 🖥️ S-SC09-25 Health centre

**Status:** ✅ specified

## Personas

- [U33 Medical secretary](../../../../01-users/personas/u33-medical-secretary.md): the counts and the bookings of the
  centre.
- [U13 Owner](../../../../01-users/personas/u13-owner.md): the activity, the targets and the reports.

## Purpose

Count the activity of the centre, compare it with the health project and send the report to the regional health agency.

## Entry points

Health practice › Centre activity; the director's workspace; the AI assistant.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Health centre Les Pins: October 2026                                 Confirmed   [Send report]   |
| Profession     Visits   Patients   Hours   Target visits   Gap                                   |
| Doctors        820      410        640     800             +20                                   |
| Nurses         310      180        380     350             -40                                   |
| Dentists       110       62        120     120             -10                                   |
| Comment on the nurses' gap: one nurse on leave     Agency acknowledgement: -                     |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC09-07 step 5, U33 | desktop | ![FL-SC09-07 step 5, U33, light](../../images/07-pharmacy-vets-dental-and-centres/u33-medical-secretary/5-health-centre-desktop-light.png) | ![FL-SC09-07 step 5, U33, dark](../../images/07-pharmacy-vets-dental-and-centres/u33-medical-secretary/5-health-centre-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc09-25-health-centre-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc09-25-health-centre-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc09-25-health-centre-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc09-25-health-centre-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc09-25-health-centre-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc09-25-health-centre-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc09-25-health-centre-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc09-25-health-centre-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Period | E-SC09-18 period | month or year | yes while Draft | yes |
| Profession | E-SC09-18 profession | choice | no | yes |
| Visits and patients | E-SC09-18 visits, patients | numbers | no | no |
| Hours | E-SC09-18 hours | number | no | no |
| Target and gap | E-SC09-18 target | numbers | yes while Draft | no |
| Comment | E-SC09-18 comment | text | yes while Draft | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Count | header | secretary, director | the figures of the period from the records |
| Confirm | header | director | the activity becomes Confirmed |
| Send | header | director | the report goes to the agency and becomes Reported |
| Reopen | header | director | a Reported period is corrected and sent again |

## States

- Normal: the visits, patients, hours and targets per profession, the comments and the sending state.
- Empty: No period yet, with Count a period.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a visit without
  a practitioner or a failed sending, with the record to correct.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC09-18 Centre activity](../../data/e-sc09-18-centre-activity.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC09-18 Centre activity | Draft | Badge "Draft"; a new record starts here; next: Confirmed (UC-SC09-25); fields editable within the role | U33, U13 | `u33-medical-secretary/s-sc09-25-health-centre-e-sc09-18-centre-activity-draft-desktop-{light,dark}.png`, `u13-owner/s-sc09-25-health-centre-e-sc09-18-centre-activity-draft-{desktop,phone}-{light,dark}.png` |
| E-SC09-18 Centre activity | Confirmed | Badge "Confirmed"; next: Reported (BR-SC09-20); fields editable within the role | U33, U13 | `u33-medical-secretary/s-sc09-25-health-centre-e-sc09-18-centre-activity-confirmed-desktop-{light,dark}.png`, `u13-owner/s-sc09-25-health-centre-e-sc09-18-centre-activity-confirmed-{desktop,phone}-{light,dark}.png` |
| E-SC09-18 Centre activity | Reported | Badge "Reported"; next: Draft (UC-SC09-25); fields editable within the role | U33, U13 | `u33-medical-secretary/s-sc09-25-health-centre-e-sc09-18-centre-activity-reported-desktop-{light,dark}.png`, `u13-owner/s-sc09-25-health-centre-e-sc09-18-centre-activity-reported-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC09-07](../../flows/fl-sc09-07-pharmacy-vets-dental-and-centres.md)

## Open questions

None.

---

⬅️ [S-SC09-24 Dental quotes](s-sc09-24-dental-quotes.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC09-26 Multi-professional practice](s-sc09-26-msp.md)
