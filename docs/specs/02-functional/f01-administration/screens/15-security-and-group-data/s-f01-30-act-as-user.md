🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛡️ [F1 Administration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F1-15 Security and group data](README.md) › 🖥️ S-F1-30 Act as a user

# 🖥️ S-F1-30 Act as a user

**Status:** ✅ specified

## Personas

- - [U07 Administrator](../../../../01-users/personas/u07-administrator.md): asks and acts.
- - [U01 Employee](../../../../01-users/personas/u01-employee.md): grants or refuses and stops the session.

## Purpose

Ask a user for the right to act as them for a short time, and see the request and the session.

## Entry points

Administration › Users › a user › Act as this user; the notification of a request.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Act as a user                                           Banner: Acting as Sonia M., ends 10:30 |
| ------------------------------------------------------------------------------------------- |
| User         Sonia M., accounts                    Reason   cannot post an expense, ticket 2031 |
| Duration     30 minutes                            State    Granted at 10:00                |
| WHAT WAS DONE                                                                [Stop session] |
| 10:04  Opened expense report 118      10:07  Posted expense 118 (as Sonia M., by the administrator) |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F1-15 step 4, U07 | desktop | ![FL-F1-15 step 4, U07, light](../../images/15-security-and-group-data/u07-administrator/4-act-as-user-desktop-light.png) | ![FL-F1-15 step 4, U07, dark](../../images/15-security-and-group-data/u07-administrator/4-act-as-user-desktop-dark.png) |
| FL-F1-15 step 4, U07 | desktop | ![FL-F1-15 step 4, U07, light](../../images/15-security-and-group-data/u07-administrator/4-act-as-user-desktop-light.png) | ![FL-F1-15 step 4, U07, dark](../../images/15-security-and-group-data/u07-administrator/4-act-as-user-desktop-dark.png) |
| Error E1, U07 | desktop | ![Error E1, U07, light](../../images/15-security-and-group-data/u07-administrator/e1-the-user-refuses-to-be-acted-as-desktop-light.png) | ![Error E1, U07, dark](../../images/15-security-and-group-data/u07-administrator/e1-the-user-refuses-to-be-acted-as-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f01-30-act-as-user-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f01-30-act-as-user-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f01-30-act-as-user-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f01-30-act-as-user-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f01-30-act-as-user-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f01-30-act-as-user-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f01-30-act-as-user-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f01-30-act-as-user-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| User | E-F1-26 target user | name | yes | yes |
| Reason | E-F1-26 reason | text | yes | yes |
| Duration | E-F1-26 duration | minutes, at most 60 | yes | yes |
| State | E-F1-26 state | badge | no | yes |
| What was done | E-T03-01 audit entries of the session | list | no | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Ask | header | the administrator | the user receives the request |
| Grant, Refuse | request (phone) | the user | the session opens or the request closes |
| Stop session | banner | the administrator, the user | the session ends at once |
| Flag an action | what was done | the user | the owner is told |

## States

- Normal: the request, the state, the banner and the actions done so far.
- Empty: No request: choose a user and give a reason.
- Loading: The request is sent first; the state follows.
- Error: the error message pattern (D122); a refused request shows Refused by the user and when.
- Read-only: an ended session: the reason, the times and every action done, without actions.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F1-26 Act-as session](../../data/e-f01-26-act-as-session.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F1-26 Act-as session | Requested | Badge "Requested"; a new record starts here; next: Granted, Refused or Expired (BR-F1-36, UC-F1-27); fields editable within the role | U07, U01 | `u07-administrator/s-f01-30-act-as-user-e-f01-26-act-as-session-requested-desktop-{light,dark}.png`, `u01-employee/s-f01-30-act-as-user-e-f01-26-act-as-session-requested-{desktop,phone}-{light,dark}.png` |
| E-F1-26 Act-as session | Granted | Badge "Granted"; next: Active (UC-F1-27); fields editable within the role | U07, U01 | `u07-administrator/s-f01-30-act-as-user-e-f01-26-act-as-session-granted-desktop-{light,dark}.png`, `u01-employee/s-f01-30-act-as-user-e-f01-26-act-as-session-granted-{desktop,phone}-{light,dark}.png` |
| E-F1-26 Act-as session | Refused | Badge "Refused"; final: read-only, no next state; the history shows how it got here | U07, U01 | `u07-administrator/s-f01-30-act-as-user-e-f01-26-act-as-session-refused-desktop-{light,dark}.png`, `u01-employee/s-f01-30-act-as-user-e-f01-26-act-as-session-refused-{desktop,phone}-{light,dark}.png` |
| E-F1-26 Act-as session | Expired | Badge "Expired"; final: read-only, no next state; the history shows how it got here | U07, U01 | `u07-administrator/s-f01-30-act-as-user-e-f01-26-act-as-session-expired-desktop-{light,dark}.png`, `u01-employee/s-f01-30-act-as-user-e-f01-26-act-as-session-expired-{desktop,phone}-{light,dark}.png` |
| E-F1-26 Act-as session | Active | Badge "Active"; next: Ended (UC-F1-27); fields editable within the role | U07, U01 | `u07-administrator/s-f01-30-act-as-user-e-f01-26-act-as-session-active-desktop-{light,dark}.png`, `u01-employee/s-f01-30-act-as-user-e-f01-26-act-as-session-active-{desktop,phone}-{light,dark}.png` |
| E-F1-26 Act-as session | Ended | Badge "Ended"; final: read-only, no next state; the history shows how it got here | U07, U01 | `u07-administrator/s-f01-30-act-as-user-e-f01-26-act-as-session-ended-desktop-{light,dark}.png`, `u01-employee/s-f01-30-act-as-user-e-f01-26-act-as-session-ended-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

The request and the grant screen are made for a phone; the administrator's side is desktop.

## Accessibility

The banner is text with the end time and is announced when it appears; the Grant and Refuse buttons are large and
labelled; keyboard: grant, refuse.

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

⬅️ [S-F1-29 Group sharing](s-f01-29-group-sharing.md) · ⬆️ [Up](README.md) ·
➡️ [S-F1-L01 Companies](../00-lists/s-f01-l01-companies.md)
