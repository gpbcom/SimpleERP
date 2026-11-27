🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › ⚖️ [SC11 Professional firms](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC11-04 Deadlines and filings](README.md) › 🖥️ S-SC11-08 Deadlines

# 🖥️ S-SC11-08 Deadlines

**Status:** ✅ specified

## Personas

- [U37 Professional's assistant](../../../../01-users/personas/u37-assistant.md)
- [U36 Professional](../../../../01-users/personas/u36-professional.md)

## Purpose

Used to follow deadlines, hearings and limitation periods,
[UC-SC11-08](../../use-cases/04-deadlines-and-filings/uc-sc11-08-follow-deadlines-hearings-and-limitation-periods.md).

## Entry points

Professional firms in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC11-04 step 1, U37 | desktop | ![FL-SC11-04 step 1, U37, light](../../images/04-deadlines-and-filings/u37-assistant/1-deadlines-desktop-light.png) | ![FL-SC11-04 step 1, U37, dark](../../images/04-deadlines-and-filings/u37-assistant/1-deadlines-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc11-08-deadlines-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc11-08-deadlines-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc11-08-deadlines-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc11-08-deadlines-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc11-08-deadlines-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc11-08-deadlines-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc11-08-deadlines-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc11-08-deadlines-offline-desktop-dark.png) |

## Fields and columns

The fields of [E-SC11-09 Deadline](../../data/e-sc11-09-deadline.md), shown as the entity pages list them, with their
examples.

## Actions

- Enter:
  [UC-SC11-08](../../use-cases/04-deadlines-and-filings/uc-sc11-08-follow-deadlines-hearings-and-limitation-periods.md),
  step 1.
- Remind:
  [UC-SC11-08](../../use-cases/04-deadlines-and-filings/uc-sc11-08-follow-deadlines-hearings-and-limitation-periods.md),
  step 2.
- Do:
  [UC-SC11-08](../../use-cases/04-deadlines-and-filings/uc-sc11-08-follow-deadlines-hearings-and-limitation-periods.md),
  step 3.
- Done:
  [UC-SC11-08](../../use-cases/04-deadlines-and-filings/uc-sc11-08-follow-deadlines-hearings-and-limitation-periods.md),
  step 4.

## States

- Normal: deadlines with owner, date, kind and state.
- Empty: "No deadline".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a missed reminder: the partner is alerted.
- Read-only: done deadlines are read-only.
- Offline: the week's deadlines stay readable on the phone; changes wait for the network.

Shown entities (VD-15): [E-SC11-09 Deadline](../../data/e-sc11-09-deadline.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC11-09 Deadline | Open | Badge "Open"; a new record starts here; next: Done (UC-SC11-08); fields editable within the role | U36, U37 | `u36-professional/s-sc11-08-deadlines-e-sc11-09-deadline-open-{desktop,phone}-{light,dark}.png`, `u37-assistant/s-sc11-08-deadlines-e-sc11-09-deadline-open-desktop-{light,dark}.png` |
| E-SC11-09 Deadline | Done | Badge "Done"; final: read-only, no next state; the history shows how it got here | U36, U37 | `u36-professional/s-sc11-08-deadlines-e-sc11-09-deadline-done-{desktop,phone}-{light,dark}.png`, `u37-assistant/s-sc11-08-deadlines-e-sc11-09-deadline-done-desktop-{light,dark}.png` |

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

- [FL-SC11-04 Deadlines and filings](../../flows/fl-sc11-04-deadlines-and-filings.md)

## Open questions

None.

---

⬅️ [S-SC11-07 Client funds](../03-time-and-billing/s-sc11-07-client-funds.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC11-09 Documents](../02-matters-and-documents/s-sc11-09-documents.md)
