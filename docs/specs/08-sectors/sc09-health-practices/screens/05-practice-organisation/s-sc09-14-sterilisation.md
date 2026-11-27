🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🩺 [SC09 Health practices](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC09-05 Practice organisation](README.md) › 🖥️ S-SC09-14 Sterilisation

# 🖥️ S-SC09-14 Sterilisation

**Status:** ✅ specified

## Personas

- [U33 Medical secretary](../../../../01-users/personas/u33-medical-secretary.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Used to trace consumables and sterilisation,
[UC-SC09-14](../../use-cases/05-practice-organisation/uc-sc09-14-trace-consumables-and-sterilisation.md).

## Entry points

Health practices in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC09-05 step 3, U33 | desktop | ![FL-SC09-05 step 3, U33, light](../../images/05-practice-organisation/u33-medical-secretary/3-sterilisation-desktop-light.png) | ![FL-SC09-05 step 3, U33, dark](../../images/05-practice-organisation/u33-medical-secretary/3-sterilisation-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc09-14-sterilisation-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc09-14-sterilisation-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc09-14-sterilisation-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc09-14-sterilisation-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc09-14-sterilisation-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc09-14-sterilisation-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc09-14-sterilisation-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc09-14-sterilisation-offline-desktop-dark.png) |

## Fields and columns

The fields of [E-SC09-11 Sterilisation cycle](../../data/e-sc09-11-sterilisation-cycle.md), shown as the entity pages
list them, with their examples.

## Actions

- Run a cycle: [UC-SC09-14](../../use-cases/05-practice-organisation/uc-sc09-14-trace-consumables-and-sterilisation.md),
  step 1.
- Record: [UC-SC09-14](../../use-cases/05-practice-organisation/uc-sc09-14-trace-consumables-and-sterilisation.md), step
  2.
- Link to patients:
  [UC-SC09-14](../../use-cases/05-practice-organisation/uc-sc09-14-trace-consumables-and-sterilisation.md), step 3.
- Restock: [UC-SC09-14](../../use-cases/05-practice-organisation/uc-sc09-14-trace-consumables-and-sterilisation.md),
  step 4.

## States

- Normal: cycles with result, instruments and linked patients.
- Empty: "No cycle".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a failed cycle: the instruments are blocked.
- Read-only: recorded cycles are read-only.
- Offline: cycles recorded on the tablet are kept and sync later,
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).

Shown entities (VD-15): [E-SC09-11 Sterilisation cycle](../../data/e-sc09-11-sterilisation-cycle.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC09-11 Sterilisation cycle | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U13, U33 | `u13-owner/s-sc09-14-sterilisation-e-sc09-11-sterilisation-cycle-active-{desktop,phone}-{light,dark}.png`, `u33-medical-secretary/s-sc09-14-sterilisation-e-sc09-11-sterilisation-cycle-active-desktop-{light,dark}.png` |

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

⬅️ [S-SC09-13 Cost sharing](s-sc09-13-cost-sharing.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC09-15 Practice accounts](s-sc09-15-practice-accounts.md)
