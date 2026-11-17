🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🎨 [Decisions: Users and UX](README.md) ›
📜 D38 Offline field tasks

# 📜 D38 Offline field tasks

**Status:** ✅ decided

## Context

Field workers use their phone on site, sometimes without network.

## Options

- Offline for field tasks.
- Always online.
- A fully offline app.

## Choice

Today's schedule, time and intervention records work offline and sync when the network is back. Everything else needs
the network.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

The field worker's phone screens keep a local copy of the day and a queue of changes; conflicts on sync are a question
for F9 and T5.

## Related

- [Field worker](../../01-users/personas/u14-field-worker.md)
- [Availability](../../05-non-functional/availability.md)

---

⬅️ [D37 Remote access](../security-and-compliance/d37-remote-access.md) · ⬆️ [Up](README.md) ·
➡️ [D39 Product name](d39-product-name.md)
