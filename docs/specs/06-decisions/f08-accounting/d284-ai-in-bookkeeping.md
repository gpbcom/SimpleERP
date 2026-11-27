🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 📒 [Decisions: F8 Accounting](README.md) ›
📜 D284 AI in bookkeeping

# 📜 D284 AI in bookkeeping

**Status:** ✅ decided

## Context

How far the AI goes in bookkeeping.

## Options

- Proposes, people post.
- Posts above a confidence.
- Reads only.

## Choice

The AI reads bills, matches bank lines and proposes accounts and entries; reconciliation models may auto-validate;
everything else is posted by a person; filings always by an accountant.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

BR-F8-09.

Revised by D439 on 2026-11-12: an auto-validated reconciliation model is a procedure switched to automatic, audited and
sampled; it never pays and never files.

## Related

- [F8 Accounting](../../02-functional/f08-accounting/README.md)

---

⬅️ [D283 Protection against IBAN fraud](d283-iban-change-protection.md) · ⬆️ [Up](README.md) ·
➡️ [D285 Activity-based timesheet drafts](../f09-hr-and-projects/d285-activity-drafts-opt-in.md)
