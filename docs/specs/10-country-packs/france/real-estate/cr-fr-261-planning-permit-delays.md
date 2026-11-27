🏠 [Specs](../../../README.md) › 🌍 [Country packs](../../README.md) › 🇫🇷 [France](../README.md) ›
🏘️ [Real estate](README.md) › ⚖️ CR-FR-261 Planning permit instruction delays

# ⚖️ CR-FR-261 Planning permit instruction delays

**Status:** ✅ specified

## Statement

A planning-permit request is acknowledged with the delay the law gives, which depends on the kind of permit;
a missing document must be asked for within a short time after filing, and the delay starts or restarts when the file is
complete; consultations may extend it; and when no decision is notified in the delay, the law gives silence an effect
that depends on the kind of permit, usually an approval, sometimes a refusal: silence is a tacit permit or a
non-opposition (R*424-1, since 2016-01-01), and an implied refusal in the cases of R*424-2 (since 2026-04-17),
R*424-2-1 (environmental assessment, since 2025-12-31) and R*424-3 (adverse opinion of the Architecte des Bâtiments de
France, since 2026-07-29) ([Code de l'urbanisme, art. R*424-1 to R*424-4](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006074075/LEGISCTA000006175976/), read 2026-11-27).

## Values

- Kinds of permit, delays and effects of silence, kept as data: 1 month for a prior declaration, 2 months for a house or
  demolition permit, 3 months for other building and development permits (R*423-23, since 2007-10-01); +1 month in a
  heritage site or near a historic monument (R*423-24), +2 months for some consultations (R*423-25), 5 months in the
  cases of R*423-26 to R*423-28 ([Code de l'urbanisme, art. R*423-17 to R423-37-3](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006074075/LEGISCTA000006158835/), read 2026-11-27); missing documents asked
  within 1 month, then 3 months to supply them (R*423-38, R*423-39) ([Code de l'urbanisme](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006074075/LEGISCTA000006175969/), read 2026-11-27).
- In communes of more than 3 500 inhabitants (L423-3), every legal person files its request or declaration
  electronically, for requests filed from 2025-01-01 ([décret n° 2024-1043 du 18 novembre 2024, art. 1 and
  3](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000050613371), read 2026-11-27); the size that counts is the
  commune's.
- SimpleERP enforces: silence after the legal delay counts as the law says.
- Read on [Service-public F1986](https://www.service-public.gouv.fr/particuliers/vosdroits/F1986) (verified 13 February
  2026; the last 4 678 characters of the page were not read); delays for other permit kinds are not read:
- Read: the acknowledgement (recepisse; electronic acknowledgement if filed online) gives the file number and the date
  from which work can start.
- Read: missing documents are asked within 1 month of filing; the applicant then has 3 months to supply them, otherwise
  the request is treated as rejected.
- Read: instruction delay once the file is complete: individual house 2 months, other projects 3 months; protected
  sector: house 3 months, other projects in principle 4 months.
- Read: silence at the end of the delay means accepted (tacit permit; non-opposition certificate on request); in some
  protected cases silence means refusal.
- Read: Code de l'urbanisme L421-1 to L421-9, L424-5, R*423-1 to R*423-2-1, R*424-1 to R*424-4; decree 2025-461 of 26
  May 2025.

## Legal references

- Code de l'urbanisme L423-3, L424-2, R*423-17 to R423-37-3, R*423-38 to R*423-41-1, R*424-1 to R*424-4, R423-2-1.

## Effective dates

R*423-23 since 2007-10-01, R*423-24 since 2026-04-17, R*423-25 since 2022-03-27 ([Code de l'urbanisme](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006074075/LEGISCTA000006158835/));
R423-2-1 for requests filed from 2025-01-01 ([décret n° 2024-1043](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000050613371), read 2026-11-27).

## Enforced by

- [BR-SC20-19 Silence after the legal delay counts as the law says](../../../08-sectors/sc20-public-bodies/business-rules/br-sc20-19-silence-after-the-legal-delay-counts-as-the-law-says.md)
- [UC-SC20-19 Instruct planning permits](../../../08-sectors/sc20-public-bodies/use-cases/05-council-registry-permits-and-assets/uc-sc20-19-instruct-planning-permits.md)

## When the law changes

Watched in the law corpus: Planning permit delays. A change flags this rule and warns the administrators; the corrected
rule ships in a pack update (D294).

## Penalty

Not read yet.

## Exceptions

None stated.

## Open questions

None, read on 2026-11-27.
[Q17 Country-rule penalties and start dates still to read](../../../07-questions/q17-unread-penalties-and-dates.md).

---

⬅️ [CR-FR-260 Civil registry records](../company/cr-fr-260-civil-registry.md) · ⬆️ [Up](README.md) ·
➡️ [CR-FR-262 Deliberations and the legality check](../company/cr-fr-262-deliberations-legality-check.md)
