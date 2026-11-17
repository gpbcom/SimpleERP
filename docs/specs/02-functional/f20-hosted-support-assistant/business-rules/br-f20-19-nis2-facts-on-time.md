🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🛟 [F20 Hosted support assistant (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F20-19 NIS2 facts on time

# 📏 BR-F20-19 NIS2 facts on time

**Status:** 🔄 waiting for the owner

## Statement

A customer that declares itself subject to NIS2 receives, after an incident affecting it, a fact sheet with what it
needs for its own notification (start, nature, services, data, measures) within (Proposed) 24 hours, then updates.

## Why

[CR-FR-169 NIS2 incident notification](../../../10-country-packs/france/digital/cr-fr-169-nis2-incident-notification.md);
the customer's deadlines are (Proposed) to read.

## Examples

| Case | Result |
|---|---|
| Customer subject to NIS2, outage at 09:00 | passes: facts by 09:00 next day |
| Customer not subject | passes: written report only (BR-F20-16) |
| Facts missing the services affected | fails: not sent until completed |

## Applies to

- [UC-F20-26 Give the facts for a NIS2 notification](../use-cases/06-after-an-incident/uc-f20-26-give-the-facts-for-a-nis2-notification.md)
- [UC-F20-15 Handle a security incident or breach](../use-cases/03-incidents/uc-f20-15-handle-a-security-incident-or-breach.md)

## Exceptions

None.

## Configurable

The customer declares whether it is subject.

## Open questions

None.

---

⬅️ [BR-F20-18 Support in French or English](br-f20-18-support-in-french-or-english.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F20-20 Calls follow the plan's times](br-f20-20-calls-follow-the-plans-times.md)
