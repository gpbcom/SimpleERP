🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛡️ [F1 Administration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F1-10 Bring users in at scale](README.md) › 🖥️ S-F1-13 Automatic provisioning

# 🖥️ S-F1-13 Automatic provisioning

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U11 IT provider administrator](../../../../01-users/personas/u11-provider-admin.md)

## Purpose

Connect the identity provider's provisioning (SCIM) and map its groups to roles and sites.

## Entry points

Administration › Single sign-on › Automatic provisioning.

## Wireframe

```text
+------------------------------------------------------------------+
| Automatic provisioning                        Status: On  [Off]  |
| Endpoint  https://acme.simpleerp.eu/scim/v2       [Copy]        |
| Token     ****7f3a                    [New token] [Revoke]       |
|------------------------------------------------------------------|
| Provider group   Roles             Site          Users           |
| Sales            Sales             Lyon yard     12              |
| Finance          Accounting        Head office   4               |
| (no mapping)     default role      -             2  [Complete]   |
|                                         [Test]  [Save]           |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F1-10 step 1, U07 | desktop | ![FL-F1-10 step 1, U07, light](../../images/10-bring-users-in-at-scale/u07-administrator/1-automatic-provisioning-desktop-light.png) | ![FL-F1-10 step 1, U07, dark](../../images/10-bring-users-in-at-scale/u07-administrator/1-automatic-provisioning-desktop-dark.png) |
| Error E1, U07 | desktop | ![Error E1, U07, light](../../images/10-bring-users-in-at-scale/u07-administrator/e1-automatic-provisioning-refused-desktop-light.png) | ![Error E1, U07, dark](../../images/10-bring-users-in-at-scale/u07-administrator/e1-automatic-provisioning-refused-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f01-13-automatic-provisioning-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f01-13-automatic-provisioning-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f01-13-automatic-provisioning-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f01-13-automatic-provisioning-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f01-13-automatic-provisioning-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f01-13-automatic-provisioning-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f01-13-automatic-provisioning-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f01-13-automatic-provisioning-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Status | E-F1-14 status | through Test and On |
| Token | E-F1-14 token | new or revoke |
| Group mappings | E-F1-14 group mappings | yes |

## Actions

| Action | Who | Result |
|---|---|---|
| Test | administrator | Reads one user and shows what would be created |
| Turn on or off | administrator | Provisioning starts or stops |
| New token | administrator | Shown once; the old one stops |

## States

- Normal: status, endpoint, mappings and the last sync.
- Empty: Off, with no mapping: "Connect single sign-on first" when it is off.
- Loading: skeleton rows in the mappings table ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md))
  while the provider's groups load.
- Error: the provider's error after a failed test (D122).
- Read-only: for the IT provider's client administrators when the provider manages it.
- Offline: Not available offline: an administration screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F1-14 Provisioning setting](../../data/e-f01-14-provisioning-setting.md),
[E-F1-03 User](../../data/e-f01-03-user.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F1-14 Provisioning setting | Off | Badge "Off"; a new record starts here; next: Tested (UC-F1-13); fields editable within the role | U07 | `u07-administrator/s-f01-13-automatic-provisioning-e-f01-14-provisioning-setting-off-desktop-{light,dark}.png` |
| E-F1-14 Provisioning setting | Tested | Badge "Tested"; next: On (UC-F1-13); fields editable within the role | U07 | `u07-administrator/s-f01-13-automatic-provisioning-e-f01-14-provisioning-setting-tested-desktop-{light,dark}.png` |
| E-F1-14 Provisioning setting | On | Badge "On"; next: Off (UC-F1-13); fields editable within the role | U07 | `u07-administrator/s-f01-13-automatic-provisioning-e-f01-14-provisioning-setting-on-desktop-{light,dark}.png` |
| E-F1-03 User | Active | Badge "Active"; next: Deactivated (UC-F1-05); fields editable within the role | U07 | `u07-administrator/s-f01-13-automatic-provisioning-e-f01-03-user-active-desktop-{light,dark}.png` |

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
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F1-10 Bring users in at scale](../../flows/fl-f01-10-bring-users-in-at-scale.md)

## Open questions

None.

---

⬅️ [S-F1-12 Users overview dashboard](../09-administration-reports/s-f01-12-users-overview-dashboard.md) ·
⬆️ [Up](README.md) · ➡️ [S-F1-14 Bulk invite](s-f01-14-bulk-invite.md)
