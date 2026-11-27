🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🛟 [F20 Hosted support assistant (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F20-15 Release notes before each upgrade

# 📏 BR-F20-15 Release notes before each upgrade

**Status:** ✅ specified

## Statement

Each upgrade of the hosted service comes with release notes in plain words, sorted by capability and role, published
before the upgrade reaches the customer; users see a short "what is new" on their first sign-in after it.

## Why

Customers must know what changes for them (D477).

## Examples

| Case | Result |
|---|---|
| Upgrade 1.4 with notes for accounting and HR | passes |
| Upgrade without notes | fails: blocked from the customer's rollout |
| Notes listing internal ticket numbers only | fails: rewritten in plain words |

## Applies to

- [UC-F20-22 Read the release notes of an upgrade](../use-cases/05-maintenance-and-releases/uc-f20-22-read-the-release-notes-of-an-upgrade.md)

## Exceptions

Security fixes may be described after the upgrade to avoid revealing the weakness.

## Configurable

Users may turn off "what is new".

## Open questions

None.

---

⬅️ [BR-F20-14 Maintenance announced ahead](br-f20-14-maintenance-announced-ahead.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F20-16 Written report after a major incident](br-f20-16-written-report-after-a-major-incident.md)
