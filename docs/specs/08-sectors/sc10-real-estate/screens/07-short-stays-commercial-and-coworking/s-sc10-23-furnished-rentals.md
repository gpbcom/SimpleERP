🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏘️ [SC10 Real estate](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC10-07 Short stays, commercial leases, LMNP and coworking](README.md) ›
🖥️ S-SC10-23 Furnished rentals

# 🖥️ S-SC10-23 Furnished rentals

**Status:** ✅ specified

## Personas

- [U34 Property manager](../../../../01-users/personas/u34-property-manager.md): the tax file of each furnished
  property.
- [U09 Customer](../../../../01-users/personas/u09-customer.md): their own figures of the year.

## Purpose

Record the values of a furnished property, plan its depreciation and see the yearly result with the depreciation
deducted and carried forward.

## Entry points

Real estate › Furnished properties; the landlord's portal; the AI assistant.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Studio Le Port: furnished rental, real regime                        Year 2026   [Close the year |
| Price 140,000  Land 20 %  Building 112,000 over 30 years  Furniture 8,000 over 7 years           |
| Rents 9,600   Charges 6,500   Result before depreciation 3,100                                   |
| Depreciation planned 4,400   Deducted 3,100   Carried forward 1,300                              |
| Carried forward from earlier years 0                                                             |
| Taxable result 0.00     [Export for the return]                                                  |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC10-07 step 3, U34 | desktop | ![FL-SC10-07 step 3, U34, light](../../images/07-short-stays-commercial-and-coworking/u34-property-manager/3-furnished-rentals-desktop-light.png) | ![FL-SC10-07 step 3, U34, dark](../../images/07-short-stays-commercial-and-coworking/u34-property-manager/3-furnished-rentals-desktop-dark.png) |
| FL-SC10-07 step 3, U34 | tablet | ![FL-SC10-07 step 3, U34, light](../../images/07-short-stays-commercial-and-coworking/u34-property-manager/3-furnished-rentals-tablet-light.png) | ![FL-SC10-07 step 3, U34, dark](../../images/07-short-stays-commercial-and-coworking/u34-property-manager/3-furnished-rentals-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc10-23-furnished-rentals-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc10-23-furnished-rentals-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc10-23-furnished-rentals-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc10-23-furnished-rentals-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc10-23-furnished-rentals-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc10-23-furnished-rentals-read-only-desktop-dark.png) |
| Offline | tablet | ![Offline, light](../../images/states/s-sc10-23-furnished-rentals-offline-tablet-light.png) | ![Offline, dark](../../images/states/s-sc10-23-furnished-rentals-offline-tablet-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Property and landlord | E-SC10-19 property, landlord | links | yes while Draft | yes |
| Acquisition values | E-SC10-19 price, land share, furniture | amounts | yes while Draft | yes |
| Depreciation plan | E-SC10-19 plan | years per component | yes while Draft | yes |
| Rents and charges | E-SC10-19 rents, charges | amounts | no | no |
| Depreciation deducted | E-SC10-19 deducted | amount | no | no |
| Carried forward | E-SC10-19 carried forward | amount | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Set the plan | file | property manager | the file becomes Active with its plan |
| Close the year | file | property manager | the figures of the year are kept |
| Export | file | property manager, landlord | the figures as a file for the return |
| Close the file | file | property manager | the file becomes Closed at the sale |

## States

- Normal: the values, the plan and the figures of the year with the depreciation deducted and carried forward.
- Empty: No furnished property yet, with New file.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a missing land
  share or depreciation above the result, with the field to correct.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC10-19 Furnished property](../../data/e-sc10-19-furnished-property.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC10-19 Furnished property | Draft | Badge "Draft"; a new record starts here; next: Active (UC-SC10-23); fields editable within the role | U34, U09 | `u34-property-manager/s-sc10-23-furnished-rentals-e-sc10-19-furnished-property-draft-{desktop,tablet}-{light,dark}.png`, `u09-customer/s-sc10-23-furnished-rentals-e-sc10-19-furnished-property-draft-phone-{light,dark}.png` |
| E-SC10-19 Furnished property | Active | Badge "Active"; next: Closed (UC-SC10-23); fields editable within the role | U34, U09 | `u34-property-manager/s-sc10-23-furnished-rentals-e-sc10-19-furnished-property-active-{desktop,tablet}-{light,dark}.png`, `u09-customer/s-sc10-23-furnished-rentals-e-sc10-19-furnished-property-active-phone-{light,dark}.png` |
| E-SC10-19 Furnished property | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U34, U09 | `u34-property-manager/s-sc10-23-furnished-rentals-e-sc10-19-furnished-property-closed-{desktop,tablet}-{light,dark}.png`, `u09-customer/s-sc10-23-furnished-rentals-e-sc10-19-furnished-property-closed-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

The property manager works on a desktop; the guest, the tenant or the member uses the phone, with the same actions in
one column.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC10-07](../../flows/fl-sc10-07-short-stays-commercial-and-coworking.md)

## Open questions

None.

---

⬅️ [S-SC10-22 Commercial leases](s-sc10-22-commercial-leases.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC10-24 Coworking](s-sc10-24-coworking.md)
