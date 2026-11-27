🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛡️ [F1 Administration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F1-15 Security and group data](README.md) › 🖥️ S-F1-27 Sessions and devices

# 🖥️ S-F1-27 Sessions and devices

**Status:** ✅ specified

## Personas

- - [U07 Administrator](../../../../01-users/personas/u07-administrator.md): the sessions of the company.
- - [U01 Employee](../../../../01-users/personas/u01-employee.md): their own sessions.

## Purpose

See every session and trusted device, end them, and for the administrator, end those of others.

## Entry points

Profile › Sessions and devices; Administration › Users › a user › Sessions; the notification of a new sign-in.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Sessions and devices          Claire P.                  [Sign out everywhere else]         |
| ------------------------------------------------------------------------------------------- |
| DEVICE                  KIND      PLACE          LAST ACTIVE     TRUSTED UNTIL              |
| This laptop (current)   Browser   Lyon, FR       now             2026-12-14                 |
| Claire's phone          App       Lyon, FR       10 min ago      2026-12-10      [End]      |
| Unknown tablet          Browser   Warsaw, PL     3 days ago      -               [End]      |
| Trusted devices: 2   [Revoke]        Trusted devices are switched on by the security policy. |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F1-15 step 1, U07 | desktop | ![FL-F1-15 step 1, U07, light](../../images/15-security-and-group-data/u07-administrator/1-sessions-and-devices-desktop-light.png) | ![FL-F1-15 step 1, U07, dark](../../images/15-security-and-group-data/u07-administrator/1-sessions-and-devices-desktop-dark.png) |
| FL-F1-15 step 1, U07 | desktop | ![FL-F1-15 step 1, U07, light](../../images/15-security-and-group-data/u07-administrator/1-sessions-and-devices-desktop-light.png) | ![FL-F1-15 step 1, U07, dark](../../images/15-security-and-group-data/u07-administrator/1-sessions-and-devices-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f01-27-sessions-and-devices-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f01-27-sessions-and-devices-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f01-27-sessions-and-devices-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f01-27-sessions-and-devices-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f01-27-sessions-and-devices-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f01-27-sessions-and-devices-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f01-27-sessions-and-devices-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f01-27-sessions-and-devices-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Device | E-F1-23 device name and kind | text and icon | no | yes |
| Place | E-F1-23 country and town | text | no | yes |
| Last active | E-F1-23 last active | relative time | no | yes |
| Trusted until | E-F1-23 trusted until | date | revoke only | no |
| State | E-F1-23 state | badge | no | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| End | row | the user, the administrator | the session ends (UC-F1-24) |
| Sign out everywhere else | header | the user | every other session ends |
| Trust this device | current row | the user | the second factor is skipped for the period |
| Revoke | trusted row | the user, the administrator | the device is no longer trusted |
| End all sessions | user page | the administrator | every session of that user ends |

## States

- Normal: the sessions of the user, the current one first, with the trusted devices below.
- Empty: No other session: this is the only device signed in.
- Loading: The list loads first; the places follow.
- Error: the error message pattern (D122); a session that already ended shows Already ended.
- Read-only: a deactivated user's sessions, all ended, kept for the audit.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F1-23 User session](../../data/e-f01-23-user-session.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F1-23 User session | Active | Badge "Active"; a new record starts here; next: Signed out, Revoked, Ended by a change or Expired (UC-F1-24, BR-F1-33, UC-F1-21); fields editable within the role | U07, U01 | `u07-administrator/s-f01-27-sessions-and-devices-e-f01-23-user-session-active-desktop-{light,dark}.png`, `u01-employee/s-f01-27-sessions-and-devices-e-f01-23-user-session-active-{desktop,phone}-{light,dark}.png` |
| E-F1-23 User session | Signed out | Badge "Signed out"; final: read-only, no next state; the history shows how it got here | U07, U01 | `u07-administrator/s-f01-27-sessions-and-devices-e-f01-23-user-session-signed-out-desktop-{light,dark}.png`, `u01-employee/s-f01-27-sessions-and-devices-e-f01-23-user-session-signed-out-{desktop,phone}-{light,dark}.png` |
| E-F1-23 User session | Revoked | Badge "Revoked"; final: read-only, no next state; the history shows how it got here | U07, U01 | `u07-administrator/s-f01-27-sessions-and-devices-e-f01-23-user-session-revoked-desktop-{light,dark}.png`, `u01-employee/s-f01-27-sessions-and-devices-e-f01-23-user-session-revoked-{desktop,phone}-{light,dark}.png` |
| E-F1-23 User session | Ended by a change | Badge "Ended by a change"; final: read-only, no next state; the history shows how it got here | U07, U01 | `u07-administrator/s-f01-27-sessions-and-devices-e-f01-23-user-session-ended-by-a-change-desktop-{light,dark}.png`, `u01-employee/s-f01-27-sessions-and-devices-e-f01-23-user-session-ended-by-a-change-{desktop,phone}-{light,dark}.png` |
| E-F1-23 User session | Expired | Badge "Expired"; final: read-only, no next state; the history shows how it got here | U07, U01 | `u07-administrator/s-f01-27-sessions-and-devices-e-f01-23-user-session-expired-desktop-{light,dark}.png`, `u01-employee/s-f01-27-sessions-and-devices-e-f01-23-user-session-expired-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

The same list on a phone, one card per session with the End button under it.

## Accessibility

Each row says its state in words, not only by colour; ending a session asks for confirmation and announces the result;
keyboard: next row, end.

## Components

- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-14 Timeline](../../../../04-ux/design-system/components/c-14-timeline.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F1-15 Security and group data](../../flows/fl-f01-15-security-and-group-data.md)

## Open questions

None.

---

⬅️ [S-F1-26 Security events dashboard](../09-administration-reports/s-f01-26-security-events-dashboard.md) ·
⬆️ [Up](README.md) · ➡️ [S-F1-28 Retention policies](s-f01-28-retention-policies.md)
