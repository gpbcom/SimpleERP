🏠 [Specs](../../../README.md) › 🌍 [Country packs](../../README.md) › 🇫🇷 [France](../README.md) ›
🏪 [Point of sale](README.md) › ⚖️ CR-FR-024 Till software holds a certificate or an attestation

# ⚖️ CR-FR-024 Till software holds a certificate or an attestation

**Status:** ✅ specified

## Statement

A company recording consumer payments in a till must use software that meets the inalterability, security, conservation
and archiving conditions, proven by a certificate from an accredited body or the publisher's individual attestation.

## Values

- Proof: certificate (NF525 or equivalent, by an accredited body) or individual attestation on the official model
  (BOI-LETTRE-000242).
- simple-ERP's choice: the certificate, before the point of sale is sold in France (D296).
- The proof names the product, its version and the acquisition date; a major version needs a new one.

## Legal references

- [Code général des impôts](https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006069577/) art. 286 I 3° bis,
  version in force since 2026-06-27 (loi n° 2026-534, art. 87).
- [BOI-TVA-DECLA-30-10-30](https://bofip.impots.gouv.fr/doctrine/pgp/10691-PGP) §280 to §390.
- [BOFiP news of 01/10/2025, LF 2025 art. 43](https://bofip.impots.gouv.fr/doctrine/pgp/14826-PGP) (attestation removed
  from 2025-02-16).
- [BOFiP news of 25/03/2026, LF 2026 art. 125](https://bofip.impots.gouv.fr/doctrine/pgp/15035-PGP) (attestation
  restored from 2026-02-21).

## Effective dates

Since 2018-01-01; attestation route removed 2025-02-16 and restored 2026-02-21; CGI art. 286 is moved out of the CGI on
2027-01-01 (ordonnance n° 2025-1247), to be read then.

## Enforced by

- [F10 Point of sale (plugin)](../../../02-functional/f10-point-of-sale/README.md)
- [Regulatory](../../../02-functional/f10-point-of-sale/regulatory.md)
- [Q2 NF525 certification](../../../07-questions/q02-nf525-certification.md)

## When the law changes

Watched in the law corpus: CGI art. 286; BOI-TVA-DECLA-30-10-30; ordonnance n° 2025-1247. A change flags this rule and
warns the administrators; the corrected rule ships in a pack update (D294).

## Penalty

7 500 EUR per system without proof, with 60 days to comply after the official report (CGI art. 1770 duodecies;
[BOI-CF-INF-20-10-20](https://bofip.impots.gouv.fr/doctrine/pgp/7234-PGP) §550 to §580). A false certificate or
attestation: 3 years' prison and 45 000 EUR (Code pénal art. 441-1).

## Exceptions

VAT franchise (CGI art. 293 B), agricultural flat-rate scheme, exempt-only businesses, businesses paid only through a
bank with direct data access (BOI §35); pure business-to-business billing with no till function.

## Open questions

Whether the 2026-09-01 certificate deadline of the 2025 transition still applies now that the attestation is back: not
found in the sources read.

---

⬅️ [CR-FR-023 SEPA payment formats](../payments/cr-fr-023-sepa-formats.md) · ⬆️ [Up](README.md) ·
➡️ [CR-FR-025 Data recorded for each sale](cr-fr-025-sale-data-recorded.md)
