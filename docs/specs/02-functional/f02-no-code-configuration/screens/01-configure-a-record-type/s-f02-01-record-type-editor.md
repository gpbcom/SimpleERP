🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔧 [F2 No-code configuration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F2-01 Configure a record type](README.md) › 🖥️ S-F2-01 Record type editor

# 🖥️ S-F2-01 Record type editor

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- Users with the Configurator role (D96): [U02 Manager](../../../../01-users/personas/u02-manager.md),
  [U16 Office worker](../../../../01-users/personas/u16-office-worker.md),
  [U13 Owner](../../../../01-users/personas/u13-owner.md),
  [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md)

## Purpose

Change a record type's fields, statuses and form, as a draft.

## Entry points

Configuration › Record types › a record type; "Customise this form" on any form, for configurators.

## Wireframe

```text
+------------------------------------------------------------------+
| Quotes            DRAFT (not live)     [Preview] [Publish]       |
| [Fields] [Statuses] [Form] [History]                              |
|------------------------------------------------------------------|
| Field            Type              Required  Visible to   Source  |
| Customer         link: Customers   yes       all          core    |
| Amount           money             yes       all          core    |
| Vehicle          link: Vehicles    no        Sales (see)  custom  |
| Margin           computed          -         Accounting   custom  |
| Site manager     link: Users       no        all     archived    |
|                                     [+ Add field] [Ask AI]       |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F2-01 step 1, U07 | desktop | ![FL-F2-01 step 1, U07, light](../../images/01-configure-a-record-type/u07-administrator/1-add-a-custom-field-desktop-light.png) | ![FL-F2-01 step 1, U07, dark](../../images/01-configure-a-record-type/u07-administrator/1-add-a-custom-field-desktop-dark.png) |
| Error E1, U07 | desktop | ![Error E1, U07, light](../../images/01-configure-a-record-type/u07-administrator/e1-duplicate-field-name-desktop-light.png) | ![Error E1, U07, dark](../../images/01-configure-a-record-type/u07-administrator/e1-duplicate-field-name-desktop-dark.png) |
| Error E2, U07 | desktop | ![Error E2, U07, light](../../images/01-configure-a-record-type/u07-administrator/e2-formula-loops-desktop-light.png) | ![Error E2, U07, dark](../../images/01-configure-a-record-type/u07-administrator/e2-formula-loops-desktop-dark.png) |
| Error E3, U07 | desktop | ![Error E3, U07, light](../../images/01-configure-a-record-type/u07-administrator/e3-field-holds-data-desktop-light.png) | ![Error E3, U07, dark](../../images/01-configure-a-record-type/u07-administrator/e3-field-holds-data-desktop-dark.png) |
| Error E4, U07 | desktop | ![Error E4, U07, light](../../images/01-configure-a-record-type/u07-administrator/e4-core-status-locked-desktop-light.png) | ![Error E4, U07, dark](../../images/01-configure-a-record-type/u07-administrator/e4-core-status-locked-desktop-dark.png) |
| Error E5, U07 | desktop | ![Error E5, U07, light](../../images/01-configure-a-record-type/u07-administrator/e5-status-in-use-desktop-light.png) | ![Error E5, U07, dark](../../images/01-configure-a-record-type/u07-administrator/e5-status-in-use-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f02-01-record-type-editor-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f02-01-record-type-editor-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f02-01-record-type-editor-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f02-01-record-type-editor-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f02-01-record-type-editor-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f02-01-record-type-editor-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f02-01-record-type-editor-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f02-01-record-type-editor-offline-desktop-dark.png) |

## Fields and columns

As [E-F2-01 Custom field](../../data/e-f02-01-custom-field.md#fields).

## Actions

| Action | Who | Result |
|---|---|---|
| Add field | configurator | Field form |
| Archive, restore | configurator | BR-F2-01 |
| Preview | configurator | Real records with the draft |
| Publish | configurator | New version (UC-F2-09) |
| Ask AI | configurator | Suggested fields or formula, as draft |

## States

- Normal: Change a record type's fields, statuses and form, as a draft, as the wireframe shows.
- Empty: a new record type with no field but its name, with Add field.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: duplicate name, broken formula.
- Read-only: core fields' type and name.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.
- Draft: banner "not live".

Shown entities (VD-15): [E-F2-05 Record type](../../data/e-f02-05-record-type.md),
[E-F2-01 Custom field](../../data/e-f02-01-custom-field.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F2-05 Record type | Draft | Badge "Draft"; a new record starts here; next: Live (UC-F2-04); fields editable within the role | U02, U07 | `u02-manager/s-f02-01-record-type-editor-e-f02-05-record-type-draft-{desktop,phone}-{light,dark}.png`, `u07-administrator/s-f02-01-record-type-editor-e-f02-05-record-type-draft-desktop-{light,dark}.png` |
| E-F2-05 Record type | Live | Badge "Live"; next: Archived (UC-F2-04); fields editable within the role | U02, U07 | `u02-manager/s-f02-01-record-type-editor-e-f02-05-record-type-live-{desktop,phone}-{light,dark}.png`, `u07-administrator/s-f02-01-record-type-editor-e-f02-05-record-type-live-desktop-{light,dark}.png` |
| E-F2-05 Record type | Archived | Badge "Archived"; next: Live (UC-F2-04); fields editable within the role | U02, U07 | `u02-manager/s-f02-01-record-type-editor-e-f02-05-record-type-archived-{desktop,phone}-{light,dark}.png`, `u07-administrator/s-f02-01-record-type-editor-e-f02-05-record-type-archived-desktop-{light,dark}.png` |
| E-F2-01 Custom field | Draft | Badge "Draft"; a new record starts here; next: Live (UC-F2-01); fields editable within the role | U07 | `u07-administrator/s-f02-01-record-type-editor-e-f02-01-custom-field-draft-desktop-{light,dark}.png` |
| E-F2-01 Custom field | Live | Badge "Live"; next: Archived (UC-F2-01); fields editable within the role | U07 | `u07-administrator/s-f02-01-record-type-editor-e-f02-01-custom-field-live-desktop-{light,dark}.png` |
| E-F2-01 Custom field | Archived | Badge "Archived"; next: Live (UC-F2-01); fields editable within the role | U07 | `u07-administrator/s-f02-01-record-type-editor-e-f02-01-custom-field-archived-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

The fields list is a table; reordering also works with the keyboard.

## Components

- [C-07 Tabs](../../../../04-ux/design-system/components/c-07-tabs.md)
- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-F2-01 Configure a record type](../../flows/fl-f02-01-configure-a-record-type.md)

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [S-F2-02 Status designer](s-f02-02-status-designer.md)
