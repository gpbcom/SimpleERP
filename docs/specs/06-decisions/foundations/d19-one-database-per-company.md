🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🧭 [Decisions: Foundations](README.md) ›
📜 D19 One database per company

# 📜 D19 One database per company

**Status:** ✅ decided

## Context

How several companies on one install are kept apart.

## Options

- One database per company.
- One shared database with row-level security.
- One schema per company.

## Choice

One database per company (answers Q5).

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

Each company is backed up, restored, moved or deleted on its own (see the data isolation page).

## Related

- [Q5](../../07-questions/q05-keeping-companies-apart.md), which it answers
- [Data isolation](../../05-non-functional/data-isolation.md)

---

⬅️ [D18 Installation](d18-installation.md) · ⬆️ [Up](README.md) · ➡️ [D20 No size limit](d20-no-size-limit.md)
