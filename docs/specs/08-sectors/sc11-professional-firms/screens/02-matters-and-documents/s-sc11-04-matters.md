🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › ⚖️ [SC11 Professional firms](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC11-02 Matters and documents](README.md) › 🖥️ S-SC11-04 Matters

# 🖥️ S-SC11-04 Matters

**Status:** 🔄 waiting for the owner

## Personas

- [U36 Professional](../../../../01-users/personas/u36-professional.md)
- [U37 Professional's assistant](../../../../01-users/personas/u37-assistant.md)

## Purpose

Used to open and organise matters
([UC-SC11-04](../../use-cases/02-matters-and-documents/uc-sc11-04-open-and-organise-matters.md)).

## Entry points

Professional firms in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC11-02 step 1, U36 | desktop | ![FL-SC11-02 step 1, U36, light](../../images/02-matters-and-documents/u36-professional/1-matter-desktop-light.png) | ![FL-SC11-02 step 1, U36, dark](../../images/02-matters-and-documents/u36-professional/1-matter-desktop-dark.png) |
| FL-SC11-02 step 1, U36 | phone | ![FL-SC11-02 step 1, U36, light](../../images/02-matters-and-documents/u36-professional/1-matter-phone-light.png) | ![FL-SC11-02 step 1, U36, dark](../../images/02-matters-and-documents/u36-professional/1-matter-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc11-04-matters-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc11-04-matters-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc11-04-matters-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc11-04-matters-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc11-04-matters-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc11-04-matters-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc11-04-matters-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc11-04-matters-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC11-05 Matter](../../data/e-sc11-05-matter.md), shown as the entity pages list them, with their
examples.

## Actions

- Open: [UC-SC11-04](../../use-cases/02-matters-and-documents/uc-sc11-04-open-and-organise-matters.md), step 1.
- Assign the team: [UC-SC11-04](../../use-cases/02-matters-and-documents/uc-sc11-04-open-and-organise-matters.md), step
  2.
- Plan steps: [UC-SC11-04](../../use-cases/02-matters-and-documents/uc-sc11-04-open-and-organise-matters.md), step 3.
- Start: [UC-SC11-04](../../use-cases/02-matters-and-documents/uc-sc11-04-open-and-organise-matters.md), step 4.

## States

- Normal: matters with team, parties, steps and wall.
- Empty: "No matter".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, no signed engagement: the matter is blocked.
- Read-only: walled matters only for their team.
- Offline: not available offline: office work on confidential matters that stay on the server. Offline work is kept for
  the phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC11-05 Matter](../../data/e-sc11-05-matter.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC11-05 Matter | Open | Badge "Open"; a new record starts here; next: Closed (BR-SC11-06); fields editable within the role | U36, U37 | `u36-professional/s-sc11-04-matters-e-sc11-05-matter-open-{desktop,phone}-{light,dark}.png`, `u37-assistant/s-sc11-04-matters-e-sc11-05-matter-open-desktop-{light,dark}.png` |
| E-SC11-05 Matter | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U36, U37 | `u36-professional/s-sc11-04-matters-e-sc11-05-matter-closed-{desktop,phone}-{light,dark}.png`, `u37-assistant/s-sc11-04-matters-e-sc11-05-matter-closed-desktop-{light,dark}.png` |

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

- [FL-SC11-02 Matters and documents](../../flows/fl-sc11-02-matters-and-documents.md)

## Open questions

None.

---

⬅️ [S-SC11-03 Engagement](../01-client-intake/s-sc11-03-engagement.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC11-05 Time](../03-time-and-billing/s-sc11-05-time.md)
