🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🤖 [F3 Assistant](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F3-06 Use an outside tool](README.md) › 🖥️ S-F3-06 My connections

# 🖥️ S-F3-06 My connections

**Status:** ✅ specified

## Personas

Roles allowed per connection (D80); every internal persona can be: [U01](../../../../01-users/personas/u01-employee.md),
[U02](../../../../01-users/personas/u02-manager.md), [U03](../../../../01-users/personas/u03-sales.md),
[U04](../../../../01-users/personas/u04-purchasing.md), [U05](../../../../01-users/personas/u05-accounting.md),
[U06](../../../../01-users/personas/u06-hr.md), [U07](../../../../01-users/personas/u07-administrator.md),
[U12](../../../../01-users/personas/u12-marketing.md), [U13](../../../../01-users/personas/u13-owner.md),
[U14](../../../../01-users/personas/u14-field-worker.md),
[U15](../../../../01-users/personas/u15-warehouse-operator.md),
[U16](../../../../01-users/personas/u16-office-worker.md).

## Purpose

Connect and remove one's own accounts for the AI assistant (D171).

## Entry points

My profile › My connections; the "Reconnect" link of an expired sign-in.

## Wireframe

```text
+------------------------------------------------------------------+
| My connections                                                    |
|------------------------------------------------------------------|
| Service           | Status                 |                     |
| Google Calendar   | Connected (marie@...)  | [Remove]            |
| Outlook mail      | Not connected          | [Connect]           |
|------------------------------------------------------------------|
| Company connections you can use: Shipping tool, GitHub            |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F3-06 step 3, U01 | desktop | ![FL-F3-06 step 3, U01, light](../../images/06-use-an-outside-tool/u01-employee/3-my-connections-desktop-light.png) | ![FL-F3-06 step 3, U01, dark](../../images/06-use-an-outside-tool/u01-employee/3-my-connections-desktop-dark.png) |
| FL-F3-06 step 3, U01 | phone | ![FL-F3-06 step 3, U01, light](../../images/06-use-an-outside-tool/u01-employee/3-my-connections-phone-light.png) | ![FL-F3-06 step 3, U01, dark](../../images/06-use-an-outside-tool/u01-employee/3-my-connections-phone-dark.png) |
| Error E2, U01 | phone | ![Error E2, U01, light](../../../f04-meetings/images/06-set-up-meetings-and-calendars/u01-employee/e2-calendar-to-reconnect-phone-light.png) | ![Error E2, U01, dark](../../../f04-meetings/images/06-set-up-meetings-and-calendars/u01-employee/e2-calendar-to-reconnect-phone-dark.png) |
| Error E2, U01 | desktop | ![Error E2, U01, light](../../../f04-meetings/images/06-set-up-meetings-and-calendars/u01-employee/e2-calendar-to-reconnect-desktop-light.png) | ![Error E2, U01, dark](../../../f04-meetings/images/06-set-up-meetings-and-calendars/u01-employee/e2-calendar-to-reconnect-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f03-06-my-connections-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f03-06-my-connections-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f03-06-my-connections-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f03-06-my-connections-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f03-06-my-connections-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f03-06-my-connections-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f03-06-my-connections-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f03-06-my-connections-offline-phone-dark.png) |

## Fields and columns

Service, status, account; the company connections the user's role may use.

## Actions

| Action | Who | Result |
|---|---|---|
| Connect | the user | Sign-in at the service, then Connected |
| Remove | the user | The connection and its tokens are deleted |

## States

- Normal: Connect and remove one's own accounts for the AI assistant (D171), as the wireframe shows.
- Empty: "Your administrator has not allowed personal services."
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the sign-in failed, the error message pattern (D122).
- Read-only: services the administrator has not allowed, shown greyed.
- Offline: Not available offline (D38): on a phone or a computer, the offline banner replaces the actions and nothing is
  changed until the network is back; nothing is queued.
- Connected, not connected, expired.

Shown entities (VD-15): [E-F3-22 AI assistant request](../../data/e-f03-22-ai-assistant-request.md),
[E-F3-08 Outside call](../../data/e-f03-08-outside-call.md),
[E-F4-05 Calendar sync](../../../f04-meetings/data/e-f04-05-calendar-sync.md),
[E-F3-07 Personal connection](../../data/e-f03-07-personal-connection.md),
[E-F4-25 Meeting recording setting](../../../f04-meetings/data/e-f04-25-meeting-recording-setting.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F3-22 AI assistant request | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U01 | `u01-employee/s-f03-06-my-connections-e-f03-22-ai-assistant-request-active-{desktop,phone}-{light,dark}.png` |
| E-F3-08 Outside call | Refused | Badge "Refused"; a new record starts here; no other state; fields editable within the role | U01 | `u01-employee/s-f03-06-my-connections-e-f03-08-outside-call-refused-{desktop,phone}-{light,dark}.png` |
| E-F4-05 Calendar sync | In sync | Badge "In sync"; a new record starts here; next: To reconnect or Failing (UC-F4-08); fields editable within the role | U01 | `u01-employee/s-f03-06-my-connections-e-f04-05-calendar-sync-in-sync-{desktop,phone}-{light,dark}.png` |
| E-F4-05 Calendar sync | To reconnect | Badge "To reconnect"; next: In sync (UC-F4-08); fields editable within the role | U01 | `u01-employee/s-f03-06-my-connections-e-f04-05-calendar-sync-to-reconnect-{desktop,phone}-{light,dark}.png` |
| E-F4-05 Calendar sync | Failing | Badge "Failing"; next: In sync (UC-F4-08); fields editable within the role | U01 | `u01-employee/s-f03-06-my-connections-e-f04-05-calendar-sync-failing-{desktop,phone}-{light,dark}.png` |
| E-F3-07 Personal connection | Connected | Badge "Connected"; a new record starts here; next: Expired (UC-F3-06); fields editable within the role | U01 | `u01-employee/s-f03-06-my-connections-e-f03-07-personal-connection-connected-{desktop,phone}-{light,dark}.png` |
| E-F3-07 Personal connection | Expired | Badge "Expired"; next: Connected (UC-F3-06); fields editable within the role | U01 | `u01-employee/s-f03-06-my-connections-e-f03-07-personal-connection-expired-{desktop,phone}-{light,dark}.png` |
| E-F4-25 Meeting recording setting | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U01 | `u01-employee/s-f03-06-my-connections-e-f04-25-meeting-recording-setting-active-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop and phone.

## Accessibility

A table with headers; buttons name the service ("Connect Outlook mail").

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F3-06 Use an outside tool](../../flows/fl-f03-06-use-an-outside-tool.md)

## Open questions

None.

---

⬅️ [S-F3-05 Configuration requests](../05-find-and-get-guided/s-f03-05-configuration-requests.md) · ⬆️ [Up](README.md) ·
➡️ [S-F3-07 Knowledge base](../07-manage-knowledge/s-f03-07-knowledge-base.md)
