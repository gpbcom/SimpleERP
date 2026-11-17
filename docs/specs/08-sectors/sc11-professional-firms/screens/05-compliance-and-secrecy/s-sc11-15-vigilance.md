🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › ⚖️ [SC11 Professional firms](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC11-05 Compliance and secrecy](README.md) › 🖥️ S-SC11-15 Vigilance

# 🖥️ S-SC11-15 Vigilance

**Status:** 🔄 waiting for the owner

## Personas

- [U36 Professional](../../../../01-users/personas/u36-professional.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Used to run anti-money-laundering vigilance,
[UC-SC11-15](../../use-cases/05-compliance-and-secrecy/uc-sc11-15-run-anti-money-laundering-vigilance.md).

## Entry points

Professional firms in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC11-05 step 1, U36 | desktop | ![FL-SC11-05 step 1, U36, light](../../images/05-compliance-and-secrecy/u36-professional/1-vigilance-desktop-light.png) | ![FL-SC11-05 step 1, U36, dark](../../images/05-compliance-and-secrecy/u36-professional/1-vigilance-desktop-dark.png) |
| FL-SC11-05 step 1, U36 | phone | ![FL-SC11-05 step 1, U36, light](../../images/05-compliance-and-secrecy/u36-professional/1-vigilance-phone-light.png) | ![FL-SC11-05 step 1, U36, dark](../../images/05-compliance-and-secrecy/u36-professional/1-vigilance-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc11-15-vigilance-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc11-15-vigilance-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc11-15-vigilance-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc11-15-vigilance-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc11-15-vigilance-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc11-15-vigilance-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc11-15-vigilance-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc11-15-vigilance-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC11-01 Client identity](../../data/e-sc11-01-client-identity.md),
[E-SC11-12 Vigilance record](../../data/e-sc11-12-vigilance-record.md), shown as the entity pages list them, with their
examples.

## Actions

- Review risks:
  [UC-SC11-15](../../use-cases/05-compliance-and-secrecy/uc-sc11-15-run-anti-money-laundering-vigilance.md), step 1.
- Record a suspicion:
  [UC-SC11-15](../../use-cases/05-compliance-and-secrecy/uc-sc11-15-run-anti-money-laundering-vigilance.md), step 2.
- Report: [UC-SC11-15](../../use-cases/05-compliance-and-secrecy/uc-sc11-15-run-anti-money-laundering-vigilance.md),
  step 3.
- Follow: [UC-SC11-15](../../use-cases/05-compliance-and-secrecy/uc-sc11-15-run-anti-money-laundering-vigilance.md),
  step 4.

## States

- Normal: risk reviews and suspicions.
- Empty: "No review due".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, the client told: never: no client-facing message can mention it.
- Read-only: only compliance sees suspicions.
- Offline: not available offline: office work on confidential matters that stay on the server. Offline work is kept for
  the phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC11-12 Vigilance record](../../data/e-sc11-12-vigilance-record.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC11-12 Vigilance record | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U13, U36 | `u13-owner/s-sc11-15-vigilance-e-sc11-12-vigilance-record-recorded-{desktop,phone}-{light,dark}.png`, `u36-professional/s-sc11-15-vigilance-e-sc11-12-vigilance-record-recorded-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC11-05 Compliance and secrecy](../../flows/fl-sc11-05-compliance-and-secrecy.md)

## Open questions

None.

---

⬅️ [S-SC11-14 Work in progress](../06-firm-management/s-sc11-14-work-in-progress.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC11-16 Access walls](s-sc11-16-access-walls.md)
