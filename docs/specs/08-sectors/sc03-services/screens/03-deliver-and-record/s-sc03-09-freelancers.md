🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💼 [SC03 Services](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC03-03 Deliver and record](README.md) › 🖥️ S-SC03-09 Freelancers

# 🖥️ S-SC03-09 Freelancers

**Status:** ✅ specified

## Personas

- [U24 Engagement manager](../../../../01-users/personas/u24-engagement-manager.md)
- [U04 Purchasing](../../../../01-users/personas/u04-purchasing.md)

## Purpose

Used to engage freelancers and subcontractors
([UC-SC03-09](../../use-cases/03-deliver-and-record/uc-sc03-09-engage-freelancers-and-subcontractors.md)).

## Entry points

Services in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC03-03 step 2, U24 | desktop | ![FL-SC03-03 step 2, U24, light](../../images/03-deliver-and-record/u24-engagement-manager/2-approve-desktop-light.png) | ![FL-SC03-03 step 2, U24, dark](../../images/03-deliver-and-record/u24-engagement-manager/2-approve-desktop-dark.png) |
| FL-SC03-03 step 2, U24 | phone | ![FL-SC03-03 step 2, U24, light](../../images/03-deliver-and-record/u24-engagement-manager/2-approve-phone-light.png) | ![FL-SC03-03 step 2, U24, dark](../../images/03-deliver-and-record/u24-engagement-manager/2-approve-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc03-09-freelancers-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc03-09-freelancers-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc03-09-freelancers-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc03-09-freelancers-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc03-09-freelancers-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc03-09-freelancers-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc03-09-freelancers-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc03-09-freelancers-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC03-10 Freelance contract](../../data/e-sc03-10-freelance-contract.md), shown as the entity pages list
them, with their examples.

## Actions

- Contract: [UC-SC03-09](../../use-cases/03-deliver-and-record/uc-sc03-09-engage-freelancers-and-subcontractors.md),
  step 1.
- Collect documents:
  [UC-SC03-09](../../use-cases/03-deliver-and-record/uc-sc03-09-engage-freelancers-and-subcontractors.md), step 2.
- Approve time: [UC-SC03-09](../../use-cases/03-deliver-and-record/uc-sc03-09-engage-freelancers-and-subcontractors.md),
  step 3.
- Pay bills: [UC-SC03-09](../../use-cases/03-deliver-and-record/uc-sc03-09-engage-freelancers-and-subcontractors.md),
  step 4.

## States

- Normal: freelance contracts with documents and their dates, time and bills.
- Empty: "No freelancer", with New contract.
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, documents expired: the freelancer is blocked from time and
  staffing ([BR-SC03-09](../../business-rules/br-sc03-09-freelancers-checked.md)).
- Read-only: an ended contract is read-only.
- Offline: not available offline: office work at a desk on shared engagement figures. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC03-10 Freelance contract](../../data/e-sc03-10-freelance-contract.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC03-10 Freelance contract | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U04, U24 | `u04-purchasing/s-sc03-09-freelancers-e-sc03-10-freelance-contract-active-desktop-{light,dark}.png`, `u24-engagement-manager/s-sc03-09-freelancers-e-sc03-10-freelance-contract-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC03-03 Deliver and record](../../flows/fl-sc03-03-deliver-and-record.md)

## Open questions

None.

---

⬅️ [S-SC03-08 Revenue](../04-bill-and-recognise/s-sc03-08-revenue.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC03-10 Engagement margin](../04-bill-and-recognise/s-sc03-10-engagement-margin.md)
