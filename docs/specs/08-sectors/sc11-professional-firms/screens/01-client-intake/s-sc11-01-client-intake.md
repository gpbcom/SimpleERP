🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › ⚖️ [SC11 Professional firms](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC11-01 Client intake](README.md) › 🖥️ S-SC11-01 Client intake

# 🖥️ S-SC11-01 Client intake

**Status:** ✅ specified

## Personas

- [U37 Professional's assistant](../../../../01-users/personas/u37-assistant.md)
- [U36 Professional](../../../../01-users/personas/u36-professional.md)

## Purpose

Used to open a client file and check identity
([UC-SC11-01](../../use-cases/01-client-intake/uc-sc11-01-open-a-client-file-and-check-identity.md)).

## Entry points

Professional firms in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC11-01 step 1, U37 | desktop | ![FL-SC11-01 step 1, U37, light](../../images/01-client-intake/u37-assistant/1-identity-desktop-light.png) | ![FL-SC11-01 step 1, U37, dark](../../images/01-client-intake/u37-assistant/1-identity-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc11-01-client-intake-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc11-01-client-intake-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc11-01-client-intake-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc11-01-client-intake-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc11-01-client-intake-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc11-01-client-intake-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc11-01-client-intake-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc11-01-client-intake-offline-desktop-dark.png) |

## Fields and columns

The fields of [E-SC11-01 Client identity](../../data/e-sc11-01-client-identity.md),
[E-SC11-02 Beneficial owner](../../data/e-sc11-02-beneficial-owner.md), shown as the entity pages list them, with their
examples.

## Actions

- Collect documents: [UC-SC11-01](../../use-cases/01-client-intake/uc-sc11-01-open-a-client-file-and-check-identity.md),
  step 1.
- Record beneficial owners:
  [UC-SC11-01](../../use-cases/01-client-intake/uc-sc11-01-open-a-client-file-and-check-identity.md), step 2.
- Rate the risk: [UC-SC11-01](../../use-cases/01-client-intake/uc-sc11-01-open-a-client-file-and-check-identity.md),
  step 3.
- Approve: [UC-SC11-01](../../use-cases/01-client-intake/uc-sc11-01-open-a-client-file-and-check-identity.md), step 4.

## States

- Normal: the client's identity, documents, owners and risk.
- Empty: "No client".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a beneficial owner unknown: the client is blocked.
- Read-only: assistants see identity, not suspicions.
- Offline: not available offline: office work on confidential matters that stay on the server. Offline work is kept for
  the phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC11-01 Client identity](../../data/e-sc11-01-client-identity.md),
[E-SC11-02 Beneficial owner](../../data/e-sc11-02-beneficial-owner.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC11-01 Client identity | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U36, U37 | `u36-professional/s-sc11-01-client-intake-e-sc11-01-client-identity-active-{desktop,phone}-{light,dark}.png`, `u37-assistant/s-sc11-01-client-intake-e-sc11-01-client-identity-active-desktop-{light,dark}.png` |
| E-SC11-02 Beneficial owner | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U36, U37 | `u36-professional/s-sc11-01-client-intake-e-sc11-02-beneficial-owner-active-{desktop,phone}-{light,dark}.png`, `u37-assistant/s-sc11-01-client-intake-e-sc11-02-beneficial-owner-active-desktop-{light,dark}.png` |

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

⬆️ [Up](README.md) · ➡️ [S-SC11-02 Conflict check](s-sc11-02-conflict-check.md)
