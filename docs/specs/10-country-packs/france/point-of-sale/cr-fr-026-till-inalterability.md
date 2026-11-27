🏠 [Specs](../../../README.md) › 🌍 [Country packs](../../README.md) › 🇫🇷 [France](../README.md) ›
🏪 [Point of sale](README.md) › ⚖️ CR-FR-026 Till data is inalterable

# ⚖️ CR-FR-026 Till data is inalterable

**Status:** ✅ specified

## Statement

A recorded sale is never edited: a correction is a new plus or minus entry, itself recorded and protected, and the chain
of sales proves nothing was altered.

## Values

- Corrections: plus and minus entries only.
- Integrity: chained signatures over sales and closures, checked on demand.

## Legal references

- [BOI-TVA-DECLA-30-10-30](https://bofip.impots.gouv.fr/doctrine/pgp/10691-PGP) §80 to §120.

## Effective dates

Since 2018-01-01, for every VAT-registered business recording payments from consumers in a till system ([impots.gouv.fr, champ d'application de l'obligation](https://www.impots.gouv.fr/professionnel/questions/quel-est-le-champ-dapplication-de-lobligation-de-detenir-un-logiciel-de), read 2026-11-27).

## Enforced by

- [Regulatory](../../../02-functional/f10-point-of-sale/regulatory.md)

## When the law changes

Watched in the law corpus: BOI-TVA-DECLA-30-10-30. A change flags this rule and warns the administrators; the corrected
rule ships in a pack update (D294).

## Penalty

As CR-FR certified till software.

## Exceptions

None.

## Open questions

[Q17 Country-rule penalties and start dates still to read](../../../07-questions/q17-unread-penalties-and-dates.md).

---

⬅️ [CR-FR-025 Data recorded for each sale](cr-fr-025-sale-data-recorded.md) · ⬆️ [Up](README.md) ·
➡️ [CR-FR-027 Till security and training mode](cr-fr-027-till-security.md)
