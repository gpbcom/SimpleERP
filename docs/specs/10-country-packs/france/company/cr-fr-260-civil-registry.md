🏠 [Specs](../../../README.md) › 🌍 [Country packs](../../README.md) › 🇫🇷 [France](../README.md) ›
🏢 [Company identity](README.md) › ⚖️ CR-FR-260 Civil registry records

# ⚖️ CR-FR-260 Civil registry records

**Status:** 🔄 (Proposed) values to read in the official source

## Statement

(Proposed) Civil-status acts of birth, marriage and death are written by the civil-status officer, signed and kept in a
register; an act is not changed after it is signed: a correction is made by a margin note or by a court's decision, and
full copies are limited to those entitled. Software used to keep the registry usually has to be certified. Personal data
of the registry are not erased on request.

## Values

- (Proposed) Kinds of acts, delays and entitlements, kept as data.
- (Proposed) Correction by margin note only.
- (Proposed) SimpleERP enforces: civil records are corrected only by a margin note.
- Read on [Service-public F1429](https://www.service-public.gouv.fr/particuliers/vosdroits/F1429) (verified 12 March
  2026) and [F1177](https://www.service-public.gouv.fr/particuliers/vosdroits/F1177) (verified 22 August 2025); the
  writing, signing and keeping of the registers and the delays for acts are not on these pages:
- Read: a later event is added as a margin note on a birth, marriage or death act, written by the civil-status service,
  which has 3 days to enter it once asked (divorce).
- Read: a material error (misspelling, wrong date) is corrected on request to the town hall (act made in France) or to
  the public prosecutor at Nantes (act made abroad), decided by the officer or the prosecutor, answer by post.
- Read: a substantial error (filiation, sex) is decided by a judge: tribunal of the domicile or place of the act, Paris
  for residents abroad, Nantes for acts made abroad.
- Read: request papers: free paper or cerfa 11531, copies of the acts under 3 months old, proof, ID; Code civil 99 to
  101, 76 and 79; Code de procedure civile 1046 to 1055; decree 2017-890 of 6 May 2017.

## Legal references

- Law to read: civil-status registers (not read yet).

## Effective dates

(Proposed) To read.

## Enforced by

- [BR-SC20-18 Civil records are corrected only by a margin note](../../../08-sectors/sc20-public-bodies/business-rules/br-sc20-18-civil-records-are-corrected-only-by-a-margin-note.md)
- [UC-SC20-18 Keep the civil registry](../../../08-sectors/sc20-public-bodies/use-cases/05-council-registry-permits-and-assets/uc-sc20-18-keep-the-civil-registry.md)

## When the law changes

Watched in the law corpus: Civil-status rules. A change flags this rule and warns the administrators; the corrected rule
ships in a pack update (D294).

## Penalty

Not read yet.

## Exceptions

None stated.

## Open questions

The law on civil-status registers is not read yet; the values are to read before launch.
[Q17 Country-rule penalties and start dates still to read](../../../07-questions/q17-unread-penalties-and-dates.md).

---

⬅️ [CR-FR-259 Builders' ten-year insurance certificate](../construction/cr-fr-259-builders-warranty-insurance.md) ·
⬆️ [Up](README.md) ·
➡️ [CR-FR-261 Planning permit instruction delays](../real-estate/cr-fr-261-planning-permit-delays.md)
