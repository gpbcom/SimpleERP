🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛡️ [F1 Administration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F1-08 The provider and its client companies](README.md) › 🖥️ S-F1-11 Provider access log

# 🖥️ S-F1-11 Provider access log

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Show the client every session of its IT provider (BR-F1-20).

## Entry points

Administration › Provider access; the notification of a new session.

## Wireframe

```text
+------------------------------------------------------------------+
| Provider access (NetServ)                                        |
|------------------------------------------------------------------|
| Started            By            Ended     Actions               |
| 10 Nov 10:02       Paul (NetServ) 10:31     3 [see]              |
|   - changed role Sales Lyon                                      |
|   - opened invoice INV-2026-0042                                 |
|   - updated connection GitHub                                    |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F1-08 step 4, U07 | desktop | ![FL-F1-08 step 4, U07, light](../../images/08-provider-and-client-companies/u07-administrator/4-client-sees-the-session-desktop-light.png) | ![FL-F1-08 step 4, U07, dark](../../images/08-provider-and-client-companies/u07-administrator/4-client-sees-the-session-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f01-11-provider-access-log-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f01-11-provider-access-log-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f01-11-provider-access-log-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f01-11-provider-access-log-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f01-11-provider-access-log-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f01-11-provider-access-log-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f01-11-provider-access-log-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f01-11-provider-access-log-offline-desktop-dark.png) |

## Fields and columns

As [E-F1-12 Provider session](../../data/e-f01-12-provider-session.md#fields).

## Actions

| Action | Who | Result |
|---|---|---|
| See | client administrator | The session's actions |

## States

- Normal: Show the client every session of its IT provider (BR-F1-20), as the wireframe shows.
- Empty: "Your provider has not entered simple-ERP."
- Loading: placeholders in the layout of the wireframe; actions are disabled until the record has loaded.
- Error: the error message pattern (D122).
- Read-only: always: the log cannot be changed (BR-F1-20).
- Offline: Not available offline (D38): on a phone or a computer, the offline banner replaces the actions and nothing is
  changed until the network is back; nothing is queued.
- A session in progress is marked live.

Shown entities (VD-15): [E-F1-12 Provider session](../../data/e-f01-12-provider-session.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F1-12 Provider session | Live | Badge "Live"; a new record starts here; next: Closed (UC-F1-11); fields editable within the role | U07 | `u07-administrator/s-f01-11-provider-access-log-e-f01-12-provider-session-live-desktop-{light,dark}.png` |
| E-F1-12 Provider session | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U07 | `u07-administrator/s-f01-11-provider-access-log-e-f01-12-provider-session-closed-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Works on a phone.

## Accessibility

Each session is a group with its actions listed.

## Components

- [C-14 Timeline](../../../../04-ux/design-system/components/c-14-timeline.md)

## Shown in

- [FL-F1-08 The provider and its client companies](../../flows/fl-f01-08-provider-and-client-companies.md)

## Open questions

None.

---

⬅️ [S-F1-10 Client companies](s-f01-10-client-companies.md) · ⬆️ [Up](README.md) ·
➡️ [S-F1-12 Users overview dashboard](../09-administration-reports/s-f01-12-users-overview-dashboard.md)
