🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › ⚖️ [SC11 Professional firms](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC11-03 Time and billing](README.md) › 🖥️ S-SC11-05 Time

# 🖥️ S-SC11-05 Time

**Status:** 🔄 waiting for the owner

## Personas

- [U36 Professional](../../../../01-users/personas/u36-professional.md)

## Purpose

Used to record time and disbursements
([UC-SC11-05](../../use-cases/03-time-and-billing/uc-sc11-05-record-time-and-disbursements.md)).

## Entry points

Professional firms in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC11-03 step 1, U36 | desktop | ![FL-SC11-03 step 1, U36, light](../../images/03-time-and-billing/u36-professional/1-time-desktop-light.png) | ![FL-SC11-03 step 1, U36, dark](../../images/03-time-and-billing/u36-professional/1-time-desktop-dark.png) |
| FL-SC11-03 step 1, U36 | phone | ![FL-SC11-03 step 1, U36, light](../../images/03-time-and-billing/u36-professional/1-time-phone-light.png) | ![FL-SC11-03 step 1, U36, dark](../../images/03-time-and-billing/u36-professional/1-time-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc11-05-time-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc11-05-time-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc11-05-time-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc11-05-time-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc11-05-time-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc11-05-time-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc11-05-time-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc11-05-time-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC11-06 Time entry](../../data/e-sc11-06-time-entry.md), shown as the entity pages list them, with
their examples.

## Actions

- Record: [UC-SC11-05](../../use-cases/03-time-and-billing/uc-sc11-05-record-time-and-disbursements.md), step 1.
- Add disbursements: [UC-SC11-05](../../use-cases/03-time-and-billing/uc-sc11-05-record-time-and-disbursements.md), step
  2.
- Review: [UC-SC11-05](../../use-cases/03-time-and-billing/uc-sc11-05-record-time-and-disbursements.md), step 3.
- Submit: [UC-SC11-05](../../use-cases/03-time-and-billing/uc-sc11-05-record-time-and-disbursements.md), step 4.

## States

- Normal: time and disbursements per matter and day.
- Empty: "No time this week".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a closed matter: the entry is refused.
- Read-only: billed time is read-only.
- Offline: time typed on the phone is kept and submitted later,
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).

Shown entities (VD-15): [E-SC11-06 Time entry](../../data/e-sc11-06-time-entry.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC11-06 Time entry | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U36 | `u36-professional/s-sc11-05-time-e-sc11-06-time-entry-recorded-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC11-03 Time and billing](../../flows/fl-sc11-03-time-and-billing.md)

## Open questions

None.

---

⬅️ [S-SC11-04 Matters](../02-matters-and-documents/s-sc11-04-matters.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC11-06 Fees](s-sc11-06-fees.md)
