🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F25-01 Intake](README.md) › 🖥️ S-F25-21 Triage board

# 🖥️ S-F25-21 Triage board

**Status:** ✅ specified

## Personas

- [U47 simple-ERP maintainer](../../../../01-users/personas/u47-simple-erp-maintainer.md)

## Purpose

Show USER tickets by priority with severity and time left.

## Entry points

Maintainer space, Triage.

## Wireframe

```text
Triage board                          Late: 1     Critical: 1
-------------------------------------------------------------------------------
Ticket   Title                    Severity   Priority   Ack by     Resolve by
#313     Invoices fail to send    critical   1          13:00      2026-11-14
#320     Label typo               low        14         -          next release
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F25-01 step 5, U47 | desktop | ![FL-F25-01 step 5, U47, light](../../images/01-intake/u47-simple-erp-maintainer/5-triage-board-desktop-light.png) | ![FL-F25-01 step 5, U47, dark](../../images/01-intake/u47-simple-erp-maintainer/5-triage-board-desktop-dark.png) |
| FL-F25-01 step 5, U47 | phone | ![FL-F25-01 step 5, U47, light](../../images/01-intake/u47-simple-erp-maintainer/5-triage-board-phone-light.png) | ![FL-F25-01 step 5, U47, dark](../../images/01-intake/u47-simple-erp-maintainer/5-triage-board-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f25-21-triage-board-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f25-21-triage-board-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f25-21-triage-board-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f25-21-triage-board-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f25-21-triage-board-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f25-21-triage-board-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f25-21-triage-board-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f25-21-triage-board-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Ticket | E-F25-11 ticket | number | no | yes |
| Severity | E-F25-11 severity | list | yes | yes |
| Priority | E-F25-11 priority | number | yes | yes |
| Targets | E-F25-11 | dates | no | yes |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Confirm triage | row | maintainer | targets set |
| Change severity | row | maintainer | targets recomputed |

## States

- Normal: tickets with triage and time left.
- Empty: "No ticket to triage".
- Loading: the frame and titles show at once with placeholder rows for the tickets; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: a ticket late, flagged.
- Read-only: hosting engineers read.
- Offline: not available offline: the board reads GitHub online. D38 keeps only today's schedule, time and intervention
  records offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and
  nothing is queued until the connection is back.

Shown entities (VD-15): [E-F25-03 USER ticket](../../data/e-f25-03-user-ticket.md),
[E-F25-11 Triage](../../data/e-f25-11-triage.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F25-03 USER ticket | Late | Badge "Late"; next: Open (BR-F25-03); fields editable within the role | U47 | `u47-simple-erp-maintainer/s-f25-21-triage-board-e-f25-03-user-ticket-late-{desktop,phone}-{light,dark}.png` |
| E-F25-03 USER ticket | Flagged | Badge "Flagged"; next: Open (BR-F25-03); fields editable within the role | U47 | `u47-simple-erp-maintainer/s-f25-21-triage-board-e-f25-03-user-ticket-flagged-{desktop,phone}-{light,dark}.png` |
| E-F25-11 Triage | Triaged | Badge "Triaged"; a new record starts here; next: Acknowledged or Late (UC-F25-21, UC-F25-03); fields editable within the role | U47 | `u47-simple-erp-maintainer/s-f25-21-triage-board-e-f25-11-triage-triaged-{desktop,phone}-{light,dark}.png` |
| E-F25-11 Triage | Acknowledged | Badge "Acknowledged"; next: Resolved or Late (UC-F25-03, UC-F25-21); fields editable within the role | U47 | `u47-simple-erp-maintainer/s-f25-21-triage-board-e-f25-11-triage-acknowledged-{desktop,phone}-{light,dark}.png` |
| E-F25-11 Triage | Late | Badge "Late"; next: Resolved (UC-F25-03); fields editable within the role | U47 | `u47-simple-erp-maintainer/s-f25-21-triage-board-e-f25-11-triage-late-{desktop,phone}-{light,dark}.png` |
| E-F25-11 Triage | Resolved | Badge "Resolved"; final: read-only, no next state; the history shows how it got here | U47 | `u47-simple-erp-maintainer/s-f25-21-triage-board-e-f25-11-triage-resolved-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F25-01 Intake](../../flows/fl-f25-01-intake.md)

## Open questions

None.

---

⬅️ [S-F25-20 Requests assistant](../05-tell-the-customer/s-f25-20-requests-assistant.md) · ⬆️ [Up](README.md) ·
➡️ [S-F25-22 Vulnerability case](../06-vulnerability-handling/s-f25-22-vulnerability-case.md)
