🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🌐 [F18 Hosted websites and domains (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F18-03 Domain and DNS](README.md) › 🖥️ S-F18-12 Mail records

# 🖥️ S-F18-12 Mail records

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Set mail records SPF, DKIM and DMARC.

## Entry points

Hosted websites and domains in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F18-03 step 4, U07 | desktop | ![FL-F18-03 step 4, U07, light](../../images/03-domain-and-dns/u07-administrator/4-mail-desktop-light.png) | ![FL-F18-03 step 4, U07, dark](../../images/03-domain-and-dns/u07-administrator/4-mail-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f18-12-mail-records-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f18-12-mail-records-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f18-12-mail-records-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f18-12-mail-records-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f18-12-mail-records-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f18-12-mail-records-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f18-12-mail-records-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f18-12-mail-records-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: SPF, DKIM and DMARC with their weekly check.
- Empty: "Mail records not set".
- Loading: the frame and titles show at once with placeholder rows for the mail records; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: generated values are read-only.
- Offline: not available offline: records are checked online. D38 keeps only today's schedule, time and intervention
  records offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and
  nothing is queued until the connection is back.

Shown entities (VD-15): [E-F18-08 DNS record](../../data/e-f18-08-dns-record.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F18-08 DNS record | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U07 | `u07-administrator/s-f18-12-mail-records-e-f18-08-dns-record-recorded-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F18-03 Domain and DNS](../../flows/fl-f18-03-domain-and-dns.md)

## Open questions

None.

---

⬅️ [S-F18-11 DNS and certificates](s-f18-11-dns-and-certificates.md) · ⬆️ [Up](README.md) ·
➡️ [S-F18-13 Preview](../04-test-and-publish/s-f18-13-preview.md)
