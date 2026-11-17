🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏠 [SC04 Home care](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC04-02 Plan the rounds](README.md) › 🖥️ S-SC04-06 Replacements

# 🖥️ S-SC04-06 Replacements

**Status:** 🔄 waiting for the owner

## Personas

- [U25 Care coordinator](../../../../01-users/personas/u25-care-coordinator.md)

## Purpose

Used to replace an absent carer
([UC-SC04-06](../../use-cases/02-plan-the-rounds/uc-sc04-06-replace-an-absent-carer.md)).

## Entry points

Home care in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC04-02 step 2, U25 | desktop | ![FL-SC04-02 step 2, U25, light](../../images/02-plan-the-rounds/u25-care-coordinator/2-replacement-desktop-light.png) | ![FL-SC04-02 step 2, U25, dark](../../images/02-plan-the-rounds/u25-care-coordinator/2-replacement-desktop-dark.png) |
| FL-SC04-02 step 2, U25 | phone | ![FL-SC04-02 step 2, U25, light](../../images/02-plan-the-rounds/u25-care-coordinator/2-replacement-phone-light.png) | ![FL-SC04-02 step 2, U25, dark](../../images/02-plan-the-rounds/u25-care-coordinator/2-replacement-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc04-06-replacements-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc04-06-replacements-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc04-06-replacements-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc04-06-replacements-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc04-06-replacements-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc04-06-replacements-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc04-06-replacements-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc04-06-replacements-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC04-04 Visit](../../data/e-sc04-04-visit.md),
[E-F9-26 Round](../../../../02-functional/f09-hr-and-projects/data/e-f09-26-round.md), shown
as the entity pages list them, with their examples.

## Actions

- Record the absence: [UC-SC04-06](../../use-cases/02-plan-the-rounds/uc-sc04-06-replace-an-absent-carer.md), step 1.
- Review proposals: [UC-SC04-06](../../use-cases/02-plan-the-rounds/uc-sc04-06-replace-an-absent-carer.md), step 2.
- Confirm and tell: [UC-SC04-06](../../use-cases/02-plan-the-rounds/uc-sc04-06-replace-an-absent-carer.md), step 3.

## States

- Normal: the absent carer's visits with proposed replacements.
- Empty: "No visit to cover".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, no replacement possible: the visit is flagged and the recipient
  called.
- Read-only: a confirmed replacement is read-only.
- Offline: not available offline: office work at the agency on shared planning and billing data. Offline work is kept
  for the phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC04-04 Visit](../../data/e-sc04-04-visit.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC04-04 Visit | Planned | Badge "Planned"; a new record starts here; next: Done or Cancelled (UC-SC04-04, BR-SC04-06); fields editable within the role | U25, U26 | `u25-care-coordinator/s-sc04-06-replacements-e-sc04-04-visit-planned-{desktop,phone}-{light,dark}.png`, `u26-carer/s-sc04-06-replacements-e-sc04-04-visit-planned-phone-{light,dark}.png` |
| E-SC04-04 Visit | Done | Badge "Done"; next: Missed or Cancelled (UC-SC04-06, BR-SC04-06); fields editable within the role | U25, U26 | `u25-care-coordinator/s-sc04-06-replacements-e-sc04-04-visit-done-{desktop,phone}-{light,dark}.png`, `u26-carer/s-sc04-06-replacements-e-sc04-04-visit-done-phone-{light,dark}.png` |
| E-SC04-04 Visit | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U25, U26 | `u25-care-coordinator/s-sc04-06-replacements-e-sc04-04-visit-cancelled-{desktop,phone}-{light,dark}.png`, `u26-carer/s-sc04-06-replacements-e-sc04-04-visit-cancelled-phone-{light,dark}.png` |
| E-SC04-04 Visit | Missed | Badge "Missed"; final: read-only, no next state; the history shows how it got here | U25, U26 | `u25-care-coordinator/s-sc04-06-replacements-e-sc04-04-visit-missed-{desktop,phone}-{light,dark}.png`, `u26-carer/s-sc04-06-replacements-e-sc04-04-visit-missed-phone-{light,dark}.png` |

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

- [FL-SC04-02 Plan the rounds](../../flows/fl-sc04-02-plan-the-rounds.md)

## Open questions

None.

---

⬅️ [S-SC04-05 Care log](../03-visit/s-sc04-05-care-log.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC04-07 Family access](../03-visit/s-sc04-07-family-access.md)
