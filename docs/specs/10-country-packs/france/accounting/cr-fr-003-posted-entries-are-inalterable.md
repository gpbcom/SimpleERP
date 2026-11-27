🏠 [Specs](../../../README.md) › 🌍 [Country packs](../../README.md) › 🇫🇷 [France](../README.md) ›
📒 [Accounting](README.md) › ⚖️ CR-FR-003 Posted entries are inalterable

# ⚖️ CR-FR-003 Posted entries are inalterable

**Status:** ✅ specified

## Statement

A posted entry never changes: it is corrected by a reversing entry; posted entries are chained so that any alteration is
detected, and a closed period cannot be reopened.

## Values

- Correction: reversal plus a new entry only.
- Integrity: hash chain over posted entries, checked on demand.
- Closing: once the fiscal year is closed and earnings allocated, its lock cannot be lifted.

## Legal references

- Plan comptable général (règlement ANC 2014-03), art. 1031-3 (definitive entries) and 1031-4 (closing procedure),
  consolidated version of 1 January 2026 ([ANC, PCG consolidated at 1 January 2026](https://www.anc.gouv.fr/files/anc/files/1_Normes_fran%C3%A7aises/Reglements/Recueils/PCG_janvier2026/PCG--1er-janvier-2026.pdf), read 2026-11-27).
- [Code de commerce](https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000005634379/) art. L123-12 to L123-28.

## Effective dates

L123-12 in force since 2000-09-21 ([Code de commerce, art. L123-12](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006219304), read 2026-11-27); the PCG rules on definitive entries and the closing
procedure are art. 1031-3 and 1031-4 of the consolidated version of 1 January 2026 ([ANC, PCG consolidated at 1 January 2026](https://www.anc.gouv.fr/files/anc/files/1_Normes_fran%C3%A7aises/Reglements/Recueils/PCG_janvier2026/PCG--1er-janvier-2026.pdf), read 2026-11-27),
which gives no date per article.

## Enforced by

- [BR-F8-01 Posted entries never change](../../../02-functional/f08-accounting/business-rules/br-f08-01-posted-entries-never-change.md)
- [BR-F8-02 Lock dates](../../../02-functional/f08-accounting/business-rules/br-f08-02-lock-dates.md)
- [Data](../../../02-functional/f08-accounting/data/README.md)
- [Regulatory](../../../02-functional/f08-accounting/regulatory.md)

## When the law changes

Watched in the law corpus: PCG art. 1031-3, 1031-4; CCom L123-12 to L123-28. A change flags this rule and warns the
administrators; the corrected rule ships in a pack update (D294).

## Penalty

None stated in the sources read.

## Exceptions

None.

## Open questions

[Q17 Country-rule penalties and start dates still to read](../../../07-questions/q17-unread-penalties-and-dates.md).

---

⬅️ [CR-FR-002 Accounting records kept 10 years](cr-fr-002-accounting-records-kept-ten-years.md) · ⬆️ [Up](README.md) ·
➡️ [CR-FR-004 Balanced entries, continuous numbers](cr-fr-004-balanced-entries-continuous-numbers.md)
