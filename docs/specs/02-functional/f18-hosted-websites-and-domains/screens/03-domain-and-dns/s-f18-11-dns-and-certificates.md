🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🌐 [F18 Hosted websites and domains (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F18-03 Domain and DNS](README.md) › 🖥️ S-F18-11 DNS and certificates

# 🖥️ S-F18-11 DNS and certificates

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U48 Hosting engineer](../../../../01-users/personas/u48-hosting-engineer.md)

## Purpose

Manage the DNS zone and certificates.

## Entry points

Hosted websites and domains in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F18-03 step 3, U07 | desktop | ![FL-F18-03 step 3, U07, light](../../images/03-domain-and-dns/u07-administrator/3-dns-plan-desktop-light.png) | ![FL-F18-03 step 3, U07, dark](../../images/03-domain-and-dns/u07-administrator/3-dns-plan-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f18-11-dns-and-certificates-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f18-11-dns-and-certificates-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f18-11-dns-and-certificates-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f18-11-dns-and-certificates-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f18-11-dns-and-certificates-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f18-11-dns-and-certificates-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f18-11-dns-and-certificates-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f18-11-dns-and-certificates-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the zone's records, the change plan and certificates.
- Empty: "No record yet".
- Loading: the frame and titles show at once with placeholder rows for the records; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: the hosting engineer helps; the administrator applies.
- Offline: not available offline: DNS changes need the network. D38 keeps only today's schedule, time and intervention
  records offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and
  nothing is queued until the connection is back.

Shown entities (VD-15): [E-F18-09 TLS certificate](../../data/e-f18-09-tls-certificate.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F18-09 TLS certificate | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07, U48 | `u07-administrator/s-f18-11-dns-and-certificates-e-f18-09-tls-certificate-active-desktop-{light,dark}.png`, `u48-hosting-engineer/s-f18-11-dns-and-certificates-e-f18-09-tls-certificate-active-{desktop,phone}-{light,dark}.png` |

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

⬅️ [S-F18-10 Connect domain](s-f18-10-connect-domain.md) · ⬆️ [Up](README.md) ·
➡️ [S-F18-12 Mail records](s-f18-12-mail-records.md)
