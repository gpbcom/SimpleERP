🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🤖 [Decisions: F3 Assistant](README.md) ›
📜 D175 Knowledge freshness

# 📜 D175 Knowledge freshness

**Status:** ✅ decided

## Context

How knowledge is kept up to date.

## Options

- An owner and a review date.
- A review date only.
- Nothing.

## Choice

Each item has an owner and a review date, one year by default; past it, the owner is reminded, and the AI assistant
warns "this may be out of date" when it uses the item.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

Stale procedures are visible (BR-F3-22).

## Related

- [UC-F3-07](../../02-functional/f03-assistant/use-cases/07-manage-knowledge/uc-f03-07-manage-the-company-knowledge-base.md)

---

⬅️ [D174 Knowledge audience](d174-knowledge-audience.md) · ⬆️ [Up](README.md) ·
➡️ [D176 Knowledge editors and proposals](d176-knowledge-editors.md)
