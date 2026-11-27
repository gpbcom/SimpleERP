🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏠 [SC04 Home care](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC04-02 Plan the rounds](README.md) › 🖥️ S-SC04-03 Rounds

# 🖥️ S-SC04-03 Rounds

**Status:** ✅ specified

## Personas

- [U25 Care coordinator](../../../../01-users/personas/u25-care-coordinator.md)

## Purpose

Used to plan visits and optimise rounds
([UC-SC04-03](../../use-cases/02-plan-the-rounds/uc-sc04-03-plan-visits-and-optimise-rounds.md)).

## Entry points

Home care in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC04-02 step 1, U25 | desktop | ![FL-SC04-02 step 1, U25, light](../../images/02-plan-the-rounds/u25-care-coordinator/1-rounds-desktop-light.png) | ![FL-SC04-02 step 1, U25, dark](../../images/02-plan-the-rounds/u25-care-coordinator/1-rounds-desktop-dark.png) |
| FL-SC04-02 step 1, U25 | phone | ![FL-SC04-02 step 1, U25, light](../../images/02-plan-the-rounds/u25-care-coordinator/1-rounds-phone-light.png) | ![FL-SC04-02 step 1, U25, dark](../../images/02-plan-the-rounds/u25-care-coordinator/1-rounds-phone-dark.png) |
| Error E1, U25 | desktop | ![Error E1, U25, light](../../images/02-plan-the-rounds/u25-care-coordinator/e1-no-carer-desktop-light.png) | ![Error E1, U25, dark](../../images/02-plan-the-rounds/u25-care-coordinator/e1-no-carer-desktop-dark.png) |
| Error E1, U25 | phone | ![Error E1, U25, light](../../images/02-plan-the-rounds/u25-care-coordinator/e1-no-carer-phone-light.png) | ![Error E1, U25, dark](../../images/02-plan-the-rounds/u25-care-coordinator/e1-no-carer-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc04-03-rounds-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc04-03-rounds-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc04-03-rounds-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc04-03-rounds-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc04-03-rounds-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc04-03-rounds-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc04-03-rounds-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc04-03-rounds-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC04-04 Visit](../../data/e-sc04-04-visit.md),
[E-F9-26 Round](../../../../02-functional/f09-hr-and-projects/data/e-f09-26-round.md),
[E-F9-26 Round](../../../../02-functional/f09-hr-and-projects/data/e-f09-26-round.md), shown as the entity pages list
them, with their examples.

## Actions

- Generate the visits: [UC-SC04-03](../../use-cases/02-plan-the-rounds/uc-sc04-03-plan-visits-and-optimise-rounds.md),
  step 1.
- Optimise the rounds: [UC-SC04-03](../../use-cases/02-plan-the-rounds/uc-sc04-03-plan-visits-and-optimise-rounds.md),
  step 2.
- Check travel and splits:
  [UC-SC04-03](../../use-cases/02-plan-the-rounds/uc-sc04-03-plan-visits-and-optimise-rounds.md), step 3.
- Publish: [UC-SC04-03](../../use-cases/02-plan-the-rounds/uc-sc04-03-plan-visits-and-optimise-rounds.md), step 4.

## States

- Normal: rounds per carer and day with visits, travel times, warnings and unassigned visits.
- Empty: "No visit this week", with Generate visits.
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a visit without a qualified carer: it is flagged and stays to
  assign ([BR-SC04-06](../../business-rules/br-sc04-06-carers-match-the-needs.md)).
- Read-only: carers see their own rounds.
- Offline: not available offline: office work at the agency on shared planning and billing data. Offline work is kept
  for the phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC04-04 Visit](../../data/e-sc04-04-visit.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC04-04 Visit | Planned | Badge "Planned"; a new record starts here; next: Done or Cancelled (UC-SC04-04, BR-SC04-06); fields editable within the role | U25 | `u25-care-coordinator/s-sc04-03-rounds-e-sc04-04-visit-planned-{desktop,phone}-{light,dark}.png` |
| E-SC04-04 Visit | Done | Badge "Done"; next: Missed or Cancelled (UC-SC04-06, BR-SC04-06); fields editable within the role | U25 | `u25-care-coordinator/s-sc04-03-rounds-e-sc04-04-visit-done-{desktop,phone}-{light,dark}.png` |
| E-SC04-04 Visit | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U25 | `u25-care-coordinator/s-sc04-03-rounds-e-sc04-04-visit-cancelled-{desktop,phone}-{light,dark}.png` |
| E-SC04-04 Visit | Missed | Badge "Missed"; final: read-only, no next state; the history shows how it got here | U25 | `u25-care-coordinator/s-sc04-03-rounds-e-sc04-04-visit-missed-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC04-02 Plan the rounds](../../flows/fl-sc04-02-plan-the-rounds.md)

## Open questions

None.

---

⬅️ [S-SC04-02 Care plan](../01-take-on-a-recipient/s-sc04-02-care-plan.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC04-04 Visit](s-sc04-04-visit.md)
