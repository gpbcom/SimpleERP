🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › ⚙️ [Decisions: Technical](README.md) ›
📜 D189 Step 19c becomes Storage

# 📜 D189 Step 19c becomes Storage

**Status:** ✅ decided

## Context

The technical design topic 19c was "Data model" (D148).

## Options

- Data model only.
- Storage as a whole.

## Choice

Step 19c is renamed "Storage" (the owner, 2026-11-10: "This step will be renamed: Storage"). It covers the data model,
the database choice (SQL or NoSQL), the databases' configuration and security, and file and object storage.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

Its target design is written in two docs/technical chapters: data-model.md and a new storage.md.

## Related

- [D148](d148-technical-interview-topics.md)
- [Technical capabilities](../../03-technical/README.md)

---

⬅️ [D188 Retry before an error](../f03-assistant/d188-retry-before-an-error.md) · ⬆️ [Up](README.md) ·
➡️ [D190 Who asks the legal assistant what](../f15-legal-assistant/d190-legal-assistant-askers.md)
