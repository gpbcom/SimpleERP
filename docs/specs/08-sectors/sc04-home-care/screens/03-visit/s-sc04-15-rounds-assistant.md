🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏠 [SC04 Home care](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC04-03 Visit](README.md) › 🖥️ S-SC04-15 Rounds assistant

# 🖥️ S-SC04-15 Rounds assistant

**Status:** 🔄 waiting for the owner

## Personas

- [U25 Care coordinator](../../../../01-users/personas/u25-care-coordinator.md)
- [U26 Carer](../../../../01-users/personas/u26-carer.md)

## Purpose

Used to ask the AI assistant about the rounds
([UC-SC04-15](../../use-cases/03-visit/uc-sc04-15-ask-the-assistant-about-the-rounds.md)).

## Entry points

Home care in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC04-03 step 3, U25 | phone | ![FL-SC04-03 step 3, U25, light](../../images/03-visit/u25-care-coordinator/3-assistant-phone-light.png) | ![FL-SC04-03 step 3, U25, dark](../../images/03-visit/u25-care-coordinator/3-assistant-phone-dark.png) |
| FL-SC04-03 step 3, U25 | desktop | ![FL-SC04-03 step 3, U25, light](../../images/03-visit/u25-care-coordinator/3-assistant-desktop-light.png) | ![FL-SC04-03 step 3, U25, dark](../../images/03-visit/u25-care-coordinator/3-assistant-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc04-15-rounds-assistant-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc04-15-rounds-assistant-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc04-15-rounds-assistant-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc04-15-rounds-assistant-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc04-15-rounds-assistant-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc04-15-rounds-assistant-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc04-15-rounds-assistant-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc04-15-rounds-assistant-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC04-04 Visit](../../data/e-sc04-04-visit.md),
[E-F9-26 Round](../../../../02-functional/f09-hr-and-projects/data/e-f09-26-round.md), shown
as the entity pages list them, with their examples.

## Actions

- Ask about gaps: [UC-SC04-15](../../use-cases/03-visit/uc-sc04-15-ask-the-assistant-about-the-rounds.md), step 1.
- Confirm a replacement: [UC-SC04-15](../../use-cases/03-visit/uc-sc04-15-ask-the-assistant-about-the-rounds.md), step
  4.

## States

- Normal: the conversation with answers, links and prepared actions.
- Empty: suggested questions about today's rounds.
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, health details beyond the user's rights: the AI assistant refuses
  ([BR-SC04-04](../../business-rules/br-sc04-04-health-data-hosted-and-restricted.md)).
- Read-only: no health detail beyond the role.
- Offline: not available offline: the AI assistant needs the network; the last answers stay readable.

Shown entities (VD-15): [E-SC04-04 Visit](../../data/e-sc04-04-visit.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC04-04 Visit | Planned | Badge "Planned"; a new record starts here; next: Done or Cancelled (UC-SC04-04, BR-SC04-06); fields editable within the role | U25, U26 | `u25-care-coordinator/s-sc04-15-rounds-assistant-e-sc04-04-visit-planned-{desktop,phone}-{light,dark}.png`, `u26-carer/s-sc04-15-rounds-assistant-e-sc04-04-visit-planned-phone-{light,dark}.png` |
| E-SC04-04 Visit | Done | Badge "Done"; next: Missed or Cancelled (UC-SC04-06, BR-SC04-06); fields editable within the role | U25, U26 | `u25-care-coordinator/s-sc04-15-rounds-assistant-e-sc04-04-visit-done-{desktop,phone}-{light,dark}.png`, `u26-carer/s-sc04-15-rounds-assistant-e-sc04-04-visit-done-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

(Proposed) Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-SC04-03 Visit](../../flows/fl-sc04-03-visit.md)

## Open questions

None.

---

⬅️ [S-SC04-14 Activity reports](../05-people-and-quality/s-sc04-14-activity-reports.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC04-16 Care home](../06-care-homes-cesu-and-nursing/s-sc04-16-care-home.md)
