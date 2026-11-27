🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔧 [F2 No-code configuration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F2-08 Views and bookings](README.md) › 🖥️ S-F2-17 View designer

# 🖥️ S-F2-17 View designer

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U02 Manager](../../../../01-users/personas/u02-manager.md)

## Purpose

Add and arrange a kanban, calendar, map, Gantt or timeline view of a record type.

## Entry points

A record type › Views › Add a view.

## Wireframe

```text
+------------------------------------------------------------------+
| Works › Add a view    (o) Gantt ( ) Kanban ( ) Calendar ( ) Map  |
| Start [start date v]  End [end date v]  Colour [site v]          |
|------------------------------------------------------------------|
| Preview        Nov 30   Dec 7    Dec 14                          |
| Works 1042     [=========]                                       |
| Works 1043              [===============]                        |
| Share with [Site manager x]           [Save draft] [Publish]     |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F2-08 step 1, U07 | desktop | ![FL-F2-08 step 1, U07, light](../../images/08-views-and-bookings/u07-administrator/1-view-designer-desktop-light.png) | ![FL-F2-08 step 1, U07, dark](../../images/08-views-and-bookings/u07-administrator/1-view-designer-desktop-dark.png) |
| Error E1, U07 | desktop | ![Error E1, U07, light](../../images/08-views-and-bookings/u07-administrator/e1-view-designer-refused-desktop-light.png) | ![Error E1, U07, dark](../../images/08-views-and-bookings/u07-administrator/e1-view-designer-refused-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f02-17-view-designer-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f02-17-view-designer-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f02-17-view-designer-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f02-17-view-designer-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f02-17-view-designer-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f02-17-view-designer-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f02-17-view-designer-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f02-17-view-designer-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Type, fields used, card fields, shared with | E-F2-16 | yes |

## Actions

| Action | Who | Result |
|---|---|---|
| Preview | configurator | Real records shown |
| Publish | configurator | View in the switcher |

## States

- Normal: add and arrange a kanban, calendar, map, Gantt or timeline view of a record type.
- Empty: no field fits: the view types the record type cannot have are greyed with the reason.
- Loading: placeholders in the preview while records load.
- Error: the error message pattern (D122).
- Read-only: views shared with the user, which only the configurator changes.
- Offline: Not available offline: a configuration screen on live, shared settings
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F2-16 Visual view](../../data/e-f02-16-visual-view.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F2-16 Visual view | Draft | Badge "Draft"; a new record starts here; next: Published (UC-F2-17); fields editable within the role | U07 | `u07-administrator/s-f02-17-view-designer-e-f02-16-visual-view-draft-desktop-{light,dark}.png` |
| E-F2-16 Visual view | Published | Badge "Published"; next: Archived (UC-F2-17); fields editable within the role | U07 | `u07-administrator/s-f02-17-view-designer-e-f02-16-visual-view-published-desktop-{light,dark}.png` |
| E-F2-16 Visual view | Archived | Badge "Archived"; final: read-only, no next state; the history shows how it got here | U07 | `u07-administrator/s-f02-17-view-designer-e-f02-16-visual-view-archived-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Every status is a word, not only a colour; drag and drop has a keyboard equivalent; fields have labels.

## Components

- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-07 Tabs](../../../../04-ux/design-system/components/c-07-tabs.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F2-08 Views and bookings](../../flows/fl-f02-08-views-and-bookings.md)

## Open questions

None.

---

⬅️ [S-F2-16 Sandbox](../07-benchmark-additions/s-f02-16-sandbox.md) · ⬆️ [Up](README.md) ·
➡️ [S-F2-18 Booking settings](s-f02-18-booking-settings.md)
