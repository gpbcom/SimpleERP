🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🛟 [F20 Hosted support assistant (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F20-14 Maintenance announced ahead

# 📏 BR-F20-14 Maintenance announced ahead

**Status:** 🔄 waiting for the owner

## Statement

Planned maintenance that may interrupt a customer's service is announced at least (Proposed) 7 days ahead with its
window, expected effect and contact, and runs outside the customer's business hours (Proposed) unless urgent for
security.

## Why

Customers plan around interruptions (D477).

## Examples

| Case | Result |
|---|---|
| Maintenance on 2026-11-22 22:00 announced on 2026-11-14 | passes |
| Maintenance announced 2 days ahead without security reason | fails: refused |
| Security patch needed at once | passes: announced as urgent, status page open |

## Applies to

- [UC-F20-21 Announce planned maintenance](../use-cases/05-maintenance-and-releases/uc-f20-21-announce-planned-maintenance.md)

## Exceptions

Urgent security fixes follow the incident rules.

## Configurable

The notice delay and the default window per region (Proposed).

## Open questions

None.

---

⬅️ [BR-F20-13 Health data out of the models' reach](br-f20-13-health-data-out-of-reach.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F20-15 Release notes before each upgrade](br-f20-15-release-notes-before-each-upgrade.md)
