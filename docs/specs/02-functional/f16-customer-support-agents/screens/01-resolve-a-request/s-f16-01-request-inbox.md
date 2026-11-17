🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🎧 [F16 Customer support agents](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F16-01 Resolve a request](README.md) › 🖥️ S-F16-01 Request inbox

# 🖥️ S-F16-01 Request inbox

**Status:** ✅ specified

## Personas

- [U09 Customer](../../../../01-users/personas/u09-customer.md)
- [U16 Office worker](../../../../01-users/personas/u16-office-worker.md)

## Purpose

Resolve a customer request automatically.

## Entry points

Support in the menu.

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F16-01 step 1, U16 | desktop | ![FL-F16-01 step 1, U16, light](../../images/01-resolve-a-request/u16-office-worker/1-inbox-with-agents-desktop-light.png) | ![FL-F16-01 step 1, U16, dark](../../images/01-resolve-a-request/u16-office-worker/1-inbox-with-agents-desktop-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-f16-01-request-inbox-empty-phone-light.png) | ![Empty, dark](../../images/states/s-f16-01-request-inbox-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-f16-01-request-inbox-loading-phone-light.png) | ![Loading, dark](../../images/states/s-f16-01-request-inbox-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-f16-01-request-inbox-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-f16-01-request-inbox-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f16-01-request-inbox-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f16-01-request-inbox-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: incoming requests with intent, branch, mode (automatic, shadow, human) and status.
- Empty: "No request yet": shown before the first channel sends one, with a link to connections.
- Loading: the frame and titles show at once with placeholder rows for the requests; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: the owner reads; resolved requests are read-only.
- Offline: not available offline: the inbox reads the channels on the server. D38 keeps only today's schedule, time and
  intervention records offline. A banner says the connection is lost; what is on screen stays visible, every action is
  disabled and nothing is queued until the connection is back.

Shown entities (VD-15): [E-F16-01 Customer request](../../data/e-f16-01-customer-request.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F16-01 Customer request | New | Badge "New"; a new record starts here; next: In progress (UC-F16-12); fields editable within the role | U16 | `u16-office-worker/s-f16-01-request-inbox-e-f16-01-customer-request-new-{desktop,phone}-{light,dark}.png` |
| E-F16-01 Customer request | In progress | Badge "In progress"; next: Resolved or Waiting (UC-F16-01, UC-F16-07); fields editable within the role | U16 | `u16-office-worker/s-f16-01-request-inbox-e-f16-01-customer-request-in-progress-{desktop,phone}-{light,dark}.png` |
| E-F16-01 Customer request | Resolved | Badge "Resolved"; next: Escalated (UC-F16-04); fields editable within the role | U16 | `u16-office-worker/s-f16-01-request-inbox-e-f16-01-customer-request-resolved-{desktop,phone}-{light,dark}.png` |
| E-F16-01 Customer request | Waiting | Badge "Waiting"; next: Resolved (UC-F16-01); fields editable within the role | U16 | `u16-office-worker/s-f16-01-request-inbox-e-f16-01-customer-request-waiting-{desktop,phone}-{light,dark}.png` |
| E-F16-01 Customer request | Escalated | Badge "Escalated"; next: Resolved (UC-F16-01); fields editable within the role | U16 | `u16-office-worker/s-f16-01-request-inbox-e-f16-01-customer-request-escalated-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; the review queue also on the phone.

## Accessibility

Labelled controls; modes and scores as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-11 Chat panel](../../../../04-ux/design-system/components/c-11-chat-panel.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F16-01 Resolve a request](../../flows/fl-f16-01-resolve-a-request.md)

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [S-F16-02 Procedure editor](../02-automate-an-intent/s-f16-02-procedure-editor.md)
