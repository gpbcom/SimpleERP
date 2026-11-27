🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🚛 [SC07 Transport and logistics](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC07-07 Passengers, removals, courier and freight](README.md) › 🖥️ S-SC07-23 Last mile

# 🖥️ S-SC07-23 Last mile

**Status:** 🔄 waiting for the owner

## Personas

- [U29 Dispatcher](../../../../01-users/personas/u29-dispatcher.md): the day's parcels by area, the rounds and the
  failed deliveries.
- [U30 Driver](../../../../01-users/personas/u30-driver.md): their round, with the scan and the proof at each stop.

## Purpose

Plan the rounds of parcels, follow the deliveries and give each failed parcel a next step.

## Entry points

Transport and logistics › Parcels; the planning board; the driver's phone.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Depot Lyon-Est   Wed 26 Nov   Parcels 412   Delivered 188   Failed 14   Held 6                   |
| Round  Driver    Stops  Done  Failed  Next stop                  Slot                            |
| R-01   Petit     96     58    3       12 rue Garibaldi          14:00-16:00                      |
| R-02   Garcia    104    71    5       4 av. Berthelot           14:30-16:30                      |
| Failed parcel 98122: no answer 15:10   Recipient choice: new slot Thu 9-12 [Send reminder]       |
| Relay points: Tabac Victor Hugo 3 free   Pressing Gerland 8 free                                 |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC07-07 step 3, U29 | desktop | ![FL-SC07-07 step 3, U29, light](../../images/07-passengers-removals-courier-and-freight/u29-dispatcher/3-last-mile-desktop-light.png) | ![FL-SC07-07 step 3, U29, dark](../../images/07-passengers-removals-courier-and-freight/u29-dispatcher/3-last-mile-desktop-dark.png) |
| FL-SC07-07 step 3, U29 | phone | ![FL-SC07-07 step 3, U29, light](../../images/07-passengers-removals-courier-and-freight/u29-dispatcher/3-last-mile-phone-light.png) | ![FL-SC07-07 step 3, U29, dark](../../images/07-passengers-removals-courier-and-freight/u29-dispatcher/3-last-mile-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc07-23-last-mile-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc07-23-last-mile-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc07-23-last-mile-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc07-23-last-mile-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc07-23-last-mile-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc07-23-last-mile-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc07-23-last-mile-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc07-23-last-mile-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Parcel | E-SC07-20 reference | text | no | yes |
| Recipient | E-SC07-20 recipient | name and address | yes while Received | yes |
| Slot | E-SC07-20 slot | date and time window | yes | yes |
| Round | E-SC07-20 round | link | yes | no |
| Attempts | E-SC07-20 attempts | number | no | no |
| Relay point | E-SC07-20 relay point | link | yes | no |
| Proof | E-SC07-20 proof | signature, photo or code | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Plan rounds | header | dispatcher | parcels grouped by area and slot |
| Deliver | driver's phone | driver | the parcel is Delivered with its proof |
| Mark failed | driver's phone | driver | a reason and a photo, and the recipient is asked to choose |
| Send to relay | parcel | dispatcher, recipient | the parcel is Held at the relay point with a code |

## States

- Normal: the parcels with their slot, round, attempts and proof.
- Empty: No parcel yet, with Receive parcels.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a scanned
  parcel outside the round or a missing proof, with the step to complete.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC07-20 Parcel](../../data/e-sc07-20-parcel.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC07-20 Parcel | Received | Badge "Received"; a new record starts here; next: Out (UC-SC07-23); fields editable within the role | U29, U30 | `u29-dispatcher/s-sc07-23-last-mile-e-sc07-20-parcel-received-{desktop,phone}-{light,dark}.png`, `u30-driver/s-sc07-23-last-mile-e-sc07-20-parcel-received-phone-{light,dark}.png` |
| E-SC07-20 Parcel | Out | Badge "Out"; next: Delivered or Failed (UC-SC07-23, BR-SC07-18); fields editable within the role | U29, U30 | `u29-dispatcher/s-sc07-23-last-mile-e-sc07-20-parcel-out-{desktop,phone}-{light,dark}.png`, `u30-driver/s-sc07-23-last-mile-e-sc07-20-parcel-out-phone-{light,dark}.png` |
| E-SC07-20 Parcel | Delivered | Badge "Delivered"; final: read-only, no next state; the history shows how it got here | U29, U30 | `u29-dispatcher/s-sc07-23-last-mile-e-sc07-20-parcel-delivered-{desktop,phone}-{light,dark}.png`, `u30-driver/s-sc07-23-last-mile-e-sc07-20-parcel-delivered-phone-{light,dark}.png` |
| E-SC07-20 Parcel | Failed | Badge "Failed"; next: Held or Out (BR-SC07-18); fields editable within the role | U29, U30 | `u29-dispatcher/s-sc07-23-last-mile-e-sc07-20-parcel-failed-{desktop,phone}-{light,dark}.png`, `u30-driver/s-sc07-23-last-mile-e-sc07-20-parcel-failed-phone-{light,dark}.png` |
| E-SC07-20 Parcel | Held | Badge "Held"; next: Delivered or Returned (UC-SC07-23, BR-SC07-18); fields editable within the role | U29, U30 | `u29-dispatcher/s-sc07-23-last-mile-e-sc07-20-parcel-held-{desktop,phone}-{light,dark}.png`, `u30-driver/s-sc07-23-last-mile-e-sc07-20-parcel-held-phone-{light,dark}.png` |
| E-SC07-20 Parcel | Returned | Badge "Returned"; final: read-only, no next state; the history shows how it got here | U29, U30 | `u29-dispatcher/s-sc07-23-last-mile-e-sc07-20-parcel-returned-{desktop,phone}-{light,dark}.png`, `u30-driver/s-sc07-23-last-mile-e-sc07-20-parcel-returned-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop for the dispatcher. The driver's phone has the scan button, the next stop and the proof form in large type.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC07-07](../../flows/fl-sc07-07-passengers-removals-courier-and-freight.md)

## Open questions

None.

---

⬅️ [S-SC07-22 Removals](s-sc07-22-removals.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC07-24 Freight forwarding](s-sc07-24-freight-forwarding.md)
