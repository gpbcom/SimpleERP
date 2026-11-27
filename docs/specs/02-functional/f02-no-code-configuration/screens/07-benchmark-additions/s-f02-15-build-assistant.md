🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔧 [F2 No-code configuration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F2-07 Benchmark additions](README.md) › 🖥️ S-F2-15 Build assistant

# 🖥️ S-F2-15 Build assistant

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U02 Manager](../../../../01-users/personas/u02-manager.md)

## Purpose

Build with plain language.

## Entry points

No-code configuration in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F2-07 step 4, U07 | desktop | ![FL-F2-07 step 4, U07, light](../../images/07-benchmark-additions/u07-administrator/4-build-with-words-desktop-light.png) | ![FL-F2-07 step 4, U07, dark](../../images/07-benchmark-additions/u07-administrator/4-build-with-words-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f02-15-build-assistant-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f02-15-build-assistant-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f02-15-build-assistant-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f02-15-build-assistant-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f02-15-build-assistant-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f02-15-build-assistant-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f02-15-build-assistant-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f02-15-build-assistant-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Build with plain language, as the wireframe shows.
- Empty: the prompt box with three example requests.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: drafts built by another configurator.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F2-15 Sandbox](../../data/e-f02-15-sandbox.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F2-15 Sandbox | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U02, U07 | `u02-manager/s-f02-15-build-assistant-e-f02-15-sandbox-active-{desktop,phone}-{light,dark}.png`, `u07-administrator/s-f02-15-build-assistant-e-f02-15-sandbox-active-desktop-{light,dark}.png` |

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

- [FL-F2-07 Benchmark additions](../../flows/fl-f02-07-benchmark-additions.md)

## Open questions

None.

---

⬅️ [S-F2-14 Signature requests](s-f02-14-signature-requests.md) · ⬆️ [Up](README.md) ·
➡️ [S-F2-16 Sandbox](s-f02-16-sandbox.md)
