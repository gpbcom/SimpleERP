🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏘️ [SC10 Real estate](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC10-07 Short stays, commercial leases, LMNP and coworking](README.md) ›
🖥️ S-SC10-22 Commercial leases

# 🖥️ S-SC10-22 Commercial leases

**Status:** 🔄 waiting for the owner

## Personas

- [U34 Property manager](../../../../01-users/personas/u34-property-manager.md): the leases, revisions and renewals.

## Purpose

Follow the periods and break dates of each commercial lease and revise the rent on its index within the caps.

## Entry points

Real estate › Commercial leases; the portfolio calendar; the AI assistant.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Lease CL-2023-012: Boulangerie Dupin, shop 4 Rue Haute                 Active   [Revise the rent |
| Start 2023-03-01   Period 1 to 2026-02-28   Next break 2029-02-28   Index ILC                    |
| Rent 18,000.00 a year   Base index 2022 Q3 = 126.05   Charges 1,200.00 a year                    |
| Revision    Date          Index      Rise    New rent    Cap                                     |
| 2026-03-01   ILC 2025 Q3  128.57     2.0 %   18,360.00   within                                  |
| Next revision 2027-03-01     Deposit 4,500.00 held                                               |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC10-07 step 2, U34 | desktop | ![FL-SC10-07 step 2, U34, light](../../images/07-short-stays-commercial-and-coworking/u34-property-manager/2-commercial-leases-desktop-light.png) | ![FL-SC10-07 step 2, U34, dark](../../images/07-short-stays-commercial-and-coworking/u34-property-manager/2-commercial-leases-desktop-dark.png) |
| FL-SC10-07 step 2, U34 | tablet | ![FL-SC10-07 step 2, U34, light](../../images/07-short-stays-commercial-and-coworking/u34-property-manager/2-commercial-leases-tablet-light.png) | ![FL-SC10-07 step 2, U34, dark](../../images/07-short-stays-commercial-and-coworking/u34-property-manager/2-commercial-leases-tablet-dark.png) |
| Error E1, U34 | desktop | ![Error E1, U34, light](../../images/07-short-stays-commercial-and-coworking/u34-property-manager/e1-the-index-cap-is-exceeded-desktop-light.png) | ![Error E1, U34, dark](../../images/07-short-stays-commercial-and-coworking/u34-property-manager/e1-the-index-cap-is-exceeded-desktop-dark.png) |
| Error E1, U34 | tablet | ![Error E1, U34, light](../../images/07-short-stays-commercial-and-coworking/u34-property-manager/e1-the-index-cap-is-exceeded-tablet-light.png) | ![Error E1, U34, dark](../../images/07-short-stays-commercial-and-coworking/u34-property-manager/e1-the-index-cap-is-exceeded-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc10-22-commercial-leases-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc10-22-commercial-leases-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc10-22-commercial-leases-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc10-22-commercial-leases-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc10-22-commercial-leases-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc10-22-commercial-leases-read-only-desktop-dark.png) |
| Offline | tablet | ![Offline, light](../../images/states/s-sc10-22-commercial-leases-offline-tablet-light.png) | ![Offline, dark](../../images/states/s-sc10-22-commercial-leases-offline-tablet-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Tenant and premises | E-SC10-18 tenant, premises | links | yes while Draft | yes |
| Start and periods | E-SC10-18 start date, periods | dates | yes while Draft | yes |
| Index | E-SC10-18 index | ILC or ILAT | yes while Draft | yes |
| Base index | E-SC10-18 base index | number | yes while Draft | yes |
| Rent and charges | E-SC10-18 rent, charges | amounts | yes | yes |
| Revision history | E-SC10-18 revisions | list | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Revise the rent | lease | property manager | a revision with the index, the new rent and its caps |
| Record a notice | lease | property manager | the lease becomes Notice given |
| Renew | lease | property manager | a new lease period with its rent |
| End | lease | property manager | the lease becomes Ended with its date |

## States

- Normal: the lease, its periods, break dates, index and the revisions with their caps.
- Empty: No lease yet, with New lease.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); an index not
  published or a revision above the cap, with the amount allowed.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC10-18 Commercial lease](../../data/e-sc10-18-commercial-lease.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC10-18 Commercial lease | Draft | Badge "Draft"; a new record starts here; next: Active (UC-SC10-22); fields editable within the role | U34 | `u34-property-manager/s-sc10-22-commercial-leases-e-sc10-18-commercial-lease-draft-{desktop,tablet}-{light,dark}.png` |
| E-SC10-18 Commercial lease | Active | Badge "Active"; next: Notice given or Ended (UC-SC10-22); fields editable within the role | U34 | `u34-property-manager/s-sc10-22-commercial-leases-e-sc10-18-commercial-lease-active-{desktop,tablet}-{light,dark}.png` |
| E-SC10-18 Commercial lease | Notice given | Badge "Notice given"; next: Active or Ended (UC-SC10-22); fields editable within the role | U34 | `u34-property-manager/s-sc10-22-commercial-leases-e-sc10-18-commercial-lease-notice-given-{desktop,tablet}-{light,dark}.png` |
| E-SC10-18 Commercial lease | Ended | Badge "Ended"; final: read-only, no next state; the history shows how it got here | U34 | `u34-property-manager/s-sc10-22-commercial-leases-e-sc10-18-commercial-lease-ended-{desktop,tablet}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop only; on a phone, the app asks to continue on a larger screen.

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

⬅️ [S-SC10-21 Short-term rentals](s-sc10-21-short-term-rentals.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC10-23 Furnished rentals](s-sc10-23-furnished-rentals.md)
