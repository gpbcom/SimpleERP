🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🤖 [F3 Assistant](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F3-10 Benchmark additions](README.md) › 🖥️ S-F3-14 Agents

# 🖥️ S-F3-14 Agents

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)
- [U02 Manager](../../../../01-users/personas/u02-manager.md)

## Purpose

Create and run AI agents.

## Entry points

Assistant in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F3-10 step 1, U07 | desktop | ![FL-F3-10 step 1, U07, light](../../images/10-benchmark-additions/u07-administrator/1-agents-desktop-light.png) | ![FL-F3-10 step 1, U07, dark](../../images/10-benchmark-additions/u07-administrator/1-agents-desktop-dark.png) |
| Error E1, U07 | desktop | ![Error E1, U07, light](../../images/10-benchmark-additions/u07-administrator/e1-over-limit-desktop-light.png) | ![Error E1, U07, dark](../../images/10-benchmark-additions/u07-administrator/e1-over-limit-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f03-14-agents-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f03-14-agents-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f03-14-agents-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f03-14-agents-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f03-14-agents-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f03-14-agents-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f03-14-agents-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f03-14-agents-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Create and run AI agents, as the wireframe shows.
- Empty: No agent yet, with Create an agent and the examples.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: a running agent's settings until it is paused.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F3-15 Agent](../../data/e-f03-15-agent.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F3-15 Agent | Paid | Badge "Paid"; a new record starts here; next: Paused (UC-F3-11); fields editable within the role | U02, U05, U07 | `u02-manager/s-f03-14-agents-e-f03-15-agent-paid-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-f03-14-agents-e-f03-15-agent-paid-desktop-{light,dark}.png`, `u07-administrator/s-f03-14-agents-e-f03-15-agent-paid-desktop-{light,dark}.png` |
| E-F3-15 Agent | Paused | Badge "Paused"; next: Paid (UC-F3-11); fields editable within the role | U02, U05, U07 | `u02-manager/s-f03-14-agents-e-f03-15-agent-paused-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-f03-14-agents-e-f03-15-agent-paused-desktop-{light,dark}.png`, `u07-administrator/s-f03-14-agents-e-f03-15-agent-paused-desktop-{light,dark}.png` |

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

- [FL-F3-10 Benchmark additions](../../flows/fl-f03-10-benchmark-additions.md)

## Open questions

None.

---

⬅️ [S-F3-13 Assistant usage dashboard](../01-ask-the-assistant/s-f03-13-assistant-usage-dashboard.md) ·
⬆️ [Up](README.md) · ➡️ [S-F3-15 Agent governance](s-f03-15-agent-governance.md)
