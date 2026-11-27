🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💼 [SC03 Services](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC03-02 Staff and plan](README.md) › 🖥️ S-SC03-03 Staffing

# 🖥️ S-SC03-03 Staffing

**Status:** ✅ specified

## Personas

- [U24 Engagement manager](../../../../01-users/personas/u24-engagement-manager.md)

## Purpose

Used to staff the engagement ([UC-SC03-03](../../use-cases/02-staff-and-plan/uc-sc03-03-staff-the-engagement.md)); to
manage consultants' skills and certifications,
[UC-SC03-13](../../use-cases/05-client-and-people/uc-sc03-13-manage-consultants-skills-and-certifications.md).

## Entry points

Services in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC03-02 step 1, U24 | desktop | ![FL-SC03-02 step 1, U24, light](../../images/02-staff-and-plan/u24-engagement-manager/1-staffing-desktop-light.png) | ![FL-SC03-02 step 1, U24, dark](../../images/02-staff-and-plan/u24-engagement-manager/1-staffing-desktop-dark.png) |
| FL-SC03-02 step 1, U24 | phone | ![FL-SC03-02 step 1, U24, light](../../images/02-staff-and-plan/u24-engagement-manager/1-staffing-phone-light.png) | ![FL-SC03-02 step 1, U24, dark](../../images/02-staff-and-plan/u24-engagement-manager/1-staffing-phone-dark.png) |
| Error E1, U24 | desktop | ![Error E1, U24, light](../../images/02-staff-and-plan/u24-engagement-manager/e1-over-allocated-desktop-light.png) | ![Error E1, U24, dark](../../images/02-staff-and-plan/u24-engagement-manager/e1-over-allocated-desktop-dark.png) |
| Error E1, U24 | phone | ![Error E1, U24, light](../../images/02-staff-and-plan/u24-engagement-manager/e1-over-allocated-phone-light.png) | ![Error E1, U24, dark](../../images/02-staff-and-plan/u24-engagement-manager/e1-over-allocated-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc03-03-staffing-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc03-03-staffing-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc03-03-staffing-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc03-03-staffing-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc03-03-staffing-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc03-03-staffing-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc03-03-staffing-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc03-03-staffing-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC03-04 Staffing assignment](../../data/e-sc03-04-staffing-assignment.md),
[E-SC03-11 Skill](../../data/e-sc03-11-skill.md), shown as the entity pages list them, with their examples.

## Actions

- List needs by role: [UC-SC03-03](../../use-cases/02-staff-and-plan/uc-sc03-03-staff-the-engagement.md), step 1.
- Search by skills and dates: [UC-SC03-03](../../use-cases/02-staff-and-plan/uc-sc03-03-staff-the-engagement.md), step
  2.
- Assign: [UC-SC03-03](../../use-cases/02-staff-and-plan/uc-sc03-03-staff-the-engagement.md), step 3.
- Staff on current skills:
  [UC-SC03-13](../../use-cases/05-client-and-people/uc-sc03-13-manage-consultants-skills-and-certifications.md), step 4.

## States

- Normal: the needs by role and the consultants matching with skills, level and free time.
- Empty: "No need open".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, an over-allocation: the owner's approval is asked,
  [BR-SC03-04](../../business-rules/br-sc03-04-staffing-respects-availability.md),
  [BR-F9-21](../../../../02-functional/f09-hr-and-projects/business-rules/br-f09-21-planned-load-stays-within-available-hours.md).
- Read-only: a confirmed assignment changes only by the manager.
- Offline: not available offline: office work at a desk on shared engagement figures. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC03-11 Skill](../../data/e-sc03-11-skill.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC03-11 Skill | New | Badge "New"; a new record starts here; next: Validated (UC-SC03-13); fields editable within the role | U06, U16, U24 | `u06-hr/s-sc03-03-staffing-e-sc03-11-skill-new-desktop-{light,dark}.png`, `u16-office-worker/s-sc03-03-staffing-e-sc03-11-skill-new-{desktop,phone}-{light,dark}.png`, `u24-engagement-manager/s-sc03-03-staffing-e-sc03-11-skill-new-{desktop,phone}-{light,dark}.png` |
| E-SC03-11 Skill | Validated | Badge "Validated"; final: read-only, no next state; the history shows how it got here | U06, U16, U24 | `u06-hr/s-sc03-03-staffing-e-sc03-11-skill-validated-desktop-{light,dark}.png`, `u16-office-worker/s-sc03-03-staffing-e-sc03-11-skill-validated-{desktop,phone}-{light,dark}.png`, `u24-engagement-manager/s-sc03-03-staffing-e-sc03-11-skill-validated-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC03-02 Staff and plan](../../flows/fl-sc03-02-staff-and-plan.md)

## Open questions

None.

---

⬅️ [S-SC03-02 Rate cards](../01-win-and-price/s-sc03-02-rate-cards.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC03-04 Resource plan](s-sc03-04-resource-plan.md)
