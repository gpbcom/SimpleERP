🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F25-03 Bugs](README.md) › 🖥️ S-F25-10 Fix pull request

# 🖥️ S-F25-10 Fix pull request

**Status:** ✅ specified

## Personas

- [U47 simple-ERP maintainer](../../../../01-users/personas/u47-simple-erp-maintainer.md)

## Purpose

Propose the fix as a pull request, tests first.

## Entry points

DevOps agents in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F25-03 step 3, U47 | desktop | ![FL-F25-03 step 3, U47, light](../../images/03-bugs/u47-simple-erp-maintainer/3-fix-pr-desktop-light.png) | ![FL-F25-03 step 3, U47, dark](../../images/03-bugs/u47-simple-erp-maintainer/3-fix-pr-desktop-dark.png) |
| FL-F25-03 step 3, U47 | phone | ![FL-F25-03 step 3, U47, light](../../images/03-bugs/u47-simple-erp-maintainer/3-fix-pr-phone-light.png) | ![FL-F25-03 step 3, U47, dark](../../images/03-bugs/u47-simple-erp-maintainer/3-fix-pr-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f25-10-fix-pull-request-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f25-10-fix-pull-request-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f25-10-fix-pull-request-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f25-10-fix-pull-request-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f25-10-fix-pull-request-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f25-10-fix-pull-request-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f25-10-fix-pull-request-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f25-10-fix-pull-request-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the failing test, the fix and the pull request.
- Empty: "No fix yet".
- Loading: the frame and titles show at once with placeholder rows for the fix; within 1 second (D408) the data replaces
  them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: maintainers merge.
- Offline: not available offline: online. D38 keeps only today's schedule, time and intervention records offline. A
  banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-F25-05 Agent pull request](../../data/e-f25-05-agent-pull-request.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F25-05 Agent pull request | In review | Badge "In review"; a new record starts here; next: Proposed or Declined (UC-F25-06, UC-F25-23); fields editable within the role | U47 | `u47-simple-erp-maintainer/s-f25-10-fix-pull-request-e-f25-05-agent-pull-request-in-review-{desktop,phone}-{light,dark}.png` |
| E-F25-05 Agent pull request | Proposed | Badge "Proposed"; next: Checked or Declined (UC-F25-06, UC-F25-23); fields editable within the role | U47 | `u47-simple-erp-maintainer/s-f25-10-fix-pull-request-e-f25-05-agent-pull-request-proposed-{desktop,phone}-{light,dark}.png` |
| E-F25-05 Agent pull request | Declined | Badge "Declined"; final: read-only, no next state; the history shows how it got here | U47 | `u47-simple-erp-maintainer/s-f25-10-fix-pull-request-e-f25-05-agent-pull-request-declined-{desktop,phone}-{light,dark}.png` |
| E-F25-05 Agent pull request | Checked | Badge "Checked"; next: Open or Declined (UC-F25-23); fields editable within the role | U47 | `u47-simple-erp-maintainer/s-f25-10-fix-pull-request-e-f25-05-agent-pull-request-checked-{desktop,phone}-{light,dark}.png` |
| E-F25-05 Agent pull request | Open | Badge "Open"; next: Waiting (BR-F25-05); fields editable within the role | U47 | `u47-simple-erp-maintainer/s-f25-10-fix-pull-request-e-f25-05-agent-pull-request-open-{desktop,phone}-{light,dark}.png` |
| E-F25-05 Agent pull request | Waiting | Badge "Waiting"; next: Open (UC-F25-23); fields editable within the role | U47 | `u47-simple-erp-maintainer/s-f25-10-fix-pull-request-e-f25-05-agent-pull-request-waiting-{desktop,phone}-{light,dark}.png` |

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

- [FL-F25-03 Bugs](../../flows/fl-f25-03-bugs.md)

## Open questions

None.

---

⬅️ [S-F25-09 Root cause](s-f25-09-root-cause.md) · ⬆️ [Up](README.md) ·
➡️ [S-F25-11 PRODUCT ticket](s-f25-11-product-ticket.md)
