🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏭 [SC05 Manufacturing](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC05-04 Quality system](README.md) › 🖥️ S-SC05-07 Documents

# 🖥️ S-SC05-07 Documents

**Status:** ✅ specified

## Personas

- [U27 Quality manager](../../../../01-users/personas/u27-quality-manager.md)

## Purpose

Used to control quality documents
([UC-SC05-07](../../use-cases/04-quality-system/uc-sc05-07-control-quality-documents.md)).

## Entry points

Manufacturing in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC05-04 step 1, U27 | desktop | ![FL-SC05-04 step 1, U27, light](../../images/04-quality-system/u27-quality-manager/1-documents-desktop-light.png) | ![FL-SC05-04 step 1, U27, dark](../../images/04-quality-system/u27-quality-manager/1-documents-desktop-dark.png) |
| FL-SC05-04 step 1, U27 | tablet | ![FL-SC05-04 step 1, U27, light](../../images/04-quality-system/u27-quality-manager/1-documents-tablet-light.png) | ![FL-SC05-04 step 1, U27, dark](../../images/04-quality-system/u27-quality-manager/1-documents-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc05-07-documents-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc05-07-documents-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc05-07-documents-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc05-07-documents-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc05-07-documents-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc05-07-documents-read-only-desktop-dark.png) |
| Offline | tablet | ![Offline, light](../../images/states/s-sc05-07-documents-offline-tablet-light.png) | ![Offline, dark](../../images/states/s-sc05-07-documents-offline-tablet-dark.png) |

## Fields and columns

The fields of [E-SC05-07 Controlled document](../../data/e-sc05-07-controlled-document.md), shown as the entity pages
list them, with their examples.

## Actions

- Draft: [UC-SC05-07](../../use-cases/04-quality-system/uc-sc05-07-control-quality-documents.md), step 1.
- Approve: [UC-SC05-07](../../use-cases/04-quality-system/uc-sc05-07-control-quality-documents.md), step 2.
- Publish: [UC-SC05-07](../../use-cases/04-quality-system/uc-sc05-07-control-quality-documents.md), step 3.
- Acknowledge: [UC-SC05-07](../../use-cases/04-quality-system/uc-sc05-07-control-quality-documents.md), step 4.

## States

- Normal: documents with versions, approval, review date and where they are in use.
- Empty: "No document", with New document.
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, an old version in use: it is withdrawn from the shop floor.
- Read-only: operators see only the current version.
- Offline: not available offline: office work on shared quality and planning records. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC05-07 Controlled document](../../data/e-sc05-07-controlled-document.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC05-07 Controlled document | Draft | Badge "Draft"; a new record starts here; next: Approved or Withdrawn (UC-SC05-07); fields editable within the role | U20, U27 | `u20-production-operator/s-sc05-07-documents-e-sc05-07-controlled-document-draft-tablet-{light,dark}.png`, `u27-quality-manager/s-sc05-07-documents-e-sc05-07-controlled-document-draft-{desktop,tablet}-{light,dark}.png` |
| E-SC05-07 Controlled document | Approved | Badge "Approved"; final: read-only, no next state; the history shows how it got here | U20, U27 | `u20-production-operator/s-sc05-07-documents-e-sc05-07-controlled-document-approved-tablet-{light,dark}.png`, `u27-quality-manager/s-sc05-07-documents-e-sc05-07-controlled-document-approved-{desktop,tablet}-{light,dark}.png` |
| E-SC05-07 Controlled document | Withdrawn | Badge "Withdrawn"; final: read-only, no next state; the history shows how it got here | U20, U27 | `u20-production-operator/s-sc05-07-documents-e-sc05-07-controlled-document-withdrawn-tablet-{light,dark}.png`, `u27-quality-manager/s-sc05-07-documents-e-sc05-07-controlled-document-withdrawn-{desktop,tablet}-{light,dark}.png` |

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

⬅️ [S-SC05-06 Labels](../03-packaging/s-sc05-06-labels.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC05-08 Audits](s-sc05-08-audits.md)
