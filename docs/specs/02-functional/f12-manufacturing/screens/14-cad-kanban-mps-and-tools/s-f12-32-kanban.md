🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F12-14](README.md) ›
🖥️ S-F12-32 Kanban

# 🖥️ S-F12-32 Kanban

**Status:** ✅ specified

## Personas

- [U20 Production operator](../../../../01-users/personas/u20-production-operator.md): scans the cards of their station,
  on a tablet.
- [U21 Production planner](../../../../01-users/personas/u21-production-planner.md): sizes and follows the cards, on a
  desktop.

## Purpose

Scan empty containers and follow the replenishment of each card.

## Entry points

The shop-floor tablet › Kanban; Manufacturing › Kanban.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Kanban                         Line 2                                      [Scan a card] [New card] |
| ------------------------------------------------------------------------------------------- |
| CARD   ITEM        LOCATION        SIZE   SOURCE             WAITING   STATE                |
| 12     Screw M4    Line 2, bin 3   2000   Purchase request   2 h       Replenishing         |
| 13     Bracket     Line 2, bin 1   200    Production order   -         Full                 |
| 14     Gasket      Line 2, bin 4   500    Transfer           4 h       Replenishing   Late  |
| Cards: 24   Empty or replenishing: 3   Waiting too long: 1                                  |
+---------------------------------------------------------------------------------------------+
```

Example images of the empty, loading, read-only and offline states, drawn in the image round
([D120](../../../../06-decisions/ux/d120-png-mockups.md)): `s-f12-32-kanban-empty-desktop-{light,dark}.png`,
`s-f12-32-kanban-empty-tablet-{light,dark}.png`, `s-f12-32-kanban-loading-desktop-{light,dark}.png`,
`s-f12-32-kanban-loading-tablet-{light,dark}.png`, `s-f12-32-kanban-offline-desktop-{light,dark}.png`,
`s-f12-32-kanban-offline-tablet-{light,dark}.png`, `s-f12-32-kanban-read-only-desktop-{light,dark}.png`,
`s-f12-32-kanban-read-only-tablet-{light,dark}.png`.

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F12-14 step 2, U20 | tablet | ![FL-F12-14 step 2, U20, light](../../images/14-cad-kanban-mps-and-tools/u20-production-operator/2-kanban-tablet-light.png) | ![FL-F12-14 step 2, U20, dark](../../images/14-cad-kanban-mps-and-tools/u20-production-operator/2-kanban-tablet-dark.png) |
| FL-F12-14 step 2, U20 | tablet | ![FL-F12-14 step 2, U20, light](../../images/14-cad-kanban-mps-and-tools/u20-production-operator/2-kanban-tablet-light.png) | ![FL-F12-14 step 2, U20, dark](../../images/14-cad-kanban-mps-and-tools/u20-production-operator/2-kanban-tablet-dark.png) |
| Empty | tablet | ![Empty, light](../../images/states/s-f12-32-kanban-empty-tablet-light.png) | ![Empty, dark](../../images/states/s-f12-32-kanban-empty-tablet-dark.png) |
| Loading | tablet | ![Loading, light](../../images/states/s-f12-32-kanban-loading-tablet-light.png) | ![Loading, dark](../../images/states/s-f12-32-kanban-loading-tablet-dark.png) |
| Read-only | tablet | ![Read-only, light](../../images/states/s-f12-32-kanban-read-only-tablet-light.png) | ![Read-only, dark](../../images/states/s-f12-32-kanban-read-only-tablet-dark.png) |
| Offline | tablet | ![Offline, light](../../images/states/s-f12-32-kanban-offline-tablet-light.png) | ![Offline, dark](../../images/states/s-f12-32-kanban-offline-tablet-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Card and item | E-F12-31 number, item | text | new card | yes |
| Location and size | E-F12-31 location, container size | text and number | planner | yes |
| Source | E-F12-31 source | choice | planner | yes |
| Waiting | E-F12-31 emptied at | duration | no | no |
| State | E-F12-31 state | badge | by scan | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Scan | screen | an operator | an empty card creates one replenishment (UC-F12-33) |
| Confirm receipt | screen | an operator | the card is Full |
| New card | header | the planner | a card is set up |
| Suspend, Resume | row | the planner | the card is suspended or back in use |
| Retire | row | the planner | the card is withdrawn |

## States

- Normal: the cards of the station with item, location, source, waiting time and state.
- Empty: No card at this station: a hint to create the first card.
- Loading: The cards as placeholders, then the waiting times.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a scan that
  matches no card says so.
- Read-only: a retired card: shown, with no action.
- Offline: Scans are kept on the tablet and sent in order when the network is back
  ([BR-F12-21](../../business-rules/br-f12-21-tablet-records-sync-in-order.md)); the planner's view is not available
  offline.

Shown entities (VD-15): [E-F12-31 Kanban card](../../data/e-f12-31-kanban-card.md),
[E-F7-06 Item](../../../f07-purchasing-and-stock/data/e-f07-06-item.md),
[E-F7-09 Reordering rule](../../../f07-purchasing-and-stock/data/e-f07-09-reordering-rule.md),
[E-F12-04 Manufacturing order](../../data/e-f12-04-manufacturing-order.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F12-31 Kanban card | Full | Badge "Full"; a new record starts here; next: Empty or Suspended or Retired (BR-F12-28, UC-F12-33); fields editable within the role | U20, U21 | `u20-production-operator/s-f12-32-kanban-e-f12-31-kanban-card-full-tablet-{light,dark}.png`; `u21-production-planner/s-f12-32-kanban-e-f12-31-kanban-card-full-{desktop,phone}-{light,dark}.png` |
| E-F12-31 Kanban card | Empty | Badge "Empty"; next: Replenishing (BR-F12-28); fields editable within the role | U20, U21 | `u20-production-operator/s-f12-32-kanban-e-f12-31-kanban-card-empty-tablet-{light,dark}.png`; `u21-production-planner/s-f12-32-kanban-e-f12-31-kanban-card-empty-{desktop,phone}-{light,dark}.png` |
| E-F12-31 Kanban card | Replenishing | Badge "Replenishing"; next: Full (UC-F12-33); fields editable within the role | U20, U21 | `u20-production-operator/s-f12-32-kanban-e-f12-31-kanban-card-replenishing-tablet-{light,dark}.png`; `u21-production-planner/s-f12-32-kanban-e-f12-31-kanban-card-replenishing-{desktop,phone}-{light,dark}.png` |
| E-F12-31 Kanban card | Suspended | Badge "Suspended"; next: Full or Retired (UC-F12-33); fields editable within the role | U20, U21 | `u20-production-operator/s-f12-32-kanban-e-f12-31-kanban-card-suspended-tablet-{light,dark}.png`; `u21-production-planner/s-f12-32-kanban-e-f12-31-kanban-card-suspended-{desktop,phone}-{light,dark}.png` |
| E-F12-31 Kanban card | Retired | Badge "Retired"; final state, read-only | U20, U21 | `u20-production-operator/s-f12-32-kanban-e-f12-31-kanban-card-retired-tablet-{light,dark}.png`; `u21-production-planner/s-f12-32-kanban-e-f12-31-kanban-card-retired-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per persona, device and theme; the
image round draws them. Rows are derived from each entity's Lifecycle: the badge is the state's name, the next states
are its transitions, and a final state is read-only.

## Responsive behaviour

On a tablet, large scan and confirm buttons with the card list below; the planner's view is a desktop table.

## Accessibility

States are words and sounds; the scan result is read aloud; touch targets are at least 44 pixels.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-14 Timeline](../../../../04-ux/design-system/components/c-14-timeline.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F12-14 CAD, kanban, MPS and tools](../../flows/fl-f12-14-cad-kanban-mps-and-tools.md)

## Open questions

None.

---

⬅️ [S-F12-31 CAD link](s-f12-31-cad-link.md) · ⬆️ [Up](README.md) · ➡️ [S-F12-33 MPS](s-f12-33-mps.md)
