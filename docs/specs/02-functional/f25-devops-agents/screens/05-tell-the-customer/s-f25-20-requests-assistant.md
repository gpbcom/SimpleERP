🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F25-05 Tell the customer](README.md) › 🖥️ S-F25-20 Requests assistant

# 🖥️ S-F25-20 Requests assistant

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Ask the AI assistant about my requests.

## Entry points

DevOps agents in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F25-05 step 4, U13 | desktop | ![FL-F25-05 step 4, U13, light](../../images/05-tell-the-customer/u13-owner/4-assistant-desktop-light.png) | ![FL-F25-05 step 4, U13, dark](../../images/05-tell-the-customer/u13-owner/4-assistant-desktop-dark.png) |
| FL-F25-05 step 4, U13 | phone | ![FL-F25-05 step 4, U13, light](../../images/05-tell-the-customer/u13-owner/4-assistant-phone-light.png) | ![FL-F25-05 step 4, U13, dark](../../images/05-tell-the-customer/u13-owner/4-assistant-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f25-20-requests-assistant-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f25-20-requests-assistant-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f25-20-requests-assistant-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f25-20-requests-assistant-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f25-20-requests-assistant-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f25-20-requests-assistant-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f25-20-requests-assistant-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f25-20-requests-assistant-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the conversation about my requests.
- Empty: example questions.
- Loading: the frame and titles show at once with placeholder rows for the conversation; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: own company only.
- Offline: the AI assistant says it is offline; the question is queued and answered when the network is back, with a
  notification (D182).

Shown entities (VD-15): [E-F25-09 Request status](../../data/e-f25-09-request-status.md),
[E-F25-14 Vote](../../data/e-f25-14-vote.md),
[E-F25-01 Bug or feature request](../../data/e-f25-01-bug-or-feature-request.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F25-09 Request status | Planned | Badge "Planned"; a new record starts here; next: Received or Declined (BR-F25-09, UC-F25-14); fields editable within the role | U07, U13 | `u07-administrator/s-f25-20-requests-assistant-e-f25-09-request-status-planned-desktop-{light,dark}.png`, `u13-owner/s-f25-20-requests-assistant-e-f25-09-request-status-planned-{desktop,phone}-{light,dark}.png` |
| E-F25-09 Request status | Received | Badge "Received"; next: Shipped or Declined (UC-F25-15, UC-F25-14); fields editable within the role | U07, U13 | `u07-administrator/s-f25-20-requests-assistant-e-f25-09-request-status-received-desktop-{light,dark}.png`, `u13-owner/s-f25-20-requests-assistant-e-f25-09-request-status-received-{desktop,phone}-{light,dark}.png` |
| E-F25-09 Request status | Shipped | Badge "Shipped"; final: read-only, no next state; the history shows how it got here | U07, U13 | `u07-administrator/s-f25-20-requests-assistant-e-f25-09-request-status-shipped-desktop-{light,dark}.png`, `u13-owner/s-f25-20-requests-assistant-e-f25-09-request-status-shipped-{desktop,phone}-{light,dark}.png` |
| E-F25-14 Vote | Counted | Badge "Counted"; a new record starts here; next: Withdrawn (UC-F25-12); fields editable within the role | U07, U13 | `u07-administrator/s-f25-20-requests-assistant-e-f25-14-vote-counted-desktop-{light,dark}.png`, `u13-owner/s-f25-20-requests-assistant-e-f25-14-vote-counted-{desktop,phone}-{light,dark}.png` |
| E-F25-14 Vote | Withdrawn | Badge "Withdrawn"; final: read-only, no next state; the history shows how it got here | U07, U13 | `u07-administrator/s-f25-20-requests-assistant-e-f25-14-vote-withdrawn-desktop-{light,dark}.png`, `u13-owner/s-f25-20-requests-assistant-e-f25-14-vote-withdrawn-{desktop,phone}-{light,dark}.png` |
| E-F25-01 Bug or feature request | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07, U13 | `u07-administrator/s-f25-20-requests-assistant-e-f25-01-bug-or-feature-request-active-desktop-{light,dark}.png`, `u13-owner/s-f25-20-requests-assistant-e-f25-01-bug-or-feature-request-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-F25-05 Tell the customer](../../flows/fl-f25-05-tell-the-customer.md)

## Open questions

None.

---

⬅️ [S-F25-19 Agent quality](../04-approve-and-govern/s-f25-19-agent-quality.md) · ⬆️ [Up](README.md) ·
➡️ [S-F25-21 Triage board](../01-intake/s-f25-21-triage-board.md)
