🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🩺 [SC09 Health practices](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC09-06 Compliance and certification](README.md) ›
🖥️ S-SC09-17 Patients' rights

# 🖥️ S-SC09-17 Patients' rights

**Status:** 🔄 waiting for the owner

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

Used to honour patients' rights
([UC-SC09-17](../../use-cases/06-compliance-and-certification/uc-sc09-17-honour-patients-rights.md)).

## Entry points

Health practices in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC09-06 step 1, U13 | desktop | ![FL-SC09-06 step 1, U13, light](../../images/06-compliance-and-certification/u13-owner/1-rights-desktop-light.png) | ![FL-SC09-06 step 1, U13, dark](../../images/06-compliance-and-certification/u13-owner/1-rights-desktop-dark.png) |
| FL-SC09-06 step 1, U13 | phone | ![FL-SC09-06 step 1, U13, light](../../images/06-compliance-and-certification/u13-owner/1-rights-phone-light.png) | ![FL-SC09-06 step 1, U13, dark](../../images/06-compliance-and-certification/u13-owner/1-rights-phone-dark.png) |
| Error E1, U13 | desktop | ![Error E1, U13, light](../../images/06-compliance-and-certification/u13-owner/e1-access-late-desktop-light.png) | ![Error E1, U13, dark](../../images/06-compliance-and-certification/u13-owner/e1-access-late-desktop-dark.png) |
| Error E1, U13 | phone | ![Error E1, U13, light](../../images/06-compliance-and-certification/u13-owner/e1-access-late-phone-light.png) | ![Error E1, U13, dark](../../images/06-compliance-and-certification/u13-owner/e1-access-late-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc09-17-patients-rights-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc09-17-patients-rights-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc09-17-patients-rights-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc09-17-patients-rights-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc09-17-patients-rights-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc09-17-patients-rights-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc09-17-patients-rights-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc09-17-patients-rights-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC09-02 Patient](../../data/e-sc09-02-patient.md),
[E-SC09-03 Clinical record entry](../../data/e-sc09-03-clinical-record-entry.md), shown as the entity pages list them,
with their examples.

## Actions

- Request: [UC-SC09-17](../../use-cases/06-compliance-and-certification/uc-sc09-17-honour-patients-rights.md), step 1.
- Check identity: [UC-SC09-17](../../use-cases/06-compliance-and-certification/uc-sc09-17-honour-patients-rights.md),
  step 2.
- Prepare the record:
  [UC-SC09-17](../../use-cases/06-compliance-and-certification/uc-sc09-17-honour-patients-rights.md), step 3.
- Answer: [UC-SC09-17](../../use-cases/06-compliance-and-certification/uc-sc09-17-honour-patients-rights.md), step 4.

## States

- Normal: requests with kind, deadline and answer.
- Empty: "No request".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, late: the practitioner is alerted.
- Read-only: answered requests are read-only.
- Offline: not available offline: work on health data that stays on certified hosting. Offline work is kept for the
  phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC09-02 Patient](../../data/e-sc09-02-patient.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC09-02 Patient | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U09, U13 | `u09-customer/s-sc09-17-patients-rights-e-sc09-02-patient-active-phone-{light,dark}.png`, `u13-owner/s-sc09-17-patients-rights-e-sc09-02-patient-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC09-06 Compliance and certification](../../flows/fl-sc09-06-compliance-and-certification.md)

## Open questions

None.

---

⬅️ [S-SC09-16 Locums](../05-practice-organisation/s-sc09-16-locums.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC09-18 Quality indicator](s-sc09-18-quality-indicator.md)
