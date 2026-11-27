🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏠 [SC04 Home care](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC04-05 People and quality](README.md) › 🖥️ S-SC04-12 Quality

# 🖥️ S-SC04-12 Quality

**Status:** ✅ specified

## Personas

- [U25 Care coordinator](../../../../01-users/personas/u25-care-coordinator.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Used to handle quality, complaints and satisfaction,
[UC-SC04-12](../../use-cases/05-people-and-quality/uc-sc04-12-handle-quality-complaints-and-satisfaction.md).

## Entry points

Home care in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC04-05 step 2, U25 | desktop | ![FL-SC04-05 step 2, U25, light](../../images/05-people-and-quality/u25-care-coordinator/2-complaint-desktop-light.png) | ![FL-SC04-05 step 2, U25, dark](../../images/05-people-and-quality/u25-care-coordinator/2-complaint-desktop-dark.png) |
| FL-SC04-05 step 2, U25 | phone | ![FL-SC04-05 step 2, U25, light](../../images/05-people-and-quality/u25-care-coordinator/2-complaint-phone-light.png) | ![FL-SC04-05 step 2, U25, dark](../../images/05-people-and-quality/u25-care-coordinator/2-complaint-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc04-12-quality-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc04-12-quality-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc04-12-quality-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc04-12-quality-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc04-12-quality-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc04-12-quality-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc04-12-quality-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc04-12-quality-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC04-10 Complaint](../../data/e-sc04-10-complaint.md), shown as the entity pages list them, with their
examples.

## Actions

- Record: [UC-SC04-12](../../use-cases/05-people-and-quality/uc-sc04-12-handle-quality-complaints-and-satisfaction.md),
  step 1.
- Answer: [UC-SC04-12](../../use-cases/05-people-and-quality/uc-sc04-12-handle-quality-complaints-and-satisfaction.md),
  step 2.
- Close with an action:
  [UC-SC04-12](../../use-cases/05-people-and-quality/uc-sc04-12-handle-quality-complaints-and-satisfaction.md), step 3.
- Read the quality figures:
  [UC-SC04-12](../../use-cases/05-people-and-quality/uc-sc04-12-handle-quality-complaints-and-satisfaction.md), step 4.

## States

- Normal: complaints with date, subject, answer delay, action and state; survey results.
- Empty: "No complaint".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, the answer is late: the coordinator and the owner are alerted.
- Read-only: a closed complaint is read-only.
- Offline: not available offline: office work at the agency on shared planning and billing data. Offline work is kept
  for the phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC04-10 Complaint](../../data/e-sc04-10-complaint.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC04-10 Complaint | Open | Badge "Open"; a new record starts here; next: Answered (UC-SC04-12); fields editable within the role | U13, U25 | `u13-owner/s-sc04-12-quality-e-sc04-10-complaint-open-{desktop,phone}-{light,dark}.png`, `u25-care-coordinator/s-sc04-12-quality-e-sc04-10-complaint-open-{desktop,phone}-{light,dark}.png` |
| E-SC04-10 Complaint | Answered | Badge "Answered"; next: Closed (UC-SC04-12); fields editable within the role | U13, U25 | `u13-owner/s-sc04-12-quality-e-sc04-10-complaint-answered-{desktop,phone}-{light,dark}.png`, `u25-care-coordinator/s-sc04-12-quality-e-sc04-10-complaint-answered-{desktop,phone}-{light,dark}.png` |
| E-SC04-10 Complaint | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U13, U25 | `u13-owner/s-sc04-12-quality-e-sc04-10-complaint-closed-{desktop,phone}-{light,dark}.png`, `u25-care-coordinator/s-sc04-12-quality-e-sc04-10-complaint-closed-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC04-05 People and quality](../../flows/fl-sc04-05-people-and-quality.md)

## Open questions

None.

---

⬅️ [S-SC04-11 Travel time](../04-bill-and-fund/s-sc04-11-travel-time.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC04-13 Carer skills](s-sc04-13-carer-skills.md)
