🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F25-02 Feature requests](README.md) › 🖥️ S-F25-07 SPECS feature

# 🖥️ S-F25-07 SPECS feature

**Status:** ✅ specified

## Personas

- [U47 SimpleERP maintainer](../../../../01-users/personas/u47-simpleerp-maintainer.md)

## Purpose

Create the SPECS feature and its tickets.

## Entry points

DevOps agents in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F25-02 step 3, U47 | desktop | ![FL-F25-02 step 3, U47, light](../../images/02-feature-requests/u47-simpleerp-maintainer/3-specs-feature-desktop-light.png) | ![FL-F25-02 step 3, U47, dark](../../images/02-feature-requests/u47-simpleerp-maintainer/3-specs-feature-desktop-dark.png) |
| FL-F25-02 step 3, U47 | phone | ![FL-F25-02 step 3, U47, light](../../images/02-feature-requests/u47-simpleerp-maintainer/3-specs-feature-phone-light.png) | ![FL-F25-02 step 3, U47, dark](../../images/02-feature-requests/u47-simpleerp-maintainer/3-specs-feature-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f25-07-specs-feature-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f25-07-specs-feature-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f25-07-specs-feature-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f25-07-specs-feature-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f25-07-specs-feature-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f25-07-specs-feature-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f25-07-specs-feature-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f25-07-specs-feature-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the SPECS feature and tickets with the approval label.
- Empty: "No feature".
- Loading: the frame and titles show at once with placeholder rows for the feature; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: maintainers remove the label.
- Offline: not available offline: online. D38 keeps only today's schedule, time and intervention records offline. A
  banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-F25-15 SPECS feature](../../data/e-f25-15-specs-feature.md),
[E-F25-06 Agent ticket](../../data/e-f25-06-agent-ticket.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F25-15 SPECS feature | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U47 | `u47-simpleerp-maintainer/s-f25-07-specs-feature-e-f25-15-specs-feature-active-{desktop,phone}-{light,dark}.png` |
| E-F25-06 Agent ticket | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U47 | `u47-simpleerp-maintainer/s-f25-07-specs-feature-e-f25-06-agent-ticket-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-F25-02 Feature requests](../../flows/fl-f25-02-feature-requests.md)

## Open questions

None.

---

⬅️ [S-F25-06 Spec pull request](s-f25-06-spec-pull-request.md) · ⬆️ [Up](README.md) ·
➡️ [S-F25-08 Reproduce](../03-bugs/s-f25-08-reproduce.md)
