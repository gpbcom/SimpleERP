🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💼 [SC03 Services](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC03-05 Client and people](README.md) › 🖥️ S-SC03-12 Satisfaction

# 🖥️ S-SC03-12 Satisfaction

**Status:** ✅ specified

## Personas

- [U24 Engagement manager](../../../../01-users/personas/u24-engagement-manager.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Used to measure client satisfaction
([UC-SC03-12](../../use-cases/05-client-and-people/uc-sc03-12-measure-client-satisfaction.md)).

## Entry points

Services in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC03-05 step 2, U24 | desktop | ![FL-SC03-05 step 2, U24, light](../../images/05-client-and-people/u24-engagement-manager/2-satisfaction-desktop-light.png) | ![FL-SC03-05 step 2, U24, dark](../../images/05-client-and-people/u24-engagement-manager/2-satisfaction-desktop-dark.png) |
| FL-SC03-05 step 2, U24 | phone | ![FL-SC03-05 step 2, U24, light](../../images/05-client-and-people/u24-engagement-manager/2-satisfaction-phone-light.png) | ![FL-SC03-05 step 2, U24, dark](../../images/05-client-and-people/u24-engagement-manager/2-satisfaction-phone-dark.png) |
| Error E1, U24 | desktop | ![Error E1, U24, light](../../images/05-client-and-people/u24-engagement-manager/e1-survey-unanswered-desktop-light.png) | ![Error E1, U24, dark](../../images/05-client-and-people/u24-engagement-manager/e1-survey-unanswered-desktop-dark.png) |
| Error E1, U24 | phone | ![Error E1, U24, light](../../images/05-client-and-people/u24-engagement-manager/e1-survey-unanswered-phone-light.png) | ![Error E1, U24, dark](../../images/05-client-and-people/u24-engagement-manager/e1-survey-unanswered-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc03-12-satisfaction-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc03-12-satisfaction-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc03-12-satisfaction-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc03-12-satisfaction-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc03-12-satisfaction-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc03-12-satisfaction-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc03-12-satisfaction-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc03-12-satisfaction-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC03-13 Satisfaction survey](../../data/e-sc03-13-satisfaction-survey.md), shown as the entity pages
list them, with their examples.

## Actions

- Send the survey: [UC-SC03-12](../../use-cases/05-client-and-people/uc-sc03-12-measure-client-satisfaction.md), step 1.
- Answer: [UC-SC03-12](../../use-cases/05-client-and-people/uc-sc03-12-measure-client-satisfaction.md), step 2.
- Follow up: [UC-SC03-12](../../use-cases/05-client-and-people/uc-sc03-12-measure-client-satisfaction.md), step 3.
- Record the follow-up: [UC-SC03-12](../../use-cases/05-client-and-people/uc-sc03-12-measure-client-satisfaction.md),
  step 4.

## States

- Normal: surveys with sent date, score, comment and follow-up.
- Empty: "No survey sent".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, no answer: one reminder is sent, then the survey closes.
- Read-only: consultants read the scores of their engagements.
- Offline: not available offline: office work at a desk on shared engagement figures. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC03-13 Satisfaction survey](../../data/e-sc03-13-satisfaction-survey.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC03-13 Satisfaction survey | Sent | Badge "Sent"; a new record starts here; next: Closed (UC-SC03-12); fields editable within the role | U09, U13, U24 | `u09-customer/s-sc03-12-satisfaction-e-sc03-13-satisfaction-survey-sent-phone-{light,dark}.png`, `u13-owner/s-sc03-12-satisfaction-e-sc03-13-satisfaction-survey-sent-{desktop,phone}-{light,dark}.png`, `u24-engagement-manager/s-sc03-12-satisfaction-e-sc03-13-satisfaction-survey-sent-{desktop,phone}-{light,dark}.png` |
| E-SC03-13 Satisfaction survey | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U13 | `u13-owner/s-sc03-12-satisfaction-e-sc03-13-satisfaction-survey-closed-{desktop,phone}-{light,dark}.png` |

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

⬅️ [S-SC03-11 Client portal](s-sc03-11-client-portal.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC03-13 Skills](s-sc03-13-skills.md)
