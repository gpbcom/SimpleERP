🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🎙️ [F4 Meetings](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F4-10 Benchmark additions](README.md) › 🖥️ S-F4-15 Chat

# 🖥️ S-F4-15 Chat

**Status:** ✅ specified

## Personas

- [U01 Employee](../../../../01-users/personas/u01-employee.md)
- [U02 Manager](../../../../01-users/personas/u02-manager.md)

## Purpose

Chat with colleagues.

## Entry points

Meetings in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F4-10 step 1, U01 | phone | ![FL-F4-10 step 1, U01, light](../../images/10-benchmark-additions/u01-employee/1-chat-phone-light.png) | ![FL-F4-10 step 1, U01, dark](../../images/10-benchmark-additions/u01-employee/1-chat-phone-dark.png) |
| FL-F4-10 step 1, U01 | desktop | ![FL-F4-10 step 1, U01, light](../../images/10-benchmark-additions/u01-employee/1-chat-desktop-light.png) | ![FL-F4-10 step 1, U01, dark](../../images/10-benchmark-additions/u01-employee/1-chat-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f04-15-chat-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f04-15-chat-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f04-15-chat-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f04-15-chat-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f04-15-chat-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f04-15-chat-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f04-15-chat-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f04-15-chat-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Chat with colleagues, as the wireframe shows.
- Empty: No conversation yet, with New message.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: an archived channel.
- Offline: Not available offline (D38): on a phone or a computer, the offline banner replaces the actions and nothing is
  changed until the network is back; nothing is queued.

Shown entities (VD-15): [E-F4-10 Chat channel](../../data/e-f04-10-chat-channel.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F4-10 Chat channel | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U01, U02 | `u01-employee/s-f04-15-chat-e-f04-10-chat-channel-active-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f04-15-chat-e-f04-10-chat-channel-active-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; approvals and lists also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-F4-10 Benchmark additions](../../flows/fl-f04-10-benchmark-additions.md)

## Open questions

None.

---

⬅️ [S-F4-14 Meeting automations](../08-share-and-reuse-outside/s-f04-14-meeting-automations.md) · ⬆️ [Up](README.md) ·
➡️ [S-F4-16 Booking page](s-f04-16-booking-page.md)
