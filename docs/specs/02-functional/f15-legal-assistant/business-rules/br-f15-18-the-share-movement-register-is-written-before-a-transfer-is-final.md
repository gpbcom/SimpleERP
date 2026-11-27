🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › ⚖️ [F15 Legal assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F15-18 The share-movement register is written before a transfer is final

# 📏 BR-F15-18 The share-movement register is written before a transfer is final

**Status:** ✅ specified

## Statement

A share movement takes effect only when its entry is written in the share-movement register with its number and date;
until then the cap table, the votes and the statements are unchanged, and a written entry is never edited, only
corrected by a new line.

## Why

The register is the company's proof of who owns it. A transfer that counted before it was written would let two tables
disagree. The owner asked for full equity
([D534](../../../06-decisions/f15-legal-assistant/d534-benchmark-gaps-f15-legal-assistant.md)). The
France-pack rule on the register is CR-FR-214: a transfer is enforceable against the company from its entry.

## Examples

| Case | Result |
|---|---|
| A transfer signed but not written | Approved, the table unchanged |
| The same transfer written as entry 2026-014 | Registered, the table updated |
| An entry made in error | corrected by a new line, the old line stays |
| An issue approved by a general meeting | written when the subscriptions are paid |
| A transfer that leaves a holder below zero | refused |

## Applies to

- [UC-F15-14](../use-cases/07-equity-contracts-and-disputes/uc-f15-14-keep-the-cap-table-and-share-movements.md)
- [E-F15-15 Shareholding](../data/e-f15-15-shareholding.md)
- [E-F15-07 Corporate decision](../data/e-f15-07-corporate-decision.md)
- France-pack rule:
  [CR-FR-214 The share-movement register](../../../10-country-packs/france/company/cr-fr-214-share-movement-register.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F15-17 Warning triggers by block](br-f15-17-warning-triggers-by-block.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F15-19](br-f15-19-grants-follow-the-plan-approved-by-shareholders.md)
