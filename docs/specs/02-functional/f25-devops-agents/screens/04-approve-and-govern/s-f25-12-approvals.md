🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F25-04 Approve and govern](README.md) › 🖥️ S-F25-12 Approvals

# 🖥️ S-F25-12 Approvals

**Status:** ✅ specified

## Personas

- [U47 SimpleERP maintainer](../../../../01-users/personas/u47-simpleerp-maintainer.md)

## Purpose

Approve or refuse agents' tickets.

## Entry points

DevOps agents in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F25-04 step 1, U47 | desktop | ![FL-F25-04 step 1, U47, light](../../images/04-approve-and-govern/u47-simpleerp-maintainer/1-approve-desktop-light.png) | ![FL-F25-04 step 1, U47, dark](../../images/04-approve-and-govern/u47-simpleerp-maintainer/1-approve-desktop-dark.png) |
| FL-F25-04 step 1, U47 | phone | ![FL-F25-04 step 1, U47, light](../../images/04-approve-and-govern/u47-simpleerp-maintainer/1-approve-phone-light.png) | ![FL-F25-04 step 1, U47, dark](../../images/04-approve-and-govern/u47-simpleerp-maintainer/1-approve-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f25-12-approvals-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f25-12-approvals-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f25-12-approvals-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f25-12-approvals-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f25-12-approvals-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f25-12-approvals-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f25-12-approvals-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f25-12-approvals-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: tickets waiting for approval.
- Empty: "Nothing to approve".
- Loading: the frame and titles show at once with placeholder rows for the tickets; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: hosting engineers read.
- Offline: not available offline: online. D38 keeps only today's schedule, time and intervention records offline. A
  banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-F25-08 Approval](../../data/e-f25-08-approval.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F25-08 Approval | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U47 | `u47-simpleerp-maintainer/s-f25-12-approvals-e-f25-08-approval-active-{desktop,phone}-{light,dark}.png` |

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
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F25-04 Approve and govern](../../flows/fl-f25-04-approve-and-govern.md)

## Open questions

None.

---

⬅️ [S-F25-11 PRODUCT ticket](../03-bugs/s-f25-11-product-ticket.md) · ⬆️ [Up](README.md) ·
➡️ [S-F25-13 Revisions](s-f25-13-revisions.md)
