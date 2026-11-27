🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F19 Feature factory (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F19-01 Describe and order](README.md) › 🖥️ S-F19-01 Feature chat

# 🖥️ S-F19-01 Feature chat

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Describe a feature in plain words.

## Entry points

Feature factory in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F19-01 step 1, U13 | desktop | ![FL-F19-01 step 1, U13, light](../../images/01-describe-and-order/u13-owner/1-describe-desktop-light.png) | ![FL-F19-01 step 1, U13, dark](../../images/01-describe-and-order/u13-owner/1-describe-desktop-dark.png) |
| FL-F19-01 step 1, U13 | phone | ![FL-F19-01 step 1, U13, light](../../images/01-describe-and-order/u13-owner/1-describe-phone-light.png) | ![FL-F19-01 step 1, U13, dark](../../images/01-describe-and-order/u13-owner/1-describe-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f19-01-feature-chat-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f19-01-feature-chat-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f19-01-feature-chat-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f19-01-feature-chat-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f19-01-feature-chat-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f19-01-feature-chat-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f19-01-feature-chat-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f19-01-feature-chat-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the conversation with the chatbot and the first outline.
- Empty: "Describe what you need": examples of features.
- Loading: the frame and titles show at once with placeholder rows for the conversation; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: other users see requests they started only.
- Offline: the chatbot says it is offline; the message is queued and answered when the network is back, with a
  notification (D182).

Shown entities (VD-15): [E-F19-01 Feature request](../../data/e-f19-01-feature-request.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F19-01 Feature request | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07, U13 | `u07-administrator/s-f19-01-feature-chat-e-f19-01-feature-request-active-desktop-{light,dark}.png`, `u13-owner/s-f19-01-feature-chat-e-f19-01-feature-request-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-F19-01 Describe and order](../../flows/fl-f19-01-describe-and-order.md)

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [S-F19-02 Specification](s-f19-02-specification.md)
