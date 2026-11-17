🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🛡️ [Decisions: F1 Administration](README.md) ›
📜 D77 Record rule kinds

# 📜 D77 Record rule kinds

**Status:** ✅ decided

## Context

Which record rules the editor offers out of the box.

## Options

- Own records only.
- Own site only.
- Own team.
- Amount limits.

## Choice

All four: own records only, own site only, own team (the people the user manages), and amount limits (for example
approve purchases up to 2,000 EUR).

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

Rules combine within a role; across roles the more permissive wins (BR-F1-08).

## Related

- [UC-F1-06](../../02-functional/f01-administration/use-cases/04-edit-a-role/uc-f01-06-edit-a-role-and-its-record-rules.md)
- [BR-F1-12](../../02-functional/f01-administration/business-rules/br-f01-12-record-rule-kinds.md)

---

⬅️ [D76 Role permissions as a matrix](d76-role-matrix.md) · ⬆️ [Up](README.md) ·
➡️ [D78 Ready-made roles are copied](d78-ready-made-roles-copied.md)
