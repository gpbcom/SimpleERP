🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
🏷️ Warehouse operator: app shell and home

# 🏷️ Warehouse operator: app shell and home

**Status:** ✅ specified

## App shell

The app shell of [D47](../../../06-decisions/ux/d47-app-shell.md): left sidebar and top bar on a desktop, bottom tabs on
a phone. Default density: compact ([D42](../../../06-decisions/ux/d42-density-per-role.md)).

## Home screen

My tasks first, then the role's widgets, customisable ([D48](../../../06-decisions/ux/d48-home-screen.md)).

- My tasks: Receipts today; Picking lists.
- Widgets: Stock counts due.

```text
+--------------------------------------------------------------+
| Good morning                                [customise]      |
| My tasks                                                     |
|  [ ] Receipts today                                          |
|  [ ] Picking lists                                           |
|                                                              |
| Stock counts due                                             |
+--------------------------------------------------------------+
```

**Example images** (the app shell and home screen, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| Home | phone | ![Home, light](mockups/home-phone-light.png) | ![Home, dark](mockups/home-phone-dark.png) |
| Home | tablet | ![Home, light](mockups/home-tablet-light.png) | ![Home, dark](mockups/home-tablet-dark.png) |

## Navigation

Home · Receipts · Picking · Counts.

## Contents

| | ID | Page | Status |
|---|---|---|---|
| 🧰 |  | [Workspace](workspace.md) | ✅ |
| 🖼️ |  | [Mockups](mockups/README.md) | ✅ |
| 🧭 |  | [Journeys](journeys/README.md) | ✅ |
| 🧭 | J-U15-01 | [Receive and ship](journeys/j-u15-01-receive-and-ship.md) | ✅ |

---

⬅️ [Field worker: app shell and home](../u14-field-worker/README.md) · ⬆️ [Up](../README.md) ·
➡️ [Office worker: app shell and home](../u16-office-worker/README.md)
