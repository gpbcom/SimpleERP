🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🎓 [SC12 Education and training](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC12-01 Offer and sessions](README.md) › 🖥️ S-SC12-01 Catalogue

# 🖥️ S-SC12-01 Catalogue

**Status:** ✅ specified

## Personas

- [U38 Training coordinator](../../../../01-users/personas/u38-training-coordinator.md)

## Purpose

Used to publish the course catalogue
([UC-SC12-01](../../use-cases/01-offer-and-sessions/uc-sc12-01-publish-the-course-catalogue.md)).

## Entry points

Education and training in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC12-01 step 1, U38 | desktop | ![FL-SC12-01 step 1, U38, light](../../images/01-offer-and-sessions/u38-training-coordinator/1-catalogue-desktop-light.png) | ![FL-SC12-01 step 1, U38, dark](../../images/01-offer-and-sessions/u38-training-coordinator/1-catalogue-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc12-01-catalogue-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc12-01-catalogue-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc12-01-catalogue-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc12-01-catalogue-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc12-01-catalogue-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc12-01-catalogue-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc12-01-catalogue-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc12-01-catalogue-offline-desktop-dark.png) |

## Fields and columns

The fields of [E-SC12-01 Course](../../data/e-sc12-01-course.md), shown as the entity pages list them, with their
examples.

## Actions

- Write the course: [UC-SC12-01](../../use-cases/01-offer-and-sessions/uc-sc12-01-publish-the-course-catalogue.md), step
  1.
- Set prices: [UC-SC12-01](../../use-cases/01-offer-and-sessions/uc-sc12-01-publish-the-course-catalogue.md), step 2.
- Check mentions: [UC-SC12-01](../../use-cases/01-offer-and-sessions/uc-sc12-01-publish-the-course-catalogue.md), step
  3.
- Publish: [UC-SC12-01](../../use-cases/01-offer-and-sessions/uc-sc12-01-publish-the-course-catalogue.md), step 4.

## States

- Normal: courses with objectives, programme, duration, price and publication.
- Empty: "No course".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, the programme missing: it is not published.
- Read-only: trainers read the catalogue.
- Offline: not available offline: office work on enrolments, funding and billing. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC12-01 Course](../../data/e-sc12-01-course.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC12-01 Course | New | Badge "New"; a new record starts here; next: Sent (UC-SC12-01); fields editable within the role | U38 | `u38-training-coordinator/s-sc12-01-catalogue-e-sc12-01-course-new-desktop-{light,dark}.png` |
| E-SC12-01 Course | Sent | Badge "Sent"; next: Published (UC-SC12-01); fields editable within the role | U38 | `u38-training-coordinator/s-sc12-01-catalogue-e-sc12-01-course-sent-desktop-{light,dark}.png` |
| E-SC12-01 Course | Published | Badge "Published"; final: read-only, no next state; the history shows how it got here | U38 | `u38-training-coordinator/s-sc12-01-catalogue-e-sc12-01-course-published-desktop-{light,dark}.png` |

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

- [FL-SC12-01 Offer and sessions](../../flows/fl-sc12-01-offer-and-sessions.md)

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [S-SC12-02 Sessions](s-sc12-02-sessions.md)
