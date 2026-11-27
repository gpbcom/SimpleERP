🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › ⚖️ [SC11 Professional firms](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC11-01 Client intake](README.md) › 🖥️ S-SC11-03 Engagement

# 🖥️ S-SC11-03 Engagement

**Status:** ✅ specified

## Personas

- [U36 Professional](../../../../01-users/personas/u36-professional.md)
- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

Used to sign the engagement letter and fee agreement,
[UC-SC11-03](../../use-cases/01-client-intake/uc-sc11-03-sign-the-engagement-letter-and-fee-agreement.md).

## Entry points

Professional firms in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC11-01 step 3, U36 | desktop | ![FL-SC11-01 step 3, U36, light](../../images/01-client-intake/u36-professional/3-engagement-desktop-light.png) | ![FL-SC11-01 step 3, U36, dark](../../images/01-client-intake/u36-professional/3-engagement-desktop-dark.png) |
| FL-SC11-01 step 3, U36 | phone | ![FL-SC11-01 step 3, U36, light](../../images/01-client-intake/u36-professional/3-engagement-phone-light.png) | ![FL-SC11-01 step 3, U36, dark](../../images/01-client-intake/u36-professional/3-engagement-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc11-03-engagement-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc11-03-engagement-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc11-03-engagement-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc11-03-engagement-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc11-03-engagement-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc11-03-engagement-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc11-03-engagement-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc11-03-engagement-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC11-04 Engagement letter](../../data/e-sc11-04-engagement-letter.md), shown as the entity pages list
them, with their examples.

## Actions

- Draft: [UC-SC11-03](../../use-cases/01-client-intake/uc-sc11-03-sign-the-engagement-letter-and-fee-agreement.md), step
  1.
- Check the fees:
  [UC-SC11-03](../../use-cases/01-client-intake/uc-sc11-03-sign-the-engagement-letter-and-fee-agreement.md), step 2.
- Send: [UC-SC11-03](../../use-cases/01-client-intake/uc-sc11-03-sign-the-engagement-letter-and-fee-agreement.md), step
  3.
- Sign: [UC-SC11-03](../../use-cases/01-client-intake/uc-sc11-03-sign-the-engagement-letter-and-fee-agreement.md), step
  4.

## States

- Normal: the letter's terms and fees and signature state.
- Empty: "No letter".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a pure success fee: it is refused.
- Read-only: a signed letter is read-only.
- Offline: not available offline: office work on confidential matters that stay on the server. Offline work is kept for
  the phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC11-04 Engagement letter](../../data/e-sc11-04-engagement-letter.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC11-04 Engagement letter | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U09, U36 | `u09-customer/s-sc11-03-engagement-e-sc11-04-engagement-letter-active-phone-{light,dark}.png`, `u36-professional/s-sc11-03-engagement-e-sc11-04-engagement-letter-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC11-01 Client intake](../../flows/fl-sc11-01-client-intake.md)

## Open questions

None.

---

⬅️ [S-SC11-02 Conflict check](s-sc11-02-conflict-check.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC11-04 Matters](../02-matters-and-documents/s-sc11-04-matters.md)
