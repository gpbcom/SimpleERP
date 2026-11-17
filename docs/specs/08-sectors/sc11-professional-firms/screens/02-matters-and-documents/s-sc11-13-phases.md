🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › ⚖️ [SC11 Professional firms](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC11-02 Matters and documents](README.md) › 🖥️ S-SC11-13 Phases

# 🖥️ S-SC11-13 Phases

**Status:** 🔄 waiting for the owner

## Personas

- [U36 Professional](../../../../01-users/personas/u36-professional.md)

## Purpose

Used to run architects' and engineers' projects by phase,
[UC-SC11-13](../../use-cases/02-matters-and-documents/uc-sc11-13-run-architects-and-engineers-projects-by-phase.md).

## Entry points

Professional firms in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC11-02 step 4, U36 | desktop | ![FL-SC11-02 step 4, U36, light](../../images/02-matters-and-documents/u36-professional/4-phases-desktop-light.png) | ![FL-SC11-02 step 4, U36, dark](../../images/02-matters-and-documents/u36-professional/4-phases-desktop-dark.png) |
| FL-SC11-02 step 4, U36 | phone | ![FL-SC11-02 step 4, U36, light](../../images/02-matters-and-documents/u36-professional/4-phases-phone-light.png) | ![FL-SC11-02 step 4, U36, dark](../../images/02-matters-and-documents/u36-professional/4-phases-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc11-13-phases-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc11-13-phases-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc11-13-phases-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc11-13-phases-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc11-13-phases-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc11-13-phases-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc11-13-phases-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc11-13-phases-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC11-05 Matter](../../data/e-sc11-05-matter.md),
[E-SC11-07 Fee bill](../../data/e-sc11-07-fee-bill.md), shown as the entity pages list them, with their examples.

## Actions

- Plan phases:
  [UC-SC11-13](../../use-cases/02-matters-and-documents/uc-sc11-13-run-architects-and-engineers-projects-by-phase.md),
  step 1.
- Deliver:
  [UC-SC11-13](../../use-cases/02-matters-and-documents/uc-sc11-13-run-architects-and-engineers-projects-by-phase.md),
  step 2.
- Accept:
  [UC-SC11-13](../../use-cases/02-matters-and-documents/uc-sc11-13-run-architects-and-engineers-projects-by-phase.md),
  step 3.
- Bill each phase:
  [UC-SC11-13](../../use-cases/02-matters-and-documents/uc-sc11-13-run-architects-and-engineers-projects-by-phase.md),
  step 4.

## States

- Normal: phases with deliverables, acceptance and fees.
- Empty: "No phase".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, the insurance certificate missing: the architect is warned.
- Read-only: billed phases are read-only.
- Offline: not available offline: office work on confidential matters that stay on the server. Offline work is kept for
  the phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

(Proposed) Desktop; approvals and receipts also on the phone.

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

⬅️ [S-SC11-12 Filings](../04-deadlines-and-filings/s-sc11-12-filings.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC11-14 Work in progress](../06-firm-management/s-sc11-14-work-in-progress.md)
