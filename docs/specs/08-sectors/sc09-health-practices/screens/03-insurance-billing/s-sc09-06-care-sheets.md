🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🩺 [SC09 Health practices](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC09-03 Insurance billing](README.md) › 🖥️ S-SC09-06 Care sheets

# 🖥️ S-SC09-06 Care sheets

**Status:** 🔄 waiting for the owner

## Personas

- [U33 Medical secretary](../../../../01-users/personas/u33-medical-secretary.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Used to bill health insurance with the Carte Vitale,
[UC-SC09-06](../../use-cases/03-insurance-billing/uc-sc09-06-bill-health-insurance-with-the-carte-vitale.md).

## Entry points

Health practices in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC09-03 step 1, U33 | desktop | ![FL-SC09-03 step 1, U33, light](../../images/03-insurance-billing/u33-medical-secretary/1-care-sheet-desktop-light.png) | ![FL-SC09-03 step 1, U33, dark](../../images/03-insurance-billing/u33-medical-secretary/1-care-sheet-desktop-dark.png) |
| Error E1, U33 | desktop | ![Error E1, U33, light](../../images/03-insurance-billing/u33-medical-secretary/e1-estimate-needed-desktop-light.png) | ![Error E1, U33, dark](../../images/03-insurance-billing/u33-medical-secretary/e1-estimate-needed-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc09-06-care-sheets-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc09-06-care-sheets-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc09-06-care-sheets-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc09-06-care-sheets-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc09-06-care-sheets-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc09-06-care-sheets-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc09-06-care-sheets-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc09-06-care-sheets-offline-desktop-dark.png) |

## Fields and columns

The fields of [E-SC09-05 Care sheet](../../data/e-sc09-05-care-sheet.md), shown as the entity pages list them, with
their examples.

## Actions

- Read the card:
  [UC-SC09-06](../../use-cases/03-insurance-billing/uc-sc09-06-bill-health-insurance-with-the-carte-vitale.md), step 1.
- Code the acts:
  [UC-SC09-06](../../use-cases/03-insurance-billing/uc-sc09-06-bill-health-insurance-with-the-carte-vitale.md), step 2.
- Sign: [UC-SC09-06](../../use-cases/03-insurance-billing/uc-sc09-06-bill-health-insurance-with-the-carte-vitale.md),
  step 3.
- Send: [UC-SC09-06](../../use-cases/03-insurance-billing/uc-sc09-06-bill-health-insurance-with-the-carte-vitale.md),
  step 4.

## States

- Normal: the care sheet's acts, amounts and sending state.
- Empty: "No care sheet".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, the module not approved: sending is blocked.
- Read-only: a sent sheet is read-only.
- Offline: not available offline: work on health data that stays on certified hosting. Offline work is kept for the
  phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC09-05 Care sheet](../../data/e-sc09-05-care-sheet.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC09-05 Care sheet | Signed | Badge "Signed"; a new record starts here; next: Sent or Rejected (UC-SC09-06, UC-SC09-07); fields editable within the role | U13, U33 | `u13-owner/s-sc09-06-care-sheets-e-sc09-05-care-sheet-signed-{desktop,phone}-{light,dark}.png`, `u33-medical-secretary/s-sc09-06-care-sheets-e-sc09-05-care-sheet-signed-desktop-{light,dark}.png` |
| E-SC09-05 Care sheet | Sent | Badge "Sent"; next: Paid or Rejected (UC-SC09-06, UC-SC09-07); fields editable within the role | U13, U33 | `u13-owner/s-sc09-06-care-sheets-e-sc09-05-care-sheet-sent-{desktop,phone}-{light,dark}.png`, `u33-medical-secretary/s-sc09-06-care-sheets-e-sc09-05-care-sheet-sent-desktop-{light,dark}.png` |
| E-SC09-05 Care sheet | Paid | Badge "Paid"; final: read-only, no next state; the history shows how it got here | U13, U33 | `u13-owner/s-sc09-06-care-sheets-e-sc09-05-care-sheet-paid-{desktop,phone}-{light,dark}.png`, `u33-medical-secretary/s-sc09-06-care-sheets-e-sc09-05-care-sheet-paid-desktop-{light,dark}.png` |

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

- [FL-SC09-03 Insurance billing](../../flows/fl-sc09-03-insurance-billing.md)

## Open questions

None.

---

⬅️ [S-SC09-05 Prescriptions](../02-patient-file-and-care/s-sc09-05-prescriptions.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC09-07 Returns](s-sc09-07-returns.md)
