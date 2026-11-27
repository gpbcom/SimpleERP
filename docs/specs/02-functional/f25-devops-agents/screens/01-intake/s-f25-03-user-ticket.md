🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F25-01 Intake](README.md) › 🖥️ S-F25-03 USER ticket

# 🖥️ S-F25-03 USER ticket

**Status:** ✅ specified

## Personas

- [U47 SimpleERP maintainer](../../../../01-users/personas/u47-simpleerp-maintainer.md)

## Purpose

Open the USER feature with its ticket.

## Entry points

DevOps agents in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F25-01 step 3, U47 | desktop | ![FL-F25-01 step 3, U47, light](../../images/01-intake/u47-simpleerp-maintainer/3-user-ticket-desktop-light.png) | ![FL-F25-01 step 3, U47, dark](../../images/01-intake/u47-simpleerp-maintainer/3-user-ticket-desktop-dark.png) |
| FL-F25-01 step 3, U47 | phone | ![FL-F25-01 step 3, U47, light](../../images/01-intake/u47-simpleerp-maintainer/3-user-ticket-phone-light.png) | ![FL-F25-01 step 3, U47, dark](../../images/01-intake/u47-simpleerp-maintainer/3-user-ticket-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f25-03-user-ticket-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f25-03-user-ticket-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f25-03-user-ticket-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f25-03-user-ticket-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f25-03-user-ticket-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f25-03-user-ticket-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f25-03-user-ticket-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f25-03-user-ticket-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the USER ticket draft with labels and reporter link.
- Empty: "No request waiting".
- Loading: the frame and titles show at once with placeholder rows for the ticket; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: filed tickets read-only here.
- Offline: not available offline: GitHub is online. D38 keeps only today's schedule, time and intervention records
  offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing
  is queued until the connection is back.

Shown entities (VD-15): [E-F25-02 USER feature](../../data/e-f25-02-user-feature.md),
[E-F25-03 USER ticket](../../data/e-f25-03-user-ticket.md), [E-F25-11 Triage](../../data/e-f25-11-triage.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F25-02 USER feature | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U47 | `u47-simpleerp-maintainer/s-f25-03-user-ticket-e-f25-02-user-feature-active-{desktop,phone}-{light,dark}.png` |
| E-F25-03 USER ticket | Open | Badge "Open"; a new record starts here; next: Late or Flagged (UC-F25-21); fields editable within the role | U47 | `u47-simpleerp-maintainer/s-f25-03-user-ticket-e-f25-03-user-ticket-open-{desktop,phone}-{light,dark}.png` |
| E-F25-03 USER ticket | Late | Badge "Late"; next: Open (BR-F25-03); fields editable within the role | U47 | `u47-simpleerp-maintainer/s-f25-03-user-ticket-e-f25-03-user-ticket-late-{desktop,phone}-{light,dark}.png` |
| E-F25-03 USER ticket | Flagged | Badge "Flagged"; next: Open (BR-F25-03); fields editable within the role | U47 | `u47-simpleerp-maintainer/s-f25-03-user-ticket-e-f25-03-user-ticket-flagged-{desktop,phone}-{light,dark}.png` |
| E-F25-11 Triage | Acknowledged | Badge "Acknowledged"; next: Resolved or Late (UC-F25-03, UC-F25-21); fields editable within the role | U47 | `u47-simpleerp-maintainer/s-f25-03-user-ticket-e-f25-11-triage-acknowledged-{desktop,phone}-{light,dark}.png` |
| E-F25-11 Triage | Late | Badge "Late"; next: Resolved (UC-F25-03); fields editable within the role | U47 | `u47-simpleerp-maintainer/s-f25-03-user-ticket-e-f25-11-triage-late-{desktop,phone}-{light,dark}.png` |
| E-F25-11 Triage | Resolved | Badge "Resolved"; final: read-only, no next state; the history shows how it got here | U47 | `u47-simpleerp-maintainer/s-f25-03-user-ticket-e-f25-11-triage-resolved-{desktop,phone}-{light,dark}.png` |

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

- [FL-F25-01 Intake](../../flows/fl-f25-01-intake.md)

## Open questions

None.

---

⬅️ [S-F25-02 Request a feature](s-f25-02-request-a-feature.md) · ⬆️ [Up](README.md) ·
➡️ [S-F25-04 Duplicates](s-f25-04-duplicates.md)
