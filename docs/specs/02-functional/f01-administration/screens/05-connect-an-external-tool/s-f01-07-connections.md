🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛡️ [F1 Administration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F1-05 Connect an external tool](README.md) › 🖥️ S-F1-07 Connections

# 🖥️ S-F1-07 Connections

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

List, add and change the company's outside connections: MCP servers, A2A agents, and (UC-F1-08, UC-F1-09) AI providers
and single sign-on.

## Entry points

Administration › Connections.

## Wireframe

```text
+------------------------------------------------------------------+
| Connections                                        [+ Connect]   |
|------------------------------------------------------------------|
| Name        Kind   Address               Tools  Changes  Status  |
| GitHub      MCP    https://api.github... 28/40  ask      on      |
| Crunchbase  MCP    https://mcp.crunch... 6/6    -        on      |
| Partner bot A2A    https://agent.partn.. 3/3    trusted  off     |
|------------------------------------------------------------------|
| ! Data sent to these services leaves your server.               |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F1-05 step 1, U07 | desktop | ![FL-F1-05 step 1, U07, light](../../images/05-connect-an-external-tool/u07-administrator/1-connect-and-review-desktop-light.png) | ![FL-F1-05 step 1, U07, dark](../../images/05-connect-an-external-tool/u07-administrator/1-connect-and-review-desktop-dark.png) |
| Error E1, U07 | desktop | ![Error E1, U07, light](../../images/05-connect-an-external-tool/u07-administrator/e1-server-unreachable-desktop-light.png) | ![Error E1, U07, dark](../../images/05-connect-an-external-tool/u07-administrator/e1-server-unreachable-desktop-dark.png) |
| Error E2, U07 | desktop | ![Error E2, U07, light](../../images/05-connect-an-external-tool/u07-administrator/e2-address-not-secure-desktop-light.png) | ![Error E2, U07, dark](../../images/05-connect-an-external-tool/u07-administrator/e2-address-not-secure-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f01-07-connections-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f01-07-connections-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f01-07-connections-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f01-07-connections-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f01-07-connections-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f01-07-connections-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f01-07-connections-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f01-07-connections-offline-desktop-dark.png) |

## Fields and columns

As [E-F1-08 Agent connection](../../data/e-f01-08-agent-connection.md#fields).

## Actions

| Action | Who | Result |
|---|---|---|
| Connect | administrator | UC-F1-07 |
| Review tools | administrator | Turn tools on or off (BR-F1-13) |
| Always ask / trusted | administrator | BR-F1-14 |
| Turn off / on | administrator | The AI assistant stops or starts using it |

## States

- Normal: List, add and change the company's outside connections: MCP servers, A2A agents, and (UC-F1-08, UC-F1-09) AI
  providers
and single sign-on, as the wireframe shows.
- Empty: "No outside connection: simple-ERP keeps everything on your server."
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: not reachable, credentials refused.
- Read-only: the IT provider's own connections, for the client's administrator.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.
- New tools to review: a badge on the row.

Shown entities (VD-15): [E-F1-08 Agent connection](../../data/e-f01-08-agent-connection.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F1-08 Agent connection | Off | Badge "Off"; a new record starts here; next: On (UC-F1-07); fields editable within the role | U07 | `u07-administrator/s-f01-07-connections-e-f01-08-agent-connection-off-desktop-{light,dark}.png` |
| E-F1-08 Agent connection | On | Badge "On"; next: Off (UC-F1-07); fields editable within the role | U07 | `u07-administrator/s-f01-07-connections-e-f01-08-agent-connection-on-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop and tablet.

## Accessibility

The warning is text with an icon, not colour only.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-05 Modal](../../../../04-ux/design-system/components/c-05-modal.md)

## Shown in

- [FL-F1-05 Connect an external tool](../../flows/fl-f01-05-connect-an-external-tool.md)

## Open questions

None.

---

⬅️ [S-F1-06 Role editor](../04-edit-a-role/s-f01-06-role-editor.md) · ⬆️ [Up](README.md) ·
➡️ [S-F1-08 AI settings](../06-choose-an-ai-provider/s-f01-08-ai-settings.md)
