🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💼 [SC03 Services](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC03-03 Deliver and record](README.md) ›
🖥️ S-SC03-15 Engagement assistant

# 🖥️ S-SC03-15 Engagement assistant

**Status:** 🔄 waiting for the owner

## Personas

- [U24 Engagement manager](../../../../01-users/personas/u24-engagement-manager.md)
- [U16 Office worker](../../../../01-users/personas/u16-office-worker.md)

## Purpose

Used to ask the AI assistant about an engagement
([UC-SC03-15](../../use-cases/03-deliver-and-record/uc-sc03-15-ask-the-assistant-about-an-engagement.md)).

## Entry points

Services in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC03-03 step 3, U24 | desktop | ![FL-SC03-03 step 3, U24, light](../../images/03-deliver-and-record/u24-engagement-manager/3-freelancer-desktop-light.png) | ![FL-SC03-03 step 3, U24, dark](../../images/03-deliver-and-record/u24-engagement-manager/3-freelancer-desktop-dark.png) |
| FL-SC03-03 step 3, U24 | phone | ![FL-SC03-03 step 3, U24, light](../../images/03-deliver-and-record/u24-engagement-manager/3-freelancer-phone-light.png) | ![FL-SC03-03 step 3, U24, dark](../../images/03-deliver-and-record/u24-engagement-manager/3-freelancer-phone-dark.png) |
| Error E1, U24 | desktop | ![Error E1, U24, light](../../images/03-deliver-and-record/u24-engagement-manager/e1-freelancer-blocked-desktop-light.png) | ![Error E1, U24, dark](../../images/03-deliver-and-record/u24-engagement-manager/e1-freelancer-blocked-desktop-dark.png) |
| Error E1, U24 | phone | ![Error E1, U24, light](../../images/03-deliver-and-record/u24-engagement-manager/e1-freelancer-blocked-phone-light.png) | ![Error E1, U24, dark](../../images/03-deliver-and-record/u24-engagement-manager/e1-freelancer-blocked-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc03-15-engagement-assistant-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc03-15-engagement-assistant-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc03-15-engagement-assistant-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc03-15-engagement-assistant-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc03-15-engagement-assistant-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc03-15-engagement-assistant-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc03-15-engagement-assistant-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc03-15-engagement-assistant-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC03-01 Engagement](../../data/e-sc03-01-engagement.md),
[E-SC03-05 Timesheet](../../data/e-sc03-05-timesheet.md), shown as the entity pages list them, with their examples.

## Actions

- Ask about E-207:
  [UC-SC03-15](../../use-cases/03-deliver-and-record/uc-sc03-15-ask-the-assistant-about-an-engagement.md), step 1.
- Confirm a draft:
  [UC-SC03-15](../../use-cases/03-deliver-and-record/uc-sc03-15-ask-the-assistant-about-an-engagement.md), step 4.

## States

- Normal: the conversation with answers, links and drafts.
- Empty: suggested questions about the engagement.
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, an action beyond the user's rights: the AI assistant refuses and
  says which role can do it.
- Read-only: answers only for roles that cannot act.
- Offline: not available offline: the AI assistant needs the network; the last answers stay readable.

Shown entities (VD-15): [E-SC03-05 Timesheet](../../data/e-sc03-05-timesheet.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC03-05 Timesheet | Draft | Badge "Draft"; a new record starts here; next: Submitted or Rejected (UC-SC03-05); fields editable within the role | U16, U24 | `u16-office-worker/s-sc03-15-engagement-assistant-e-sc03-05-timesheet-draft-{desktop,phone}-{light,dark}.png`, `u24-engagement-manager/s-sc03-15-engagement-assistant-e-sc03-05-timesheet-draft-{desktop,phone}-{light,dark}.png` |
| E-SC03-05 Timesheet | Submitted | Badge "Submitted"; next: Approved or Rejected (UC-SC03-05); fields editable within the role | U16, U24 | `u16-office-worker/s-sc03-15-engagement-assistant-e-sc03-05-timesheet-submitted-{desktop,phone}-{light,dark}.png`, `u24-engagement-manager/s-sc03-15-engagement-assistant-e-sc03-05-timesheet-submitted-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC03-03 Deliver and record](../../flows/fl-sc03-03-deliver-and-record.md)

## Open questions

None.

---

⬅️ [S-SC03-14 Foreign billing](../04-bill-and-recognise/s-sc03-14-foreign-billing.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC03-16 Staffing assignments](../06-staffing-agencies-and-certification/s-sc03-16-staffing-assignments.md)
