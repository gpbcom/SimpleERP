🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F25-20 Credits go to confirmed, non-duplicate reports only

# 📏 BR-F25-20 Credits go to confirmed, non-duplicate reports only

**Status:** ✅ specified

## Statement

A credit is granted only to a report that a maintainer has confirmed and that is not a duplicate of an earlier one; each
fault earns at most one credit, to its first reporter, and a vulnerability report earns its credit only once its
advisory is disclosed.

## Why

Credits must reward real help and must not pay for repetition or noise. The owner asked for bug-report credits
([D544](../../../06-decisions/f25-devops-agents/d544-benchmark-gaps-f25-devops-agents.md)); duplicates are merged
([BR-F25-03](br-f25-03-duplicates-merged.md)).

## Examples

| Case | Result |
|---|---|
| First confirmed report of a fault | credit by severity |
| A second report of the same fault | no credit, shown the first one |
| A report nobody can reproduce | no credit |
| A vulnerability report before disclosure | credit pending, not granted |
| Two companies reporting the same fault on the same day | the earlier timestamp earns the credit |

## Applies to

- [UC-F25-27](../use-cases/07-roadmap-beta-and-credits/uc-f25-27-receive-credits-for-confirmed-reports.md)
- [E-F25-18 Report credit](../data/e-f25-18-report-credit.md)
- [BR-F25-03 Duplicates are merged](br-f25-03-duplicates-merged.md)
- [BR-F25-15](br-f25-15-vulnerabilities-handled-under-the-cra.md)
- [E-F25-03 USER ticket](../data/e-f25-03-user-ticket.md)

## Exceptions

None.

## Configurable

The schedule of amounts by severity, by the maintainers, published before it takes effect.

## Open questions

None.

---

⬅️ [BR-F25-19 Betas run on a sandbox copy only](br-f25-19-betas-run-on-a-sandbox-copy-only.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F25-21 The changelog shows installed modules only](br-f25-21-the-changelog-shows-installed-modules-only.md)
