🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏠 [SC04 Home care](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC04-01 Take on a recipient](README.md) › 🖥️ S-SC04-02 Care plan

# 🖥️ S-SC04-02 Care plan

**Status:** ✅ specified

## Personas

- [U25 Care coordinator](../../../../01-users/personas/u25-care-coordinator.md)
- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

Used to assess needs and write the care plan
([UC-SC04-02](../../use-cases/01-take-on-a-recipient/uc-sc04-02-assess-needs-and-write-the-care-plan.md)).

## Entry points

Home care in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC04-01 step 2, U25 | desktop | ![FL-SC04-01 step 2, U25, light](../../images/01-take-on-a-recipient/u25-care-coordinator/2-care-plan-desktop-light.png) | ![FL-SC04-01 step 2, U25, dark](../../images/01-take-on-a-recipient/u25-care-coordinator/2-care-plan-desktop-dark.png) |
| FL-SC04-01 step 2, U25 | phone | ![FL-SC04-01 step 2, U25, light](../../images/01-take-on-a-recipient/u25-care-coordinator/2-care-plan-phone-light.png) | ![FL-SC04-01 step 2, U25, dark](../../images/01-take-on-a-recipient/u25-care-coordinator/2-care-plan-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc04-02-care-plan-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc04-02-care-plan-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc04-02-care-plan-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc04-02-care-plan-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc04-02-care-plan-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc04-02-care-plan-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc04-02-care-plan-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc04-02-care-plan-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC04-03 Care plan](../../data/e-sc04-03-care-plan.md), shown as the entity pages list them, with their
examples.

## Actions

- Assess at home:
  [UC-SC04-02](../../use-cases/01-take-on-a-recipient/uc-sc04-02-assess-needs-and-write-the-care-plan.md), step 1.
- Write the plan:
  [UC-SC04-02](../../use-cases/01-take-on-a-recipient/uc-sc04-02-assess-needs-and-write-the-care-plan.md), step 2.
- Sign: [UC-SC04-02](../../use-cases/01-take-on-a-recipient/uc-sc04-02-assess-needs-and-write-the-care-plan.md), step 3.
- Release for planning:
  [UC-SC04-02](../../use-cases/01-take-on-a-recipient/uc-sc04-02-assess-needs-and-write-the-care-plan.md), step 4.

## States

- Normal: the care plan's tasks, frequency, hours, funding shares and signature.
- Empty: "No care plan", with Assess needs.
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, hours over the funding: the recipient's extra share is shown
  before signing.
- Read-only: a signed version is read-only; a change makes a new one.
- Offline: the assessment typed at home is kept on the tablet and synced after; signing needs the network.

Shown entities (VD-15): [E-SC04-03 Care plan](../../data/e-sc04-03-care-plan.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC04-03 Care plan | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U09, U25 | `u09-customer/s-sc04-02-care-plan-e-sc04-03-care-plan-active-phone-{light,dark}.png`, `u25-care-coordinator/s-sc04-02-care-plan-e-sc04-03-care-plan-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC04-01 Take on a recipient](../../flows/fl-sc04-01-take-on-a-recipient.md)

## Open questions

None.

---

⬅️ [S-SC04-01 Recipient](s-sc04-01-recipient.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC04-03 Rounds](../02-plan-the-rounds/s-sc04-03-rounds.md)
