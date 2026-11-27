🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F25-03 Duplicates are merged

# 📏 BR-F25-03 Duplicates are merged

**Status:** ✅ specified

## Statement

A request matching an open USER ticket is linked to it as a new voice, not filed twice.

## Why

See [D433](../../../06-decisions/f25-devops-agents/d433-user-family-and-labels.md).

## Examples

| Case | Result |
|---|---|
| Same bug from 3 companies | One ticket, 3 reporters |

## Applies to

Every F25 use case concerned.

## Exceptions

None.

## Configurable

Similarity threshold.

## Open questions

None.

---

⬅️ [BR-F25-02 One USER feature, one ticket](br-f25-02-one-user-feature-one-ticket.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F25-04 Read-only on production](br-f25-04-read-only-on-production.md)
