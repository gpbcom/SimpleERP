🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F25-07 Roadmap, beta, credits and changelog](README.md) › 🖥️ S-F25-25 Public roadmap

# 🖥️ S-F25-25 Public roadmap

**Status:** ✅ specified

## Personas

- [U09 Customer](../../../../01-users/personas/u09-customer.md): the roadmap on a phone, by module.
- [U47 SimpleERP maintainer](../../../../01-users/personas/u47-simpleerp-maintainer.md): the items to write, publish,
  move and drop.

## Purpose

Show the accepted tickets in plain words by horizon, module and status.

## Entry points

The public roadmap page of the product; the app's What is coming link; a request's status page.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Roadmap     Module [All v]    Now 6   Next 9   Later 14                  [+ New item]        |
|---------------------------------------------------------------------------------------------|
| NOW                                                                                          |
|  Export payslips as a file for the payroll firm      Payroll           In progress          |
|  Faster stock counts on a phone                      Purchasing, stock In progress          |
| NEXT                                                                                         |
|  Seat check for software subscriptions               Platform costs    Planned              |
| This is a statement of intent, not a promise of dates.   [Follow] [Open] [Move] [Drop]      |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F25-07 step 1, U09 | phone | ![FL-F25-07 step 1, U09, light](../../images/07-roadmap-beta-and-credits/u09-customer/1-public-roadmap-phone-light.png) | ![FL-F25-07 step 1, U09, dark](../../images/07-roadmap-beta-and-credits/u09-customer/1-public-roadmap-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-f25-25-public-roadmap-empty-phone-light.png) | ![Empty, dark](../../images/states/s-f25-25-public-roadmap-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-f25-25-public-roadmap-loading-phone-light.png) | ![Loading, dark](../../images/states/s-f25-25-public-roadmap-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-f25-25-public-roadmap-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-f25-25-public-roadmap-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f25-25-public-roadmap-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f25-25-public-roadmap-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Title in plain words | E-F25-16 title | text | maintainer | yes |
| Module | E-F25-16 module | text | maintainer | yes |
| Horizon | E-F25-16 horizon | Now, Next, Later | maintainer | yes |
| Status | E-F25-16 status | badge | set by the work | yes |
| Reason for a move | E-F25-16 reason | text | maintainer | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| New item | header | maintainer | proposes an item from an accepted ticket |
| Publish | item | maintainer | makes the item public |
| Move or drop | item | maintainer | changes the horizon or drops the item, with a reason |
| Follow | item | hosted customer | sends the status changes of the item |

## States

- Normal: the published items by horizon with module and status.
- Empty: No item published yet, with the link to the declined requests.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a refused item
  shows that its ticket lacks the approval label or is private.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: The last roadmap read is shown with its date; following an item waits for the network.

Shown entities (VD-15): [E-F25-16 Roadmap item](../../data/e-f25-16-roadmap-item.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F25-16 Roadmap item | Planned | Badge "Planned"; a new record starts here; next: In progress or Dropped (UC-F25-25); fields editable within the role | U09, U47 | `u09-customer/s-f25-25-public-roadmap-e-f25-16-roadmap-item-planned-phone-{light,dark}.png`, `u47-simpleerp-maintainer/s-f25-25-public-roadmap-e-f25-16-roadmap-item-planned-{desktop,phone}-{light,dark}.png` |
| E-F25-16 Roadmap item | In progress | Badge "In progress"; next: Shipped or Dropped (UC-F25-25); fields editable within the role | U09, U47 | `u09-customer/s-f25-25-public-roadmap-e-f25-16-roadmap-item-in-progress-phone-{light,dark}.png`, `u47-simpleerp-maintainer/s-f25-25-public-roadmap-e-f25-16-roadmap-item-in-progress-{desktop,phone}-{light,dark}.png` |
| E-F25-16 Roadmap item | Shipped | Badge "Shipped"; final: read-only, no next state; the history shows how it got here | U09, U47 | `u09-customer/s-f25-25-public-roadmap-e-f25-16-roadmap-item-shipped-phone-{light,dark}.png`, `u47-simpleerp-maintainer/s-f25-25-public-roadmap-e-f25-16-roadmap-item-shipped-{desktop,phone}-{light,dark}.png` |
| E-F25-16 Roadmap item | Dropped | Badge "Dropped"; final: read-only, no next state; the history shows how it got here | U09, U47 | `u09-customer/s-f25-25-public-roadmap-e-f25-16-roadmap-item-dropped-phone-{light,dark}.png`, `u47-simpleerp-maintainer/s-f25-25-public-roadmap-e-f25-16-roadmap-item-dropped-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

On a phone the roadmap is one column: horizon headings, module filter on top, items as cards. The maintainer's editing
screen is desktop only.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F25-07](../../flows/fl-f25-07-roadmap-beta-and-credits.md)

## Open questions

None.

---

⬅️ [S-F25-24 Public requests](../05-tell-the-customer/s-f25-24-public-requests.md) · ⬆️ [Up](README.md) ·
➡️ [S-F25-26 Beta programme](s-f25-26-beta-programme.md)
