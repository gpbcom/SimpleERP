🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💼 [SC03 Services](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC03-05 Client and people](README.md) › 🖥️ S-SC03-13 Skills

# 🖥️ S-SC03-13 Skills

**Status:** ✅ specified

## Personas

- [U16 Office worker](../../../../01-users/personas/u16-office-worker.md)
- [U06 HR](../../../../01-users/personas/u06-hr.md)

## Purpose

Used to manage consultants' skills and certifications,
[UC-SC03-13](../../use-cases/05-client-and-people/uc-sc03-13-manage-consultants-skills-and-certifications.md).

## Entry points

Services in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC03-05 step 3, U16 | desktop | ![FL-SC03-05 step 3, U16, light](../../images/05-client-and-people/u16-office-worker/3-skills-desktop-light.png) | ![FL-SC03-05 step 3, U16, dark](../../images/05-client-and-people/u16-office-worker/3-skills-desktop-dark.png) |
| FL-SC03-05 step 3, U16 | phone | ![FL-SC03-05 step 3, U16, light](../../images/05-client-and-people/u16-office-worker/3-skills-phone-light.png) | ![FL-SC03-05 step 3, U16, dark](../../images/05-client-and-people/u16-office-worker/3-skills-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc03-13-skills-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc03-13-skills-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc03-13-skills-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc03-13-skills-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc03-13-skills-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc03-13-skills-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc03-13-skills-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc03-13-skills-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC03-11 Skill](../../data/e-sc03-11-skill.md), shown as the entity pages list them, with their
examples.

## Actions

- Update the profile:
  [UC-SC03-13](../../use-cases/05-client-and-people/uc-sc03-13-manage-consultants-skills-and-certifications.md), step 1.
- Validate levels:
  [UC-SC03-13](../../use-cases/05-client-and-people/uc-sc03-13-manage-consultants-skills-and-certifications.md), step 2.
- Plan renewals:
  [UC-SC03-13](../../use-cases/05-client-and-people/uc-sc03-13-manage-consultants-skills-and-certifications.md), step 3.

## States

- Normal: skills and certifications with level, evidence and expiry.
- Empty: "No skill recorded", with Add a skill.
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, an expired certification: the consultant is not staffed on roles
  asking for it ([BR-SC03-13](../../business-rules/br-sc03-13-skills-kept-current.md)).
- Read-only: consultants edit their own; levels are validated by HR.
- Offline: not available offline: office work at a desk on shared engagement figures. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC03-11 Skill](../../data/e-sc03-11-skill.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC03-11 Skill | New | Badge "New"; a new record starts here; next: Validated (UC-SC03-13); fields editable within the role | U06, U16, U24 | `u06-hr/s-sc03-13-skills-e-sc03-11-skill-new-desktop-{light,dark}.png`, `u16-office-worker/s-sc03-13-skills-e-sc03-11-skill-new-{desktop,phone}-{light,dark}.png`, `u24-engagement-manager/s-sc03-13-skills-e-sc03-11-skill-new-{desktop,phone}-{light,dark}.png` |
| E-SC03-11 Skill | Validated | Badge "Validated"; final: read-only, no next state; the history shows how it got here | U06, U16, U24 | `u06-hr/s-sc03-13-skills-e-sc03-11-skill-validated-desktop-{light,dark}.png`, `u16-office-worker/s-sc03-13-skills-e-sc03-11-skill-validated-{desktop,phone}-{light,dark}.png`, `u24-engagement-manager/s-sc03-13-skills-e-sc03-11-skill-validated-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC03-05 Client and people](../../flows/fl-sc03-05-client-and-people.md)

## Open questions

None.

---

⬅️ [S-SC03-12 Satisfaction](s-sc03-12-satisfaction.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC03-14 Foreign billing](../04-bill-and-recognise/s-sc03-14-foreign-billing.md)
