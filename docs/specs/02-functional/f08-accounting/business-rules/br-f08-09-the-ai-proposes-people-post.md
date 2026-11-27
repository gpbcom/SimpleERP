🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 📒 [F8 Accounting](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F8-09 The AI proposes, people post

# 📏 BR-F8-09 The AI proposes, people post

**Status:** ✅ specified

## Statement

The AI reads documents, matches bank lines and proposes accounts, taxes and entries; only reconciliation models set to
auto-validate post by themselves; every other entry is posted by a person; filings are always validated by an accountant
(BR-F8-04).

A reconciliation model set to auto-validate is a procedure an administrator switched to automatic: its entries are
audited and sampled; it never pays and never files
([D439](../../../06-decisions/f03-assistant/d439-ai-autonomy-tiers.md)).

## Why

See [D284](../../../06-decisions/f08-accounting/d284-ai-in-bookkeeping.md).

## Examples

| Case | Result |
|---|---|
| A bill read, account 606 proposed | The accountant posts it |
| Card fees by an auto-validated model | Posted automatically |

## Applies to

Every F8 use case concerned.

- [UC-F8-27 Analyse the month's flux with AI comments](../use-cases/09-pay-analyse-and-report/uc-f08-27-analyse-the-months-flux-with-ai-comments.md)

## Exceptions

None.

## Configurable

Yes: which models auto-validate.

## Open questions

None.

---

⬅️ [BR-F8-08 New IBANs are checked](br-f08-08-new-ibans-are-checked.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F8-10 Several books share one source](br-f08-10-books-share-one-source.md)
