🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💇 [SC17 Beauty and wellness](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC17-04 Commissions and tips](README.md) › 🖥️ S-SC17-15 Staff targets

# 🖥️ S-SC17-15 Staff targets

**Status:** 🔄 waiting for the owner

## Personas

- [U23 Store manager](../../../../01-users/personas/u23-store-manager.md): the targets of every staff member.
- [U52 Beautician](../../../../01-users/personas/u52-beautician.md): their own targets only.

## Purpose

Follow each staff member's targets and progress during the month.

## Entry points

Beauty and wellness › Staff targets; the home screen; the AI assistant.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Targets: November                                                      9 days left               |
| Staff        Services   Products   Rebooking    Status                                           |
| Ines B.      3,200/5,000  420/600    68/70 %     On track                                        |
| Louis T.     1,900/4,500  150/500    52/70 %     At risk                                         |
| Sana M.      4,100/4,500  610/500    71/70 %     Reached                                         |
| [Set targets]  [Adjust with a reason]                                                            |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC17-04 step 3, U23 | desktop | ![FL-SC17-04 step 3, U23, light](../../images/04-commissions-and-tips/u23-store-manager/3-staff-targets-desktop-light.png) | ![FL-SC17-04 step 3, U23, dark](../../images/04-commissions-and-tips/u23-store-manager/3-staff-targets-desktop-dark.png) |
| FL-SC17-04 step 3, U23 | phone | ![FL-SC17-04 step 3, U23, light](../../images/04-commissions-and-tips/u23-store-manager/3-staff-targets-phone-light.png) | ![FL-SC17-04 step 3, U23, dark](../../images/04-commissions-and-tips/u23-store-manager/3-staff-targets-phone-dark.png) |
| FL-SC17-04 step 3, U23 | tablet | ![FL-SC17-04 step 3, U23, light](../../images/04-commissions-and-tips/u23-store-manager/3-staff-targets-tablet-light.png) | ![FL-SC17-04 step 3, U23, dark](../../images/04-commissions-and-tips/u23-store-manager/3-staff-targets-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc17-15-staff-targets-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc17-15-staff-targets-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc17-15-staff-targets-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc17-15-staff-targets-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc17-15-staff-targets-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc17-15-staff-targets-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc17-15-staff-targets-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc17-15-staff-targets-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Staff member | E-F6-18 owner | link | no | yes |
| Target | E-F6-18 target | kind and amount | yes while open | yes |
| Progress | E-F6-19 amount | amount | no | no |
| Period | E-F6-18 period | month | no | yes |
| Status | E-F6-18 status | on track, at risk, reached | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Set targets | header | manager | targets are created for the month |
| Adjust | target row | manager | the target changes with a reason |
| Close the month | header | manager | the results are kept and the targets locked |

## States

- Normal: the targets with progress, days left and status.
- Empty: No target set for this month.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a sale with no
  seller or a refused access, with what to do.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

The beautician works on the tablet at the chair, the manager on a desktop and the customer on a phone, with the same
actions in one column.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC17-04 Commissions and tips](../../flows/fl-sc17-04-commissions-and-tips.md)

## Open questions

None.

---

⬅️ [S-SC17-14 Salon tips](s-sc17-14-salon-tips.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC17-16 Salon AI assistant](s-sc17-16-salon-assistant.md)
