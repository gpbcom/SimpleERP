🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
⚖️ [F15 Legal assistant](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F15-04 Set up the legal assistant](README.md) › 🖥️ S-F15-06 Standards register

# 🖥️ S-F15-06 Standards register

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md), who uploads the company's own copies
- [U13 Owner](../../../../01-users/personas/u13-owner.md), who attests the AI-use licence

## Purpose

List the copyrighted standards that apply, by reference only, and the company's own copies indexed after attestation.

## Entry points

Legal assistant settings, "Standards"; a legal answer citing a standard.

## Wireframe

```text
Standards register                                      [Upload own copy]
-------------------------------------------------------------------------------
Reference        Title                         Edition   Status    Own copy
NF C 15-100      Low-voltage installations     2024      in force  indexed (attested)
ISO 22000        Food safety management        2018      in force  -
-------------------------------------------------------------------------------
Where to get it: the publisher's page for each standard
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F15-04 step 4, U07 | desktop | ![FL-F15-04 step 4, U07, light](../../images/04-set-up-the-legal-assistant/u07-administrator/4-standards-register-desktop-light.png) | ![FL-F15-04 step 4, U07, dark](../../images/04-set-up-the-legal-assistant/u07-administrator/4-standards-register-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f15-06-standards-register-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f15-06-standards-register-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f15-06-standards-register-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f15-06-standards-register-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f15-06-standards-register-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f15-06-standards-register-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f15-06-standards-register-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f15-06-standards-register-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Reference | E-F15-04 reference | text | no | yes |
| Title, edition, status | E-F15-04 | text | no | yes |
| Own copy | E-F15-04 own copy | indexed, references only, none | no | no |
| Attestation | E-F15-04 attestation | date and person | yes (owner) | for an upload |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Upload own copy | header | administrator | copy indexed once attested |
| Attest | upload dialog | owner | AI-use licence attested |
| Withdraw attestation | row | owner | copy removed from the index |

## States

- Normal: the standards that apply to the company's sector with their status and own copies.
- Empty: "No standard applies to your sector yet".
- Loading: the frame and titles show at once with placeholder rows for the standards; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: an upload without attestation, refused with the reason.
- Read-only: register entries come from open sources and cannot be edited.
- Offline: not available offline: the register is on the server. D38 keeps only today's schedule, time and intervention
  records offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and
  nothing is queued until the connection is back.

Shown entities (VD-15): [E-F15-04 Standard register entry](../../data/e-f15-04-standard-register-entry.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F15-04 Standard register entry | Open | Badge "Open"; a new record starts here; no other state; fields editable within the role | U07, U13 | `u07-administrator/s-f15-06-standards-register-e-f15-04-standard-register-entry-open-desktop-{light,dark}.png`, `u13-owner/s-f15-06-standards-register-e-f15-04-standard-register-entry-open-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-12 File upload](../../../../04-ux/design-system/components/c-12-file-upload.md)
- [C-05 Modal](../../../../04-ux/design-system/components/c-05-modal.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F15-04 Set up the legal assistant](../../flows/fl-f15-04-set-up-the-legal-assistant.md)

## Open questions

None.

---

⬅️ [S-F15-05 Law packs refresh](s-f15-05-law-packs-refresh.md) · ⬆️ [Up](README.md) ·
➡️ [S-F15-07 Compliance calendar](../05-duties-and-records/s-f15-07-compliance-calendar.md)
