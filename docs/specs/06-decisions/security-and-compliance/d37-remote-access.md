🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🛡️ [Decisions: Security and compliance](README.md) ›
📜 D37 Remote access

# 📜 D37 Remote access

**Status:** ✅ decided

## Context

How office workers reach SimpleERP when working remotely (U16).

## Options

- Internet and two-factor authentication.
- VPN only.
- Office network only.

## Choice

From anywhere over HTTPS, with two-factor authentication (D13). An administrator can restrict some roles to the office
network if needed.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

No VPN is needed; T2 offers the network restriction per role.

Revised by D450 on 2026-11-12: the two factors apply to every user, passkeys preferred.

## Related

- [Security](../../05-non-functional/security.md)
- [T2 Identity and access engine](../../03-technical/t02-identity-and-access/README.md)

---

⬅️ [D36 What a location holds](../f07-purchasing-and-stock/d36-what-a-location-holds.md) · ⬆️ [Up](README.md) ·
➡️ [D38 Offline field tasks](../ux/d38-offline-field-tasks.md)
