🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F25-04 Read-only on production

# 📏 BR-F25-04 Read-only on production

**Status:** ✅ specified

## Statement

The agents read only the reporting customer's namespace, through the audited read-only access of F20, with personal data
and secrets masked.

## Why

See [D435](../../../06-decisions/f25-devops-agents/d435-agents-access-and-limits.md).

## Examples

| Case | Result |
|---|---|
| Needs another customer's logs | Refused |

## Applies to

Every F25 use case concerned.

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F25-03 Duplicates are merged](br-f25-03-duplicates-merged.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F25-05 Agents never merge or deploy](br-f25-05-agents-never-merge-or-deploy.md)
