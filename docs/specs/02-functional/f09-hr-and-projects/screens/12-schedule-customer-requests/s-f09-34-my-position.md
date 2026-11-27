🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F9-12 Schedule customer requests](README.md) › 🖥️ S-F9-34 My position

# 🖥️ S-F9-34 My position

**Status:** 🔄 draft (GH-2 step S4b, from VD-21 to VD-23 / D503 to D505)

## Personas

- [U26 Carer](../../../../01-users/personas/u26-carer.md) and [U30 Driver](../../../../01-users/personas/u30-driver.md),
  in a team where the live-position option is on: their own position only.

## Purpose

Show the employee when their position is shared, what is recorded, who sees it, and let them pause it.

## Entry points

The live indicator at the top of the phone app, during working hours; My HR › My position history (S-F9-04).

## Wireframe

No map of others: the employee sees what is shared about them. The small map of their own last position follows
[C-17 Map](../../../../04-ux/design-system/components/c-17-map.md) (Proposed).

```text
Phone, top of every screen:  [ (o) Position shared · Pause ]

+--------------------------------------+
| My position                          |
| (o) Shared since 07:58               |
| Until the end of your working hours  |
| (16:00), never after                 |
|                                      |
| What is recorded: your position,     |
| every few minutes (Proposed)         |
| Why: planning the next visit         |
| Who sees it: your coordinator,       |
| your manager; the customer sees an   |
| arrival time only                    |
| Kept: 2 months at most               |
|                                      |
|           [ Pause for my break ]     |
| [My history]                         |
+--------------------------------------+
Paused: "( ) Paused since 12:00 · [Resume]"
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F9-12 step 9, U26 | phone | ![FL-F9-12 step 9, U26, light](../../images/12-schedule-customer-requests/u26-carer/9-my-position-phone-light.png) | ![FL-F9-12 step 9, U26, dark](../../images/12-schedule-customer-requests/u26-carer/9-my-position-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-f09-34-my-position-empty-phone-light.png) | ![Empty, dark](../../images/states/s-f09-34-my-position-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-f09-34-my-position-loading-phone-light.png) | ![Loading, dark](../../images/states/s-f09-34-my-position-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-f09-34-my-position-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-f09-34-my-position-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f09-34-my-position-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f09-34-my-position-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| State | E-F9-32 state | Off, Sharing, Paused | Pause, Resume | yes |
| Since, until | E-F9-32, E-F9-16 Shift | times | no | yes |
| What, why, who, how long | the team option (BR-F9-30, BR-F9-32, BR-F9-31) | text | no | yes |
| History | E-F9-32 by day | days, times shared and paused | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Pause | indicator, screen | the employee | nothing recorded until Resume |
| Resume | screen | the employee | sharing starts again, within working hours |
| My history | screen | the employee | the days and times shared and paused |

## States

- Normal: shared, with what, why, who and how long.
- Empty: the team option is off: "Your position is recorded at check-in and check-out only" (BR-F9-06); no indicator.
- Loading: the indicator shows at once; the details follow.
- Error: the phone's location is off: "Not shared: location is off on this phone"; nobody is told it is a fault.
- Read-only: outside working hours: "Not shared", the history only.
- Offline: positions are kept on the phone and sent when the connection is back; the indicator says so (Proposed).

Shown entities (VD-15): [E-F9-32 Live position](../../data/e-f09-32-live-position.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F9-32 Live position | Sharing | Filled indicator; Pause | U26, U30 | `u26-carer/s-f09-34-my-position-e-f09-32-live-position-sharing-phone-{light,dark}.png`, `u30-driver/s-f09-34-my-position-e-f09-32-live-position-sharing-phone-{light,dark}.png` |
| E-F9-32 Live position | Paused | Hollow indicator, "Paused since"; Resume | U26, U30 | `u26-carer/s-f09-34-my-position-e-f09-32-live-position-paused-phone-{light,dark}.png`, `u30-driver/s-f09-34-my-position-e-f09-32-live-position-paused-phone-{light,dark}.png` |
| E-F9-32 Live position | Off | No indicator; the screen says "Not shared" | U26, U30 | `u26-carer/s-f09-34-my-position-e-f09-32-live-position-off-phone-{light,dark}.png`, `u30-driver/s-f09-34-my-position-e-f09-32-live-position-off-phone-{light,dark}.png` |

The states are those of the entity draft.

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none.

## Responsive behaviour

Phone only; the history is also in My HR on desktop.

## Accessibility

The indicator is a word and an icon, never only a colour; Pause and Resume are large buttons with labels; the state
change is announced.

## Components

- [C-04 Card](../../../../04-ux/design-system/components/c-04-card.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)
- [C-17 Map](../../../../04-ux/design-system/components/c-17-map.md)

## Shown in

- [FL-F9-12 Schedule customer requests](../../flows/fl-f09-12-schedule-customer-requests.md)

## Open questions

None.

---

⬅️ [S-F9-33 Planning map](s-f09-33-planning-map.md) · ⬆️ [Up](README.md) ·
➡️ [S-F9-35 Employee qualifications](../13-keep-qualifications/s-f09-35-employee-qualifications.md)
