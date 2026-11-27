🏠 [Specs](../../../README.md) › 🌍 [Country packs](../../README.md) › 🇫🇷 [France](../README.md) ›
🏘️ [Real estate](README.md) › ⚖️ CR-FR-261 Planning permit instruction delays

# ⚖️ CR-FR-261 Planning permit instruction delays

**Status:** 🔄 (Proposed) values to read in the official source

## Statement

(Proposed) A planning-permit request is acknowledged with the delay the law gives, which depends on the kind of permit;
a missing document must be asked for within a short time after filing, and the delay starts or restarts when the file is
complete; consultations may extend it; and when no decision is notified in the delay, the law gives silence an effect
that depends on the kind of permit, usually an approval, sometimes a refusal.

## Values

- (Proposed) Kinds of permit, delays and effects of silence, kept as data.
- (Proposed) Electronic filing for bodies of a size.
- (Proposed) SimpleERP enforces: silence after the legal delay counts as the law says.
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

- Law to read: planning permit instruction (not read yet).

## Effective dates

(Proposed) To read.

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

The law on planning permit instruction is not read yet; the values are to read before launch.
[Q17 Country-rule penalties and start dates still to read](../../../07-questions/q17-unread-penalties-and-dates.md).

---

⬅️ [CR-FR-260 Civil registry records](../company/cr-fr-260-civil-registry.md) · ⬆️ [Up](README.md) ·
➡️ [CR-FR-262 Deliberations and the legality check](../company/cr-fr-262-deliberations-legality-check.md)
