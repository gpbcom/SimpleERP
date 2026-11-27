🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🩺 [SC09 Health practices](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC09-05 Practice organisation](README.md) › 🖥️ S-SC09-16 Locums

# 🖥️ S-SC09-16 Locums

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Used to manage locums and fee retrocession
([UC-SC09-16](../../use-cases/05-practice-organisation/uc-sc09-16-manage-locums-and-fee-retrocession.md)).

## Entry points

Health practices in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC09-05 step 5, U13 | desktop | ![FL-SC09-05 step 5, U13, light](../../images/05-practice-organisation/u13-owner/5-locum-desktop-light.png) | ![FL-SC09-05 step 5, U13, dark](../../images/05-practice-organisation/u13-owner/5-locum-desktop-dark.png) |
| FL-SC09-05 step 5, U13 | phone | ![FL-SC09-05 step 5, U13, light](../../images/05-practice-organisation/u13-owner/5-locum-phone-light.png) | ![FL-SC09-05 step 5, U13, dark](../../images/05-practice-organisation/u13-owner/5-locum-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc09-16-locums-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc09-16-locums-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc09-16-locums-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc09-16-locums-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc09-16-locums-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc09-16-locums-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc09-16-locums-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc09-16-locums-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC09-12 Locum agreement](../../data/e-sc09-12-locum-agreement.md), shown as the entity pages list them,
with their examples.

## Actions

- Record the locum:
  [UC-SC09-16](../../use-cases/05-practice-organisation/uc-sc09-16-manage-locums-and-fee-retrocession.md), step 1.
- Bill under the agreement:
  [UC-SC09-16](../../use-cases/05-practice-organisation/uc-sc09-16-manage-locums-and-fee-retrocession.md), step 2.
- Compute: [UC-SC09-16](../../use-cases/05-practice-organisation/uc-sc09-16-manage-locums-and-fee-retrocession.md), step
  3.
- Retrocede fees:
  [UC-SC09-16](../../use-cases/05-practice-organisation/uc-sc09-16-manage-locums-and-fee-retrocession.md), step 4.

## States

- Normal: locum agreements, acts and retrocessions.
- Empty: "No locum".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, the agreement missing: billing is blocked.
- Read-only: paid retrocessions are read-only.
- Offline: not available offline: work on health data that stays on certified hosting. Offline work is kept for the
  phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC09-12 Locum agreement](../../data/e-sc09-12-locum-agreement.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC09-12 Locum agreement | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U05, U13 | `u05-accounting/s-sc09-16-locums-e-sc09-12-locum-agreement-active-desktop-{light,dark}.png`, `u13-owner/s-sc09-16-locums-e-sc09-12-locum-agreement-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC09-05 Practice organisation](../../flows/fl-sc09-05-practice-organisation.md)

## Open questions

None.

---

⬅️ [S-SC09-15 Practice accounts](s-sc09-15-practice-accounts.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC09-17 Patients' rights](../06-compliance-and-certification/s-sc09-17-patients-rights.md)
