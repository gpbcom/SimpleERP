🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🤖 [Decisions: F3 Assistant](README.md) ›
📜 D174 Knowledge audience

# 📜 D174 Knowledge audience

**Status:** ✅ decided

## Context

Who sees what in the knowledge base.

## Options

- An audience per item.
- Everyone sees all.
- Per folder only.

## Choice

Each item or folder has an audience: everyone, chosen roles, chosen sites or teams; items inherit their folder's unless
set; the AI assistant never uses an item outside its audience.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

T8 filters by audience (BR-F3-21).

## Related

- [UC-F3-07](../../02-functional/f03-assistant/use-cases/07-manage-knowledge/uc-f03-07-manage-the-company-knowledge-base.md)

---

⬅️ [D173 Knowledge base content](d173-knowledge-content.md) · ⬆️ [Up](README.md) ·
➡️ [D175 Knowledge freshness](d175-knowledge-freshness.md)
