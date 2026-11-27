🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛡️ [F1 Administration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F1-13 Security and audit](README.md) › 🖥️ S-F1-22 Audit trail

# 🖥️ S-F1-22 Audit trail

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Search the audit trail, export it, and stream it to a SIEM.

## Entry points

Administration › Audit trail; History on any record.

## Wireframe

```text
+------------------------------------------------------------------+
| Audit trail   [Who v] [Action v] [Record type v] [Dates] [search]|
| When              Who         Action   Record          Change    |
| 2026-10-14 10:02  Lea Roux    changed  Price list DUR  10 % > 12 %|
| 2026-10-14 10:03  Lea Roux    changed  Price list DUR  date       |
|                     [Export CSV] [Export JSON] [SIEM settings]   |
| SIEM: siem.acme.fr:6514  on  last delivered 09:12                |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F1-13 step 2, U07 | desktop | ![FL-F1-13 step 2, U07, light](../../images/13-security-and-audit/u07-administrator/2-audit-trail-desktop-light.png) | ![FL-F1-13 step 2, U07, dark](../../images/13-security-and-audit/u07-administrator/2-audit-trail-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f01-22-audit-trail-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f01-22-audit-trail-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f01-22-audit-trail-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f01-22-audit-trail-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f01-22-audit-trail-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f01-22-audit-trail-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f01-22-audit-trail-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f01-22-audit-trail-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| When, who, action, record, before and after | audit events (T3) | no |
| SIEM destination | E-F1-20 | administrator |

## Actions

| Action | Who | Result |
|---|---|---|
| Filter | administrator, owner | Events shown |
| Export | administrator | CSV or JSON with checksums |
| SIEM settings | administrator | Test, turn on or off |

## States

- Normal: the events matching the filters.
- Empty: no event for these filters: Clear the filters.
- Loading: skeleton rows ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md)).
- Error: a broken checksum chain, a failing SIEM (D122).
- Read-only: always: the trail is never changed.
- Offline: Not available offline: an administration screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F1-20 SIEM destination](../../data/e-f01-20-siem-destination.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F1-20 SIEM destination | Off | Badge "Off"; a new record starts here; next: On (UC-F1-22); fields editable within the role | U07, U13 | `u07-administrator/s-f01-22-audit-trail-e-f01-20-siem-destination-off-desktop-{light,dark}.png`, `u13-owner/s-f01-22-audit-trail-e-f01-20-siem-destination-off-{desktop,phone}-{light,dark}.png` |
| E-F1-20 SIEM destination | On | Badge "On"; next: Failing (UC-F1-22); fields editable within the role | U07, U13 | `u07-administrator/s-f01-22-audit-trail-e-f01-20-siem-destination-on-desktop-{light,dark}.png`, `u13-owner/s-f01-22-audit-trail-e-f01-20-siem-destination-on-{desktop,phone}-{light,dark}.png` |
| E-F1-20 SIEM destination | Failing | Badge "Failing"; next: On (UC-F1-22); fields editable within the role | U07, U13 | `u07-administrator/s-f01-22-audit-trail-e-f01-20-siem-destination-failing-desktop-{light,dark}.png`, `u13-owner/s-f01-22-audit-trail-e-f01-20-siem-destination-failing-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop and tablet.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-14 Timeline](../../../../04-ux/design-system/components/c-14-timeline.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F1-13 Security and audit](../../flows/fl-f01-13-security-and-audit.md)

## Open questions

None.

---

⬅️ [S-F1-21 Security policies](s-f01-21-security-policies.md) · ⬆️ [Up](README.md) ·
➡️ [S-F1-23 Close the company](../14-close-a-company/s-f01-23-close-the-company.md)
