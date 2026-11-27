🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F12-14](README.md) ›
🖥️ S-F12-34 Tools and moulds

# 🖥️ S-F12-34 Tools and moulds

**Status:** ✅ specified

## Personas

- [U20 Production operator](../../../../01-users/personas/u20-production-operator.md): mounts the tools and sees their
  counts, on a tablet.
- [U27 Quality manager](../../../../01-users/personas/u27-quality-manager.md): follows life, services and blocked tools,
  on a desktop.

## Purpose

Mount tools, follow their life count and refurbish them before they block production.

## Entry points

The shop-floor tablet › Tools; Manufacturing › Tools and moulds; the warning notification.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Tools and moulds                                                            [Register a tool] |
| ------------------------------------------------------------------------------------------- |
| TOOL   KIND    MOUNTED ON   COUNT / LIMIT        LAST SERVICE   STATE                       |
| M-17   Mould   Press 2       98 200 / 100 000     2026-02-10     In use       98 percent    |
| M-21   Mould   -             100 000 / 100 000    2025-11-04     Blocked      [Refurbish]   |
| D-04   Die     Press 4       12 400 / 50 000      2026-06-18     In use                     |
| Near the limit: 1   Blocked: 1   Services due this month: 2                                 |
+---------------------------------------------------------------------------------------------+
```

Example images of the empty, loading, read-only and offline states, drawn in the image round
([D120](../../../../06-decisions/ux/d120-png-mockups.md)): `s-f12-34-tools-and-moulds-empty-desktop-{light,dark}.png`,
`s-f12-34-tools-and-moulds-empty-tablet-{light,dark}.png`, `s-f12-34-tools-and-moulds-loading-desktop-{light,dark}.png`,
`s-f12-34-tools-and-moulds-loading-tablet-{light,dark}.png`,
`s-f12-34-tools-and-moulds-offline-desktop-{light,dark}.png`,
`s-f12-34-tools-and-moulds-offline-tablet-{light,dark}.png`,
`s-f12-34-tools-and-moulds-read-only-desktop-{light,dark}.png`,
`s-f12-34-tools-and-moulds-read-only-tablet-{light,dark}.png`.

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F12-14 step 4, U20 | tablet | ![FL-F12-14 step 4, U20, light](../../images/14-cad-kanban-mps-and-tools/u20-production-operator/4-tools-and-moulds-tablet-light.png) | ![FL-F12-14 step 4, U20, dark](../../images/14-cad-kanban-mps-and-tools/u20-production-operator/4-tools-and-moulds-tablet-dark.png) |
| FL-F12-14 step 4, U20 | tablet | ![FL-F12-14 step 4, U20, light](../../images/14-cad-kanban-mps-and-tools/u20-production-operator/4-tools-and-moulds-tablet-light.png) | ![FL-F12-14 step 4, U20, dark](../../images/14-cad-kanban-mps-and-tools/u20-production-operator/4-tools-and-moulds-tablet-dark.png) |
| Empty | tablet | ![Empty, light](../../images/states/s-f12-34-tools-and-moulds-empty-tablet-light.png) | ![Empty, dark](../../images/states/s-f12-34-tools-and-moulds-empty-tablet-dark.png) |
| Loading | tablet | ![Loading, light](../../images/states/s-f12-34-tools-and-moulds-loading-tablet-light.png) | ![Loading, dark](../../images/states/s-f12-34-tools-and-moulds-loading-tablet-dark.png) |
| Read-only | tablet | ![Read-only, light](../../images/states/s-f12-34-tools-and-moulds-read-only-tablet-light.png) | ![Read-only, dark](../../images/states/s-f12-34-tools-and-moulds-read-only-tablet-dark.png) |
| Offline | tablet | ![Offline, light](../../images/states/s-f12-34-tools-and-moulds-offline-tablet-light.png) | ![Offline, dark](../../images/states/s-f12-34-tools-and-moulds-offline-tablet-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Tool and kind | E-F12-33 reference, kind | text | new tool | yes |
| Count and limit | E-F12-33 count, life limit | n of m | reset only | yes |
| Mounted on | E-F12-33 mounted on | work centre | by action | no |
| Service | E-F12-33 last refurbished, interval | date | no | no |
| State | E-F12-33 state | badge | by action | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Mount, Unmount | row, tablet | an operator | the tool is in use or available |
| Register | header | the quality manager | an Available tool (UC-F12-35) |
| Refurbish | blocked row | the quality manager | a maintenance request is opened |
| Reset | row | the quality manager | the count returns to 0 with a note |
| Extend, Retire | row | the quality manager | the limit is extended once, or the tool is retired |

## States

- Normal: the tools with kind, work centre, count against limit, last service and state.
- Empty: No tool registered yet: a hint to register the first.
- Loading: The tools as placeholders, then the counts.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); mounting a
  blocked tool says so with the count and the limit.
- Read-only: a retired tool: shown, with no action.
- Offline: The operator can mount a tool and record quantities offline, kept on the tablet and synchronised in order
  ([BR-F12-21](../../business-rules/br-f12-21-tablet-records-sync-in-order.md)); a block is applied when the count
  syncs.

Shown entities (VD-15): [E-F12-33 Tool](../../data/e-f12-33-tool.md),
[E-F12-02 Work centre](../../data/e-f12-02-work-centre.md), [E-F12-05 Work order](../../data/e-f12-05-work-order.md),
[E-F12-10 Maintenance request](../../data/e-f12-10-maintenance-request.md),
[E-F12-13 Machine signal](../../data/e-f12-13-machine-signal.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F12-33 Tool | Available | Badge "Available"; a new record starts here; next: In use or Blocked or In maintenance (UC-F12-35, BR-F12-30); fields editable within the role | U20, U27 | `u20-production-operator/s-f12-34-tools-and-moulds-e-f12-33-tool-available-tablet-{light,dark}.png`; `u27-quality-manager/s-f12-34-tools-and-moulds-e-f12-33-tool-available-{desktop,tablet}-{light,dark}.png` |
| E-F12-33 Tool | In use | Badge "In use"; next: Available or Blocked (UC-F12-35, BR-F12-30); fields editable within the role | U20, U27 | `u20-production-operator/s-f12-34-tools-and-moulds-e-f12-33-tool-in-use-tablet-{light,dark}.png`; `u27-quality-manager/s-f12-34-tools-and-moulds-e-f12-33-tool-in-use-{desktop,tablet}-{light,dark}.png` |
| E-F12-33 Tool | Blocked | Badge "Blocked"; next: In maintenance (UC-F12-35); fields editable within the role | U20, U27 | `u20-production-operator/s-f12-34-tools-and-moulds-e-f12-33-tool-blocked-tablet-{light,dark}.png`; `u27-quality-manager/s-f12-34-tools-and-moulds-e-f12-33-tool-blocked-{desktop,tablet}-{light,dark}.png` |
| E-F12-33 Tool | In maintenance | Badge "In maintenance"; next: Available or Retired (UC-F12-35); fields editable within the role | U20, U27 | `u20-production-operator/s-f12-34-tools-and-moulds-e-f12-33-tool-in-maintenance-tablet-{light,dark}.png`; `u27-quality-manager/s-f12-34-tools-and-moulds-e-f12-33-tool-in-maintenance-{desktop,tablet}-{light,dark}.png` |
| E-F12-33 Tool | Retired | Badge "Retired"; final state, read-only | U20, U27 | `u20-production-operator/s-f12-34-tools-and-moulds-e-f12-33-tool-retired-tablet-{light,dark}.png`; `u27-quality-manager/s-f12-34-tools-and-moulds-e-f12-33-tool-retired-{desktop,tablet}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per persona, device and theme; the
image round draws them. Rows are derived from each entity's Lifecycle: the badge is the state's name, the next states
are its transitions, and a final state is read-only.

## Responsive behaviour

On a tablet, large mount and unmount buttons with the count as a bar; the quality manager's table is desktop.

## Accessibility

The count is a number with its limit in words, not only a bar; keyboard: next tool, mount, refurbish.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-14 Timeline](../../../../04-ux/design-system/components/c-14-timeline.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)
- [C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md)

## Shown in

- [FL-F12-14 CAD, kanban, MPS and tools](../../flows/fl-f12-14-cad-kanban-mps-and-tools.md)

## Open questions

None.

---

⬅️ [S-F12-33 MPS](s-f12-33-mps.md) · ⬆️ [Up](README.md) ·
➡️ [S-F12-L01 Bill of materials](../00-lists/s-f12-l01-bill-of-materials.md)
