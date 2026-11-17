🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › ⚖️ [SC11 Professional firms](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC11-02 Matters and documents](README.md) › 🖥️ S-SC11-20 Matter assistant

# 🖥️ S-SC11-20 Matter assistant

**Status:** 🔄 waiting for the owner

## Personas

- [U36 Professional](../../../../01-users/personas/u36-professional.md)
- [U37 Professional's assistant](../../../../01-users/personas/u37-assistant.md)

## Purpose

Used to ask the AI assistant about a matter
([UC-SC11-20](../../use-cases/02-matters-and-documents/uc-sc11-20-ask-the-assistant-about-a-matter.md)).

## Entry points

Professional firms in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC11-02 step 5, U36 | desktop | ![FL-SC11-02 step 5, U36, light](../../images/02-matters-and-documents/u36-professional/5-assistant-desktop-light.png) | ![FL-SC11-02 step 5, U36, dark](../../images/02-matters-and-documents/u36-professional/5-assistant-desktop-dark.png) |
| FL-SC11-02 step 5, U36 | phone | ![FL-SC11-02 step 5, U36, light](../../images/02-matters-and-documents/u36-professional/5-assistant-phone-light.png) | ![FL-SC11-02 step 5, U36, dark](../../images/02-matters-and-documents/u36-professional/5-assistant-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc11-20-matter-assistant-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc11-20-matter-assistant-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc11-20-matter-assistant-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc11-20-matter-assistant-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc11-20-matter-assistant-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc11-20-matter-assistant-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc11-20-matter-assistant-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc11-20-matter-assistant-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC11-05 Matter](../../data/e-sc11-05-matter.md),
[E-SC11-09 Deadline](../../data/e-sc11-09-deadline.md), shown as the entity pages list them, with their examples.

## Actions

- Ask: [UC-SC11-20](../../use-cases/02-matters-and-documents/uc-sc11-20-ask-the-assistant-about-a-matter.md), step 1.
- Confirm a draft:
  [UC-SC11-20](../../use-cases/02-matters-and-documents/uc-sc11-20-ask-the-assistant-about-a-matter.md), step 4.

## States

- Normal: the conversation with answers, links and drafts.
- Empty: suggested questions.
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a walled matter: the AI assistant refuses.
- Read-only: nothing from walled matters outside the team.
- Offline: not available offline: the AI assistant needs the network; the last answers stay readable.

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

⬅️ [S-SC11-19 Performance](../06-firm-management/s-sc11-19-performance.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC11-21 Notary](../07-notaries-brokers-officers-and-auditors/s-sc11-21-notary.md)
