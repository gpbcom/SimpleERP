🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › ⚖️ [SC11 Professional firms](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC11-02 Matters and documents](README.md) › 🖥️ S-SC11-09 Documents

# 🖥️ S-SC11-09 Documents

**Status:** ✅ specified

## Personas

- [U36 Professional](../../../../01-users/personas/u36-professional.md)
- [U37 Professional's assistant](../../../../01-users/personas/u37-assistant.md)

## Purpose

Used to manage documents with versions and e-signature,
[UC-SC11-09](../../use-cases/02-matters-and-documents/uc-sc11-09-manage-documents-with-versions-and-e-signature.md).

## Entry points

Professional firms in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC11-02 step 2, U36 | desktop | ![FL-SC11-02 step 2, U36, light](../../images/02-matters-and-documents/u36-professional/2-documents-desktop-light.png) | ![FL-SC11-02 step 2, U36, dark](../../images/02-matters-and-documents/u36-professional/2-documents-desktop-dark.png) |
| FL-SC11-02 step 2, U36 | phone | ![FL-SC11-02 step 2, U36, light](../../images/02-matters-and-documents/u36-professional/2-documents-phone-light.png) | ![FL-SC11-02 step 2, U36, dark](../../images/02-matters-and-documents/u36-professional/2-documents-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc11-09-documents-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc11-09-documents-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc11-09-documents-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc11-09-documents-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc11-09-documents-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc11-09-documents-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc11-09-documents-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc11-09-documents-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC11-10 Matter document](../../data/e-sc11-10-matter-document.md), shown as the entity pages list them,
with their examples.

## Actions

- Draft:
  [UC-SC11-09](../../use-cases/02-matters-and-documents/uc-sc11-09-manage-documents-with-versions-and-e-signature.md),
  step 1.
- Review:
  [UC-SC11-09](../../use-cases/02-matters-and-documents/uc-sc11-09-manage-documents-with-versions-and-e-signature.md),
  step 2.
- Sign:
  [UC-SC11-09](../../use-cases/02-matters-and-documents/uc-sc11-09-manage-documents-with-versions-and-e-signature.md),
  step 3.
- Lock:
  [UC-SC11-09](../../use-cases/02-matters-and-documents/uc-sc11-09-manage-documents-with-versions-and-e-signature.md),
  step 4.

## States

- Normal: documents with versions and signatures.
- Empty: "No document".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a change after signature: a new version is made; the signed one
  stays locked.
- Read-only: signed versions are read-only.
- Offline: not available offline: office work on confidential matters that stay on the server. Offline work is kept for
  the phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC11-10 Matter document](../../data/e-sc11-10-matter-document.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC11-10 Matter document | Draft | Badge "Draft"; a new record starts here; next: Signed (UC-SC11-09); fields editable within the role | U36, U37 | `u36-professional/s-sc11-09-documents-e-sc11-10-matter-document-draft-{desktop,phone}-{light,dark}.png`, `u37-assistant/s-sc11-09-documents-e-sc11-10-matter-document-draft-desktop-{light,dark}.png` |
| E-SC11-10 Matter document | Signed | Badge "Signed"; final: read-only, no next state; the history shows how it got here | U36, U37 | `u36-professional/s-sc11-09-documents-e-sc11-10-matter-document-signed-{desktop,phone}-{light,dark}.png`, `u37-assistant/s-sc11-09-documents-e-sc11-10-matter-document-signed-desktop-{light,dark}.png` |

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

- [FL-SC11-02 Matters and documents](../../flows/fl-sc11-02-matters-and-documents.md)

## Open questions

None.

---

⬅️ [S-SC11-08 Deadlines](../04-deadlines-and-filings/s-sc11-08-deadlines.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC11-10 Client portal](s-sc11-10-client-portal.md)
