🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💼 [SC03 Services](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC03-04 Bill and recognise](README.md) › 🖥️ S-SC03-08 Revenue

# 🖥️ S-SC03-08 Revenue

**Status:** ✅ specified

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)
- [U24 Engagement manager](../../../../01-users/personas/u24-engagement-manager.md)

## Purpose

Used to follow work in progress and recognise revenue,
[UC-SC03-08](../../use-cases/04-bill-and-recognise/uc-sc03-08-follow-work-in-progress-and-recognise-revenue.md).

## Entry points

Services in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC03-04 step 3, U05 | desktop | ![FL-SC03-04 step 3, U05, light](../../images/04-bill-and-recognise/u05-accounting/3-revenue-desktop-light.png) | ![FL-SC03-04 step 3, U05, dark](../../images/04-bill-and-recognise/u05-accounting/3-revenue-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc03-08-revenue-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc03-08-revenue-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc03-08-revenue-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc03-08-revenue-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc03-08-revenue-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc03-08-revenue-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc03-08-revenue-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc03-08-revenue-offline-desktop-dark.png) |

## Fields and columns

The fields of [E-SC03-09 Revenue position](../../data/e-sc03-09-revenue-position.md), shown as the entity pages list
them, with their examples.

## Actions

- Compute progress:
  [UC-SC03-08](../../use-cases/04-bill-and-recognise/uc-sc03-08-follow-work-in-progress-and-recognise-revenue.md), step
  1.
- Review:
  [UC-SC03-08](../../use-cases/04-bill-and-recognise/uc-sc03-08-follow-work-in-progress-and-recognise-revenue.md), step
  2.
- Post entries:
  [UC-SC03-08](../../use-cases/04-bill-and-recognise/uc-sc03-08-follow-work-in-progress-and-recognise-revenue.md), step
  3.
- Read the margin:
  [UC-SC03-08](../../use-cases/04-bill-and-recognise/uc-sc03-08-follow-work-in-progress-and-recognise-revenue.md), step
  4.

## States

- Normal: per engagement: progress, billed, work in progress, deferred, and the entries.
- Empty: "No engagement to recognise".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, progress missing: the engagement manager is asked before posting.
- Read-only: a closed month is read-only.
- Offline: not available offline: office work at a desk on shared engagement figures. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC03-09 Revenue position](../../data/e-sc03-09-revenue-position.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC03-09 Revenue position | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U05, U24 | `u05-accounting/s-sc03-08-revenue-e-sc03-09-revenue-position-active-desktop-{light,dark}.png`, `u24-engagement-manager/s-sc03-08-revenue-e-sc03-09-revenue-position-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC03-04 Bill and recognise](../../flows/fl-sc03-04-bill-and-recognise.md)

## Open questions

None.

---

⬅️ [S-SC03-07 Milestones](s-sc03-07-milestones.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC03-09 Freelancers](../03-deliver-and-record/s-sc03-09-freelancers.md)
