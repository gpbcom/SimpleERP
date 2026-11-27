🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F9-11 Capacity, rounds and partners](README.md) › 🖥️ S-F9-27 Rounds

# 🖥️ S-F9-27 Rounds

**Status:** ✅ specified

## Personas

- [U25 Care coordinator](../../../../01-users/personas/u25-care-coordinator.md)
- [U29 Dispatcher](../../../../01-users/personas/u29-dispatcher.md)
- [U26 Carer](../../../../01-users/personas/u26-carer.md)
- [U30 Driver](../../../../01-users/personas/u30-driver.md)

## Purpose

Optimise and publish rounds on a map, and see one's round on the phone.

## Entry points

Planning › Rounds; My round on the phone.

## Wireframe

```text
+------------------------------------------------------------------+
| Rounds  Mon 2026-12-08   312 visits  14 people  3 unplaced         |
| [map with 14 coloured routes]                                     |
| Lea: 9 visits, 84 min driving    [open]                           |
| Unplaced: Mme Faure 08:00-08:30 (no carer free)   [Place by hand] |
|                             [Optimise again] [Publish]            |
+------------------------------------------------------------------+
Phone: My round  1 Mme Roche 08:15  2 M. Blanc 09:10 ... [Navigate]
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F9-11 step 2, U25 | desktop | ![FL-F9-11 step 2, U25, light](../../images/11-capacity-rounds-and-partners/u25-care-coordinator/2-rounds-desktop-light.png) | ![FL-F9-11 step 2, U25, dark](../../images/11-capacity-rounds-and-partners/u25-care-coordinator/2-rounds-desktop-dark.png) |
| FL-F9-11 step 2, U25 | phone | ![FL-F9-11 step 2, U25, light](../../images/11-capacity-rounds-and-partners/u25-care-coordinator/2-rounds-phone-light.png) | ![FL-F9-11 step 2, U25, dark](../../images/11-capacity-rounds-and-partners/u25-care-coordinator/2-rounds-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f09-27-rounds-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f09-27-rounds-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f09-27-rounds-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f09-27-rounds-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f09-27-rounds-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f09-27-rounds-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f09-27-rounds-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f09-27-rounds-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Rounds, stops, travel, unplaced | E-F9-26 | move stops |

## Actions

| Action | Who | Result |
|---|---|---|
| Optimise | coordinators, dispatchers | Rounds rebuilt |
| Publish | coordinators | Sent to phones |

## States

- Normal: optimise and publish rounds on a map, and see one's round on the phone.
- Empty: nothing to plan for the day: "No visit to place".
- Loading: the map greyed with "Optimising" while routes compute.
- Error: the error message pattern (D122).
- Read-only: published past days; staff see their own round only.
- Offline: The published round works offline on the phone
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); changes made by the coordinator reach the phone at
  its next sync.

Shown entities (VD-15): [E-F9-26 Round](../../data/e-f09-26-round.md),
[E-F9-12 Qualification](../../data/e-f09-12-certification.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F9-26 Round | Draft | Badge "Draft"; a new record starts here; next: Published (UC-F9-30); fields editable within the role | U25 | `u25-care-coordinator/s-f09-27-rounds-e-f09-26-round-draft-{desktop,phone}-{light,dark}.png` |
| E-F9-26 Round | Published | Badge "Published"; next: Changed (UC-F9-30); fields editable within the role | U25 | `u25-care-coordinator/s-f09-27-rounds-e-f09-26-round-published-{desktop,phone}-{light,dark}.png` |
| E-F9-12 Qualification | To verify | Badge "To verify"; a new record starts here; next: Verified or Rejected (UC-F9-33, BR-F9-27); fields editable within the role | U25 | `u25-care-coordinator/s-f09-27-rounds-e-f09-12-certification-to-verify-{desktop,phone}-{light,dark}.png` |
| E-F9-12 Qualification | Verified | Badge "Verified"; a new record starts here; next: Expired (UC-F12-22); fields editable within the role | U25 | `u25-care-coordinator/s-f09-27-rounds-e-f09-12-certification-verified-{desktop,phone}-{light,dark}.png` |
| E-F9-12 Qualification | Rejected | Badge "Rejected"; final: read-only, no next state; the history shows how it got here | U25 | `u25-care-coordinator/s-f09-27-rounds-e-f09-12-certification-rejected-{desktop,phone}-{light,dark}.png` |
| E-F9-12 Qualification | Expired | Badge "Expired"; next: To verify (UC-F9-33); fields editable within the role | U25 | `u25-care-coordinator/s-f09-27-rounds-e-f09-12-certification-expired-{desktop,phone}-{light,dark}.png` |
| E-F9-26 Round | Changed | Badge "Changed"; final: read-only, no next state; the history shows how it got here | U25 | `u25-care-coordinator/s-f09-27-rounds-e-f09-26-round-changed-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Map on desktop; the round on a phone.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-04 Card](../../../../04-ux/design-system/components/c-04-card.md)
- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F9-11 Capacity, rounds and partners](../../flows/fl-f09-11-capacity-rounds-and-partners.md)
- [FL-F9-12 Schedule customer requests](../../flows/fl-f09-12-schedule-customer-requests.md)

## Open questions

None.

---

⬅️ [S-F9-26 Capacity planning](s-f09-26-capacity-planning.md) · ⬆️ [Up](README.md) ·
➡️ [S-F9-28 Customer project view](s-f09-28-customer-project-view.md)
