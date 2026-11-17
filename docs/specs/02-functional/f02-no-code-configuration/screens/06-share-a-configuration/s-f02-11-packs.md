🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔧 [F2 No-code configuration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F2-06 Share a configuration](README.md) › 🖥️ S-F2-11 Packs

# 🖥️ S-F2-11 Packs

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- Users with the Configurator role

## Purpose

Export, import and publish configuration packs.

## Entry points

Configuration › Packs.

## Wireframe

```text
+------------------------------------------------------------------+
| Packs                               [Import a pack] [Export]     |
|------------------------------------------------------------------|
| Export: [x] Record types and fields  [x] Templates               |
|         [x] Automations (inactive on import)  [x] Roles          |
|         Never included: records, users, secrets                  |
|                                 [Download] [Publish to store]    |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F2-06 step 1, U07 | desktop | ![FL-F2-06 step 1, U07, light](../../images/06-share-a-configuration/u07-administrator/1-export-a-pack-desktop-light.png) | ![FL-F2-06 step 1, U07, dark](../../images/06-share-a-configuration/u07-administrator/1-export-a-pack-desktop-dark.png) |
| Error E1, U07 | desktop | ![Error E1, U07, light](../../images/06-share-a-configuration/u07-administrator/e1-pack-from-newer-version-desktop-light.png) | ![Error E1, U07, dark](../../images/06-share-a-configuration/u07-administrator/e1-pack-from-newer-version-desktop-dark.png) |
| Error E2, U07 | desktop | ![Error E2, U07, light](../../images/06-share-a-configuration/u07-administrator/e2-pack-needs-a-plugin-desktop-light.png) | ![Error E2, U07, dark](../../images/06-share-a-configuration/u07-administrator/e2-pack-needs-a-plugin-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f02-11-packs-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f02-11-packs-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f02-11-packs-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f02-11-packs-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f02-11-packs-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f02-11-packs-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f02-11-packs-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f02-11-packs-offline-desktop-dark.png) |

## Fields and columns

As [E-F2-11 Configuration pack](../../data/e-f02-11-configuration-pack.md#fields).

## Actions

| Action | Who | Result |
|---|---|---|
| Export | configurator | A pack file |
| Publish to store | administrator | A sector pack in F14 |
| Import | administrator | A draft |

## States

- Normal: Export, import and publish configuration packs, as the wireframe shows.
- Empty: No pack exported or imported yet, with Export and Import.
- Loading: placeholders in the layout of the wireframe; actions are disabled until the record has loaded.
- Error: a newer version, a missing plugin.
- Read-only: packs installed from the plugin store.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.
- Import preview: what is added and changed.

Shown entities (VD-15): [E-F2-11 Configuration pack](../../data/e-f02-11-configuration-pack.md),
[E-F2-26 Configuration draft](../../data/e-f02-26-configuration-draft.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F2-11 Configuration pack | Published | Badge "Published"; a new record starts here; no other state; fields editable within the role | U07 | `u07-administrator/s-f02-11-packs-e-f02-11-configuration-pack-published-desktop-{light,dark}.png` |
| E-F2-26 Configuration draft | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07 | `u07-administrator/s-f02-11-packs-e-f02-26-configuration-draft-active-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Each part is a labelled checkbox.

## Components

- [C-12 File upload](../../../../04-ux/design-system/components/c-12-file-upload.md)

## Shown in

- [FL-F2-06 Share a configuration](../../flows/fl-f02-06-share-a-configuration.md)

## Open questions

None.

---

⬅️ [S-F2-10 Publish and versions](../05-publish-and-roll-back/s-f02-10-publish-and-versions.md) · ⬆️ [Up](README.md) ·
➡️ [S-F2-12 Spreadsheet](../07-benchmark-additions/s-f02-12-spreadsheet.md)
