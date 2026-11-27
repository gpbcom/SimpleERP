🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F25-05 Agents never merge or deploy

# 📏 BR-F25-05 Agents never merge or deploy

**Status:** ✅ specified

## Statement

The agents write branches, pull requests, issues and comments only; merging, deploying and moving to Ready stay with
maintainers.

## Why

See [D435](../../../06-decisions/f25-devops-agents/d435-agents-access-and-limits.md).

## Examples

| Case | Result |
|---|---|
| Fix ready | Pull request opened, waiting for review |

## Applies to

Every F25 use case concerned.

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F25-04 Read-only on production](br-f25-04-read-only-on-production.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F25-06 Specs and code studied first](br-f25-06-specs-and-code-studied-first.md)
