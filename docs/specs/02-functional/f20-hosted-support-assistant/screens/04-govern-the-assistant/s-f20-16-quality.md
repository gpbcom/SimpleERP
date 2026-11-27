🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛟 [F20 Hosted support assistant (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F20-04 Govern the AI assistant](README.md) › 🖥️ S-F20-16 Quality

# 🖥️ S-F20-16 Quality

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U48 Hosting engineer](../../../../01-users/personas/u48-hosting-engineer.md)

## Purpose

Rate the help and review quality.

## Entry points

Hosted support assistant in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F20-04 step 1, U07 | desktop | ![FL-F20-04 step 1, U07, light](../../images/04-govern-the-assistant/u07-administrator/1-quality-desktop-light.png) | ![FL-F20-04 step 1, U07, dark](../../images/04-govern-the-assistant/u07-administrator/1-quality-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f20-16-quality-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f20-16-quality-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f20-16-quality-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f20-16-quality-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f20-16-quality-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f20-16-quality-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f20-16-quality-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f20-16-quality-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: ratings and samples to review.
- Empty: "No rating yet".
- Loading: the frame and titles show at once with placeholder rows for the ratings; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: customers rate only.
- Offline: not available offline: reviews run online. D38 keeps only today's schedule, time and intervention records
  offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing
  is queued until the connection is back.

Shown entities (VD-15): [E-F20-10 Rating](../../data/e-f20-10-rating.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F20-10 Rating | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07, U48 | `u07-administrator/s-f20-16-quality-e-f20-10-rating-active-desktop-{light,dark}.png`, `u48-hosting-engineer/s-f20-16-quality-e-f20-10-rating-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-F20-04 Govern the AI assistant](../../flows/fl-f20-04-govern-the-assistant.md)

## Open questions

None.

---

⬅️ [S-F20-15 Security incident](../03-incidents/s-f20-15-security-incident.md) · ⬆️ [Up](README.md) ·
➡️ [S-F20-17 Assistant rights](s-f20-17-assistant-rights.md)
