🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 📒 [Decisions: F8 Accounting](README.md) ›
📜 D279 Bank connections

# 📜 D279 Bank connections

**Status:** ✅ decided

## Context

How bank accounts are connected.

## Options

- Aggregators and files.
- Files only.
- One aggregator.

## Choice

Open-banking (PSD2) aggregators the company picks (for example Bridge, Powens, GoCardless Bank Account Data, Salt Edge,
Enable Banking) and statement files (CAMT.053, OFX, QIF, CSV, MT940); AI matching with reconciliation models.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

BR-F8-03; aggregators through T12, credentials in the vault (D240).

## Related

- [F8 Accounting](../../02-functional/f08-accounting/README.md)

---

⬅️ [D278 French filings prepared and filed](d278-french-filings.md) · ⬆️ [Up](README.md) ·
➡️ [D280 Who keeps the books](d280-bookkeepers.md)
