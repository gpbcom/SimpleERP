🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F9-04 Grow](README.md) ›
🖥️ S-F9-11 Appraisals and skills

# 🖥️ S-F9-11 Appraisals and skills

**Status:** ✅ specified

## Personas

- [U02 Manager](../../../../01-users/personas/u02-manager.md)
- [U01 Employee](../../../../01-users/personas/u01-employee.md)
- [U06 HR](../../../../01-users/personas/u06-hr.md)

## Purpose

Run appraisals and track skills.

## Entry points

HR and projects in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F9-04 step 1, U02 | desktop | ![FL-F9-04 step 1, U02, light](../../images/04-grow/u02-manager/1-appraisals-desktop-light.png) | ![FL-F9-04 step 1, U02, dark](../../images/04-grow/u02-manager/1-appraisals-desktop-dark.png) |
| FL-F9-04 step 1, U02 | phone | ![FL-F9-04 step 1, U02, light](../../images/04-grow/u02-manager/1-appraisals-phone-light.png) | ![FL-F9-04 step 1, U02, dark](../../images/04-grow/u02-manager/1-appraisals-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f09-11-appraisals-and-skills-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f09-11-appraisals-and-skills-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f09-11-appraisals-and-skills-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f09-11-appraisals-and-skills-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f09-11-appraisals-and-skills-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f09-11-appraisals-and-skills-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f09-11-appraisals-and-skills-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f09-11-appraisals-and-skills-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Run appraisals and track skills, as the wireframe shows.
- Empty: No appraisal yet, with Start a campaign.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: validated or signed records; other employees' records outside the user's record rules.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F9-11 Appraisal](../../data/e-f09-11-appraisal.md),
[E-F9-12 Qualification](../../data/e-f09-12-certification.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F9-11 Appraisal | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U01, U02, U06 | `u01-employee/s-f09-11-appraisals-and-skills-e-f09-11-appraisal-active-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f09-11-appraisals-and-skills-e-f09-11-appraisal-active-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f09-11-appraisals-and-skills-e-f09-11-appraisal-active-desktop-{light,dark}.png` |
| E-F9-12 Qualification | To verify | Badge "To verify"; a new record starts here; next: Verified or Rejected (UC-F9-33, BR-F9-27); fields editable within the role | U01, U02, U06 | `u01-employee/s-f09-11-appraisals-and-skills-e-f09-12-certification-to-verify-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f09-11-appraisals-and-skills-e-f09-12-certification-to-verify-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f09-11-appraisals-and-skills-e-f09-12-certification-to-verify-desktop-{light,dark}.png` |
| E-F9-12 Qualification | Verified | Badge "Verified"; a new record starts here; next: Expired (UC-F12-22); fields editable within the role | U01, U02, U06 | `u01-employee/s-f09-11-appraisals-and-skills-e-f09-12-certification-verified-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f09-11-appraisals-and-skills-e-f09-12-certification-verified-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f09-11-appraisals-and-skills-e-f09-12-certification-verified-desktop-{light,dark}.png` |
| E-F9-12 Qualification | Rejected | Badge "Rejected"; final: read-only, no next state; the history shows how it got here | U01, U02, U06 | `u01-employee/s-f09-11-appraisals-and-skills-e-f09-12-certification-rejected-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f09-11-appraisals-and-skills-e-f09-12-certification-rejected-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f09-11-appraisals-and-skills-e-f09-12-certification-rejected-desktop-{light,dark}.png` |
| E-F9-12 Qualification | Expired | Badge "Expired"; next: To verify (UC-F9-33); fields editable within the role | U01, U02, U06 | `u01-employee/s-f09-11-appraisals-and-skills-e-f09-12-certification-expired-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f09-11-appraisals-and-skills-e-f09-12-certification-expired-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f09-11-appraisals-and-skills-e-f09-12-certification-expired-desktop-{light,dark}.png` |

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

- [FL-F9-04 Grow](../../flows/fl-f09-04-grow.md)

## Open questions

None.

---

⬅️ [S-F9-10 Attendance](../03-time/s-f09-10-attendance.md) · ⬆️ [Up](README.md) ·
➡️ [S-F9-12 Fleet](../05-workplace-services/s-f09-12-fleet.md)
