🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🎭 [SC16 Events and culture](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC16-03 People and partners](README.md) › 🖥️ S-SC16-09 Shifts

# 🖥️ S-SC16-09 Shifts

**Status:** ✅ specified

## Personas

- [U43 Event producer](../../../../01-users/personas/u43-event-producer.md)
- [U32 Volunteer](../../../../01-users/personas/u32-volunteer.md)

## Purpose

Used to plan staff and volunteer shifts
([UC-SC16-09](../../use-cases/03-people-and-partners/uc-sc16-09-plan-staff-and-volunteer-shifts.md)).

## Entry points

Events and culture in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC16-03 step 2, U43 | desktop | ![FL-SC16-03 step 2, U43, light](../../images/03-people-and-partners/u43-event-producer/2-shifts-desktop-light.png) | ![FL-SC16-03 step 2, U43, dark](../../images/03-people-and-partners/u43-event-producer/2-shifts-desktop-dark.png) |
| FL-SC16-03 step 2, U43 | phone | ![FL-SC16-03 step 2, U43, light](../../images/03-people-and-partners/u43-event-producer/2-shifts-phone-light.png) | ![FL-SC16-03 step 2, U43, dark](../../images/03-people-and-partners/u43-event-producer/2-shifts-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc16-09-shifts-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc16-09-shifts-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc16-09-shifts-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc16-09-shifts-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc16-09-shifts-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc16-09-shifts-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc16-09-shifts-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc16-09-shifts-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC16-10 Staffing post](../../data/e-sc16-10-staffing-post.md), shown as the entity pages list them,
with their examples.

## Actions

- Define posts: [UC-SC16-09](../../use-cases/03-people-and-partners/uc-sc16-09-plan-staff-and-volunteer-shifts.md), step
  1.
- Assign: [UC-SC16-09](../../use-cases/03-people-and-partners/uc-sc16-09-plan-staff-and-volunteer-shifts.md), step 2.
- Confirm: [UC-SC16-09](../../use-cases/03-people-and-partners/uc-sc16-09-plan-staff-and-volunteer-shifts.md), step 3.
- Check coverage: [UC-SC16-09](../../use-cases/03-people-and-partners/uc-sc16-09-plan-staff-and-volunteer-shifts.md),
  step 4.

## States

- Normal: posts, shifts, people and gaps.
- Empty: "No post".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a gap: it is shown.
- Read-only: volunteers see their own.
- Offline: the shift list stays readable on the phone; changes wait.

Shown entities (VD-15): [E-SC16-10 Staffing post](../../data/e-sc16-10-staffing-post.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC16-10 Staffing post | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U32, U43 | `u32-volunteer/s-sc16-09-shifts-e-sc16-10-staffing-post-active-phone-{light,dark}.png`, `u43-event-producer/s-sc16-09-shifts-e-sc16-10-staffing-post-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC16-03 People and partners](../../flows/fl-sc16-03-people-and-partners.md)

## Open questions

None.

---

⬅️ [S-SC16-08 Accreditations](s-sc16-08-accreditations.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC16-10 Sponsors](s-sc16-10-sponsors.md)
