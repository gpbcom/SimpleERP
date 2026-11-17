🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › ⚖️ [F15 Legal assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F15-24 A probable loss gets a provision proposal in F8

# 📏 BR-F15-24 A probable loss gets a provision proposal in F8

**Status:** ✅ specified

## Statement

When a dispute's risk of loss is assessed as probable and an estimate of the loss is given, a provision proposal for
that estimate is created for accounting in F8, which approves and posts it; the legal side never posts an entry.

## Why

The accounts must show a probable loss in the period it becomes probable, and only accounting posts entries
([UC-F8-02](../../f08-accounting/use-cases/01-set-up-and-post/uc-f08-02-post-and-review-entries.md)). The owner asked
for a litigation register
([D534](../../../06-decisions/f15-legal-assistant/d534-benchmark-gaps-f15-legal-assistant.md)). The
France-pack rule is written later.

## Examples

| Case | Result |
|---|---|
| Probable, estimate 30,000 EUR | proposal of 30,000 EUR to accounting |
| Possible, no estimate | no proposal, noted for the accounts' notes |
| Remote | no proposal |
| Judgment of 28,000 after a provision of 30,000 | the provision is adjusted by 2,000 |
| A won case | the provision is reversed |

## Applies to

- [UC-F15-20](../use-cases/07-equity-contracts-and-disputes/uc-f15-20-keep-the-litigation-register.md)
- [E-F15-21 Dispute](../data/e-f15-21-dispute.md)
- [E-F15-21 Dispute](../data/e-f15-21-dispute.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F15-23 Renewals are warned before their deadline](br-f15-23-renewals-are-warned-before-their-deadline.md) ·
⬆️ [Up](README.md)
