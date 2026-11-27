🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F25-18 The roadmap shows accepted tickets only

# 📏 BR-F25-18 The roadmap shows accepted tickets only

**Status:** ✅ specified

## Statement

The roadmap shows an item only if its ticket carries the maintainers' approval label and is not a private case; a ticket
that is declined, pending, a vulnerability case or marked for health data never appears, and no reporter is named.

## Why

A roadmap that shows what was not accepted creates promises the maintainers did not make. The owner asked for a public
roadmap ([D544](../../../06-decisions/f25-devops-agents/d544-benchmark-gaps-f25-devops-agents.md)); approval is the
maintainers' ([BR-F25-07](br-f25-07-approval-before-ready.md)) and security reports stay private
([BR-F25-12](br-f25-12-security-reports-stay-private.md)).

## Examples

| Case | Result |
|---|---|
| An approved ticket | can be published |
| A ticket still under triage | not shown |
| A vulnerability case before disclosure | not shown |
| A declined request | not on the roadmap, shown on the public declined list instead |
| A ticket whose reporter asked for anonymity | shown without any name |

## Applies to

- [UC-F25-25](../use-cases/07-roadmap-beta-and-credits/uc-f25-25-read-the-public-roadmap.md)
- [E-F25-16 Roadmap item](../data/e-f25-16-roadmap-item.md)
- [BR-F25-07 Approval before Ready](br-f25-07-approval-before-ready.md)
- [BR-F25-17](br-f25-17-declined-requests-stay-public-as-votes.md)

## Exceptions

None.

## Configurable

No: the rule cannot be relaxed.

## Open questions

None.

---

⬅️ [BR-F25-17 Declined requests stay public as votes](br-f25-17-declined-requests-stay-public-as-votes.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F25-19 Betas run on a sandbox copy only](br-f25-19-betas-run-on-a-sandbox-copy-only.md)
