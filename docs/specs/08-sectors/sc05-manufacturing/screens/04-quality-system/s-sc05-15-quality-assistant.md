🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏭 [SC05 Manufacturing](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC05-04 Quality system](README.md) › 🖥️ S-SC05-15 Quality assistant

# 🖥️ S-SC05-15 Quality assistant

**Status:** ✅ specified

## Personas

- [U27 Quality manager](../../../../01-users/personas/u27-quality-manager.md)
- [U21 Production planner](../../../../01-users/personas/u21-production-planner.md)

## Purpose

Used to ask the AI assistant about quality
([UC-SC05-15](../../use-cases/04-quality-system/uc-sc05-15-ask-the-assistant-about-quality.md)).

## Entry points

Manufacturing in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC05-04 step 5, U27 | desktop | ![FL-SC05-04 step 5, U27, light](../../images/04-quality-system/u27-quality-manager/5-assistant-desktop-light.png) | ![FL-SC05-04 step 5, U27, dark](../../images/04-quality-system/u27-quality-manager/5-assistant-desktop-dark.png) |
| FL-SC05-04 step 5, U27 | tablet | ![FL-SC05-04 step 5, U27, light](../../images/04-quality-system/u27-quality-manager/5-assistant-tablet-light.png) | ![FL-SC05-04 step 5, U27, dark](../../images/04-quality-system/u27-quality-manager/5-assistant-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc05-15-quality-assistant-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc05-15-quality-assistant-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc05-15-quality-assistant-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc05-15-quality-assistant-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc05-15-quality-assistant-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc05-15-quality-assistant-read-only-desktop-dark.png) |
| Offline | tablet | ![Offline, light](../../images/states/s-sc05-15-quality-assistant-offline-tablet-light.png) | ![Offline, dark](../../images/states/s-sc05-15-quality-assistant-offline-tablet-dark.png) |

## Fields and columns

The fields of [E-SC05-09 Quality action](../../data/e-sc05-09-quality-action.md),
[E-SC05-07 Controlled document](../../data/e-sc05-07-controlled-document.md), shown as the entity pages list them, with
their examples.

## Actions

- Ask: [UC-SC05-15](../../use-cases/04-quality-system/uc-sc05-15-ask-the-assistant-about-quality.md), step 1.
- Confirm a list: [UC-SC05-15](../../use-cases/04-quality-system/uc-sc05-15-ask-the-assistant-about-quality.md), step 4.

## States

- Normal: the conversation with answers, links and prepared lists.
- Empty: suggested questions about quality.
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, an action beyond the user's rights: the AI assistant refuses and
  says which role can do it.
- Read-only: answers only for roles that cannot act.
- Offline: not available offline: the AI assistant needs the network; the last answers stay readable.

Shown entities (VD-15): [E-SC05-07 Controlled document](../../data/e-sc05-07-controlled-document.md),
[E-SC05-09 Quality action](../../data/e-sc05-09-quality-action.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC05-07 Controlled document | Withdrawn | Badge "Withdrawn"; final: read-only, no next state; the history shows how it got here | U21, U27 | `u21-production-planner/s-sc05-15-quality-assistant-e-sc05-07-controlled-document-withdrawn-{desktop,phone}-{light,dark}.png`, `u27-quality-manager/s-sc05-15-quality-assistant-e-sc05-07-controlled-document-withdrawn-{desktop,tablet}-{light,dark}.png` |
| E-SC05-09 Quality action | Open | Badge "Open"; a new record starts here; next: Done (BR-SC05-09); fields editable within the role | U21, U27 | `u21-production-planner/s-sc05-15-quality-assistant-e-sc05-09-quality-action-open-{desktop,phone}-{light,dark}.png`, `u27-quality-manager/s-sc05-15-quality-assistant-e-sc05-09-quality-action-open-{desktop,tablet}-{light,dark}.png` |
| E-SC05-09 Quality action | Done | Badge "Done"; next: Effective (UC-SC05-09); fields editable within the role | U21, U27 | `u21-production-planner/s-sc05-15-quality-assistant-e-sc05-09-quality-action-done-{desktop,phone}-{light,dark}.png`, `u27-quality-manager/s-sc05-15-quality-assistant-e-sc05-09-quality-action-done-{desktop,tablet}-{light,dark}.png` |
| E-SC05-09 Quality action | Effective | Badge "Effective"; final: read-only, no next state; the history shows how it got here | U21, U27 | `u21-production-planner/s-sc05-15-quality-assistant-e-sc05-09-quality-action-effective-{desktop,phone}-{light,dark}.png`, `u27-quality-manager/s-sc05-15-quality-assistant-e-sc05-09-quality-action-effective-{desktop,tablet}-{light,dark}.png` |

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

- [FL-SC05-04 Quality system](../../flows/fl-sc05-04-quality-system.md)

## Open questions

None.

---

⬅️ [S-SC05-14 Management review](../05-suppliers-and-customers/s-sc05-14-management-review.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC05-16 Alcohol excise](../06-excise-refurbishment-and-cutting/s-sc05-16-alcohol-excise.md)
