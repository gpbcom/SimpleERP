🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › ⚙️ [Decisions: Technical](README.md) ›
📜 D147 Target design sections in docs/technical

# 📜 D147 Target design sections in docs/technical

**Status:** ✅ decided

## Context

docs/technical describes what is built (DOC-2), and nothing is built yet.

## Options

- A "Target design" section in each chapter.
- A separate design folder.
- Only in docs/specs.

## Choice

Each chapter of docs/technical holds a section "Target design (specified in GH-2, not built yet)"; topics without a
chapter get a new one. Later tickets move each part above it as they build it.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

Nine new chapters: performance and capacity, security, supply chain and licences, observability, AI operations,
deployment, release and versioning, data migration, plugin SDK.

## Related

- [Technical capabilities](../../03-technical/README.md)
- [Technical documentation](../../../technical/README.md)

---

⬅️ [D146 Technical design interviews before T1 to T11](d146-technical-interviews-placement.md) · ⬆️ [Up](README.md) ·
➡️ [D148 The 15 technical design topics](d148-technical-interview-topics.md)
